import cv2, numpy as np
PANEL = [(318, 366), (398, 350), (366, 522), (266, 535)]       # end-face inner panel, 2016x3024 reference frame of render3_storm
def fix_hammer(A, ox, oy, sc):
    """repaint the hammer's narrow striking-end panel as plain cracked black stone (no bolt)."""
    pts = np.array([(ox + x * sc, oy + y * sc) for x, y in PANEL], np.float32)
    x0, y0 = pts.min(0).astype(int) - 20; x1, y1 = pts.max(0).astype(int) + 20
    roi = A[y0:y1, x0:x1].astype(np.float32); h, w = roi.shape[:2]
    m = np.zeros((h * 4, w * 4), np.uint8); cv2.fillPoly(m, [((pts - (x0, y0)) * 4).astype(np.int32)], 255)
    m = cv2.resize(m, (w, h), interpolation=cv2.INTER_AREA).astype(np.float32) / 255
    # texture source: a clean strip of cracked stone on the broad face (right of its bolt), luminance detail only
    sx0, sy0, sx1, sy1 = [int(round(v * sc)) for v in (648, 385, 724, 640)]
    src = cv2.cvtColor(A[oy + sy0:oy + sy1, ox + sx0:ox + sx1].clip(0, 255).astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)
    src = cv2.resize(src, (w, h), interpolation=cv2.INTER_CUBIC)
    hp = (src - cv2.GaussianBlur(src, (0, 0), 5 * sc))[..., None]
    # stone value: the end face stone tone from the original panel's dark pixels
    lum = roi.max(2); sel = (m > 0.9) & (lum < 90)
    tone = np.median(roi[sel], axis=0) if sel.sum() > 50 else np.array([38, 40, 42], np.float32)
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    # key light upper-left: brighter toward top-left of the face, falling off to lower-right; warm lightning bounce
    t = np.clip((xx / w * 0.5 + yy / h * 0.5), 0, 1)
    shade = (1.28 - 0.45 * t)[..., None]
    warm = np.array([0.97, 1.0, 1.04], np.float32)                   # BGR: slight warm tint from the bolt glow
    fill = tone[None, None] * shade * warm + hp * 0.9
    # inner edge occlusion: darken just inside the panel's ink border so the face sits recessed in its rim
    edge = cv2.GaussianBlur(m, (0, 0), 3 * sc); occ = np.clip((1 - edge) * 2.2, 0, 1)[..., None] * (m[..., None] > 0)
    fill = fill * (1 - 0.55 * occ)
    # a few inked cracks (same hand as the broad face): polylines in panel-relative coords (u along top edge, v down)
    P0, P1, P3 = pts[0] - (x0, y0), pts[1] - (x0, y0), pts[3] - (x0, y0)
    def uv(u, v): return P0 + (P1 - P0) * u + (P3 - P0) * v
    cracks = [[(0.0, 0.30), (0.22, 0.34), (0.35, 0.47), (0.58, 0.50), (0.70, 0.62)], [(0.35, 0.47), (0.30, 0.66), (0.42, 0.86), (0.40, 1.0)],
              [(0.58, 0.50), (0.80, 0.40), (1.0, 0.43)], [(0.15, 0.0), (0.20, 0.14), (0.12, 0.22)], [(0.70, 0.62), (0.88, 0.80), (0.86, 1.0)]]
    cm = np.zeros((h * 4, w * 4), np.uint8)
    for c in cracks: cv2.polylines(cm, [(np.array([uv(u, v) for u, v in c]) * 4).astype(np.int32)], False, 255, max(4, int(5 * sc)), cv2.LINE_AA)
    cm = cv2.resize(cm, (w, h), interpolation=cv2.INTER_AREA).astype(np.float32)[..., None] / 255 * m[..., None]
    fill = fill * (1 - 0.85 * cm) + 6 * cm
    hl = np.roll(np.roll(cm, 1, 0), 1, 1) * (1 - cm)                 # thin lit lip on the upper-left of each crack
    fill = fill + hl * 22
    a = cv2.erode(m, np.ones((3, 3), np.uint8))[..., None]
    out = roi * (1 - a) + fill * a
    A[y0:y1, x0:x1] = out.clip(0, 255)
    return A, (x0, y0, x1, y1)
