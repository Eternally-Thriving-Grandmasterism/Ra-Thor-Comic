# v15 lettering-layer cleanup: remove the two stray gold lightning flecks baked into the locked title layer
# (left of LIVING THUNDER; under the ISSUE #1 seal). Glyphs, ornament rules and the seal itself are untouched.
import numpy as np, cv2
D = '/workspace/issue01/'
T = np.load(D + 'v11/title_rgb_hires.npy').astype(np.float32); a = np.load(D + 'v11/title_a_hires.npy').astype(np.float32)
H, W = a.shape; yy, xx = np.mgrid[:H, :W]
# 1) left fleck: lightning stub + loose dashes below/left of the LIVING THUNDER rules -> fade alpha to 0 (feathered)
box = np.zeros((H, W), np.float32)
box[412:492, 950:1132] = 1; box[395:492, 950:1016] = 1; box[432:492, 1130:1185] = 1
box = cv2.GaussianBlur(box, (0, 0), 2.5)
a_new = a * (1 - box)
# 2) under-seal fleck: bright streaks in the seal's opaque dark outer band -> recolour from the surrounding dark band
seal = (a > 0.98) & (xx > 2050)
pts = np.argwhere(seal)[:, ::-1].astype(np.float32); (cx, cy), r = cv2.minEnclosingCircle(pts)
lum = T.max(2)
gold = (lum > 120) & (np.hypot(xx - cx, yy - cy) < r - 2)
# the gold rim ends at r~186 along the bottom; the band r 189..disc edge is the seal's dark drop-shadow crescent
rg = 185.0
R = np.hypot(xx - cx, yy - cy)
band = (R > 192) & (R < r - 4) & (yy > cy + 120) & ~((xx > 2110) & (xx < 2280))
fill = np.median(T[band], axis=0)                      # the crescent's own dark colour
m = ((xx > 2115) & (xx < 2275) & (yy > 395) & (yy < 470) & (R > rg)).astype(np.float32)
m = cv2.GaussianBlur(m, (0, 0), 2.0) * (R > rg - 1.5)
T_new = T * (1 - m[..., None]) + fill[None, None, :] * m[..., None]
print('seal centre (%.1f,%.1f) r %.1f, gold rim r %.1f, band fill px %d, left-fleck alpha removed %.0f' % (cx, cy, r, rg, (m>0.5).sum(), (a - a_new).sum()))
np.save(D + 'v15/title_rgb_hires_v15.npy', T_new.astype(np.float16)); np.save(D + 'v15/title_a_hires_v15.npy', a_new.astype(np.float16))
bg = np.zeros_like(T); bg[..., 1] = 90
for nm, (TT, aa) in {'before': (T, a), 'after': (T_new, a_new)}.items():
    C = (bg * (1 - aa[..., None]) + TT * aa[..., None]).astype(np.uint8)
    cv2.imwrite(D + 'v15/_cl2_%s_L.png' % nm, cv2.resize(C[360:500, 920:1200], None, fx=2, fy=2))
    cv2.imwrite(D + 'v15/_cl2_%s_R.png' % nm, cv2.resize(C[330:500, 2000:2460], None, fx=2, fy=2))
