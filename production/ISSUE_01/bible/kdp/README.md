# Issue 1 KDP paperback wraparound cover (ISSUE01-KDP-WRAP-1)

Docs, specs and proof assets only. Nothing here buys, registers or publishes anything, and nothing touches a KDP account.
The front (#91) and back (#92) cover files are inputs and are not changed.

## Council rulings (Wild, 2026-10-15 11:01 PM ET), as relayed

1. **Page count:** keep the story length as written and bring the interior to 24 pages (or the next even count up to about 32) with front and back matter (title/credits page, Bible extras, back-matter art). Never pad to 80. Below 80 pages the spine is blank. Use the resulting count for the spine width and document how it was reached (or the range if the extras aren't final).
2. **Paper:** white paper with Premium Color ink. Trim 6.625 x 10.25 in, bleed on.
3. **Spine:** blank, no text; carry the cover background colour across it. Keep a separate text-ready spine layer in the source for a future collected edition over 79 pages.
4. **Colour:** the RGB masters are the source of truth. Soft-proof against GRACoL 2013 (CRPC6), not FOGRA39. The upload is a flattened RGB PDF. If the proof shows rose-gold or obsidian shifting badly, also make a GRACoL CMYK PDF as a flagged fallback variant (don't swap it in). One printed author proof must be ordered before sale.
5. **Scope:** the paperback wraparound is the first target. Kindle/ComiXology is named as a second card. **UNVERIFIED:** this repo has not confirmed that ComiXology is now part of KDP, or that a fixed-layout comic built with Kindle Create is that route. Keep the barcode zone clear. Keep the ⚡ off KDP metadata fields. The ISBN is an open decision for Sherif (below).

## Spec used: 24 pages, white paper, Premium Color ink

| Item | Value | Source (checked 2026-10-15 ET) |
|---|---|---|
| Trim | 6.625 x 10.25 in (custom trim; "large" trim because width > 6.12 in and height > 9 in) | KDP trim-size help, https://kdp.amazon.com/en_US/help/topic/G201834180: custom paperback width 4–8.5 in, height 6–11.69 in |
| Paper / ink | White paper, Premium Color ink (KDP: 60–71 lb / 88–105 GSM white) | same page |
| Minimum pages | 24 for Premium Color (72 for Standard Color, which is why Standard Color is not used) | same page (table) |
| Bleed | 0.125 in on top, bottom and outside edges | KDP "Create a Paperback Cover", https://kdp.amazon.com/en_US/help/topic/G201953020 |
| Spine formula | pages x 0.002347 in (Premium Color) | G201953020 |
| Spine at 24 pages | **0.056328 in (1.431 mm)**; 17 px at 300 dpi | computed |
| Full cover | Bleed + back 6.625 + spine + front 6.625 + bleed = **13.556328 x 10.5 in (344.331 x 266.7 mm)**; 4067 x 3150 px at 300 dpi | G201953020 formula |
| Spine text | None. KDP prints spine text only on books with more than 79 pages | G201953020 |
| Fold variance | 0.0625 in either side of each fold (shown orange on the guides) | G201953020 |
| Barcode | Zone 2.0 x 1.2 in, bottom 0.25 in above the bottom trim, right edge 0.25 in left of the spine (LTR). Left empty for KDP to place; the build asserts no type there | KDP Print Publishing Guidelines PDF, https://images-na.ssl-images-amazon.com/images/G/01/00/01/00/02/17/60/10002176030.pdf; KDP "Barcodes", https://kdp.amazon.com/en_US/help/topic/G5HDYGP4BXLX4RUW |
| File | One PDF, back + spine + front as one image; 40 MB or less recommended, 650 MB hard limit; no colour profiles (KDP strips them) | G201953020 |

Range if the extras change (all blank spine):

| Pages | Spine (in) | Full cover width (in) | px at 300 dpi |
|---|---|---|---|
| 24 | 0.056328 | 13.556328 | 4067 |
| 26 | 0.061022 | 13.561022 | 4068 |
| 28 | 0.065716 | 13.565716 | 4070 |
| 30 | 0.070410 | 13.570410 | 4071 |
| 32 | 0.075104 | 13.575104 | 4073 |

The difference between 24 and 32 pages is 0.019 in (6 px). Rebuild with `--pages N` once the extras are final.

### Differences between the KDP pages and our earlier notes (flagged)

- **Cover calculator must be run before upload.** KDP's cover calculator and template generator (linked from G201953020) is an interactive form. This card used the published formula on the same page. That formula does not override the calculator. Before any upload, enter 6.625 x 10.25, Premium Color, white, and the final page count into the calculator. If its size differs from 13.556328 x 10.5 in, the calculator wins: rebuild the wrap to the calculator's number.
- **Spine text threshold wording is inconsistent on G201953020.** The page says "more than 79 pages" in one place, "at least 79 pages" in two others, and 80 pages for Cover Creator. It doesn't matter for a 24-page book (blank spine), but a future collected edition should use 80 or more to be safe.
- **Colour space.** G201953020 says "Images should be in CMYK color to ensure your cover looks good in print", and also says not to mix colour spaces and that profiles are removed. The council ruling makes the upload a flattened RGB PDF. KDP does accept RGB, but its own page recommends CMYK. This is one more reason the CMYK fallback below exists. The author proof decides.
- **Text safe distance.** G201953020 now says cover text must be at least 0.125 in inside the trim. The guides draw a stricter 0.25 in safe line (cyan). The named threshold is `ALPHA_THRESHOLD = 0.03` in `production/ISSUE_01/check_costume_lock.py`: a type pixel counts only when its alpha is strictly greater than 0.03 (3% of 255). The true trim is 0.125 in × 300 dpi = 37.5 px, not the 37 px bleed constant in the sheet builders. Measured that way, the back type is at least 0.262 in inside the trim. The front type was 0.158 in from the top trim (alpha > 0.03 started at y=84; (84−37.5)/300 = 0.155 in; an earlier note used integer trim y=37 and recorded 0.157 in). ISSUE01-BIBLE-LOCK-KDP-FIX-1 shifted the front type down 28 px, then one more px on 2026-10-16 after Clerk measured 74.5 px (0.248 in): ymin 112 − 37.5 = 74.5. The title band and the ISSUE #1 badge now start at y=113. Clearance is (113−37.5)/300 = **75.5 px (0.2517 in)** inside the top trim. Side and bottom clearance stay inside the 0.25 in line (type bbox x 1086–1946, y 113–416 on the 2063×3150 sheet). Pixels at or below alpha 0.03 are the soft shadow and are not counted; the strongest of those above y=113 is alpha 0.027.
- **Own barcode.** If we ever supply our own barcode, it must not be flattened into the cover image (Barcodes help). We don't supply one: KDP places it.
- **`ISSUE_01_PRODUCTION.md` §10** keeps the comic-shop plan (8 story pages plus a 4-page cover wrap, 12 total, saddle-stitched) as history. The current KDP plan there is a perfect-bound 24-page paperback. The story stays 8 pages.

## How 24 pages was reached (PROPOSED: the extras are not final)

The story is unchanged: 8 story pages (`ISSUE_01_PRODUCTION.md` §4). The title page, the copyright page and the credits page make 11. Pages 12–24 are 13 proposed extras drawn from Bible material already in the repo. No new story pages, and no padding to 80.

| Interior page | Content | Status |
|---|---|---|
| 1 (right) | Title page (§5.2; indicia per `CREDITS_AND_INDICIA.md` §3) | exists in the plan |
| 2 (left) | Copyright / indicia page | to make |
| 3–10 | Story pages 1–8. Page 1 lands on a right-hand page, so the 4–5 spread faces correctly (4 on the left, 5 on the right) | exists in the plan |
| 11 | Credits (§5.3 / `CREDITS_AND_INDICIA.md` §2) | exists in the plan |
| 12 | Character page: armor, helm, chest sun disc with radiating rays, rose-gold lightning-bolt buckle, cape (`CHARACTER_BIBLE.md` §2; `09_CHARACTER_BIBLE.md` canon locks) | proposed |
| 13 | Shield page: the tall v21 shape, central Vegvísir, decorative gold runes, no Eye of Horus on the shield (`CHARACTER_BIBLE.md` §3). The rune fill is not yet painted on the merged cover | proposed |
| 14 | Hammer and lightning as painted on the approved cover (`CHARACTER_BIBLE.md` §3). Lightning-bolt motif on at least both faces of the head. No Eye of Horus on the hammer (Sherif, 2026-10-16, 4:08 AM) | proposed |
| 15 | Cover evolution: V15 (`RaThor_Issue01_Cover_V15_source_GrokImagine_1152x1728.jpg`) | proposed |
| 16 | Cover evolution: V16 | proposed |
| 17 | Cover evolution: V17 | proposed |
| 18 | Approved cover: V18 | proposed |
| 19 | Back-cover art (`RaThor_Issue01_BackCover_v2_6.625x10.25_bleed_300dpi.jpg`) | proposed |
| 20 | The TOLC: gold lattice arch, `LEFT IS NOISE.` / `RIGHT IS LIVE.`, and the canon line (`09_CHARACTER_BIBLE.md`, The TOLC). No count of the mercy checks | proposed |
| 21 | Presence & Protective Power, short (`09_CHARACTER_BIBLE.md`) | proposed |
| 22 | Realms & Rathor.ai, short (`09_CHARACTER_BIBLE.md`) | proposed |
| 23 | Idea Recycler (`09_CHARACTER_BIBLE.md`) | proposed |
| 24 | Palette one-sheet: obsidian, antique gold, white-hot gold; no blue. Green only as the emerald pauldron seal (`CHARACTER_BIBLE.md` §4) | proposed |

If the extras grow, go up in steps of 2 pages to about 32 and rebuild. The spine stays blank throughout.

## Spine

Blank. The 17 px spine is filled with a smooth per-row blend of the back's and the front's facing edge colours (obsidian/black), with no text and no new art. `*_spine_text_layer.png` is the separate, text-ready spine layer. It is empty for this build. `build_wrap.py --spine-text "..."` renders it, but refuses to run below 80 pages. (A test at 150 pages rendered fine; the test output is not committed.)

## Colour: GRACoL 2013 (CRPC6) soft proof

Profile: `icc/GRACoL2013_CRPC6.icc` from the ICC Profile Registry (https://www.color.org/registry/GRACoL2013_CRPC6.xalter; Idealliance, X-Rite copyright; "may be used, embedded, exchanged and shared without restriction", stored unaltered). TAC 320%, Medium+ GCR, CGATS.21-2 CRPC6. Engine: Little CMS via Pillow ImageCms; sRGB → CMYK, relative colorimetric with black-point compensation.

Findings (`out/softproof_GRACoL2013_CRPC6_relative.json`):

| Area | Share of cover | Out of gamut (dE76 > 10, display-matched) | Shift with black ink simulated |
|---|---|---|---|
| Rose-gold / copper | 0.08% | 0% (p95 dE 1.3) | chroma p95 dE 8.6, max 12.3; L* +2.0 |
| Gold / amber | 3.0% | 0% (p95 dE 1.7) | chroma p95 dE 8.6, max 11.7; L* +1.2 |
| Blue / white-blue lightning | 0.04% | 0% (p95 dE 0.6) | negligible (p95 dE 0.7) |
| **Obsidian / near-black** | **89.9%** | 0% (p95 dE 1.2) | **L* +10.0 on average**: the blacks print lifted and greyer, and shadow detail compresses |
| Max TAC | | 318% (CRPC6 limit 320%) | |

Read: no colour on the cover falls outside the CRPC6 gamut. Rose-gold and gold lose some saturation on paper (moderate). The obsidian, about 90% of the cover, lifts by about 10 L* once real black ink on white paper is simulated. Under ruling 4 that counts as shifting badly, so the flagged fallback was made:

- `out/RaThor_Issue01_KDPwrap_24p_premium-color_FALLBACK_CMYK_GRACoL2013_CRPC6.pdf`: **the file for the first printed author proof.** DeviceCMYK, GRACoL 2013 (CRPC6), relative colorimetric + BPC, no ICC embedded, same size. It does not fix the paper-black limit; it only fixes the black build (CRPC6 GCR). **The RGB PDF stays the master.** Do not swap the CMYK file in as the master.
- Ordering that author proof is a KDP account action, so it is for Sherif, not this card.

## Files (`bible/kdp/`)

| File | What |
|---|---|
| `build_wrap.py` | Parametric wrap builder (`--pages`, `--paper`, `--spine-text` for 80+ pages only). Checks that the layers rebuild the committed front and back prints, that there is no type on the spine and no type in the barcode zone |
| `softproof.py` | CMYK soft proof plus gamut flags (CRPC6 by default) |
| `cmyk_fallback.py` | Flagged CMYK fallback PDF |
| `icc/GRACoL2013_CRPC6.icc` | Proof profile (unaltered) |
| `out/RaThor_Issue01_KDPwrap_24p_premium-color.pdf` | **The KDP upload candidate**: flattened RGB, 976.056 x 756 pt (13.556328 x 10.5 in), JPEG q95, no ICC, no marks |
| `out/..._24p_premium-color.jpg` | The same image as the PDF (sRGB tagged) |
| `out/..._type_layer.png` / `..._spine_text_layer.png` | Separate type layers (the type meets the art only in the export) |
| `out/..._guides.jpg`, `..._guides_620.jpg` | Preview only: trim (red), folds (yellow), fold variance (orange), 0.25 in safe (cyan), barcode zone (magenta) |
| `out/softproof_GRACoL2013_CRPC6_relative_side_by_side.jpg`, `_crops.jpg`, `.json` | Soft proof: original, proof (BPC), black-ink simulation, flags; 100% crops of the title, sigil and lightning |
| `out/spec_24p_premium-color.json` | Numbers above, machine-readable |

Rebuild from this folder:

```
python3 build_wrap.py --pages 24 --paper premium-color
python3 softproof.py out/RaThor_Issue01_KDPwrap_24p_premium-color.jpg
python3 cmyk_fallback.py out/RaThor_Issue01_KDPwrap_24p_premium-color.jpg out/RaThor_Issue01_KDPwrap_24p_premium-color_FALLBACK_CMYK_GRACoL2013_CRPC6.pdf --w-in 13.556328 --h-in 10.5
```

## Open decisions (Sherif / councils)

- **ISBN (Sherif).** A KDP paperback needs an ISBN. (a) A free KDP ISBN: the imprint shows as "Independently published", and it can only be used on KDP (KDP "Get an ISBN", https://kdp.amazon.com/en_US/help/topic/GTJ8LBXL6Z4WV5QX; "What is an ISBN and Imprint?", https://kdp.amazon.com/en_US/help/topic/G201834170). (b) AlphaProMega Media Inc.'s own ISBN, so the book shows that imprint: free for eligible Canadian publishers from ISBN Canada (Library and Archives Canada, https://www.canada.ca/en/library-archives/services/publishers/isbn.html). Eligibility for a company: main place of business in Canada and at least 75% of employees in Canada. New accounts currently take up to about 2 months. Each format needs its own ISBN. Nothing has been applied for.
- **Final interior extras** (pages 12–24 above) and the final count (24–32). The 13-page list is a proposal.
- **Author proof** before sale (KDP account action). The first proof uses the GRACoL CMYK PDF. The RGB PDF stays the master.
- **⚡ off KDP metadata:** checked in `STORE_LISTING_AND_EXPORT.md` §2. Title, subtitle, series name, description, keywords and categories contain no ⚡ and no ⚡️. The bolt stays on the cover art, the title page, the credits and the Patreon post title.
- **Second card: UNVERIFIED.** Kindle / ComiXology is not confirmed as a KDP route in this repo. Kindle Create's own comic help is a separate page (https://kdp.amazon.com/help/topic/G201217140). Do not treat "ComiXology is now part of KDP" as checked.
