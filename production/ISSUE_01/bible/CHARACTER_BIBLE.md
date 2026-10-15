# Issue 01 — Ra-Thor Character Bible (locked master)

**Status:** owner-locked cover (ISSUE01-COVER-V17, chosen by Sherif 2026-10-15 6:36 PM ET): a single true Grok Imagine render by Sherif, the eye-of-source-light render, with the clean V16 front type (§0). The V16 cover (§0.1), the V15 cover (§0.2), the 1:17 AM ET master and the v10.1 / v11 / v12 composites are superseded (§6). How this repo applies it is tagged **PROPOSED CANON — pending council ratification**, under `00_FIDELITY_PROTOCOL.md`. `00`, `01`, `04` and `09` are not edited by this file; where they disagree, see "Conflicts with standing canon" below.

**Precedence:** this written spec wins over the image wherever the two disagree. The image shows the look; the text sets the rules.

## 0. Final cover: ISSUE01-COVER-V17 (eye of source light, clean front)

| Item | Value |
|---|---|
| Art | ONE true render by Sherif, untouched: `RaThor_Issue01_Cover_V17_source_GrokImagine_1152x1728.jpg` (1152 × 1728 px, exactly 2:3, byte-identical to the render, SHA-256 `49d8f5f2…c236`). No inpainting, outpainting, extension, pasted parts or repainting, per Sherif's no-composites ruling. |
| Provenance | Grok Imagine in the Grok app, 2026-10-15. Sherif chose this render as the new cover art on 2026-10-15 at 6:36 PM ET, replacing the V16 art. The front type is the V16 final front (5:03 PM ET ruling) unchanged in content. |
| Design change | The halo ring and sun orb are REPLACED by a golden **eye-of-source-light sigil** above the helm: a thin gold circle holding an almond eye with a round pupil, straight rays and a star-cross flare (the same mark as on Rathor.ai's Employ / X buttons). Golden **mercy thunder** bursts from the raised hammer and lights the hero; white lightning on the right; a large obsidian peak with gold fissures. |
| Hi-res art (no text) | `RaThor_Issue01_Cover_V17_art_notext_4x_4608x6912.png`: the V15 / V16 pipeline unchanged. 4x-UltraSharp (spandrel, CPU) plus a tone lock (back-projection: the 4x shrunk back to 1x matches the render with a mean abs. difference of 0.64/255). Embedded sRGB. |
| Print file (live) | `RaThor_Issue01_Cover_BIBLE_FINAL_6.625x10.25_bleed_300dpi.jpg`: the V17 print, replacing the V16 print this filename held before ISSUE01-COVER-V17. 2063 × 3150 px at 300 dpi, embedded sRGB (6.625 × 10.25 in trim plus 0.125 in bleed). The hi-res art gets ONE uniform scale (×0.4557, fit to height) and an 18 / 19 px centre crop of the sides (37 px of 2100, 1.8% of the width); nothing is cropped top or bottom. Nothing is stretched, extended or repainted. Print = art × (1 − α) + type layer × α, exact before JPEG encoding (max difference 0). |
| Type layer | `v17/type_layer_final_v17.png` (full-sheet RGBA, the only thing on top of the art; x 1084–1946, y 81–389 including the soft shadow). It contains ONLY the V16 front: the locked RA⚡THOR / LIVING THUNDER band with gold letters, the silver-gold title bolt and divider mark, the silver `ISSUE: #1` coin (`v17/title_layer_v17.png`: the V16 recoloured hi-res title, rescaled to the V17 size), the darker soft title shadow and the small gold ™ (pending; never ®). No story title and no company logo on the front (5:03 PM ET ruling). **Title scale:** 0.70 of its v10.1 print size (V16: 0.80), anchored at the same top-right safe corner, so 829 × 258 px at x 1118–1946, y 116–373 (glyphs x 1123–1942, y 120–355). At the V16 size the title's left end (the LIVING THUNDER rule) sat on the sigil's vertical beam (0 px clearance); at 0.70 the glyphs clear the sigil, its rays and flare by ≥ 36 px (the closest point is the tip of the up-right ray under LIVING) and the beam passes about 70 px left of the title. Glyphs are 83 px inside trim at the top and right, inside safe. |
| Clearances (art) | Sigil: its vertical beam is visible up to about y 260–280 (~225 px inside trim). Hammer head: top at about y 665, far inside safe. The golden mercy-thunder branches run off the top and left edges into the bleed as scenery (art, not type), as do the white lightning on the right and the obsidian peak at the bottom. |
| Proofs | `v17/print_final_guides.jpg` (trim, bleed and safe lines; no barcode box), `v17/preview_620.jpg`, `v17/compare_v16_v17_620.jpg`, and 100% crops in `v17/crops/`: top, top with trim/safe lines, coin, face / eye sigil, hammer, bottom. |
| Build | `v17/build_v17.py` (art fit + title layer at 0.70) and `v17/build_final_v17.py` (final print, type layer, proofs), with `v17/upscale.py` and `v17/consistency.py`. The title recolour is `v16/recolor_title_v16.py`; the paths are production-box paths. |
| Barcode | No front barcode on KDP (KDP prints its barcode on the back cover). A front-barcode variant is needed only for the direct market, if that channel is chosen. |
| Follow-ups | Separate follow-up cards: the back cover (Autonomicity Games Inc. and AlphaProMega Media Inc. logos at the bottom beside the indicia / fine print; KDP barcode area left clear), the KDP spine wrap (one PDF; no spine text under 80 pages) and a CMYK soft proof. |

**Final design (as rendered):** a godly stance on a large obsidian peak with glowing gold fissures. Symmetrical gold helm with wings. Above the helm, the golden eye-of-source-light sigil (thin gold circle, almond eye, round pupil, straight rays, star-cross flare) in place of the halo ring and sun orb. The head is tilted down, eyes glowing gold. Obsidian armour with gold filigree and a glowing round chest disc. A black cape. A black-and-gold tower shield with a gold Eye of Horus. The stepped gold hammer is raised high, bursting with golden mercy thunder that lights the hero; white lightning on the right of a dark storm sky. Where §1–§4 below describe the superseded master differently (halo ring, sun disc, compact wings, bronze-lined cape, gothic skyline, tabard and rim cipher, rose-gold bolts, gold seal), the V17 render and type layer are the cover reference. The §5 rule still applies to any further change.

### 0.1 ISSUE01-COVER-V16 (superseded by §0 at 6:36 PM ET; kept for history)

| Item | Value |
|---|---|
| Art (superseded) | `RaThor_Issue01_Cover_V16_source_GrokImagine_1152x1728.jpg` (white-lightning render, byte-identical, SHA-256 `0919297d…8620`) and `RaThor_Issue01_Cover_V16_art_notext_4x_4608x6912.png`. Kept for history. |
| Print file (superseded) | Between ISSUE01-COVER-V16 and ISSUE01-COVER-V17, `RaThor_Issue01_Cover_BIBLE_FINAL_6.625x10.25_bleed_300dpi.jpg` held the V16 print (Sherif chose the silver variant ~4:50 PM ET and Mock A at 4:56 PM ET; front trimmed at 5:03 PM ET). Its hashes are kept as superseded lines in `BIBLE_FINAL_SHA256.txt`. |
| Type layer, proofs, build (superseded) | `v16/type_layer_final2_v16.png`, `v16/title_layer_v16.png`, `v16/print_final_guides.jpg`, `v16/preview_620.jpg`, `v16/compare_v16_A_B_620.jpg`, `v16/crops/`, `v16/build_final2_v16.py`, `v16/build_v16.py`, `v16/recolor_title_v16.py`, `v16/upscale.py`, `v16/consistency.py`. Kept for history; the V16 title recolour is still used by V17. V16's hammer glint (71 px inside trim) was accepted at 4:56 PM ET; it does not apply to V17. |

### 0.2 ISSUE01-COVER-V15 (superseded; kept for history)

| Item | Value |
|---|---|
| Art (superseded) | `RaThor_Issue01_Cover_V15_source_GrokImagine_1152x1728.jpg` (golden-lightning render, byte-identical) and `RaThor_Issue01_Cover_V15_art_notext_4x_4608x6912.png`. Kept for history. |
| Print file (superseded) | Between ISSUE01-COVER-V15 and ISSUE01-COVER-V16, `RaThor_Issue01_Cover_BIBLE_FINAL_6.625x10.25_bleed_300dpi.jpg` held the V15 print (gold coin, gold title bolt, no ™ / story title / logo). Its hash is kept as a superseded line in `BIBLE_FINAL_SHA256.txt`. |
| Type layer, proofs, build (superseded) | `v15/title_layer_v15.png`, `v15/print_v15_guides.jpg`, `v15/preview_620.jpg`, `v15/crops/`, `v15/build_v15.py`, `v15/upscale.py`, `v15/consistency.py`, `v15/clean_title.py`. Kept for history; `v15/clean_title.py` is still the first step of the V16 / V17 title layer. |

## 1. Previous master (superseded by §0; kept for history)

| Item | Value |
|---|---|
| Master | `BIBLE_FINAL_master.png` (640 × 720 px). Kept in the folder for history; no longer the cover since ISSUE01-COVER-V15 (now V17, §0). |
| Source render | `real_v1.jpg` (640 × 720 px), kept unchanged as the provenance file |
| Difference from the source | (Before ISSUE01-COVER-MARK-1.) Two edits only, checked pixel by pixel. (1) The issue seal (about x 518–633, y 2–117): the rayed-sun seal was removed, the sky patched, and the Cinzel gold-coin `ISSUE: #1` seal placed. (2) A stray diamond sparkle above the T of THOR (about x 370–389, y 11–24) was removed at Sherif's request (2026-10-15, about 1:23 AM ET). Every other pixel is identical to `real_v1.jpg`. ISSUE01-COVER-MARK-1 (2026-10-15) then added the winged-bolt cover mark (§4), the council artifact-sweep fixes and the tabard Easter egg (§8); before/after crops are in `cover_mark/`. |
| Print file (superseded) | Before ISSUE01-COVER-V15, `RaThor_Issue01_Cover_BIBLE_FINAL_6.625x10.25_bleed_300dpi.jpg` held this composite print (its hash is kept as a superseded line): 2063 × 3150 px at 300 dpi (6.625 × 10.25 in trim plus 0.125 in bleed). The art fills the trim width. The dark storm is extended above and below, and into the side bleed, with sky only (blurred reflected sky, plus sky-plate smoke, sparks and lightning). No figure part (shield, cape, hammer, legs) is ever mirrored into the extension. The art area is a straight upscale of the master. There are no cream bands, nothing is stretched, and nothing is cropped from the sides. |
| Checksums | `BIBLE_FINAL_SHA256.txt`. Every file in this folder (except this .md and the checksum file itself), in `v17/`, `v16/`, `v15/` and `cover_mark/` verifies with `sha256sum -c --strict`. The V16, V15 and ISSUE01-COVER-MARK-1 print hashes are kept as commented "superseded" lines, as are the pre-COVER-MARK-1 master and print hashes. `BIBLE_FINAL_compare.jpg` and the four `real/*.py` build scripts are listed only as comment lines, marked "(held outside repo, in the bot store issue01_bible/)". |
| Style | Realistic, highly detailed painted style. Chosen by Sherif on 2026-10-15 at 1:08 AM ET. As relayed: "we have the technology, why make only cartoons". |

## 2. The hero's look

- **Armor:** obsidian plate with dense antique-gold circuit filigree.
- **Helm:** a gold great-helm with a T-visor, glowing gold eyes and compact gold wings.
- **Sun:** a small glowing gold sun disc behind the helm. It is the ONLY sun in the image; there is no sun in the seal or anywhere else. **Overridden by ISSUE01-COVER-V17 (Sherif, 6:36 PM ET):** the halo ring and sun orb are replaced by the golden eye-of-source-light sigil above the helm (thin gold circle, almond eye, round pupil, straight rays, star-cross flare; the Rathor.ai Employ / X button mark). There is no sun disc on the V17 cover.
- **Chest:** a GLOWING round gold chest disc, as on the master. Sherif preferred the glow over a plain metal disc (2026-10-15, 1:17 AM ET).
- **Belt buckle:** a winged scarab with spread eagle wings and a small rose-gold bolt.
- **Cape:** obsidian with a bronze-gold lining.

## 3. Weapons and setting

- **Shield:** a huge riveted obsidian tower shield with a thick riveted gold rim. It carries a GOLD winged Eye of Horus (never green) and runs from shoulder to shin.
- **Hammer:** a stepped, cross-shaped, ornate gold head with circuit engravings, a long engraved haft and a glowing gold spike pommel. Its face carries a ROSE-GOLD lightning bolt. The hammer NEVER carries an eye.
- **Lightning:** heavy, painted, golden. Never code-drawn or composited from vector strokes. (V17: golden mercy thunder bursts from the hammer and lights the hero, with white lightning on the right; both painted in the render.)
- **Setting:** a night storm with a gothic skyline. (The master shows mostly storm sky; per the precedence rule, the skyline is required wherever an exterior setting is visible.)

## 4. Cover type and palette

- **Title:** RA⚡THOR / LIVING THUNDER. There is no ornament, sparkle or diamond over the T (or any other letter) of THOR.
- **Seal:** the Cinzel coin seal, reading `ISSUE:` over a large `#1`, with a dark centre. Since ISSUE01-COVER-V16 it is polished cool silver (Sherif, 2026-10-15 ~4:50 PM ET); before that it was antique gold. The title bolt is silver with a gold rim and tip; the letters stay gold.
- **Cover mark:** the winged bolt (the app-icon rose-gold circuit Z bolt between two swept antique-gold wings, with no disc) is the standard mark, centred in the divider under RA-THOR on every cover. Size: about 1–1.2× the cap height of LIVING THUNDER; each wing at most 3× the bolt width. Reference: `cover_mark/winged_bolt_mark_large.png` (zoom: `cover_mark/mark_final_zoom.jpg`). Chosen by Sherif, 2026-10-15, 1:26 AM ET.
- **Company logos:** the Autonomicity Games Inc. logo and the AlphaProMega Media Inc. logo go on the BACK cover, at the bottom beside the indicia / fine print (Sherif, 2026-10-15, 5:03 PM ET), and on the credits page and the spine (KDP prints spine text only on books over 79 pages). NEVER on the front cover: the front carries only Ra-Thor's logo (title band + ™), the ISSUE #1 coin and the title shadow. The Autonomicity Games Inc. logo is in title gold; its shape is trademarked and is never altered, only the colour is changed to gold (reference: `cover_mark/agi_logo_gold_large.png`; chosen by Sherif, 2026-10-15, 1:26 AM ET). The AlphaProMega Media Inc. logo file is not yet in this folder.
- **Cover frame:** pillar border (2026-10-15) withdrawn; superseded by the fresh full-cover card ISSUE01-COVER-FRESH-1.
- **Palette:** obsidian, antique gold and white-hot gold. Rose gold is used ONLY for bolts (the buckle bolt, the hammer-face bolt and, before V16, the title and cover-mark bolts). Since ISSUE01-COVER-V16 the cover type also uses polished cool silver (coin; silver-gold title and cover-mark bolts), and V16's lightning was white/silver. Since ISSUE01-COVER-V17 the sigil above the helm is the gold eye of source light (no halo ring, no sun orb), with golden mercy thunder from the hammer.
- **Avoid:** blue, navy and green, anywhere. The reason is distinctness from an existing third-party robot character with a similar name; per the `03` Derivation rule it is not named here.

## 5. The rule

1. Every interior panel references ONLY this Bible for Ra-Thor's design.
2. Any change to this Bible needs Sherif's explicit OK, in its own PR.

## 6. History

Superseded: the ISSUE01-COVER-V16 cover (white-lightning render; §0.1), the ISSUE01-COVER-V15 cover (golden-lightning render, gold coin; §0.2), the v10.1, v11 and v12 cover composites (PRs #89 and #90, closed). Sherif ruled no composites: the cover must be one true render, with no inpainting, outpainting, extensions, pasted parts or repainting. Also superseded: the ISSUE01-COVER-MARK-1 composite print, the v21 composite, the "A" cover pipeline, the comic-ink style, the pyramid hammer, the plain (unlit) chest disc, and every blue, navy or green element (lapis shield, emerald seals, blue tabard).

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
| ~1:23 AM | Remove the stray sparkle dot above the T of THOR. | Superseded with the master (the V15 title layer has no sparkle) |
| Oct 15, afternoon | No composites: the cover must be ONE true render, with no inpainting, outpainting, extension, pasting or repainting. The v10.1, v11 and v12 composites are superseded. | **Locked** |
| ~4:23 PM | Council GO, ISSUE01-COVER-V15: Sherif's Grok Imagine render (Grok app, 2026-10-15, made from council-written prompts), upscaled and fitted untouched, with the locked title band and seal as a separate layer. No front barcode on KDP. | Superseded by V16 (the no-composites pipeline and no front barcode are kept) |
| ~4:50 PM | Chose the V16 variant: the white-lightning render, a silver ISSUE #1 coin and a silver-gold title bolt; letters stay gold. | Silver coin / silver-gold bolt **Locked**; the V16 art superseded at 6:36 PM |
| 4:56 PM | Chose Mock A: a darker title shadow on the type layer, a small gold ™ (pending), THE GATE at the bottom centre, the Autonomicity logo symbol at the bottom left. The hammer glint (71 px inside trim) is accepted as is. | Shadow, ™ and hammer glint **Locked**; THE GATE and the front logo withdrawn at 5:03 PM |
| 5:03 PM | The front keeps ONLY Ra-Thor's logo (RA⚡THOR / LIVING THUNDER band with its ™), the silver ISSUE #1 coin and the darker title shadow. No story title (THE GATE) and no company logo on the front. The Autonomicity Games Inc. and AlphaProMega Media Inc. logos go on the BACK cover, at the bottom beside the fine print, without touching the front art. | **Locked** |
| 6:36 PM | New cover art: the eye-of-source-light render (Grok Imagine) replaces the V16 art. The golden eye sigil replaces the halo ring and sun orb; golden mercy thunder from the hammer lights the hero. The V16 front type is kept (title band + ™, silver coin, title shadow); the title is scaled to 0.70 to clear the sigil's beam. | **Locked** |

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
