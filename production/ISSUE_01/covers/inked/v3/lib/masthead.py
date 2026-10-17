import numpy as np, cv2, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from letter import *
SS = 2

def pad_to(m, H, W, x, y):
    o = np.zeros((H, W), np.float32); h, w = m.shape; o[y:y + h, x:x + w] = m; return o

def crop_mask(m, thr=0.02):
    ys, xs = np.where(m > thr); return ys.min(), ys.max() + 1, xs.min(), xs.max() + 1

VARIANTS = {
    # name: wordmark font, weight, cap px (final), track (em), shear, subline font
    'A_anton':  dict(f='anton', w=None, cap=250, track=0.02, shear=0.0, sub='anton', subw=None, subtrack=0.20, outer=None),
    'B_cinzel': dict(f='cinzel', w=900, cap=165, track=0.03, shear=0.0, sub='cinzel', subw=800, subtrack=0.22, outer=None),
    'C_bebas':  dict(f='bebas', w=None, cap=260, track=0.03, shear=0.12, sub='bebas', subw=None, subtrack=0.28, outer=(248, 184, 156)),
}

def masthead(var):
    v = VARIANTS[var]; cap = v['cap'] * SS
    f = font(v['f'], cap * 1.38, v['w']); bb = f.getbbox('H'); f = font(v['f'], cap * 1.38 * cap / (bb[3] - bb[1]), v['w'])
    t, b, capH = text_mask(['RA', '⚡', 'THOR'], f, track=v['track'] * cap, pad=int(cap * 0.5), shear=v['shear'], bolt_scale=1.32, gap=0.04)
    # subline
    sc = cap * 0.30
    fs = font(v['sub'], sc * 1.38, v['subw']); bb = fs.getbbox('H'); fs = font(v['sub'], sc * 1.38 * sc / (bb[3] - bb[1]), v['subw'])
    s, _, _ = text_mask(['LIVING THUNDER'], fs, track=v['subtrack'] * sc, pad=int(cap * 0.3), shear=v['shear'])
    # TM
    ft = font('anton', sc * 0.75); tm, _, _ = text_mask(['TM'], ft, track=sc * 0.03, pad=10)
    # assemble on one canvas
    y0, y1, x0, x1 = crop_mask(t + b); t, b = t[y0:y1, x0:x1], b[y0:y1, x0:x1]
    sy0, sy1, sx0, sx1 = crop_mask(s); s = s[sy0:sy1, sx0:sx1]
    ty0, ty1, tx0, tx1 = crop_mask(tm); tm = tm[ty0:ty1, tx0:tx1]
    P = int(cap * 0.35); Wd = t.shape[1]
    gapv = int(cap * 0.16)
    H = P + t.shape[0] + gapv + s.shape[0] + P + int(cap * 0.2); W = Wd + 2 * P + tm.shape[1] + int(cap * 0.1)
    T = pad_to(t, H, W, P, P); B = pad_to(b, H, W, P, P)
    sx = P + (Wd - s.shape[1]) // 2; sy = P + t.shape[0] + gapv
    S = pad_to(s, H, W, sx, sy)
    # gold rules either side of subline
    R = np.zeros((H, W), np.float32); ry = sy + s.shape[0] // 2; rh = max(3, int(sc * 0.12)); gap = int(sc * 0.5)
    for xa, xb in [(P + int(Wd * 0.04), sx - gap), (sx + s.shape[1] + gap, P + Wd - int(Wd * 0.04))]:
        if xb - xa > 20:
            cv2.rectangle(R, (xa, ry - rh), (xb, ry + rh), 1.0, -1)
            for ex_ in (xa, xb):
                pts = np.array([[ex_ - rh * 3, ry], [ex_, ry - rh * 3], [ex_ + rh * 3, ry], [ex_, ry + rh * 3]], np.int32); cv2.fillPoly(R, [pts], 1.0)
    TM = pad_to(tm, H, W, P + Wd + int(cap * 0.04), sy + s.shape[0] - tm.shape[0])
    key = cap * 0.055
    C = inked([(T, GOLD, cap * 0.07), (B, ROSE, cap * 0.07)], key, ext=(cap * 0.045, cap * 0.07), outer=v['outer'])
    C2 = inked([(S, GOLD, sc * 0.10), (R, GOLD, rh * 0.6)], sc * 0.11, ext=(sc * 0.06, sc * 0.10), ht=False)
    C3 = inked([(TM, GOLD, 2)], sc * 0.07, ext=(sc * 0.03, sc * 0.05), ht=False)
    for Cx in (C2, C3): C.put(Cx.a, Cx.rgb)
    rgb, a = C.down(SS)
    return rgb, a, dict(key_px=key / SS)

def coin(D=330, var='A'):
    """comic roundel: black keyline, gold cel-shaded rim, emerald field, ISSUE small, #1 big."""
    R = D * SS / 2; P = int(R * 0.35); N = int(2 * R + 2 * P); C = Comp(N, N); c = N / 2
    yy, xx = np.mgrid[0:N, 0:N].astype(np.float32); r = np.hypot(xx - c, yy - c)
    key = R * 0.055 * 2.0
    disc = np.clip(R - r + 0.5, 0, 1)
    # extrusion shadow + halftone
    dx, dy = R * 0.06, R * 0.09
    kl = np.clip(R + key - r + 0.5, 0, 1)
    ex = np.zeros_like(kl)
    for i in range(1, 25): M = np.float32([[1, 0, dx * i / 24], [0, 1, dy * i / 24]]); ex = np.maximum(ex, cv2.warpAffine(kl, M, (N, N)))
    M = np.float32([[1, 0, dx * 1.9], [0, 1, dy * 1.9]]); sh = cv2.warpAffine(kl, M, (N, N))
    dots = (halftone((N, N), key * 1.1) < 0.36).astype(np.float32); C.put(np.clip(sh - ex, 0, 1) * dots * 0.85, INK)
    C.put(cv2.dilate(ex, k(key * 0.55)), INK); C.put(cv2.erode(ex, k(key * 0.5)), BRONZE); C.put(kl, INK)
    # rim: cel ring lit from upper-left
    ang = np.arctan2(yy - c, xx - c); lit = -(np.cos(ang) * -0.75 + np.sin(ang) * -0.66) * -1      # >0 facing light (upper-left)
    rim = np.empty((N, N, 3), np.float32); rim[:] = GOLD[2]
    rim[lit > 0.35] = GOLD[3]; rim[lit > 0.8] = GOLD[4]; rim[lit < -0.3] = GOLD[1]; rim[lit < -0.8] = GOLD[0]
    C.put(disc, rim)
    # inner bevel step (reverse lighting = recessed)
    r2 = R * 0.80; inner = np.clip(r2 - r + 0.5, 0, 1); C.put(np.clip(r2 + key * 0.45 - r + 0.5, 0, 1), INK)
    bev = np.empty((N, N, 3), np.float32); bev[:] = GOLD[2]; bev[lit > 0.3] = GOLD[1]; bev[lit < -0.3] = GOLD[3]
    C.put(inner, bev)
    r3 = R * 0.72; C.put(np.clip(r3 + key * 0.4 - r + 0.5, 0, 1), INK)
    field = np.clip(r3 - r + 0.5, 0, 1); fc = np.empty((N, N, 3), np.float32); fc[:] = EMER[2]
    fc[(yy - c) > (xx - c) * -0.4 + r3 * 0.15] = EMER[1]                        # cel split: lower-right darker
    fc[lit > 0.5 * (r > r3 * 0.86)] = fc[lit > 0.5 * (r > r3 * 0.86)]
    hd = halftone((N, N), R * 0.035, 30); rr_ = np.hypot(xx - c, yy - c); fc[(hd < 0.22 * np.clip((yy - c) / r3 + 0.2, 0, 1)) ] = EMER[0]   # halftone in the field's shadow
    C.put(field, fc)
    # rivets on rim
    for i in range(12):
        a = i * np.pi / 6 + np.pi / 12; px, py = c + R * 0.90 * np.cos(a), c + R * 0.90 * np.sin(a)
        rr = np.hypot(xx - px, yy - py); C.put(np.clip(R * 0.045 - rr + 0.5, 0, 1), INK)
        C.put(np.clip(R * 0.028 - np.hypot(xx - px + R * 0.008, yy - py + R * 0.008) + 0.5, 0, 1), GOLD[4] if np.cos(a) * -0.75 + np.sin(a) * -0.66 > 0 else GOLD[2])
    # text
    fI = font('anton', R * 0.30); tI, _, _ = text_mask(['ISSUE'], fI, track=R * 0.035, pad=20)
    f1 = font('anton', R * 0.92); t1, _, _ = text_mask(['#1'], f1, track=R * 0.02, pad=30)
    y0, y1, x0, x1 = crop_mask(tI); tI = tI[y0:y1, x0:x1]; y0, y1, x0, x1 = crop_mask(t1); t1 = t1[y0:y1, x0:x1]
    gapv = R * 0.07; tot = tI.shape[0] + gapv + t1.shape[0]; ty = int(c - tot / 2 + R * 0.03)
    TI = pad_to(tI, N, N, int(c - tI.shape[1] / 2), ty); T1 = pad_to(t1, N, N, int(c - t1.shape[1] / 2), int(ty + tI.shape[0] + gapv))
    Ct = inked([(TI, GOLD, R * 0.016), (T1, GOLD, R * 0.04)], R * 0.035, ext=(R * 0.022, R * 0.034), ht=False)
    C.put(Ct.a, Ct.rgb)
    rgb, a = C.down(SS); return rgb, a
