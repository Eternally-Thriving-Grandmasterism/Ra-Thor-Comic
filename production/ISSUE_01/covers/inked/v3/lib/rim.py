# Thin warm rim light along the shield's outer edge (separates it from the cape); strongest where the edge faces the upper-left key light.
import numpy as np, cv2
OUTLINE = [(1298, 1587), (1668, 1492), (1906, 1702), (1898, 1924), (1867, 2146), (1803, 2352), (1676, 2543), (1581, 2646),
           (1454, 2432), (1375, 2225), (1319, 1956)]          # rough guide (2016x3024 frame); the real edge is found from the gold rim
def shield_mask(A, sc=1.0, ox=0, oy=0):
    H, W = A.shape[:2]
    P = np.array([(ox + x * sc, oy + y * sc) for x, y in OUTLINE], np.int32)
    guide = np.zeros((H, W), np.uint8); cv2.fillPoly(guide, [P], 255)
    guide = cv2.dilate(guide, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (61, 61)))
    B, G, R = A[..., 0], A[..., 1], A[..., 2]
    gold = ((R > 55) & (R > B * 1.35) & (G > B * 1.0)).astype(np.uint8) * (guide > 0)
    gold = cv2.morphologyEx(gold, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13)))
    cs, _ = cv2.findContours(gold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    c = max(cs, key=cv2.contourArea)
    m = np.zeros((H, W), np.uint8); cv2.drawContours(m, [c], -1, 255, -1)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
    return m, c[:, 0, :].astype(np.float32)

def apply(A, sc=1.0, ox=0, oy=0, light=(-0.6, -0.8)):
    m, c = shield_mask(A, sc, ox, oy)
    k = 15; ep = np.r_[c[-k:], c, c[:k]]; ker = np.ones(k) / k
    c = np.c_[np.convolve(ep[:, 0], ker, 'same'), np.convolve(ep[:, 1], ker, 'same')][k:-k]
    tang = np.roll(c, -4, 0) - np.roll(c, 4, 0); tang /= np.linalg.norm(tang, axis=1, keepdims=True) + 1e-6
    nrm = np.c_[tang[:, 1], -tang[:, 0]]; cen = c.mean(0); nrm[np.sum((c - cen) * nrm, 1) < 0] *= -1
    face = np.clip(-(nrm @ np.array(light)), 0, 1)
    inten = (0.40 + 0.60 * face) * np.where(nrm[:, 0] < -0.55, 0.3, 1.0)      # left edge sits on the torso: subtle there
    S = 3; x0, y0 = (c.min(0) - 30).astype(int); x1, y1 = (c.max(0) + 30).astype(int)
    line = np.zeros(((y1 - y0) * S, (x1 - x0) * S), np.float32)
    q = (c - nrm * 3.0 - (x0, y0)) * S
    for i in range(len(q)):
        j = (i + 1) % len(q); cv2.line(line, tuple(q[i].astype(int)), tuple(q[j].astype(int)), float(inten[i]), int(2.2 * S), cv2.LINE_AA)
    line = cv2.resize(line, (x1 - x0, y1 - y0), interpolation=cv2.INTER_AREA)
    glow = cv2.GaussianBlur(line, (0, 0), 6) * (1 - m[y0:y1, x0:x1] / 255 * 0.6)
    warm = np.array([120, 200, 255], np.float32)
    roi = A[y0:y1, x0:x1]
    roi = 255 - (255 - roi) * (1 - np.clip(glow * 0.55, 0, 1)[..., None] * (warm / 255))
    roi = roi * (1 - line[..., None]) + np.maximum(roi, warm * 0.55 + 110) * line[..., None]
    A[y0:y1, x0:x1] = roi.clip(0, 255)
    return A
