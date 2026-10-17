# Canon halo: Eye of Horus centred in 3 thin concentric rings (white-gold inner, softer gold, outer with faint rose thread),
# 8 evenly spaced radial spokes on the main sun rays, 8 short rays between; flat glowing disc facing camera (unforeshortened).
import numpy as np, cv2
SS = 3
WG = np.array([255, 252, 236], np.float32); GOLD = np.array([255, 206, 102], np.float32); SOFT = np.array([240, 184, 92], np.float32)
ROSE = np.array([246, 170, 156], np.float32)

def bg_mask(A, cx, cy, R, thr=20):
    """background (sky + old halo) pixels inside radius R: flood from the halo centre through non-ink pixels; enclosed dark holes added."""
    X0, Y0 = int(cx - R - 40), int(cy - R - 40); X1, Y1 = int(cx + R + 40), int(cy + R + 40)
    Lm = A[Y0:Y1, X0:X1].min(2)
    ink = cv2.dilate((Lm < thr).astype(np.uint8), np.ones((3, 3), np.uint8))
    n, lab = cv2.connectedComponents((1 - ink).astype(np.uint8), connectivity=4)
    seeds = [(cx, cy - R * 0.55), (cx, cy - R * 0.2), (cx - R * 0.4, cy - R * 0.3), (cx + R * 0.4, cy - R * 0.3)]
    ids = {lab[int(y - Y0), int(x - X0)] for x, y in seeds} - {0}
    m = np.isin(lab, list(ids)).astype(np.uint8)
    # holes: complement components not touching the crop border -> background too (dark sky islands)
    comp = (1 - m).astype(np.uint8); n2, lab2 = cv2.connectedComponents(comp, connectivity=4)
    border = set(np.unique(np.r_[lab2[0], lab2[-1], lab2[:, 0], lab2[:, -1]]))
    sizes = np.bincount(lab2.ravel())
    for i in range(1, n2):
        if i not in border: m[lab2 == i] = 1
    yy, xx = np.mgrid[Y0:Y1, X0:X1]; m = m * (np.hypot(xx - cx, yy - cy) < R)
    full = np.zeros(A.shape[:2], np.float32); full[Y0:Y1, X0:X1] = m
    return full

def draw(W, H, cx, cy, r_in, r_mid, r_out, r_sun, eye_w):
    """returns core (white-gold line art, RGB float 0..255 premult) and alpha at 1x; drawn at SSx."""
    S = SS; Wc, Hc = W * S, H * S; X, Y = cx * S, cy * S
    def P(x, y): return int(round(x)), int(round(y))
    layers = []   # (mask, colour)
    def ring(r, w, col):
        m = np.zeros((Hc, Wc), np.uint8); cv2.circle(m, P(X, Y), int(r * S), 255, max(1, int(w * S)), cv2.LINE_AA); layers.append((m, col))
    def poly(pts, col):
        m = np.zeros((Hc, Wc), np.uint8); cv2.fillPoly(m, [np.array([P(X + x * S, Y + y * S) for x, y in pts], np.int32)], 255, cv2.LINE_AA); layers.append((m, col))
    def stroke(pts, w, col, closed=False):
        m = np.zeros((Hc, Wc), np.uint8); cv2.polylines(m, [np.array([P(X + x * S, Y + y * S) for x, y in pts], np.int32)], closed, 255, max(1, int(w * S)), cv2.LINE_AA); layers.append((m, col))
    # rings
    ring(r_out, 4.0, SOFT); ring(r_out + 0.5, 1.6, ROSE)
    ring(r_mid, 5.0, GOLD)
    ring(r_in, 6.0, WG)
    ring(r_sun, 8.0, WG)
    # 8 spokes on the main rays: from the sun disc to the outer ring, tapered; small diamond where they meet the outer ring
    for k in range(8):
        a = k * np.pi / 4 - np.pi / 2; c, s = np.cos(a), np.sin(a); n = (-s, c)
        r0, r1 = r_sun + 4, r_out + (24 if k % 2 == 0 else 10); w0, w1 = 10 if k % 2 == 0 else 7, 2.0
        poly([(c * r0 + n[0] * w0, s * r0 + n[1] * w0), (c * r1 + n[0] * w1, s * r1 + n[1] * w1), (c * (r1 + 10), s * (r1 + 10)), (c * r1 - n[0] * w1, s * r1 - n[1] * w1), (c * r0 - n[0] * w0, s * r0 - n[1] * w0)], WG)
        rd = r_out; dd = 11 if k % 2 == 0 else 8
        poly([(c * (rd - dd * 1.6), s * (rd - dd * 1.6)), (c * rd + n[0] * dd, s * rd + n[1] * dd), (c * (rd + dd * 1.6), s * (rd + dd * 1.6)), (c * rd - n[0] * dd, s * rd - n[1] * dd)], WG)
    # 8 short sun rays between the spokes
    for k in range(8):
        a = k * np.pi / 4 - np.pi / 2 + np.pi / 8; c, s = np.cos(a), np.sin(a); n = (-s, c)
        r0, r1, w0 = r_sun + 4, r_in - 30, 11
        poly([(c * r0 + n[0] * w0, s * r0 + n[1] * w0), (c * r1, s * r1), (c * r0 - n[0] * w0, s * r0 - n[1] * w0)], GOLD)
    # Eye of Horus (line art, white-gold), centred
    ew = eye_w / 2; eh = ew * 0.42; lw = 10
    t = np.linspace(0, 1, 60)
    up = [(-ew + 2 * ew * u, -eh * np.sin(np.pi * u) ** 0.85) for u in t]
    lo = [(-ew + 2 * ew * u, eh * 0.72 * np.sin(np.pi * u) ** 0.95) for u in t[::-1]]
    stroke(up + lo, lw, WG, closed=True)
    stroke([(ew * 0.98, eh * 0.02), (ew * 1.22, eh * 0.10)], lw * 0.9, WG)                        # cosmetic line to the back
    brow = [(-ew * 1.02 + 2.2 * ew * u, -eh * 1.55 - eh * 0.55 * np.sin(np.pi * min(1, u * 1.12))) for u in t]
    stroke(brow, lw * 1.25, WG)
    ri = eh * 0.80
    m = np.zeros((Hc, Wc), np.uint8); cv2.circle(m, P(X, Y), int(ri * S), 255, int(lw * S), cv2.LINE_AA); layers.append((m, WG))
    m = np.zeros((Hc, Wc), np.uint8); cv2.circle(m, P(X, Y), int(ri * 0.45 * S), 255, -1, cv2.LINE_AA); layers.append((m, WG))
    # teardrop: hangs below the front of the eye, slightly slanted
    tx = -ew * 0.42
    poly([(tx - 7, eh * 0.66), (tx + 7, eh * 0.70), (tx - 2, eh * 2.0), (tx - 12, eh * 2.30), (tx - 16, eh * 2.0)], WG)
    # spiral tail: leaves the back of the eye low, sweeps out and curls clockwise (never letter-like)
    sp = [(ew * 0.40 + ew * 0.45 * u, eh * 0.62 + eh * 0.95 * u ** 1.4) for u in np.linspace(0, 1, 40)]
    ex_, ey_ = sp[-1]; R0 = eh * 0.48; ccx, ccy = ex_ - R0, ey_
    for a in np.linspace(0, 1.65 * np.pi, 80):
        rr = R0 * (1 - a / (2.3 * np.pi)); sp.append((ccx + rr * np.cos(a), ccy + rr * np.sin(a)))
    stroke(sp, lw * 0.9, WG)
    rgb = np.zeros((Hc, Wc, 3), np.float32); al = np.zeros((Hc, Wc), np.float32)
    # two-tone glowing line: every white-gold element sits on a slightly wider warm-gold edge
    wgu = np.zeros((Hc, Wc), np.uint8)
    for m, col in layers:
        if col is WG: wgu = np.maximum(wgu, m)
    layers.insert(0, (cv2.dilate(wgu, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3 * S + 1, 3 * S + 1))), GOLD))
    for m, col in layers:
        mm = m.astype(np.float32) / 255; rgb = rgb * (1 - mm[..., None]) + col * mm[..., None]; al = np.maximum(al, mm)
    rgb = cv2.resize(rgb * al[..., None], (W, H), interpolation=cv2.INTER_AREA); al = cv2.resize(al, (W, H), interpolation=cv2.INTER_AREA)
    return rgb, al

def apply(A, cx, cy, r_in=326, r_mid=385, r_out=494, r_sun=188, eye_w=270, R_erase=540):
    """A float32 BGR page art. Erase the old halo (background pixels only) and paint the canon halo behind the figure."""
    H, W = A.shape[:2]
    m = bg_mask(A, cx, cy, R_erase)
    # clean backdrop: remove thin bright strokes (opening) and old glow (blur), keep low-frequency clouds
    op = cv2.morphologyEx(A, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (45, 45)))
    back = cv2.GaussianBlur(op, (0, 0), 14)
    dark = (m > 0) & (A.max(2) < 26); sky = np.median(A[dark], axis=0) if dark.sum() > 500 else np.array([22, 16, 14], np.float32)
    lum = back.max(2, keepdims=True); back = back * np.minimum(1, sky.max() / np.maximum(lum, 1))    # cap at the dark-sky level: no old glow
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32); rr = np.hypot(xx - cx, yy - cy)
    edge = np.clip((R_erase - rr) / 26, 0, 1)                                   # feather into the untouched sky
    me = cv2.GaussianBlur(m, (0, 0), 0.8) * edge
    base = A * (1 - me[..., None]) + back * me[..., None]
    B = int(r_out + 70); lx0, ly0 = int(cx) - B, int(cy) - B
    cr, ca = draw(2 * B, 2 * B, cx - lx0, cy - ly0, r_in, r_mid, r_out, r_sun, eye_w)
    core_rgb = np.zeros((H, W, 3), np.float32); core_a = np.zeros((H, W), np.float32)
    core_rgb[ly0:ly0 + 2 * B, lx0:lx0 + 2 * B] = cr[..., ::-1]; core_a[ly0:ly0 + 2 * B, lx0:lx0 + 2 * B] = ca
    # glow: two blurs of the line art (gold), plus a faint disc wash for the backlight
    g1 = cv2.GaussianBlur(core_rgb, (0, 0), 5); g2 = cv2.GaussianBlur(core_rgb, (0, 0), 22)
    wash = (np.clip(1 - rr / (r_out + 40), 0, 1) ** 1.6)[..., None] * np.array([30, 70, 120], np.float32) * 0.45
    light = g1 * 0.8 + g2 * 0.75 + wash
    lit = 255 - (255 - base) * (1 - np.clip(light / 255, 0, 1))                    # screen
    lit = lit * (1 - core_a[..., None]) + np.maximum(core_rgb / np.maximum(core_a, 1e-4)[..., None], lit) * core_a[..., None]
    out = base * (1 - me[..., None]) + lit * me[..., None]
    # the halo's light also spills softly onto the figure's top edges (backlight rim), outside the bg mask
    spill = cv2.GaussianBlur(m, (0, 0), 6) * (1 - m) * np.clip(1 - rr / (r_out + 60), 0, 1)
    out = out + spill[..., None] * np.array([30, 80, 120], np.float32) * 0.8
    return out.clip(0, 255), m
