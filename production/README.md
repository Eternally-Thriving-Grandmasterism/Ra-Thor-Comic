# Production — Script Format (production prep)

Status: production prep for the existing arcs only: Season 0 (E01–E06), Season 1 (arc A), Season 2 (arc C) and Season 3 (arc B) (council ruling, 2026-10-01 1:40 PM ET). No S4 and no new arc until Sherif names one. No canon changes. This file defines a format only; it contains no episode scripts.

Sources, and the only sources: the merged episode files in `episodes/`, `00_FIDELITY_PROTOCOL.md`, `01_VISUAL_STYLE_GUIDE.md`, `03_TONE_SPECS.md`, `04_VISUAL_CANON.md`, `05_LORE_BIBLE.md`, `06_MUSIC_SPEC.md`, `09_CHARACTER_BIBLE.md`, `10_LOCATION_BIBLE.md`, and the season locks and sheets in `seasons/`. Where they disagree, `00`, `03`, `04`, `05` and `06` win.

## Rules

1. **Nothing new on the page.** No new lines, captions, guests, props, cues or canon. Production files restate; they never author.
2. **Every line traceable.** Each caption, bubble, card text and stage direction cites its source: the episode file and panel (e.g. `S1E01 P4`), or a canon doc and section (e.g. `06 §3.2`). Captions and bubbles are copied verbatim, punctuation included.
3. **Gaps are flagged, never filled.** If the episode file does not give a field, write `GAP: not in <file>` and list it under "Open gaps" at the end of the file. Do not infer a key, a BPM, a location, a sound or a count.
4. **Prop counts in prompts only.** Counts may appear in art prompts (ruling, PR #36). Captions and bubbles never gain numbers beyond what the episode file already has.
5. **Fixed bounds hold.** Canon armor (00, 01, 04); faces hidden; no outside IP, brands, real people or "like X" (05 rules 6–8; 06 §5); the Founder implied only (05 Q3); TOLC named only; series title on packaging only (PR #27); no health claims for any frequency (06 §4).
6. **AGiRBE and Fresco.** The AGiRBE line and the Fresco credit appear only in docs and the end-credits crawl, never on a page, panel, card, prompt, cover, title card or promo art. Fresco is never depicted. Crawl text is copied only from `seasons/S3_SEASON_SHEET.md` §7, the one source of truth. S0–S2 scripts write `No crawl defined (only S3 sheet §7 defines one)` and list it under Open gaps; never invent a crawl. Any S0–S2 crawl is a later ruling.

## Files and location

One folder per episode, three files each:

```
production/S0/E01/{SCRIPT,ART_PROMPTS,MUSIC_CUES}.md   … production/S0/E06/
production/S1/S1E01/{SCRIPT,ART_PROMPTS,MUSIC_CUES}.md … production/S1/S1E06/
production/S2/S2E01/…  production/S3/S3E01/…
```

Season 0 folders use the episode file's own IDs (`E01`–`E06`, from `episodes/E01_THE_GATE.md` etc.). Each file opens with a header: episode ID, title, source file path, main commit it was built from, lead mode (03), and status (`draft` until council review).

## (a) SCRIPT.md — panel-by-panel

One block per panel, in the episode file's order:

| Field | Content | Source |
|---|---|---|
| Panel | number and heading, as in the file | episode file |
| Location | Threshold / Recycler Bay / Quiet Room / object flashback, as stated | episode file; 10 for set names |
| Action / staging | the file's stage direction, trimmed, not added to | episode file |
| Captions | verbatim | episode file |
| Bubbles | verbatim, with speaker (Ra-Thor, guest, council mask and its clock position) | episode file |
| SFX | only sounds the file or its music section names (e.g. the fixed "Blocked." thud, a drum hiccup); otherwise `none in file` | episode file; 06 §1 |
| Continuity notes | fidelity notes from the file, plus the canon rule each panel must keep (eye-seal on the shield, hammer head-down, one bubble per panel) | episode file; 00; 01; season sheet |

End with: Recycler items and CLEAN card text (verbatim), and "Open gaps".

## (b) ART_PROMPTS.md — per panel

- **Stem.** The episode file's prompt stem if it has one; otherwise the `01_VISUAL_STYLE_GUIDE.md` stem, marked as such.
- **Set add-on.** As in the episode file (mode lighting per 03).
- **Per panel.** The file's `Prompt:` line verbatim. If the file has no prompt line for a panel, write `GAP: no prompt in file` and do not write one.
- **Prop counts.** Allowed here only (ruling, PR #36).
- **Design references.** Cite, don't restate: armor and emblem (04 canon rulings; 01 "Locked details"); the Founder's objects (05 Q3); faction and guest looks (05 Q9; the season lock and sheet; the Watcher per `seasons/S3_SEASON_SHEET.md` §3); detection device (season sheet's device table).
- **Rejects.** The episode file's Reject list plus `01` Reject.

## (c) MUSIC_CUES.md — per panel

Header row from the episode file and its season sheet: lead mode, key, BPM, lead instrument, borrow. Then one row per panel:

| Field | Rule | Source |
|---|---|---|
| Cue | the file's cue for that panel (groove, drop-out, held pad, silence) | episode file |
| Key / BPM | as stated; BPM within the mode range | episode file; season sheet; 06 §2 |
| Drone | on/off per panel, and its pitch: 108 Hz for A- and D-major beds, E2 80.91 or B2 121.23 Hz for E-major beds, 54 Hz siege only and doubled; S3 drones only under the 543-pad sections | 06 §3.3–3.4; season lock |
| 543 Hz | held only over chords containing C#; muted over any C natural | 06 §3.2 |
| 528 Hz | short chime on the bloom only, never held | 06 §3.2 |
| Stingers | "Blocked." = low muted thud + filter close; "That one can live." = major bloom + 528 chime; card stingers OBVIOUS / FERAL / CLEAN where the file has them | 06 §1, §2 |
| Choir | flag `YES` only where the file has it: one wordless swell, E06 only (S1E06, S2E06, S3E06 per the S1 sheet and the S2 and S3 locks); otherwise `no` | season sheets/locks; 06 §5 |
| Ending | Grounded motif: four notes rise, land on the tonic, hold | 06 §1 |

Footer: tuning A4 = 432, wordless in-episode, mood words only (no artist, band, label or track names), no health claims (06 §4–5).

## Next script cards (in order)

Sherif picked The Long Table to open S1, and the rich S1 files test the full format first. S0 comes later, as a gap audit after S1–S3, and is never filled in.

1. **Card 1 — S1E01, The Ribbon Clause:** full set (SCRIPT, ART_PROMPTS, MUSIC_CUES), the Season 1 opener.
2. **Card 2 — S1E02, The Tall Chair:** full set.
3. **Card 3 — S1E03, The Ghost Clause:** full set.

## Known gaps (from the merged files)

- Season 0 has no season sheet or lock, and E01–E06 have no music-cue sections; E01–E03 also have no per-panel prompt lines (E03 has one episode-level prompt stem). S0 is handled later, after S1–S3, as a gap audit only: its gaps are listed, never filled in. The S0 choir flag reads `no` (no S0 file records a choir swell).
- Only S3 defines an end-credits crawl (`seasons/S3_SEASON_SHEET.md` §7). S0–S2 scripts record `No crawl defined (only S3 sheet §7 defines one)` under Open gaps.
- No episode file has a dedicated SFX field; SFX come only from sounds named in the stage directions and the fixed stingers.
