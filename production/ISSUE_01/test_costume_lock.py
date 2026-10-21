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
    extra = [CHECKER] + list(load(ROOT).PAULDRON_REFS)
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
case("'no blue and a Vegvísir shield'", 'FAIL', append(V, '- Shield: no blue and a Vegvísir shield.'))
case('§13.3 cover prompt swap (L832)', 'FAIL', replace(P, [
    ('black kite shield with a riveted gold rim and a gold sun-spoke design around a central gold boss', 'tall shield bearing the elongated Vegvísir'),
    ('round gold belt buckle with a gold lightning bolt', 'rose-gold lightning-bolt buckle'),
    ('an all-gold halo centred behind the head: a gold Greek-key disc, two thin gold rings and seven straight gold sun rays, no eye in the halo', 'a radiant Eye of Horus halo')], line=832))
case("§13.4 'Prompt: rose-gold bolt buckle on a thick belt, not silver.'", 'FAIL', replace(P, [
    ('**8.1** Prompt:', 'Prompt: rose-gold bolt buckle on a thick belt, not silver.\n\n**8.1** Prompt:')]))
case('09: Vegvísir shield / rose-gold buckle / emerald halo', 'FAIL', append('09_CHARACTER_BIBLE.md',
    '- Shield: the Vegvísir elongated vertically on a tall shield.\n- Buckle: a rose-gold lightning bolt buckle.\n- Halo: emerald halo ring.'))
for line in ['- Shield: the elongated Vegvísir shield, with no blue.',
             '- Halo: no eye in the halo; a tall shield bearing the elongated Vegvísir.',
             '- Proportions: compact helm wings no wider than the shoulders; never stretch art.',
             '- Hammer: polished antique gold hammer, no eye.',
             '- Rest: both hands stacked on the pommel, never swung.',
             '- Cape: obsidian with a bronze-gold lining, no blue.',
             '- Halo: eight fine radial spokes, never letter-like.',
             '- Buckle: rose gold only for the bolt, no text.',
             '- Shield: not silver or navy but a Vegvísir shield.',
             '- Shield: never blue yet an Eye of Horus halo.',
             '- Buckle: round gold, a rose-gold bolt.',
             '- Shield: black with an emerald boss.']:
    case('04 must-fail: ' + line, 'FAIL', append(V, line))
for line in ['- Guard: no Vegvísir, no knotwork border and no Eye of Horus on the shield; no rose-gold bolt; never a bronze-gold lining.',
             '- Buckle: round gold, no rose-gold buckle.',
             '- Buckle: a round gold buckle with a gold bolt, no rose-gold buckle.',
             '- Bolt: the buckle bolt is not rose gold.',
             '- Shield: black, never emerald.',
             '- Halo: the halo has no Eye of Horus sigil.',
             '- Shield: never a Vegvísir shield.',
             '- Look: no eye in the halo, black kite shield, no rose gold.']:
    case('04 must-pass: ' + line, 'PASS', append(V, line))
case("drop 'black kite shield' from 01", 'FAIL', replace('01_VISUAL_STYLE_GUIDE.md', [('black kite shield', 'black shield')]))
case('STORE_LISTING stale line', 'FAIL', append('production/ISSUE_01/STORE_LISTING_AND_EXPORT.md', '- The cover shows the Vegvísir shield and a rose-gold bolt buckle.'))
case('newly scanned ART_PROMPTS stale prompt', 'FAIL', append('production/S2/S2E01/ART_PROMPTS.md', 'Prompt: [stem] + gold kite shield with the emerald eye-seal clearly visible.'))
case('newly scanned season file stale line', 'FAIL', append('seasons/S2_ARC_LOCK.md', '- Canon armor: Vegvísir shield.'))
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
                  ('docs/LIGHT_OCEAN_FORGED_BY_TOLC_SERIES_SEED.md', 'Ra-Thor, Vegvísir shield raised.'),
                  ('production/ISSUE_01/LETTERING_SPEC.md', '- Bubble: tail away from the eye-seal.')]:
    case('AMEND-3 must-fail (%s): %s' % (rel, line), 'FAIL', append(rel, line))
for rel, line in [(S, '- **Continuity:** shield face out (no eye-seal on the shield).'),
                  (S, '- **Continuity:** eye-seal out. (superseded (in part) 2026-10-18 by the LOOK LOCK: shield face.)'),
                  ('production/ISSUE_01/LETTERING_SPEC.md', '4. Keep-clear zones on the guide layer: eye-seal, visor slit.'),
                  ('production/ISSUE_01/LETTERING_SPEC.md', '- Bubble: clear of the eye-seal and the confetti.'),
                  ('production/S2/S2E04/MUSIC_CUES.md', '| P9 | The tick stops as the pauldron Eyes light. |'),
                  ('OWNERSHIP-NOTE-2026-10.md', 'Ra-Thor with the black kite shield and gold sun-spoke design.')]:
    case('AMEND-3 must-pass (%s): %s' % (rel, line), 'PASS', append(rel, line))


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
