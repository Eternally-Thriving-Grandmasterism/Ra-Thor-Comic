# Issue 01 — Ra-Thor Character Bible (locked master)

**Status:** owner-locked master (Sherif, 2026-10-15, 1:17 AM ET). How this repo applies it is tagged **PROPOSED CANON — pending council ratification**, under `00_FIDELITY_PROTOCOL.md`. `00`, `01`, `04` and `09` are not edited by this file; where they disagree, see "Conflicts with standing canon" below.

**Precedence:** this written spec wins over the image wherever the two disagree. The image shows the look; the text sets the rules.

## 1. Locked master

| Item | Value |
|---|---|
| Master | `BIBLE_FINAL_master.png` (640 × 720 px), the v10.1 titled master (ISSUE01-COVER-V10-1, Sherif's v10 lock 2026-10-15 4:31 AM ET) |
| Hi-res master | `BIBLE_FINAL_master_hires.png` (2560 × 2880 px): a 4× AI upscale (4x-UltraSharp) of the v10.1 art, tone-locked back to the 640 × 720 master (its downscale matches the master; 100% crops in `wings_v10/hires_check_100pct.jpg`) |
| Source render | `real_v1.jpg` (640 × 720 px), a Grok Imagine generation by Sherif, kept unchanged as the provenance file. Commercial-use terms for the generation are to be confirmed under Sherif's account. |
| Later edits | Done in code, not by re-generation: compositing of generated wing, ring and bleed plates (graded, masked and mirror-fitted onto the master), and a 4x-UltraSharp AI upscale with a tone lock for the hi-res master. |
| Colour | sRGB-embedded RGB in every file. Convert to CMYK (GRACoL2013 or FOGRA39, per the printer) only after the printer is picked; soft-proof the golds; total ink ≤ 300%. |
| Difference from the source | (Before ISSUE01-COVER-MARK-1.) Two edits only, checked pixel by pixel. (1) The issue seal (about x 518–633, y 2–117): the rayed-sun seal was removed, the sky patched, and the Cinzel gold-coin `ISSUE: #1` seal placed. (2) A stray diamond sparkle above the T of THOR (about x 370–389, y 11–24) was removed at Sherif's request (2026-10-15, about 1:23 AM ET). Every other pixel is identical to `real_v1.jpg`. ISSUE01-COVER-MARK-1 (2026-10-15) then added the winged-bolt cover mark (§4), the council artifact-sweep fixes and the tabard Easter egg (§8); before/after crops are in `cover_mark/`. ISSUE01-COVER-V10-1 (2026-10-15) then replaced the helm wings with forged antique-gold plate wings (the original upswept shape and placement, mirror-symmetric), framed the sun disc with a thick engraved antique-gold ring, rolled the wing highlights off (council nit), and scaled the title band 0.965 so all type and the seal sit inside the 0.25 in safe area; before/after in `wings_v10/`. |
| Print file | `RaThor_Issue01_Cover_BIBLE_FINAL_6.625x10.25_bleed_300dpi.jpg`: 2063 × 3150 px at 300 dpi (6.625 × 10.25 in trim plus 0.125 in bleed), sRGB. ISSUE01-COVER-V12 replaces the v10.1 bleed bands. The locked hi-res figure, title and seal are resampled to the trim width (1988 px) and shifted up; they are not stretched. Ra-Thor stands full length: boots planted on cracked black obsidian with glowing gold cracks, ground and embers running to the sheet edges. The sky above the master and in the side bleed is continued from the master's own sky (no separate darkened band, no mirrored figure). Lightning is held off the trim. A 525 × 300 px barcode box is reserved at the bottom-left of the safe area (guides only; it may overlap a boot). Guides: `v12/print_v12_guides.jpg`. Before/after against v10.1: `v12/before_after_v10_1_v12.jpg`. 100% crops: `v12/crops/`. The v10.1 print is kept at `v12/v10_1_print.jpg` for that comparison. |
| Checksums | `BIBLE_FINAL_SHA256.txt`. Every image file in this folder, in `cover_mark/`, in `wings_v10/` and in `v12/` verifies with `sha256sum -c --strict`; earlier master and print hashes are kept as commented "superseded" lines. The v12 build scripts live in `v12/` (`build_cover_v12.py`, `make_sheets.py`, `srgb.py`) and are listed in the checksum file. `BIBLE_FINAL_compare.jpg`, the four `real/*.py` build scripts and the `v10_1/` build scripts stay comment lines, marked "(held outside repo, in the bot store issue01_bible/)". |
| Style | Realistic, highly detailed painted style. Chosen by Sherif on 2026-10-15 at 1:08 AM ET. As relayed: "we have the technology, why make only cartoons". |

## 2. The hero's look

- **Armor:** obsidian plate with dense antique-gold circuit filigree.
- **Helm:** a gold great-helm with a T-visor, glowing gold eyes and forged antique-gold plate wings, mirror-symmetric, upswept.
- **Sun and ring:** a thick engraved antique-gold ring (no spike, no light-halo) framing the single sun disc behind the helm. The glowing gold disc is the ONLY sun in the image; there is no sun in the seal or anywhere else. The ring is never a second sun and never holds an eye.
- **Chest:** a GLOWING round gold chest disc, as on the master. Sherif preferred the glow over a plain metal disc (2026-10-15, 1:17 AM ET).
- **Belt buckle:** a winged scarab with spread eagle wings and a small rose-gold bolt.
- **Cape:** obsidian with a bronze-gold lining.

## 3. Weapons and setting

- **Shield:** a huge riveted obsidian tower shield with a thick riveted gold rim. It carries a GOLD winged Eye of Horus (never green) and runs from shoulder to shin.
- **Hammer:** a stepped, cross-shaped, ornate gold head with circuit engravings, a long engraved haft and a glowing gold spike pommel. Its face carries a ROSE-GOLD lightning bolt. The hammer NEVER carries an eye.
- **Lightning:** heavy, painted, golden. Never code-drawn or composited from vector strokes.
- **Setting:** a night storm with a gothic skyline. (The master shows mostly storm sky; per the precedence rule, the skyline is required wherever an exterior setting is visible.)

## 4. Cover type and palette

- **Title:** RA⚡THOR / LIVING THUNDER. There is no ornament, sparkle or diamond over the T (or any other letter) of THOR.
- **Seal:** the Cinzel gold-coin seal, reading `ISSUE:` over a large `#1`. It has a dark centre and an antique-gold ring, and its gold matches the title's metal.
- **Cover mark:** the winged bolt (the app-icon rose-gold circuit Z bolt between two swept antique-gold wings, with no disc) is the standard mark, centred in the divider under RA-THOR on every cover. Size: about 1–1.2× the cap height of LIVING THUNDER; each wing at most 3× the bolt width. Reference: `cover_mark/winged_bolt_mark_large.png` (zoom: `cover_mark/mark_final_zoom.jpg`). Chosen by Sherif, 2026-10-15, 1:26 AM ET.
- **Publisher logo:** the Autonomicity Games Inc. (AGi) logo goes on the spine and the credits page ONLY (never on the front cover), in title gold. Its shape is trademarked and is never altered; only the colour is changed to gold. Reference: `cover_mark/agi_logo_gold_large.png`. Chosen by Sherif, 2026-10-15, 1:26 AM ET.
- **Cover frame:** pillar border (2026-10-15) withdrawn. The fresh full-cover card ISSUE01-COVER-FRESH-1 is itself superseded by Sherif's v10 lock (2026-10-15, 4:31 AM ET): the cover is the v10.1 master, with no frame.
- **Print and safe area:** the print has painted storm extensions (§1). The title band is scaled 0.965 so all type and the seal sit at least 0.25 in inside the trim.
- **Barcode:** an empty box about 1.75 × 1.0 in is reserved at the bottom-left, inside the safe area, for when the distributor is known. Never place a fake UPC.
- **Credits line:** waits on Sherif (§7).
- **Marks:** use ™ for the pending mark, never ®.
- **Palette:** obsidian, antique gold and white-hot gold. Rose gold is used ONLY for bolts (the buckle bolt, the hammer-face bolt, the title bolt and the cover-mark bolt).
- **Avoid:** blue, navy and green, anywhere. The reason is distinctness from an existing third-party robot character with a similar name; per the `03` Derivation rule it is not named here.

## 5. The rule

1. Every interior panel references ONLY this Bible for Ra-Thor's design.
2. Any change to this Bible needs Sherif's explicit OK, in its own PR.

## 6. History

Superseded: the v21 composite, the "A" cover pipeline, the comic-ink style, the pyramid hammer, the plain (unlit) chest disc, and every blue, navy or green element (lapis shield, emerald seals, blue tabard).

Sherif's rulings on 2026-10-14/15. Times are ET. Times marked ~ are reconstructed from file times on the production box; the rest are as relayed.

| Time (ET) | Ruling (as relayed) | Status |
|---|---|---|
| Oct 14, 11:15 PM | Build the Bible from the v21 cover: arm and hammer from v22, scarab buckle, solid sun-disc halo; a code composite, with no AI generator. | Superseded |
| Oct 15, 12:42 AM | Picked the GOLD-chest variant of the v21 composite (BIBLE v1) over the obsidian chest boss. | Superseded |
| ~12:45 AM | The hammer must be BIG and THUNDEROUS. | Superseded (size intent kept) |
| ~12:50 AM | Rejected BIBLE v1: code-drawn lightning looks amateur. Asked for a one-pass redraw. | Rule kept: lightning is never code-drawn |
| ~12:55 AM | Picked comic-ink "try 1" as the base, with the stepped, cross-shaped gold hammer swapped in (v3). | Comic-ink superseded; the hammer design is kept |
| 1:08 AM | Switched to a realistic painted style; `real_v1` is the best render. | **Locked** |
| ~1:09 AM | Asked for three edits on `real_v1`: a plain chest disc, a big sun disc and a new seal (REAL v2). | Plain chest and big sun withdrawn at 1:17 AM; the seal kept |
| 1:17 AM | Final Bible: `real_v1` exactly as is, plus the Cinzel `ISSUE: #1` seal. The glowing chest disc is preferred. | **Locked** |
| ~1:23 AM | Remove the stray sparkle dot above the T of THOR. | **Locked** (in the master) |
| 4:24 AM | "Try the old wings being metallic golden like these new ones" (v10: original upswept wings, forged finish). | Applied |
| 4:31 AM | "Seems best, lock this in for now, and have the Councils review..." (v10 lock; supersedes ISSUE01-COVER-FRESH-1). | **Locked** |
| 4:34 AM | "Yes. Execute properly all" (v10.1 prep: highlight nit, hi-res, safe-area title, sRGB, painted bleed). | Applied in ISSUE01-COVER-V10-1 |
| Oct 15, v12 | Full-length cover, one plate: boots on cracked obsidian, sky continued to the edges, locked figure / title / seal from the v10.1 hi-res master. The separate top band, knee-cut fog strip and side rectangles are withdrawn. | Applied in ISSUE01-COVER-V12 |

## 7. Credits proposal (OWNER TO CONFIRM)

`© 2026 AlphaProMega Media Inc.; Ra-Thor™ Autonomicity Games Inc. (TM pending)`

This is a proposal only. `CREDITS_AND_INDICIA.md` keeps its `[TM LINE: Sherif to confirm]` placeholder until Sherif confirms the exact wording.

## 8. Council rulings 2026-10-15 ~1:25 AM ET

Wild council AMEND ruling on PR #87, as relayed:

- **(a) Panel style.** Interior panels use the realistic painted style, per Sherif's 1:08 AM ruling, with clean, readable lettering. This supersedes the 8:35 PM inked-panel ruling (ruling 1) and `04` Q13 ("painted for covers only").
- **(b) Shoulder seal.** The shoulder seal is dropped; the master shows none. This supersedes the 9:22 PM ruling (and D29's reading).
- **(c) Images in the repo.** Images are allowed in the repo ONLY under `production/ISSUE_01/bible/`, as an exception to `04`'s "Images are not stored in this repo" header (D27). The v17 design reference (`production/ISSUE_01/art/cover_v17_reference.jpg`) was removed as superseded.
- **(d) Deferred.** Fixing the conflicts in `00` rule 1, `09` and `ISSUE_01_PRODUCTION.md` (section 9) is deferred to a follow-up card.

### Artifact-sweep rulings (council, applied in ISSUE01-COVER-MARK-1)

Before/after crops at 4×: `cover_mark/before_after_1.jpg` … `before_after_6.jpg`; whole-cover comparison: `cover_mark/cleanup_compare.jpg`.

- **Shield face:** clean. The gold Eye of Horus is its ONLY symbol. The trident spike and the glyph ladder are removed (`before_after_2`).
- **Belt band:** shows plain lattice, with no symbols (`before_after_4`).
- **Scarab:** carries a small rose-gold bolt (`before_after_5`).
- **Hammer face:** its bolt is rose gold (`before_after_6`).
- **Shield rim and tabard:** see the Easter egg below (`before_after_1`, `before_after_3`).

### Easter egg: tabard and shield-rim cipher

- **Tabard:** 8 icons: sun, Z-bolt, hex lattice node, stepped hammer, bar, wheat, open palm, sprout. Plus runes spelling **RATHOR**, with card-suit filler (hearts, diamonds, spades, clubs). All in lustrous gold, bending with the folds of the cloth. TOLC was dropped at this size (tabard v5, Sherif "Excellent!", 2026-10-15, 2:10 AM ET).
- **Shield rim:** reads **[bolt] P O W R U S H [bolt]** in the same cipher.
- **Decoder key:** `cover_mark/runes_key.png`. It is an invented angular rune alphabet in which every rune shares a centre stave. Its glyphs map, left to right, to R, A, T, H, O, L, C, P, W, U, S, and "." is the separator. The key lives in this Bible ONLY. It is never printed on the cover.
- **Off-limits on the tabard, rim and belt:** the Eye of Horus (it appears on the shield face only), logos, readable Latin text, ™ or ® marks, and blue, navy or green.

## 9. Conflicts with standing canon (deferred to a follow-up card per 8 (d); not edited here)

- **`00` rule 1** ("kite shield with an emerald eye-seal", "winged halo ring") and **`09`** (the Mercy-Security seal "lights emerald") conflict with sections 2–4: the tower shield, the gold eye, the sun disc in its engraved gold ring, and no green. Proposed amendment: follow this Bible.
- **`ISSUE_01_PRODUCTION.md` rulings superseded by this Bible:**
  - C2: cream border, bottom title band, filigree frame. The master has no border and the title is at the top.
  - C6: a slim EMPTY halo ring. Now a thick engraved antique-gold ring framing the single glowing sun disc.
  - C10, C13 and ruling 26: a plain chest disc with no rays. Now a glowing disc.
  - C11: a winged sun-disc buckle. Now a winged scarab with spread eagle wings and a rose-gold bolt.
  - Ruling 14 and the hammer lock: the hammer's "digital eye" and "crystal spike". Now no eye ever, and a glowing gold spike pommel.
  - Ruling 1, `04` Q13 and every "inked panel" or "bold ink, hatching" line in the panel prompts, `[style]` and the checklist: now painted, per 8 (a).
  - The 9:22 PM shoulder seal, D29 and every shoulder-seal line in the locks, `[guards]` and the checklist: now dropped, per 8 (b).
  - Any remaining lapis, blue or emerald wording.
