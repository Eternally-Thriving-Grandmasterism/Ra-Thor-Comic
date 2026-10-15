# ISSUE01-COVER-V16 FINAL (Mock A, chosen by Sherif 2026-10-15 4:56 PM ET). Art untouched; everything below is extra type/graphic layers over
# ../art_v16_print_notext.png + ../title_layer_v16.png. Placeholder wording is flagged in the report.
import cv2, numpy as np, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, '/workspace/issue01/release'); import srgb
D = '/workspace/issue01/v16/'; R = D + 'rnd/'
FW, FH, BL, SAFE = 2063, 3150, 37, 112
A = cv2.imread(D + 'art_v16_print_notext.png').astype(np.float32)
TL = cv2.imread(D + 'title_layer_v16.png', -1).astype(np.float32); Ta = TL[..., 3:] / 255; Trgb = TL[..., :3]
CINZEL = '/usr/share/fonts/truetype/sand-box/google/Cinzel/Cinzel-VariableFont_wght.ttf'
GOLD = np.array([[8, 40, 75], [42, 100, 134], [113, 139, 157], [127, 192, 204], [148, 209, 241], [176, 221, 249]], np.float32)  # BGR ramp sampled from LIVING THUNDER
SILV = np.array([[52, 50, 47], [110, 106, 100], [170, 166, 160], [214, 211, 206], [240, 238, 235], [252, 251, 250]], np.float32)

def font(px, wght=700):
    f = ImageFont.truetype(CINZEL, px)
    try: f.set_variation_by_axes([wght])
    except Exception: pass
    return f

def text_mask(txt, px, wght=700, track=0.0):
    f = font(px, wght); ws = [f.getbbox(c)[2] - f.getbbox(c)[0] if c != ' ' else px * 0.32 for c in txt]
    W = int(sum(f.getlength(c) for c in txt) + track * px * len(txt) + px); H = int(px * 1.6)
    im = Image.new('L', (W * 4, H * 4), 0); d = ImageDraw.Draw(im); f4 = font(px * 4, wght); x = px * 2
    for c in txt:
        d.text((x, px * 0.6), c, font=f4, fill=255); x += f4.getlength(c) + track * px * 4
    m = np.asarray(im, np.float32) / 255; m = cv2.resize(m, (W, H), interpolation=cv2.INTER_AREA)
    ys, xs = np.where(m > 0.02); return m[ys.min() - 2:ys.max() + 3, xs.min() - 2:xs.max() + 3]

def metal(m, ramp, light=1.0):
    """bevelled metal fill: vertical ramp + emboss from the blurred mask gradient (top-left light) + crisp edge line"""
    h, w = m.shape; t = np.linspace(1.0, 0.25, h)[:, None] * np.ones((1, w))
    b = cv2.GaussianBlur(m, (0, 0), max(1.0, h / 40)); gy = np.gradient(b, axis=0); gx = np.gradient(b, axis=1)
    emb = np.clip(0.5 + (gy + gx) * h / 7 * light, 0, 1)                       # >0.5 lit edges, <0.5 shadowed edges
    v = np.clip(0.55 * t + 0.6 * (emb - 0.5) + 0.25, 0, 1)
    band = np.exp(-((np.linspace(0, 1, h) - 0.38) / 0.09) ** 2)[:, None]       # specular band across the cap height
    v = np.clip(v + 0.22 * band, 0, 1)
    idx = v * (len(ramp) - 1); i0 = np.floor(idx).astype(int).clip(0, len(ramp) - 2); f = (idx - i0)[..., None]
    return ramp[i0] * (1 - f) + ramp[i0 + 1] * f

class Layer:
    def __init__(s): s.rgb = np.zeros((FH, FW, 3), np.float32); s.a = np.zeros((FH, FW, 1), np.float32)
    def put(s, rgb, a, x, y):
        h, w = a.shape; a = a[..., None]
        s.rgb[y:y + h, x:x + w] = rgb * a + s.rgb[y:y + h, x:x + w] * (1 - a); s.a[y:y + h, x:x + w] = a + s.a[y:y + h, x:x + w] * (1 - a)
    def shadow(s, a, x, y, sig, op, dx=0, dy=4, grow=0):
        h, w = a.shape; P = int(sig * 3 + grow + 8); big = np.zeros((h + 2 * P, w + 2 * P), np.float32); big[P:P + h, P:P + w] = a
        if grow: big = cv2.dilate(big, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * grow + 1, 2 * grow + 1)))
        sh = np.clip(cv2.GaussianBlur(big, (0, 0), sig) * op, 0, 1); x0, y0 = x - P + dx, y - P + dy
        s.put(np.full(sh.shape + (3,), (6, 6, 8), np.float32), sh, x0, y0)

def comp(base, *layers):
    O = base.copy()
    for l in layers: O = O * (1 - l.a) + l.rgb * l.a
    return O

def text_block(lay, txt, px, ramp, cx=None, x=None, y=0, wght=700, track=0.08, sh=(5, .85, 3), anchor='c'):
    m = text_mask(txt, px, wght, track); h, w = m.shape
    if anchor == 'c': x = int(cx - w / 2)
    elif anchor == 'r': x = int(x - w)
    lay.shadow(m, x, y, sh[0], sh[1], dy=sh[2], grow=1); lay.put(metal(m, ramp), m, x, y); return x, y, w, h

# ---------- 1. title legibility veil (type layer only): soft dark smoke under the band, strongest under THOR/LIVING THUNDER ----------
def veil(op):
    g = (Ta[..., 0] > 0.5).astype(np.float32); g[:, 1690:] = 0                # letters only (coin already has its own dark body)
    v = cv2.GaussianBlur(cv2.dilate(g, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (31, 31))), (0, 0), 16)
    l = Layer(); l.put(np.full((FH, FW, 3), (8, 7, 9), np.float32), np.clip(v * op, 0, 1), 0, 0); return l
V = veil(0.62)
TITLE = Layer(); TITLE.rgb = Trgb; TITLE.a = Ta

# ---------- 2. TM mark (small, gold, after LIVING THUNDER's right rule, left of the coin) ----------
TM = Layer(); text_block(TM, 'TM', 20, GOLD, x=1660, y=352, wght=600, track=0.05, sh=(2, .9, 1), anchor='l')

# ---------- 3. publisher mark: Autonomicity Games logo glyph (no text), gold ----------
lg = cv2.imread('/workspace/issue01/mark/agi_logo_gold_large.png').astype(np.float32)
la = np.clip((lg.max(2) - 12) / 40, 0, 1)
def logo(lay, hpx, x, y):
    s = hpx / lg.shape[0]; w = round(lg.shape[1] * s)
    a = cv2.resize(la, (w, hpx), interpolation=cv2.INTER_AREA); c = cv2.resize(lg * la[..., None], (w, hpx), interpolation=cv2.INTER_AREA) / np.maximum(a, 1e-3)[..., None]
    c = np.clip(c * 1.12 + 6, 0, 255); lay.shadow(a, x, y, 5, .9, dy=3, grow=2); lay.put(c, a, x, y); return w

# ---------- 4. story title, bottom centre: THE GATE between silver hairline rules ----------
def story(lay, ybase=2948):
    x, y, w, h = text_block(lay, 'THE GATE', 80, GOLD, cx=FW // 2, y=ybase, wght=800, track=0.16, sh=(10, .95, 4))
    for side in (-1, 1):
        L = 150; xs = (x - 28 - L) if side < 0 else (x + w + 28); yy = y + h // 2
        m = np.zeros((9, L), np.float32); m[3:6] = np.linspace(0, 1, L)[None] if side < 0 else np.linspace(1, 0, L)[None]
        m[1:8, (L - 10 if side < 0 else 2):(L - 2 if side < 0 else 10)] = 1
        lay.shadow(m, xs, yy - 4, 3, .9, dy=2); lay.put(metal(np.ones_like(m), SILV), m, xs, yy - 4)
    return x, y, w, h

# =================== MOCK A: "minimal premium" (recommended) ===================
MA = Layer()
story(MA)
logo(MA, 118, SAFE + 6, FH - SAFE - 118 - 6)                                   # bottom-left publisher corner
OA = comp(A, V, TITLE, TM, MA)

# =================== FINAL OUTPUTS ===================
F = D + 'final/'; import os; os.makedirs(F + 'crops', exist_ok=True)
# combined type layer = veil + title + TM + Mock A graphics, one RGBA (straight alpha), 'over' composited
Lrgb = np.zeros((FH, FW, 3), np.float32); La = np.zeros((FH, FW, 1), np.float32)
for l in (V, TITLE, TM, MA):
    Lrgb = l.rgb * l.a + Lrgb * (1 - l.a); La = l.a + La * (1 - l.a)          # premultiplied accumulation
Ls = Lrgb / np.maximum(La, 1e-6)
cv2.imwrite(F + 'type_layer_final_v16_mockA.png', np.dstack([np.clip(Ls + .5, 0, 255), np.clip(La * 255 + .5, 0, 255)]).astype(np.uint8))
O8 = np.clip(OA + .5, 0, 255).astype(np.uint8)
chk = np.abs(np.clip(A * (1 - La) + Lrgb + .5, 0, 255).astype(np.uint8).astype(int) - O8).max(); print('art+type_layer == print (max diff %d)' % chk)
srgb.save(F + 'RaThor_Issue01_Cover_BIBLE_FINAL_6.625x10.25_bleed_300dpi.jpg', O8, dpi=300, quality=97)
G = O8.copy()
def rect(img, m, col, t=3): cv2.rectangle(img, (m, m), (FW - 1 - m, FH - 1 - m), col, t, cv2.LINE_AA)
rect(G, 1, (255, 0, 255)); rect(G, BL, (0, 0, 255)); rect(G, SAFE, (255, 255, 0))
cv2.putText(G, 'BLEED 0.125" (sheet edge 2063x3150)', (10, FH - 10), cv2.FONT_HERSHEY_SIMPLEX, .8, (255, 0, 255), 2, cv2.LINE_AA)
cv2.putText(G, 'TRIM 6.625x10.25"', (BL + 12, FH - BL - 12), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2, cv2.LINE_AA)
cv2.putText(G, 'SAFE 0.25" inside trim', (SAFE + 12, FH - SAFE - 14), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 2, cv2.LINE_AA)
srgb.save(F + 'print_final_guides.jpg', G, dpi=300, quality=92)
srgb.save(F + 'preview_620.jpg', cv2.resize(O8, (620, 947), interpolation=cv2.INTER_AREA), dpi=72, quality=92)
for nm, (xa, xb, ya, yb) in {'top': (0, FW, 0, 640), 'bottom': (0, FW, 2760, FH), 'coin': (1639, 1975, 90, 426), 'face': (760, 1480, 422, 1182)}.items():
    srgb.save(F + 'crops/%s_100.jpg' % nm, O8[ya:yb, xa:xb], dpi=300, quality=95)
G1 = O8.copy(); rect(G1, BL, (0, 0, 255), 1); rect(G1, SAFE, (255, 255, 0), 1)       # hammer glint vs trim/safe (accepted: 71 px inside trim)
srgb.save(F + 'crops/hammer_top_trim_100.jpg', G1[0:560, 320:1120], dpi=300, quality=95)
# safe-area check of every added element (type layer alpha > 0.5)
yy, xx = np.where(La[..., 0] > 0.5); print('type layer (a>0.5) bbox x %d..%d y %d..%d | inside safe: %s' % (xx.min(), xx.max(), yy.min(), yy.max(),
      xx.min() >= SAFE and yy.min() >= SAFE and xx.max() <= FW - 1 - SAFE and yy.max() <= FH - 1 - SAFE))
print('final ok')
