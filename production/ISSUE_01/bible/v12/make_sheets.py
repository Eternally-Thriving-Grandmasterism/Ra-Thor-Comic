#!/usr/bin/env python3
"""Guides, before/after against v10.1, and 100% edge/hammer crops for the v12 print."""
import os
import sys

import cv2
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import srgb

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
V12 = os.path.dirname(os.path.abspath(__file__))
PRINT = os.path.join(ROOT, "RaThor_Issue01_Cover_BIBLE_FINAL_6.625x10.25_bleed_300dpi.jpg")
OLD = os.path.join(V12, "v10_1_print.jpg")

FW, FH = 2063, 3150
TRIM = (37, 37, 2025, 3112)
SAFE = 75
BAR_W, BAR_H = 525, 300


def load(path):
    bgr = cv2.imread(path, cv2.IMREAD_COLOR)
    if bgr is None:
        raise SystemExit("missing %s" % path)
    return cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)


def label(img, text):
    out = img.copy()
    cv2.rectangle(out, (0, 0), (min(img.shape[1] - 1, 640), 64), (0, 0, 0), -1)
    cv2.putText(out, text, (16, 44), cv2.FONT_HERSHEY_SIMPLEX, 1.15, (255, 255, 255), 2, cv2.LINE_AA)
    return out


def main():
    rgb = load(PRINT)
    assert rgb.shape == (FH, FW, 3), rgb.shape
    crops = os.path.join(V12, "crops")
    os.makedirs(crops, exist_ok=True)

    # guides: red trim, cyan safe, white barcode reservation. Not burned into the print.
    g = rgb.copy()
    x0, y0, x1, y1 = TRIM
    cv2.rectangle(g, (x0, y0), (x1 - 1, y1 - 1), (255, 40, 40), 3, cv2.LINE_AA)
    cv2.rectangle(
        g, (x0 + SAFE, y0 + SAFE), (x1 - 1 - SAFE, y1 - 1 - SAFE), (0, 255, 255), 3, cv2.LINE_AA
    )
    cv2.putText(g, 'TRIM 6.625x10.25"', (x0 + 14, y0 + 36), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 40, 40), 2, cv2.LINE_AA)
    cv2.putText(
        g, 'SAFE 0.25" inside trim', (x0 + SAFE + 14, y0 + SAFE + 36),
        cv2.FONT_HERSHEY_SIMPLEX, 0.85, (0, 255, 255), 2, cv2.LINE_AA,
    )
    cv2.putText(g, 'BLEED 0.125"', (10, FH - 16), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    bx, by1 = x0 + SAFE, y1 - SAFE
    cv2.rectangle(g, (bx, by1 - BAR_H), (bx + BAR_W, by1), (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(g, "barcode box (reserved)", (bx + 12, by1 - BAR_H + 36), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    srgb.save(os.path.join(V12, "print_v12_guides.jpg"), g, dpi=300, quality=92)

    old = load(OLD)
    assert old.shape == rgb.shape
    scale = 0.42
    def down(im):
        return cv2.resize(im, (int(FW * scale), int(FH * scale)), interpolation=cv2.INTER_AREA)
    sep = np.full((down(old).shape[0], 12, 3), 255, np.uint8)
    pair = np.hstack([label(down(old), "v10.1"), sep, label(down(rgb), "v12 full length")])
    srgb.save(os.path.join(V12, "before_after_v10_1_v12.jpg"), pair, dpi=150, quality=90)

    # 100% crops from the print pixels (no extra resample).
    tiles = {
        "top_edge_100.png": rgb[0:220, 0:FW],
        "bottom_edge_100.png": rgb[FH - 320 : FH, 0:FW],
        "side_left_100.png": rgb[0:FH, 0:180],
        "side_right_100.png": rgb[0:FH, FW - 180 : FW],
        "hammer_100.png": rgb[140:720, 40:620],
    }
    for name, tile in tiles.items():
        srgb.save(os.path.join(crops, name), tile)
        print(name, tile.shape)
    print("sheets ok", pair.shape)


if __name__ == "__main__":
    main()
