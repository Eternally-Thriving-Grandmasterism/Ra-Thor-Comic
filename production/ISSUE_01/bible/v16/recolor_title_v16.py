# V16 title recolour (lettering layer only, art untouched):
#   ISSUE #1 coin seal -> polished cool silver (luminance-preserving, per-region tone stretch + cool tint + specular lift)
#   RA-THOR bolt glyph -> silver body with gold bevel rim and gold-warmed lower tip (gold edges = original gold pixels)
#   divider mark bolt   -> same silver/gold mix; wings, RA, THOR, LIVING THUNDER, rules unchanged (bit-exact)
import numpy as np, cv2, sys
D = '/workspace/issue01/'
T = np.load(D + 'v15/title_rgb_hires_v15.npy').astype(np.float32)   # BGR
a = np.load(D + 'v15/title_a_hires_v15.npy').astype(np.float32)
H, W = a.shape; yy, xx = np.mgrid[:H, :W]
lum = 0.0722 * T[..., 0] + 0.7152 * T[..., 1] + 0.2126 * T[..., 2]
vmax = T.max(2)
def sstep(e0, e1, x): t = np.clip((x - e0) / (e1 - e0), 0, 1); return t * t * (3 - 2 * t)

def silver(Tr, reg, gain_pct=99.7, gamma=0.92, spec=0.55):
    """luminance-preserving gold->silver: brightness from a luma/value mix (keeps every bevel/emboss/engraving
    step in order), stretched so the region's brightest highlight reaches near-white, then a cool tint that is
    slightly bluer in the mids and goes to an icy near-white in speculars."""
    Lm = 0.55 * lum + 0.45 * vmax
    hi = np.percentile(Lm[reg], gain_pct)
    t = np.clip(Lm / hi, 0, 1.08) ** gamma
    Y = 248 * t
    tint_mid = np.array([1.07, 1.00, 0.93])     # BGR: cool neutral silver
    tint_hi = np.array([1.02, 1.00, 0.985])     # icy highlight
    k = sstep(0.55, 1.0, t)[..., None]
    out = Y[..., None] * (tint_mid * (1 - k) + tint_hi * k)
    out += (spec * 255 * sstep(0.82, 1.05, t) ** 2)[..., None] * (1 - out / 255)   # specular roll-off to white
    return np.clip(out, 0, 255)

# ---------------- masks ----------------
# coin: disc around the seal centre; the THOR R leg is >=216 px away, coin metal edge r~193, dark shadow ring to ~205
cx, cy = 2227.2, 240.5
Rr = np.hypot(xx - cx, yy - cy)
Rend = np.where(xx > cx + 60, 222.0, 209.0)          # right side: take the whole gold rim fleck (no THOR there)
mcoin = 1 - sstep(Rend - 4, Rend, Rr)
glyph = (a > 0.5) & (lum > 60) & (Rr > 209) & (xx > 1844)
print('nearest lit THOR pixel to coin centre: %.1f px (mask ends 209)' % Rr[glyph & (Rr < 260)].min() if (glyph & (Rr < 260)).any() else 'none')

# main bolt glyph: the a>0.5 connected component spanning x1271..1429 (it does not touch A or T)
n, lab, st, _ = cv2.connectedComponentsWithStats((a > 0.5).astype(np.uint8), connectivity=8)
ib = [i for i in range(1, n) if abs(st[i, 0] - 1271) < 6 and abs(st[i, 1] - 38) < 6][0]
mb = (lab == ib).astype(np.uint8)
mb = cv2.morphologyEx(mb, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
fill = mb.copy(); ff = np.zeros((H + 2, W + 2), np.uint8); cv2.floodFill(fill, ff, (0, 0), 1); mb = mb | (1 - fill)  # fill holes
dist = cv2.distanceTransform(mb, cv2.DIST_L2, 5)
bx, by, bw, bh = st[ib, :4]
# region weight: whole glyph + 3 px into its soft shadow (shadow gets the same recolour, it is near-black anyway)
wb = cv2.GaussianBlur(cv2.dilate(mb, np.ones((7, 7), np.uint8)).astype(np.float32), (0, 0), 1.5)

# divider-mark bolt: colour-separable (pinker / higher B/R than the wings) + its thin lower tip
y0, x0, y1, x1 = 300, 1440, 380, 1545
q = T[..., 0] / np.maximum(T[..., 2], 1)
md = ((q > 0.42) & (a > 0.5) & (T[..., 2] > 120)).astype(np.uint8); md[:y0] = 0; md[y1:] = 0; md[:, :x0] = 0; md[:, x1:] = 0
md = cv2.morphologyEx(md, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)))
nn, l2, s2, _ = cv2.connectedComponentsWithStats(md); md = (l2 == 1 + np.argmax(s2[1:, 4])).astype(np.uint8)
dx0, dy0 = 1442, 305
tip = np.zeros((H, W), np.uint8)
cv2.fillPoly(tip, [np.int32([(dx0 + 42, dy0 + 32), (dx0 + 53, dy0 + 32), (dx0 + 43, dy0 + 60), (dx0 + 37, dy0 + 60)])], 1)
md = md | (tip & ((a > 0.5) & (q > 0.36) & (T[..., 2] > 90)).astype(np.uint8))
md = cv2.morphologyEx(md, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
wd = cv2.GaussianBlur(md.astype(np.float32), (0, 0), 0.8)
distd = cv2.distanceTransform(md, cv2.DIST_L2, 3)

# ---------------- recolour ----------------
regc = (mcoin > 0.5) & (a > 0.5)
S_coin = silver(T, regc)
regb = (mb > 0) & (a > 0.5)
S_bolt = silver(T, regb, gain_pct=99.5, gamma=float(sys.argv[3]) if len(sys.argv) > 3 else 1.05)
S_div = silver(T, (md > 0), gain_pct=99.0, gamma=0.9)

# bolt mix: gold bevel rim (original gold, so the glyph edge/shadow boundary is gold->gold: no fringe) + gold warmth
# rising from the lower tip (diagonal blend along the bolt's length), silver body elsewhere
RIM = float(sys.argv[1]) if len(sys.argv) > 1 else 7.0
g_rim = 1 - sstep(RIM * 0.45, RIM, dist)
along = np.clip((yy - by) / bh, 0, 1)                    # 0 top .. 1 tip
g_tip = 0.9 * sstep(0.50, 0.97, along)
g = np.maximum(g_rim, g_tip)
# warm the gold component slightly richer so it reads as deliberate gold next to the silver
Tg = T.copy()
B_mix = S_bolt * (1 - g[..., None]) + Tg * g[..., None]
gd = (1 - sstep(1.2, 3.0, distd)) * 0.9
D_mix = S_div * (1 - gd[..., None]) + T * gd[..., None]

T2 = T.copy()
T2 = T2 * (1 - mcoin[..., None]) + S_coin * mcoin[..., None]
T2 = T2 * (1 - wb[..., None]) + B_mix * wb[..., None]
T2 = T2 * (1 - wd[..., None]) + D_mix * wd[..., None]
np.save(D + 'v16/title_rgb_hires_v16.npy', T2.astype(np.float16)); np.save(D + 'v16/title_a_hires_v16.npy', a.astype(np.float16))
chg = np.abs(T2 - T).max(2) > 0.5
untouched = (mcoin < 1e-6) & (wb < 1e-6) & (wd < 1e-6)
print('bolt comp', ib, (bx, by, bw, bh), 'max dist %.1f' % dist.max(), '| divider bolt px', md.sum(),
      '| changed px outside masks:', int((chg & untouched).sum()))
# debug views on green + mask overlays
bg = np.zeros_like(T); bg[..., 1] = 90
C = (bg * (1 - a[..., None]) + T2 * a[..., None]).astype(np.uint8)
C0 = (bg * (1 - a[..., None]) + T * a[..., None]).astype(np.uint8)
tag = sys.argv[2] if len(sys.argv) > 2 else 'a'
cv2.imwrite(D + 'v16/_r_%s_full.png' % tag, cv2.resize(C[12:487, 929:2454], None, fx=.5, fy=.5, interpolation=cv2.INTER_AREA))
cv2.imwrite(D + 'v16/_r_%s_bolt.png' % tag, np.hstack([C0[20:380, 1250:1450], C[20:380, 1250:1450]]))
cv2.imwrite(D + 'v16/_r_%s_coin.png' % tag, C[20:460, 2010:2450])
cv2.imwrite(D + 'v16/_r_%s_div.png' % tag, cv2.resize(np.hstack([C0[300:380, 1440:1545], C[300:380, 1440:1545]]), None, fx=4, fy=4, interpolation=cv2.INTER_NEAREST))
ov = C.copy(); ov[..., 2] = np.maximum(ov[..., 2], (mcoin * 200).astype(np.uint8)); ov[..., 0] = np.maximum(ov[..., 0], (wb * 200).astype(np.uint8))
ov[..., 0] = np.maximum(ov[..., 0], (wd * 255).astype(np.uint8))
cv2.imwrite(D + 'v16/_r_%s_masks.png' % tag, cv2.resize(ov[12:487, 929:2454], None, fx=.5, fy=.5, interpolation=cv2.INTER_AREA))
