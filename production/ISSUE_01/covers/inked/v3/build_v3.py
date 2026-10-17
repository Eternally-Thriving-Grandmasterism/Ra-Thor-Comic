#!/usr/bin/env python3
"""Ra-Thor  Living Thunder  Issue #1  front + back covers, inked v3 (DRAFT for review).
usage: python3 build_v3.py [--art /path/to/base.jpg] [--variant B_cinzel] [--no-fixes] [--out DIR]
Base art defaults to Sherif's render3_storm.jpg. The art fixes (hammer end face, shield knotwork, canon halo, shield rim light,
pauldron emblems) are tied to that render's geometry (2016x3024 reference frame); pass --no-fixes for a fresh re-roll."""
import argparse, os, sys, hashlib, subprocess, shutil
import numpy as np, cv2
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'lib'))
import masthead as MH, fix_hammer, halo, shield, rim, pauldron
from letter import INK, GOLD as LGOLD

FW, FH, TRIM, SAFE = 2063, 3150, 37.5, 112
STORE = os.environ.get('RATHOR_BIBLE_DIR', os.path.normpath(os.path.join(HERE, '..', '..', '..', 'bible')))  # repo production/ISSUE_01/bible
TYPE_V2 = STORE + '/back/back_type_layer_v2.png'
UPSCALER = STORE + '/v18/upscale.py'; MODEL = os.environ.get('UPSCALE_MODEL', '4x-UltraSharp.pth')  # path to the 4x-UltraSharp model (not in repo)
ART_SCALE = 1.75                          # render px -> page px (1152 -> 2016 wide); figure + masthead room
ART_Y = 230                               # page y of the art's top edge (sky extended above it)
REF_W = 2016                              # fix coordinates are in this frame


def set_dpi(path, dpi=300):
    """Stamp 300 dpi into the JFIF APP0 header in place (no re-encode)."""
    b = bytearray(open(path, 'rb').read())
    assert b[2:4] == b'\xff\xe0' and b[6:11] == b'JFIF\x00'
    b[13] = 1; b[14:16] = dpi.to_bytes(2, 'big'); b[16:18] = dpi.to_bytes(2, 'big')
    open(path, 'wb').write(bytes(b))

def upscale(path, cache):
    h = hashlib.sha1(open(path, 'rb').read()).hexdigest()[:12]; out = os.path.join(cache, 'up4x_%s.png' % h)
    if not os.path.exists(out):
        print('AI upscale 4x (4x-UltraSharp, tiled, CPU) ...', flush=True)
        subprocess.check_call([sys.executable, UPSCALER, MODEL, path, out])
    return cv2.imread(out)

def art_page(U, src_w):
    W = round(src_w * ART_SCALE); H = round(U.shape[0] / U.shape[1] * W)
    return cv2.resize(U, (W, H), interpolation=cv2.INTER_AREA).astype(np.float32)

def ink_finish(A):
    """inked finish: crisp line edges (small-radius unsharp on luminance) + slightly deeper blacks."""
    L = A.mean(2); bl = cv2.GaussianBlur(L, (0, 0), 1.1); L = L[..., None]; bl = bl[..., None]
    A = A + 0.55 * (L - bl)
    v = A / 255; A = 255 * np.where(v < 0.25, v * (0.86 + 0.56 * v), v)
    return A.clip(0, 255)

def extend_page(A):
    """place art on the 2063x3150 page: sky extended upward by a mirrored, de-lightninged copy (no seam), sides reflected (bleed only)."""
    H, W = A.shape[:2]; x0 = (FW - W) // 2
    P = np.zeros((FH, FW, 3), np.float32)
    vis = A[:min(H, FH - ART_Y)]
    P[ART_Y:ART_Y + vis.shape[0], x0:x0 + W] = vis
    band = A[:ART_Y].copy()                                               # top rows of the art, mirrored upward about the top edge
    op = cv2.morphologyEx(band, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (31, 31)))   # strip thin lightning
    sm = cv2.GaussianBlur(op, (0, 0), 3)
    bright = np.clip((band.max(2, keepdims=True) - 60) / 60, 0, 1)
    band = band * (1 - bright) + sm * bright
    ext = band[::-1]                                                      # page row ART_Y-1-k = art row k
    yy = np.arange(ART_Y)[:, None, None]; fade = 0.80 + 0.20 * (yy / ART_Y)   # slightly darker toward the very top
    P[:ART_Y, x0:x0 + W] = ext * fade
    if x0 > 0:
        P[:, :x0] = P[:, x0:2 * x0][:, ::-1]; P[:, x0 + W:] = P[:, x0 + W - (FW - x0 - W):x0 + W][:, ::-1]
    return P

def halo_brightest(P, cx, cy, R):
    """soft-knee the highlights everywhere outside the halo so the halo stays the brightest value on the page."""
    yy, xx = np.mgrid[0:FH, 0:FW].astype(np.float32); w = np.clip((np.hypot(xx - cx, yy - cy) - R) / 60, 0, 1)[..., None]
    k = 214.0; comp = np.where(P > k, k + (P - k) * 0.55, P)
    return P * (1 - w) + comp * w

def over(P, rgb, a, x, y):
    h, w = a.shape; x0, y0 = max(0, x), max(0, y); x1, y1 = min(P.shape[1], x + w), min(P.shape[0], y + h)
    aa = a[y0 - y:y1 - y, x0 - x:x1 - x, None]; P[y0:y1, x0:x1] = P[y0:y1, x0:x1] * (1 - aa) + rgb[y0 - y:y1 - y, x0 - x:x1 - x] * aa
    return (x0, y0, x1, y1)

def ink_bbox(a, thr=0.5):
    ys, xs = np.where(a > thr); return xs.min(), ys.min(), xs.max(), ys.max()

def lettering_front(P, var, coin_d=318):
    rgb, a, info = MH.masthead(var); rgb = rgb[..., ::-1]                 # RGB -> BGR
    bx0, by0, bx1, by1 = ink_bbox(a, 0.02)
    maxw, maxh = FW - 2 * SAFE - coin_d - 18, 400
    s = min(1.0, maxw / (bx1 - bx0), maxh / (by1 - by0))
    if s < 1: rgb = cv2.resize(rgb, None, fx=s, fy=s, interpolation=cv2.INTER_AREA); a = cv2.resize(a, None, fx=s, fy=s, interpolation=cv2.INTER_AREA)
    bx0, by0, bx1, by1 = ink_bbox(a, 0.02)
    mx, my = SAFE + 6 - bx0, SAFE + 6 - by0
    box = over(P, rgb, a, mx, my)
    crgb, ca = MH.coin(coin_d); crgb = crgb[..., ::-1]
    cx0, cy0, cx1, cy1 = ink_bbox(ca, 0.02)
    wx1 = mx + bx1; cxp = FW - SAFE - 4 - cx1; cyp = max(SAFE + 4 - cy0, my + by0 + (by1 - by0) * 0.40 - (cy0 + cy1) / 2)
    cbox = over(P, crgb, ca, int(cxp), int(cyp))
    return dict(mast=(mx + bx0, my + by0, mx + bx1, my + by1), coin=(int(cxp) + cx0, int(cyp) + cy0, int(cxp) + cx1, int(cyp) + cy1),
                key_px=info['key_px'] * s, scale=s)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--art', default=os.path.normpath(os.path.join(HERE, '..', '..', '..', 'imagine', 'render3_storm.jpg')))
    ap.add_argument('--variant', default='B_cinzel'); ap.add_argument('--no-fixes', action='store_true')
    ap.add_argument('--out', default=HERE)
    o = ap.parse_args(); OUT = o.out; os.makedirs(OUT + '/crops', exist_ok=True); CACHE = OUT + '/work'; os.makedirs(CACHE, exist_ok=True)
    src = cv2.imread(o.art); U = upscale(o.art, CACHE)
    A0 = art_page(U, src.shape[1]); A = A0.copy(); sc = A.shape[1] / REF_W
    before = {}
    def snap(name, box): before[name] = box
    HCX, HCY = 1103 * sc, 862 * sc
    if not o.no_fixes:
        A, _ = fix_hammer.fix_hammer(A, 0, 0, sc); print('fix a: hammer striking end repainted plain')
        A = shield.apply(A, sc); print('fix b: shield border runes -> knotwork')
        A, hm = halo.apply(A, HCX, HCY); print('fix c: canon halo (3 rings, 8 spokes, no arrow)')
        A = rim.apply(A, sc); print('fix e: shield rim light')
        A, rb, lb = pauldron.apply(A, sc); print('fix i: pauldron emblems')
    A = ink_finish(A)
    cv2.imwrite(CACHE + '/art_fixed_page.png', A.clip(0, 255).astype(np.uint8))
    P = extend_page(A); P0 = extend_page(ink_finish(A0.copy()))
    x0 = (FW - A.shape[1]) // 2
    P = halo_brightest(P, HCX + x0, HCY + ART_Y, 540 * sc)
    art_only = P.copy()
    L = lettering_front(P, o.variant)
    print('masthead box', L['mast'], 'coin box', L['coin'], 'keyline px %.1f' % L['key_px'], flush=True)
    for nm, (bx0, by0, bx1, by1) in (('masthead', L['mast']), ('coin', L['coin'])):
        print(nm, bx0, by0, bx1, by1); assert bx0 >= SAFE and by0 >= SAFE and bx1 <= FW - SAFE and by1 <= FH - SAFE, nm + ' outside safe'
    F8 = P.clip(0, 255).astype(np.uint8)
    cv2.imwrite(OUT + '/front_inked_v3.jpg', F8, [cv2.IMWRITE_JPEG_QUALITY, 95]); set_dpi(OUT + '/front_inked_v3.jpg')

    # ---------------- masthead variants preview ----------------
    rows = []
    for v in MH.VARIANTS:
        Q = art_only.copy(); lettering_front(Q, v)
        r = cv2.resize(Q[:820].clip(0, 255).astype(np.uint8), (1000, 397), interpolation=cv2.INTER_AREA)
        cv2.rectangle(r, (0, 0), (300, 34), (0, 0, 0), -1); cv2.putText(r, v + (' (chosen)' if v == o.variant else ''), (8, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv2.LINE_AA)
        rows.append(r); rows.append(np.full((10, 1000, 3), 255, np.uint8))
    cv2.imwrite(OUT + '/masthead_variants_preview.jpg', np.vstack(rows[:-1]), [cv2.IMWRITE_JPEG_QUALITY, 92])

    # ---------------- back ----------------
    B = back_cover(A, x0, L['key_px'], o.variant)
    B8 = B.clip(0, 255).astype(np.uint8); cv2.imwrite(OUT + '/back_inked_v3.jpg', B8, [cv2.IMWRITE_JPEG_QUALITY, 95]); set_dpi(OUT + '/back_inked_v3.jpg')

    # ---------------- previews + crops ----------------
    pf = cv2.resize(F8, (406, 620), interpolation=cv2.INTER_AREA); pb = cv2.resize(B8, (406, 620), interpolation=cv2.INTER_AREA)
    cv2.imwrite(OUT + '/preview_front_back.jpg', np.hstack([pf, np.full((620, 16, 3), 255, np.uint8), pb]), [cv2.IMWRITE_JPEG_QUALITY, 92])
    mx0, my0, mx1, my1 = L['mast']; cx0, cy0, cx1, cy1 = L['coin']
    cv2.imwrite(OUT + '/crop_masthead_100.jpg', F8[max(0, my0 - 30):max(my1, cy1) + 40, max(0, mx0 - 30):min(FW, cx1 + 30)], [cv2.IMWRITE_JPEG_QUALITY, 95])
    cv2.imwrite(OUT + '/crops/coin_100.jpg', F8[cy0 - 20:cy1 + 20, cx0 - 20:cx1 + 20], [cv2.IMWRITE_JPEG_QUALITY, 95])
    if not o.no_fixes:
        def pair(nm, bx):   # before/after at 100% in page coordinates
            X0, Y0, X1, Y1 = [int(v) for v in bx]
            a = P0[Y0:Y1, X0:X1].clip(0, 255).astype(np.uint8); b = F8[Y0:Y1, X0:X1]
            cv2.imwrite(OUT + '/crops/%s_before_after_100.jpg' % nm, np.hstack([a, np.full((a.shape[0], 8, 3), 255, np.uint8), b]), [cv2.IMWRITE_JPEG_QUALITY, 95])
        def pg(x, y): return x * sc + x0, y * sc + ART_Y
        for nm, (ax0, ay0, ax1, ay1) in {'hammer_end': (230, 300, 560, 600), 'halo': (560, 330, 1650, 1080), 'shield_knotwork': (1300, 1480, 1940, 1960),
                                         'shield_bottom': (1460, 2300, 1760, 2620), 'shield_rim_right': (1700, 1650, 1960, 2400),
                                         'shoulder_viewer_left': (640, 1040, 960, 1250), 'shoulder_viewer_right': (1260, 1100, 1700, 1380),
                                         'chest_disc': (840, 1270, 1100, 1520), 'belt_buckle': (840, 1640, 1050, 1800), 'helm_wings': (700, 860, 1500, 1120)}.items():
            X0, Y0 = pg(ax0, ay0); X1, Y1 = pg(ax1, ay1); pair(nm, (X0, Y0, min(FW, X1), min(FH, Y1)))
    # (h) upscale linework check: Lanczos (from the 1152 px render) vs 4x-UltraSharp AI upscale, same page scale, 100%
    lz = cv2.resize(src, (A0.shape[1], A0.shape[0]), interpolation=cv2.INTER_LANCZOS4)
    for nm, (ax0, ay0, ax1, ay1) in {'helm_face': (900, 980, 1200, 1200), 'fist_handle': (180, 700, 480, 1000), 'chest_greek_key': (820, 1250, 1120, 1520),
                                     'boot_rocks': (300, 2650, 700, 2950), 'cape_edge': (0, 1500, 300, 1800), 'vegvisir_arm': (1380, 2050, 1680, 2350)}.items():
        a = lz[ay0:ay1, ax0:ax1]; b = A0[ay0:ay1, ax0:ax1].clip(0, 255).astype(np.uint8)
        cv2.imwrite(OUT + '/crops/upscale_check_%s_lanczos_vs_ai.jpg' % nm, np.hstack([a, np.full((a.shape[0], 8, 3), 255, np.uint8), b]), [cv2.IMWRITE_JPEG_QUALITY, 95])
    print('done')

def back_cover(A, x0, key_px, var):
    """dark background, ghosted final front figure (~0.35), v2 type layer as-is (except the old series mark, restyled), comic panel border."""
    G = np.zeros((FH, FW, 3), np.float32) + np.array([14, 10, 9], np.float32)
    fig = A.copy()
    g = fig.mean(2, keepdims=True); fig = fig * 0.75 + g * 0.25                     # slightly muted
    H, W = fig.shape[:2]; y0 = 300
    vis = fig[:min(H, FH - y0)]
    fade = np.clip(np.arange(vis.shape[0]) / 260.0, 0, 1)[:, None, None] ** 1.5       # figure's sky fades in: no hard top edge
    base = G[y0:y0 + vis.shape[0], x0:x0 + W]
    G[y0:y0 + vis.shape[0], x0:x0 + W] = base * (1 - fade) + vis * 0.35 * fade
    yy, xx = np.mgrid[0:FH, 0:FW].astype(np.float32)
    vig = 1 - 0.50 * np.clip(((xx - FW / 2) / (FW * 0.62)) ** 2 + ((yy - FH * 0.45) / (FH * 0.60)) ** 2, 0, 1)
    bot = 1 - 0.65 * np.clip((yy - 2380) / 260, 0, 1)
    G = G * (vig * bot)[..., None]
    # comic panel behind the headline + blurb: darker caption field, black keyline (same weight as the masthead keyline) + thin gold inner line
    px0, py0, px1, py1 = 250, 1190, FW - 250, 2272
    inside = (xx >= px0) & (xx <= px1) & (yy >= py0) & (yy <= py1)
    G[inside] = G[inside] * 0.42
    k = key_px
    def rect_line(img, x0_, y0_, x1_, y1_, t, col):
        cv2.rectangle(img, (int(round(x0_)), int(round(y0_))), (int(round(x1_)), int(round(y1_))), col, max(1, int(round(t))), cv2.LINE_AA)
    sh = np.zeros((FH, FW), np.float32); rect_line(sh, px0 - k / 2 + 10, py0 - k / 2 + 14, px1 + k / 2 + 10, py1 + k / 2 + 14, k, 1.0)
    G = G * (1 - 0.6 * sh[..., None])                                           # hard offset shadow of the border (comic style)
    rect_line(G, px0 - k / 2, py0 - k / 2, px1 + k / 2, py1 + k / 2, k, tuple(float(c) for c in INK))
    gi = 3.0; inset = k / 2 + 5 + gi / 2
    rect_line(G, px0 + inset, py0 + inset, px1 - inset, py1 - inset, gi, tuple(float(c) for c in LGOLD[2][::-1]))
    # v2 type layer, as-is; only the old series mark rows (y 200..505) are swapped for the comic lettering
    T = cv2.imread(TYPE_V2, -1).astype(np.float32); Ta = T[..., 3:] / 255; Trgb = T[..., :3]
    keep = np.ones((FH, FW, 1), np.float32); keep[200:506] = 0
    G = G * (1 - Ta * keep) + Trgb * Ta * keep
    rgb, a, info = MH.masthead(var); rgb = rgb[..., ::-1]
    crgb, ca = MH.coin(200); crgb = crgb[..., ::-1]
    bx0, by0, bx1, by1 = ink_bbox(a, 0.02); s = min(760 / (bx1 - bx0), 250 / (by1 - by0))
    rgb = cv2.resize(rgb, None, fx=s, fy=s, interpolation=cv2.INTER_AREA); a = cv2.resize(a, None, fx=s, fy=s, interpolation=cv2.INTER_AREA)
    bx0, by0, bx1, by1 = ink_bbox(a, 0.02); cx0, cy0, cx1, cy1 = ink_bbox(ca, 0.02)
    totw = (bx1 - bx0) + 24 + (cx1 - cx0); lx = (FW - totw) // 2; ty = 222 + (268 - (by1 - by0)) // 2
    over(G, rgb, a, lx - bx0, ty - by0)
    over(G, crgb, ca, lx + (bx1 - bx0) + 24 - cx0, int(ty + (by1 - by0) * 0.42 - (cy0 + cy1) / 2))
    return G

if __name__ == '__main__':
    main()
