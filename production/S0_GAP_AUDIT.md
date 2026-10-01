# S0 gap audit (Card 19)

**Scope: notes only; fills nothing; no canon changes.** This file lists gaps and banked file-vs-sheet items. It fills no gap, proposes no replacement text, and edits no other file. Every entry cites its source file and line(s) on `main` at `a984ec915b1f74bb96bf167a9dfccffd8dae0e39`. Quoted text is copied exactly from the cited line.

**Location.** No audit location or file name is defined in `production/README.md`, `bots/ROUTINE.md`, `11_MASTER_INDEX.md` or the season locks. `production/README.md` L77 lists the card only as a gap audit whose gaps are "listed, never filled in." This file therefore uses `production/S0_GAP_AUDIT.md`.

## C. Header: merged PRs audited

| PR | Card | Commit on main |
|---|---|---|
| #40 | docs: production prep (script format) + banked doc fixes | `24f9c2c` |
| #41 | S1E01 production set | `7dc58fb` |
| #42 | S1E02 production set | `bee1c23` |
| #43 | S1E03 production set | `d2e695f` |
| #44 | S1E04 production set | `54ea43c` |
| #45 | GUEST-SET-FIX (S1E01–S1E04 SCRIPT Guest lines) | `c7dfc14` |
| #46 | Card 5, S1E05 production set | `ca40326` |
| #47 | QUOTE-CASE-FIX | `647a24f` |
| #48 | Card 6, S1E06 production set | `7786fe2` |
| #49 | Card 7, S2E01 production set | `56eddb5` |
| #50 | Card 8, S2E02 production set | `4729702` |
| #51 | Card 9, S2E03 production set | `23b3743` |
| #52 | Card 10, S2E04 production set | `3c56e05` |
| #53 | Card 11, S2E05 production set | `85017ae` |
| #54 | Card 12, S2E06 production set | `df14ccc` |
| #55 | Card 13, S3E01 production set | `9698f6c` |
| #56 | Card 14, S3E02 production set | `952ad24` |
| #57 | Card 15, S3E03 production set | `4627045` |
| #58 | Card 16, S3E04 production set | `735fbc8` |
| #59 | Card 17, S3E05 production set | `31b2e52` |
| #60 | Card 18, S3E06 production set | `a984ec9` |

Sections: A (banked items), B (GAPs across the 18 production sets), D (Season 0 episode files, which have no production sets).

## A. Banked items (noted only)

Each item was checked against current `main`. Holds means the cited lines read as described.

### A1. S2 sheet §8 item 1: stale status (resolved; sheet not edited)

- Item: `seasons/S2_SEASON_SHEET.md` L114 is headed "NOT FIXED (stale status). The arc lock still says" and says all six episodes are now merged.
- Now on main: `seasons/S2_ARC_LOCK.md` L99 reads "the six episodes were merged in separate PRs (#23–#28, §10)." `11_MASTER_INDEX.md` L41 reads "complete (S2E01–S2E06 merged)".
- S2 episode files on main: `episodes/S2E01_THE_LONE_LAMP.md` L1, `episodes/S2E02_THE_WHOLE_MAP.md` L1, `episodes/S2E03_THE_SIMPLE_SIMULATOR.md` L1, `episodes/S2E04_THE_AWAKENING_PAGE.md` L1, `episodes/S2E05_THE_BENCH_LAMP.md` L1, `episodes/S2E06_THE_FIRST_BLOCK.md` L1.
- Status: holds; the item is resolved (fixed in #30). Not papered over: the item quotes three phrases. Two of them, the lock's outline phrase and the index's outline phrase, no longer occur anywhere on main. The third, the checklist phrase, still begins `seasons/S2_ARC_LOCK.md` L99, but that line now goes on to say the episodes were merged. Only the S2 sheet item itself is stale; the sheet is not edited here.

### A2. S2 sheet §8 item 4: S2E03 flashback stem (resolved since #30)

- Item: `seasons/S2_SEASON_SHEET.md` L117 is headed "NO FIX (minor). S2E03's flashback stem."
- Now on main: `episodes/S2E03_THE_SIMPLE_SIMULATOR.md` L21 ends "no readable text except the era card, which reads the year only, with no caption." The same wording is in `production/S2/S2E03/ART_PROMPTS.md` L17.
- Status: holds; resolved since #30. The #51 PR body also noted the item as stale. Context, not a finding: the stem phrase that item 4 quotes still occurs in the S2E01 and S2E02 flashback stems (`episodes/S2E01_THE_LONE_LAMP.md` L19, `episodes/S2E02_THE_WHOLE_MAP.md` L21). Item 4 is about S2E03 only.

### A3. S2 MUSIC_CUES sine-pad notes (moot; tidy-able)

- Notes: `production/S2/S2E01/MUSIC_CUES.md` L39, `production/S2/S2E02/MUSIC_CUES.md` L38, `production/S2/S2E03/MUSIC_CUES.md` L39, `production/S2/S2E04/MUSIC_CUES.md` L38. The same note also appears in `production/S2/S2E05/MUSIC_CUES.md` L39 and `production/S2/S2E06/MUSIC_CUES.md` L38, beyond E01–E04.
- Each note says 06's Quiet Board row has "one sustained pad" and the file has "one sustained sine pad" (e.g. `production/S2/S2E01/MUSIC_CUES.md` L39).
- 06: `06_MUSIC_SPEC.md` L35 (§2, Quiet Board row). Its cue text has "one sustained pad", and its instrumentation column lists "Muted pluck, sine pad, sub kick".
- Status: holds. The row already names a sine pad, so the six notes are moot and tidy-able. No file is changed here.

### A4. S1E06 Set vs P1: where the markers rest (future canon card)

- Set: `episodes/S1E06_THE_KEPT_CHAIR.md` L7 reads "The knot, step, pen, hinge and fan markers rest on their chairs."
- P1: `episodes/S1E06_THE_KEPT_CHAIR.md` L19 reads "Each marker now rests on the table in front of its house."
- Status: holds as a textual difference between the Set line and P1. Not papered over: `seasons/S1_SEASON_SHEET.md` L46 (§3) describes a move, where each marker "moves to the table in front of its house (P1)", and P1 says "now" (`episodes/S1E06_THE_KEPT_CHAIR.md` L19). The difference is noted for a future canon card; no ruling is made here.

### A5. S3E04 P6 caption vs S3 sheet §5 item 9

- Caption: `episodes/S3E04_THE_LOCKED_CRATES.md` L64 reads "Caption: CRATES UNTOUCHED. ONE INVITATION. HAMMER STILL GROUNDED."
- Ruling: `seasons/S3_SEASON_SHEET.md` L85 (§5 item 9) reads "The S3E04 invitation is left open on the page and not recapped by a caption (council ruling, PR #35)."
- Status: holds textually (flagged in #58). Not papered over: the same sheet's closing-captions list carries this caption for E04 (`seasons/S3_SEASON_SHEET.md` L44, "CRATES UNTOUCHED. ONE INVITATION. HAMMER STILL GROUNDED. (E04)"). The S3E05 Reject bars "A caption recapping the S3E04 invitation" (`episodes/S3E05_THE_BETTER_DEAL.md` L91). Whether item 9 covers S3E04's own caption is left for the council.

### A6. S3E04 P2 light source vs 10's Quiet Room lighting

- P2: `episodes/S3E04_THE_LOCKED_CRATES.md` L35 reads "over Ra-Thor's shoulder toward the feed wall, which is the main light source".
- 10: `10_LOCATION_BIBLE.md` L13 (The Quiet Room) reads "Suave Hour lighting: one practical, deep shadow, armor still fully on."
- Status: holds (flagged in #58). Context: the same 10 line also reads "Episode 04 and 06." (`10_LOCATION_BIBLE.md` L13).

### A7. Other banked items from the production files and PR bodies #41–#60 (noted only)

1. **AGIRBE vs AGiRBE (#60).** The S3 sheet §7 crawl text has "Realistic abundance is likely AGIRBE" (`seasons/S3_SEASON_SHEET.md` L123), copied in `production/S3/S3E06/SCRIPT.md` L100. The placement line and rule use the lowercase-i form: `episodes/S3E06_THE_FULL_HOPPER.md` L9 has "the AGiRBE credit line (verbatim", and `production/README.md` L14 (rule 6) has "The AGiRBE line and the Fresco credit". Existing ruling: `seasons/S3_ARC_LOCK.md` L34 records "Sherif's answer spells it" with the capital I, and closes "Both are quoted as written." (the section is a council ruling, `seasons/S3_ARC_LOCK.md` L30). The same capital-I form is in `05_LORE_BIBLE.md` L208 (Q11) and `seasons/S3_ARC_LOCK.md` L27.
2. **Crawl date vs the S3E06 Reject (#60).** `episodes/S3E06_THE_FULL_HOPPER.md` L9 carries the crawl attribution with "2026-10-01 12:14 AM ET"; the S3E06 Reject has "Any era card, year or date." (`episodes/S3E06_THE_FULL_HOPPER.md` L88). The Reject governs the page; the crawl is off-page (README rule 6, `production/README.md` L14).
3. **Painted board (#60).** The S3 sheet §2 row has "put in by the Watcher and the crate-keepers by choice" (`seasons/S3_SEASON_SHEET.md` L40). The S3E06 P6 staging has "the painted board is already going in beside them" (`episodes/S3E06_THE_FULL_HOPPER.md` L69) and credits no one. The same point is GAP `production/S3/S3E06/SCRIPT.md` L110 (B1).
4. **E6 in the S3E06 summary (#60).** The episode lists E6 among the 543-pad chords (`episodes/S3E06_THE_FULL_HOPPER.md` L76). `production/S3/S3E06/MUSIC_CUES.md` L21 reads "E6 is listed in the summary but no per-panel cue names it".
5. **S3E05 Grounded on two bass lines (#59).** 06 §1 has "One lead synth timbre belongs to Ra-Thor" (`06_MUSIC_SPEC.md` L22). The file flags the unison bass lines (`production/S3/S3E05/MUSIC_CUES.md` L38), and the S3 sheet records them as "two bass lines, the commons' and the Tollkeeper's, joined in unison on Grounded on E" (`seasons/S3_SEASON_SHEET.md` L70).
6. **S3E02 Grounded passed across the voices (#56).** The episode has "the Grounded motif on the blip lead, passed across the voices" (`episodes/S3E02_ONE_TOOL_MANY_HANDS.md` L76), against 06 §1 L22 as in item 5. The production file has the same text (`production/S3/S3E02/MUSIC_CUES.md` L32), with no flag in its Notes.
7. **S3E03 P4 drone vs its summary (#57).** The summary puts the drone under "the Panel 4 resolution" (`episodes/S3E03_LET_IT_COOL.md` L70). The P4 cue puts the held beat "over the E2 drone" before the stinger (`episodes/S3E03_LET_IT_COOL.md` L74).
8. **S3E03 held bar of silence (#57).** The P5 cue has "one held bar of silence for LET IT COOL" (`episodes/S3E03_LET_IT_COOL.md` L75). 06 does not anticipate it (per the #57 PR body).
9. **No Snap stinger in S3E04 (#58).** The S3 lock has "S3E04 has no Snap panel and no Snap stinger." (`seasons/S3_ARC_LOCK.md` L133), and its §11 item 3 has "no Snap stinger in S3E04 (§7, §9)" (`seasons/S3_ARC_LOCK.md` L158). The S3 sheet clarifies that this "means only that there is no Snap button panel" (`seasons/S3_SEASON_SHEET.md` L77, clarification at the #31 merge).
10. **Crawl placement (#55, #56).** Ruled in Card 14: the S3E02–S3E05 files read "Council ruling, Card 14." (e.g. `production/S3/S3E02/SCRIPT.md` L86). The S3E01 files, merged before that ruling, still carry the older wording "Crawl: GAP: not placed in S3E01." (`production/S3/S3E01/SCRIPT.md` L83, `production/S3/S3E01/ART_PROMPTS.md` L70, `production/S3/S3E01/MUSIC_CUES.md` L45). The two wordings differ; this is noted as tidy-able only.
11. **05 Snap button panel vs S2 files (#49–#54).** 05 C has "one Snap panel per episode for the button" (`05_LORE_BIBLE.md` L182). Each S2 MUSIC_CUES notes the file's "no Snap cue, the stinger only" per S2 sheet §5 item 1: `production/S2/S2E01/MUSIC_CUES.md` L40, `production/S2/S2E02/MUSIC_CUES.md` L39, `production/S2/S2E03/MUSIC_CUES.md` L41, `production/S2/S2E04/MUSIC_CUES.md` L39, `production/S2/S2E05/MUSIC_CUES.md` L40, `production/S2/S2E06/MUSIC_CUES.md` L41.
12. **No S1 lock file (#48).** `seasons/` on main holds `S1_SEASON_SHEET.md`, `S2_ARC_LOCK.md`, `S2_SEASON_SHEET.md`, `S3_ARC_LOCK.md` and `S3_SEASON_SHEET.md`; there is no S1 arc lock.
13. **File-vs-06 Notes in MUSIC_CUES (#44–#60).** Each heading below is "Notes (file differs from 06; the file wins)" (e.g. `production/S1/S1E04/MUSIC_CUES.md` L34). The bullets are not restated here. S1E01–S1E03 have no such heading.

| File:line | Bullets |
|---|---|
| `production/S1/S1E04/MUSIC_CUES.md` L34 | 2 |
| `production/S1/S1E05/MUSIC_CUES.md` L34 | 1 |
| `production/S1/S1E06/MUSIC_CUES.md` L34 | 2 |
| `production/S2/S2E01/MUSIC_CUES.md` L34 | 5 |
| `production/S2/S2E02/MUSIC_CUES.md` L34 | 4 |
| `production/S2/S2E03/MUSIC_CUES.md` L34 | 6 |
| `production/S2/S2E04/MUSIC_CUES.md` L34 | 4 |
| `production/S2/S2E05/MUSIC_CUES.md` L34 | 5 |
| `production/S2/S2E06/MUSIC_CUES.md` L34 | 6 |
| `production/S3/S3E01/MUSIC_CUES.md` L34 | 2 |
| `production/S3/S3E02/MUSIC_CUES.md` L34 | 2 |
| `production/S3/S3E03/MUSIC_CUES.md` L34 | 2 |
| `production/S3/S3E04/MUSIC_CUES.md` L36 | 2 |
| `production/S3/S3E05/MUSIC_CUES.md` L34 | 3 |
| `production/S3/S3E06/MUSIC_CUES.md` L38 | 4 |

## B. GAPs across the 18 production sets (S1E01–S3E06)

Found by scanning every `production/**/{SCRIPT,ART_PROMPTS,MUSIC_CUES}.md` on main (54 files) for GAP entries. Not from memory.

### B1. GAPs by episode

Each row is one numbered item under a file's Open gaps heading, or (S3E02–E05) the line under its Crawl heading. The None-for-prompts items are not counted as GAPs, except the S3E06 item's Fidelity-note sentence. No S0 production sets exist under `production/` on main (`production/` holds only `README.md` and the S1, S2 and S3 folders), so S0 has no rows here; see Section D.


#### S1E01 (10)

| File:line | Type |
|---|---|
| `production/S1/S1E01/SCRIPT.md` L77 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E01/SCRIPT.md` L78 | Speaker |
| `production/S1/S1E01/SCRIPT.md` L79 | SFX |
| `production/S1/S1E01/SCRIPT.md` L80 | Glassy bell not placed on a panel |
| `production/S1/S1E01/ART_PROMPTS.md` L64 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E01/MUSIC_CUES.md` L40 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E01/MUSIC_CUES.md` L41 | Lead instrument |
| `production/S1/S1E01/MUSIC_CUES.md` L42 | Panel cue missing |
| `production/S1/S1E01/MUSIC_CUES.md` L43 | Per-panel chords (S1–S2) |
| `production/S1/S1E01/MUSIC_CUES.md` L44 | Per-panel drone changes |

#### S1E02 (8)

| File:line | Type |
|---|---|
| `production/S1/S1E02/SCRIPT.md` L77 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E02/SCRIPT.md` L78 | Speaker |
| `production/S1/S1E02/SCRIPT.md` L79 | SFX |
| `production/S1/S1E02/ART_PROMPTS.md` L66 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E02/MUSIC_CUES.md` L40 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E02/MUSIC_CUES.md` L41 | Lead instrument |
| `production/S1/S1E02/MUSIC_CUES.md` L42 | Per-panel chords (S1–S2) |
| `production/S1/S1E02/MUSIC_CUES.md` L43 | Per-panel drone changes |

#### S1E03 (8)

| File:line | Type |
|---|---|
| `production/S1/S1E03/SCRIPT.md` L77 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E03/SCRIPT.md` L78 | Speaker |
| `production/S1/S1E03/SCRIPT.md` L79 | SFX |
| `production/S1/S1E03/ART_PROMPTS.md` L66 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E03/MUSIC_CUES.md` L40 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E03/MUSIC_CUES.md` L41 | Lead instrument |
| `production/S1/S1E03/MUSIC_CUES.md` L42 | Per-panel chords (S1–S2) |
| `production/S1/S1E03/MUSIC_CUES.md` L43 | Per-panel drone changes |

#### S1E04 (9)

| File:line | Type |
|---|---|
| `production/S1/S1E04/SCRIPT.md` L77 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E04/SCRIPT.md` L78 | Speaker |
| `production/S1/S1E04/SCRIPT.md` L79 | SFX |
| `production/S1/S1E04/ART_PROMPTS.md` L66 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E04/MUSIC_CUES.md` L45 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E04/MUSIC_CUES.md` L46 | Lead instrument |
| `production/S1/S1E04/MUSIC_CUES.md` L47 | Panel cue missing |
| `production/S1/S1E04/MUSIC_CUES.md` L48 | Per-panel chords (S1–S2) |
| `production/S1/S1E04/MUSIC_CUES.md` L49 | Per-panel drone changes |

#### S1E05 (8)

| File:line | Type |
|---|---|
| `production/S1/S1E05/SCRIPT.md` L77 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E05/SCRIPT.md` L78 | Speaker |
| `production/S1/S1E05/SCRIPT.md` L79 | SFX |
| `production/S1/S1E05/ART_PROMPTS.md` L68 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E05/MUSIC_CUES.md` L44 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E05/MUSIC_CUES.md` L45 | Lead instrument |
| `production/S1/S1E05/MUSIC_CUES.md` L46 | Per-panel chords (S1–S2) |
| `production/S1/S1E05/MUSIC_CUES.md` L47 | Per-panel drone changes |

#### S1E06 (10)

| File:line | Type |
|---|---|
| `production/S1/S1E06/SCRIPT.md` L77 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E06/SCRIPT.md` L78 | Speaker |
| `production/S1/S1E06/SCRIPT.md` L79 | SFX |
| `production/S1/S1E06/SCRIPT.md` L80 | Glassy bell not placed on a panel |
| `production/S1/S1E06/ART_PROMPTS.md` L67 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E06/MUSIC_CUES.md` L45 | Crawl: not defined (S1–S2 wording) |
| `production/S1/S1E06/MUSIC_CUES.md` L46 | Lead instrument |
| `production/S1/S1E06/MUSIC_CUES.md` L47 | Per-panel chords (S1–S2) |
| `production/S1/S1E06/MUSIC_CUES.md` L48 | Per-panel drone changes |
| `production/S1/S1E06/MUSIC_CUES.md` L49 | Glassy bell not placed on a panel |

#### S2E01 (8)

| File:line | Type |
|---|---|
| `production/S2/S2E01/SCRIPT.md` L80 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E01/SCRIPT.md` L81 | Panel location (P3; P4 in S3E04) |
| `production/S2/S2E01/SCRIPT.md` L82 | SFX |
| `production/S2/S2E01/ART_PROMPTS.md` L73 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E01/MUSIC_CUES.md` L48 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E01/MUSIC_CUES.md` L49 | Lead instrument |
| `production/S2/S2E01/MUSIC_CUES.md` L50 | Per-panel chords (S1–S2) |
| `production/S2/S2E01/MUSIC_CUES.md` L51 | Per-panel drone changes |

#### S2E02 (8)

| File:line | Type |
|---|---|
| `production/S2/S2E02/SCRIPT.md` L84 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E02/SCRIPT.md` L85 | Panel location (P3; P4 in S3E04) |
| `production/S2/S2E02/SCRIPT.md` L86 | SFX |
| `production/S2/S2E02/ART_PROMPTS.md` L73 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E02/MUSIC_CUES.md` L47 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E02/MUSIC_CUES.md` L48 | Lead instrument |
| `production/S2/S2E02/MUSIC_CUES.md` L49 | Per-panel chords (S1–S2) |
| `production/S2/S2E02/MUSIC_CUES.md` L50 | Per-panel drone changes |

#### S2E03 (8)

| File:line | Type |
|---|---|
| `production/S2/S2E03/SCRIPT.md` L84 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E03/SCRIPT.md` L85 | Panel location (P3; P4 in S3E04) |
| `production/S2/S2E03/SCRIPT.md` L86 | SFX |
| `production/S2/S2E03/ART_PROMPTS.md` L73 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E03/MUSIC_CUES.md` L49 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E03/MUSIC_CUES.md` L50 | Lead instrument |
| `production/S2/S2E03/MUSIC_CUES.md` L51 | Per-panel chords (S1–S2) |
| `production/S2/S2E03/MUSIC_CUES.md` L52 | Per-panel drone changes |

#### S2E04 (8)

| File:line | Type |
|---|---|
| `production/S2/S2E04/SCRIPT.md` L84 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E04/SCRIPT.md` L85 | Panel location (P3; P4 in S3E04) |
| `production/S2/S2E04/SCRIPT.md` L86 | SFX |
| `production/S2/S2E04/ART_PROMPTS.md` L73 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E04/MUSIC_CUES.md` L47 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E04/MUSIC_CUES.md` L48 | Lead instrument |
| `production/S2/S2E04/MUSIC_CUES.md` L49 | Per-panel chords (S1–S2) |
| `production/S2/S2E04/MUSIC_CUES.md` L50 | Per-panel drone changes |

#### S2E05 (8)

| File:line | Type |
|---|---|
| `production/S2/S2E05/SCRIPT.md` L86 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E05/SCRIPT.md` L87 | Panel location (P3; P4 in S3E04) |
| `production/S2/S2E05/SCRIPT.md` L88 | SFX |
| `production/S2/S2E05/ART_PROMPTS.md` L75 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E05/MUSIC_CUES.md` L48 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E05/MUSIC_CUES.md` L49 | Lead instrument |
| `production/S2/S2E05/MUSIC_CUES.md` L50 | Per-panel chords (S1–S2) |
| `production/S2/S2E05/MUSIC_CUES.md` L51 | Per-panel drone changes |

#### S2E06 (8)

| File:line | Type |
|---|---|
| `production/S2/S2E06/SCRIPT.md` L86 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E06/SCRIPT.md` L87 | Panel location (P3; P4 in S3E04) |
| `production/S2/S2E06/SCRIPT.md` L88 | SFX |
| `production/S2/S2E06/ART_PROMPTS.md` L76 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E06/MUSIC_CUES.md` L49 | Crawl: not defined (S1–S2 wording) |
| `production/S2/S2E06/MUSIC_CUES.md` L50 | Lead instrument |
| `production/S2/S2E06/MUSIC_CUES.md` L51 | Per-panel chords (S1–S2) |
| `production/S2/S2E06/MUSIC_CUES.md` L52 | Per-panel drone changes |

#### S3E01 (6)

| File:line | Type |
|---|---|
| `production/S3/S3E01/SCRIPT.md` L83 | Crawl: S3E01 GAP wording |
| `production/S3/S3E01/SCRIPT.md` L84 | Panel location (P3; P4 in S3E04) |
| `production/S3/S3E01/SCRIPT.md` L85 | SFX |
| `production/S3/S3E01/ART_PROMPTS.md` L70 | Crawl: S3E01 GAP wording |
| `production/S3/S3E01/MUSIC_CUES.md` L45 | Crawl: S3E01 GAP wording |
| `production/S3/S3E01/MUSIC_CUES.md` L46 | Chords for the swung sections (S3) |

#### S3E02 (6)

| File:line | Type |
|---|---|
| `production/S3/S3E02/SCRIPT.md` L86 | Crawl: not in this episode (S3E02–E05 line) |
| `production/S3/S3E02/SCRIPT.md` L90 | Panel location (P3; P4 in S3E04) |
| `production/S3/S3E02/SCRIPT.md` L91 | SFX |
| `production/S3/S3E02/ART_PROMPTS.md` L72 | Crawl: not in this episode (S3E02–E05 line) |
| `production/S3/S3E02/MUSIC_CUES.md` L45 | Crawl: not in this episode (S3E02–E05 line) |
| `production/S3/S3E02/MUSIC_CUES.md` L49 | Chords for the swung sections (S3) |

#### S3E03 (6)

| File:line | Type |
|---|---|
| `production/S3/S3E03/SCRIPT.md` L85 | Crawl: not in this episode (S3E02–E05 line) |
| `production/S3/S3E03/SCRIPT.md` L89 | Panel location (P3; P4 in S3E04) |
| `production/S3/S3E03/SCRIPT.md` L90 | SFX |
| `production/S3/S3E03/ART_PROMPTS.md` L73 | Crawl: not in this episode (S3E02–E05 line) |
| `production/S3/S3E03/MUSIC_CUES.md` L45 | Crawl: not in this episode (S3E02–E05 line) |
| `production/S3/S3E03/MUSIC_CUES.md` L49 | Chords for the swung sections (S3) |

#### S3E04 (6)

| File:line | Type |
|---|---|
| `production/S3/S3E04/SCRIPT.md` L92 | Crawl: not in this episode (S3E02–E05 line) |
| `production/S3/S3E04/SCRIPT.md` L96 | Panel location (P3; P4 in S3E04) |
| `production/S3/S3E04/SCRIPT.md` L97 | SFX |
| `production/S3/S3E04/ART_PROMPTS.md` L74 | Crawl: not in this episode (S3E02–E05 line) |
| `production/S3/S3E04/MUSIC_CUES.md` L47 | Crawl: not in this episode (S3E02–E05 line) |
| `production/S3/S3E04/MUSIC_CUES.md` L51 | Chords for the swung sections (S3) |

#### S3E05 (6)

| File:line | Type |
|---|---|
| `production/S3/S3E05/SCRIPT.md` L94 | Crawl: not in this episode (S3E02–E05 line) |
| `production/S3/S3E05/SCRIPT.md` L98 | Panel location (P3; P4 in S3E04) |
| `production/S3/S3E05/SCRIPT.md` L99 | SFX |
| `production/S3/S3E05/ART_PROMPTS.md` L75 | Crawl: not in this episode (S3E02–E05 line) |
| `production/S3/S3E05/MUSIC_CUES.md` L46 | Crawl: not in this episode (S3E02–E05 line) |
| `production/S3/S3E05/MUSIC_CUES.md` L50 | Chords for the swung sections (S3) |

#### S3E06 (8)

| File:line | Type |
|---|---|
| `production/S3/S3E06/SCRIPT.md` L107 | Panel location (P3; P4 in S3E04) |
| `production/S3/S3E06/SCRIPT.md` L108 | SFX |
| `production/S3/S3E06/SCRIPT.md` L109 | Next section |
| `production/S3/S3E06/SCRIPT.md` L110 | S3E06 painted-board placer |
| `production/S3/S3E06/ART_PROMPTS.md` L79 | Fidelity note not in file (P2, P3) |
| `production/S3/S3E06/MUSIC_CUES.md` L55 | Chords for the swung sections (S3) |
| `production/S3/S3E06/MUSIC_CUES.md` L56 | S3E06 P5 bloom chord |
| `production/S3/S3E06/MUSIC_CUES.md` L57 | S3E06 crawl music cue |

### B2. Summary count by type

| Type | Count |
|---|---|
| Crawl: not defined (S1–S2 wording) | 36 |
| SFX | 18 |
| Lead instrument | 12 |
| Per-panel chords (S1–S2) | 12 |
| Per-panel drone changes | 12 |
| Panel location (P3; P4 in S3E04) | 12 |
| Crawl: not in this episode (S3E02–E05 line) | 12 |
| Speaker | 6 |
| Chords for the swung sections (S3) | 6 |
| Glassy bell not placed on a panel | 3 |
| Crawl: S3E01 GAP wording | 3 |
| Panel cue missing | 2 |
| Next section | 1 |
| S3E06 painted-board placer | 1 |
| Fidelity note not in file (P2, P3) | 1 |
| S3E06 P5 bloom chord | 1 |
| S3E06 crawl music cue | 1 |
| **Total** | **139** |

### B3. Summary count by episode

| Episode | SCRIPT | ART_PROMPTS | MUSIC_CUES | Total |
|---|---|---|---|---|
| S1E01 | 4 | 1 | 5 | 10 |
| S1E02 | 3 | 1 | 4 | 8 |
| S1E03 | 3 | 1 | 4 | 8 |
| S1E04 | 3 | 1 | 5 | 9 |
| S1E05 | 3 | 1 | 4 | 8 |
| S1E06 | 4 | 1 | 5 | 10 |
| S2E01 | 3 | 1 | 4 | 8 |
| S2E02 | 3 | 1 | 4 | 8 |
| S2E03 | 3 | 1 | 4 | 8 |
| S2E04 | 3 | 1 | 4 | 8 |
| S2E05 | 3 | 1 | 4 | 8 |
| S2E06 | 3 | 1 | 4 | 8 |
| S3E01 | 3 | 1 | 2 | 6 |
| S3E02 | 3 | 1 | 2 | 6 |
| S3E03 | 3 | 1 | 2 | 6 |
| S3E04 | 3 | 1 | 2 | 6 |
| S3E05 | 3 | 1 | 2 | 6 |
| S3E06 | 4 | 1 | 3 | 8 |
| **Total** | **57** | **18** | **64** | **139** |

### B4. Type by season

| Type | S1 | S2 | S3 |
|---|---|---|---|
| Crawl: not defined (S1–S2 wording) | 18 | 18 | 0 |
| SFX | 6 | 6 | 6 |
| Lead instrument | 6 | 6 | 0 |
| Per-panel chords (S1–S2) | 6 | 6 | 0 |
| Per-panel drone changes | 6 | 6 | 0 |
| Panel location (P3; P4 in S3E04) | 0 | 6 | 6 |
| Crawl: not in this episode (S3E02–E05 line) | 0 | 0 | 12 |
| Speaker | 6 | 0 | 0 |
| Chords for the swung sections (S3) | 0 | 0 | 6 |
| Glassy bell not placed on a panel | 3 | 0 | 0 |
| Crawl: S3E01 GAP wording | 0 | 0 | 3 |
| Panel cue missing | 2 | 0 | 0 |
| Next section | 0 | 0 | 1 |
| S3E06 painted-board placer | 0 | 0 | 1 |
| Fidelity note not in file (P2, P3) | 0 | 0 | 1 |
| S3E06 P5 bloom chord | 0 | 0 | 1 |
| S3E06 crawl music cue | 0 | 0 | 1 |

### B5. Inline GAP markers in the body of each file (108)

These are the in-body markers (table cells and field lines) that sit above each file's Open gaps heading. They mark the same gaps as B1 at the panel or field where they occur; they are listed for completeness and are not added to the B2–B4 counts.

| File | Lines |
|---|---|
| `production/S1/S1E01/SCRIPT.md` | L29 |
| `production/S1/S1E01/MUSIC_CUES.md` | L15, L23, L24, L25, L26, L27, L28 |
| `production/S1/S1E02/SCRIPT.md` | L29 |
| `production/S1/S1E02/MUSIC_CUES.md` | L15, L23, L24, L25, L26, L27, L28 |
| `production/S1/S1E03/SCRIPT.md` | L29 |
| `production/S1/S1E03/MUSIC_CUES.md` | L15, L24, L25, L26, L27, L28 |
| `production/S1/S1E04/SCRIPT.md` | L65 |
| `production/S1/S1E04/MUSIC_CUES.md` | L15, L23, L24, L25, L26, L27, L28 |
| `production/S1/S1E05/SCRIPT.md` | L29 |
| `production/S1/S1E05/MUSIC_CUES.md` | L15, L23, L24, L25, L26, L27 |
| `production/S1/S1E06/SCRIPT.md` | L29 |
| `production/S1/S1E06/MUSIC_CUES.md` | L15, L23, L24, L25, L26, L27 |
| `production/S2/S2E01/SCRIPT.md` | L38 |
| `production/S2/S2E01/MUSIC_CUES.md` | L15, L24, L25, L26, L27, L28 |
| `production/S2/S2E02/SCRIPT.md` | L42 |
| `production/S2/S2E02/MUSIC_CUES.md` | L15, L24, L25, L26, L27, L28 |
| `production/S2/S2E03/SCRIPT.md` | L42 |
| `production/S2/S2E03/MUSIC_CUES.md` | L15, L24, L26, L27, L28 |
| `production/S2/S2E04/SCRIPT.md` | L42 |
| `production/S2/S2E04/MUSIC_CUES.md` | L15, L24, L25, L26, L27, L28 |
| `production/S2/S2E05/SCRIPT.md` | L44 |
| `production/S2/S2E05/MUSIC_CUES.md` | L15, L24, L26, L27, L28 |
| `production/S2/S2E06/SCRIPT.md` | L44 |
| `production/S2/S2E06/MUSIC_CUES.md` | L15, L26, L27, L28 |
| `production/S3/S3E01/SCRIPT.md` | L41 |
| `production/S3/S3E01/MUSIC_CUES.md` | L23, L24, L27 |
| `production/S3/S3E02/SCRIPT.md` | L44 |
| `production/S3/S3E02/MUSIC_CUES.md` | L23, L24, L27 |
| `production/S3/S3E03/SCRIPT.md` | L43 |
| `production/S3/S3E03/MUSIC_CUES.md` | L23, L24, L27 |
| `production/S3/S3E04/SCRIPT.md` | L55 |
| `production/S3/S3E04/MUSIC_CUES.md` | L23, L24, L25 |
| `production/S3/S3E05/SCRIPT.md` | L48 |
| `production/S3/S3E05/MUSIC_CUES.md` | L23, L24, L27 |
| `production/S3/S3E06/SCRIPT.md` | L49 |
| `production/S3/S3E06/MUSIC_CUES.md` | L27, L28, L31, L32 |

Not a GAP marker: `production/S2/S2E02/SCRIPT.md` L71 is the P6 caption text, which contains the word GAP as story text.

None-for-prompts items (not GAPs): 18, one in every ART_PROMPTS file.

## D. Season 0 episode files (no production sets; noted only)

The README's Known gaps note for S0 is at `production/README.md` L81. Checked against `episodes/E01_THE_GATE.md` to `episodes/E06_THE_QUIET_BOARD.md` on main:

1. **No S0 season sheet or lock.** `seasons/` has no S0 file (see A7 item 12). Holds.
2. **No music-cue sections.** None of E01–E06 has a music or cue heading; their headings are panels, prompt stems and Reject only (e.g. `episodes/E04_THE_SUAVE_HOUR.md` L54, `episodes/E06_THE_QUIET_BOARD.md` L58). Holds.
3. **Prompt lines.** E01–E03 have no per-panel prompt lines. E04–E06 have a stem heading (`episodes/E04_THE_SUAVE_HOUR.md` L7, `episodes/E05_LAB_NIGHT.md` L9, `episodes/E06_THE_QUIET_BOARD.md` L9) and per-panel prompt lines. Not papered over: README L81 says only E03 has an episode-level stem (`episodes/E03_WHITE_HAT.md` L20). E02 also has one (`episodes/E02_THE_RECYCLER.md` L25), and E01 has none. The README cite holds only in part; the README is not edited here.
4. **No Reject section in E01–E03.** E04–E06 have one (`episodes/E04_THE_SUAVE_HOUR.md` L54, `episodes/E05_LAB_NIGHT.md` L58, `episodes/E06_THE_QUIET_BOARD.md` L58).
5. **Panel counts.** E01 has 5 panel headings (`episodes/E01_THE_GATE.md` L26 is Panel 5), E02 has 4 (`episodes/E02_THE_RECYCLER.md` L20 is Panel 4), and E03 has 3 (`episodes/E03_WHITE_HAT.md` L15 is Panel 3). E04–E06 have 6. These are noted only; no panel count is proposed.
6. **Crawl and SFX.** There is no crawl (`production/README.md` L82) and no SFX field (`production/README.md` L83).
7. **Choir flag.** The S0 choir flag reads no (`production/README.md` L81).
8. **No S0 production sets.** `production/` holds only `README.md` and the S1, S2 and S3 folders.
