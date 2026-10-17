# Replace the shield's letter-like border runes with an interlaced knotwork band (never letter-like), re-inked, lit from the upper left.
import numpy as np, cv2, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from letter import cel_fill
# band centre path (2016x3024 reference frame of render3_storm), runs up the left side, across the top, down the right side
PATH = [(1392, 1848), (1392, 1760), (1394, 1700), (1408, 1655), (1450, 1626), (1500, 1606), (1556, 1590), (1610, 1578), (1665, 1572),
        (1720, 1590), (1762, 1615), (1800, 1645), (1834, 1690), (1853, 1740), (1859, 1800), (1857, 1868)]
BOT_BOX = (1515, 2372, 1672, 2552)          # glitchy rune marks above the bottom tip (the diamond at y~2340 is kept)
SHIELD_C = (1650, 1960)
ANT = np.array([(70, 42, 12), (128, 84, 26), (186, 132, 52), (226, 178, 88), (250, 222, 150)], np.float32)   # antique gold (RGB) to match the shield
INK = np.array((8, 7, 6), np.float32)

def resample(P, step=1.0):
    P = np.array(P, np.float32)
    # Catmull-Rom smoothing
    pts = []
    for i in range(len(P) - 1):
        p0, p1, p2, p3 = P[max(0, i - 1)], P[i], P[i + 1], P[min(len(P) - 1, i + 2)]
        for t in np.linspace(0, 1, 30, endpoint=False):
            pts.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t ** 2 + (-p0 + 3 * p1 - 3 * p2 + p3) * t ** 3))
    pts.append(P[-1]); pts = np.array(pts)
    d = np.r_[0, np.cumsum(np.hypot(*np.diff(pts, axis=0).T))]; s = np.arange(0, d[-1], step)
    return np.c_[np.interp(s, d, pts[:, 0]), np.interp(s, d, pts[:, 1])], s

def apply(A, sc=1.0, ox=0, oy=0, half=30):
    H, W = A.shape[:2]
    P = [(ox + x * sc, oy + y * sc) for x, y in PATH]; C = np.array([ox + SHIELD_C[0] * sc, oy + SHIELD_C[1] * sc])
    pts, s = resample(P)
    tang = np.gradient(pts, axis=0); tang /= np.linalg.norm(tang, axis=1, keepdims=True) + 1e-6
    nrm = np.c_[-tang[:, 1], tang[:, 0]]
    if np.mean(np.sum((C - pts) * nrm, 1)) < 0: nrm = -nrm               # normal points into the shield
    x0, y0 = (pts.min(0) - 80).astype(int); x1, y1 = (pts.max(0) + 80).astype(int)
    roi = A[y0:y1, x0:x1].astype(np.float32); h, w = roi.shape[:2]
    # ---- erase: small bright marks within the band (rim and Vegvisir are large components, kept) ----
    band = np.zeros((h, w), np.uint8)
    cv2.polylines(band, [(pts - (x0, y0)).astype(np.int32)], False, 255, int(2 * half * sc))
    mx = roi.max(2); br = (mx > 62).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(br, connectivity=8)
    kill = np.zeros((h, w), np.uint8)
    for i in range(1, n):
        if st[i, 4] < 2600 * sc * sc and st[i, 2] < 95 * sc and st[i, 3] < 95 * sc:
            comp = lab == i
            if (band[comp] > 0).mean() > 0.5: kill[comp] = 255
    kill = cv2.dilate(kill, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
    clean = cv2.inpaint(roi.clip(0, 255).astype(np.uint8), kill, 7, cv2.INPAINT_TELEA).astype(np.float32)
    # ---- knotwork: two interlaced strands + thin border rules, supersampled ----
    S = 3; amp, lam, sw = 12.0 * sc, 54.0 * sc, 8.5 * sc
    def canvas(): return np.zeros((h * S, w * S), np.uint8)
    def draw_line(m, Q, width):
        cv2.polylines(m, [((Q - (x0, y0)) * S).astype(np.int32)], False, 255, max(1, int(width * S)), cv2.LINE_AA)
    ph = 2 * np.pi * s / lam
    st1 = pts + nrm * (amp * np.sin(ph))[:, None]; st2 = pts - nrm * (amp * np.sin(ph))[:, None]
    # crossings where sin(ph)=0 -> s = k*lam/2; split strands into pieces centred on crossings
    under_ink, under_fill, over_ink, over_fill = canvas(), canvas(), canvas(), canvas()
    half_l = lam / 4
    ncross = int(s[-1] / (lam / 2)) + 1
    for k in range(ncross):
        sc_ = k * lam / 2; sel = (s >= sc_ - half_l) & (s <= sc_ + half_l)
        if sel.sum() < 2: continue
        a, b = (st1, st2) if k % 2 == 0 else (st2, st1)                  # a = over strand at this crossing
        draw_line(under_ink, b[sel], sw + 2 * 2.6 * sc); draw_line(under_fill, b[sel], sw)
        draw_line(over_ink, a[sel], sw + 2 * 2.6 * sc); draw_line(over_fill, a[sel], sw)
    rules_ink, rules_fill = canvas(), canvas()
    for o in (amp + sw * 0.5 + 7 * sc, -(amp + sw * 0.5 + 7 * sc)):
        Q = pts + nrm * o; draw_line(rules_ink, Q, 3.2 * sc + 2 * 2.2 * sc); draw_line(rules_fill, Q, 3.2 * sc)
    # end caps: small lens knots terminate the band at both ends
    caps_ink, caps_fill = canvas(), canvas()
    for idx, sgn in ((0, -1), (-1, 1)):
        c = pts[idx] + tang[idx] * sgn * 10 * sc
        for m, rad in ((caps_ink, amp + sw * 0.5 + 9 * sc + 2.6 * sc), (caps_fill, amp + sw * 0.5 + 9 * sc)):
            cv2.circle(m, tuple(((c - (x0, y0)) * S).astype(int)), int(rad * S), 255, -1, cv2.LINE_AA)
    def f(m): return cv2.resize(m.astype(np.float32) / 255, (w, h), interpolation=cv2.INTER_AREA)
    out = clean.copy()
    def put(m, col):
        nonlocal out
        out = out * (1 - m[..., None]) + col * m[..., None]
    def gold(m, bev):
        c = cel_fill((m > 0.5).astype(np.float32), ANT, bev, light=(-0.75, -0.66), band=False)[..., ::-1]   # RGB->BGR
        return cv2.GaussianBlur(c, (0, 0), 0.6)
    put(f(caps_ink), INK); put(f(caps_fill), gold(f(caps_fill), 3 * sc))
    put(f(rules_ink), INK); put(f(rules_fill), gold(f(rules_fill), 1.2 * sc))
    put(f(under_ink), INK); put(f(under_fill), gold(f(under_fill), 2.2 * sc) * 0.82)
    put(f(over_ink), INK); put(f(over_fill), gold(f(over_fill), 2.2 * sc))
    # cast shadow of the band onto the field (light from upper left -> shadow offset down-right)
    allm = np.maximum.reduce([f(under_ink), f(over_ink), f(rules_ink), f(caps_ink)])
    shd = cv2.warpAffine(allm, np.float32([[1, 0, 3 * sc], [0, 1, 4 * sc]]), (w, h)); shd = cv2.GaussianBlur(shd, (0, 0), 2) * (1 - allm)
    out = out * (1 - 0.45 * shd[..., None])
    A[y0:y1, x0:x1] = out.clip(0, 255)
    # ---- bottom marks: clean to plain field ----
    bx0, by0, bx1, by1 = [int(round(v * sc)) for v in BOT_BOX]; bx0 += ox; bx1 += ox; by0 += oy; by1 += oy
    r2 = A[by0:by1, bx0:bx1].clip(0, 255).astype(np.uint8)
    km = (r2.max(2) > 55).astype(np.uint8); n, lab, st, _ = cv2.connectedComponentsWithStats(km, 8)
    kk = np.zeros_like(km)
    for i in range(1, n):
        x_, y_, w_, h_, a_ = st[i]
        touches = x_ == 0 or y_ == 0 or x_ + w_ >= km.shape[1] or y_ + h_ >= km.shape[0]
        if a_ < 1500 * sc * sc and not touches: kk[lab == i] = 255
    kk = cv2.dilate(kk, np.ones((7, 7), np.uint8))
    A[by0:by1, bx0:bx1] = cv2.inpaint(r2, kk, 6, cv2.INPAINT_TELEA)
    return A
