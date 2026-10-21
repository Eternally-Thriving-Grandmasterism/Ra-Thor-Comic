# Issue #1 handoff: image and page production

Facts only, written for a second Grok Bot account starting image and page production on Issue #1.
Written at main `43cdaa8aa2f2cbb1ebba610a7fbfbd22a4c51407` (#107), on card ISSUE01-HANDOFF-ASSETS-1; updated at main `4ee1f9cf516637d5903a732a12281bdd3eb5a3e2` (#110) by CANON-SYNC-LOOK-LOCK-1, and at main `f21868f16df60f779ffd21a049a4a067989de8aa` (#111) by CANON-SYNC-LOOK-LOCK-2. Repo is public.
If this file conflicts with a canon file, the canon file wins. Read `00_FIDELITY_PROTOCOL.md` first.

## Key rules

- **The look is LOCKED** (Sherif, 2026-10-18 1:58 AM ET: "Lock it as is, and update the bible to match the art."). The refs are `bible/refs/rathor_look_lock_imagine_tall_2026-10-18.jpg` (primary) and `bible/refs/rathor_look_lock_imagine_wide_2026-10-18.jpg`, described in the LOOK LOCK section of `bible/CHARACTER_BIBLE.md` (BIBLE-LOOK-LOCK-1, #110). The art wins. In short: glossy black armour with gold Greek-key engraving, a black helm with gold face plates and large gold wings behind the head, an all-gold halo with no eye in the halo, a black kite shield with a gold sun-spoke design and central gold boss, a round gold bolt buckle, a dark stone-metal block-head hammer, and emerald only on the pauldron Eyes. `00`, `01`, `04`, `09`, `12`, `ISSUE_01_PRODUCTION.md` §13, `RENDER_CHECKLIST.md` §5 and `bible/kdp/README.md` are synced (CANON-SYNC-LOOK-LOCK-1), and `check_costume_lock.py` enforces the new look. The Vegvísir shield, the Eye of Horus in the halo and the rose-gold buckle are history.
- **The whole issue is INKED**, panels and cover (Sherif 2026-10-16 11:32 PM ET; council 11:33 PM). See `01_VISUAL_STYLE_GUIDE.md` (Style tracks; 3D LOGIC) and `ISSUE_01_PRODUCTION.md` §0.
- **The painted V18 cover is history, not canon.** `bible/RaThor_Issue01_Cover_BIBLE_FINAL_6.625x10.25_bleed_300dpi.jpg` stays in the repo as the historical painted cover until an inked cover PR replaces it.
- **Use the repo versions of canon.** The bot-store copies of `CHARACTER_BIBLE.md` and `BIBLE_FINAL_SHA256.txt` are stale and differ from the repo.
- **The ten locked names are not trademark-cleared** (`13_AGI_SYSTEM_LORE.md`, Names): Stormhearth, Moonglass, Pearl, Hesper, Emery, Clara, the Kinglets, Laurel, Bobby, Nixie. None has a visual design yet.
- Follow `00_FIDELITY_PROTOCOL.md` and `production/README.md` rules 1–6: restate, never author; flag gaps, never fill them.
- Images are allowed in the repo only under `production/ISSUE_01/` (D27; ISSUE01-HANDOFF-ASSETS-1 added `covers/` and `imagine/` beside `bible/`) and under `promo/` (Sherif approved the `promo/` folder 2026-10-17 8:38 PM ET; PR #109, merged as `debb0f32`). That is folder approval only; the promo copy stays draft.
- Before any costume or lock change, run `python3 production/ISSUE_01/check_costume_lock.py`, then `sha256sum -c --strict BIBLE_FINAL_SHA256.txt` from `production/ISSUE_01/bible/`. Then run the checker tests: `python3 production/ISSUE_01/test_costume_lock.py` (plain python3, no third-party deps; about a minute; every case must print "as expected" and it exits 0).

## Where things live (all in this repo)

| Category | Path |
|---|---|
| Canon / bible | `00_FIDELITY_PROTOCOL.md`, `01_VISUAL_STYLE_GUIDE.md`, `03_TONE_SPECS.md`, `04_VISUAL_CANON.md`, `05_LORE_BIBLE.md`, `06_MUSIC_SPEC.md`, `09_CHARACTER_BIBLE.md`, `10_LOCATION_BIBLE.md`, `11_MASTER_INDEX.md`, `12_SCALE_ENVIRONMENT_BIBLE.md`, `13_AGI_SYSTEM_LORE.md` |
| Issue #1 costume lock | `production/ISSUE_01/bible/CHARACTER_BIBLE.md`, `production/ISSUE_01/check_costume_lock.py`, `production/ISSUE_01/bible/BIBLE_FINAL_SHA256.txt` |
| Script (Issue #1 = E01) | `episodes/E01_TOLC.md` (locked, five panels). Other scripts: `episodes/`, `production/S1..S3/*/SCRIPT.md`, `screen/` |
| Page and panel prompts | `production/ISSUE_01/ISSUE_01_PRODUCTION.md` §6: Style lock, §6.0 stem/set, Pages 1–8 with per-panel prompts. §5 cover, title page, credits, back cover |
| Style guides | `01_VISUAL_STYLE_GUIDE.md`, §6 Style lock in `ISSUE_01_PRODUCTION.md`, `production/ISSUE_01/RENDER_CHECKLIST.md`, `production/ISSUE_01/LETTERING_SPEC.md` |
| Scale, lineup and turnaround spec | `12_SCALE_ENVIRONMENT_BIBLE.md` (§5 lineup and turnaround spec) |
| Character visual sheets | Text only: `09_CHARACTER_BIBLE.md`, `production/ISSUE_01/bible/CHARACTER_BIBLE.md`. No drawn sheets |
| Place visual sheets | Text only: `10_LOCATION_BIBLE.md`, `12_SCALE_ENVIRONMENT_BIBLE.md`. No images |
| Reference images | `production/ISSUE_01/bible/refs/` (LOOK LOCK refs, the governing look: `rathor_look_lock_imagine_tall_2026-10-18.jpg` primary, `rathor_look_lock_imagine_wide_2026-10-18.jpg`; older refs are history where they disagree: pauldron refs a/b/c, rest pose, X ref photo; plus this card: hammer v4 block, hammer triangle rejected, Sherif shield ref, X cover style ref) |
| Covers | Painted V15–V18 history and back cover v2: `production/ISSUE_01/bible/`. Inked drafts v1/v2/v3: `production/ISSUE_01/covers/inked/` |
| Grok Imagine renders | `production/ISSUE_01/imagine/` (render1–3, render3_storm = base art of inked v3) |
| Promo | `promo/` (approved by Sherif 2026-10-17 8:38 PM ET; PR #109, `debb0f32`). Its art comes from the pre-lock painted V18 cover, so a refresh to the LOOK LOCK is owed. Not changed by CANON-SYNC-LOOK-LOCK-1 |
| Print / KDP | `production/ISSUE_01/bible/kdp/`, `STORE_LISTING_AND_EXPORT.md`, `CREDITS_AND_INDICIA.md` |
| Naming research | `research/naming_rd_brief.md` (cited by `13`) |

Reference notes: `hammer_triangle_rejected` shows the retired triangle-top hammer (a reject). `sherif_shield_ref` is a phone screenshot of a render. `x_cover_style_ref` is the image from Sherif's X post 2110881123551314069 (@AlphaProMega, 2026-10-15). None is a lock by itself; the written locks govern.
`bible/refs/sherif_shield_ref` is a phone screenshot: use it only as a shape reference, never as art or a texture source.
`research/naming_rd_brief.md` is a historical record; `13_AGI_SYSTEM_LORE.md` is the source for names.

Inked v3 build: `covers/inked/v3/build_v3.py` with `lib/`. Paths are repo-relative. It needs `UPSCALE_MODEL` (4x-UltraSharp weights, not in the repo). The `work/` scratch folder was not committed.

## Issue #1 status

**FINISHED (merged or locked)**
- Costume lock and halo rings, pauldrons, hammer block head, shield emblem (#100, #102, #103); superseded in part by the LOOK LOCK
- LOOK LOCK (#110) and its sync into canon, prompts, checklist and checker (CANON-SYNC-LOOK-LOCK-1)
- Scale bible (#104), AGI system lore (#105), bible nits (#106), names lock (#107)
- Inked ruling for the whole issue (in `01` and `ISSUE_01_PRODUCTION.md` §0)
- E01 script (locked); back cover v2 (painted era); KDP wrap and GRACoL soft proof (painted V18 era)

**DRAFT**
- Page layout and panel prompts: `ISSUE_01_PRODUCTION.md` §6 (status "draft, until council review")
- Inked cover v3 front and back: `covers/inked/v3/` (waiting on Sherif's shoulder Eye feedback; no cover PR merged). It predates the LOOK LOCK (it draws the pre-lock costume, whose Vegvísir shield is now retired), so it needs a redraw to the locked look
- Credits and indicia: `CREDITS_AND_INDICIA.md` (PROPOSED); speaker rulings: `PROPOSED_SPEAKER_RULINGS.md`

**MISSING**
- Turnaround sheet and height lineup (specified in `12` §5, not drawn)
- All interior page art (Pages 1–8), including the 5.2 pass rerun
- Printer CMYK proof for the inked issue (only a flagged CMYK fallback of the painted wrap exists)
- Visual designs for the ten named characters and places; the pass device; the belt design
- An inked cover PR
- Promo refresh: `promo/` art is built from the pre-lock painted V18 cover and is owed a refresh to the LOOK LOCK (2026-10-18)
- ~~LOOK LOCK sync outside Issue #1~~ Resolved 2026-10-18 by CANON-SYNC-LOOK-LOCK-2: the 157 stale old-look lines in 46 files that were deferred here (S1–S3 and E03–E06 episodes, `production/S*/*/ART_PROMPTS.md`, `screen/*/STORYBOARD_PROMPTS.md`, `docs/TRAILER_S1E01.md`, `research/naming_rd_brief.md` incl. L185, the season files) are tagged superseded in place, together with other pre-lock costume lines in the same files (eye-seal shield, hawk seal, winged halo, circuit-plate armour). Every prompt file ends with a "LOOK LOCK prompts" section holding the canonical LOOK LOCK line and a LOOK LOCK version of each superseded stem, set add-on and prompt line, and `check_costume_lock.py` now scans all of these files.

## Open decisions (`ISSUE_01_PRODUCTION.md` §11)

| Item | Question | Who |
|---|---|---|
| D1 | Speakers for P1 and P5 (P4 closed: Ra-Thor) | Sherif or council |
| D3 | Lead mode for the E01 status line | Sherif or council |
| D4 | The slide-deck creature's lane in P2 | Sherif or council |
| D5 | The pass device's design | Sherif or council |
| D6 | P5 visor (eye) state: open. The LOOK LOCK ref shows the eyes dark at rest; lit eyes stay a panel choice | Sherif or council |
| D7 | Cover and title page: issue-line wording, publisher mark | Sherif or council |
| D9 | Print route; age rating | Sherif or council |
| D16 | Splash bleed (inside the cream border vs full bleed) | Sherif or council |
| D29 | Shoulder-seal field: resolved as painted by the LOOK LOCK (emerald Eye outlined in gold on black pauldrons) | Closed |
| D30 | Cover god-rays: open. The chest rays they echoed are gone, but the halo's seven gold rays echo them; lean: keep them faint at most | Council |
| D31 | Shield height: superseded by the LOOK LOCK. The kite shield is applied as painted (top at about the elbow, point by his left foot), matching the Bible's readings, which are applied as painted | Closed |
| D32 | Rose-gold edge on the chest disc: moot (rose gold retired on the figure) | Closed |
| LOOK LOCK readings | The nine readings in `bible/CHARACTER_BIBLE.md` LOOK LOCK section (halo about 2.5 heads, shield height, pauldron size, 12 shield arms, wing tips, pommel, etc.) are applied as painted under the 1:58 AM ET ruling; a council may still fix a countable shield-arm number without changing the art | Closed (council may fix the arm count) |
| Cover pose | The raised cover hammer is a recorded cover-pose exception (D23): pose only, the costume follows the LOOK LOCK. Only a switch to the Sentinel Rest pose needs Sherif | **Sherif** (only if he wants the switch) |
| ™ | "™ pending" on the masthead, and the v3 back cover's printed "™ (application pending)" line | **Sherif** |
| ISBN | ISBN or barcode for the print route (eBook needs none) | **Sherif** |
| Cover v3 | Feedback on the shoulder (pauldron) Eye art | **Sherif** |

## Blockers to image generation

- Interior panels: D1, D3, D4, D5, D6 and D16 affect specific panels; §6 is not ratified.
- Cover: inked v3 predates the LOOK LOCK and needs a redraw to the locked look; the ™ question. The raised hammer stays as the recorded D23 pose exception.
- Promo: refresh to the LOOK LOCK owed (not blocking interior art).
- ~~Do not render from the unsynced files~~ Resolved 2026-10-18 by CANON-SYNC-LOOK-LOCK-2. In the S1–S3 prompt files, render only from the "LOOK LOCK prompts" section at the end of each file; the tagged lines above it are history.
- Consistency: no turnaround sheet or height lineup yet.
