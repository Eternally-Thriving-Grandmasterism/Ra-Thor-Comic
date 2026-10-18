# Ra-Thor⚡Living Thunder #1 · TOLC — DRAFT social promo kit

**DRAFT ONLY, for Sherif to post himself. Nothing here has been posted, scheduled or sent.** Built 2026-10-16 (ET). Re-run with `python3 build_promo.py`.

## Files

| File | Dimensions | Size | Purpose |
|---|---|---|---|
| rathor01_square_1080x1080.png | 1080x1080 | 1.79 MB | Instagram/Facebook feed square. Crop of the front cover, hero centred, cover logo + ISSUE #1 coin whole. No added type. |
| rathor01_square_1080x1080.jpg | 1080x1080 | 625 KB | High-quality JPG (q95, 4:4:4, sRGB ICC) of the same image. |
| rathor01_story_1080x1920.png | 1080x1920 | 2.37 MB | Instagram/Facebook story (9:16). Full front cover with a dark text panel: LEFT IS NOISE. / RIGHT IS LIVE., #1 · TOLC, COMING SOON. Type kept above the bottom UI zone; art starts below the top header zone. |
| rathor01_story_1080x1920.jpg | 1080x1920 | 828 KB | High-quality JPG (q95, 4:4:4, sRGB ICC) of the same image. |
| rathor01_card_1600x900.png | 1600x900 | 1.37 MB | X/Facebook link card (16:9). Front hero on the right; left column on a dark gradient made from the back-cover art: #1 · TOLC, headline, "All that comes to the TOLC is weighed.", FOLLOW FOR UPDATES, publisher/TM fine print. |
| rathor01_card_1600x900.jpg | 1600x900 | 518 KB | High-quality JPG (q95, 4:4:4, sRGB ICC) of the same image. |
| layers/rathor01_card_1600x900_art.png | 1600x900 | 1.31 MB | Art only (no words), the exact pixels under the type. |
| layers/rathor01_card_1600x900_type.png | 1600x900 | 195 KB | Type only: straight-alpha RGBA, all words/rules. Final = art·(1−a) + type·a. |
| layers/rathor01_square_1080x1080_art.png | 1080x1080 | 1.83 MB | Art only (no words), the exact pixels under the type. |
| layers/rathor01_story_1080x1920_art.png | 1080x1920 | 2.44 MB | Art only (no words), the exact pixels under the type. |
| layers/rathor01_story_1080x1920_type.png | 1080x1920 | 145 KB | Type only: straight-alpha RGBA, all words/rules. Final = art·(1−a) + type·a. |
| build_promo.py | — | 11 KB | Re-runnable build script (Pillow + NumPy + OpenCV). Copy lines are in the EDITABLE COPY block at the top; type is built on separate layers from the art. |
| promo_copy.md | — | 4 KB | 5 X posts (with character counts) + 2 long captions + alt text. |
| README.md | — | — | This file. |

## Sources (only these)

- Front art: right half of `/workspace/issue01/kdp/RaThor_Issue01_KDPwrap_24p_premium-color.jpg` (painted V18-era KDP wrap, 4067x3150 @300 dpi; per `production/ISSUE_01/HANDOFF.md` the painted V18 cover is now history, not canon, since the issue went inked). Crops stay inside the front trim (x 2046–4029, y ≥ 40) so no spine or bleed shows; the script asserts the RA⚡THOR LIVING THUNDER logo + ISSUE #1 coin box (wrap x 3120–3905, y 115–345) is fully inside every crop.
- Dark backgrounds: `/workspace/issue01/back/back_art_v2.png` (the back cover's art layer, no text), cropped, heavily blurred and dimmed.
- No other Ra-Thor/Grok images were used (none of the protected cards), and no AI-generated art. Everything is crop/resize/blur/tone in Python.

## Typography

Matches the back cover (`/workspace/issue01/back/build_back_v2.py`): **Cinzel** (variable, wght 700) in the back cover's metallic gold ramp for headlines and the issue line; Cinzel wght 600 in the silver ramp, widely tracked, for COMING SOON / FOLLOW FOR UPDATES; **EB Garamond Italic** in warm parchment for the TOLC line; EB Garamond for the fine print. Fonts are at `/usr/share/fonts/truetype/sand-box/google/`. All were found; no substitutes needed.

## Rules followed

- Draft files only: nothing posted, sent, scheduled or uploaded.
- Banned word (a surname) not used anywhere; Mercy-Checks / Mercy-Ways are never numbered or counted.
- TOLC8 and PATSAGi Councils are names only, with no explanation; no TOLC mathematics.
- No preorder links, prices, release dates or "available now". CTAs are only "Coming soon" / "Follow for updates".
- No AGSi claims, no crypto/NFT.
- Credits: Publisher AlphaProMega Media Inc.; Ra-Thor™ is a trademark of Autonomicity Games Inc. (application pending), used with permission.
- The ⚡ is optional. Use it where emoji render and drop it ("Ra-Thor Living Thunder") in fields that strip emoji. Images use the cover logo's own bolt, so no emoji is rendered in the art.
- Type is kept separate from the art (see `layers/`).
- Social safe zones: on the story, the art starts 170 px down and the type ends above y≈1700. On the square and card, the logo stays whole and sits well inside the edges.
