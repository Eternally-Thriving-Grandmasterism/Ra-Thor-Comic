# Ra-Thor⚡️Living Thunder audio plan: end-to-end pipeline — PROPOSED — pending council ratification

**Card:** AUDIO-PLAN-1. **Council GO (Wild) with AMENDs, 2026-10-14.** Docs only. This file is the only change.

**Status: every line in this file is PROPOSED — pending council ratification.** That covers the source order, the ledger and its rules, the style traits, the cue maps, the specs, the amendment text and the follow-ups. Nothing here amends `06_MUSIC_SPEC.md`. Where this file and `06_MUSIC_SPEC.md`, `docs/AUDIO_RND.md` (#82) or `docs/TRAILER_S1E01.md` (#83) disagree, those files win until the council rules.

**Scope.** One audio pipeline for Living Thunder: where music comes from, how a licensed track is cleared, what each cue should sound like, and how voice, SFX, mix, master and deliverables are specified. It covers the S1E01 trailer, the S1E01 episode, comic promos and Patreon. Every missing field is marked **GAP** and left unfilled.

**Read first:** `00_FIDELITY_PROTOCOL.md`, `bots/GROKBOT_COMIC_SEAT.md`, `06_MUSIC_SPEC.md`, `docs/AUDIO_RND.md`, `docs/TRAILER_S1E01.md`, then `screen/S1E01/SCORE_PLAN.md`.

**Rulings this file follows** (PR #83, comment 6178168603, Wild, ACCEPT @ `ec5c1d8d`):

> (1) Fallback proposal ACCEPT: temp or promo use only, it may only replace C01/C02/C08, and AUDIO-PLAN-1 amends §5 with the ledger. The final trailer and episodes stay original music. (2) Add S29, so 'Recycle it.' lands on its own shot (~59 s). (3) A title card of 2–4 s brings it to 61–63 s, inside the 60–90 s target. Title card text waits on the GAP and must not invent new copy. Apply (2) and (3) as a follow-up slice.

Rulings (2) and (3) belong to the trailer follow-up slice. This file records their effect on the cue map (§4.1) and does not apply them to `docs/TRAILER_S1E01.md`.

**Sherif directive (2026-10-14, 4:52 PM ET), as relayed on the card:**

> No unnecessary walls. If something is legally usable for free or at minimal cost and works for the audio, it's approved. That includes CC-BY with attribution, low-cost royalty-free subscriptions, and licensed tracks in the final cut, not only temp. Keep the checks lean: a verified license page and a ledger row are enough. Drop the extra hurdles (no written sync licence when the license page already grants commercial use, and no original-only restriction for C01/C02/C08). Write the 06 §5 amendment as a PROPOSED change to match. The only lines that stay are no infringement, no named-artist imitation prompts, and no purchases by bots.

This file follows the directive. Where it widens Wild ruling 1 (licensed tracks in the final cut, not only temp or promo), the directive is applied here as PROPOSED, pending the council recording it.

---

## 0. Bounds — PROPOSED — pending council ratification

**The three lines that stay** (Sherif directive):

1. **No infringement.** Every track has a verified licence page that covers the use, and a ledger row. A track that is recognisable as someone else's work without a licence for it is out.
2. **No named-artist imitation prompts.** No AI prompt or brief names an artist or track, or asks for "like X." Craft terms only: tempo, key, instrumentation, texture.
3. **No purchases by bots.** No agent buys, subscribes or signs up. A human (Sherif or someone he names) makes every purchase.

**Approved, under the directive:** free and low-cost licensed music, including CC-BY with attribution and royalty-free subscriptions, in temp, promo **and the final cut**. A verified licence page and a ledger row are the whole check.

**Other house rules this card does not touch** (they are not licensing walls, and the directive does not mention them):

- **Fixed house assets.** "Blocked.", "That one can live." and the Grounded motif are reused unchanged across episodes (`06_MUSIC_SPEC.md` §1). The directive frees C01, C02 and C08. C06, C09 and C10 stay the house files (GAP A17 if Sherif wants them opened too).
- **No names in this file.** This planning file names no individual track or artist, as the card asked. Ledger rows and required attribution credits may carry names (§2, §6).
- **Vendor names are licence sources only.** The libraries and tools named in §2 and §5 are where a licence comes from, not prompt material.
- **No outside IP or show names** anywhere in this file, including in the style traits.
- **Frequencies are mood only.** 432 Hz, 543 Hz, 528 Hz and 108 / 54 Hz carry no health claim. Banned wording includes "healing frequency", "DNA repair", "miracle tone", "pineal activation" and "safe & effective" (`06_MUSIC_SPEC.md` §4). This applies to ledger notes, Patreon copy and promo captions too.
- **Wordless in episodes.** Sung words only in the series intro and outro themes (Sherif, 2026-10-01 12:17 AM ET; `06_MUSIC_SPEC.md` §5).
- **No commerce here.** No purchase, no price taken as a commitment, no publishing. A vendor fact in this file is what a page said on the date shown. A human re-checks it at purchase (§7).
- **This file edits nothing else.**

---

## 1. Source order — PROPOSED — pending council ratification

One order for every use: temp, promo and final. Take the first tier that works for the cue. Every track, from any tier, gets a ledger row (§2).

1. **Sherif's own X-posted tracks**, under the §2.2 X-post rule.
2. **Free or low-cost licensed music**: CC0, no-attribution libraries, CC-BY with attribution, and low-cost royalty-free subscriptions (§2.4). Prefer CC0 or no-attribution when two tracks fit equally, because it keeps the credits short. It is a preference, not a gate.
3. **The #82 path: AI drafting with a human finisher** (`docs/AUDIO_RND.md` §5.2, §5.3 and §6), or a human composer.

**Where licensed tracks may go.** Temp, promo and the final cut of the trailer, the episodes, comic promos and Patreon (Sherif directive). In the trailer, C01, C02 and C08 are open to any tier. C06, C09 and C10 are the fixed house assets (`06_MUSIC_SPEC.md` §1; §0 above).

**Today's state.** No track from any tier is in a ledger yet. The track list is pending from Sherif (GAP T14 in `docs/TRAILER_S1E01.md` §6). No finisher is named and no host is picked (`docs/AUDIO_RND.md` §8 items 3–4). No subscription is bought; a human buys one if Sherif wants it.

---

## 2. License ledger — PROPOSED — pending council ratification

### 2.1 Template (one row per track)

| ID | Tier | Use and slot | Source URL | License text or link | Attribution needed (credit text) | Content ID / registration risk | Date verified | Status |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

**Column rules**

- **ID.** An internal ID such as `LIC-001`, used in cue sheets and file names.
- **Tier.** 1, 2 or 3 (§1). Tier-3 takes also get a row in the `06_MUSIC_SPEC.md` §5 per-track log.
- **Use and slot.** Temp, promo or final, plus the slot: a cue such as `C01`, or a promo ID for a comic or Patreon piece.
- **Source URL.** The original creator's or library's page, not a repost.
- **License text or link.** The licence page as read that day, with its version or "last updated" date if it shows one, and the plan or tier if it is a subscription. It must cover the use in the row (for example, broadcast or theatrical if the piece goes there).
- **Attribution needed (credit text).** No, or yes plus the exact credit the licence asks for. A "yes" goes into the credits or description of every piece that uses the track.
- **Content ID / registration risk.** Whether the track is registered with a fingerprinting system, and what proof the source offers (a licence certificate, a channel safelist). "Unknown" is fine to write down.
- **Date verified.** The date the licence page was read for this row.
- **Status.** One of the values in §2.3.

That is the whole check: a verified licence page and this row (Sherif directive).

### 2.2 X-post rule (tier 1)

An X-posted track is usable if Sherif made it, **or** the original creator's own licence page grants commercial use. No separate written sync licence is needed when the licence page already grants commercial use (Sherif directive). Hands' #83 note asked for a written sync licence. Under the directive that applies only when the licence page does not grant commercial use.

**UNVERIFIED until a licence page is found.** A repost, a "free" or "no copyright" caption, or a reply calling a track royalty-free is not a licence page. Find the creator's page, then add the row. The four music-link posts recorded in `docs/AUDIO_RND.md` §1 are UNVERIFIED for that reason. Their links were not opened.

If Sherif made the track with an AI tool, the row also records that tool's terms on the creation date (`06_MUSIC_SPEC.md` §5).

### 2.3 Status values

| Status | Meaning |
|---|---|
| **UNVERIFIED** | No licence page yet, or the page does not cover the use. Not usable yet. |
| **APPROVED** | Licence page verified for the use in the row. Usable in temp, promo or final, as the row says. |
| **REJECTED** | Infringes, or the licence does not allow the use. |
| **RETIRED** | Replaced or no longer used. Kept for the record. |

**Practical notes** (not gates)

- Skip non-commercial (NC) licences for anything published, and skip no-derivatives (ND) licences for picture: the Free Music Archive guide says syncing to video counts as a derivative work, which ND forbids (§2.4). That is just what those licences say.
- Subscriptions: most cover what is published while the plan is active, and some need a higher plan for broadcast or theatrical use (§2.4). Record the plan in the row.
- In-episode cues stay wordless (Sherif, 2026-10-01; `06_MUSIC_SPEC.md` §5). Vocal tracks fit the intro, outro, comic promos and Patreon.
- A4 = 432 (`06_MUSIC_SPEC.md` §3.1): retune if the licence allows modification. Most licences in §2.4 do. A track that cannot be retuned: GAP A18 for Sherif.
- Re-read the licence page on the day of use. A licence can change. The row keeps the version that applied on the download date.

### 2.4 Candidate libraries (tier 2) — verified 2026-10-14

Licence pages as read on **2026-10-14**. No individual track is named or chosen. "Fit" is a proposal.

| Library | Licence page (as verified 2026-10-14) | What the page says | Attribution | Content ID / registration risk | Fit |
|---|---|---|---|---|---|
| **Pixabay** (music and SFX) | https://pixabay.com/service/license-summary/ ; FAQ https://pixabay.com/service/faq/ | Use free; modify or adapt; no standalone sale or distribution. The summary says only the full Content License is binding. FAQ: commercial video, including OTT and subscription platforms, is allowed when the music is part of a larger creative work. | Not required | **Medium.** FAQ: some contributors register tracks with Content ID; tracks with a shield icon are registered and "may trigger claims"; a licence certificate is offered for those. Keep the certificate with the row. | Beds for C01, C02 and C08 in any use; comic and Patreon promos. |
| **Mixkit** (music) | https://mixkit.co/license/modal/musicFree/ ; index https://mixkit.co/license/ ; terms https://mixkit.co/terms/ | Stock Music Free License: commercial use on web and social platforms, internet video on demand, podcasts and advertisements. **Not** CDs or DVDs, video games, or TV or radio broadcast. No remix into a music-only track. No registering on a rights-management service. | Not required (stated on https://mixkit.co/free-stock-music/) | Low on registration: the licence bars registering. Claims go to the address on the licence page. | Web promos and Patreon only. Not for a broadcast pilot or a game. |
| **Mixkit** (SFX) | https://mixkit.co/license/modal/sfxFree/ | Sound Effects Free License: films, TV and radio broadcast, video games, VOD, inside a larger end product. No standalone redistribution; no registering. | Not required | Low | Staged-action SFX and room tone. |
| **YouTube Audio Library** | https://support.google.com/youtube/answer/3376882 | Two licence types: the standard library licence, and Creative Commons tracks that must be credited in the video description. Audio Library tracks "won't be claimed by a rights holder through the Content ID system." The page says YouTube cannot give guidance on issues off the platform. | Standard: not required (filter "Attribution not required"). CC tracks: required. | Low **on YouTube**. Off-YouTube use is GAP A5. | YouTube uploads, both licence types (CC tracks with the credit in the description). |
| **Freesound** (SFX) | https://freesound.org/help/faq/ | Per-sound licence chosen by the uploader: CC0, CC BY, CC BY-NC, and legacy Sampling+. | CC0: no. BY: yes. | Unknown per sound | CC0 and CC BY (credit the creator). Skip BY-NC and Sampling+ for published pieces. Staged-action SFX and room-tone layers. |
| **Sonniss #GameAudioGDC bundle** (SFX) | https://sonniss.com/gdc-bundle-license/ (version 2.0, effective 27 August 2026) | Worldwide, royalty-free; personal and commercial projects without attribution; sync with games, films, television and interactive projects. No redistribution as sound effects. **No AI training** with the sounds. Licensor warrants it has authority to license. | Not required | Low | Staged-action SFX, room tone, impacts. Never fed to an AI tool. |
| **Kenney** (game audio, CC0) | https://kenney.nl/support | All game assets on the asset pages are public domain (CC0), commercial use allowed. Do not use the studio logo. | Not required | Low | UI-style blips for the twelve-mask ring or Lab Night, retuned to 432 if tonal. |
| **OpenGameArt** | https://opengameart.org/content/faq | Mixed licences per submission, including CC0, CC BY, CC BY-SA and GPL. CC0 is described as usable in any way without asking or crediting. | CC0: no. Others: yes. | Unknown per item | CC0, CC BY and CC BY-SA (credit as asked; BY-SA asks that a derivative carries the same licence, so check that fits before use). |
| **Free Music Archive** | https://freemusicarchive.org/License_Guide | Per-track Creative Commons licences set by each artist. ND licences: syncing to video is a derivative work and is prohibited. NC licences: no advertising or promotion without permission. | Most require it | Unknown per track | CC0 and CC BY tracks (credit as the guide shows: title, author, source, licence). Skip NC and ND for published picture. |
| **Openverse** (search, not a library) | https://openverse.org/about | Searches openly licensed and public-domain audio across sources. "Openverse does not verify licensing information for individual works." | Per source | Per source | Discovery only. Verify every licence at its source page. |

**Low-cost royalty-free subscriptions.** Read 2026-10-14. Uppbeat and Artlist block automated page loads, so their licence text was read through search extracts of the pages listed. A human re-reads each page and checks the plan before buying (§7). No price here is a commitment, and no agent buys a plan.

| Service | Licence pages (as read 2026-10-14) | What the pages say | Attribution | Content ID / registration risk | Fit |
|---|---|---|---|---|---|
| **Uppbeat** (music and SFX) | https://uppbeat.io/user-agreement ; https://uppbeat.io/uppbeat-basic-license ; https://uppbeat.io/pricing | Each download carries a pre-cleared master and sync licence. Free users must give the track's credit; the Basic License calls this "a material term". The plan sets where you may publish: the free and lower plans cover individuals on their own channels; Pro adds client work and commercial digital use; Business covers companies. Broadcast, cinema, radio and paid streaming need a custom licence. | Free plan: yes. Paid plans: GAP A19 (not confirmed from the extracts). | Low with the per-track credit and channel safelisting the service describes | Online trailer, promos and Patreon. Not broadcast without a custom licence. |
| **Epidemic Sound** (music and SFX) | https://www.epidemicsound.com/pricing/ ; https://www.epidemicsound.com/filmmaking/ ; https://www.epidemicsound.com/how-it-works/license-music-legally/ | Royalty-free direct licence for the catalogue. The Pro plan covers online ads, branded content and client work for social media and websites. TV, broadcast, and films for theatrical or festival release need the Enterprise plan. Content published during an active subscription stays cleared; new content after cancellation is not covered. | Not stated on the pages read: GAP A19 | Low on safelisted channels | Online trailer, promos and Patreon on Pro. Broadcast or festival use needs a higher plan. |
| **Artlist** (music and SFX) | https://help-center.artlist.io/help-center/privacy-terms/artlist-license/ ; https://help.artlist.io/hc/en-us/articles/7856595463581-Using-the-assets-in-a-film ; https://artlist.zendesk.com/hc/en-us/articles/6185461392029-Commercial-projects-and-advertising | A Pro licence covers commercial projects, and the film article lists YouTube, social media, TV, theatres, festivals, streaming and OTT. Projects published while subscribed stay covered in the same media. Not for standalone audio or radio. Companies with more than 50 employees need a Business plan. The film article notes the licence does not pay public-performance royalties to performing-rights organisations. | Not stated on the pages read: GAP A19 | Low on clearlisted channels | Widest reach of the three, including a pilot or festival screening, on a Pro plan. |

**CC0 reference.** https://creativecommons.org/publicdomain/zero/1.0/ (read 2026-10-14). CC0 waives copyright "to the extent allowed by law". It does not cover trademark, publicity or privacy rights, and the dedicator makes no warranty.

Libraries not listed were not read for this card. Adding one is a new read of its licence page, logged with the date (GAP A6).

---

## 3. Style reference — PROPOSED — pending council ratification

**Reference only:** Sherif's YouTube Music playlist, https://music.youtube.com/playlist?list=PLVTpZcM10F04 .

**What was read, 2026-10-14.** The public playlist page, logged out. The page is titled "Liked" and lists 25 items, updated that day. Only page metadata was read: item titles, uploading channel labels and running times. **No audio was heard.** No track, artist, channel or show name from the playlist is recorded here.

**What the metadata supports.** These are reads from titles and channel labels, not from listening. Each needs Sherif to confirm by ear (GAP A7).

- **Main cluster:** retro analog-style synth instrumentals with night, neon, drive and space imagery. Mood: nocturnal, nostalgic, steady forward motion.
- **A darker, heavier cluster.** Mood: menace and drive. In house terms that is darksynth, which is siege-only (`06_MUSIC_SPEC.md` §1). S1E01 has no siege.
- **Orchestral and cinematic score pieces.** Mood: wide, heroic swells. In house terms, the sparing choir and low-brass swell. The S1 choir is in S1E06 only.
- **One gentle, pastoral score compilation.** Mood: light, unhurried, cosy.
- **One lounge-jazz reworking led by saxophone.** Mood: smoky, late-night. Saxophone is not in the `06` palette.
- **One vocal version and one slowed edit.** In-episode cues stay wordless. Slowed edits suggest Sherif likes lower tempos; this is not a measured tempo.
- **Running times:** most single items run about 2 to 6 minutes; one item is a compilation of about 2 hours.

**Tempo: GAP A7.** No tempo can be measured from metadata. Every tempo in §4 comes from `06_MUSIC_SPEC.md` §2 and `screen/S1E01/SCORE_PLAN.md`, not from the playlist.

**How the traits are used.** As house craft terms in §4, and as a listening guide for humans picking tracks. No AI prompt names or imitates any item on the playlist (Sherif directive, line 2).

**Status of the link.** The current `06_MUSIC_SPEC.md` §5 says no brief, prompt, temp track, mix note or metadata may reference any existing work. The §6 amendment narrows that rule to named-artist imitation prompts, so a human reference link would be allowed. Until the amendment is applied, the link stays here as reference only.

---

## 4. Cue maps — PROPOSED — pending council ratification

Every cue keeps A4 = 432, the 543 Hz pad only over chords that contain C#, and the 528 Hz chime short only (`06_MUSIC_SPEC.md` §3). Every cue below is wordless.

### 4.1 S1E01 trailer

Timecodes are the current 56 s cut in `docs/TRAILER_S1E01.md` §2. Tempo: Suave Hour at 88 BPM (`screen/S1E01/SCORE_PLAN.md`). "Any tier" means a Sherif track, a licensed track or an original, in temp, promo or the final cut (Sherif directive).

| Cue | Span (current cut) | House cue (from `SCORE_PLAN.md`) | Style traits (tempo · instrumentation · mood) | Source |
|---|---|---|---|---|
| **C01** | 00:00–00:11 | A – F#m – Dmaj7 – E6, pad holds, 108 Hz drone, lead answers, soft drums, no bell | 88 BPM · analog-style pad, sine bass, soft snare, an answering lead · warm, unhurried, nocturnal (main cluster) | **Any tier** |
| **C02** | 00:11–00:16 | A – C#m – F#m – A, pad holds, drone on, **bell once on S11** | 88 BPM · electric-piano-style keys, pad, glassy bell once · nocturnal, colder minor tinge, late-night (main cluster; lounge colour) | **Any tier.** The one bell lands on S11; pick or edit so there is no second bell. |
| **C06** | 00:16–00:24 | Fixed "Blocked." stinger, unchanged; drone 108 Hz, no 54 Hz | Free time · short low muted thud, filter close · decisive, not menacing | House file (`06` §1) |
| **C08** | 00:24–00:37 | Light and dry, three card tones, CLEAN a clean A major bloom; drone **out**; pad back on the bloom | 88 BPM · sparse light figure, sparse drums, three short tones · dry, light (pastoral cluster's lightness, nothing heroic) | **Any tier.** Leave room for the three card tones and the two staged SFX. |
| **C09** | 00:37–00:50 | Fixed "That one can live." stinger, unchanged; drone returns | Free time · open A major bloom, short 528 Hz chime · open, kind | House file (`06` §1) |
| **C10** | 00:50–00:56 | Grounded motif, unchanged, lands on A and holds; no drums, no bell | Free time · Ra-Thor's lead timbre over the pad and drone · settled, home | House file (`06` §1) |

**Effect of Wild rulings 2 and 3 (follow-up slice, not applied here).** Adding S29 (3 s) puts "Recycle it." on its own shot. `SCORE_PLAN.md` already places S29 inside C08, so C08 would start on S29 and every later span would shift by 3 s, for about 59 s. A 2–4 s title card brings the cut to 61–63 s. **Music under the title card:** any tier under the directive; the choice is GAP A9. Title card text: GAP T1 in `docs/TRAILER_S1E01.md`.

**Fit notes from the house spec, not licensing:** the darker cluster is siege colour (S1E01 has no siege), the S1 choir is in S1E06, and trailer cues come from in-episode cues, which are wordless.

### 4.2 S1E01 episode

Cues from `screen/S1E01/SCORE_PLAN.md`. Under the directive, licensed tracks may be used in the final episode as well as in temp, each with a ledger row.

| Cue | Shots | Style traits (tempo · instrumentation · mood) | Source |
|---|---|---|---|
| C01 | S01–S06 | 88 BPM · pad, sine bass, soft drums, answering lead · warm, unhurried | Any tier |
| C02 | S07–S12 | 88 BPM · keys, pad, bell once on S11 · nocturnal, minor tinge | Any tier |
| C03 | S13–S15 | 88 BPM · pad muted over plain D and E, soft drums · colder, the offer has strings | Any tier |
| C04 | S16–S20 | Drums out · pad, twelve-mask blip ring panned wide · suspended, deliberating | Any tier for the pad. The blip ring is a house sound (`06` §1). |
| C05 | S21–S22 | 88 BPM · groove returns, answering lead · forward, poised | Any tier |
| C06 | S23–S25 | Fixed "Blocked." stinger | House file |
| C07 | S26–S28 | 88 BPM · groove resumes one bar later · settled | Any tier |
| C08 | S29–S33 | Light and dry, three card tones, drone out | Any tier |
| C09 | S34–S36 | Fixed "That one can live." stinger | House file |
| C10 | S37–S39 | Grounded motif | House file |

**Continuity note.** A licensed bed that changes key or tempo mid-cue may fight the 543 Hz pad rule (`06` §3.2) and the cue joins. The human editor picks for fit.

**Series intro and outro themes:** not in `SCORE_PLAN.md`. GAP A10. Sung words would be allowed there only, original, with no real names and no frequency claims (`06_MUSIC_SPEC.md` §5).

### 4.3 Comic promos

Issue #1 is E01 The Gate (`docs/SHIP_READINESS_AUDIT.md`). "E01 has no cue section; not needed for print" (`production/ISSUE_01/ISSUE_01_PRODUCTION.md` §12 item 11). The E01 lead mode is open (D3 in that file).

| Piece | Audio | Source |
|---|---|---|
| Issue #1 promo clip (motion or still-with-audio) | Bed: GAP A11 (no E01 cue exists; mode open). Button: the fixed "Blocked." or "That one can live." stinger once it is locked. | Bed: any tier, with a ledger row. Stingers: the house files. |
| Later issue promos | GAP A11 | Same rule |

**Promo rules.** Vocals are fine in promos. Required attribution goes in the post or description. No health wording. No series title inside a story frame (`seasons/S2_SEASON_SHEET.md` §5 item 8). No AGiRBE line or Fresco material in promo art or its audio copy (`production/README.md` rule 6). No prices or store links in this plan.

### 4.4 Patreon

`production/ISSUE_01/ISSUE_01_PRODUCTION.md` §10 defines digital page exports for Kindle and Patreon. It defines no Patreon audio.

| Piece | Audio | Source |
|---|---|---|
| Patreon post with audio or video | GAP A12 (no Patreon audio is defined anywhere) | Any tier, with a ledger row and any required credit in the post. |
| Behind-the-scenes audio (stems, drafts) | GAP A12 | Our own material. Licensed tracks only where the licence allows the file to be shared on its own; most library licences in §2.4 do not (standalone redistribution). |

---

## 5. Production specs — PROPOSED — pending council ratification

### 5.1 Voice-over casting

**Whether lines are spoken at all is open** (GAP T4 in `docs/TRAILER_S1E01.md`). There is no narrator (GAP T5 there). This section only states what a casting brief must meet if the council rules for spoken lines.

| Role | Lines in scope | Direction from canon | Casting |
|---|---|---|---|
| Ra-Thor (he) | Trailer: "A gift with knots is a contract.", "Blocked.", "That one can live."; with S29, "Recycle it." Episode: all his S1E01 lines. | "Voice in bubbles is dry, short, slightly fond. Never lectures." (`09_CHARACTER_BIBLE.md`). The visor slit carries the line; there is no mouth (`docs/TRAILER_S1E01.md` T03). | GAP A13 |
| The Ribbon Envoy (she) | Episode only: "My house sends gifts, not terms." (`episodes/S1E01_THE_RIBBON_CLAUSE.md` L18). Not in the trailer. | Invented guest, veiled, never mocked (`episodes/S1E01_THE_RIBBON_CLAUSE.md` L5, L70). Any further direction: GAP A13. | GAP A13 |
| The councils | Episode only: "Untie it. Keep her." (L32). Not in the trailer. | Twelve masks, silhouettes and seals (`00_FIDELITY_PROTOCOL.md` rule 6). One voice or several: GAP A13. | GAP A13 |

**Casting rules**

- A human performer whose agreement covers this use. No celebrity, no impression of a real person, no "sounds like" brief (`00_FIDELITY_PROTOCOL.md` rules 4 and 6).
- AI or library voice on a plan whose terms page grants commercial use, logged in the ledger. No cloned voice of a real person. Whether Sherif wants AI voice at all: GAP A14.
- Lines read verbatim from canon, character for character. No ad-libs, no new lines.
- **Recording spec:** WAV 48 kHz / 24-bit, mono, dry (no reverb or music printed), one file per line, at least three takes, a quiet treated room. File names use the shot and line ID, not the performer's name.

### 5.2 SFX

- **Scope (S1E01).** Room tone plus the three staged actions only: the scroll into the hopper, the cards landing in the tray, the token set on the chair (`screen/S1E01/GAP_RULINGS.md` G5 C). No trailer hits, risers or whooshes (`docs/TRAILER_S1E01.md` §0). No machine hiccup.
- **Do-nots by mode** (`06_MUSIC_SPEC.md` §2): no lab-equipment foley presented as a procedure (Lab Night); no modem or keyboard foley (Quiet Board); no gunplay or spy-gadget stings (Suave Hour).
- **Sources, any of:** recorded foley; free libraries from §2.4 (Sonniss bundle, Freesound CC0 or CC BY, Kenney, Mixkit SFX, Pixabay, OpenGameArt); the SFX catalogue of a subscription in §2.4; AI SFX on a paid plan whose terms cover films and trailers (`docs/AUDIO_RND.md` §3, ElevenLabs Sound Effects row). Each library SFX gets a ledger row. The Sonniss licence bars AI training with its sounds.
- **Tonal SFX** (blips, card tones) are tuned to A4 = 432. The fixed stingers are music, not SFX, and are never rebuilt from library sounds.
- **Format:** WAV 48 kHz / 24-bit.

### 5.3 Mix and master

- Dialogue first when lines are spoken. Music and SFX sit under the line.
- Drone mono below 120 Hz, low-passed around 150–200 Hz. 54 Hz only in siege, always doubled at 108 Hz or higher (`06_MUSIC_SPEC.md` §3.3).
- No stem at 440 (`06_MUSIC_SPEC.md` §3.1). Licensed tracks are retuned where the licence allows modification; a track that cannot be retuned is GAP A18 (§2.3).
- The fixed stingers and Grounded are placed from their locked files, never regenerated (`docs/AUDIO_RND.md` §6 step 4).
- Check the mix on full-range monitors, headphones, and a phone or laptop speaker.

### 5.4 Loudness targets

From `06_MUSIC_SPEC.md` §3.5. Measured with an ITU-R BS.1770 meter.

| Master | Integrated | True peak | Use |
|---|---|---|---|
| Show / trailer master | −23 LUFS | ≤ −1.0 dBTP | Episodes, trailer, any broadcast-style delivery |
| Streaming / web master | −14 LUFS | ≤ −1.0 dBTP | Only if a platform needs it |

Per-platform targets for each promo and Patreon destination: GAP A15. Re-check each platform's published spec on the day of delivery.

### 5.5 Stems

- **Music stems** (`06_MUSIC_SPEC.md` §3.5): drone, pad, top pad (543), chime (528), rhythm, lead, stingers. All at A4 = 432.
- **Mix stems:** dialogue (DX), music (MX), effects (SFX), room tone (BG).
- **M&E:** music plus effects, no dialogue, for any version that letters the lines instead of voicing them.
- All stems the same length, starting at the same timecode, at 48 kHz / 24-bit.

### 5.6 Deliverables per piece

| Item | Format | Notes |
|---|---|---|
| Full mix, show master | Stereo WAV 48 kHz / 24-bit, −23 LUFS, ≤ −1.0 dBTP | |
| Full mix, web master | Stereo WAV, −14 LUFS, ≤ −1.0 dBTP | Only if needed |
| Mix stems and M&E | WAV 48 kHz / 24-bit | §5.5 |
| Music stems | WAV 48 kHz / 24-bit | §5.5 |
| Cue sheet | Text | Cue ID, in and out timecodes, tier, ledger ID or per-track-log row |
| Ledger rows and per-track-log rows | Text | §2.1 and `06_MUSIC_SPEC.md` §5 |
| Music credits | Text | Every attribution a licence requires, worded as the licence asks, for the end card, description or post |
| Session archive | DAW session plus raw takes | Keeps AI-tool provenance metadata intact (`docs/AUDIO_RND.md` §4.3) |

Picture-side delivery (aspect ratio, frame rate, platform masters): GAP T11 in `docs/TRAILER_S1E01.md`.

**Suggested file name pattern:** `LT_<piece>_<cue>_<stem>_v<nnn>.wav`, for example `LT_S1E01TRL_C01_MX_v001.wav`. A licensed track's working file adds its ledger ID, for example `LT_S1E01TRL_C01_MX_LIC-001_v001.wav`.

---

## 6. Proposed amendment to `06_MUSIC_SPEC.md` §5 — PROPOSED — NOT APPLIED

**Status: PROPOSED. Not applied.** `06_MUSIC_SPEC.md` is unchanged by this card. Applying this text needs a council ruling and Steward sign-off on `06`, in a separate card. It is written to match Sherif's 2026-10-14 directive and Wild's #83 ruling 1 ("AUDIO-PLAN-1 amends §5 with the ledger").

**Bullets it replaces** (`06_MUSIC_SPEC.md` §5, current text): "Original compositions only.", "No samples", "No soundalikes.", "No names.", "AI music tools" and "Temp tracks". The "Sung words" bullet and the per-track log template stay as they are.

**Proposed replacement:**

> - **Sources (Sherif, 2026-10-14).** Music may be original, made by the Steward, or licensed. Licensed music that is legally usable for free or at low cost is approved for temp, promo and the final cut, including CC0, no-attribution libraries, CC-BY with attribution, and royalty-free subscriptions. Original cues composed for Living Thunder are owned by AlphaProMega Media Inc. (see `LICENSE`).
> - **The check.** Every licensed track needs a verified licence page that covers the use and a row in the license ledger (`docs/AUDIO_PLAN.md` §2). That is enough. No separate written sync licence is needed when the licence page already grants commercial use.
> - **Attribution.** When a licence requires credit, give it as the licence asks, in the credits, description or post. Credits may name licensed creators for that purpose.
> - **No infringement.** Nothing is used without a licence that covers the use. No samples of commercial recordings and no loops outside their licence terms.
> - **No named-artist imitation prompts.** No AI prompt or brief names an artist, band, label or track, or asks for "like X". Describe music in craft terms only: tempo, key, instrumentation, texture.
> - **AI music tools** are used on plans whose terms page grants commercial use of the output. Each AI-assisted cue gets a log row.
> - **No purchases by bots.** Only a human buys a plan, licence or subscription.
> - **Fixed house assets.** "Blocked.", "That one can live." and the Grounded motif stay the house files, reused unchanged (§1). Licensed tracks may fill any other cue, including C01, C02 and C08 in the S1E01 trailer.

**What the amendment would not change.** §1 (genre palette and fixed stingers), §2 (cue styles), §3 (tuning, including A4 = 432), §4 (honesty), the sung-words rule and the per-track log template.

**Open before ratification:** whether C06, C09 and C10 should also open to licensed tracks (GAP A17); what to do with a track whose licence does not allow retuning to 432 (GAP A18).

---

## 7. Follow-ups (not done here) — PROPOSED — pending council ratification

**Clerk's #82 nits** (votes comment on PR #82, 6177605018: "Non-blocking nits, banked"):

1. **Reword `docs/AUDIO_RND.md` L3.** Change "Sherif GO, 2026-10-14." to "Sherif GO to research, 2026-10-14." A separate one-line card. This file does not edit `docs/AUDIO_RND.md`.
2. **Re-verify vendor facts at purchase.** Before any account, plan or licence is bought (by a human; no bot purchases), re-read `docs/AUDIO_RND.md` §3 and §4 vendor facts, and §2.4 of this file, on the purchase date. Record the terms, tier and date in the ledger or per-track log. This also carries Wild's #82 note: "before any paid release, confirm the commercial-use license terms for the chosen tool (Stable Audio or Suno), and keep Sherif's 432 Hz synthwave spec as the reference."

**Related follow-ups, owned by other cards:**

3. Trailer follow-up slice for Wild #83 rulings 2 and 3: add S29 and a 2–4 s title card in `docs/TRAILER_S1E01.md`. The title card text waits on GAP T1 and must not invent copy.
4. A `06` amendment card to apply §6, if the council ratifies it.
5. Once Sherif sends the track list (GAP T14), fill ledger rows.

---

## 8. Gaps (flagged, never filled) — PROPOSED — pending council ratification

| ID | Gap | Needs |
|---|---|---|
| A1–A4, A8, A16 | Closed by Sherif's 2026-10-14 directive: Sherif-made and licensed tracks may go in the final cut; ledger rows may carry URLs and names; CC-BY with attribution is approved; vocals are fine in promos; the playlist link is a human reference; no promo-versus-final boundary is needed | Council records the directive |
| A5 | Off-YouTube use of YouTube Audio Library tracks | Read the in-Studio licence text; Sherif |
| A6 | Libraries not read for this card | A new dated read per library |
| A7 | Playlist style traits confirmed by ear, and any tempo reading | Sherif |
| A9 | Music under the trailer title card | Sherif's pick, any tier |
| A10 | Series intro and outro themes | Council ruling; composer |
| A11 | Comic promo bed (E01 has no cue; lead mode D3 open) | Council ruling |
| A12 | Patreon audio, and the platform's music rules on the day of posting | Sherif |
| A13 | Voice casting and direction for Ra-Thor, the Ribbon Envoy and the councils | Council ruling on T4; casting by Sherif |
| A14 | Whether AI or synthetic voice is allowed | Council ruling |
| A15 | Per-platform loudness targets for promos and Patreon | Read on the day of delivery |
| A17 | Whether C06, C09 and C10 (the fixed house stingers and motif) should also open to licensed tracks. The directive names only C01, C02 and C08. | Sherif |
| A18 | A licensed track whose licence does not allow retuning to A4 = 432 | Sherif |
| A19 | Whether paid subscription plans (Uppbeat, Epidemic Sound, Artlist) require attribution | A human reads the plan terms before buying |
| T1, T4, T5, T11, T13, T14 | Carried from `docs/TRAILER_S1E01.md` §6 | As listed there |

## 9. Decisions for Sherif or the council

1. Record Sherif's 2026-10-14 directive against Wild's #83 ruling 1 (§0, §1).
2. Ratify the tier order, the lean ledger, the X-post rule and the status values (§1, §2).
3. Confirm or cut the library and subscription candidates (§2.4). No purchase follows from this list; a human buys anything Sherif picks.
4. Confirm the playlist traits by ear (§3; GAP A7).
5. Ratify the cue maps (§4) and the specs (§5).
6. Rule the §6 amendment, and open a `06` card if it passes.
7. Answer GAP A17 and A18.
8. Send the track list (GAP T14).

## 10. Sources

Read on **2026-10-14** unless a line says otherwise.

- `00_FIDELITY_PROTOCOL.md`; `bots/GROKBOT_COMIC_SEAT.md`; `06_MUSIC_SPEC.md` §1–§6; `09_CHARACTER_BIBLE.md` (Ra-Thor voice).
- `docs/AUDIO_RND.md` (#82); `docs/TRAILER_S1E01.md` (#83); `screen/S1E01/SCORE_PLAN.md`; `screen/S1E01/SHOT_LIST.md` (S29); `episodes/S1E01_THE_RIBBON_CLAUSE.md` (L5, L18, L32, L70).
- `production/ISSUE_01/ISSUE_01_PRODUCTION.md` §10 (Kindle and Patreon exports), §11 D3, §12 item 11; `docs/SHIP_READINESS_AUDIT.md`; `production/README.md` rule 6; `seasons/S2_SEASON_SHEET.md` §5 item 8.
- Sherif directive, 2026-10-14 4:52 PM ET, as relayed on the card.
- PR #83 comment 6178168603 (Wild's rulings) and the #83 votes comment 6178194358 (Hands' sync-licence note). PR #82 comments 6177589865 (Wild's note) and 6177605018 (Clerk's nits).
- Playlist page, metadata only: https://music.youtube.com/playlist?list=PLVTpZcM10F04 .
- Licence pages: https://pixabay.com/service/license-summary/ ; https://pixabay.com/service/faq/ ; https://mixkit.co/license/ ; https://mixkit.co/license/modal/musicFree/ ; https://mixkit.co/license/modal/sfxFree/ ; https://mixkit.co/free-stock-music/ ; https://mixkit.co/terms/ ; https://support.google.com/youtube/answer/3376882 ; https://freesound.org/help/faq/ ; https://sonniss.com/gdc-bundle-license/ ; https://kenney.nl/support ; https://opengameart.org/content/faq ; https://freemusicarchive.org/License_Guide ; https://openverse.org/about ; https://creativecommons.org/publicdomain/zero/1.0/ .
- Subscription pages (Uppbeat and Artlist through search extracts): https://uppbeat.io/user-agreement ; https://uppbeat.io/uppbeat-basic-license ; https://uppbeat.io/pricing ; https://www.epidemicsound.com/pricing/ ; https://www.epidemicsound.com/filmmaking/ ; https://www.epidemicsound.com/how-it-works/license-music-legally/ ; https://help-center.artlist.io/help-center/privacy-terms/artlist-license/ ; https://help.artlist.io/hc/en-us/articles/7856595463581-Using-the-assets-in-a-film ; https://artlist.zendesk.com/hc/en-us/articles/6185461392029-Commercial-projects-and-advertising .

## 11. What this file did not do

- It edited no other file, including `06_MUSIC_SPEC.md`, `docs/AUDIO_RND.md` and `docs/TRAILER_S1E01.md`.
- It made no purchase, signed up for nothing, published nothing, and quotes no price.
- It named no individual track, artist, band, label, channel or show, and entered no ledger row.
- It wrote no AI prompt, no lyric, no line and no title-card copy, and it filled no gap.
