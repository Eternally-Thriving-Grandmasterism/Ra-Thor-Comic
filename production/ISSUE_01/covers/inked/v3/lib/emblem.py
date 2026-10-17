# Vector winged Eye of Horus emblem, inked comic style (flat cel tones + black keylines), RGBA.
import numpy as np, cv2, os
from PIL import Image, ImageDraw
SS = 4
INK = (12, 10, 8)
GOLD = [(120, 78, 22), (196, 140, 46), (240, 196, 92), (255, 236, 160)]       # shadow, base, light, spec
EMER = [(6, 60, 34), (18, 128, 70), (60, 200, 120), (190, 255, 215)]

def _m(W, H): return Image.new('L', (W * SS, H * SS), 0)
def _np(im): return np.asarray(im, np.float32) / 255

class Canvas:
    def __init__(s, W, H):
        s.W, s.H = W, H; s.rgb = np.zeros((H * SS, W * SS, 3), np.float32); s.a = np.zeros((H * SS, W * SS), np.float32)
    def put(s, m, col):
        if isinstance(col, tuple): col = np.array(col, np.float32)[None, None]
        s.rgb = s.rgb * (1 - m[..., None]) + col * m[..., None]; s.a = np.maximum(s.a, m)
    def ink(s, m, w):
        k = int(w * SS) * 2 + 1
        d = cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k))); s.put(d, INK)
    def shape(s, m, ramp, w=4, light=(-1, -1), split=0.5):
        """inked flat shape with 3-tone cel shading: tone from the mask's distance-to-edge gradient vs light dir"""
        s.ink(m, w)
        b = cv2.GaussianBlur(m, (0, 0), 6 * SS)
        gy, gx = np.gradient(b); sh = (gx * light[0] + gy * light[1])
        sh = sh / (np.abs(sh).max() + 1e-6)
        col = np.empty(m.shape + (3,), np.float32); col[:] = ramp[1]
        col[sh > 0.08] = ramp[2]; col[sh < -0.10] = ramp[0]
        s.put(m, col)
    def out(s, glow=None):
        rgb = cv2.resize(s.rgb, (s.W, s.H), interpolation=cv2.INTER_AREA); a = cv2.resize(s.a, (s.W, s.H), interpolation=cv2.INTER_AREA)
        return rgb, a

def poly(W, H, pts):
    im = _m(W, H); ImageDraw.Draw(im).polygon([(x * SS, y * SS) for x, y in pts], fill=255); return _np(im)
def line(W, H, pts, w):
    im = _m(W, H); d = ImageDraw.Draw(im); P = [(x * SS, y * SS) for x, y in pts]
    d.line(P, fill=255, width=int(w * SS), joint='curve')
    for x, y in P[::max(1, len(P) - 1)]: r = w * SS / 2; d.ellipse([x - r, y - r, x + r, y + r], fill=255)
    return _np(im)
def ellipse(W, H, cx, cy, rx, ry):
    im = _m(W, H); ImageDraw.Draw(im).ellipse([(cx - rx) * SS, (cy - ry) * SS, (cx + rx) * SS, (cy + ry) * SS], fill=255); return _np(im)

def wing(W, H, x0, y0, L, side, nf=7, up=0.0):
    """Egyptian-style wing from root (x0,y0), length L, side=+1 to the right/-1 left. returns list of feather masks + covert band mask"""
    feathers = []
    for i in range(nf):
        t = i / (nf - 1)
        # feather lies along the bottom of the wing: rows stack downward, outer rows longer at top
        ln = L * (1.0 - 0.55 * t)
        top = y0 + t * L * 0.34
        th = L * 0.075
        lift = -L * (0.16 + up) * (1 - t * 0.6)                        # tips sweep upward
        pts = []
        N = 24
        for k in range(N + 1):
            u = k / N; x = x0 + side * u * ln; y = top + lift * u ** 2
            pts.append((x, y))
        tipx, tipy = pts[-1]
        bot = [(x0 + side * u * ln * 0.97, top + th + lift * u ** 2 * 0.97) for u in np.linspace(1, 0, N + 1)]
        # rounded tip
        tip = [(tipx + side * th * 0.45 * np.sin(a), tipy + th * 0.5 - th * 0.5 * np.cos(a)) for a in np.linspace(0, np.pi, 8)]
        feathers.append(poly(W, H, pts + tip + bot))
    # covert band along the leading edge
    N = 30; ln = L * 1.02; th = L * 0.11; lift = -L * (0.16 + up)
    topc = [(x0 + side * u * ln, y0 - th * 0.75 + lift * u ** 2) for u in np.linspace(0, 1, N)]
    botc = [(x0 + side * u * ln * 0.92, y0 + th * 0.35 + lift * u ** 2 * 0.95) for u in np.linspace(1, 0, N)]
    cov = poly(W, H, topc + botc)
    return feathers[::-1], cov

def emblem(W=1400, H=760, wings='both', glow=True):
    """full emblem: wings ('both' | 'right' | 'left' | 'none'), Eye of Horus in emerald with gold outline. returns rgb(0-255 float), alpha"""
    C = Canvas(W, H); cx, cy = W / 2, H * 0.40
    ew, eh = W * 0.20, H * 0.13                                      # eye half-width / half-height
    L = W * 0.36
    for side in ([1, -1] if wings == 'both' else [1] if wings == 'right' else [-1] if wings == 'left' else []):
        fs, cov = wing(W, H, cx + side * ew * 0.75, cy + eh * 0.25, L, side)
        for f in fs: C.shape(f, GOLD, 3.2, light=(-side * 0.3, -1))
        C.shape(cov, GOLD, 3.6, light=(0, -1))
        # feather barbs: thin ink ticks on the covert band
        for k in range(1, 9):
            u = k / 9; x = cx + side * (ew * 0.75 + u * L * 0.95); lift = -L * 0.16 * u ** 2
            C.put(line(W, H, [(x, cy + eh * 0.25 - L * 0.08 + lift), (x - side * L * 0.03, cy + eh * 0.25 + L * 0.03 + lift)], 2.4), INK)
    # brow
    brow = [(cx - ew * 1.15, cy - eh * 1.35)]
    brow += [(cx - ew * 1.15 + 2.35 * ew * u, cy - eh * 1.35 - eh * 0.75 * np.sin(np.pi * min(1, u * 1.15))) for u in np.linspace(0, 1, 30)]
    brow_b = [(x, y + eh * 0.42) for x, y in brow[::-1]]
    C.shape(poly(W, H, brow + brow_b), EMER, 4, light=(0, -1))
    # eye almond: gold rim, white-gold sclera tone, emerald gem iris
    def almond(s):
        up = [(cx - ew * s * 1.12 + 2.24 * ew * s * u, cy - eh * s * np.sin(np.pi * u) ** 0.8) for u in np.linspace(0, 1, 40)]
        lo = [(cx - ew * s * 1.12 + 2.24 * ew * s * u, cy + eh * s * 0.75 * np.sin(np.pi * u) ** 0.9) for u in np.linspace(1, 0, 40)]
        lo[-1] = (cx - ew * s * 1.35, cy + eh * 0.10)                  # inner canthus line extends
        return up + lo
    C.shape(poly(W, H, almond(1.18)), GOLD, 4.5, light=(0, -1))
    C.shape(poly(W, H, almond(0.92)), [(18, 28, 22), (30, 44, 36), (46, 66, 54), (80, 110, 90)], 2.5)
    # tail line from outer corner (cosmetic line)
    C.shape(poly(W, H, [(cx + ew * 0.95, cy - eh * 0.10), (cx + ew * 2.05, cy - eh * 0.25), (cx + ew * 2.12, cy + eh * 0.12), (cx + ew * 1.0, cy + eh * 0.32)]), EMER, 3.5, light=(0, -1))
    # iris gem
    r = eh * 0.80; C.ink(ellipse(W, H, cx, cy, r, r), 4)
    gem = ellipse(W, H, cx, cy, r, r); C.shape(gem, EMER, 0.01, light=(-1, -1))
    C.put(ellipse(W, H, cx + r * 0.12, cy + r * 0.12, r * 0.52, r * 0.52), EMER[0])
    C.put(ellipse(W, H, cx - r * 0.32, cy - r * 0.34, r * 0.22, r * 0.18), EMER[3])
    # teardrop (vertical marking below the eye)
    tx = cx - ew * 0.05
    C.shape(poly(W, H, [(tx - eh * 0.22, cy + eh * 0.70), (tx + eh * 0.22, cy + eh * 0.70), (tx + eh * 0.26, cy + eh * 2.15), (tx, cy + eh * 2.45), (tx - eh * 0.26, cy + eh * 2.15)]), EMER, 3.5, light=(-1, 0))
    # spiral marking: starts under the eye's back corner, sweeps down and curls
    sp = []
    sx0, sy0 = cx + ew * 0.55, cy + eh * 0.65
    for u in np.linspace(0, 1, 60):
        sp.append((sx0 + ew * 0.35 * u, sy0 + eh * 1.1 * u))
    ccx, ccy, R = sx0 + ew * 0.35 - eh * 0.55, sy0 + eh * 1.1, eh * 0.55
    for a in np.linspace(0, 1.75 * np.pi, 60):
        rr = R * (1 - a / (2.6 * np.pi)); sp.append((ccx + rr * np.cos(a), ccy + rr * np.sin(a)))
    spm = line(W, H, sp, eh * 0.30)
    C.shape(spm, EMER, 3.5, light=(-1, -1))
    rgb, a = C.out()
    if glow:                                                           # soft emerald glow under everything
        g = cv2.GaussianBlur(a, (0, 0), W * 0.012) * 0.55
        gc = np.array(EMER[2], np.float32)
        out_a = a + g * (1 - a)
        rgb = (rgb * a[..., None] + gc * (g * (1 - a))[..., None]) / np.maximum(out_a, 1e-4)[..., None]
        a = out_a
    return rgb, a, (cx, cy)

if __name__ == '__main__':
    for wg in ['both', 'left']:
        rgb, a, _ = emblem(wings=wg)
        bg = np.full(rgb.shape, 40, np.float32)
        o = bg * (1 - a[..., None]) + rgb * a[..., None]
        cv2.imwrite(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'work', 'emb_%s.png') % wg, o[..., ::-1].clip(0, 255).astype(np.uint8))
