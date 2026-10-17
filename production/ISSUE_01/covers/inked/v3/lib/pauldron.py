# Pauldron emblems: emerald Eye of Horus with gold-feathered wings, raised inlay with visible rim thickness, lit from the upper left.
# Right plate (viewer's right, frontal): enhanced in place (wings recoloured to gold feathers, gem eye, inlay rim, glow).
# Left plate (viewer's left, side-on): old emblem removed; Eye + ONE foreshortened wing warped on from the enhanced right emblem.
import numpy as np, cv2
GOLD_BGR = np.array([(14, 52, 96), (30, 104, 170), (60, 160, 224), (130, 214, 252), (200, 240, 255)], np.float32)
EMER_BGR = np.array([(22, 46, 6), (44, 96, 14), (70, 132, 22), (118, 196, 64), (210, 250, 190)], np.float32)   # emerald-tablet green
LIGHT = np.array([-0.6, -0.8])
# reference frame 2016x3024 (render3_storm at 1.75x). Emblem zones:
R_BOX = (1300, 1160, 1665, 1355)            # right emblem bbox
R_EYE = (1500, 1250)                         # right emblem iris centre (approx; refined from the image)
L_FACE = [(716, 1100), (780, 1092), (850, 1093), (905, 1104), (938, 1128), (900, 1152), (850, 1182), (800, 1216), (758, 1206), (737, 1160), (724, 1126)]

def green_mask(A):
    B, G, R = A[..., 0], A[..., 1], A[..., 2]
    return ((G > R + 12) & (G > B + 4)).astype(np.float32)

def ramp_map(t, ramp):
    t = np.clip(t, 0, 1) * (len(ramp) - 1); i = np.floor(t).astype(int).clip(0, len(ramp) - 2); f = (t - i)[..., None]
    return ramp[i] * (1 - f) + ramp[i + 1] * f

def inlay(roi, m, depth=3.0):
    """raised inlay: lit lip on edges facing the light, dark side wall + small cast shadow on the stone down-right."""
    mb = cv2.GaussianBlur(m, (0, 0), 1.2); gy, gx = np.gradient(mb)
    facing = -(gx * LIGHT[0] + gy * LIGHT[1])
    lip = np.clip(facing * 6, 0, 1) * (m > 0.3); wall = np.clip(-facing * 6, 0, 1) * (m > 0.3)
    sh = cv2.warpAffine(m, np.float32([[1, 0, depth * 0.8], [0, 1, depth]]), (m.shape[1], m.shape[0])); sh = cv2.GaussianBlur(sh, (0, 0), 1.5) * (1 - m)
    roi = roi * (1 - 0.55 * sh[..., None])
    roi = roi * (1 - 0.45 * wall[..., None])
    roi = roi + lip[..., None] * 70
    return roi

def enhance_right(A, sc=1.0, ox=0, oy=0):
    x0, y0, x1, y1 = [int(round(v * sc)) for v in R_BOX]; x0 += ox; x1 += ox; y0 += oy; y1 += oy
    roi = A[y0:y1, x0:x1].astype(np.float32).copy(); h, w = roi.shape[:2]
    g = green_mask(roi)
    # iris: darkest-saturated green blob centre near the expected eye position
    ex, ey = (R_EYE[0] * sc + ox - x0), (R_EYE[1] * sc + oy - y0)
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    near = (np.hypot(xx - ex, yy - ey) < 40 * sc) & (g > 0)
    if near.sum() > 20:
        sat = (roi[..., 1] - roi[..., 2]) * near; ys, xs = np.where(sat > np.percentile(sat[near], 70)); ex, ey = xs.mean(), ys.mean()
    eye_hw = 72 * sc
    # wing zones: green strips left/right of the eye, above the spiral/teardrop line
    wings = (g > 0) & (((xx < ex - eye_hw) & (yy < ey + 40 * sc)) | ((xx > ex + 36 * sc) & (yy > ey + 2 * sc) & (yy < ey + 48 * sc)))
    wings = cv2.morphologyEx(wings.astype(np.uint8), cv2.MORPH_OPEN, np.ones((2, 2), np.uint8)).astype(bool)
    lum = roi.max(2) / 255
    t = np.clip((lum - 0.18) / 0.62, 0, 1)
    # cel tones: 3 steps + highlight on the upper part of each feather strip
    tq = np.where(t > 0.72, 0.85, np.where(t > 0.42, 0.60, 0.32))
    gm = cv2.GaussianBlur(wings.astype(np.float32), (0, 0), 1.0); gy, gx = np.gradient(cv2.GaussianBlur(wings.astype(np.float32), (0, 0), 2.5))
    top = np.clip(-(gx * LIGHT[0] + gy * LIGHT[1]) * 8, 0, 1)
    gold = ramp_map(np.clip(tq + 0.25 * top, 0, 1), GOLD_BGR)
    roi = roi * (1 - gm[..., None]) + gold * gm[..., None]
    # eye parts stay emerald: deepen + clean the green into the emerald-tablet ramp
    em = (g > 0) & ~wings
    emf = cv2.GaussianBlur(em.astype(np.float32), (0, 0), 0.8)
    te = np.clip((lum - 0.08) / 0.75, 0, 1)
    emc = 0.35 * ramp_map(te, EMER_BGR) + 0.65 * roi                 # keep the original drawing, pull it to emerald-tablet green
    roi = roi * (1 - emf[..., None]) + emc * emf[..., None]
    # gem iris: radial cel shading + specular + soft glow
    r = np.hypot(xx - ex, yy - ey); ir = 20 * sc
    gem = np.clip(ir - r + 0.5, 0, 1)
    d = ((xx - ex) * LIGHT[0] + (yy - ey) * LIGHT[1]) / ir                  # +1 toward the light
    gt = np.where(d > 0.35, 0.80, np.where(d > -0.3, 0.55, 0.30))
    roi = roi * (1 - gem[..., None]) + ramp_map(gt, EMER_BGR) * gem[..., None]
    ring = np.clip(1.6 * sc - np.abs(r - ir), 0, 1); roi = roi * (1 - ring[..., None]) + np.array([8, 10, 6]) * ring[..., None]
    spec = np.clip(5 * sc - np.hypot(xx - (ex - 7 * sc), yy - (ey - 8 * sc)) + 0.5, 0, 1); roi = roi * (1 - spec[..., None]) + 255 * spec[..., None]
    spec2 = np.clip(2.2 * sc - np.hypot(xx - (ex + 7 * sc), yy - (ey + 7 * sc)) + 0.5, 0, 1) * 0.7; roi = roi * (1 - spec2[..., None]) + EMER_BGR[4] * spec2[..., None]
    # inlay rim thickness on the whole emblem
    allm = cv2.dilate(((g > 0) | wings).astype(np.uint8), np.ones((3, 3), np.uint8)).astype(np.float32)
    roi = inlay(roi, allm, 3.0 * sc)
    # emerald glow (eye only) - screen
    glow = cv2.GaussianBlur(emf + gem, (0, 0), 9 * sc) * 0.30
    roi = 255 - (255 - roi) * (1 - np.clip(glow, 0, 1)[..., None] * (EMER_BGR[2] / 255))
    out = A.copy(); out[y0:y1, x0:x1] = roi.clip(0, 255)
    return out, (x0, y0, x1, y1), (ex + x0, ey + y0)

def left_plate(A, src, eye_src, sc=1.0, ox=0, oy=0):
    """src = enhanced page (for the right emblem). Paint out the old left emblem, then warp Eye + left wing on."""
    H, W = A.shape[:2]
    face = np.zeros((H, W), np.uint8); cv2.fillPoly(face, [np.array([(ox + x * sc, oy + y * sc) for x, y in L_FACE], np.int32)], 255)
    fx0, fy0, fw, fh = cv2.boundingRect(face); fx1, fy1 = fx0 + fw, fy0 + fh
    pad = 12; X0, Y0, X1, Y1 = fx0 - pad, fy0 - pad, fx1 + pad, fy1 + pad
    roi = A[Y0:Y1, X0:X1].astype(np.float32).copy(); fm = face[Y0:Y1, X0:X1].astype(np.float32) / 255
    # 1) remove the old emblem: inpaint green (+ its ink) inside the face, then add the plate's stone grain back
    g = green_mask(roi) * fm
    gk = cv2.dilate((g > 0).astype(np.uint8) * 255, np.ones((13, 13), np.uint8))
    clean = cv2.inpaint(roi.clip(0, 255).astype(np.uint8), gk, 5, cv2.INPAINT_TELEA).astype(np.float32)
    gray = cv2.cvtColor(roi.clip(0, 255).astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)
    stone = np.median(roi[(fm > 0.5) & (roi.max(2) < 70) & (gk == 0)], axis=0)
    yy, xx = np.mgrid[0:roi.shape[0], 0:roi.shape[1]].astype(np.float32)
    shade = 1.15 - 0.35 * np.clip((xx / roi.shape[1]) * 0.4 + (yy / roi.shape[0]) * 0.6, 0, 1)     # side-on plate lit from upper left
    noise = cv2.GaussianBlur(np.random.default_rng(7).standard_normal(roi.shape[:2]).astype(np.float32), (0, 0), 1.0) * 5
    stone_fill = stone[None, None] * shade[..., None] + noise[..., None]
    a = cv2.GaussianBlur((gk > 0).astype(np.float32), (0, 0), 1.5)[..., None] * fm[..., None]
    roi = roi * (1 - a) + (0.15 * clean + 0.85 * stone_fill) * a
    # 2) source: enhanced right emblem = Eye + its LEFT wing + teardrop/spiral (the right wing is hidden by the plate's turn)
    ex, ey = eye_src
    sx0, sy0, sx1, sy1 = int(ex - 78 * sc), int(ey - 75 * sc), int(ex + 92 * sc), int(ey + 95 * sc)
    S = src[sy0:sy1, sx0:sx1].astype(np.float32); gS = green_mask(A[sy0:sy1, sx0:sx1].astype(np.float32))
    # emblem alpha: original green (eye + wings) + ink around it
    am = cv2.morphologyEx((gS > 0).astype(np.uint8), cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (int(15 * sc) | 1,) * 2))
    am = cv2.dilate(am, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (int(7 * sc) | 1,) * 2)).astype(np.float32)
    am = cv2.GaussianBlur(am, (0, 0), 0.8)
    sh, sw = S.shape[:2]
    # 3) perspective: eye lands on the frontal part of the face, wing compresses toward the outer (left) side and curves down
    e_dst = np.array([ox + 840 * sc, oy + 1128 * sc])
    k = 0.68                                                          # overall scale onto the smaller, side-on plate
    eu, ev = ex - sx0, ey - sy0
    src_q = np.float32([[0, 0], [sw, 0], [sw, sh], [0, sh]])
    def D(u, v):                                                      # src (u,v) -> dst, with left-side foreshortening (x compressed + drops)
        du, dv = (u - eu) * k, (v - ev) * k
        if du < 0: du = du * 0.70; dv = dv * 0.85 + (-du) * 0.42      # wing side turns away: narrower and droops with the curve
        return e_dst + np.array([du, dv * 0.92])
    dst_q = np.float32([D(0, 0), D(sw, 0), D(sw, sh), D(0, sh)])
    M = cv2.getPerspectiveTransform(src_q, (dst_q - np.float32([X0, Y0])).astype(np.float32))
    Sw = cv2.warpPerspective(S, M, (roi.shape[1], roi.shape[0]), flags=cv2.INTER_CUBIC)
    Aw = cv2.warpPerspective(am, M, (roi.shape[1], roi.shape[0]), flags=cv2.INTER_LINEAR)
    # occlusion: emblem only on the face; slightly darker toward the side that turns away; wing tip clipped by the rim = 'curving around'
    Aw = Aw * cv2.GaussianBlur(fm, (0, 0), 1.0)
    turn = np.clip(1.0 - 0.30 * np.clip((e_dst[0] - X0 - xx) / (70 * sc), 0, 1), 0.7, 1)[..., None]
    roi = roi * (1 - Aw[..., None]) + (Sw * turn) * Aw[..., None]
    # inked gold wing: 5 stacked feathers from the eye's inner corner sweeping to the plate's turned-away side, drooping with the curve
    SS = 4; Hh, Ww = roi.shape[:2]
    ink = np.zeros((Hh * SS, Ww * SS), np.uint8); fil = np.zeros_like(ink)
    root = e_dst - np.float32([X0, Y0]) + np.float32([-30 * sc, -12 * sc])
    feathers = []
    for i in range(5):
        L = (112 - 13 * i) * sc; th0 = (14.0 - 0.8 * i) * sc; r0 = root + np.float32([4 * i * sc, 9.0 * i * sc])
        pts_top, pts_bot = [], []
        for t in np.linspace(0, 1, 28):
            x = r0[0] - L * t * (1 - 0.10 * t); y = r0[1] + L * (0.06 + 0.05 * i) * t + L * 0.42 * t ** 2.0      # droops as it wraps
            th = th0 * (1 - 0.55 * t ** 1.5)
            pts_top.append((x, y - th / 2)); pts_bot.append((x, y + th / 2))
        poly = np.array(pts_top + [(pts_top[-1][0] - 5 * sc, pts_top[-1][1] + th0 * 0.3)] + pts_bot[::-1], np.float32)
        feathers.append(poly)
    allink = np.zeros((Hh, Ww), np.float32)
    for i, poly in list(enumerate(feathers))[::-1]:                    # back (lowest) feather first, each overlaps the one below
        ik = np.zeros((Hh * SS, Ww * SS), np.uint8); fl = np.zeros_like(ik); p = (poly * SS).astype(np.int32)
        cv2.fillPoly(ik, [p], 255, cv2.LINE_AA); cv2.polylines(ik, [p], True, 255, int(1.9 * sc * SS) * 2 + 1, cv2.LINE_AA)
        cv2.fillPoly(fl, [p], 255, cv2.LINE_AA)
        ik = cv2.resize(ik.astype(np.float32) / 255, (Ww, Hh), interpolation=cv2.INTER_AREA) * fm * (1 - Aw)
        fl = cv2.resize(fl.astype(np.float32) / 255, (Ww, Hh), interpolation=cv2.INTER_AREA)
        fb = cv2.GaussianBlur(fl, (0, 0), 2.0); gy, gx = np.gradient(fb); lit = -(gx * LIGHT[0] + gy * LIGHT[1])
        tone = np.where(lit > 0.004, 0.94, np.where(lit < -0.02, 0.58, 0.74)) * (1 - 0.15 * np.clip((root[0] - xx) / (110 * sc), 0, 1))
        fl = cv2.erode(fl, np.ones((2, 2), np.uint8)) * fm * (1 - Aw)
        roi = roi * (1 - ik[..., None]) + np.array([8, 7, 6], np.float32) * ik[..., None]
        roi = roi * (1 - fl[..., None]) + ramp_map(tone, GOLD_BGR) * fl[..., None]
        allink = np.maximum(allink, ik)
    ink = allink
    wsil = cv2.morphologyEx(((ink > 0.5) * (fm > 0.5)).astype(np.uint8), cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)))
    roi = inlay(roi, np.clip((Aw > 0.5) + wsil, 0, 1).astype(np.float32), 2.4 * sc)
    out = A.copy(); out[Y0:Y1, X0:X1] = roi.clip(0, 255)
    return out, (X0, Y0, X1, Y1)

def apply(A, sc=1.0, ox=0, oy=0):
    E, rb, eye = enhance_right(A, sc, ox, oy)
    E2, lb = left_plate(E, E, eye, sc, ox, oy)
    return E2, rb, lb
