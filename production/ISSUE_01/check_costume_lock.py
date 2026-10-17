#!/usr/bin/env python3
"""ISSUE01 costume lock (Sherif, 2026-10-16).

Eye placement: an Eye of Horus may appear only in the halo sigil and on the
pauldron seal. The check fails if a scanned line gives one to the shield or
the hammer.

Shield shape: the check fails on "kite shield" or an emerald eye-seal on the
shield, unless the same line marks that wording amended, superseded, or history.

Shield emblem (Wild, 2026-10-16, 2:20 PM ET): the current written lock in the
four costume files must name the tall pointed outline, the Vegvísir elongated
vertically, the gold interlaced knotwork, the band of gold knotwork and abstract glyph marks, and the
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
    '12_SCALE_ENVIRONMENT_BIBLE.md',
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
    r'an eye on the hammer is a reject|reject: any eye on the hammer|hammer eye rejected',
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
    ('glyph band', re.compile(
        r'band of gold knotwork and abstract glyph marks inside the gold rim, '
        r'decorative only, never letter-like', re.I)),
    ('decorative only', re.compile(r'decorative only', re.I)),
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
# Hammer head (ISSUE01-HAMMER-BLOCK-HEAD-1, Sherif 2026-10-16, 6:45 PM ET).
# The live lock is a plain rectangular block head. A triangle top stated as a
# current requirement fails unless the same line marks it retired, superseded,
# history, amended, or a reject. A line that still bans the rectangular block
# fails the same way.
HAMMER_LOCK_FILES = [
    '09_CHARACTER_BIBLE.md',
    'production/ISSUE_01/ISSUE_01_PRODUCTION.md',
    'production/ISSUE_01/RENDER_CHECKLIST.md',
    'production/ISSUE_01/bible/CHARACTER_BIBLE.md',
    'production/ISSUE_01/bible/kdp/README.md',
    '00_FIDELITY_PROTOCOL.md',
    '01_VISUAL_STYLE_GUIDE.md',
    '04_VISUAL_CANON.md',
    'README.md',
]
# Shape phrases belong in every hammer-lock file, including a short pointer.
# The Mjölnir name, the Marvel guardrail and the trademark check stay in the
# main locks only. Generator prompts use the canonical hammer line and must
# not carry that meta text.
HAMMER_SHAPE_REQUIRED = (
    ('plain rectangular block head', re.compile(r'plain rectangular block head', re.I)),
    ('cone-bottom hilt', re.compile(r'cone-bottom hilt')),
    ('no eye', re.compile(r'\bno eye\b|no Eye of Horus on the hammer')),
    # Sherif, 2026-10-16, 11:16–11:18 PM ET. One bolt on each broad side,
    # striking ends plain, and the head-down mass with Sentinel Rest.
    ('two broad side faces only', re.compile(r'two broad side faces only')),
    ('striking ends plain', re.compile(r'striking ends plain')),
    ('Sentinel Rest', re.compile(r'Sentinel Rest')),
    ('long sturdy haft to lean on', re.compile(r'long sturdy haft to lean on')),
    ('stands on its head', re.compile(r'massive block-head hammer that stands on its head')),
)
HAMMER_GUARDRAIL_FILES = [
    '09_CHARACTER_BIBLE.md',
    'production/ISSUE_01/ISSUE_01_PRODUCTION.md',
    'production/ISSUE_01/bible/CHARACTER_BIBLE.md',
    '00_FIDELITY_PROTOCOL.md',
    '04_VISUAL_CANON.md',
]
HAMMER_GUARDRAIL_REQUIRED = (
    ('Mjölnir remix', re.compile(r'remix of the mythological Mjölnir \(Norse myth\)')),
    ('Marvel guardrail', re.compile(r'never Marvel')),
    ('trademark check', re.compile(r'trademark check')),
)
PROMPT_META = re.compile(r'Mjölnir|never Marvel|trademark check')
# ISSUE01-HALO-RINGS-ARMOR-REF-1 (Wild, 2026-10-16, 11:00 PM ET, delegated by
# Sherif at 10:58 PM ET; pauldron refs and symbol palette, Sherif, 11:06 PM ET).
# The meaning line stays in the two character bibles. Generator prompts, and
# every other scanned file, must not carry it.
ICON_LOCK_FILES = [
    '09_CHARACTER_BIBLE.md',
    'production/ISSUE_01/ISSUE_01_PRODUCTION.md',
    'production/ISSUE_01/RENDER_CHECKLIST.md',
    'production/ISSUE_01/bible/CHARACTER_BIBLE.md',
]
BIBLE_NOTE_FILES = (
    '09_CHARACTER_BIBLE.md',
    'production/ISSUE_01/bible/CHARACTER_BIBLE.md',
)
MEANING_RE = re.compile(r"Light Soul of TOLC's Primordial Source")
ICON_REQUIRED = (
    ('three thin concentric rings', re.compile(r'three thin concentric rings')),
    ('rays still reaching past', re.compile(r'rays still reaching past them')),
    ('eight fine radial spokes', re.compile(r'[Ee]ight fine radial spokes')),
    ('bright white-gold', re.compile(r'bright white-gold')),
    ('faint rose-gold thread', re.compile(r'faint rose-gold thread')),
    ('no glyphs on the rings', re.compile(r'no glyphs on the rings')),
    ('the halo rings', re.compile(r'the halo rings')),
    ('never named, captioned or numbered', re.compile(r'never named, captioned or numbered')),
    ('abstract glyph marks', re.compile(r'abstract glyph marks')),
    ('never letter-like', re.compile(r'never letter-like')),
    ('molten-gold inlay', re.compile(r'molten-gold inlay')),
    ('forged for an eternal deity', re.compile(r'as if forged for an eternal deity')),
    ('no readable text', re.compile(r'no readable text')),
    ('Vegvísir stays the centre', re.compile(r'Vegv[ií]sir stays the centre')),
    ('oversized but wearable', re.compile(r'oversized but wearable')),
    ('rounded-angular', re.compile(r'rounded-angular')),
    ('about 1.3x the natural shoulder', re.compile(r'about 1\.3x the natural shoulder')),
    ('two or three layered lames', re.compile(r'two or three layered lames')),
    ('no wing extensions', re.compile(r'no wing extensions')),
    ('not dozens of feathers', re.compile(r'not dozens of feathers')),
    ('thick layered belt', re.compile(r'thick layered belt')),
    ('bulkier gauntlets', re.compile(r'bulkier gauntlets')),
    ('black armor with gold trim', re.compile(r'black armor with gold trim')),
    ('gold sun buckle', re.compile(r'gold sun buckle')),
    ('not a variant', re.compile(r'not a variant')),
    ('Style-proof iconic forms', re.compile(r'Style-proof iconic forms')),
    ('shape count', re.compile(r'shape count')),
    ('detail layer', re.compile(r'detail layer')),
    ('pauldron prompt', re.compile(
        r'oversized but wearable rounded gold-rimmed pauldrons capping the shoulders, '
        r'each with a large carved emerald winged Eye of Horus; no wing extensions')),
    ('one eye, two wings', re.compile(r'one eye, two wings')),
    ('few large feather bands', re.compile(r'few large feather bands')),
    ('gold-rimmed black', re.compile(r'gold-rimmed black')),
    ('both shoulders', re.compile(r'both shoulders')),
    ('pauldron ref a', re.compile(r'pauldron_winged_eye_ref_a_2026-10-16\.jpg')),
    ('pauldron ref b', re.compile(r'pauldron_winged_eye_ref_b_2026-10-16\.jpg')),
    ('pauldron ref c', re.compile(r'pauldron_winged_eye_ref_c_2026-10-16\.jpg')),
    ('emerald-tablet green', re.compile(r'emerald-tablet green')),
    ('symbol palette prompt', re.compile(r'gold and emerald-green symbol palette')),
    ('open options, not locks', re.compile(r'[Oo]pen options, not locks')),
    ('not redrawn here', re.compile(r'not redrawn here')),
    ('COMICS track', re.compile(r'COMICS track')),
    ('ANIMATED SERIES track', re.compile(r'ANIMATED SERIES track')),
    ('proposed direction, not final', re.compile(r'proposed direction, not final')),
    ('books come first', re.compile(r'[Bb]ooks come first')),
    ('panels and covers inked track', re.compile(
        r'All comic production, panels and covers, uses the COMICS \(inked\) track')),
    ('style line governs panels', re.compile(
        r'The \[style\] line still governs panel prompts')),
    ('decided later, after the books', re.compile(r'decided later, after the books')),
    ('only the rendering style differs', re.compile(r'[Oo]nly the rendering style differs')),
    ('rest-pose draft', re.compile(r'rest_pose_pauldrons_draft_2026-10-16\.jpg')),
    ('x style ref', re.compile(r'x_ref_photo_2026-10-16\.jpg')),
    ('Eyes are too small', re.compile(r'Eyes are too small')),
    ('shield lost its Vegvísir', re.compile(r'shield lost its Vegv[ií]sir')),
    ('halo rings are faint', re.compile(r'halo rings are faint')),
    # 3D LOGIC and the scale lock (Wild, 2026-10-16 11:38 PM ET, Sherif-delegated).
    # Observable review wording. Do not require "ellipse" or "always".
    ('3D LOGIC', re.compile(r'3D LOGIC')),
    ('one wingtip', re.compile(r'one wingtip')),
    ('one wing tip', re.compile(r'one wing tip')),
    ('full winged Eye', re.compile(r'full winged Eye')),
    ('visible rim thickness', re.compile(r'visible rim thickness')),
    ('key-light direction', re.compile(r'key-light direction')),
    ('halo is light, not an object', re.compile(r'halo is light, not an object')),
    ('flat circle facing the camera', re.compile(r'flat circle facing the camera')),
    ('not foreshortened', re.compile(r'not foreshortened')),
    ('flat pasted-on symbols fail', re.compile(r'Flat or pasted-on symbols fail review')),
    ('lighting from the wrong side', re.compile(r'lighting from the wrong side')),
    ('must READ as 3D', re.compile(r'must READ as 3D')),
    ('shoulder emblems drawn in perspective', re.compile(r'shoulder emblems drawn in perspective')),
    ('physically wearable armour', re.compile(r'physically wearable armour')),
    ("viewer's left", re.compile(r"viewer's left")),
    ('7 ft 0 in', re.compile(r'7 ft 0 in')),
    ('213 cm', re.compile(r'213 cm')),
    ('about 25 cm per head', re.compile(r'about 25 cm per head')),
    ('5 ft 9 in', re.compile(r'5 ft 9 in')),
    ('175 cm', re.compile(r'175 cm')),
    ('about 1.22', re.compile(r'about 1\.22')),
    ('eyes line up with his upper chest', re.compile(r'eyes line up with his upper chest')),
    ('1.5 heads in diameter', re.compile(r'1\.5 heads in diameter')),
    ('Sentinel Rest geometry', re.compile(r'Sentinel Rest geometry')),
    ('Everything else stays PROPOSED', re.compile(r'Everything else stays PROPOSED')),
    ('turnaround sheet', re.compile(r'turnaround sheet')),
    ('height lineup', re.compile(r'height lineup')),
)
CANONICAL_PROMPTS = (
    'a radiant glowing Eye of Horus halo above his head, framed by three thin concentric rings of light joined by eight fine radial spokes, set inside the original sun-ray burst; bright white-gold inner ring fading to soft gold, faint rose-gold thread on the outer ring; clean, symmetrical, sacred-geometry precision',
    'shield face deeply engraved with gold knotwork and abstract glyph marks, decorative only, never letter-like (no real runic or Latin letter shapes) around the glowing Vegvísir, molten-gold inlay, flawless master-forged metalwork as if forged for an eternal deity, purely decorative patterns, no letters, no readable text, no words',
    'oversized but wearable rounded gold-rimmed pauldrons capping the shoulders, each with a large carved emerald winged Eye of Horus; no wing extensions',
    'gold and emerald-green symbol palette',
    'shoulder emblems drawn in perspective on the curved plates: the turned-away shoulder shows the emerald Eye with one wing tip, the facing shoulder shows the full winged Eye',
    'designed as consistent 3D objects; correct perspective and foreshortening on surface emblems; the halo stays a flat circle of light facing the camera and is not foreshortened; physically wearable armour',
    'All 2D art, inked panels and covers alike, must READ as 3D: solid volumes, consistent light direction with form shading and cast shadows, correct perspective and overlap, and emblems that wrap their surfaces. Flat or pasted-on symbols fail review.',
)
PAULDRON_REFS = (
    'production/ISSUE_01/bible/refs/pauldron_winged_eye_ref_a_2026-10-16.jpg',
    'production/ISSUE_01/bible/refs/pauldron_winged_eye_ref_b_2026-10-16.jpg',
    'production/ISSUE_01/bible/refs/pauldron_winged_eye_ref_c_2026-10-16.jpg',
    'production/ISSUE_01/bible/refs/rest_pose_pauldrons_draft_2026-10-16.jpg',
    'production/ISSUE_01/bible/refs/x_ref_photo_2026-10-16.jpg',
)
CANON_PROMPT_TAIL = re.compile(
    r'[Cc]anonical\b[^\n:]*prompt line\**(?:\s*\([^)\n]*\))?\**\s*:\**\s*(.*)$'
)
LOCK_PROMPT_HEAD = '### Costume lock prompts'
TRIANGLE_POS = re.compile(r'triangle at the top|triangle top|triangle-and-cone', re.I)
TRIANGLE_NEG = re.compile(r'retired|superseded|history|amended|is a reject', re.I)
BLOCK_BAN = re.compile(
    r'never a plain rectangular block|not a plain rectangular block|'
    r'plain rectangular Thor-style block(?: head)?|plain rectangular block hammer head|'
    r'the square block hammer head',
    re.I)
BLOCK_BAN_NEG = re.compile(r'retired|superseded|history|amended', re.I)

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
        if TRIANGLE_POS.search(line) and not TRIANGLE_NEG.search(line):
            fails.append((n, 'triangle-top', line.strip()[:220]))
        if BLOCK_BAN.search(line) and not BLOCK_BAN_NEG.search(line):
            fails.append((n, 'block-ban', line.strip()[:220]))
    return fails

def shield_lock_missing(path):
    text = open(path, encoding='utf-8').read()
    missing = []
    for name, pat in SHIELD_REQUIRED:
        if not pat.search(text):
            missing.append(name)
    return missing

def hammer_lock_missing(path, required):
    text = open(path, encoding='utf-8').read()
    missing = []
    for name, pat in required:
        if not pat.search(text):
            missing.append(name)
    return missing

def prompt_texts(path):
    """Generator-prompt text.

    Blockquote and Prompt: lines are prompts. So is the tail of a canonical
    prompt line. In RENDER_CHECKLIST the costume-lock prompt block is scanned
    in full, so a prompt that does not start with '>' is still checked.
    """
    rel_check = path.endswith('RENDER_CHECKLIST.md')
    in_lock = False
    for n, line in enumerate(open(path, encoding='utf-8'), 1):
        if rel_check and line.startswith(LOCK_PROMPT_HEAD):
            in_lock = True
        elif in_lock and line.startswith('## '):
            in_lock = False
        s = line.lstrip()
        if s.startswith('>') or s.startswith('Prompt:'):
            yield n, line
        elif in_lock and line.strip():
            yield n, line
        else:
            m = CANON_PROMPT_TAIL.search(line)
            if m and m.group(1).strip():
                yield n, m.group(1)

def prompt_meta_failures(path):
    fails = []
    for n, text in prompt_texts(path):
        if PROMPT_META.search(text) or MEANING_RE.search(text):
            fails.append((n, text.strip()[:220]))
    return fails

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
        if rel in HAMMER_LOCK_FILES:
            for name in hammer_lock_missing(path, HAMMER_SHAPE_REQUIRED):
                bad += 1
                print('HAMMER REQUIRE %s missing %s' % (rel, name))
            if rel in HAMMER_GUARDRAIL_FILES:
                for name in hammer_lock_missing(path, HAMMER_GUARDRAIL_REQUIRED):
                    bad += 1
                    print('HAMMER REQUIRE %s missing %s' % (rel, name))
        if rel in (
            'production/ISSUE_01/ISSUE_01_PRODUCTION.md',
            'production/ISSUE_01/RENDER_CHECKLIST.md',
        ):
            for n, text in prompt_meta_failures(path):
                bad += 1
                print('PROMPT META %s:%d %s' % (rel, n, text))
        if rel in ICON_LOCK_FILES:
            for name in hammer_lock_missing(path, ICON_REQUIRED):
                bad += 1
                print('ICON REQUIRE %s missing %s' % (rel, name))
        if rel not in BIBLE_NOTE_FILES and MEANING_RE.search(open(path, encoding='utf-8').read()):
            bad += 1
            print('MEANING %s must stay in the character bibles' % rel)
    for rel in HAMMER_LOCK_FILES:
        if rel in SCAN:
            continue
        path = os.path.join(ROOT, rel)
        for n, kind, text in eye_failures(path):
            if kind not in ('triangle-top', 'block-ban'):
                continue
            bad += 1
            print('EYE %s %s:%d %s' % (kind, rel, n, text))
        for name in hammer_lock_missing(path, HAMMER_SHAPE_REQUIRED):
            bad += 1
            print('HAMMER REQUIRE %s missing %s' % (rel, name))
        if rel in HAMMER_GUARDRAIL_FILES:
            for name in hammer_lock_missing(path, HAMMER_GUARDRAIL_REQUIRED):
                bad += 1
                print('HAMMER REQUIRE %s missing %s' % (rel, name))
    for rel in BIBLE_NOTE_FILES:
        path = os.path.join(ROOT, rel)
        if not MEANING_RE.search(open(path, encoding='utf-8').read()):
            bad += 1
            print('MEANING REQUIRE %s missing the halo-rings meaning' % rel)
    checklist = os.path.join(ROOT, 'production/ISSUE_01/RENDER_CHECKLIST.md')
    checklist_text = open(checklist, encoding='utf-8').read()
    if LOCK_PROMPT_HEAD not in checklist_text:
        bad += 1
        print('PROMPT BLOCK missing from RENDER_CHECKLIST.md')
    for line in CANONICAL_PROMPTS:
        if line not in checklist_text:
            bad += 1
            print('PROMPT LINE missing from RENDER_CHECKLIST.md')
    for rel in PAULDRON_REFS:
        if not os.path.isfile(os.path.join(ROOT, rel)):
            bad += 1
            print('PAULDRON REF missing %s' % rel)
    production = open(os.path.join(ROOT, 'production/ISSUE_01/ISSUE_01_PRODUCTION.md'), encoding='utf-8').read()
    if 'into rune knotwork on the haft (superseded by the 2026-10-16 block head' not in production:
        bad += 1
        print('C8 haft knotwork is not tagged superseded by the 2026-10-16 block head')

    scale = os.path.join(ROOT, '12_SCALE_ENVIRONMENT_BIBLE.md')
    if not os.path.isfile(scale):
        bad += 1
        print('SCALE missing 12_SCALE_ENVIRONMENT_BIBLE.md')
    else:
        scale_text = open(scale, encoding='utf-8').read()
        for phrase in (
            '3D LOGIC',
            '7 ft 0 in',
            '213 cm',
            '5 ft 9 in',
            '175 cm',
            'about 1.22',
            '8.5 heads',
            'about 25 cm per head',
            '1.3x the natural shoulder',
            'Sentinel Rest',
            '1.5 heads',
            'not foreshortened',
            'scale stays fixed across the camera',
            'whose eyes meet his upper chest',
        ):
            if phrase not in scale_text:
                bad += 1
                print('SCALE REQUIRE missing %s' % phrase)
    scale_prompt = 'scale stays fixed across the camera: Ra-Thor reads 7 ft 0 in armoured from sole to helm crest'
    for rel in (
        'production/ISSUE_01/ISSUE_01_PRODUCTION.md',
        'production/ISSUE_01/RENDER_CHECKLIST.md',
        '01_VISUAL_STYLE_GUIDE.md',
    ):
        if scale_prompt not in open(os.path.join(ROOT, rel), encoding='utf-8').read():
            bad += 1
            print('SCALE PROMPT missing %s' % rel)
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
