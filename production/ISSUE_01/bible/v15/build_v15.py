# ISSUE01-COVER-V15 print cover: Sherif's single true Grok Imagine render, untouched painting.
#  art  : 4x-UltraSharp (spandrel, CPU, upscale.py) -> tone lock (consistency.py back-projection: the 4x shrunk back
#         to 1x matches the source) -> ONE uniform INTER_AREA scale to fit height 3150 -> centre-crop width to 2063.
#         No inpainting/outpainting/extension/paste/repaint of the art.
#  type : the locked RA-THOR / LIVING THUNDER band + ISSUE #1 seal (v10.1 layer, ../v11/title_layer.py), with the two
#         stray gold flecks removed by clean_title.py (lettering-layer cleanup only), uniformly scaled and composited as a
#         separate RGBA layer in the top-right sky, fully inside safe, clear of the hammer, halo and wings and their glow.
#  run  : python3 upscale.py /workspace/models/4x-UltraSharp.pth src_v15.jpg up_x4_us_raw.png
#         python3 consistency.py up_x4_us_raw.png src_v15.jpg up_x4_us_bp.png
#         python3 clean_title.py && python3 build_v15.py
import cv2, numpy as np, sys
sys.path.insert(0, '/workspace/issue01/release'); import srgb
D = '/workspace/issue01/v15/'
FW, FH, BL, SF = 2063, 3150, 37, 75          # sheet w/ bleed, bleed px (0.125 in), safe inset from trim (0.25 in)
SAFE = BL + SF                               # 112 px from the sheet edge
F = float(sys.argv[1]) if len(sys.argv) > 1 else 0.80   # title scale relative to its v10.1 print size
RM, TM = 4, 4                                # px between the layer's outermost (shadow) pixel and the right / top safe line

# ---------- art ----------
N = cv2.imread(D + 'src_v15.jpg'); h1, w1 = N.shape[:2]
U = cv2.imread(D + 'up_x4_us_bp.png'); assert U.shape[:2] == (h1 * 4, w1 * 4)
k = FH / U.shape[0]; W = round(U.shape[1] * k)
A = cv2.resize(U, (W, FH), interpolation=cv2.INTER_AREA); del U
cx = (W - FW) // 2; A = A[:, cx:cx + FW].copy()
print('art: scale %.5f of 4x (x%.4f vs source), %dx%d -> crop x %d..%d' % (k, k * 4, W, FH, cx, cx + FW))
srgb.save(D + 'art_v15_print_notext.png', A, dpi=300)

# ---------- type layer ----------
T = np.load(D + 'title_rgb_hires_v15.npy').astype(np.float32); a = np.load(D + 'title_a_hires_v15.npy').astype(np.float32)
ys, xs = np.where(a > 0.004); y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
T, a = T[y0:y1, x0:x1], a[y0:y1, x0:x1]
s = 1988 / 640 / 4 * F
tw, th = round((x1 - x0) * s), round((y1 - y0) * s)
pa = cv2.resize(a, (tw, th), interpolation=cv2.INTER_AREA)
pT = cv2.resize(T * a[..., None], (tw, th), interpolation=cv2.INTER_AREA) / np.maximum(pa, 1e-4)[..., None]
X0 = FW - 1 - SAFE - RM - tw + 1; Y0 = SAFE + TM
L = np.zeros((FH, FW), np.float32); LT = np.zeros((FH, FW, 3), np.float32)
L[Y0:Y0 + th, X0:X0 + tw] = pa; LT[Y0:Y0 + th, X0:X0 + tw] = pT
rgba = np.dstack([np.clip(LT + .5, 0, 255), np.clip(L * 255 + .5, 0, 255)]).astype(np.uint8)
cv2.imwrite(D + 'title_layer_v15.png', rgba)                 # separate full-sheet type layer (RGBA)
O = np.clip(A * (1 - L[..., None]) + LT * L[..., None] + .5, 0, 255).astype(np.uint8)
srgb.save(D + 'print_v15.jpg', O, dpi=300, quality=97)
for t, nm in ((0.004, 'layer incl. soft shadow'), (0.5, 'glyphs + seal')):
    yy, xx = np.where(L > t)
    print('title %-24s x %d..%d y %d..%d | inside trim by L %d R %d T %d px | inside safe: %s' % (nm, xx.min(), xx.max(), yy.min(), yy.max(),
          xx.min() - BL, FW - 1 - BL - xx.max(), yy.min() - BL, xx.min() >= SAFE and xx.max() <= FW - 1 - SAFE and yy.min() >= SAFE))
print('title: F %.3f -> %.4f of hi-res layer, %dx%d px (%.2fx%.2f in) at x %d..%d y %d..%d' % (F, s, tw, th, tw / 300, th / 300, X0, X0 + tw - 1, Y0, Y0 + th - 1))

# ---------- guides (overlay only; no barcode box) ----------
G = O.copy()
def rect(img, m, col, t=3): cv2.rectangle(img, (m, m), (FW - 1 - m, FH - 1 - m), col, t, cv2.LINE_AA)
rect(G, 1, (255, 0, 255)); rect(G, BL, (0, 0, 255)); rect(G, SAFE, (255, 255, 0))
cv2.putText(G, 'BLEED 0.125" (sheet edge 2063x3150)', (10, FH - 10), cv2.FONT_HERSHEY_SIMPLEX, .8, (255, 0, 255), 2, cv2.LINE_AA)
cv2.putText(G, 'TRIM 6.625x10.25"', (BL + 12, FH - BL - 12), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2, cv2.LINE_AA)
cv2.putText(G, 'SAFE 0.25" inside trim', (SAFE + 12, FH - SAFE - 14), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 2, cv2.LINE_AA)
srgb.save(D + 'print_v15_guides.jpg', G, dpi=300, quality=92)

# ---------- preview + 100% crops ----------
srgb.save(D + 'preview_620.jpg', cv2.resize(O, (620, round(FH * 620 / FW)), interpolation=cv2.INTER_AREA), dpi=72, quality=92)
def src2p(x, y): return round(x * FH / h1 - cx), round(y * FH / h1)
G1 = O.copy(); rect(G1, BL, (0, 0, 255), 1); rect(G1, SAFE, (255, 255, 0), 1)   # 1 px lines for the hammer-top crop
crops = {'face_helm': (O, src2p(624, 440), (720, 760)), 'hammer_top_trim': (G1, None, (0, 760, 0, 600)),
         'boots': (O, src2p(540, 1290), (1500, 1100)), 'title': (O, None, (X0 - 40, X0 + tw + 40, Y0 - 76, Y0 + th + 220))}
hx, hy = src2p(405, 185); crops['hammer_top_trim'] = (G1, None, (hx - 400, hx + 400, 0, 560))
for nm, (img, c, sz) in crops.items():
    if c is None: xa, xb, ya, yb = sz
    else: xa, xb, ya, yb = c[0] - sz[0] // 2, c[0] + sz[0] // 2, c[1] - sz[1] // 2, c[1] + sz[1] // 2
    xa, ya = max(0, xa), max(0, ya); xb, yb = min(FW, xb), min(FH, yb)
    cv2.imwrite(D + 'crops/%s_100.png' % nm, img[ya:yb, xa:xb]); print('crop', nm, xa, xb, ya, yb)
