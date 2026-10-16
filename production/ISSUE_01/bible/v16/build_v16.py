# ISSUE01-COVER-V16 print-cover VARIANT: identical pipeline to V15 (build_v15.py) on the white-lightning render.
#  art  : src_v16.jpg (Sherif's white/silver-lightning Grok Imagine render, 1152x1728) -> 4x-UltraSharp (upscale.py)
#         -> tone lock (consistency.py) -> one uniform INTER_AREA scale to height 3150 -> centre crop to 2063. Untouched.
#  type : V15 title layer recoloured by recolor_title_v16.py (lettering layer only): ISSUE #1 seal silver, RA-THOR bolt
#         silver body + gold bevel rim + gold tip, divider bolt silver/gold; all letters gold, bit-exact to V15.
#  run  : python3 upscale.py /workspace/models/4x-UltraSharp.pth src_v16.jpg up_x4_us_raw.png
#         python3 consistency.py up_x4_us_raw.png src_v16.jpg up_x4_us_bp.png
#         python3 recolor_title_v16.py 12 b 1.1 && python3 build_v16.py
import cv2, numpy as np, sys
sys.path.insert(0, '/workspace/issue01/release'); import srgb
D = '/workspace/issue01/v16/'
FW, FH, BL, SF = 2063, 3150, 37, 75          # sheet w/ bleed, bleed px (0.125 in), safe inset from trim (0.25 in)
SAFE = BL + SF                               # 112 px from the sheet edge
F = float(sys.argv[1]) if len(sys.argv) > 1 else 0.80   # title scale relative to its v10.1 print size
RM, TM = 4, 4                                # px between the layer's outermost (shadow) pixel and the right / top safe line

# ---------- art ----------
N = cv2.imread(D + 'src_v16.jpg'); h1, w1 = N.shape[:2]
U = cv2.imread(D + 'up_x4_us_bp.png'); assert U.shape[:2] == (h1 * 4, w1 * 4)
k = FH / U.shape[0]; W = round(U.shape[1] * k)
A = cv2.resize(U, (W, FH), interpolation=cv2.INTER_AREA); del U
cx = (W - FW) // 2; A = A[:, cx:cx + FW].copy()
print('art: scale %.5f of 4x (x%.4f vs source), %dx%d -> crop x %d..%d' % (k, k * 4, W, FH, cx, cx + FW))
srgb.save(D + 'art_v16_print_notext.png', A, dpi=300)

# ---------- type layer ----------
T = np.load(D + 'title_rgb_hires_v16.npy').astype(np.float32); a = np.load(D + 'title_a_hires_v16.npy').astype(np.float32)
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
cv2.imwrite(D + 'title_layer_v16.png', rgba)                 # separate full-sheet type layer (RGBA)
O = np.clip(A * (1 - L[..., None]) + LT * L[..., None] + .5, 0, 255).astype(np.uint8)
srgb.save(D + 'print_v16.jpg', O, dpi=300, quality=97)
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
srgb.save(D + 'print_v16_guides.jpg', G, dpi=300, quality=92)

# ---------- preview + 100% crops ----------
P = cv2.resize(O, (620, round(FH * 620 / FW)), interpolation=cv2.INTER_AREA)
srgb.save(D + 'preview_620.jpg', P, dpi=72, quality=92)
P15 = cv2.imread('/workspace/issue01/v15/preview_620.jpg'); gap = np.full((P.shape[0], 16, 3), 255, np.uint8)
srgb.save(D + 'compare_v15_v16_620.jpg', np.hstack([P15, gap, P]), dpi=72, quality=92)
def src2p(x, y): return round(x * FH / h1 - cx), round(y * FH / h1)
G1 = O.copy(); rect(G1, BL, (0, 0, 255), 1); rect(G1, SAFE, (255, 255, 0), 1)   # 1 px lines for the hammer-top crop
hx, hy = src2p(405, 185)
CX, CY = X0 + round((2227.2 - x0) * s), Y0 + round((240.5 - y0) * s); CR = round(222 * s) + 30
BX0, BY0, BX1, BY1 = X0 + round((1271 - x0) * s), Y0 + round((38 - y0) * s), X0 + round((1429 - x0) * s), Y0 + round((356 - y0) * s)
crops = {'title': (O, (X0 - 40, X0 + tw + 40, Y0 - 76, Y0 + th + 220)),
         'coin': (O, (CX - CR, CX + CR, CY - CR, CY + CR)),
         'bolt': (O, (BX0 - 60, BX1 + 60, BY0 - 40, BY1 + 60)),
         'face_helm': (O, (src2p(624, 440)[0] - 360, src2p(624, 440)[0] + 360, src2p(624, 440)[1] - 380, src2p(624, 440)[1] + 380)),
         'hammer_top_trim': (G1, (hx - 400, hx + 400, 0, 560))}
for nm, (img, (xa, xb, ya, yb)) in crops.items():
    xa, ya = max(0, xa), max(0, ya); xb, yb = min(FW, xb), min(FH, yb)
    srgb.save(D + 'crops/%s_100.jpg' % nm, img[ya:yb, xa:xb], dpi=300, quality=95); print('crop', nm, xa, xb, ya, yb)

# ---------- clearances ----------
Af = A.astype(np.int16); warm = ((Af[..., 2] - Af[..., 0]) > 25) & (Af[..., 2] > 50)
lumA = A.mean(2)
# hammer head = the warm-metal component under the hammer, restricted to the head box (left of the title)
hz = np.zeros_like(warm); hz[:620, max(0, hx - 450):hx + 330] = True
n, lab, st, _ = cv2.connectedComponentsWithStats((warm & hz).astype(np.uint8), connectivity=8)
keep = np.isin(lab, [i for i in range(1, n) if st[i, 4] > 300]); hm = keep
top = np.where(keep.any(1))[0].min(); hcols = np.where(keep[top])[0]
ax = int(hcols.mean()); rim = top
while rim > 0 and lumA[rim - 1, ax - 6:ax + 6].max() > 150: rim -= 1          # bright edge highlight sitting on the apex
print('hammer apex: metal y %d (x~%d) -> %d px inside trim (%+d vs safe line); incl. its bright rim highlight y %d -> %d px inside trim (%+d vs safe)' % (
      top, ax, top - BL, top - SAFE, rim, rim - BL, rim - SAFE))
yy, xx = np.where(L > 0.004); ty1 = yy.max(); tx0 = xx.min()
wz = warm.copy(); wz[:ty1 + 1] = False; wz[:, :tx0 - 200] = False
n2, lab2, st2, _ = cv2.connectedComponentsWithStats(wz[:1100].astype(np.uint8), connectivity=8)
big2 = [i for i in range(1, n2) if st2[i, 4] > 1500]
if big2:
    i = min(big2, key=lambda i: st2[i, 1]); print('nearest warm figure element below title (halo/wings): top y %d, x %d..%d -> %d px below title layer bottom (%d)' % (st2[i, 1], st2[i, 0], st2[i, 0] + st2[i, 2], st2[i, 1] - ty1, ty1))
hr = np.where(hm[:ty1 + 1].any(0))[0].max(); print('hammer head right edge (rows <= title bottom) x %d vs title layer left x %d -> horizontal gap %d px' % (hr, tx0, tx0 - hr))
white = (lumA > 185) & ((A.max(2).astype(int) - A.min(2)) < 45)
gl = L > 0.5; band = (L > 0.004)
print('white-lightning pixels behind title: under glyph/seal pixels %d (%.2f%%), within layer incl. shadow %d' % ((white & gl).sum(), 100 * (white & gl).mean() / max(gl.mean(), 1e-9), (white & band).sum()))
ys2, xs2 = np.where(white[:Y0 + th + 150, X0 - 150:]); print('white lightning bbox near title: x %d..%d y %d..%d' % (xs2.min() + X0 - 150, xs2.max() + X0 - 150, ys2.min(), ys2.max()) if len(xs2) else 'no white lightning near title')
cv2.imwrite(D + '_white_under_title.png', np.dstack([white * 255, gl * 120, band * 60]).astype(np.uint8)[: Y0 + th + 200, X0 - 200:])
