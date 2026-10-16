# Issue #1 — Lettering spec · PROPOSED

- **Card:** ISSUE01-FINISH-1 (c). Docs only.
- **Built from main:** `1ad0ae04c73254ee6eadfdca2fda43d16b1b9c43`.
- **Status:** **PROPOSED CANON — pending council ratification**, except where a line cites canon.
- **Text source:** `ISSUE_01_PRODUCTION.md` §7 lettering script, which is verbatim from `episodes/E01_TOLC.md`. This spec changes no words, no case and no punctuation.

## 1. Canon this spec must keep

- White oval bubbles, hard black outline, pointed tail (`04_VISUAL_CANON.md` L43; Q11 white fill).
- Tail aimed at the visor slit even though the mouth is hidden (`01_VISUAL_STYLE_GUIDE.md` L18). Under the 8:57 PM owner ruling of 2026-10-14 the helm has a T-visor with two glowing eyes; wherever this file says "visor slit", read the T-visor's eye line (`ISSUE_01_PRODUCTION.md` §6 Style lock).
- Captions small, bottom-left, Quiet Board dossier voice (`01_VISUAL_STYLE_GUIDE.md` L19).
- One bubble per panel; silent panels carry no text (`00_FIDELITY_PROTOCOL.md` rule 3; council ruling 2026-10-14).
- Bold hand-lettering; all caps (R1, R2) or mixed-case italic (R3, R6) (`04_VISUAL_CANON.md` L43). Which one is unruled (`ISSUE_01_PRODUCTION.md` §11 D2). Until it is ruled, letter the file's case.
- P4 tail goes to Ra-Thor's visor in the background without turning him (council ruling 2026-10-14).

## 2. Fonts (free for commercial use, licence verified 2026-10-14)

| Use | Family and weights | Licence | Licence URL (fetched 2026-10-14) | Project |
|---|---|---|---|---|
| Bubbles and captions | Comic Neue: Bold; Bold Italic only if D2 rules mixed-case italic | SIL Open Font License 1.1 | https://raw.githubusercontent.com/google/fonts/main/ofl/comicneue/OFL.txt | https://github.com/crozynski/comicneue |
| Title only (cover, title page, credits) | Cinzel: Bold or Black | SIL Open Font License 1.1 | https://raw.githubusercontent.com/google/fonts/main/ofl/cinzel/OFL.txt | https://github.com/NDISCOVER/Cinzel |

What was checked on 2026-10-14:

- Both `OFL.txt` files state "This Font Software is licensed under the SIL Open Font License, Version 1.1." Neither lists a Reserved Font Name after its copyright line.
- OFL 1.1 grants permission "to use, study, copy, merge, embed, modify, redistribute, and sell modified and unmodified copies", with the one bar that the font may not "be sold by itself". It adds: "The requirement for fonts to remain under this license does not apply to any document created using the Font Software."
- OFL FAQ 1.1 (https://openfontlicense.org/ofl-faq/): "Can I use the fonts for a book or other print publication…? Yes." FAQ 1.13: embedding an OFL font "does not change the license of the document itself."

Rules:

- [ ] Download the fonts from the project or the `google/fonts` repository above, not from a mirror.
- [ ] Keep each `OFL.txt` with the lettering source files. Do not commit font files to this repo.
- [ ] Do not ship the font files with the comic. Embedding in a PDF is allowed (FAQ 1.12–1.13); handing the font files over is distribution and needs the licence text.
- [ ] Re-check the licence URL on the day of export; record the date beside the files.
- [ ] No other font enters the book without its own row in this table.

The `⚡️` in the title is drawn as vector art, not taken from an emoji font (`ISSUE_01_PRODUCTION.md` §10). Neither font above is used for it. On the cover, the bolt is the rose-gold Ra-Thor app-icon bolt set as RA-THOR's hyphen (council lettering ruling, `ISSUE_01_PRODUCTION.md` §5.1).

## 3. Sizes

Sizes are at print size on the 6.625 × 10.25 in trim (`ISSUE_01_PRODUCTION.md` §10). Digital pages are scaled from the same master, so the type scales with them.

| Element | Size / leading | Case | Notes |
|---|---|---|---|
| Bubble text (2.3, 4.1, 5.2, 8.1) | 10 pt on 11.5 pt | File case (D2) | Comic Neue Bold |
| Tiny bubble (6.1, "Recycle it.") | 8 pt on 9 pt | File case (D2) | "Tiny" is locked text (E01 P4); the balloon and type are smaller than the rest |
| Caption text (1.1, 8.1) | 10 pt on 11.5 pt | All caps, as written | Comic Neue Bold |
| Cover title | Fit to the bottom title band (council frame ruling, `ISSUE_01_PRODUCTION.md` §0) | RA-THOR over LIVING THUNDER (council lettering ruling) | Cinzel with a gold-foil bevel look; the hyphen is the rose-gold app-icon bolt as vector art, no emoji; LIVING THUNDER in spaced caps |
| Cover medallion | Fit to the medallion in the title band | `ISSUE: #1`, exactly | Cinzel; no other cover text, no tagline |
| Title page title | 28–36 pt | As written | Cinzel |
| Credits and indicia | 7–8 pt | As written | Comic Neue Bold or Regular |

**Legibility check against KDP.** KDP's fixed-layout text rule: capitals "at least 2mm high in pop-ups, when viewed on a 7" device" (https://kdp.amazon.com/en_US/help/topic/G9GSTY4LTRT39D4Z, fetched 2026-10-14). Worked check, assuming a cap height of 0.7 em (measure the real font before relying on it):

- A 7 in 16:10 screen held portrait is about 3.71 in wide. The page fits by width, so the page shows at about 0.56× print size.
- 10 pt text: caps 7 pt = 2.47 mm in print, about 1.38 mm on screen. At the 150% default zoom, 2.07 mm: passes.
- 8 pt tiny bubble: caps 5.6 pt = 1.98 mm in print, about 1.11 mm on screen. 150% gives 1.66 mm (fails); 200% gives 2.22 mm (passes). KDP lists 200% as the zoom "for small text" (same URL). So panel 6.1's Guided View selection must zoom to at least 200%, or the tiny bubble's type goes up to 10 pt.
- The deciding test is the Kindle Create Previewer on the Phone device type in horizontal orientation, which KDP recommends for checking Guided View (https://kdp.amazon.com/help/topic/G201217140, fetched 2026-10-14).

## 4. Bubble style

- Shape: oval, white fill, black outline 1 pt at print size. Pointed tail, same stroke.
- Text: 100% K, centred, at least 1.5× cap height of white space between text and outline.
- Tail: one tail per bubble, aimed at the visor slit. The tip stops about 1 mm short of the slit so the gold slit stays visible.
- 6.1: the tail runs from the bubble near the hopper back to Ra-Thor's visor in the background. Do not turn or redraw him.
- No bubble covers the shield's Vegvísir, the visor slit, the NO or LIVE stamps where a panel shows them, the three cards in 6.2, or the hammer's contact point.
- No bursts, no whispers, no colour fills. Canon describes one bubble type (`04` L43).

## 5. Caption style

- Position: bottom-left of the panel, inside the safe area (`01` L19; `ISSUE_01_PRODUCTION.md` §10).
- Box: rectangle, 100% K fill, 0.5 pt gold keyline. White text, all caps, as written.
- 1.1: the caption is the only text on the splash.
- 8.1: the caption sits bottom-left and reads after the "Next." bubble.

## 6. Order of placement over renders

Do these steps in order, on the print master first.

1. **Lock the render.** Only renders that pass `RENDER_CHECKLIST.md` (fidelity check plus 4–5/5) are lettered.
2. **Place art in the page template** at final size, with bleed. Panel borders and gutters live on the template, not in the render (`ISSUE_01_PRODUCTION.md` §10).
3. **Mark keep-clear zones** on a guide layer: eye-seal, visor slit, lane stamps, cards, hammer contact, safe area.
4. **Place captions** (1.1, then 8.1), bottom-left.
5. **Place bubbles in reading order:** 2.3, 4.1, 5.2, 6.1, 8.1. Within 8.1, the bubble sits higher or further left than the caption, so the caption reads second.
6. **Draw tails last**, to the visor slit, checking the keep-clear zones.
7. **Proof every line** character for character against `episodes/E01_TOLC.md`.
8. **Keep the vector layers** in the print master. Flatten only the digital exports (JPEG pages for Kindle Create, which has no text tools: https://kdp.amazon.com/help/topic/G201217140).
9. **Run the legibility check** (§3) in the Kindle Create Previewer.

Layer stack, bottom to top: art · panel borders and gutters · caption boxes · bubble shapes · tails · text · guides (hidden on export).

## 7. Not in this spec

- No SFX lettering: E01 has no SFX (`ISSUE_01_PRODUCTION.md` §12 item 10).
- No new captions or bubbles on the 12 `PACING` panels.
