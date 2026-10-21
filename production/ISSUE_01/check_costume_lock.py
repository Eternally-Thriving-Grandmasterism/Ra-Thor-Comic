#!/usr/bin/env python3
"""ISSUE01 costume lock (Sherif, 2026-10-16; LOOK LOCK, Sherif, 2026-10-18).

Eye placement: an Eye of Horus may appear only on the pauldron Eyes (the
halo sigil is retired by the LOOK LOCK). The check fails if a scanned line gives one to the shield or
the hammer.

LOOK LOCK (Sherif, 2026-10-18 1:58 AM ET: "Lock it as is, and update the
bible to match the art."; CANON-SYNC-LOOK-LOCK-1): the costume files must
carry the locked look: the black kite shield with a gold sun-spoke design and
a central gold boss, the all-gold halo with no eye in the halo, the round gold
buckle, the gold Greek-key engraving, and emerald only on the pauldron Eyes.
The Vegvísir shield (and its elongated form), the Eye of Horus in the halo,
the eight halo spokes, the rose-gold buckle, the
bronze-gold cape lining and the helm-side wings are history. A scanned line
that still states one of them as current fails, unless the same line marks it
superseded, history, retired, amended, moot, resolved or a reject. A negation
word (no, not, never, without, was, ...) exempts only the phrase it directly
governs: it must sit within a few words before the match in the same clause.
A line that puts emerald on any figure part other than the pauldron Eyes fails
the same way. The kite shield is canon again, so "kite shield" no longer fails.

DUAL LOOK LOCK (Sherif 2026-10-21 2:30 PM ET): two locked looks, PRINT
(comic pages, covers, KDP) and ANIMATED (screen/, trailer, 3D, Blender). The
check requires both refs, the DUAL LOOK LOCK section in the Issue #1 Bible
and both prompt stems in 01. The stacked-hands rest is valid again; the
sun-spoke kite shield is an optional prop (Sherif 2:31 PM ET).

Scan scope: the stale check covers the files in SCAN and STALE_SCAN.
Untagged-term guard (AMEND-3): any eye-seal or hawk-seal mention in a scanned
file fails unless it is tagged, directly negated, or a keep-clear-zone phrase.

Tests: run `python3 production/ISSUE_01/test_costume_lock.py` from the repo
root (plain python3, no third-party deps). It copies the repo's .md files to
a temp dir, injects each must-fail / must-pass line, and runs the text checks
(the type-margin check needs numpy and cv2 and is skipped there).
STALE_SCAN includes the episode files, production/S*/*/ART_PROMPTS.md,
screen/*/STORYBOARD_PROMPTS.md, docs/TRAILER_S1E01.md,
research/naming_rd_brief.md and the season files. (The deferral to
CANON-SYNC-LOOK-LOCK-2 is resolved: that card tagged those files and added
LOOK LOCK prompts to the prompt files, 2026-10-18.)

Type margin: every type pixel whose alpha is greater than ALPHA_THRESHOLD
must sit at least 75 px (0.25 in) inside the trim at 300 dpi. The trim line
is 0.125 in, which is 37.5 px, not the 37 px bleed constant used by the
sheet builders.
"""
import os, sys, re

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
# Further docs scanned for stale current-tense costume lines only
# (CANON-SYNC-LOOK-LOCK-1 AMEND).
STALE_SCAN = [
    'README.md',
    'production/ISSUE_01/HANDOFF.md',
    'production/ISSUE_01/STORE_LISTING_AND_EXPORT.md',
    'production/ISSUE_01/CREDITS_AND_INDICIA.md',
    'production/ISSUE_01/PROPOSED_SPEAKER_RULINGS.md',
    'production/ISSUE_01/bible/kdp/README.md',
    # CANON-SYNC-LOOK-LOCK-2 (2026-10-18): the deferred docs.
    'docs/TRAILER_S1E01.md',
    'research/naming_rd_brief.md',
    # CANON-SYNC-LOOK-LOCK-2 AMEND-2.
    '03_TONE_SPECS.md',
    '05_LORE_BIBLE.md',
    'docs/LORE_BRIDGE_POWRUSH_RATHOR.md',
    # CANON-SYNC-LOOK-LOCK-2 AMEND-3.
    'screen/SCREEN_BIBLE_ADDENDUM.md',
    'production/README.md',
    'bots/GROKBOT_COMIC_SEAT.md',
    'OWNERSHIP-NOTE-2026-10.md',
    'docs/LIGHT_OCEAN_FORGED_BY_TOLC_SERIES_SEED.md',
]
STALE_GLOBS = (
    'episodes/*.md',
    'production/S*/*/ART_PROMPTS.md',
    'screen/*/STORYBOARD_PROMPTS.md',
    'seasons/*.md',
    # AMEND-3.
    'production/S*/*/SCRIPT.md',
    'production/S*/*/MUSIC_CUES.md',
    'screen/S1E0[12]/*.md',
)
import glob as _glob
for _g in STALE_GLOBS:
    for _f in sorted(_glob.glob(os.path.join(ROOT, _g))):
        _rel = os.path.relpath(_f, ROOT)
        if _rel not in SCAN and _rel not in STALE_SCAN:
            STALE_SCAN.append(_rel)
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
EMERALD_SEAL_POS = re.compile(r'emerald eye-seal', re.I)
EMERALD_SEAL_NEG = re.compile(
    r'no emerald eye-seal|superseded|history|amended',
    re.I)
# LOOK LOCK (CANON-SYNC-LOOK-LOCK-1). Sherif, 2026-10-18 1:58 AM ET: "Lock it
# as is, and update the bible to match the art." Every costume-lock file must
# name the locked look.
LOOK_FILES = [
    '00_FIDELITY_PROTOCOL.md',
    '01_VISUAL_STYLE_GUIDE.md',
    '04_VISUAL_CANON.md',
    '09_CHARACTER_BIBLE.md',
    'production/ISSUE_01/ISSUE_01_PRODUCTION.md',
    'production/ISSUE_01/RENDER_CHECKLIST.md',
    'production/ISSUE_01/bible/CHARACTER_BIBLE.md',
]
LOOK_REQUIRED = (
    ('LOOK LOCK', re.compile(r'LOOK LOCK')),
    ('black kite shield', re.compile(r'black kite shield', re.I)),
    ('gold sun-spoke design', re.compile(r'gold sun-spoke design', re.I)),
    ('central gold boss', re.compile(r'central gold boss', re.I)),
    ('no eye in the halo', re.compile(r'no eye in the halo', re.I)),
    ('round gold buckle', re.compile(r'round gold (?:belt )?buckle', re.I)),
    ('gold Greek-key', re.compile(r'gold Greek-key', re.I)),
    ('emerald only on the pauldron Eyes', re.compile(
        r'emerald (?:appears )?only on the (?:two )?pauldron Eyes', re.I)),
    ('tall look-lock ref', re.compile(r'rathor_look_lock_imagine_tall_2026-10-18\.jpg')),
)
# Retired costume parts stated as current (CANON-SYNC-LOOK-LOCK-1, Hands and
# Wild AMEND 2026-10-18). Two kinds of exemption:
#   * a supersession tag (superseded, history, retired, amended, moot,
#     resolved, reject) anywhere on the line exempts the whole line;
#   * a negation word (no, not, never, without, nor, was, were, once, ...)
#     exempts only the phrase it directly negates: it must sit within the
#     NEG_WINDOW words just before the match, in the same clause (no , ; : .
#     ( ) between). So "no eye in the halo" never exempts a Vegvísir shield
#     elsewhere on the line.
# Headings of superseded, history, reject or conflict sections, and dated
# history-table rows, are skipped.
STALE_CURRENT = (
    ('vegvisir', re.compile(r'Vegv[ií]sir', re.I)),
    ('halo-eye', re.compile(
        r'Eye of Horus (?:halo|sigil|disc)|Eye of Horus in the halo|halo(?:\'s)? Eye of Horus|'
        r'Eye of Horus sigil|halo sigil', re.I)),
    ('eight-spokes', re.compile(r'eight (?:fine )?(?:radial )?spokes', re.I)),
    ('rose-gold-buckle', re.compile(
        r'rose[- ]gold (?:lightning[- ])?(?:bolt )?buckle|buckle[^.;]{0,40}(?P<term>rose[- ]gold)', re.I)),
    # The rose-gold bolt (buckle bolt, hammer-face bolt). The cover title
    # hyphen is type, not costume, and is exempted below.
    ('rose-gold-bolt', re.compile(
        r'rose[- ]gold (?:lightning[- ]?)?bolt|rose gold only for the bolt|'
        r'buckle-centre bolt|bolt[^.;]{0,25}\bis (?P<term>rose gold)', re.I)),
    # BIBLE-DUAL-LOOK-LOCK-1 (2026-10-21): both hands stacked on the pommel is
    # the rest in both locked looks again, so 'stacked-hands' is no longer stale.
    ('bronze-gold-lining', re.compile(r'bronze-gold', re.I)),
    ('helm-side-wings', re.compile(
        r'wings are fixed to the sides|compact (?:up-swept )?(?:gold )?(?:helm )?wings|'
        r'wings? no wider than the shoulders', re.I)),
    # CANON-SYNC-LOOK-LOCK-2 AMEND-2: pre-lock costume terms, scoped to
    # Ra-Thor's costume. Keep-clear uses ("eye-seal zone", "clear of the
    # eye-seal", "eye-seal rerun") and scenery ("circuit-plate workshop",
    # "lab", "walls") do not match.
    ('eye-seal', re.compile(
        r'(?P<term>(?:emerald |gold )?eye-seal) (?:kite )?shield|'
        r'shield with (?:the |an |its )?(?P<term2>(?:emerald )?eye-seal)|'
        r'(?P<term3>eye-seal) (?:in circuit inlay )?on (?:the|a|its) (?:gold )?(?:kite )?shield|'
        r'emerald (?:only )?(?:on|for) the (?P<term4>eye-seal)|(?P<term5>eye-seal) only|'
        r'reserved for the (?P<term6>eye-seal)|[Cc]anon emblem[^.;|]{0,40}(?P<term7>eye-seal)', re.I)),
    ('hawk-seal', re.compile(r'(?P<term>hawk[- ](?:shaped )?(?:pauldron |shoulder )?seal)', re.I)),
    ('circuit-plate-armour', re.compile(
        r'(?P<term>circuit[- ]plate) armou?r|Ra-Thor[^.;]{0,40}(?P<term2>circuit[- ]?plate)(?! workshop| lab| walls?)|'
        r'(?P<term3>circuit[- ]plate) is Ra-Thor|(?P<term4>gold circuit plate) \(winged', re.I)),
    ('winged-halo', re.compile(r'(?P<term>\bwinged[- ]halo)', re.I)),
    ('polished-gold-hammer', re.compile(
        r'all metal polished antique gold|polished antique[- ]gold (?:thunder )?hammer|'
        r'hammer[^.;]{0,20}\bpolished antique gold', re.I)),
)
LINE_TAG = re.compile(
    r'supersed|history|historical|retired|amended|\bmoot\b|resolved|reject', re.I)
NEG_WORD = re.compile(
    r'\b(?:no|not|never|without|nor|was|were|once|formerly|instead of|rather than|no longer)\b',
    re.I)
NEG_WINDOW = 6
# 'but' and 'yet' also break a clause: in 'not silver or navy but a Vegvísir
# shield' the 'not' does not reach the Vegvísir.
CLAUSE_BREAK = re.compile(r'[,;:.()\[\]!?]|\bbut\b|\byet\b', re.I)
TYPE_CONTEXT = re.compile(r'title|hyphen|lettering|cover[- ]mark|\bmark\b|RA⚡THOR|type', re.I)
HISTORY_ROW = re.compile(r'^\s*\|\s*(?:Oct |Sep |~|PR |#|R\d)')
RECORD_HEAD = re.compile(r'supersed|history|reject|conflict', re.I)

DUAL_REFS = [
    'production/ISSUE_01/bible/refs/rathor_look_lock_print_2026-10-21.jpg',
    'production/ISSUE_01/bible/refs/rathor_look_lock_animated_2026-10-21.jpg',
]
DUAL_REQUIRED = [
    ('production/ISSUE_01/bible/CHARACTER_BIBLE.md', (
        '## DUAL LOOK LOCK 2026-10-21', 'rathor_look_lock_print_2026-10-21.jpg',
        'rathor_look_lock_animated_2026-10-21.jpg', 'PRINT LOOK prompt line:',
        'ANIMATED LOOK prompt line:', 'OPTIONAL prop', '**Buckle bolt.**')),
    ('01_VISUAL_STYLE_GUIDE.md', (
        '## DUAL LOOK LOCK (2026-10-21)', '**Prompt stem, PRINT look',
        '**Prompt stem, ANIMATED look')),
    ('04_VISUAL_CANON.md', ('## DUAL LOOK LOCK (2026-10-21)',)),
    ('09_CHARACTER_BIBLE.md', ('**DUAL LOOK LOCK',)),
    ('production/ISSUE_01/HANDOFF.md', ('DUAL LOOK LOCK',)),
]

def term_start(m):
    """Where the retired term itself starts. For patterns that lead with a
    context word (e.g. 'buckle ... rose gold'), the negation must govern the
    retired term, so 'round gold, no rose-gold buckle' passes."""
    for g in m.re.groupindex:
        if g.startswith('term') and m.group(g) is not None:
            return m.start(g)
    return m.start()

# A negation does not reach past a verb or an "and" to the retired term:
# in "the buckle not silver is rose gold" the "not" governs "silver" only.
NEG_BLOCK = re.compile(
    r'\b(?:is|are|be|becomes?|reads?|stays?|has|have|carries|shows?|bears?|'
    r'holds?|wears?|and)\b', re.I)

def negated(line, start):
    """True if a negation directly governs the phrase starting at `start`."""
    before = line[max(0, start - 80):start]
    parts = CLAUSE_BREAK.split(before)
    clause = parts[-1] if parts else ''
    window = ' '.join(clause.split()[-NEG_WINDOW:])
    negs = list(NEG_WORD.finditer(window))
    if not negs:
        return False
    between = window[negs[-1].end():]
    return not NEG_BLOCK.search(between)

# Emerald on a figure part other than the pauldron Eyes. Cover type (the coin)
# and the R1 reference record are not costume.
EMERALD_FIG = re.compile(
    r'emerald[^.;,]{0,25}\b(?:shield|halo|buckle|chest|hammer|visor|helm|cape|wings?)\b|'
    r'\b(?:shield|halo|buckle|chest|hammer|visor|helm|cape)\b[^.;,]{0,20}\b(?P<term>emerald)', re.I)
EMERALD_LINE_OK = re.compile(r'\bcoin\b|\bR1\b', re.I)
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
    # 'cone-bottom hilt' is no longer required: the LOOK LOCK ref hides the
    # pommel under his fist (CANON-SYNC-LOOK-LOCK-1, Clerk nit L12/L85).
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
    ('the halo rings', re.compile(r'the halo rings')),
    ('never named, captioned or numbered', re.compile(r'never named, captioned or numbered')),
    ('bulkier gauntlets', re.compile(r'bulkier gauntlets')),
    ('black armor with gold trim', re.compile(r'black armor with gold trim')),
    ('not a variant', re.compile(r'not a variant')),
    ('Style-proof iconic forms', re.compile(r'Style-proof iconic forms')),
    ('shape count', re.compile(r'shape count')),
    ('detail layer', re.compile(r'detail layer')),
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
    # 3D LOGIC and the scale lock (Wild, 2026-10-16 11:38 PM ET, Sherif-delegated).
    # Observable review wording. Do not require "ellipse" or "always".
    ('3D LOGIC', re.compile(r'3D LOGIC')),
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
    ('Sentinel Rest geometry', re.compile(r'Sentinel Rest geometry')),
    ('Everything else stays PROPOSED', re.compile(r'Everything else stays PROPOSED')),
    ('turnaround sheet', re.compile(r'turnaround sheet')),
    ('height lineup', re.compile(r'height lineup')),
)
# LOOK LOCK generator lines (RENDER_CHECKLIST.md §5).
CANONICAL_PROMPTS = (
    'Ra-Thor in glossy black armour with gold trim and gold Greek-key engraving, black helm with gold Spartan-style face plates forming a T-visor and a gold centre ridge, two large gold feathered wings rising from behind the head, an all-gold halo centred behind the head: a gold Greek-key disc, two thin gold rings and seven straight gold sun rays, no eye in the halo, a glowing gold sun disc in a gold Greek-key ring on the chest, round gold belt buckle with a gold lightning bolt, gold knee plates, large round black pauldrons with stepped gold rims, each with an emerald-green Eye of Horus outlined in gold, mirrored, tattered black cape, black kite shield with a riveted gold rim and a gold sun-spoke design around a central gold boss, dark stone-metal rectangular block-head hammer with one gold lightning bolt on each broad side face, striking ends plain, cross-wrapped haft with gold bands, no eye; emerald only on the pauldron Eyes; no rose gold, no teal, no blue',
    'dark stone-metal rectangular block-head war hammer, one gold lightning bolt set into each of the two broad side faces only; striking ends plain, massive block-head hammer that stands on its head; long sturdy haft to lean on, cross-wrapped haft with gold bands, no eye',
    'gold and emerald-green symbol palette',
    'shoulder emblems drawn in perspective on the curved plates: the turned-away shoulder shows the emerald Eye foreshortened, the facing shoulder shows the full Eye with its stripe bands',
    'designed as consistent 3D objects; correct perspective and foreshortening on surface emblems; the halo stays a flat circle of light facing the camera and is not foreshortened; physically wearable armour',
    'All 2D art, inked panels and covers alike, must READ as 3D: solid volumes, consistent light direction with form shading and cast shadows, correct perspective and overlap, and emblems that wrap their surfaces. Flat or pasted-on symbols fail review.',
)
PAULDRON_REFS = (
    'production/ISSUE_01/bible/refs/pauldron_winged_eye_ref_a_2026-10-16.jpg',
    'production/ISSUE_01/bible/refs/pauldron_winged_eye_ref_b_2026-10-16.jpg',
    'production/ISSUE_01/bible/refs/pauldron_winged_eye_ref_c_2026-10-16.jpg',
    'production/ISSUE_01/bible/refs/rest_pose_pauldrons_draft_2026-10-16.jpg',
    'production/ISSUE_01/bible/refs/x_ref_photo_2026-10-16.jpg',
    'production/ISSUE_01/bible/refs/rathor_look_lock_imagine_tall_2026-10-18.jpg',
    'production/ISSUE_01/bible/refs/rathor_look_lock_imagine_wide_2026-10-18.jpg',
)
CANON_PROMPT_TAIL = re.compile(
    r'[Cc]anonical\b[^\n:]*prompt line\**(?:\s*\([^)\n]*\))?\**\s*:\**\s*(.*)$'
)
LOCK_PROMPT_HEAD = '### Costume lock prompts (LOOK LOCK, 2026-10-18)'
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
        # AMEND-2: a directly negated hit ('no eye-seal shield') is a guard,
        # not a stale shield eye.
        if (any(not negated(line, m.start()) for m in SHIELD_POS.finditer(line))
                and not SHIELD_NEG.search(line)):
            fails.append((n, 'shield', line.strip()[:220]))
        if EMERALD_SEAL_POS.search(line) and not EMERALD_SEAL_NEG.search(line):
            fails.append((n, 'emerald-seal', line.strip()[:220]))
        if TRIANGLE_POS.search(line) and not TRIANGLE_NEG.search(line):
            fails.append((n, 'triangle-top', line.strip()[:220]))
        if BLOCK_BAN.search(line) and not BLOCK_BAN_NEG.search(line):
            fails.append((n, 'block-ban', line.strip()[:220]))
    return fails

# AMEND-3 untagged-term guard: in a scanned file every eye-seal or hawk-seal
# mention must be tagged (LINE_TAG), directly negated (a guard such as 'no
# eye-seal'), or a recognised layout keep-clear-zone phrase.
SEAL_TERM = re.compile(r'eye[- ]seal|hawk[- ](?:shaped )?(?:pauldron |shoulder )?seal', re.I)
KEEP_CLEAR = re.compile(
    r'keep-clear|clear of the eye[- ]seal|eye[- ]seal (?:keep-clear )?zone|layout (?:keep-clear )?zone', re.I)

def stale_failures(path):
    fails = []
    in_record = False
    for n, line in enumerate(open(path, encoding='utf-8'), 1):
        if line.startswith('#'):
            # A heading names its section; a section of superseded items,
            # history, rejects or conflicts lists retired parts on purpose.
            in_record = bool(RECORD_HEAD.search(line))
            continue
        if in_record or HISTORY_ROW.match(line) or LINE_TAG.search(line):
            continue
        if not KEEP_CLEAR.search(line) and any(
                not negated(line, m.start()) for m in SEAL_TERM.finditer(line)):
            fails.append((n, 'untagged-seal', line.strip()[:220]))
        for kind, pat in STALE_CURRENT:
            for m in pat.finditer(line):
                if negated(line, term_start(m)):
                    continue
                if kind == 'rose-gold-bolt' and TYPE_CONTEXT.search(
                        line[max(0, m.start() - 60):m.end() + 60]):
                    continue
                fails.append((n, kind, line.strip()[:220]))
                break
        if not EMERALD_LINE_OK.search(line):
            for m in EMERALD_FIG.finditer(line):
                if negated(line, term_start(m)) or 'pauldron' in m.group(0).lower():
                    continue
                fails.append((n, 'emerald-off-pauldron', line.strip()[:220]))
                break
    return fails

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
    import numpy as np
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

def main(type_check=True):
    bad = 0
    for rel in SCAN:
        path = os.path.join(ROOT, rel)
        for n, kind, text in eye_failures(path):
            bad += 1
            print('EYE %s %s:%d %s' % (kind, rel, n, text))
        for n, kind, text in stale_failures(path):
            bad += 1
            print('STALE %s %s:%d %s' % (kind, rel, n, text))
        if rel in LOOK_FILES:
            for name in hammer_lock_missing(path, LOOK_REQUIRED):
                bad += 1
                print('LOOK REQUIRE %s missing %s' % (rel, name))
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
    for rel in STALE_SCAN:
        for n, kind, text in stale_failures(os.path.join(ROOT, rel)):
            bad += 1
            print('STALE %s %s:%d %s' % (kind, rel, n, text))
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
            'Sentinel Rest',
            'LOOK LOCK',
            '2.5 head widths',
            'not foreshortened',
            'scale stays fixed across the camera',
            'whose eyes meet his upper chest',
            '## 7. Support system',
            'Ra-Thor offline lattice',
            'Palm to forearm',
            '1 to 1.5 m',
            '150 to 180 cm',
            'gold glow pulse',
            'one gold glow pulse',
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
    support_prompt = 'a connected device assists with one gold glow pulse'
    for rel in (
        '12_SCALE_ENVIRONMENT_BIBLE.md',
        'production/ISSUE_01/RENDER_CHECKLIST.md',
    ):
        if support_prompt not in open(os.path.join(ROOT, rel), encoding='utf-8').read():
            bad += 1
            print('SUPPORT PROMPT missing %s' % rel)
    for rel, phrases in DUAL_REQUIRED:
        path = os.path.join(ROOT, rel)
        text = open(path, encoding='utf-8').read() if os.path.isfile(path) else ''
        for ph in phrases:
            if ph not in text:
                bad += 1
                print('DUAL REQUIRE %s missing %s' % (rel, ph))
    for rel in DUAL_REFS:
        if not os.path.isfile(os.path.join(ROOT, rel)):
            bad += 1
            print('DUAL REF missing %s' % rel)
    if not type_check:
        # test_costume_lock.py runs the text checks only (no numpy/cv2).
        return bad
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
