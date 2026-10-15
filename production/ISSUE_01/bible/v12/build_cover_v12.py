#!/usr/bin/env python3
"""ISSUE01-COVER-V12 — full-length plate.

The locked hi-res figure, title and seal are resampled to the trim width
and shifted up. They are never mirrored, reflected or tiled.

Bleed, the sky under the feet and the ground come from generated plates
(plates/sky_plate.jpg, plates/ground_v12b.jpg). The title and the seal are
masked out of every sample used to grade that sky. The greaves and sabatons
are a generated plate (plates/greaves_plate.jpg), feathered under the hem.
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
TW = 1988
BLEED_X = (FW - TW) // 2                 # 37
BLEED_Y = 37
TRIM = (BLEED_X, BLEED_Y, BLEED_X + TW, BLEED_Y + 3075)
SAFE = 75

# Greaves plate: skip the generated tabard, keep both greaves and both boots.
GREAVE_CROP = (340, 1060)
LEG_W = 1020
LEG_CX = 1036
HEM_Y0, HEM_Y1 = 2210, 2340


def load_rgb(path):
    bgr = cv2.imread(path, cv2.IMREAD_COLOR)
    if bgr is None:
        raise SystemExit("missing %s" % path)
    return cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB).astype(np.float32)


def blur(img, sigma):
    if sigma <= 0:
        return img
    return cv2.GaussianBlur(img, (0, 0), sigma)


def smoothstep(t):
    t = np.clip(t, 0, 1)
    return t * t * (3 - 2 * t)


def kill_blue(img):
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    out = img.copy()
    out[:, :, 2] = np.minimum(b, np.maximum(r, g))
    return out


def lift_shadows(img, power=0.78, mix=0.45):
    """Open crushed blacks so engraving survives a thumbnail. Highlights stay."""
    x = np.clip(img / 255.0, 0, 1)
    y = np.power(x, power)
    return np.clip((x * (1 - mix) + y * mix) * 255.0, 0, 255)


def seal_top_row(art):
    h, w, _ = art.shape
    r, g, b = art[:, :, 0], art[:, :, 1], art[:, :, 2]
    zone = (r > 150) & (g > 115) & (b < 150) & (g > b + 20)
    x0, x1 = int(w * 0.78), int(w * 0.95)
    rows = zone[: int(h * 0.2), x0:x1].sum(1)
    ys = np.where(rows > 18)[0]
    for y in ys:
        if rows[y : y + 4].min() > 12:
            return int(y)
    return int(ys[0]) if len(ys) else 30


def dark_column_color(img, thresh=46.0):
    """Per-column mean of the dark sky pixels only. Title and seal are excluded."""
    lum = img.mean(2, keepdims=True)
    m = (lum < thresh).astype(np.float32)
    num = (img * m).sum(axis=0)
    den = m.sum(axis=0)[:, 0]
    good = den > 2
    col = np.zeros((img.shape[1], 3), np.float32)
    if good.sum() >= 8:
        col[good] = num[good] / den[good, None]
        idx = np.arange(img.shape[1])
        for c in range(3):
            col[:, c] = np.interp(idx, idx[good], col[good, c])
    else:
        flat = img.reshape(-1, 3)
        take = flat[np.argsort(flat.mean(1))[: max(16, flat.shape[0] // 6)]]
        col[:] = np.median(take, axis=0)
    return blur(col[None].astype(np.float32), 22)[0]


def fit_width(img, width):
    h = int(round(img.shape[0] * width / img.shape[1]))
    return cv2.resize(img, (width, h), interpolation=cv2.INTER_LANCZOS4)


def grade_to_color(img, target_row):
    """Multiply so img's blurred column color meets target_row (1xWx3). No pixel copy."""
    local = blur(img.mean(axis=0, keepdims=True), 18)
    gain = np.clip((target_row[None] + 4.0) / (local + 4.0), 0.45, 1.7)
    return np.clip(img * gain, 0, 255)


def cover_with_sky(art):
    """One generated sky, scaled and cropped. Never mirrored, never tiled from the master.

    Two uniform scales of the same plate cover the tall sheet. They meet under
    a single crossfade behind the figure, where the locked art will hide the join.
    """
    src = kill_blue(load_rgb(os.path.join(PLATES, "sky_plate.jpg")))
    sh, sw = src.shape[:2]

    def uniform(height, x_bias):
        scale = height / float(sh)
        wide = cv2.resize(src, (int(round(sw * scale)), height), interpolation=cv2.INTER_LANCZOS4)
        if wide.shape[1] < FW:
            wide = cv2.resize(wide, (FW, height), interpolation=cv2.INTER_LANCZOS4)
        extra = wide.shape[1] - FW
        x0 = int(np.clip(extra * x_bias, 0, extra))
        return wide[:, x0 : x0 + FW]

    upper_h = 1680
    upper = uniform(upper_h, 0.25)
    lower = uniform(FH - upper_h + 240, 0.75)
    canvas = np.zeros((FH, FW, 3), np.float32)
    canvas[:upper_h] = upper
    yb = upper_h - 240
    f = smoothstep(np.linspace(0, 1, 240)).astype(np.float32)[:, None, None]
    canvas[yb : yb + 240] = upper[-240:] * (1 - f) + lower[:240] * f
    canvas[yb + 240 :] = lower[240 : 240 + (FH - (yb + 240))]
    # Grade only the rows that touch the locked art, using dark sky pixels.
    # Bright pixels (title, seal, lightning cores) are excluded from the target.
    h = art.shape[0]
    # The caller places the art at y_place; grading is applied later once y_place is known.
    return canvas


def feather_art_bottom(canvas, art, art_bottom, sky_under):
    """Ease the flank sky at the bottom of the locked art into the generated sky.

    The centre (the legs) is left alone. sky_under is the generated sky that
    sat here before the locked art was pasted. No full-width copy of the figure.
    """
    w = art.shape[1]
    x0 = BLEED_X
    fade_h = sky_under.shape[0]
    rows = np.arange(fade_h, dtype=np.float32)
    vert = smoothstep(rows / fade_h)[:, None]
    xx = np.arange(w, dtype=np.float32)
    left = smoothstep((LEG_CX - 80 - (x0 + xx)) / 160.0)
    right = smoothstep(((x0 + xx) - (LEG_CX + 80)) / 160.0)
    flank = np.clip(np.maximum(left, right), 0, 1)[None, :]
    a = (vert * flank)[..., None]
    locked = art[-fade_h:]
    canvas[art_bottom - fade_h : art_bottom, x0 : x0 + w] = locked * (1 - a) + sky_under * a


def paint_ground(canvas):
    g = fit_width(kill_blue(load_rgb(os.path.join(PLATES, "ground_v12b.jpg"))), FW)
    if g.shape[0] < 900:
        g = cv2.resize(g, (FW, 1100), interpolation=cv2.INTER_LANCZOS4)
    patch = np.zeros_like(canvas)
    patch[-g.shape[0] :] = g[-min(g.shape[0], FH) :]
    if g.shape[0] < FH:
        patch[-g.shape[0] :] = g
    yy = np.arange(FH, dtype=np.float32)[:, None]
    xx = np.arange(FW, dtype=np.float32)[None, :]
    wave = 34 * np.sin(xx / 130.0) + 22 * np.sin(xx / 53.0 + 0.7) + 12 * np.sin(xx / 19.0)
    # Long feather. A short one reads as a hard band at thumbnail size.
    alpha = smoothstep((yy - (2520 + wave)) / 380.0)
    canvas[:] = canvas * (1 - alpha[..., None]) + patch * alpha[..., None]
    return 2520


def paint_greaves(canvas):
    plate = lift_shadows(kill_blue(load_rgb(os.path.join(PLATES, "greaves_plate.jpg"))), mix=0.5)
    y0, y1 = GREAVE_CROP
    crop = plate[y0:y1]
    scale = LEG_W / crop.shape[1]
    nh = int(round(crop.shape[0] * scale))
    up = cv2.resize(crop, (LEG_W, nh), interpolation=cv2.INTER_LANCZOS4 if scale >= 1 else cv2.INTER_AREA)
    if scale > 1.02:
        soft = blur(up, 0.6)
        up = np.clip(up + 0.2 * (up - soft), 0, 255)
    x0 = int(round(LEG_CX - LEG_W / 2))
    # The hem of the locked art is the only colour match, and it fades within
    # a short distance so the greaves are not pulled down to black.
    top = min(HEM_Y1, FH - 1)
    ov = min(50, nh, top - HEM_Y0)
    if ov > 8:
        xa, xb = max(0, x0), min(FW, x0 + LEG_W)
        dst = canvas[HEM_Y0 : HEM_Y0 + ov, xa:xb]
        src = up[:ov, xa - x0 : xa - x0 + (xb - xa)]
        if src.shape == dst.shape and src.size:
            dark = src.mean(2) < 70
            if int(dark.sum()) > 30:
                offset = dst[dark].mean(0) - src[dark].mean(0)
                fade = np.linspace(1, 0, 80).astype(np.float32)[: min(80, nh), None, None]
                up[: fade.shape[0]] = np.clip(up[: fade.shape[0]] + offset * fade * 0.35, 0, 255)
    # Silhouette from the plate itself: gold engraving plus the dark armour
    # between the plates, feathered. The corners of the plate stay out.
    r, g, b = up[:, :, 0], up[:, :, 1], up[:, :, 2]
    gold = ((r > 80) & (g > 45) & (r > b + 12)).astype(np.float32)
    gold = cv2.dilate(gold, np.ones((9, 9), np.uint8))
    # armour is the darker structured mass inside the gold outline
    yy = np.linspace(0, 1, nh)[:, None]
    xx = np.linspace(-1, 1, LEG_W)[None, :]
    # Stay inside the legs. The plate's side sky must not paint a rectangle.
    half = 0.34 + 0.16 * yy
    trap = (np.abs(xx) < half).astype(np.float32)
    trap = cv2.GaussianBlur(trap, (0, 0), 16)
    detail = gold
    detail = cv2.GaussianBlur(detail, (0, 0), 6)
    mask = np.clip(trap * 0.85 + detail * 0.55, 0, 1)
    # top feather into the tabard, bottom feather into the ground plate
    mask *= smoothstep(np.arange(nh) / 70.0)[:, None]
    mask *= 1 - smoothstep((np.arange(nh) - (nh - 90)) / 90.0)[:, None]
    # place so the feather begins at the hem
    y_put = HEM_Y0 - 30
    placed = np.zeros_like(canvas)
    cover = np.zeros((FH, FW), np.float32)
    yb = min(FH, y_put + nh)
    xb0, xb1 = max(0, x0), min(FW, x0 + LEG_W)
    sy, sx = max(0, -y_put), max(0, -x0)
    ph, pw = yb - max(y_put, 0), xb1 - xb0
    placed[max(y_put, 0) : yb, xb0:xb1] = up[sy : sy + ph, sx : sx + pw]
    cover[max(y_put, 0) : yb, xb0:xb1] = mask[sy : sy + ph, sx : sx + pw]
    # keep the locked art fully opaque above the hem
    cover[:HEM_Y0] = 0
    a = cover[..., None]
    canvas[:] = canvas * (1 - a) + placed * a
    return (x0, y_put, LEG_W, nh, float(scale), float(up[nh // 2].mean()))


def suppress_edge_lightning(canvas):
    """Bolts must not touch the trim. Ground cracks below the feet may."""
    x0, y0, x1, y1 = TRIM
    lum = canvas.mean(2)
    yy, xx = np.mgrid[:FH, :FW]
    dist = np.minimum(
        np.minimum(np.abs(xx - x0), np.abs(xx - x1)),
        np.minimum(np.abs(yy - y0), np.abs(yy - y1)),
    ).astype(np.float32)
    above = yy < 2860
    bright = lum > 50
    a = np.clip(1.0 - np.maximum(dist - 14.0, 0) / 24.0, 0, 1)
    # The trim gutter stops at the trim. Bolt tips in the outer bleed still
    # sit on the sheet edge, so fade those the same way.
    sheet = np.minimum(np.minimum(xx, FW - 1 - xx), np.minimum(yy, FH - 1 - yy)).astype(np.float32)
    a = np.maximum(a, np.clip(1.0 - sheet / 28.0, 0, 1))
    a = a * bright.astype(np.float32) * above.astype(np.float32)
    a = np.maximum(a, cv2.GaussianBlur(a, (0, 0), 0.6))
    dim = np.clip(18.0 / (lum + 1.0), 0, 1)[..., None]
    canvas[:] = canvas * (1 - a[..., None] * (1 - dim))
    return int((a > 0.5).sum())


def corr(a, b):
    a = a.reshape(-1).astype(np.float64)
    b = b.reshape(-1).astype(np.float64)
    a -= a.mean()
    b -= b.mean()
    return float((a * b).sum() / (np.sqrt((a * a).sum() * (b * b).sum()) + 1e-9))


def assert_clean(canvas, y_place):
    """Fail the build if the thumbnail failures are still in the pixels."""
    def hp(img):
        return img - blur(img, 2.5)
    top = hp(canvas[:60])
    title = canvas[y_place + 40 : y_place + 100]
    if title.shape[0] == 60:
        title = hp(title)
        c_same = corr(top, title)
        c_flip = corr(top, np.flip(title, 1))
        c_ud = corr(top, title[::-1])
    else:
        c_same = c_flip = c_ud = 0
    print("ghost corr top-vs-title", round(c_same, 3), "flip", round(c_flip, 3), "flipud", round(c_ud, 3))
    if max(c_same, c_flip, c_ud) > 0.12:
        raise SystemExit("top bleed still echoes the title (corr %.3f)" % max(c_same, c_flip, c_ud))
    for name, x0, x1 in (("left", 0, 90), ("right", FW - 90, FW)):
        g = canvas[2180:2780, x0:x1].mean(2)
        g = g - blur(g, 8)
        best, shift = 0.0, 0
        for s in range(20, 140, 8):
            c = corr(g[:-s], g[s:])
            if c > best:
                best, shift = c, s
        print("side period", name, round(best, 3), "shift", shift)
        if best > 0.32:
            raise SystemExit("%s edge still repeats (corr %.3f at %d px)" % (name, best, shift))
    # a hard full-width band shows up as a row-diff spike on the flanks
    lum = canvas.mean(2)
    flank = np.concatenate([lum[:, 80:280], lum[:, FW - 280 : FW - 80]], axis=1)
    d = np.abs(np.diff(flank, axis=0)).mean(1)
    for y0, y1, label in ((2100, 2500, "hem"), (2500, 3000, "ground")):
        peak = float(d[y0:y1].max())
        at = y0 + int(d[y0:y1].argmax())
        print("flank row-diff", label, round(peak, 2), "at", at)
        if peak > 14:
            raise SystemExit("hard band on the %s flanks (row-diff %.1f at y=%d)" % (label, peak, at))


def main():
    hires = load_rgb(HIRES)
    art = cv2.resize(
        hires, (TW, int(round(hires.shape[0] * TW / hires.shape[1]))), interpolation=cv2.INTER_AREA
    )
    seal = seal_top_row(art)
    y_place = (TRIM[1] + SAFE + 22) - seal
    h, w = art.shape[:2]
    print("art", art.shape, "seal_row", seal, "y_place", y_place, "art_bottom", y_place + h)

    canvas = cover_with_sky(art)
    art_bottom = y_place + h
    # Match the sky just above the art to the dark pixels of the art's top.
    # The target is a blurred column color, so letter shapes cannot print into it.
    tone = np.zeros((FW, 3), np.float32)
    tone[BLEED_X : BLEED_X + w] = dark_column_color(art[:22], thresh=40)
    tone[:BLEED_X] = tone[BLEED_X]
    tone[BLEED_X + w :] = tone[BLEED_X + w - 1]
    if y_place >= 36:
        # Gain only. Replacing rows with a flat colour leaves a band, and it
        # can pick up the title's horizontal brightness.
        band = canvas[y_place - 36 : y_place]
        local = blur(band.mean(axis=0, keepdims=True), 24)
        gain = np.clip((tone[None] + 4.0) / (local + 4.0), 0.55, 1.45)
        ramp = smoothstep(np.linspace(0, 1, 36)).astype(np.float32)[:, None, None]
        canvas[y_place - 36 : y_place] = np.clip(band * (1 + (gain - 1) * ramp), 0, 255)
    fade_h = 110
    sky_under = canvas[art_bottom - fade_h : art_bottom, BLEED_X : BLEED_X + w].copy()
    canvas[y_place : y_place + h, BLEED_X : BLEED_X + w] = art
    feather_art_bottom(canvas, art, art_bottom, sky_under)
    ground_line = paint_ground(canvas)
    leg_box = paint_greaves(canvas)
    # locked interior, above the hem, clear of the lightning gutter
    inset = 70
    y_lock = min(HEM_Y0, y_place + h)
    exact = canvas[y_place:y_lock, BLEED_X + inset : BLEED_X + w - inset]
    src = art[: y_lock - y_place, inset : w - inset]
    diff = float(np.abs(exact - src).mean()) if exact.shape == src.shape else 999
    print("locked-region mean abs", round(diff, 4), "leg", leg_box, "ground", ground_line)
    if diff > 0.05:
        raise SystemExit("locked region changed (diff %.3f)" % diff)
    killed = suppress_edge_lightning(canvas)
    print("bolts cleared", killed)
    assert_clean(canvas, y_place)

    out = np.clip(canvas + 0.5, 0, 255).astype(np.uint8)
    print_path = os.path.join(ROOT, "RaThor_Issue01_Cover_BIBLE_FINAL_6.625x10.25_bleed_300dpi.jpg")
    prev = os.path.join(V12, "v10_1_print.jpg")
    if not os.path.exists(prev):
        import shutil
        shutil.copy(print_path, prev)
    srgb.save(print_path, out, dpi=300, quality=95)
    thumb = cv2.resize(out, (620, int(round(620 * FH / FW))), interpolation=cv2.INTER_AREA)
    srgb.save(os.path.join(V12, "thumb_620.jpg"), thumb, dpi=72, quality=90)
    print("wrote", print_path, "thumb", thumb.shape)
    return out


if __name__ == "__main__":
    main()
