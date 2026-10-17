# Inked comic lettering: flat gold with cel-shaded bevel, thick black keyline, hard offset extrusion shadow + halftone.
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
GF = '/usr/share/fonts/truetype/sand-box/google/'
FONTS = {'anton': GF + 'Anton/Anton-Regular.ttf', 'bebas': GF + 'Bebas Neue/BebasNeue-Regular.ttf',
         'cinzel': GF + 'Cinzel/Cinzel-VariableFont_wght.ttf', 'bigsh': GF + 'Big Shoulders/BigShoulders-VariableFont_opsz,wght.ttf'}
INK = np.array((10, 8, 6), np.float32)
# RGB cel ramps: deep, shadow, base, light, highlight
GOLD = np.array([(92, 52, 12), (168, 108, 26), (228, 166, 48), (255, 214, 104), (255, 246, 200)], np.float32)
ROSE = np.array([(96, 40, 30), (170, 84, 64), (222, 132, 106), (248, 184, 156), (255, 232, 214)], np.float32)
EMER = np.array([(4, 46, 26), (10, 92, 52), (22, 140, 80), (70, 196, 128), (190, 250, 212)], np.float32)
BRONZE = np.array((58, 30, 10), np.float32)

def font(name, px, wght=None):
    f = ImageFont.truetype(FONTS[name], int(px))
    if wght is not None:
        try:
            ax = f.get_variation_axes()
            f.set_variation_by_axes([wght] if len(ax) == 1 else [ax[0]['default'], wght][:len(ax)] if ax[0].get('name', b'') not in (b'Weight', 'Weight') else [wght] + [a['default'] for a in ax[1:]])
        except Exception: pass
    return f

def k(r): r = max(1, int(round(r))); return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1))

def bolt_poly(h, x0=0, y0=0, slant=0.0):
    w = 0.60 * h
    P = [(0.64 * w, 0), (0.02 * w, 0.60 * h), (0.40 * w, 0.60 * h), (0.18 * w, h), (0.98 * w, 0.34 * h), (0.58 * w, 0.34 * h), (0.84 * w, 0)]
    return [(x0 + x - slant * y, y0 + y) for x, y in P], w

def text_mask(parts, fnt, track=0, pad=60, shear=0.0, bolt_scale=1.25, gap=0.06):
    """parts: list of strings, '⚡' = rose bolt. returns (letters mask, bolt mask) float 0..1 on same canvas (supersampled px)."""
    asc, desc = fnt.getmetrics(); bb = fnt.getbbox('H'); capT, capB = bb[1], bb[3]; capH = capB - capT
    widths = []
    for p in parts:
        if p == '⚡': widths.append(bolt_poly(capH * bolt_scale)[1] + 2 * gap * capH)
        else: widths.append(sum(fnt.getlength(c) for c in p) + track * (len(p) - 1))
    W = int(sum(widths) + 2 * pad + capH * 0.6); H = int(capH * bolt_scale + 2 * pad + capH * 0.2)
    T = Image.new('L', (W, H)); B = Image.new('L', (W, H)); dT, dB = ImageDraw.Draw(T), ImageDraw.Draw(B)
    x = pad; base = pad + capH * (bolt_scale - 1) / 2 + capH                    # baseline y
    for p, w in zip(parts, widths):
        if p == '⚡':
            bh = capH * bolt_scale; P, bw = bolt_poly(bh, x + gap * capH, base - capH - (bh - capH) / 2); dB.polygon(P, fill=255)
        else:
            for c in p: dT.text((x, base - capB), c, font=fnt, fill=255); x += fnt.getlength(c) + track
            x -= track; continue
        x += w
    t = np.asarray(T, np.float32) / 255; b = np.asarray(B, np.float32) / 255
    if shear:
        M = np.float32([[1, -shear, shear * H * 0.5], [0, 1, 0]]); t = cv2.warpAffine(t, M, (W, H)); b = cv2.warpAffine(b, M, (W, H))
    return t, b, capH

def cel_fill(m, ramp, bevel, light=(-0.75, -0.66), band=True, spec=True):
    """flat cel-shaded fill: 2-tone face split (upper lighter) + bevel ring lit/shadow by edge normal vs light dir + thin spec line."""
    mb = (m > 0.5).astype(np.uint8)
    d = cv2.distanceTransform(mb, cv2.DIST_L2, 5)
    sm = cv2.GaussianBlur(m, (0, 0), bevel * 0.8); gy, gx = np.gradient(sm)
    n = np.sqrt(gx ** 2 + gy ** 2) + 1e-6; facing = -(gx * light[0] + gy * light[1]) / n   # >0 edge faces the light
    H, W = m.shape; out = np.empty((H, W, 3), np.float32)
    # face: base, with a lighter upper zone (classic logo split), per-row
    ys, xs = np.where(mb);
    if len(ys) == 0: out[:] = ramp[2]; return out
    y0, y1 = ys.min(), ys.max(); yy = (np.arange(H)[:, None] - y0) / max(1, y1 - y0)
    face = np.where(yy < 0.47 + 0.0 * xs.mean(), 1, 0)
    out[:] = ramp[2]; out[np.broadcast_to(face, (H, W)) == 1] = ramp[3]
    if band:   # thin darker band just below the split for a crisp cel break
        bandm = (yy >= 0.47) & (yy < 0.53); out[np.broadcast_to(bandm, (H, W))] = ramp[1] * 0.5 + ramp[2] * 0.5
    ring = d < bevel
    out[ring & (facing > 0.25)] = ramp[4] if spec else ramp[3]
    out[ring & (facing <= 0.25) & (facing > -0.25)] = ramp[2]
    out[ring & (facing <= -0.25)] = ramp[1]
    out[ring & (facing <= -0.7)] = ramp[0]
    # inner ink line separating bevel from face (thin)
    il = (np.abs(d - bevel) < max(1.0, bevel * 0.12))
    out[il] = out[il] * 0.55 + ramp[0] * 0.45
    return out

def halftone(shape, pitch, angle=45, rmax=0.5):
    H, W = shape; yy, xx = np.mgrid[0:H, 0:W].astype(np.float32); a = np.deg2rad(angle)
    u = (xx * np.cos(a) + yy * np.sin(a)) / pitch; v = (-xx * np.sin(a) + yy * np.cos(a)) / pitch
    du = u - np.round(u); dv = v - np.round(v); return np.sqrt(du ** 2 + dv ** 2)          # distance to dot centre, in pitch units

class Comp:
    """RGBA accumulator (supersampled)."""
    def __init__(s, H, W): s.rgb = np.zeros((H, W, 3), np.float32); s.a = np.zeros((H, W), np.float32)
    def put(s, m, col):
        col = np.broadcast_to(np.asarray(col, np.float32), s.rgb.shape) if np.asarray(col).ndim == 1 else col
        s.rgb = s.rgb * (1 - m[..., None]) + col * m[..., None]; s.a = m + s.a * (1 - m)
    def down(s, f):
        H, W = s.a.shape; sz = (W // f, H // f)
        a = cv2.resize(s.a, sz, interpolation=cv2.INTER_AREA); pm = cv2.resize(s.rgb * s.a[..., None], sz, interpolation=cv2.INTER_AREA)
        return pm / np.maximum(a, 1e-5)[..., None], a

def inked(masks, key, ext=(0.07, 0.10), ext_col=BRONZE, ht=True, outer=None):
    """masks: list of (mask, ramp, bevel) layers sharing one canvas. key = keyline radius (ss px).
    ext = (dx,dy) extrusion as fraction of cap height handled by caller via px: here absolute px tuple."""
    H, W = masks[0][0].shape; C = Comp(H, W)
    union = np.clip(sum(m for m, _, _ in masks), 0, 1)
    kl = cv2.dilate(union, k(key))
    dx, dy = ext
    # hard extrusion: sweep keyline silhouette along (dx,dy)
    steps = int(max(abs(dx), abs(dy)))
    ex = np.zeros_like(kl)
    for i in range(1, steps + 1):
        M = np.float32([[1, 0, dx * i / steps], [0, 1, dy * i / steps]]); ex = np.maximum(ex, cv2.warpAffine(kl, M, (W, H)))
    if ht:   # halftone drop shadow further out
        M = np.float32([[1, 0, dx * 1.9], [0, 1, dy * 1.9]]); sh = cv2.warpAffine(cv2.dilate(kl, k(key * 0.6)), M, (W, H))
        dist = halftone((H, W), max(6, key * 1.1)); dots = (dist < 0.36).astype(np.float32)
        C.put(np.clip(sh - ex, 0, 1) * dots * 0.85, INK)
    exo = cv2.dilate(ex, k(key * 0.55)); C.put(exo, INK)
    if outer is not None:   # optional thin coloured outer line then black again
        o1 = cv2.dilate(union, k(key * 1.6)); o2 = cv2.dilate(union, k(key * 2.2)); C.put(o2, INK); C.put(o1, outer)
    # extrusion body: dark bronze with ink edge
    body = ex * (1 - cv2.erode(ex, k(key * 0.45)) * 0) ; C.put(cv2.erode(ex, k(key * 0.5)), ext_col)
    C.put(kl, INK)
    for m, ramp, bev in masks: C.put(m, cel_fill(m, ramp, bev))
    return C
