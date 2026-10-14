# Ship-readiness audit: Ra-Thor⚡️Living Thunder

**Status: audit only. Polish-only scope, council-approved.** This file adds no episode, no canon and no replacement text. It flags every gap and fills none. It edits no other file.

**Built from:** `main` at `c1e00a3` ("Screen: S1E01 + S1E02 teleplay amend per Steward ruling (R1 R5 X6) (#74)"). Read in this order: `00_FIDELITY_PROTOCOL.md` first, then `READING_ORDER.md`, `02`, `03`, `05`, `06`, the episode files, `production/`, `screen/` and `seasons/`.

**Goal.** Sherif wants polished comics (Amazon and Patreon) and an animated trailer, maybe a pilot, built only from what already exists.

## 1. Bottom line

1. **There is no art and no audio in the repo.** Every tracked file is Markdown (plus `LICENSE`). "Art assets" means prompt text only. No rendered panel, cover, lettered page, storyboard frame, cue or stem exists here. Anything rendered outside the repo is invisible to this audit. Ship-readiness is therefore "prompts and scripts ready to render", not "assets ready to publish".
2. **Season 0 has no production set.** `production/` holds `S1/`, `S2/` and `S3/` only (confirmed in `production/S0_GAP_AUDIT.md` §B1). E01–E06 have no `SCRIPT.md`, `ART_PROMPTS.md` or `MUSIC_CUES.md`.
3. **Screen packages exist for S1E01 and S1E02 only.** S1E04 has an episode file and a production set, but no beat sheet, teleplay, shot list, storyboard prompts or score plan.
4. **The full title does not appear anywhere in the repo.** `Ra-Thor⚡️Living Thunder` and the bare `⚡️` return zero hits. Every title use is the short form (section 6).
5. **Every episode status line still says "not yet prompted"** (S0 E04–E06 and all of S1–S3), although each file carries six `Prompt:` lines. The status text and the file contents disagree. The status line is canon text, so this audit flags it and does not edit it.
6. **Recommendation:** comic issue #1 = **E01 The Gate**. Trailer (60–90 s) = **S1E01 The Ribbon Clause**. Reasons and steps are in sections 4 and 5.

## 2. Legend

| Term | Meaning |
|---|---|
| **Finished** | Script locked, or all six panels, prompts and reject list present, with no open GAP or PROPOSED CANON in the file |
| **Rough** | Present but thinner than the later episodes, or carries open items that block use |
| **Skeleton** | Outline-level only |
| **GAP** | A marker where the source gives no field. Never filled in this audit |
| **PC** | `PROPOSED CANON — pending council ratification` tag |

## 3. Inventory

### 3.1 Season 0 episodes (comic files only; no production set exists for any of them)

| Item | Completeness | Open GAP / PC | Outside-IP risk | Title-line / notes |
|---|---|---|---|---|
| `episodes/E01_THE_GATE.md` | **Finished script** (status "script locked"), 5 panels. No `Prompt:` lines and no stem in the file. Art is **rough**: status says the pass panel's armor drifted (shield gem instead of eye-seal) and must be rerun before print. | GAP 0. PC 0. Open item: the eye-seal rerun. | None found. Cards OBVIOUS / FERAL / CLEAN are fine. The word "Captain" appears nowhere in the repo; keep it that way. | No title use. |
| `episodes/E02_THE_RECYCLER.md` | **Rough**. 4 panels, no status line, only a prompt stem, no per-panel prompts, no reject list. | GAP 0. PC 0. Missing status line is itself an open item. | None found. | None. |
| `episodes/E03_WHITE_HAT.md` | **Skeleton**. 3 panels, no status line, stem only, no reject list. Shortest file in the repo. | GAP 0. PC 0. | None found. It is a story device only (00 rule 5): no claim of certification or authority. | None. |
| `episodes/E04_THE_SUAVE_HOUR.md` | **Finished (draft)**. 6 panels, 6 prompts, stem, set add-on, reject list. Not Season 1's S1E04. | GAP 0. PC 0. Status says "not yet prompted" yet prompts are present. | Low: the set add-on says "spy-thriller elegance". It names a genre, not a work, but `03_TONE_SPECS.md` L5 bars reaching for outside references, so a lawyer or the council may want to look. The same phrase is in S1E01–S1E06 and in both storyboard files. Counterpart is invented and faceless. | None. |
| `episodes/E05_LAB_NIGHT.md` | **Finished (draft)**. 6 panels, 6 prompts, reject list. | GAP 0. PC 0. | "Cartoon-lab gag timing" is generic. None found. | None. |
| `episodes/E06_THE_QUIET_BOARD.md` | **Finished (draft)**. 6 panels, 6 prompts, reject list. Silent bubbles in P1–P5 (ellipsis only). | GAP 0. PC 0. | None found. | None. |

### 3.2 Season 1 (arc A, The Long Table)

| Item | Completeness | Open GAP / PC | Outside-IP risk | Title-line / notes |
|---|---|---|---|---|
| `episodes/S1E01`–`S1E06` | **Finished (draft)**. 6 panels, 6 prompts, reject list, music section each. | GAP 0 in the episode files. PC 0. Each file carries the `[HOUSE-X]` placeholder, ruled as glyph-only and never on the page (Q9, `seasons/S1_SEASON_SHEET.md` L82). | "Spy-thriller elegance" (low, as above). Envoy faces are hidden and invented. | None. |
| `production/S1/S1E01`–`S1E06` (SCRIPT, ART_PROMPTS, MUSIC_CUES) | **Finished (draft)** as restatements. Audit counts of open items: S1E01 10, S1E02 8, S1E03 8, S1E04 9, S1E05 8, S1E06 10 (`production/S0_GAP_AUDIT.md` §B1, taken as audited, not re-counted). | Open gaps by type: no crawl (S1–S2 wording), bubble speaker not named (P2 or P6), no SFX field, per-panel chords, per-panel drone changes, lead instrument. S1E01 also has the glassy bell not placed on a panel. PC 0. | None found. | None. |
| **S1E04 The Sideways Glass** (comic, production set) | Finished (draft). Hourglass gag. **No screen package.** | Production gaps: P1 cue, "Next." speaker, lead instrument, chords. PC 0. | None found. | None. |

### 3.3 Season 2 (arc C) and Season 3 (arc B)

| Item | Completeness | Open GAP / PC | Outside-IP risk | Title-line / notes |
|---|---|---|---|---|
| `episodes/S2E01`–`S2E06`, `S3E01`–`S3E06` | **Finished (draft)**, 6 panels, 6 prompts each. Longest and most constrained files in the repo (13–20 KB). | GAP 0 in episode files. PC 0. | **Real person named in docs:** Jacque Fresco appears in `seasons/S3_SEASON_SHEET.md` (inspiration credit and crawl). Ruled docs-and-end-credits-crawl only (PR #31, #38). Never on a page, cover, title card, prompt or promo art. The AGiRBE line has the same rule. Both are a **trailer risk**: keep them out of any cut. S2 and S3 also depend on the Founder (implied only, 05 Q3) and Colossusoft/Powrush-MMO, which are owner names, not outside IP. | S2E05 P2 is the only "wink" and carries no title. |
| `production/S2/*`, `production/S3/*` | **Finished (draft)**. Audit counts: S2E01–S2E06 8 each; S3E01–S3E05 6 each; S3E06 8. Extra open item in S3: where the end-credits crawl is placed. | Types as in S1, plus "Location: not stated in file" for the mask close-ups (S2E02, S3E01, S3E04). PC 0. | As above. | None. |

### 3.4 Screen packages (the only teleplay, beat sheet, shot list, storyboard and score material)

| Item | Completeness | Open GAP / PC | Outside-IP risk | Title-line / notes |
|---|---|---|---|---|
| **S1E01** `screen/S1E01/` BEAT_SHEET, TELEPLAY, SHOT_LIST, STORYBOARD_PROMPTS, SCORE_PLAN | **Finished (draft for council review)**. 39 shots, about 185 s of picture before main titles. GAP_RULINGS G1–G10 ruled; ratification ledger: 13 items RULED/ACCEPT, 3 REFUSED by Steward ruling (R1, R5, X6). | **GAP markers still in the working files:** 2 in `BEAT_SHEET.md` (L165, L167), 2 in `SHOT_LIST.md` (S13, S33). Both pairs come from the X6/R5 cuts. **PC tags still open (grep counts, all sub-lines):** TELEPLAY 26, STORYBOARD 16, SHOT_LIST 12, BEAT_SHEET 10, SCORE_PLAN 4. Ratified items still carry the tag; whether to strip it is a council call. `MAIN TITLES` (TELEPLAY L50) is a PC placeholder; the intro theme is "outside this plan". | None found beyond "spy-thriller elegance" (low). All 15 storyboard rejects name only prohibitions (superhero logos, xAI marks). | Title cards in the teleplay are episode captions, not series title cards. No series title card is defined. |
| **S1E02** `screen/S1E02/` (same five files plus SCREEN_ADDENDUM) | **Finished (draft)**. 37 shots, about 175 s. Ledger: **25 of 29 items still PENDING COUNCIL**, 3 ruled, 1 refused. | GAP markers in TELEPLAY (L201), SHOT_LIST (S31) and BEAT_SHEET (L165): the X6 handover cut. PC tags open (grep counts): TELEPLAY 24, STORYBOARD 15, SHOT_LIST 11, BEAT_SHEET 12, SCORE_PLAN 7, SCREEN_ADDENDUM 3. `MAIN TITLES` at TELEPLAY L55 is the same placeholder. | As S1E01. | As S1E01. |
| `screen/SCREEN_BIBLE_ADDENDUM.md` | Whole file is **PROPOSED**, pending ratification. Every screen rule rests on it. | PC 5, GAP 6 (grep counts). | None found; it carries the no-outside-references rule. | Defines `TITLE CARD:` format for dossier captions only. |

### 3.5 Bibles, specs, sheets and support files

| Item | Completeness | Open GAP / PC | Outside-IP risk | Title-line / notes |
|---|---|---|---|---|
| `00`, `01`, `04` (fidelity, style, visual canon) | Finished. 00 is obeyed throughout this audit. | None | `01` reject list names "modern superhero logos" and "xAI wordmarks" as prohibitions, which is correct. | None. |
| `02_SERIES_STRUCTURE.md` | Finished, but thin. | None | None | **L3 "Working title: Living Thunder"**. Short form on first mention, and "working title" implies the full title is unruled. |
| `03_TONE_SPECS.md`, `09`, `10` | Finished. | None | None found. | `03` L3 short form only. Fine as a doc. |
| `05_LORE_BIBLE.md` | Finished sourced draft. The "Founder", Fresco and AGiRBE rules live here. | None open. | Names "an online fantasy MMO" without naming it, which is the correct handling. Fresco: docs only. | L3 short form on first mention. |
| `06_MUSIC_SPEC.md` | Finished spec. §6 still lists open questions (synthwave flavor; who composes: in-house, commissioned or AI-assisted). | Open questions are unanswered. | No artist, band, label or track names, by ruling (§5). Sung words only in intro and outro. | L3 short form first mention; it already scopes the file to "comic motion and trailer use". |
| `README.md` | Finished. Status paragraph says S1E01/S1E02 screen packages are drafts. | None | Mentions "Grok Imagine" (L12) and xAI (L26) as a tool and a disclaimer. Fine in a bible, but never put either on a cover or in store copy. Links the sibling "Odyssey" and "Homer visual bible" repos (own repos; "Homer" is a public-domain name but is a reference to another work, so flag for a quick look). | **L1 H1 "Living Thunder — Ra-Thor Comic Series Bible"**. First mention is short form. |
| `bots/GROKBOT_COMIC_SEAT.md`, `bots/ROUTINE.md` | Finished, internal. | None | Name a third-party product ("Grok app", display name "Grokbot - Living Thunder"). Keep it internal; never in packaging or marketing. | Display name uses the short form; it is an external app label, not packaging. |
| `seasons/*` (S1 sheet, S2/S3 arc locks and sheets) | Finished. Season sheets for S2 and S3 hold the rulings ledgers and the S3 crawl (§7). | None open. | Fresco and AGiRBE (see 3.3). | Packaging-only rule for the title is here (S2 sheet §5 item 8). |
| `production/README.md`, `S0_GAP_AUDIT.md`, `CONTINUITY_LEDGER.md` | Process files. Ledger: 6 items ruled, 0 pending. Audit predates the screen packages. | The audit counts as of `a984ec9`. | None | Production README rule 5: "series title on packaging only (PR #27)". |

## 4. Recommendations

### 4.1 Comic issue #1: **E01 The Gate**

**Why.**
- It is the only episode whose status reads "script locked", and the master index calls it the pilot.
- It is first in the council-ruled reading order (Season 0 first, `READING_ORDER.md`, 3–0), and "each stands alone" (`02` L4), so a newcomer needs no lore.
- Its comic file carries no GAP and no PC tags. The open items are art-side only: the eye-seal rerun, and the missing production set.
- It teaches the series rules in five panels: Block, Pass, Recycle, Next, hammer grounded.

**Caveats to put in front of Sherif (none resolvable here).**
- **Length.** Five panels is not a retail issue. The repo has no page-count or format ruling. Padding it would add canon, which is out of scope. Options for Sherif: bundle E01–E03 or E01–E06 as an anthology issue, or ship E01 as a short. Both need a packaging ruling.
- **Fallback.** If Sherif wants a comic with a complete production set today, S1E01 is the alternative: 6 panels, full set, and 10 production-level open items that are mostly music and SFX, so they do not touch a printed page. The cost is that it opens an arc and leans on the Ninefold Houses lore.

### 4.2 Trailer, 60–90 s: **S1E01 The Ribbon Clause**

**Why.**
- It is the only episode with a full screen package: beat sheet, teleplay, 39-shot list, storyboard prompts and score plan.
- Its ledger has 13 items ruled ACCEPT and three REFUSED cuts, so it is the most-ratified screen material.
- The Block / Recycle / Pass beats cut down cleanly from the shot list.
- The fixed stinger (C09) and Grounded motif (C10) are ruled in the episode file.

**Caveats.**
- A trailer is new editorial material (cut order, trailer card, VO if any). No trailer ruling or spec exists. Keep it to picking existing shots and cues, and flag every added element for council review.
- Do not use shots S13 or S33. Both are GAP markers after the X6/R5 cuts.
- No Fresco or AGiRBE material in any frame (production README rule 6).
- The full title card needs a ruling on where and how (section 6).

## 5. Polish steps, in order

### 5.1 E01 The Gate (comic issue #1)

1. **Get a council ruling on format.** Standalone short, or bundled with other Season 0 shorts (Sherif's call). Nothing else is blocked on it, but page count drives every later step.
2. **Reconcile E01's status line.** It says five panels were prompted on 2026-09-30, but no prompts are in the repo. Either the prompts live elsewhere (locate them) or the status is stale. Do not invent them.
3. **Produce a Season 0 production set for E01** (`production/S0/E01/{SCRIPT,ART_PROMPTS,MUSIC_CUES}.md`) using the existing format in `production/README.md`. It restates; it never authors. Mark every missing field `GAP: not in <file>`. This is a new-file step needing a council card, because `production/README.md` lists S0 folders as format only.
4. **Render the five panels and apply the 00 fidelity checks.** Eye-seal on every shield, hammer grounded, one bubble per panel, no xAI marks.
5. **Rerun the pass panel (P3)** with the eye-seal. Reject any drift per rule 7.
6. **Letter the page.** Bubbles and captions copied verbatim from the episode file.
7. **Naming pass on the packaging.** Full title `Ra-Thor⚡️Living Thunder` on the cover and any title card, short form after (section 6). Needs the ruling in section 6 first.
8. **Store copy review.** No health claims for any frequency (06 §4). No certification, affiliation or legal authority for the Recycler or White-Hat devices (00 rule 5). No xAI or Grok marks.
9. **Final outside-IP sweep** of cover, copy and metadata, including the spy-thriller phrase if any prompt text is public.

### 5.2 S1E01 The Ribbon Clause (trailer)

1. **Ask the council to rule S1E01's open screen items**, or confirm the trailer may use only the 13 RULED/ACCEPT shots. Four items stay pending Sherif's word by the ledger's own rules.
2. **Decide the fate of the PC tags** on ratified lines. Stripping tags is a canon-file edit, so it needs its own card.
3. **Rule on `MAIN TITLES`** (TELEPLAY L50) and the intro theme, which the plan says is outside it. A trailer needs a title card, and none is defined.
4. **Fix the render style.** `screen/SCREEN_BIBLE_ADDENDUM.md` L89 says render style is not yet ruled; storyboards stay inked comic linework.
5. **Select shots from the 39** that cover Block, Recycle and Pass, excluding S13 and S33. Target 60–90 s. Selection only; no new shots.
6. **Resolve the music questions in 06 §6** (who composes, synthwave flavor) before any cue is made. Resolve the S1E01 MUSIC_CUES gaps (lead instrument, per-panel chords, drone changes) with the composer under the ruled G5–G10 frame.
7. **Render the key frames** from `STORYBOARD_PROMPTS.md`. Check each against the Reject line and armor canon.
8. **Final outside-IP sweep.** No Fresco, no AGiRBE, no Captain Obvious, no brands, no "like X" in the cut or its metadata.

## 6. Naming rule (full title on first mention, covers and title cards; short forms fine)

Rule as given: `Ra-Thor⚡️Living Thunder` in full on first mention, covers and title cards. `Living Thunder` alone is fine elsewhere.

**Spots needing the full title:**

| Spot | Current text | Needs |
|---|---|---|
| `README.md` L1 (H1 and first mention) | "Living Thunder — Ra-Thor Comic Series Bible" | Full title |
| `02_SERIES_STRUCTURE.md` L3 | "Working title: **Living Thunder**" | Full title (and note "Working title" wording) |
| `03_TONE_SPECS.md` L3 | "House tone modes for Living Thunder." | Full title on first mention |
| `05_LORE_BIBLE.md` L3 | "Series lore for Living Thunder." | Full title on first mention |
| `06_MUSIC_SPEC.md` L3 | "Score and cues for Living Thunder (comic motion and trailer use, and the show)." | Full title on first mention |
| `bots/ROUTINE.md` L1 | "Living Thunder — forever routine" | Full title on first mention |
| `bots/GROKBOT_COMIC_SEAT.md` L3, L6 | "Grokbot - Living Thunder" | External app display name; leave unless Sherif says otherwise |
| Cover, intro/outro title card, credits | **Do not exist in the repo** | Full title (packaging) |
| Trailer title card, `MAIN TITLES` (S1E01/S1E02 TELEPLAY L50/L55) | PC placeholder | Full title, once a title card is defined |

**Conflicts and open points (flagged, not resolved):**
- `production/README.md` L13 and `seasons/S2_SEASON_SHEET.md` §5 item 8 (PR #27) say the series title is **packaging only**: cover, intro/outro title card and credits, never on a page, panel or prop. The first-mention rule for docs is consistent with that. The two should not be mixed up. No ruling says the docs' first mention must carry the full form; this audit takes it from Sherif's instruction.
- The "⚡️" character needs a font and encoding check for covers and metadata (Amazon and Patreon fields). Not testable in the repo.
- No file defines a cover or title-card layout. Defining one is new canon, so it needs a ruling.

## 7. Outside-IP sweep summary

- **Brands, shows, franchises, characters, studios, creators:** none found in any episode, production, screen or bible file (searched all Markdown). Mentions of xAI, Grok, superhero logos and similar appear only as prohibitions or as the README's independence disclaimer.
- **Captain Obvious:** zero hits. The card "OBVIOUS" (lightbulb) is the series' own device; never extend it.
- **Real persons:** Jacque Fresco, docs and S3 crawl only (ruled). Keep out of all marketing, trailer and cover material.
- **Low-risk phrases to confirm with the council:** "spy-thriller elegance" (genre label in every Suave Hour set add-on), "Homer visual bible" / "Odyssey" (README), "cartoon-lab" (generic).
- **Product-claim risk:** Idea Recycler and White-Hat Mercy-Security must stay fiction (00 rule 5). The frequencies (432/528/543/108/54 Hz) are mood only (06 §4).
- **Third-party tools:** Grok Imagine as an image tool and the Grok app seat. Not for packaging.

## 8. What this audit did not do

- No episode, panel, caption, bubble, prompt, cue or title text was written, and no GAP was filled.
- No rendered asset outside the repo was seen.
- Per-episode open-gap counts for S1–S3 come from `production/S0_GAP_AUDIT.md` (as audited at `a984ec9`) and were not re-counted file by file.
- Grep counts for GAP and PC include mentions of the tags inside explanatory text, so treat them as upper bounds. The marker lines named by file and line are exact.
