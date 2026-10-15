#!/usr/bin/env python3
"""ISSUE01-COVER-V12 — one full-length plate.

The locked v10.1 hi-res master (figure, title, seal) is resampled, never
stretched, and shifted up so the boots fit. New paint is only:

  * a short sky continuation above the master and in the bleed, sampled
    from the master's own sky (no second sky painting, no darkening ramp)
  * the lower legs, boots and obsidian ground, from generated plates,
    feathered under the tabard hem

Title and seal pixels are the master's. Lightning is kept off the trim.
"""
import os
import sys

import cv2
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import srgb

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
V12 = os.path.dirname(os.path.abspath(__file__))
HIRES = os.path.join(ROOT, "BIBLE_FINAL_master_hires.png")
PLATES = os.path.join(V12, "plates")

FW, FH = 2063, 3150
TW, TH = 1988, 3075
BLEED_X = (FW - TW) // 2          # 37
BLEED_Y = (FH - TH) // 2          # 37
TRIM = (BLEED_X, BLEED_Y, BLEED_X + TW, BLEED_Y + TH)  # 37,37,2025,3112
SAFE = 75                         # 0.25 in * 300
SAFE_BOX = (TRIM[0] + SAFE, TRIM[1] + SAFE, TRIM[2] - SAFE, TRIM[3] - SAFE)
# barcode reservation, bottom-left of the safe box, 525 x 300 (guides only)
BAR_W, BAR_H = 525, 300

# Legs plate crop: greaves through the boots. The tabard hem stays the master's.
CROP_Y0, CROP_Y1 = 620, 1000
LEG_TOP = 2235
LEG_W = 1280
LEG_CX = 1060
# Vertical window where the new legs take over from the locked art (print px).
HEM_Y0, HEM_Y1 = 2245, 2365


def load_rgb(path):
    bgr = cv2.imread(path, cv2.IMREAD_COLOR)
    if bgr is None:
        raise SystemExit("missing %s" % path)
    return cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB).astype(np.float32)


def blur(img, sigma):
    return cv2.GaussianBlur(img, (0, 0), sigma)


def smoothstep(t):
    t = np.clip(t, 0, 1)
    return t * t * (3 - 2 * t)


def seal_top_row(art):
    """First row of the issue seal in the resized art (bright coin, upper right)."""
    h, w, _ = art.shape
    r, g, b = art[:, :, 0], art[:, :, 1], art[:, :, 2]
    zone = (r > 150) & (g > 115) & (b < 150) & (g > b + 20)
    x0, x1 = int(w * 0.78), int(w * 0.95)
    rows = zone[: int(h * 0.2), x0:x1].sum(1)
    ys = np.where(rows > 18)[0]
    if len(ys) == 0:
        return 30
    # skip a stray spark: require a run of 4
    for y in ys:
        if rows[y : y + 4].min() > 12:
            return int(y)
    return int(ys[0])


def compress_highlights(img, knee=48.0, gain=0.35):
    """Pull lightning down so a continued sky stays cloud, not a copied bolt."""
    lum = img.mean(2, keepdims=True)
    over = np.clip((lum - knee) / 80.0, 0, 1)
    return img * (1 - over * (1 - gain))


def continue_above(canvas, y_join, n, rng):
    src = canvas[y_join : y_join + n + 30].copy()
    src = compress_highlights(src, knee=42, gain=0.25)
    shift = int(rng.integers(40, 90))
    src = np.roll(src, shift, axis=1)
    patch = src[12 : 12 + n]
    join = blur(canvas[y_join : y_join + 6].mean(0, keepdims=True), 11)
    local = blur(patch[-6:].mean(0, keepdims=True), 11)
    gain = np.clip((join + 3.0) / (local + 3.0), 0.55, 1.35)
    patch = np.clip(patch * gain, 0, 255)
    # 8px hand-off so the join row is the master's own row
    f = smoothstep(np.linspace(0, 1, 8)).astype(np.float32)[:, None, None]
    patch[-8:] = patch[-8:] * (1 - f) + canvas[y_join : y_join + 1] * f
    canvas[y_join - n : y_join] = patch


def continue_side(canvas, x_join, n, direction, rng, y0, y1):
    """direction -1 fills to the left of x_join; +1 fills to the right."""
    if direction < 0:
        src = canvas[y0:y1, x_join : x_join + n + 24].copy()
    else:
        src = canvas[y0:y1, x_join - n - 24 : x_join].copy()
    src = compress_highlights(src, knee=46, gain=0.22)
    src = np.roll(src, int(rng.integers(18, 48)) * direction, axis=0)
    if direction < 0:
        patch = src[:, 10 : 10 + n]
        join = blur(canvas[y0:y1, x_join : x_join + 4].mean(1, keepdims=True), 9)
        local = blur(patch[:, -4:].mean(1, keepdims=True), 9)
        gain = np.clip((join + 3.0) / (local + 3.0), 0.55, 1.4)
        patch = np.clip(patch * gain, 0, 255)
        f = smoothstep(np.linspace(0, 1, 6)).astype(np.float32)[None, :, None]
        patch[:, -6:] = patch[:, -6:] * (1 - f) + canvas[y0:y1, x_join : x_join + 1] * f
        canvas[y0:y1, x_join - n : x_join] = patch
    else:
        patch = src[:, -n - 10 : -10] if src.shape[1] > n + 10 else src[:, :n]
        patch = patch[:, :n]
        join = blur(canvas[y0:y1, x_join - 4 : x_join].mean(1, keepdims=True), 9)
        local = blur(patch[:, :4].mean(1, keepdims=True), 9)
        gain = np.clip((join + 3.0) / (local + 3.0), 0.55, 1.4)
        patch = np.clip(patch * gain, 0, 255)
        f = smoothstep(np.linspace(1, 0, 6)).astype(np.float32)[None, :, None]
        patch[:, :6] = patch[:, :6] * (1 - f) + canvas[y0:y1, x_join - 1 : x_join] * f
        canvas[y0:y1, x_join : x_join + n] = patch


def continue_below(canvas, y_join, y_end, rng):
    """Carry the lower sky downward over the flanks. The centre is covered later."""
    n = y_end - y_join
    if n <= 0:
        return
    band_h = min(160, y_join)
    src = canvas[y_join - band_h : y_join].copy()
    src = compress_highlights(src, knee=36, gain=0.3)
    # prefer the darker flank columns: damp the bright centre a little
    src = np.roll(src, int(rng.integers(20, 50)), axis=1)
    reps = int(np.ceil(n / src.shape[0])) + 1
    tiled = np.vstack([np.roll(src, int(rng.integers(-30, 30)), axis=1) for _ in range(reps)])[:n]
    edge = canvas[y_join - 1 : y_join]
    join = blur(canvas[y_join - 6 : y_join].mean(0, keepdims=True), 13)
    local = blur(tiled[:6].mean(0, keepdims=True), 13)
    gain = np.clip((join + 3.0) / (local + 3.0), 0.45, 1.25)
    tiled = np.clip(tiled * gain, 0, 255)
    # first extended row matches the last art row; the hand-off is 18px
    f = smoothstep(np.linspace(0, 1, 18)).astype(np.float32)[:, None, None]
    tiled[:18] = edge * (1 - f) + tiled[:18] * f
    canvas[y_join:y_end] = tiled


def paint_ground(canvas, rng):
    g = kill_blue(load_rgb(os.path.join(PLATES, "ground_plate.jpg")))
    scale = FW / g.shape[1]
    g = cv2.resize(g, (FW, int(round(g.shape[0] * scale))), interpolation=cv2.INTER_LANCZOS4)
    # grade toward the canvas's lower darks so the stone isn't a different picture
    ref = canvas[2600:2750].reshape(-1, 3)
    ref = ref[ref.mean(1) < 40]
    if len(ref) > 100:
        # lift only the stone's black toward the sky black; keep the gold cracks
        tgt = np.median(ref, axis=0)
        lum = g.mean(2, keepdims=True)
        dark = np.clip((40 - lum) / 40.0, 0, 1)
        delta = (tgt - np.array([18.0, 14.0, 10.0], np.float32))[None, None, :]
        g = np.clip(g + dark * delta * 0.35, 0, 255)
    gh = g.shape[0]
    # stone becomes solid in the lower fifth and feathers up into the dark
    line = 2680
    yy = np.arange(FH, dtype=np.float32)[:, None]
    xx = np.arange(FW, dtype=np.float32)[None, :]
    wave = 22 * np.sin(xx / 84.0) + 14 * np.sin(xx / 31.0 + 1.3) + 8 * np.sin(xx / 13.0)
    alpha = smoothstep((yy - (line + wave)) / 170.0)
    y0 = FH - gh
    patch = np.zeros_like(canvas)
    if y0 >= 0:
        patch[y0:] = g[: FH - y0]
    else:
        patch[:] = g[-y0 : -y0 + FH]
    canvas[:] = canvas * (1 - alpha[..., None]) + patch * alpha[..., None]
    return line


def kill_blue(img):
    """Generated plates sometimes drift cool. Keep every channel at or under the warmer ones."""
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    cap = np.maximum(r, g)
    img = img.copy()
    img[:, :, 2] = np.minimum(b, cap)
    return img


def leg_alpha(nh_canvas=None):
    """Soft leg/boot/shield silhouette on the full print. Zero on the sky flanks."""
    yy, xx = np.mgrid[:FH, :FW].astype(np.float32)
    t = np.clip((yy - HEM_Y0) / 780.0, 0, 1)
    # Asymmetric: cape to the left, shield to the right, boots under the body.
    half_l = 210 + t * 260
    half_r = 250 + t * 420
    dx = xx - LEG_CX
    dist = np.where(dx < 0, (-dx) / half_l, dx / half_r)
    m = 1 - smoothstep((dist - 0.82) / 0.18)
    m *= smoothstep((yy - HEM_Y0) / float(HEM_Y1 - HEM_Y0))
    # release the silhouette once the boots are planted, so the ground plate
    # owns the stone around the soles instead of the legs-plate background
    m *= 1 - smoothstep((yy - 2960) / 90.0)
    return m.astype(np.float32)


def paint_legs(canvas):
    legs = kill_blue(load_rgb(os.path.join(PLATES, "legs_plate.jpg")))
    crop = legs[CROP_Y0:CROP_Y1]
    scale = LEG_W / crop.shape[1]
    nh = int(round(crop.shape[0] * scale))
    up = cv2.resize(crop, (LEG_W, nh), interpolation=cv2.INTER_LANCZOS4)
    if scale > 1.05:
        soft = blur(up, 0.65)
        up = np.clip(up + 0.22 * (up - soft), 0, 255)
    x0 = int(round(LEG_CX - LEG_W / 2))
    y0 = LEG_TOP
    # Match the crop's shadow tone to the master's hem, then let the boots
    # keep the plate's own light so the gold cracks still read.
    ov = min(70, nh)
    x1 = min(FW, x0 + LEG_W)
    xa = max(0, x0)
    dst = canvas[y0 : y0 + ov, xa:x1]
    src = up[:ov, xa - x0 : xa - x0 + dst.shape[1]]
    if src.shape == dst.shape and src.size:
        dark = src.mean(2) < 50
        if dark.sum() > 40:
            offset = dst[dark].mean(0) - src[dark].mean(0)
            fade_n = max(8, int(nh * 0.35))
            fade = np.linspace(1, 0, fade_n).astype(np.float32)[:, None, None]
            up[:fade_n] = np.clip(up[:fade_n] + offset * fade * 0.85, 0, 255)
    alpha = leg_alpha()
    placed = np.zeros_like(canvas)
    y1 = min(FH, y0 + nh)
    placed[y0:y1, xa:x1] = up[: y1 - y0, xa - x0 : xa - x0 + (x1 - xa)]
    a = alpha[..., None]
    # only where the scaled plate actually exists, and dissolve its lower
    # edge into the ground plate so the plate's own floor doesn't end in a line
    cover = np.zeros((FH, FW), np.float32)
    cover[y0:y1, xa:x1] = 1
    dissolve = 1 - smoothstep((np.arange(FH) - 2685) / 100.0)
    a = a * cover[..., None] * dissolve.astype(np.float32)[:, None, None]
    canvas[:] = canvas * (1 - a) + placed * a
    return (x0, y0, LEG_W, nh, float(scale))


def suppress_edge_lightning(canvas, ground_line):
    """No bolt may touch the trim. Cracks in the ground may run off the sheet."""
    x0, y0, x1, y1 = TRIM
    lum = canvas.mean(2)
    yy, xx = np.mgrid[:FH, :FW]
    # distance to the nearest trim edge, inside or outside the trim box
    dist = np.minimum(np.minimum(np.abs(xx - x0), np.abs(xx - x1)),
                      np.minimum(np.abs(yy - y0), np.abs(yy - y1))).astype(np.float32)
    above = yy < (ground_line - 40)
    bright = lum > 48
    # Full strength on the trim line, falling off over ~36px. Take the max
    # with a light blur so the falloff widens without weakening the core.
    # Hold a full dim for the first 16px so a bolt cannot reach the trim, then fade.
    a = np.clip(1.0 - np.maximum(dist - 16.0, 0) / 26.0, 0, 1)
    a = a * bright.astype(np.float32) * above.astype(np.float32)
    a = np.maximum(a, cv2.GaussianBlur(a, (0, 0), 0.7))
    if not (a > 0.01).any():
        return 0
    dim = np.clip(18.0 / (lum + 1.0), 0, 1)[..., None]
    canvas[:] = canvas * (1 - a[..., None] * (1 - dim))
    return int((a > 0.5).sum())


def ember_check(canvas):
    lum = canvas.mean(2)
    # small bright specks per horizontal band, to confirm the field reaches the edges
    bands = []
    for y0, y1, name in (
        (0, 120, "top"),
        (120, 500, "upper"),
        (FH - 400, FH - 80, "lower"),
    ):
        sub = lum[y0:y1]
        specks = (sub > 90) & (sub < 220)
        bands.append((name, int(specks.sum())))
    return bands


def main():
    rng = np.random.default_rng(12)
    hires = load_rgb(HIRES)
    art = cv2.resize(hires, (TW, int(round(hires.shape[0] * TW / hires.shape[1]))), interpolation=cv2.INTER_AREA)
    # INTER_AREA downscale is the sharp one; 2236 or 2237
    seal = seal_top_row(art)
    # seal sits 14px inside the safe line
    # +22px puts the seal's outer ring inside the 0.25in safe line, not merely
    # the dense part of the coin the detector locks onto.
    y_place = (TRIM[1] + SAFE + 22) - seal
    if y_place < 0:
        raise SystemExit("art would start above the canvas (seal row %d)" % seal)
    print("art", art.shape, "seal_row", seal, "y_place", y_place, "art_bottom", y_place + art.shape[0])

    canvas = np.zeros((FH, FW, 3), np.float32)
    h, w = art.shape[:2]
    canvas[y_place : y_place + h, BLEED_X : BLEED_X + w] = art

    # side bleed first, so the rows the top continuation samples are full-width
    art_bottom = y_place + h
    if BLEED_X > 0:
        continue_side(canvas, BLEED_X, BLEED_X, -1, rng, y_place, art_bottom)
    right_gap = FW - (BLEED_X + w)
    if right_gap > 0:
        continue_side(canvas, BLEED_X + w, right_gap, +1, rng, y_place, art_bottom)
    if y_place > 0:
        continue_above(canvas, y_place, y_place, rng)
    continue_below(canvas, art_bottom, FH, rng)

    ground_line = paint_ground(canvas, rng)
    # Legs go on after the ground, only inside the silhouette. Everything
    # outside that mask — title, seal, hammer, sky flanks — stays the master.
    leg_box = paint_legs(canvas)
    killed = suppress_edge_lightning(canvas, ground_line)

    # diagnostics
    _sx0, sy0, _sx1, _sy1 = SAFE_BOX
    seal_print_top = y_place + seal
    print("seal print y", seal_print_top, "safe top", sy0, "margin", seal_print_top - sy0)
    print("leg box x,y,w,h", leg_box, "ground line", ground_line, "bolts cleared", killed)
    print("embers", ember_check(canvas))
    # title / seal / hammer stay exact: the leg mask is below the hem,
    # and the lightning gutter is only the outer 24px
    inset = 60
    y_lock1 = min(HEM_Y0, y_place + h)
    exact = canvas[y_place:y_lock1, BLEED_X + inset : BLEED_X + w - inset]
    src = art[: y_lock1 - y_place, inset : w - inset]
    d = float(np.abs(exact - src).mean()) if exact.shape == src.shape else 999
    print("locked-region mean abs diff", round(d, 4))
    if d > 0.05:
        raise SystemExit("locked region was modified (diff %.3f)" % d)

    out = np.clip(canvas + 0.5, 0, 255).astype(np.uint8)
    print_path = os.path.join(ROOT, "RaThor_Issue01_Cover_BIBLE_FINAL_6.625x10.25_bleed_300dpi.jpg")
    # keep the previous print beside the new one for the before/after
    prev = os.path.join(V12, "v10_1_print.jpg")
    if not os.path.exists(prev):
        import shutil
        shutil.copy(print_path, prev)
    srgb.save(print_path, out, dpi=300, quality=95)
    print("wrote", print_path)
    return out, y_place, seal


if __name__ == "__main__":
    main()
