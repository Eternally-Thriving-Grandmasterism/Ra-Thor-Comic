# Extract the AlphaProMega Media logo from its navy starfield: estimate the background plate, colour-to-alpha against it
# (keeps the rays' gold glow soft, removes the navy contribution from every edge pixel), solidify letter/alpha cores, drop stars.
# usage: apm_extract.py SRC_RGB [SCALE_SRC_TO_1X]   (SRC may be the 1x jpg or the 4x UltraSharp png)
import cv2, numpy as np, sys
D = '/workspace/issue01/back/'
src = sys.argv[1] if len(sys.argv) > 1 else D + 'apm_logo_source.jpg'
I1 = cv2.imread(D + 'apm_logo_source.jpg').astype(np.float32)          # 1x reference (bg plate + masks are built at 1x)
h1, w1 = I1.shape[:2]
L1 = I1.max(2)
# --- 1. background plate at 1x: mask everything brighter than the local navy, inpaint, smooth ---
med = cv2.medianBlur(I1.astype(np.uint8), 31).astype(np.float32)
fg = ((I1 - med).max(2) > 10).astype(np.uint8)
fg = cv2.dilate(fg, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (41, 41)))
B1 = cv2.inpaint(I1.astype(np.uint8), fg, 25, cv2.INPAINT_TELEA).astype(np.float32)
B1 = cv2.GaussianBlur(B1, (0, 0), 12)
# --- 2. which pixels belong to the logo: big components of the (blurred) excess over the plate ---
ex = np.clip((I1 - B1).max(2), 0, None)
core = (cv2.GaussianBlur(ex, (0, 0), 1.5) > 14).astype(np.uint8)
n, lab, st, _ = cv2.connectedComponentsWithStats(core, 8)
keep = np.zeros_like(core); emb = np.zeros_like(core); kept = 0
for i in range(1, n):
    x, y, w, h, ar = st[i]
    if ar < 60: continue                                                 # stars
    if x > 400 and y + h < 330: continue                                 # the nebula wisp top-right, above the wordmark
    keep[lab == i] = 1; kept += 1
    if x < 400: emb[lab == i] = 1                                        # alpha glyph + rays (one component)
print('components kept', kept, 'of', n - 1)
el = lambda k: cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k))
# emblem: generous room for the soft gold ray glow; wordmark: tight (its own antialias + faint glow only)
region1 = np.maximum(cv2.GaussianBlur(cv2.dilate(emb, el(41)).astype(np.float32), (0, 0), 8),
                     cv2.GaussianBlur(cv2.dilate(keep, el(7)).astype(np.float32), (0, 0), 1.5))
solid1 = cv2.erode(keep, np.ones((2, 2), np.uint8)).astype(np.float32)
# --- 3. go to working resolution ---
I = cv2.imread(src); s = I.shape[1] / w1
ys, xs = np.where(region1 > 0.002); P = 6
cy0, cy1, cx0, cx1 = max(0, ys.min() - P), min(h1, ys.max() + P), max(0, xs.min() - P), min(w1, xs.max() + P)
I = I[round(cy0 * s):round(cy1 * s), round(cx0 * s):round(cx1 * s)].astype(np.float32); H, W = I.shape[:2]   # work on the logo box only (memory)
crop1 = lambda x: x[cy0:cy1, cx0:cx1]
up = lambda x: cv2.resize(crop1(x), (W, H), interpolation=cv2.INTER_CUBIC)
B = up(B1); region = np.clip(up(region1), 0, 1)
# --- 4. colour-to-alpha vs the plate (GIMP-style: smallest alpha that keeps the foreground colour in gamut) ---
# only light ADDED over the plate counts (the logo is all gold/white light); pixels darker than the plate are grain -> alpha 0
a = (np.clip(I - B, 0, None) / np.maximum(255 - B, 1)).max(2)
a = cv2.GaussianBlur(a, (0, 0), 0.7 * s) * 0.5 + a * 0.5 if s < 2 else cv2.GaussianBlur(a, (0, 0), 0.5 * s)   # de-grain
a = np.clip((a - 0.045) / 0.955, 0, 1)                                     # kill the plate's grain / JPEG noise floor
# solid cores: letters and the alpha glyph are fully opaque (no see-through gold); soft ramp only at the edge
solid = cv2.GaussianBlur(up(solid1), (0, 0), 0.6 * s)
asol = np.clip((a - 0.35) / 0.30, 0, 1) * np.clip(solid * 1.6, 0, 1)
a = np.maximum(a, asol) * region
F = (I - (1 - a[..., None]) * B) / np.maximum(a[..., None], 1e-3)
F = np.clip(F, 0, 255)
F[a < 0.004] = 0
# anti-navy guard: anything left on the foreground where blue dominates the warm channels is pulled to neutral
blue_x = np.clip(F[..., 0] - np.maximum(F[..., 1], F[..., 2]), 0, None)
F[..., 0] -= blue_x
out = np.dstack([F, a * 255]).round().clip(0, 255).astype(np.uint8)
ys, xs = np.where(a > 0.01); P = int(24 * s)
y0, y1, x0, x1 = max(0, ys.min() - P), min(H, ys.max() + P), max(0, xs.min() - P), min(W, xs.max() + P)
out = out[y0:y1, x0:x1]
dst = sys.argv[2] if len(sys.argv) > 2 else D + 'apm_logo_transparent_1x.png'
cv2.imwrite(dst, out); print('wrote', dst, out.shape, 'crop', x0, y0)
