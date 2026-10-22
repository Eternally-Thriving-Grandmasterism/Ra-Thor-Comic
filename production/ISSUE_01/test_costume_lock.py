#!/usr/bin/env python3
"""Must-fail / must-pass tests for check_costume_lock.py (text checks).

Run from anywhere:  python3 production/ISSUE_01/test_costume_lock.py
Plain python3, standard library only. Each case copies the repo's .md files
(plus the checker and the pauldron ref files) into a temp dir, injects one
change, and runs the checker's text checks there (main(type_check=False)).
The real repo files are never edited. Exit code 0 = every case as expected.
"""
import contextlib, importlib.util, io, os, shutil, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CHECKER = 'production/ISSUE_01/check_costume_lock.py'


def load(root):
    spec = importlib.util.spec_from_file_location('ccl_%d' % id(root), os.path.join(root, CHECKER))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def make_tree():
    tmp = tempfile.mkdtemp(prefix='ccl_')
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x != '.git']
        for f in files:
            if f.endswith('.md'):
                src = os.path.join(d, f)
                dst = os.path.join(tmp, os.path.relpath(src, ROOT))
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
    m = load(ROOT)
    extra = [CHECKER] + list(m.PAULDRON_REFS) + list(getattr(m, 'DUAL_REFS', []))
    for rel in extra:
        src = os.path.join(ROOT, rel)
        if os.path.isfile(src):
            os.makedirs(os.path.dirname(os.path.join(tmp, rel)), exist_ok=True)
            shutil.copy2(src, os.path.join(tmp, rel))
    return tmp


def run(root):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        bad = load(root).main(type_check=False)
    return bad, buf.getvalue()


def append(rel, text):
    def f(root):
        with open(os.path.join(root, rel), 'a', encoding='utf-8') as fh:
            fh.write('\n' + text + '\n')
    return f


def replace(rel, pairs, line=None):
    def f(root):
        p = os.path.join(root, rel)
        L = open(p, encoding='utf-8').read().split('\n')
        if line is None:
            s = '\n'.join(L)
            for o, n in pairs:
                assert o in s, o
                s = s.replace(o, n) if n is not None else s
            open(p, 'w', encoding='utf-8').write(s)
            return
        l = L[line - 1]
        for o, n in pairs:
            assert o in l, o
            l = l.replace(o, n)
        L[line - 1] = l
        open(p, 'w', encoding='utf-8').write('\n'.join(L))
    return f


V = '04_VISUAL_CANON.md'
P = 'production/ISSUE_01/ISSUE_01_PRODUCTION.md'
CASES = []
def case(name, expect, mutate):
    CASES.append((name, expect, mutate))

# --- earlier cases (CANON-SYNC-LOOK-LOCK-1 / -2 and AMEND-2) ---
case("Wild edge: 'the buckle not silver is rose gold'", 'FAIL', append(V, '- Buckle: the buckle not silver is rose gold.'))
case("SHIELD LOCK must-pass: 'no blue and a Vegvísir shield'", 'PASS', append(V, '- Shield: no blue and a Vegvísir shield.'))
# §13.3 (L832) is history since the SHIELD LOCK tagged it; Wild's repro now targets the current PRINT stem in 01.
case('Wild repro on the current PRINT stem in 01 (old halo eye + rose-gold buckle)', 'FAIL', replace('01_VISUAL_STYLE_GUIDE.md', [
    ('a thin gold ring halo with sharp gold spikes behind the head, no eye in the halo', 'a radiant Eye of Horus halo'),
    ('round gold sun-disc belt buckle with no bolt', 'rose-gold lightning-bolt buckle')]))
case("§13.4 'Prompt: rose-gold bolt buckle on a thick belt, not silver.'", 'FAIL', replace(P, [
    ('**8.1** Prompt:', 'Prompt: rose-gold bolt buckle on a thick belt, not silver.\n\n**8.1** Prompt:')]))
case('09: Vegvísir shield / rose-gold buckle / emerald halo', 'FAIL', append('09_CHARACTER_BIBLE.md',
    '- Shield: the Vegvísir elongated vertically on a tall shield.\n- Buckle: a rose-gold lightning bolt buckle.\n- Halo: emerald halo ring.'))
for line in ['- Proportions: compact helm wings no wider than the shoulders; never stretch art.',
             '- Hammer: polished antique gold hammer, no eye.',
             '- Cape: obsidian with a bronze-gold lining, no blue.',
             '- Halo: eight fine radial spokes, never letter-like.',
             '- Buckle: rose gold only for the bolt, no text.',
             '- Shield: never blue yet an Eye of Horus halo.',
             '- Buckle: round gold, a rose-gold bolt.',
             '- Shield: black with an emerald boss.']:
    case('04 must-fail: ' + line, 'FAIL', append(V, line))
for line in ['- Buckle: round gold, no rose-gold buckle.',
             '- Buckle: a round gold buckle with a gold bolt, no rose-gold buckle.',
             '- Bolt: the buckle bolt is not rose gold.',
             '- Shield: black, never emerald.',
             '- Halo: the halo has no Eye of Horus sigil.',
             '- Look: no eye in the halo, black kite shield, no rose gold.']:
    case('04 must-pass: ' + line, 'PASS', append(V, line))
case("drop 'black kite shield' from 01", 'FAIL', replace('01_VISUAL_STYLE_GUIDE.md', [('black kite shield', 'black shield')]))
case('STORE_LISTING stale line', 'FAIL', append('production/ISSUE_01/STORE_LISTING_AND_EXPORT.md', '- The cover shows the Vegvísir shield and a rose-gold bolt buckle.'))
case('newly scanned ART_PROMPTS stale prompt', 'FAIL', append('production/S2/S2E01/ART_PROMPTS.md', 'Prompt: [stem] + gold kite shield with the emerald eye-seal clearly visible.'))
case('newly scanned season file stale line', 'FAIL', append('seasons/S2_ARC_LOCK.md', '- Canon armor: the sun-spoke shield.'))
for line in ['- Shield: emerald eye-seal kite shield.',
             '- Shield: a gold kite shield with the emerald eye-seal.',
             '- Palette: emerald on the eye-seal, one accent.',
             '- Palette: Emerald only on the eye-seal.',
             '- Emblem: Canon emblem: the eye-seal in circuit inlay.',
             '- Shoulder: a small hawk seal on the shoulder.',
             '- Shoulder: a hawk-shaped pauldron seal lighting emerald.',
             '- Armour: Ra-Thor in gold circuit plate.',
             '- Armour: gold-and-black circuit-plate armor.',
             '- Armour: gold circuit plate (winged halo).',
             '- Helm: winged halo ring over the helm.',
             '- Helm: the winged-halo closed helm.',
             # AMEND-3: was must-pass in AMEND-2; the untagged-term guard now fails it.
             '- Page 5: the pass (the eye-seal rerun).']:
    case('AMEND-2 must-fail: ' + line, 'FAIL', append(V, line))
for line in ['- Lettering: keep the bubble clear of the eye-seal zone.',
             '- Guide layer: mark keep-clear zones: eye-seal, visor slit, lane stamps.',
             '- Set: a cartoon-scale gold circuit-plate workshop at night.',
             '- Set: Recycler Bay, a cartoon-scale lab grown out of gold circuit plate.',
             '- Set: Ra-Thor stands in the gold circuit-plate workshop.',
             '- Set: gold circuit walls, warm panel lights.',
             '- Halo: all-gold halo (no eye in the halo) with large gold wings behind the head.',
             '- Guard: no hawk seal, no eye-seal shield, never a winged halo.',
             '- Shield: the shield carries no eye-seal.']:
    case('AMEND-2 must-pass: ' + line, 'PASS', append(V, line))

# --- AMEND-3: untagged-term guard and widened scan ---
S = 'production/S1/S1E01/SCRIPT.md'
for rel, line in [(S, '- **Continuity:** Shield upright, eye-seal out.'),
                  (S, '- **Caption:** HAWK SEAL LIT.'),
                  ('production/S2/S2E04/MUSIC_CUES.md', '| P9 | The tick stops as the hawk seal lights. |'),
                  ('screen/S1E01/SHOT_LIST.md', '| S99 | 3.2 | Tight: the eye-seal clearly readable | Locked off | 3 | |'),
                  ('screen/SCREEN_BIBLE_ADDENDUM.md', '- The shield eye-seal reads first.'),
                  ('production/README.md', '| Notes | eye-seal on the shield | 00 |'),
                  ('bots/GROKBOT_COMIC_SEAT.md', '- Keep the gold plate, eye-seal, grounded hammer.'),
                  ('OWNERSHIP-NOTE-2026-10.md', 'Ra-Thor with the eye-seal shield.'),
                  ('docs/LIGHT_OCEAN_FORGED_BY_TOLC_SERIES_SEED.md', 'Ra-Thor, Vegvísir halo blazing.'),
                  ('production/ISSUE_01/LETTERING_SPEC.md', '- Bubble: tail away from the eye-seal.')]:
    case('AMEND-3 must-fail (%s): %s' % (rel, line), 'FAIL', append(rel, line))
for rel, line in [(S, '- **Continuity:** shield face out (no eye-seal on the shield).'),
                  (S, '- **Continuity:** eye-seal out. (superseded (in part) 2026-10-18 by the LOOK LOCK: shield face.)'),
                  ('production/ISSUE_01/LETTERING_SPEC.md', '4. Keep-clear zones on the guide layer: eye-seal, visor slit.'),
                  ('production/ISSUE_01/LETTERING_SPEC.md', '- Bubble: clear of the eye-seal and the confetti.'),
                  ('production/S2/S2E04/MUSIC_CUES.md', '| P9 | The tick stops as the pauldron Eyes light. |'),
                  ('OWNERSHIP-NOTE-2026-10.md', 'Ra-Thor with the Vegvísir kite shield as an optional prop.')]:
    case('AMEND-3 must-pass (%s): %s' % (rel, line), 'PASS', append(rel, line))

# --- BIBLE-DUAL-LOOK-LOCK-1 (2026-10-21): two locked looks ---
B = 'production/ISSUE_01/bible/CHARACTER_BIBLE.md'
PRINT_LINE = 'Ra-Thor, inked comic art with bold outlines and flat colour on parchment: black dome helm with gold Spartan-style face plates forming a T-visor and a gold centre ridge, two small gold feathered wings behind the head, a thin gold ring halo with sharp gold spikes behind the head, no eye in the halo, black armour with simple gold line trim and no Greek-key, large round black pauldrons with gold rims, each with an emerald-green Eye of Horus outlined in gold, mirrored, round gold sun-disc belt buckle with no bolt, black knee plates with gold trim, long tattered black cape, dark stone block-head hammer with a gold band near each end and one gold lightning bolt on the broad side face, head-down on rock, both hands resting on the pommel; no shield unless the scene calls for it (then the SHIELD RE-LOCK prop: a heraldic kite shield with a straight notched top and flared upper corners, a thick riveted gold rim, bold raised gold Norse interlace around the gold Vegvísir and domed gold boss, all in armour gold, plain borders); emerald only on the pauldron Eyes; no rose gold, no teal, no blue.'
ANIM_LINE = 'Ra-Thor, painted realistic render ready for 3D, storm sky: glossy black armour with gold trim and gold Greek-key engraving, black dome helm with gold Spartan-style face plates forming a T-visor and a gold centre ridge, two large gold feathered wings rising behind the head, an all-gold halo: a gold Greek-key disc with long straight gold sun rays, no eye in the halo, a glowing gold sun disc in a gold Greek-key ring on the chest, round gold belt buckle with a gold lightning bolt, black knee plates with gold trim, large round black pauldrons with stepped gold rims, each with an emerald-green Eye of Horus outlined in gold, mirrored, long intact black cape with a gold Greek-key border, dark stone block-head hammer with one gold lightning bolt on each visible face, head-down on rock, both hands stacked on the pommel; no shield unless the scene calls for it (then the SHIELD RE-LOCK prop: a heraldic kite shield with a straight notched top and flared upper corners, a thick riveted gold rim, bold raised gold Norse interlace around the gold Vegvísir and domed gold boss, all in armour gold, plain borders); emerald only on the pauldron Eyes; no rose gold, no teal, no blue.'
# Was must-fail under the 2026-10-18 lock; both dual looks rest both hands on the pommel.
case('DUAL must-pass: - Rest: both hands stacked on the pommel, never swung.', 'PASS', append(V, '- Rest: both hands stacked on the pommel, never swung.'))
case('DUAL must-pass: PRINT prompt line in 04', 'PASS', append(V, '- Prompt: ' + PRINT_LINE))
case('DUAL must-pass: ANIMATED prompt line in a screen file', 'PASS', append('screen/S1E01/SHOT_LIST.md', 'Prompt: ' + ANIM_LINE))
case('DUAL must-pass: print buckle with no bolt', 'PASS', append(V, '- Buckle (print): a round gold sun-disc buckle with no bolt.'))
case('DUAL must-pass: no shield in the base silhouette', 'PASS', append(V, '- Shield: none in the base silhouette; optional prop only.'))
case('DUAL must-pass: tattered print cape / intact animated cape', 'PASS', append(V, '- Cape: tattered in print; intact with a gold Greek-key border in animation.'))
case('SHIELD LOCK must-pass: Vegvísir shield prop', 'PASS', append(V, '- Shield (prop): the Vegvísir shield.'))
case('DUAL must-fail: eye in the halo still fails', 'FAIL', append(V, '- Halo (animated): an Eye of Horus halo.'))
case('DUAL must-fail: rose-gold buckle still fails', 'FAIL', append(V, '- Buckle (print): a rose-gold buckle.'))
case('DUAL must-fail: DUAL section removed from the Bible', 'FAIL', replace(B, [('## DUAL LOOK LOCK 2026-10-21', '## Removed 2026-10-21')]))
case('DUAL must-fail: PRINT prompt stem removed from 01', 'FAIL', replace('01_VISUAL_STYLE_GUIDE.md', [('**Prompt stem, PRINT look', '**Prompt stem, removed')]))
case('DUAL must-fail: shield ruling removed from the Bible', 'FAIL', replace(B, [('OPTIONAL prop', 'prop')]))
case('DUAL must-fail: buckle flag removed from the Bible', 'FAIL', replace(B, [('**Buckle bolt.**', '**Buckle.**')]))

# --- SHIELD LOCK (Sherif 2026-10-21 2:35 PM ET) ---
for line in ['- Shield: the elongated Vegvísir shield, with no blue.',
             '- Halo: no eye in the halo; a tall shield bearing the elongated Vegvísir.',
             '- Shield: not silver or navy but a Vegvísir shield.',
             '- Shield prop: the gold Vegvísir on the black kite shield, hammer grounded.',
             '- Shield: the Vegvísir on the shield and a hammer at his side.',
             '- Guard: no sun-spokes, no emerald, no eye on the shield.',
             '- Shield: black field, never emerald.',
             '- Prompt: ' + "Shield prop, inked comic art, bold clean outlines, flat colour on parchment: a heraldic kite shield about 165 cm tall and 78 cm wide (about 2.1 times taller than wide): a straight top edge with a shallow central notch, flared upper corners that sweep slightly outward like shoulders, widest at about one-fifth of the height, nearly straight parallel sides down to about halfway, then convex curves to one sharp point; not a pointed oval, not round-topped; gently curved across the width; a gloss-black field framed by a thick riveted rim; on the face, the Vegvísir in raised gold: eight bold staves at even 45-degree spacing, each with its own end-mark, around a domed polished gold boss in a riveted collar; a ring of thick braided Norse knotwork around the Vegvísir, not chain links; mirrored panels of thick broad-ribbon Norse interlace above and below with clear over-under weave, joined as one unbroken thread; generous black negative space; no thin filigree, no scribbles, no runes or letters anywhere; all gold is the identical bright warm polished gold of Ra-Thor's armour trim, helm wings and halo, with no bronze or brass tone; no eye, no emerald, no sun-spokes, no runes, no blue.",
             '- Prompt: ' + "Shield prop, painted realistic render ready for 3D, warm key light, storm-lit rim light: a heraldic kite shield about 165 cm tall and 78 cm wide (about 2.1 times taller than wide): a straight top edge with a shallow central notch, flared upper corners that sweep slightly outward like shoulders, widest at about one-fifth of the height, nearly straight parallel sides down to about halfway, then convex curves to one sharp point; not a pointed oval, not round-topped; gently curved across the width; a gloss-black field framed by a thick riveted rim; on the face, the Vegvísir in raised gold: eight bold staves at even 45-degree spacing, each with its own end-mark, around a domed polished gold boss in a riveted collar; a ring of thick braided Norse knotwork around the Vegvísir, not chain links; mirrored panels of thick broad-ribbon Norse interlace above and below with clear over-under weave, joined as one unbroken thread; generous black negative space; no thin filigree, no scribbles, no runes or letters anywhere, the interlace raised in relief; all gold is the identical bright warm polished gold of Ra-Thor's armour trim, helm wings and halo, with no bronze or brass tone; no eye, no emerald, no sun-spokes, no runes, no blue.",
             '- Prompt: ' + "Shield prop, front-view orthographic reference for 3D modelling, flat even light, no perspective, centred on neutral grey, with a scale bar: a heraldic kite shield 165 cm tall by 78 cm wide, straight top edge with a shallow central notch, flared upper corners, widest at 20 percent of the height, nearly straight parallel sides to 50 percent, convex curves to one sharp point, not a pointed oval, not round-topped; a gloss-black field framed by a thick riveted rim; on the face, the Vegvísir in raised gold: eight bold staves at even 45-degree spacing, each with its own end-mark, around a domed polished gold boss in a riveted collar; a ring of thick braided Norse knotwork around the Vegvísir, not chain links; mirrored panels of thick broad-ribbon Norse interlace above and below with clear over-under weave, joined as one unbroken thread; generous black negative space; no thin filigree, no scribbles, no runes or letters anywhere; all gold is the identical bright warm polished gold of Ra-Thor's armour trim, helm wings and halo, with no bronze or brass tone; no eye, no emerald, no sun-spokes, no runes, no blue.",
             '- Prompt: ' + 'Ra-Thor, 7 ft 0 in armoured hero standing on dark rock, full figure, slight low angle, commanding legendary presence: the hammer is planted head-down on the rock at his right side, its long rectangular black stone block head with bevelled edges and one gold lightning bolt on each broad face, no spikes; a long wrist-thick dark iron and leather haft with three gold bands (at the head, at the middle, and just below the grip), reaching from the rock to between his waist and lower chest; the pommel is a flat, wide, softly domed polished gold cap, and his right gauntlet rests flat on it; his left arm holds the shield at his side, standing point-down on the rock, its face toward the viewer; the shield is the SHIELD RE-LOCK design (heraldic kite, straight notched top, flared corners, bold raised gold Norse interlace around the gold Vegvísir, no runes, armour gold); [PRINT or ANIMATED look stem from `01_VISUAL_STYLE_GUIDE.md`]; emerald only on the pauldron Eyes; no rose gold, no teal, no blue. Avoid: a round knob or ball pommel, a pommel on a flared dish, a spiked pommel, a short haft, spikes on the hammer head, a shield held off the ground.']:
    case('SHIELD LOCK must-pass: ' + line[:90], 'PASS', append(V, line))
for line in ['- Halo: a Vegvísir in the halo.',
             '- Chest: a gold Vegvísir on the chest.',
             '- Helm: the Vegvísir engraved on the helm.',
             '- Shield: an emerald kite shield.',
             '- Shield: a black kite shield edged in emerald.',
             '- Shield: black kite shield with the gold sun-spoke design.',
             '- Shield: the eye-seal shield.']:
    case('SHIELD LOCK must-fail: ' + line, 'FAIL', append(V, line))
case('SHIELD LOCK must-fail: SHIELD LOCK section removed', 'FAIL', replace(B, [('## SHIELD LOCK 2026-10-21', '## Removed')]))
case('SHIELD LOCK must-fail: shield prompts removed from 01', 'FAIL', replace('01_VISUAL_STYLE_GUIDE.md', [('Shield prompts (SHIELD RE-LOCK', 'Removed')]))
case('SHIELD LOCK must-fail: shield ref missing', 'FAIL', lambda root: os.remove(os.path.join(root, 'production/ISSUE_01/bible/refs/rathor_shield_lock_2026-10-21.jpg')))

# --- SHIELD RE-LOCK (Sherif 2026-10-21 8:20-8:44 PM ET): MERCY runes removed; heraldic kite 165 x 78 cm; armour gold ---
case('RE-LOCK must-fail: a MERCY rune band on the shield', 'FAIL', append(V, '- Shield: the left border spells MERCY in runes ᛗᛖᚱᚲᛁ.'))
case('RE-LOCK must-fail: a rune border on the shield', 'FAIL', append(V, '- Shield: a rune border down the left side.'))
case('RE-LOCK must-fail: a border of rune-like marks', 'FAIL', append(V, '- Shield: a narrow border column of rune-like marks.'))
case('RE-LOCK must-pass: no runes anywhere', 'PASS', append(V, '- Shield: plain left border, no runes anywhere on the shield.'))
case('RE-LOCK must-fail: bronze-gold rim', 'FAIL', append(V, '- Shield: a riveted bronze-gold rim.'))
case('RE-LOCK must-fail: brass interlace', 'FAIL', append(V, '- Shield: brass interlace on the face.'))
case('RE-LOCK must-pass: armour gold, no bronze or brass', 'PASS', append(V, '- Shield: armour gold throughout, no bronze or brass tone.'))
case('RE-LOCK must-fail: Bible loses the 165 cm height', 'FAIL', replace(B, [('| 165 cm | 5 ft 5 in | 6.6 heads |', '| tall |')]))
case('RE-LOCK must-fail: Bible loses the 78 cm width', 'FAIL', replace(B, [('| 78 cm | 2 ft 7 in | 3.1 heads |', '| wide |')]))
case('RE-LOCK must-fail: Bible loses not-oval / not-round-topped', 'FAIL', replace(B, [('Not a pointed oval, and not round-topped.', 'An oval.')]))
case('RE-LOCK must-fail: 01 loses not-oval / not-round-topped', 'FAIL', replace('01_VISUAL_STYLE_GUIDE.md', [('not a pointed oval and not round-topped', 'an oval')]))
case('RE-LOCK must-fail: Bible loses NOT chain links', 'FAIL', replace(B, [('NOT chain links', 'chain links')]))
case('RE-LOCK must-fail: Bible loses the Blender re-lock line', 'FAIL', replace(B, [('**3D / Blender scale line (re-lock).**', '**3D.**')]))
case('RE-LOCK must-fail: Bible loses the prompts-only art rule', 'FAIL', replace(B, [('Bots write prompts only and never hand-paint', 'Bots may paint')]))
case('REF must-fail: Bible loses the 9:02 PM ET reference images', 'FAIL', replace(B, [('**Reference images (locked, Sherif 2026-10-21 9:02 PM ET).**', '**Reference image: TODO.**')]))
case('REF must-fail: Bible loses the hidden-pommel gap', 'FAIL', replace(B, [('The pommel cap is hidden under his hand', 'The pommel is shown')]))
case('REF must-fail: hero ref file missing', 'FAIL', lambda root: os.remove(os.path.join(root, 'production/ISSUE_01/bible/refs/rathor_hero_shield_lock_2026-10-21.jpg')))
case('RE-LOCK must-fail: vows no longer marked proposed', 'FAIL', replace(B, [('stay **proposed**', 'are canon')]))
case('RE-LOCK must-fail: Bible hero prompt loses the Avoid line', 'FAIL', replace(B, [('Avoid: a round knob or ball pommel', 'Avoid: nothing')]))
case('RE-LOCK must-fail: 01 loses the hero prompt', 'FAIL', replace('01_VISUAL_STYLE_GUIDE.md', [('> **Hero (with shield):**', '> **Hero:**')]))
# --- Hands AMEND on #113: stale sun-spoke / Vegvísir-reject lines ---
case('SHIELD-HIST must-fail: sun-spoke shield stated as current (with a reject clause)', 'FAIL', append(V, "- 4.1: the shield's gold sun-spoke design must read. A knotwork border is a reject."))
case('SHIELD-HIST must-fail: Vegvísir on the shield is a reject', 'FAIL', append(V, '- A Vegvísir on the shield is a reject.'))
case('SHIELD-HIST must-fail: no Vegvísir anywhere', 'FAIL', append('14_ANIMATED_SERIES_BIBLE.md', '- No Vegvísir anywhere on the figure.'))
case('SHIELD-HIST must-fail: Vegvísir in a Rejects section', 'FAIL', append(P, '### 13.9 Rejects (test)\n- A Vegvísir or knotwork border on the shield.'))
case('SHIELD-HIST must-pass: no Vegvísir on the halo', 'PASS', append(V, '- Halo: no Vegvísir on the halo; a Vegvísir in the halo is a reject.'))
case('SHIELD-HIST must-pass: tagged sun-spoke line', 'PASS', append(V, '- Shield: the gold sun-spoke design. (superseded 2026-10-21 by the SHIELD LOCK.)'))
case('SHIELD-HIST must-pass: Rejects section, Vegvísir on the chest', 'PASS', append(P, '### 13.9 Rejects (test)\n- A Vegvísir on the chest.'))
case('VOW must-fail: vow 8 gate wording', 'FAIL', replace(B, [('Keep the watch; the vigil', 'Keep the gate; the vigil')]))
# Were 10-18 must-pass guards; under the SHIELD LOCK they reject the locked shield, so they now fail.
case('SHIELD-HIST must-fail (was must-pass): no Vegvísir ... on the shield guard', 'FAIL', append(V, '- Guard: no Vegvísir, no knotwork border and no Eye of Horus on the shield; no rose-gold bolt; never a bronze-gold lining.'))
case('SHIELD-HIST must-fail (was must-pass): never a Vegvísir shield', 'FAIL', append(V, '- Shield: never a Vegvísir shield.'))

def main():
    base = make_tree()
    try:
        bad, out = run(base)
        if bad:
            print(out)
            print('baseline tree fails the checker; fix that first')
            return 1
        print('[ok] baseline: check_costume_lock text checks pass')
        wrong = 0
        for name, expect, mutate in CASES:
            tmp = tempfile.mkdtemp(prefix='ccl_case_')
            try:
                shutil.rmtree(tmp)
                shutil.copytree(base, tmp)
                mutate(tmp)
                bad, out = run(tmp)
                got = 'FAIL' if bad else 'PASS'
                ok = got == expect
                wrong += not ok
                print('[%s] %s -> %s' % ('as expected' if ok else 'UNEXPECTED', name, got))
                if not ok:
                    print('     ' + out.strip().replace('\n', '\n     ')[:600])
            finally:
                shutil.rmtree(tmp, ignore_errors=True)
        print('%d/%d cases as expected' % (len(CASES) - wrong, len(CASES)))
        return 1 if wrong else 0
    finally:
        shutil.rmtree(base, ignore_errors=True)


if __name__ == '__main__':
    sys.exit(main())
