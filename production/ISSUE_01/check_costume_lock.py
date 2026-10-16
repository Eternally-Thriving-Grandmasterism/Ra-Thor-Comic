#!/usr/bin/env python3
"""ISSUE01 costume lock (Sherif, 2026-10-16).

Eye placement: an Eye of Horus may appear only in the halo sigil and on the
pauldron seal. The check fails if a scanned line gives one to the shield or
the hammer.

Shield shape: the check fails on "kite shield" or an emerald eye-seal on the
shield, unless the same line marks that wording amended, superseded, or history.

Shield emblem (Wild, 2026-10-16, 2:20 PM ET): the current written lock in the
four costume files must name the tall pointed outline, the Vegvísir elongated
vertically, the gold interlaced knotwork, the band of gold runes, and the
plain gold boss. A scanned line that gives a round or disc Vegvísir, or a sun
or a bolt, as the current shield spec fails, unless that same line marks the
wording superseded, history, amended, or a reject, or negates it.

Type margin: every type pixel whose alpha is greater than ALPHA_THRESHOLD
must sit at least 75 px (0.25 in) inside the trim at 300 dpi. The trim line
is 0.125 in, which is 37.5 px, not the 37 px bleed constant used by the
sheet builders.
"""
import os, sys, re
import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SCAN = [
    '09_CHARACTER_BIBLE.md',
    'production/ISSUE_01/ISSUE_01_PRODUCTION.md',
    'production/ISSUE_01/RENDER_CHECKLIST.md',
    'production/ISSUE_01/bible/CHARACTER_BIBLE.md',
    'production/ISSUE_01/LETTERING_SPEC.md',
    '00_FIDELITY_PROTOCOL.md',
    '01_VISUAL_STYLE_GUIDE.md',
    '04_VISUAL_CANON.md',
    'episodes/E01_TOLC.md',
]
# A counted type pixel has alpha strictly greater than this fraction of 255.
ALPHA_THRESHOLD = 0.03
DPI = 300
TRIM_IN = 0.125
TRIM_PX = TRIM_IN * DPI          # 37.5
MIN_MARGIN_PX = 75               # 0.25 in
TYPE_LAYER = os.path.join(ROOT, 'production/ISSUE_01/bible/v18/type_layer_final_v18.png')

# Positive assignments. The halo sigil and the pauldron seal are not in these patterns.
HAMMER_POS = re.compile(
    r'digital eye of horus|eye of horus on the boss|eye of horus on its (?:front )?face|'
    r"hammer's digital eye|(?<!no )hammer eye|eye of horus on the hammer",
    re.I)
SHIELD_POS = re.compile(
    r'eye of horus stays on the shield|eye of horus at its centre|winged eye of horus at|'
    r"shield's eye|eye-seal shield|eye-seal kite|eye-seal on the shield|eye-seal out|"
    r'eye-seal must stay|gold eye-seal|shield field with a gold eye|as the shield\'s eye',
    re.I)
HAMMER_NEG = re.compile(
    r'no eye of horus on the hammer|never carries an eye|eye on the hammer is a reject|'
    r'an eye on the hammer is a reject|reject: any eye on the hammer',
    re.I)
SHIELD_NEG = re.compile(
    r'no eye of horus on the shield|not on the shield|not repeated on the shield|'
    r'is a reject|superseded|history|amended',
    re.I)
# "kite shield" and an emerald eye-seal assigned to the shield. A same-line
# amendment, supersession, or reject note keeps the historical sentence.
KITE_POS = re.compile(r'kite shield', re.I)
KITE_NEG = re.compile(
    r'not a kite shield|no kite shield|superseded|history|amended|is a reject',
    re.I)
EMERALD_SEAL_POS = re.compile(r'emerald eye-seal', re.I)
EMERALD_SEAL_NEG = re.compile(
    r'no emerald eye-seal|superseded|history|amended',
    re.I)
# Current shield spec (ISSUE01-SHIELD-TALL-EMBLEM-1). These four files state
# the written lock. Each must carry every required phrase.
SHIELD_LOCK_FILES = [
    '09_CHARACTER_BIBLE.md',
    'production/ISSUE_01/ISSUE_01_PRODUCTION.md',
    'production/ISSUE_01/RENDER_CHECKLIST.md',
    'production/ISSUE_01/bible/CHARACTER_BIBLE.md',
]
SHIELD_REQUIRED = (
    ('tall pointed outline', re.compile(r'tall, narrow, pointed bottom', re.I)),
    ('elongated Vegvísir', re.compile(r'Vegv[ií]sir elongated vertically', re.I)),
    ('knotwork binding', re.compile(r'gold interlaced knotwork', re.I)),
    ('rune band', re.compile(r'band of gold runes', re.I)),
    ('plain boss', re.compile(r'plain gold boss', re.I)),
)
# A round or disc Vegvísir given as the emblem. "not rounded" (the shield
# outline) does not match. A same-line negation, reject, or history note holds.
ROUND_DISC_VEG = re.compile(
    r'(?:round|circular|disc)\s+(?:gold\s+)?(?:norse\s+)?Vegv[ií]sir|'
    r'Vegv[ií]sir\s+(?:rune\s+compass\s+)?(?:is\s+)?(?:a\s+)?(?:round|circular|disc)\b|'
    r'(?:round|circular)\s+(?:gold\s+)?rune\s+compass|'
    r'disc\s+Vegv[ií]sir|Vegv[ií]sir\s+disc',
    re.I)
ROUND_DISC_NEG = re.compile(
    r'not\s+(?:a\s+)?(?:round|circular|disc)|'
    r'no\s+(?:round|circular|disc)\s+Vegv|'
    r'superseded|history|amended|is a reject',
    re.I)
# A sun or a bolt assigned to the shield emblem, the Vegvísir, or its boss.
# Chest sun discs and hammer bolts on the same line do not match.
SUN_BOLT_ON_EMBLEM = re.compile(
    r'shield emblem[^.]{0,70}\b(?:with|carries|bearing|and)\b[^.]{0,40}\b(?:sun|bolt)\b|'
    r'\b(?:sun(?:\s+rays|\s+disc)?|lightning[\s-]?bolt|\bbolt)\b[^.]{0,40}'
    r'\b(?:on|in|at|over)\s+the\s+(?:shield emblem|emblem|Vegv[ií]sir|boss)|'
    r'Vegv[ií]sir[^.]{0,40}\b(?:with|and)\s+(?:a\s+)?(?:sun|bolt|lightning)|'
    r'\bboss\b[^.]{0,30}\b(?:with|and)\s+(?:a\s+)?(?:sun|bolt)',
    re.I)
SUN_BOLT_NEG = re.compile(
    r'no sun|no bolt|out of the emblem|stay out|stays out|'
    r'superseded|history|amended|is a reject',
    re.I)

def eye_failures(path):
    fails = []
    for n, line in enumerate(open(path, encoding='utf-8'), 1):
        if HAMMER_POS.search(line) and not HAMMER_NEG.search(line):
            fails.append((n, 'hammer', line.strip()[:220]))
        if SHIELD_POS.search(line) and not SHIELD_NEG.search(line):
            fails.append((n, 'shield', line.strip()[:220]))
        if KITE_POS.search(line) and not KITE_NEG.search(line):
            fails.append((n, 'kite', line.strip()[:220]))
        if EMERALD_SEAL_POS.search(line) and not EMERALD_SEAL_NEG.search(line):
            fails.append((n, 'emerald-seal', line.strip()[:220]))
        if ROUND_DISC_VEG.search(line) and not ROUND_DISC_NEG.search(line):
            fails.append((n, 'round-disc-vegvisir', line.strip()[:220]))
        if SUN_BOLT_ON_EMBLEM.search(line) and not SUN_BOLT_NEG.search(line):
            fails.append((n, 'sun-or-bolt', line.strip()[:220]))
    return fails

def shield_lock_missing(path):
    text = open(path, encoding='utf-8').read()
    missing = []
    for name, pat in SHIELD_REQUIRED:
        if not pat.search(text):
            missing.append(name)
    return missing

def type_margin():
    import cv2
    T = cv2.imread(TYPE_LAYER, cv2.IMREAD_UNCHANGED)
    if T is None or T.shape[2] < 4:
        raise SystemExit('type layer missing or not RGBA: ' + TYPE_LAYER)
    a = T[..., 3].astype(np.float32) / 255.0
    ys = np.where(a > ALPHA_THRESHOLD)[0]
    if len(ys) == 0:
        raise SystemExit('no type pixels above ALPHA_THRESHOLD %.2f' % ALPHA_THRESHOLD)
    ymin = int(ys.min())
    margin = ymin - TRIM_PX
    return ymin, margin, margin / DPI

def main():
    bad = 0
    for rel in SCAN:
        path = os.path.join(ROOT, rel)
        for n, kind, text in eye_failures(path):
            bad += 1
            print('EYE %s %s:%d %s' % (kind, rel, n, text))
        if rel in SHIELD_LOCK_FILES:
            for name in shield_lock_missing(path):
                bad += 1
                print('SHIELD REQUIRE %s missing %s' % (rel, name))
    ymin, margin, inches = type_margin()
    print('TYPE alpha > %.2f ymin %d trim_px %.1f margin_px %.1f (%.4f in)' % (
        ALPHA_THRESHOLD, ymin, TRIM_PX, margin, inches))
    if margin + 1e-6 < MIN_MARGIN_PX:
        bad += 1
        print('TYPE FAIL: margin %.2f px is under %d px' % (margin, MIN_MARGIN_PX))
    if bad:
        sys.exit(1)
    print('check_costume_lock: ok')

if __name__ == '__main__':
    main()
