# ISSUE01-COVER-V17 art fit + title layer: identical pipeline to V16 (build_v16.py) on Sherif's eye-of-source-light render.
#  art  : src_v17.jpg (Grok Imagine, 1152x1728) -> 4x-UltraSharp (upscale.py) -> tone lock (consistency.py) -> one uniform
#         INTER_AREA scale to height 3150 -> centre crop to 2063. Untouched.
#  type : the V16 recoloured title layer (silver coin, silver-gold bolt, gold letters; ../v16/recolor_title_v16.py output),
#         scaled to F = 0.70 of its v10.1 print size (V16: 0.80), anchored at the same top-right safe corner.
#  run  : python3 upscale.py /workspace/models/4x-UltraSharp.pth src_v17.jpg up_x4_us_raw.png
#         python3 consistency.py up_x4_us_raw.png src_v17.jpg up_x4_us_bp.png
#         python3 build_v17.py && python3 build_final_v17.py
import cv2, numpy as np, sys
sys.path.insert(0, '/workspace/issue01/release'); import srgb
D = '/workspace/issue01/v17/'
FW, FH, BL, SF = 2063, 3150, 37, 75          # sheet w/ bleed, bleed px (0.125 in), safe inset from trim (0.25 in)
SAFE = BL + SF                               # 112 px from the sheet edge
F = float(sys.argv[1]) if len(sys.argv) > 1 else 0.70   # title scale (V17: 0.70, shrunk from 0.80 about the top-right anchor to clear the eye sigil's vertical beam) relative to its v10.1 print size
RM, TM = 4, 4                                # px between the layer's outermost (shadow) pixel and the right / top safe line

# ---------- art ----------
N = cv2.imread(D + 'src_v17.jpg'); h1, w1 = N.shape[:2]
U = cv2.imread(D + 'up_x4_us_bp.png'); assert U.shape[:2] == (h1 * 4, w1 * 4)
k = FH / U.shape[0]; W = round(U.shape[1] * k)
A = cv2.resize(U, (W, FH), interpolation=cv2.INTER_AREA); del U
cx = (W - FW) // 2; A = A[:, cx:cx + FW].copy()
print('art: scale %.5f of 4x (x%.4f vs source), %dx%d -> crop x %d..%d' % (k, k * 4, W, FH, cx, cx + FW))
srgb.save(D + 'art_v17_print_notext.png', A, dpi=300)

# ---------- type layer ----------
T = np.load('/workspace/issue01/v16/title_rgb_hires_v16.npy').astype(np.float32); a = np.load('/workspace/issue01/v16/title_a_hires_v16.npy').astype(np.float32)
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
cv2.imwrite(D + 'title_layer_v17.png', rgba)                 # separate full-sheet type layer (RGBA)
O = np.clip(A * (1 - L[..., None]) + LT * L[..., None] + .5, 0, 255).astype(np.uint8)
srgb.save(D + '_print_v17_titleonly.jpg', O, dpi=300, quality=97)
for t, nm in ((0.004, 'layer incl. soft shadow'), (0.5, 'glyphs + seal')):
    yy, xx = np.where(L > t)
    print('title %-24s x %d..%d y %d..%d | inside trim by L %d R %d T %d px | inside safe: %s' % (nm, xx.min(), xx.max(), yy.min(), yy.max(),
          xx.min() - BL, FW - 1 - BL - xx.max(), yy.min() - BL, xx.min() >= SAFE and xx.max() <= FW - 1 - SAFE and yy.min() >= SAFE))
print('title: F %.3f -> %.4f of hi-res layer, %dx%d px (%.2fx%.2f in) at x %d..%d y %d..%d' % (F, s, tw, th, tw / 300, th / 300, X0, X0 + tw - 1, Y0, Y0 + th - 1))

