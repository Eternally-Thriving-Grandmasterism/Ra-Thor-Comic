# Issue 01 — Ra-Thor Character Bible (locked master)

**Status:** owner-locked master (Sherif, 2026-10-15, 1:17 AM ET). How this repo applies it is tagged **PROPOSED CANON — pending council ratification**, under `00_FIDELITY_PROTOCOL.md`. `00`, `01`, `04` and `09` are not edited by this file; where they disagree, see "Conflicts with standing canon" below.

**Precedence:** this written spec wins over the image wherever the two disagree. The image shows the look; the text sets the rules.

## 1. Locked master

| Item | Value |
|---|---|
| Master | `BIBLE_FINAL_master.png` (640 × 720 px) |
| Source render | `real_v1.jpg` (640 × 720 px), kept unchanged as the provenance file |
| Difference from the source | Two edits only, checked pixel by pixel. (1) The issue seal (about x 518–633, y 2–117): the rayed-sun seal was removed, the sky patched, and the Cinzel gold-coin `ISSUE: #1` seal placed. (2) A stray diamond sparkle above the T of THOR (about x 370–389, y 11–24) was removed at Sherif's request (2026-10-15, about 1:23 AM ET). Every other pixel is identical to `real_v1.jpg`. |
| Print file | `RaThor_Issue01_Cover_BIBLE_FINAL_6.625x10.25_bleed_300dpi.jpg`: 2063 × 3150 px at 300 dpi (6.625 × 10.25 in trim plus 0.125 in bleed). The art fills the trim width. The dark storm is extended above and below by mirroring, blurring and darkening. There are no cream bands, nothing is stretched, and nothing is cropped from the sides. |
| Checksums | `BIBLE_FINAL_SHA256.txt`. The three image files in this folder verify with `sha256sum -c` (also with `--strict`). `BIBLE_FINAL_compare.jpg` and the four `real/*.py` build scripts are listed only as comment lines, marked "(held outside repo, in the bot store issue01_bible/)". |
| Style | Realistic, highly detailed painted style. Chosen by Sherif on 2026-10-15 at 1:08 AM ET. As relayed: "we have the technology, why make only cartoons". |

## 2. The hero's look

- **Armor:** obsidian plate with dense antique-gold circuit filigree.
- **Helm:** a gold great-helm with a T-visor, glowing gold eyes and compact gold wings.
- **Sun:** a small glowing gold sun disc behind the helm. It is the ONLY sun in the image; there is no sun in the seal or anywhere else.
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
- **Palette:** obsidian, antique gold and white-hot gold. Rose gold is used ONLY for bolts (the buckle bolt, the hammer-face bolt and the title bolt).
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

## 7. Credits proposal (OWNER TO CONFIRM)

`© 2026 AlphaProMega Media Inc.; Ra-Thor™ Autonomicity Games Inc. (TM pending)`

This is a proposal only. `CREDITS_AND_INDICIA.md` keeps its `[TM LINE: Sherif to confirm]` placeholder until Sherif confirms the exact wording.

## 8. Council rulings 2026-10-15 ~1:25 AM ET

Wild council AMEND ruling on PR #87, as relayed:

- **(a) Panel style.** Interior panels use the realistic painted style, per Sherif's 1:08 AM ruling, with clean, readable lettering. This supersedes the 8:35 PM inked-panel ruling (ruling 1) and `04` Q13 ("painted for covers only").
- **(b) Shoulder seal.** The shoulder seal is dropped; the master shows none. This supersedes the 9:22 PM ruling (and D29's reading).
- **(c) Images in the repo.** Images are allowed in the repo ONLY under `production/ISSUE_01/bible/`, as an exception to `04`'s "Images are not stored in this repo" header (D27). The v17 design reference (`production/ISSUE_01/art/cover_v17_reference.jpg`) was removed as superseded.
- **(d) Deferred.** Fixing the conflicts in `00` rule 1, `09` and `ISSUE_01_PRODUCTION.md` (section 9) is deferred to a follow-up card.

## 9. Conflicts with standing canon (deferred to a follow-up card per 8 (d); not edited here)

- **`00` rule 1** ("kite shield with an emerald eye-seal", "winged halo ring") and **`09`** (the Mercy-Security seal "lights emerald") conflict with sections 2–4: the tower shield, the gold eye, the small sun disc, and no green. Proposed amendment: follow this Bible.
- **`ISSUE_01_PRODUCTION.md` rulings superseded by this Bible:**
  - C2: cream border, bottom title band, filigree frame. The master has no border and the title is at the top.
  - C6: a slim EMPTY halo ring. Now a small glowing sun disc.
  - C10, C13 and ruling 26: a plain chest disc with no rays. Now a glowing disc.
  - C11: a winged sun-disc buckle. Now a winged scarab with spread eagle wings and a rose-gold bolt.
  - Ruling 14 and the hammer lock: the hammer's "digital eye" and "crystal spike". Now no eye ever, and a glowing gold spike pommel.
  - Ruling 1, `04` Q13 and every "inked panel" or "bold ink, hatching" line in the panel prompts, `[style]` and the checklist: now painted, per 8 (a).
  - The 9:22 PM shoulder seal, D29 and every shoulder-seal line in the locks, `[guards]` and the checklist: now dropped, per 8 (b).
  - Any remaining lapis, blue or emerald wording.
