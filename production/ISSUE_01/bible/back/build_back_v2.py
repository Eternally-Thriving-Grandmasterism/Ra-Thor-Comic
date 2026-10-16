# ISSUE01-BACK-COVER-V2 (Sherif OK of the V1 layout 2026-10-15 9:31 PM ET, 3D-crest variant; blurb copy = Sherif's option C, 9:32 PM ET).
# Back cover at the front's exact print spec: 2063 x 3150 px, 300 dpi, sRGB (6.625 x 10.25 in trim + 0.125 in bleed; safe 75 px inside trim).
# Layers: (1) back_art_v2.png  = art only: a toned-down obsidian/antique-gold echo of the V18 front art (no text painted in)
#         (2) back_type_layer_v2.png = every word, rule and logo, one straight-alpha RGBA, 'over'-composited on (1)
# Print = art * (1 - a) + type * a (checked below).  KDP barcode zone (2.0 x 1.2 in, lower right inside safe) is kept empty.
import cv2, numpy as np, sys, os
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, '/workspace/issue01/release'); import srgb
D = '/workspace/issue01/back/'; V18 = '/workspace/issue01/v18/'
VAR = sys.argv[1] if len(sys.argv) > 1 else '3d'                      # '3d' = embossed website crest (owner, 9:24 PM); 'flat' = flat gold fallback
TAG = 'v2' if VAR == '3d' else 'v2_flatAGI'
# ============ EDITABLE COPY (swap the blurb here; layout re-flows, auto-wrapped, centred) ============
HEADLINE = ['LEFT IS NOISE.', 'RIGHT CAN LIVE.']                    # E01 Panel 1 bubble, verbatim
# Sherif, 2026-10-15 9:32 PM ET (option C): line 1 'Ra-Thor stands watch where the sun meets the storm.' set in silver small caps
# (two lines so it fits the measure); lines 2-3 in the body serif.
BLURB_KICKER = ['RA-THOR STANDS WATCH', 'WHERE THE SUN MEETS THE STORM.']   # silver Cinzel caps; [] to drop
BLURB_BODY = [                                                         # EB Garamond paragraphs; each auto-wraps at BODY_MAXW
    'All that comes to the Gate is weighed.',
    'What is noise falls away. What can live is let through.',
]
BLURB_CLOSER = 'What gets blocked is recycled, not wasted.'            # italic closing line (Sherif: keep exactly)
BODY_PX, BODY_LEAD, BODY_MAXW = 58, 82, 1500
BLURB_MAX_Y = 2440                                                     # blurb must end above the bottom block (hairline y 2520)
# =====================================================================================================
FW, FH, BL, SAFE = 2063, 3150, 37, 112
BCW, BCH = 600, 360                                                   # KDP barcode box 2.0 x 1.2 in at 300 dpi
BX1, BY1 = FW - SAFE, FH - SAFE; BX0, BY0 = BX1 - BCW, BY1 - BCH       # x 1351..1951, y 2678..3038
GF = '/usr/share/fonts/truetype/sand-box/google/'
CINZEL = GF + 'Cinzel/Cinzel-VariableFont_wght.ttf'
GARA = GF + 'EB Garamond/EBGaramond-VariableFont_wght.ttf'
GARA_I = GF + 'EB Garamond/EBGaramond-Italic-VariableFont_wght.ttf'
MONT = GF + 'Montserrat/Montserrat-VariableFont_wght.ttf'
GOLD = np.array([[8, 40, 75], [42, 100, 134], [113, 139, 157], [127, 192, 204], [148, 209, 241], [176, 221, 249]], np.float32)  # BGR ramp = front LIVING THUNDER
SILV = np.array([[52, 50, 47], [110, 106, 100], [170, 166, 160], [214, 211, 206], [240, 238, 235], [252, 251, 250]], np.float32)
ROSE = (92, 128, 214)                                                 # rose-gold/copper (BGR) for the inline bolt
BODY = (198, 222, 238)                                                # warm parchment (BGR) for the blurb
FINE = (150, 170, 186)                                                # muted warm grey-gold (BGR) for the fine print
WHITE = (238, 240, 242)

def font(path, px, wght=None):
    f = ImageFont.truetype(path, px)
    if wght is not None:
        try: f.set_variation_by_axes([wght] if 'Inter' not in path else [14, wght])
        except Exception: pass
    return f

# ---------------- art layer: toned-down echo of the V18 front art ----------------
def build_art():
    A = cv2.imread(V18 + 'art_v18_print_notext.png').astype(np.float32) / 255
    L = cv2.cvtColor(A, cv2.COLOR_BGR2GRAY)
    L = cv2.GaussianBlur(L, (0, 0), 2.2)                              # soften: an echo, not a second cover
    # duotone obsidian -> antique gold, compressed hard (max ~30% of the front's brightness)
    t = np.clip(L, 0, 1) ** 1.35
    obs = np.array([10, 9, 11], np.float32) / 255; gold = np.array([60, 128, 182], np.float32) / 255
    E = obs + (gold - obs) * (t[..., None] * 0.55)
    # vignette + quiet zones where the type sits (centre blurb band, bottom block) so text never fights the art
    yy, xx = np.mgrid[0:FH, 0:FW].astype(np.float32)
    vig = 1 - 0.55 * np.clip(((xx - FW / 2) / (FW * 0.62)) ** 2 + ((yy - FH * 0.42) / (FH * 0.62)) ** 2, 0, 1)
    band = 1 - 0.50 * np.exp(-((yy - 1770) / 520) ** 2)               # blurb band
    bot = 1 - 0.60 * np.clip((yy - 2350) / 300, 0, 1)                 # bottom: fine print + logos + barcode
    E = E * (vig * band * bot)[..., None]
    # fine film grain in warm tone (the front's velvet-matte finish), deterministic
    rng = np.random.default_rng(18); g = cv2.GaussianBlur(rng.standard_normal((FH, FW)).astype(np.float32), (0, 0), 0.8)
    E = E + g[..., None] * np.array([0.004, 0.006, 0.008], np.float32)
    return np.clip(E * 255, 0, 255)

# ---------------- type helpers ----------------
class Layer:
    def __init__(s): s.rgb = np.zeros((FH, FW, 3), np.float32); s.a = np.zeros((FH, FW, 1), np.float32)
    def put(s, rgb, a, x, y):
        h, w = a.shape; a = a[..., None]
        if not isinstance(rgb, np.ndarray) or rgb.ndim == 1: rgb = np.broadcast_to(np.array(rgb, np.float32), (h, w, 3))
        s.rgb[y:y + h, x:x + w] = rgb * a + s.rgb[y:y + h, x:x + w] * (1 - a); s.a[y:y + h, x:x + w] = a + s.a[y:y + h, x:x + w] * (1 - a)
    def shadow(s, a, x, y, sig, op, dx=0, dy=4, grow=0):
        h, w = a.shape; P = int(sig * 3 + grow + 8); big = np.zeros((h + 2 * P, w + 2 * P), np.float32); big[P:P + h, P:P + w] = a
        if grow: big = cv2.dilate(big, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * grow + 1, 2 * grow + 1)))
        sh = np.clip(cv2.GaussianBlur(big, (0, 0), sig) * op, 0, 1); s.put((6, 6, 8), sh, x - P + dx, y - P + dy)

def metal(m, ramp, light=1.0):
    h, w = m.shape; t = np.linspace(1.0, 0.25, h)[:, None] * np.ones((1, w))
    b = cv2.GaussianBlur(m, (0, 0), max(1.0, h / 40)); gy = np.gradient(b, axis=0); gx = np.gradient(b, axis=1)
    emb = np.clip(0.5 + (gy + gx) * h / 7 * light, 0, 1)
    v = np.clip(0.55 * t + 0.6 * (emb - 0.5) + 0.25, 0, 1)
    band = np.exp(-((np.linspace(0, 1, h) - 0.38) / 0.09) ** 2)[:, None]; v = np.clip(v + 0.22 * band, 0, 1)
    idx = v * (len(ramp) - 1); i0 = np.floor(idx).astype(int).clip(0, len(ramp) - 2); f = (idx - i0)[..., None]
    return ramp[i0] * (1 - f) + ramp[i0 + 1] * f

def bolt_poly(h):
    """the Ra-Thor app-icon style Z bolt as a small vector glyph, cap-height h (used where a font cannot render the ⚡)"""
    w = 0.62 * h
    return [(0.62 * w, 0), (0.05 * w, 0.58 * h), (0.42 * w, 0.58 * h), (0.25 * w, h), (0.95 * w, 0.36 * h), (0.56 * w, 0.36 * h), (0.80 * w, 0)], w

def runs_mask(runs, f, px, track=0.0, SS=3):
    """render a line of text runs at SSx then area-downsample. runs: list of str; '⚡' -> vector bolt, '™' -> raised small TM.
    returns (text mask, bolt mask) of identical shape, baseline-aligned, tight-cropped horizontally."""
    fS = ImageFont.truetype(f.path, px * SS)
    try: fS.set_variation_by_axes(f.get_variation_axes() and [a.get('default') for a in f.get_variation_axes()])
    except Exception: pass
    if hasattr(f, '_wght'):
        try: fS.set_variation_by_axes(f._wght)
        except Exception: pass
    asc, desc = fS.getmetrics(); H = asc + desc + 4 * SS
    total = 0; items = []
    for r in runs:
        if r == '⚡':
            poly, bw = bolt_poly(px * SS * 0.80); items.append(('b', poly, bw)); total += bw + 0.10 * px * SS
        elif r == '™':
            fT = ImageFont.truetype(f.path, int(px * SS * 0.50)); w = fT.getlength('TM'); items.append(('tm', fT, w)); total += w + 0.04 * px * SS
        else:
            w = (sum(fS.getlength(c) for c in r) if track else fS.getlength(r)) + track * px * SS * len(r); items.append(('t', r, w)); total += w   # per-char sum when tracked (kerned length is shorter)
    W = int(total + 4 * SS + px * SS)                                 # + 1 em spare so no glyph overhang is ever clipped
    T = Image.new('L', (W, H), 0); Bm = Image.new('L', (W, H), 0); dT = ImageDraw.Draw(T); dB = ImageDraw.Draw(Bm)
    x = 2 * SS; capH = fS.getbbox('H')[3] - fS.getbbox('H')[1]; capTop = asc - capH + 2 * SS
    for k, a, w in items:
        if k == 'b':
            bh = px * SS * 0.80; y0 = capTop + capH - bh + 0.04 * bh
            dB.polygon([(x + 0.05 * px * SS + p[0], y0 + p[1]) for p in a], fill=255); x += w + 0.10 * px * SS
        elif k == 'tm':
            dT.text((x, capTop - 0.02 * px * SS), 'TM', font=a, fill=255); x += w + 0.04 * px * SS
        elif track:
            for c in a: dT.text((x, 2 * SS), c, font=fS, fill=255); x += fS.getlength(c) + track * px * SS
        else:
            dT.text((x, 2 * SS), a, font=fS, fill=255); x += w
    t = cv2.resize(np.asarray(T, np.float32) / 255, (W // SS, H // SS), interpolation=cv2.INTER_AREA)
    b = cv2.resize(np.asarray(Bm, np.float32) / 255, (W // SS, H // SS), interpolation=cv2.INTER_AREA)
    xs = np.where((t + b).max(0) > 0.02)[0]; return t[:, xs.min():xs.max() + 1], b[:, xs.min():xs.max() + 1]

def F(path, px, wght):
    f = ImageFont.truetype(path, px); f._wght = [wght]
    try: f.set_variation_by_axes([wght])
    except Exception: pass
    return f

def split_runs(s):
    out, cur = [], ''
    for c in s:
        if c in '⚡™':
            if cur: out.append(cur)
            out.append(c); cur = ''
        else: cur += c
    if cur: out.append(cur)
    return out

def put_line(lay, text, f, px, color, x=None, cx=None, y=0, anchor='l', track=0.0, sh=(3, .85, 2), bolt=ROSE, metal_ramp=None):
    t, b = runs_mask(split_runs(text), f, px, track); h, w = t.shape
    if anchor == 'c': x = int(round(cx - w / 2))
    elif anchor == 'r': x = int(round(x - w))
    m = np.maximum(t, b)
    if sh: lay.shadow(m, x, y, sh[0], sh[1], dy=sh[2], grow=1)
    if metal_ramp is not None: lay.put(metal(t, metal_ramp), t, x, y)
    else: lay.put(color, t, x, y)
    if b.max() > 0: lay.put(bolt, b, x, y)
    return x, y, w, h

def wrap(text, f, px, maxw):
    fS = ImageFont.truetype(f.path, px)
    try: fS.set_variation_by_axes(f._wght)
    except Exception: pass
    words, lines, cur = text.split(' '), [], ''
    for wd in words:
        t = (cur + ' ' + wd).strip()
        if fS.getlength(t.replace('⚡', 'MM').replace('™', 'TM')) <= maxw: cur = t
        else: lines.append(cur); cur = wd
    lines.append(cur); return lines

def hairline(lay, x0, x1, y, ramp=GOLD, fade=True, th=4):
    L = x1 - x0; m = np.zeros((th + 4, L), np.float32)
    prof = np.minimum(np.linspace(0, 1, L) * 4, 1) * np.minimum(np.linspace(1, 0, L) * 4, 1) if fade else np.ones(L)
    m[2:2 + th] = prof[None]; lay.shadow(m, x0, y, 2, .8, dy=2); lay.put(metal(np.ones_like(m), ramp), m, x0, y)

# ---------------- logos ----------------
def agi_logo_rgba():
    if VAR == '3d':   # embossed metallic-gold crest from https://acitygames.com/images/logo-dark-1024.webp (1024x1169 RGBA, already transparent)
        L = cv2.imread(D + 'agi_logo_3d_transparent.png', -1).astype(np.float32); a = L[..., 3] / 255
        return L[..., :3] * a[..., None], a
    """flat fallback: Autonomicity Games Inc. glyph in title gold (shape untouched; same source + alpha rule as the front's publisher-mark code)"""
    lg = cv2.imread('/workspace/issue01/mark/agi_logo_gold_large.png').astype(np.float32)
    la = np.clip((lg.max(2) - 12) / 40, 0, 1); c = lg * la[..., None]
    return c, la                                                       # premultiplied colour, alpha

def apm_logo_rgba():
    L = cv2.imread(D + 'apm_logo_transparent.png', -1).astype(np.float32)
    a = L[..., 3] / 255; return L[..., :3] * a[..., None], a

def place_logo(lay, pm, a, hpx, x, y, sh=True):
    s = hpx / a.shape[0]; w = round(a.shape[1] * s)
    A2 = cv2.resize(a, (w, hpx), interpolation=cv2.INTER_AREA); C2 = cv2.resize(pm, (w, hpx), interpolation=cv2.INTER_AREA)
    C2 = np.clip(C2 / np.maximum(A2, 1e-4)[..., None], 0, 255)
    if sh: lay.shadow(np.clip(A2 * 1.2, 0, 1), x, y, 4, .7, dy=2, grow=1)
    lay.put(C2, A2, x, y); return w

# =========================================================================================
if __name__ == '__main__':
    ART = build_art(); cv2.imwrite(D + 'back_art_v2.png', np.clip(ART + .5, 0, 255).astype(np.uint8))
    T = Layer(); CX = FW // 2

    # 1. series logo (the front's title band + ISSUE #1 coin, same pixels, unscaled) + TM, centred at the top
    TL = cv2.imread(V18 + 'title_layer_v18.png', -1).astype(np.float32)
    tx0, tx1, ty0, ty1 = 1100, 1962, 100, 380
    ta = TL[ty0:ty1, tx0:tx1, 3] / 255; tc = TL[ty0:ty1, tx0:tx1, :3]
    TX = CX - (tx1 - tx0) // 2; TY = 210
    T.shadow(ta, TX, TY, 10, .9, dy=5, grow=2); T.put(tc, ta, TX, TY)
    fTM = F(CINZEL, 20, 600)
    put_line(T, 'TM', fTM, 20, None, x=TX + (1660 - tx0), y=TY + (352 - 116) + (116 - ty0) - 12, metal_ramp=GOLD, sh=(2, .9, 1))

    # 2. issue line under the logo:  #1 · THE GATE  between silver hairline rules
    fIss = F(CINZEL, 60, 700)
    x, y, w, h = put_line(T, '#1 · THE GATE', fIss, 60, None, cx=CX, y=TY + 330, anchor='c', track=0.14, metal_ramp=GOLD, sh=(6, .95, 3))
    for side in (-1, 1):
        Lr = 170; xs = (x - 36 - Lr) if side < 0 else (x + w + 36); yy = y + h // 2 - 4
        m = np.zeros((9, Lr), np.float32); m[3:6] = (np.linspace(0, 1, Lr) if side < 0 else np.linspace(1, 0, Lr))[None]
        m[1:8, (Lr - 10 if side < 0 else 2):(Lr - 2 if side < 0 else 10)] = 1
        T.shadow(m, xs, yy, 3, .9, dy=2); T.put(metal(np.ones_like(m), SILV), m, xs, yy)

    # 3. headline: E01 Panel 1 bubble, verbatim (Ra-Thor's own line)
    fH = F(CINZEL, 118, 700)
    hy = 1260
    for i, ln in enumerate(HEADLINE):
        put_line(T, ln, fH, 118, None, cx=CX, y=hy + 160 * i, anchor='c', track=0.06, metal_ramp=GOLD, sh=(12, .95, 5))

    # 4. blurb (see EDITABLE COPY at the top)
    by = 1690
    fK = F(CINZEL, 50, 600)
    for i, ln in enumerate(BLURB_KICKER):
        put_line(T, ln, fK, 50, None, cx=CX, y=by + 78 * i, anchor='c', track=0.12, metal_ramp=SILV, sh=(5, .95, 2))
    fB = F(GARA, BODY_PX, 450)
    yb = by + (78 * len(BLURB_KICKER) + 49 if BLURB_KICKER else 0)
    for para in BLURB_BODY:
        for ln in wrap(para, fB, BODY_PX, BODY_MAXW):
            put_line(T, ln, fB, BODY_PX, BODY, cx=CX, y=yb, anchor='c', sh=(5, .95, 2)); yb += BODY_LEAD
    fBI = F(GARA_I, BODY_PX, 450)
    _, cy_, _, ch_ = put_line(T, BLURB_CLOSER, fBI, BODY_PX, BODY, cx=CX, y=yb + 34, anchor='c', sh=(5, .95, 2))
    print('blurb ends at y %d (limit %d)' % (cy_ + ch_, BLURB_MAX_Y)); assert cy_ + ch_ <= BLURB_MAX_Y, 'blurb too long: shorten copy or lower BODY_PX'

    # 5. bottom block: hairline, two company logos side by side, fine print; barcode zone kept clear on the right
    LX0 = SAFE + 8; LX1 = BX0 - 60                                     # left column x 120..1291
    LOGO_TOP, LOGO_BOT = 2590, 2790                                    # logo row; fine print below it (left of the barcode zone)
    hairline(T, SAFE + 40, FW - SAFE - 40, LOGO_TOP - 70, fade=True, th=3)
    gp, ga = agi_logo_rgba()
    LOGO_H = LOGO_BOT - LOGO_TOP - 30                                  # AGI crest height
    # AGI lockup = crest + wordmark set in the APM logo's own scheme (white name, gold spaced descriptor)
    fA1 = F(MONT, 54, 500); fA2 = F(MONT, 36, 500)
    wg_est = round(ga.shape[1] * LOGO_H / ga.shape[0])
    t1, _ = runs_mask(['Autonomicity'], fA1, 54); t2, _ = runs_mask(['G A M E S'], fA2, 36)
    agi_w = wg_est + 28 + max(t1.shape[1], t2.shape[1])
    # APM: tight-crop its transparent margin, then size it to the same lockup width (balanced optical weight)
    pp, pa = apm_logo_rgba(); ys, xs = np.where(pa > 0.03); pp, pa = pp[ys.min():ys.max() + 1, xs.min():xs.max() + 1], pa[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    apm_w = round(agi_w * 0.86); apm_h = round(pa.shape[0] * apm_w / pa.shape[1])
    gap = (LX1 - LX0) - agi_w - apm_w
    cy = (LOGO_TOP + LOGO_BOT) // 2
    ly = cy - LOGO_H // 2
    wg = place_logo(T, gp, ga, LOGO_H, LX0, ly, sh=(VAR != '3d'))
    ax = LX0 + wg + 28; blk = t1.shape[0] + 6 + t2.shape[0]; ty = cy - blk // 2 - 4
    _, _, w1, h1 = put_line(T, 'Autonomicity', fA1, 54, WHITE, x=ax, y=ty, sh=(3, .8, 2))
    put_line(T, 'G A M E S', fA2, 36, None, x=ax + 2, y=ty + h1 + 6, metal_ramp=GOLD, sh=(3, .8, 2))
    px0 = LX1 - apm_w; py0 = round(cy - apm_h * 0.73)                 # rays sit above: align the wordmarks optically
    place_logo(T, pp, pa, apm_h, px0, py0, sh=False)
    print('logos: AGI crest %dx%d at (%d,%d), AGI lockup %d px wide; APM %dx%d at (%d,%d); gap %d' % (wg, LOGO_H, LX0, ly, agi_w, apm_w, apm_h, px0, py0, gap))
    if VAR == '3d': print('AGI 3D crest effective resolution at placed size: %.0f ppi (native %d px tall over %.2f in)' % (ga.shape[0] / (LOGO_H / 300), ga.shape[0], LOGO_H / 300))
    APM_PPI = pa.shape[0] / (apm_h / 300); print('APM effective resolution: %.0f ppi' % APM_PPI)

    FP = 30; fF = F(GARA, FP, 450); lh = 39
    fine = [
        'Ra-Thor⚡Living Thunder #1: The Gate. Published by AlphaProMega Media Inc.',
        'Copyright © 2026 AlphaProMega Media Inc. All rights reserved.',
        'Ra-Thor™ is a trademark of Autonomicity Games Inc. (application pending), used with permission.',   # Sherif 2026-10-15 9:37 PM ET
        'This is a work of fiction. Contact: info@Rathor.ai',
    ]
    lines = []
    for p in fine: lines += wrap(p, fF, FP, LX1 - LX0)
    fy = BY1 - len(lines) * lh - 6
    for ln in lines:
        put_line(T, ln, fF, FP, FINE, x=LX0, y=fy, sh=(2, .8, 1)); fy += lh
    print('fine print lines:'); [print('   ', l) for l in lines]

    # ---------------- composite + outputs ----------------
    O = ART * (1 - T.a) + T.rgb * T.a
    O8 = np.clip(O + .5, 0, 255).astype(np.uint8)
    cv2.imwrite(D + 'back_type_layer_%s.png' % TAG, np.dstack([np.clip(T.rgb + .5, 0, 255), np.clip(T.a * 255 + .5, 0, 255)]).astype(np.uint8))
    srgb.save(D + 'RaThor_Issue01_BackCover_%s_6.625x10.25_bleed_300dpi.jpg' % TAG, O8, dpi=300, quality=97)
    # checks
    yy, xx = np.where(T.a[..., 0] > 0.5)
    print('type (a>0.5) bbox x %d..%d y %d..%d | inside safe: %s' % (xx.min(), xx.max(), yy.min(), yy.max(),
          xx.min() >= SAFE and yy.min() >= SAFE and xx.max() <= FW - 1 - SAFE and yy.max() <= FH - 1 - SAFE))
    print('barcode zone type coverage (a>0.02 px):', int((T.a[BY0:BY1, BX0:BX1] > 0.02).sum()))
    # guides preview
    G = O8.copy()
    def rect(img, m, col, t=3): cv2.rectangle(img, (m, m), (FW - 1 - m, FH - 1 - m), col, t, cv2.LINE_AA)
    rect(G, 1, (255, 0, 255)); rect(G, BL, (0, 0, 255)); rect(G, SAFE, (255, 255, 0))
    for xd in range(BX0, BX1, 24):
        cv2.line(G, (xd, BY0), (min(xd + 12, BX1), BY0), (230, 230, 230), 2); cv2.line(G, (xd, BY1), (min(xd + 12, BX1), BY1), (230, 230, 230), 2)
    for yd in range(BY0, BY1, 24):
        cv2.line(G, (BX0, yd), (BX0, min(yd + 12, BY1)), (230, 230, 230), 2); cv2.line(G, (BX1, yd), (BX1, min(yd + 12, BY1)), (230, 230, 230), 2)
    cv2.putText(G, 'KDP BARCODE 2.0x1.2" (keep clear)', (BX0 + 18, BY0 + 40), cv2.FONT_HERSHEY_SIMPLEX, .8, (230, 230, 230), 2, cv2.LINE_AA)
    cv2.putText(G, 'BLEED 0.125" (sheet edge 2063x3150)', (10, FH - 10), cv2.FONT_HERSHEY_SIMPLEX, .8, (255, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(G, 'TRIM 6.625x10.25"', (BL + 12, BL + 34), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(G, 'SAFE 0.25" inside trim', (SAFE + 12, SAFE + 36), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 2, cv2.LINE_AA)
    srgb.save(D + 'RaThor_Issue01_BackCover_%s_guides.jpg' % TAG, G, dpi=300, quality=92)
    P = cv2.resize(O8, (620, 947), interpolation=cv2.INTER_AREA); srgb.save(D + 'back_preview_620_%s.jpg' % TAG, P, dpi=72, quality=92)
    Fp = cv2.resize(cv2.imread(V18 + 'RaThor_Issue01_Cover_BIBLE_FINAL_6.625x10.25_bleed_300dpi.jpg'), (620, 947), interpolation=cv2.INTER_AREA)
    srgb.save(D + 'front_back_620_%s.jpg' % TAG, np.hstack([Fp, np.full((947, 16, 3), 255, np.uint8), P]), dpi=72, quality=92)
    os.makedirs(D + 'crops', exist_ok=True)
    for nm, (xa, xb, ya, yb) in {'top_logo': (500, 1563, 150, 700), 'headline_blurb': (150, 1913, 1140, 2250), 'bottom_block': (0, FW, 2500, FH),
                                 'logos_200': (110, 1300, 2570, 2810)}.items():
        c = O8[ya:yb, xa:xb]
        if nm.endswith('_200'): c = cv2.resize(c, None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
        srgb.save(D + 'crops/%s_%s.jpg' % (nm, TAG), c, dpi=300, quality=95)
    print('ok')
