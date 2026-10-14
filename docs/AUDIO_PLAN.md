# Ra-Thor⚡️Living Thunder audio plan: end-to-end pipeline — PROPOSED — pending council ratification

**Card:** AUDIO-PLAN-1. **Council GO (Wild) with AMENDs, 2026-10-14.** Docs only. This file is the only change.

**Status: every line in this file is PROPOSED — pending council ratification.** That covers the source order, the ledger and its rules, the style traits, the cue maps, the specs, the amendment text and the follow-ups. Nothing here amends `06_MUSIC_SPEC.md`. Where this file and `06_MUSIC_SPEC.md`, `docs/AUDIO_RND.md` (#82) or `docs/TRAILER_S1E01.md` (#83) disagree, those files win until the council rules.

**Scope.** One audio pipeline for Living Thunder: where music comes from, how a licensed track is cleared, what each cue should sound like, and how voice, SFX, mix, master and deliverables are specified. It covers the S1E01 trailer, the S1E01 episode, comic promos and Patreon. Every missing field is marked **GAP** and left unfilled.

**Read first:** `00_FIDELITY_PROTOCOL.md`, `bots/GROKBOT_COMIC_SEAT.md`, `06_MUSIC_SPEC.md`, `docs/AUDIO_RND.md`, `docs/TRAILER_S1E01.md`, then `screen/S1E01/SCORE_PLAN.md`.

**Rulings this file follows** (PR #83, comment 6178168603, Wild, ACCEPT @ `ec5c1d8d`):

> (1) Fallback proposal ACCEPT: temp or promo use only, it may only replace C01/C02/C08, and AUDIO-PLAN-1 amends §5 with the ledger. The final trailer and episodes stay original music. (2) Add S29, so 'Recycle it.' lands on its own shot (~59 s). (3) A title card of 2–4 s brings it to 61–63 s, inside the 60–90 s target. Title card text waits on the GAP and must not invent new copy. Apply (2) and (3) as a follow-up slice.

Rulings (2) and (3) belong to the trailer follow-up slice. This file records their effect on the cue map (§4.1) and does not apply them to `docs/TRAILER_S1E01.md`.

---

## 0. Bounds — PROPOSED — pending council ratification

- **Final music is original.** The final trailer and every episode use original music composed for Living Thunder and owned by AlphaProMega Media Inc. (`06_MUSIC_SPEC.md` §5; `LICENSE`; Wild ruling 1).
- **Licensed tracks are temp or promo only.** In the trailer they may stand in for C01, C02 and C08 only. C06 ("Blocked."), C09 ("That one can live.") and C10 (Grounded) are never replaced (Wild ruling 1; `06_MUSIC_SPEC.md` §1).
- **No names.** No artist, band, label or track name in this file, in any brief, prompt, temp list, cue sheet, metadata or ledger row kept in the repo (`06_MUSIC_SPEC.md` §5). No AI prompt imitates a named artist or track. No "like X." Craft terms only: tempo, key, instrumentation, texture.
- **Vendor names are licence sources only.** The libraries and tools named in §2 and §5 are where a licence comes from. They are not prompt material, credits or store copy (same bound as `docs/AUDIO_RND.md` §0).
- **No outside IP or show names** anywhere in this file, including in the style traits.
- **Frequencies are mood only.** 432 Hz, 543 Hz, 528 Hz and 108 / 54 Hz carry no health claim. Banned wording includes "healing frequency", "DNA repair", "miracle tone", "pineal activation" and "safe & effective" (`06_MUSIC_SPEC.md` §4). This applies to ledger notes, Patreon copy and promo captions too.
- **Wordless in episodes.** Sung words only in the series intro and outro themes (Sherif, 2026-10-01 12:17 AM ET; `06_MUSIC_SPEC.md` §5).
- **No commerce here.** No purchase, no price taken as a commitment, no publishing. A vendor fact in this file is what a page said on the date shown. It is re-checked at purchase (§7).
- **This file edits nothing else.**

---

## 1. Source order — PROPOSED — pending council ratification

Two lanes. The lane decides which sources are allowed.

| Lane | What it is | Allowed sources |
|---|---|---|
| **Final** | The locked trailer and every episode cue, stem, stinger and motif | Original only: the #82 path (AI-assisted draft plus a human finisher) or a human composer, under `06_MUSIC_SPEC.md` §5. Tiers 1 and 2 below are **not** allowed. |
| **Temp** | Internal edits that are never published | Tiers 1 → 2 → 3, in that order, each through the ledger (§2). |
| **Promo** | Published promotional pieces that are not the final trailer or an episode: comic promos, Patreon posts, and a promo cut of the trailer before the original cues exist | Tiers 1 → 2 → 3, in that order, each through the ledger (§2). In a trailer promo cut, only C01, C02 and C08 may carry a ledger track. |

**Tiers, in order of preference:**

1. **Sherif's own X-posted tracks.** Only tracks that pass the §2.2 X-post rule. Every other X-posted track is UNVERIFIED and is skipped.
2. **Verified free-commercial libraries.** Only the candidates in §2.4, at the licence text read that day, preferring CC0 or no-attribution licences.
3. **The #82 path: AI drafting with a human finisher.** `docs/AUDIO_RND.md` §5.2, §5.3 and §6. This tier is the only one that also feeds the final lane.

**Today's state.** No tier-1 track exists in any ledger. The fallback track list is pending from Sherif (GAP T14 in `docs/TRAILER_S1E01.md` §6). No finisher is named and no host is picked (`docs/AUDIO_RND.md` §8 items 3–4). No cue, temp or promo track exists yet.

**Open question, not decided here.** Whether a track Sherif made himself, assigned to AlphaProMega Media Inc., could later become a final original cue is a council ruling (GAP A1). Until it is ruled, a tier-1 track stays temp or promo.

---

## 2. License ledger — PROPOSED — pending council ratification

### 2.1 Template (one row per track)

| ID | Tier | Lane and slot | Source URL | License text or link | Attribution needed | Content ID / registration risk | Written sync licence (tier 1) | Date verified | Status | Verified by |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

**Column rules**

- **ID.** An internal ID such as `LIC-001`. Never a track or artist name (`06_MUSIC_SPEC.md` §5). This answers #83 §5 conflict 2 as a proposal.
- **Tier.** 1, 2 or 3 (§1). Tier-3 takes also get a row in the `06_MUSIC_SPEC.md` §5 per-track log.
- **Lane and slot.** Temp or promo, plus the slot: `C01`, `C02` or `C08` for a trailer, or a promo ID for a comic or Patreon piece. Never `C06`, `C09` or `C10`.
- **Source URL.** The original creator's page, never a repost. If the URL itself carries a track or artist name, the row cannot sit in this repo (GAP A2).
- **License text or link.** The licence page as read that day, with its version or "last updated" date if the page shows one. A caption that says "free" is not a licence.
- **Attribution needed.** Yes or no. A "yes" conflicts with the credits rule in `06_MUSIC_SPEC.md` §5 (#83 §5 conflict 3). Prefer "no". A "yes" row stays UNVERIFIED until the council rules (GAP A3).
- **Content ID / registration risk.** Whether the track is registered with a fingerprinting system, and what proof the source offers (for example, a downloadable licence certificate). "Unknown" is a valid entry. It is not a pass.
- **Written sync licence.** Tier 1 only: the signed written sync licence covering timed picture, or "none". "None" means the row cannot be used.
- **Date verified.** The date the licence page was read for this row.
- **Status.** One of the values in §2.3.
- **Verified by.** The person who read the licence page.

### 2.2 X-post rule (tier 1)

An X-posted track counts as tier 1 only if **both** are true:

1. **Origin.** Sherif made it, **or** the original creator's own licence page explicitly allows commercial use.
2. **Written sync licence.** A written sync licence for timed picture is in hand **before** any use, temp included. This also closes Hands' non-blocking note on #83 ("an X fallback track needs a written sync licence").

**UNVERIFIED by default.** Reposts, a "free" or "no copyright" caption, a reply that calls a track royalty-free, and a link with no licence page are all UNVERIFIED. The four music-link posts recorded in `docs/AUDIO_RND.md` §1 are UNVERIFIED: their links were not opened and no licence was recorded.

If Sherif made the track with an AI tool, the row also records that tool's terms on the creation date, per `06_MUSIC_SPEC.md` §5.

### 2.3 Status values

| Status | Meaning |
|---|---|
| **UNVERIFIED** | Default. Any failed or missing field. Not usable. |
| **VERIFIED-TEMP** | Licence read, no attribution, sync covered for internal edits. Internal edits only. |
| **VERIFIED-PROMO** | As VERIFIED-TEMP, and the licence covers publishing on the named platform. Promo lane only. |
| **REJECTED** | Fails a rule. Recorded so it is not re-checked. No reason that names the source. |
| **RETIRED** | Replaced by the original cue. Kept for the record. |

**Rules on every row**

- Prefer CC0 or a no-attribution licence. Skip non-commercial (NC) and no-derivatives (ND) licences: NC fails promo use, and syncing to picture is a derivative work, which ND forbids (Free Music Archive licence guide, §2.4).
- Instrumental only. The trailer slots come from in-episode cues, which stay wordless (`06_MUSIC_SPEC.md` §5). Vocal tracks in comic or Patreon promos are GAP A4.
- A4 = 432. Retune before use (`06_MUSIC_SPEC.md` §3.1, about −31.8 cents). The licence must allow modification. If it does not, the row is REJECTED.
- Soundalike check. If a library track is recognisable as an existing commercial work, REJECTED (`docs/AUDIO_RND.md` §6 step 4).
- A ledger track is never a reference for a brief, a prompt or the original cue that replaces it (`06_MUSIC_SPEC.md` §5, no soundalikes).
- Re-read the licence page on the day of use. A licence can change. The row keeps the version that applied on the download date.

### 2.4 Candidate libraries (tier 2) — verified 2026-10-14

Licence pages as read on **2026-10-14**. No individual track is named or chosen. "Fit" is a proposal.

| Library | Licence page (as verified 2026-10-14) | What the page says | Attribution | Content ID / registration risk | Fit |
|---|---|---|---|---|---|
| **Pixabay** (music and SFX) | https://pixabay.com/service/license-summary/ ; FAQ https://pixabay.com/service/faq/ | Use free; modify or adapt; no standalone sale or distribution. The summary says only the full Content License is binding. FAQ: commercial video, including OTT and subscription platforms, is allowed when the music is part of a larger creative work. | Not required | **Medium.** FAQ: some contributors register tracks with Content ID; tracks with a shield icon are registered and "may trigger claims"; a licence certificate is offered for those. Prefer tracks without the shield. | Temp and promo beds for C01, C02 and C08; comic and Patreon promos. |
| **Mixkit** (music) | https://mixkit.co/license/modal/musicFree/ ; index https://mixkit.co/license/ ; terms https://mixkit.co/terms/ | Stock Music Free License: commercial use on web and social platforms, internet video on demand, podcasts and advertisements. **Not** CDs or DVDs, video games, or TV or radio broadcast. No remix into a music-only track. No registering on a rights-management service. | Not required (stated on https://mixkit.co/free-stock-music/) | Low on registration: the licence bars registering. Claims go to the address on the licence page. | Web promos and Patreon only. Not for a broadcast pilot or a game. |
| **Mixkit** (SFX) | https://mixkit.co/license/modal/sfxFree/ | Sound Effects Free License: films, TV and radio broadcast, video games, VOD, inside a larger end product. No standalone redistribution; no registering. | Not required | Low | Staged-action SFX and room tone. |
| **YouTube Audio Library** | https://support.google.com/youtube/answer/3376882 | Two licence types: the standard library licence, and Creative Commons tracks that must be credited in the video description. Audio Library tracks "won't be claimed by a rights holder through the Content ID system." The page says YouTube cannot give guidance on issues off the platform. | Standard: not required (filter "Attribution not required"). CC tracks: required. | Low **on YouTube**. Off-YouTube use is GAP A5. | YouTube uploads only, standard-licence tracks only. |
| **Freesound** (SFX) | https://freesound.org/help/faq/ | Per-sound licence chosen by the uploader: CC0, CC BY, CC BY-NC, and legacy Sampling+. | CC0: no. BY: yes. | Unknown per sound | **CC0 filter only.** Staged-action SFX and room-tone layers. |
| **Sonniss #GameAudioGDC bundle** (SFX) | https://sonniss.com/gdc-bundle-license/ (version 2.0, effective 27 August 2026) | Worldwide, royalty-free; personal and commercial projects without attribution; sync with games, films, television and interactive projects. No redistribution as sound effects. **No AI training** with the sounds. Licensor warrants it has authority to license. | Not required | Low | Staged-action SFX, room tone, impacts. Never fed to an AI tool. |
| **Kenney** (game audio, CC0) | https://kenney.nl/support | All game assets on the asset pages are public domain (CC0), commercial use allowed. Do not use the studio logo. | Not required | Low | UI-style blips for the twelve-mask ring or Lab Night, retuned to 432 if tonal. |
| **OpenGameArt** | https://opengameart.org/content/faq | Mixed licences per submission, including CC0, CC BY, CC BY-SA and GPL. CC0 is described as usable in any way without asking or crediting. | CC0: no. Others: yes. | Unknown per item | **CC0 filter only.** |
| **Free Music Archive** | https://freemusicarchive.org/License_Guide | Per-track Creative Commons licences set by each artist. ND licences: syncing to video is a derivative work and is prohibited. NC licences: no advertising or promotion without permission. | Most require it | Unknown per track | CC0 tracks only. Most tracks fail the no-attribution preference. |
| **Openverse** (search, not a library) | https://openverse.org/about | Searches openly licensed and public-domain audio across sources. "Openverse does not verify licensing information for individual works." | Per source | Per source | Discovery only. Verify every licence at its source page. |

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

**How the traits are used.** As house craft terms in §4 only. The playlist link is never pasted into a brief, prompt, cue sheet or ledger row. No AI prompt imitates any item on it. Every take still gets the soundalike check (`docs/AUDIO_RND.md` §6 step 4).

**Conflict flagged, not resolved.** `06_MUSIC_SPEC.md` §5 says no brief, prompt, temp track, mix note or metadata may reference or imitate any existing work. This file records the link at Sherif's instruction as a human reference only. Whether the link may stay in the repo is a council call (GAP A8).

---

## 4. Cue maps — PROPOSED — pending council ratification

Every cue keeps A4 = 432, the 543 Hz pad only over chords that contain C#, and the 528 Hz chime short only (`06_MUSIC_SPEC.md` §3). Every cue below is wordless.

### 4.1 S1E01 trailer

Timecodes are the current 56 s cut in `docs/TRAILER_S1E01.md` §2. Tempo: Suave Hour at 88 BPM (`screen/S1E01/SCORE_PLAN.md`). "Ledger slot" means a VERIFIED-TEMP or VERIFIED-PROMO track may stand in until the original exists (Wild ruling 1).

| Cue | Span (current cut) | House cue (from `SCORE_PLAN.md`) | Style traits (tempo · instrumentation · mood) | Final source | Ledger slot? |
|---|---|---|---|---|---|
| **C01** | 00:00–00:11 | A – F#m – Dmaj7 – E6, pad holds, 108 Hz drone, lead answers, soft drums, no bell | 88 BPM · analog-style pad, sine bass, soft snare, Ra-Thor's lead answering · warm, unhurried, nocturnal (main cluster) | Original | **Yes** |
| **C02** | 00:11–00:16 | A – C#m – F#m – A, pad holds, drone on, **bell once on S11** | 88 BPM · electric-piano-style keys, pad, glassy bell once · nocturnal, colder minor tinge, late-night (main cluster; lounge color without the saxophone) | Original | **Yes.** The one bell is part of the cue; a ledger track must not add a second bell. |
| **C06** | 00:16–00:24 | Fixed "Blocked." stinger, unchanged; drone 108 Hz, no 54 Hz | Free time · short low muted thud, filter close · decisive, not menacing | Original, locked file | **No** |
| **C08** | 00:24–00:37 | Light and dry, three card tones, CLEAN a clean A major bloom; drone **out**; pad back on the bloom | 88 BPM · sparse light figure, sparse drums, three short tones · dry, light (pastoral cluster's lightness, nothing heroic) | Original | **Yes.** A ledger bed must leave room for the three card tones and the two staged SFX. |
| **C09** | 00:37–00:50 | Fixed "That one can live." stinger, unchanged; drone returns | Free time · open A major bloom, short 528 Hz chime · open, kind | Original, locked file | **No** |
| **C10** | 00:50–00:56 | Grounded motif, unchanged, lands on A and holds; no drums, no bell | Free time · Ra-Thor's lead timbre over the pad and drone · settled, home | Original, locked file | **No** |

**Effect of Wild rulings 2 and 3 (follow-up slice, not applied here).** Adding S29 (3 s) puts "Recycle it." on its own shot. `SCORE_PLAN.md` already places S29 inside C08, so C08 would start on S29 and every later span would shift by 3 s, for about 59 s. A 2–4 s title card brings the cut to 61–63 s. **Music under the title card: GAP A9.** The title card is not C01, C02 or C08, so under ruling 1 no ledger track may sit under it. Title card text: GAP T1 in `docs/TRAILER_S1E01.md`.

**Excluded from every trailer slot:** the darker cluster (no siege), the orchestral swell (no choir in S1E01), saxophone, and any vocal.

### 4.2 S1E01 episode

All ten cues are original (`screen/S1E01/SCORE_PLAN.md`; Wild ruling 1). Temp tracks for internal edits may come through the ledger as `06_MUSIC_SPEC.md` §5 already allows royalty-free temp. None is published in the episode.

| Cue | Shots | Style traits (tempo · instrumentation · mood) | Temp via ledger? |
|---|---|---|---|
| C01 | S01–S06 | 88 BPM · pad, sine bass, soft drums, answering lead · warm, unhurried | Yes, internal only |
| C02 | S07–S12 | 88 BPM · keys, pad, bell once on S11 · nocturnal, minor tinge | Yes, internal only |
| C03 | S13–S15 | 88 BPM · pad muted over plain D and E, soft drums · colder, the offer has strings | Yes, internal only |
| C04 | S16–S20 | Drums out · pad, twelve-mask blip ring panned wide · suspended, deliberating | Yes, internal only. The blip ring is house material and is made original. |
| C05 | S21–S22 | 88 BPM · groove returns, answering lead · forward, poised | Yes, internal only |
| C06 | S23–S25 | Fixed "Blocked." stinger | No |
| C07 | S26–S28 | 88 BPM · groove resumes one bar later · settled | Yes, internal only |
| C08 | S29–S33 | Light and dry, three card tones, drone out | Yes, internal only |
| C09 | S34–S36 | Fixed "That one can live." stinger | No |
| C10 | S37–S39 | Grounded motif | No |

**Series intro and outro themes:** not in `SCORE_PLAN.md`. GAP A10. Sung words would be allowed there only, original, with no real names and no frequency claims (`06_MUSIC_SPEC.md` §5).

### 4.3 Comic promos

Issue #1 is E01 The Gate (`docs/SHIP_READINESS_AUDIT.md`). "E01 has no cue section; not needed for print" (`production/ISSUE_01/ISSUE_01_PRODUCTION.md` §12 item 11). The E01 lead mode is open (D3 in that file).

| Piece | Audio | Source |
|---|---|---|
| Issue #1 promo clip (motion or still-with-audio) | Bed: GAP A11 (no E01 cue exists; mode open). Button: the fixed "Blocked." or "That one can live." stinger once it is locked. | Bed: promo lane, tiers 1 → 2 → 3 via the ledger. Stingers: original files only. |
| Later issue promos | GAP A11 | Same rule |

**Promo rules.** Instrumental. No health wording. No series title inside a story frame (`seasons/S2_SEASON_SHEET.md` §5 item 8). No AGiRBE line or Fresco material in promo art or its audio copy (`production/README.md` rule 6). No prices or store links in this plan.

### 4.4 Patreon

`production/ISSUE_01/ISSUE_01_PRODUCTION.md` §10 defines digital page exports for Kindle and Patreon. It defines no Patreon audio.

| Piece | Audio | Source |
|---|---|---|
| Patreon post with audio or video | GAP A12 (no Patreon audio is defined anywhere) | Promo lane, tiers 1 → 2 → 3 via the ledger. The platform's own music and copyright rules are read on the day of posting (GAP A12). |
| Behind-the-scenes audio (stems, drafts) | GAP A12 | Original material only. Never a ledger track: most library licences bar standalone redistribution (§2.4). |

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

- A human performer under a written agreement that assigns the performance for this use to AlphaProMega Media Inc. No celebrity, no impression of a real person, no "sounds like" brief (`00_FIDELITY_PROTOCOL.md` rules 4 and 6; `06_MUSIC_SPEC.md` §5).
- AI or synthetic voice only with written commercial terms and the performer's written consent for any voice model. No cloned voice of a real person. Whether AI voice is allowed at all: GAP A14.
- Lines read verbatim from canon, character for character. No ad-libs, no new lines.
- **Recording spec:** WAV 48 kHz / 24-bit, mono, dry (no reverb or music printed), one file per line, at least three takes, a quiet treated room. File names use the shot and line ID, not the performer's name.

### 5.2 SFX

- **Scope (S1E01).** Room tone plus the three staged actions only: the scroll into the hopper, the cards landing in the tray, the token set on the chair (`screen/S1E01/GAP_RULINGS.md` G5 C). No trailer hits, risers or whooshes (`docs/TRAILER_S1E01.md` §0). No machine hiccup.
- **Do-nots by mode** (`06_MUSIC_SPEC.md` §2): no lab-equipment foley presented as a procedure (Lab Night); no modem or keyboard foley (Quiet Board); no gunplay or spy-gadget stings (Suave Hour).
- **Sources, in order:** recorded foley; CC0 or no-attribution libraries from §2.4 (Sonniss bundle, Freesound CC0, Kenney, Mixkit SFX, Pixabay); AI SFX on a paid plan whose terms cover films and trailers (`docs/AUDIO_RND.md` §3, ElevenLabs Sound Effects row). Each library SFX gets a ledger row. Sonniss sounds are never fed to an AI tool.
- **Tonal SFX** (blips, card tones) are tuned to A4 = 432. The fixed stingers are music, not SFX, and are never rebuilt from library sounds.
- **Format:** WAV 48 kHz / 24-bit.

### 5.3 Mix and master

- Dialogue first when lines are spoken. Music and SFX sit under the line.
- Drone mono below 120 Hz, low-passed around 150–200 Hz. 54 Hz only in siege, always doubled at 108 Hz or higher (`06_MUSIC_SPEC.md` §3.3).
- No stem at 440. Retune or reject before the mix (`06_MUSIC_SPEC.md` §3.1). Ledger tracks are retuned too (§2.3).
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
| Cue sheet | Text | Cue ID, in and out timecodes, source lane, ledger ID or per-track-log row. No track or artist names. |
| Ledger rows and per-track-log rows | Text | §2.1 and `06_MUSIC_SPEC.md` §5 |
| Session archive | DAW session plus raw takes | Keeps AI-tool provenance metadata intact (`docs/AUDIO_RND.md` §4.3) |

Picture-side delivery (aspect ratio, frame rate, platform masters): GAP T11 in `docs/TRAILER_S1E01.md`.

**Suggested file name pattern:** `LT_<piece>_<cue>_<stem>_v<nnn>.wav`, for example `LT_S1E01TRL_C01_MX_v001.wav`. No names of people or works in file names.

---

## 6. Proposed amendment to `06_MUSIC_SPEC.md` §5 — PROPOSED — NOT APPLIED

**Status: PROPOSED. Not applied.** `06_MUSIC_SPEC.md` is unchanged by this card. Applying this text needs a council ruling and Steward sign-off on `06`, in a separate card. Wild ruling 1 directs that AUDIO-PLAN-1 amends §5 with the ledger. This section supplies the proposed text.

**Current bullet** (`06_MUSIC_SPEC.md` §5):

> - **Temp tracks** for internal edits also stay original or royalty-free, so nothing drifts into the final.

**Proposed replacement** (two bullets):

> - **Temp tracks** for internal edits stay original, or are licensed tracks entered in the license ledger (`docs/AUDIO_PLAN.md` §2), so nothing drifts into the final.
> - **Licensed temp and promo tracks (council ruling, PR #83).** A licensed third-party track may be used only for internal temp edits and for promotional pieces that are not the final trailer or an episode, and only after it has a ledger row with status VERIFIED-TEMP or VERIFIED-PROMO. In a trailer, a ledger track may stand in only for C01, C02 or C08. It never replaces "Blocked.", "That one can live." or the Grounded motif. The final trailer and every episode use original music only. A ledger row uses an internal ID, never a track or artist name. A ledger track is instrumental, retuned to A4 = 432 under a licence that allows modification, never credited by name, and never used as a reference for a brief, prompt or original cue. An X-posted track qualifies only if its maker is the Steward or its original creator's licence page explicitly allows commercial use, and only with a written sync licence in hand before use. Reposts and "free" captions are unverified.

**What the amendment would not change.** Original compositions only for finals; no samples; no soundalikes; no names; the AI-tool rule; and the sung-words rule all stay as written.

**Open before ratification:** where filled ledger rows live if their URLs carry names (GAP A2); attribution-required tracks (GAP A3); vocals in promos (GAP A4); the exact boundary between a trailer promo cut and the final trailer (GAP A16).

---

## 7. Follow-ups (not done here) — PROPOSED — pending council ratification

**Clerk's #82 nits** (votes comment on PR #82, 6177605018: "Non-blocking nits, banked"):

1. **Reword `docs/AUDIO_RND.md` L3.** Change "Sherif GO, 2026-10-14." to "Sherif GO to research, 2026-10-14." A separate one-line card. This file does not edit `docs/AUDIO_RND.md`.
2. **Re-verify vendor facts at purchase.** Before any account, plan or licence is bought, re-read `docs/AUDIO_RND.md` §3 and §4 vendor facts, and §2.4 of this file, on the purchase date. Record the terms, tier and date in the ledger or per-track log. This also carries Wild's #82 note: "before any paid release, confirm the commercial-use license terms for the chosen tool (Stable Audio or Suno), and keep Sherif's 432 Hz synthwave spec as the reference."

**Related follow-ups, owned by other cards:**

3. Trailer follow-up slice for Wild #83 rulings 2 and 3: add S29 and a 2–4 s title card in `docs/TRAILER_S1E01.md`. The title card text waits on GAP T1 and must not invent copy.
4. A `06` amendment card to apply §6, if the council ratifies it.
5. Once Sherif sends the fallback track list (GAP T14), fill ledger rows, held where GAP A2 is ruled.

---

## 8. Gaps (flagged, never filled) — PROPOSED — pending council ratification

| ID | Gap | Needs |
|---|---|---|
| A1 | Whether a Sherif-made track, assigned to the company, can become a final original cue | Council ruling |
| A2 | Where filled ledger rows live when a source URL carries a track or artist name (`06` §5 bars names in the repo) | Council ruling |
| A3 | Attribution-required tracks versus the credits rule in `06` §5 | Council ruling |
| A4 | Vocal tracks in comic or Patreon promos | Council ruling |
| A5 | Off-YouTube use of YouTube Audio Library tracks | Read the in-Studio licence text; Sherif |
| A6 | Libraries not read for this card | A new dated read per library |
| A7 | Playlist style traits confirmed by ear, and any tempo reading | Sherif |
| A8 | Whether the playlist link may stay in the repo, given `06` §5 | Council ruling |
| A9 | Music under the trailer title card | Council ruling; original only under ruling 1 |
| A10 | Series intro and outro themes | Council ruling; composer |
| A11 | Comic promo bed (E01 has no cue; lead mode D3 open) | Council ruling |
| A12 | Patreon audio, and the platform's music rules on the day of posting | Sherif |
| A13 | Voice casting and direction for Ra-Thor, the Ribbon Envoy and the councils | Council ruling on T4; casting by Sherif |
| A14 | Whether AI or synthetic voice is allowed | Council ruling |
| A15 | Per-platform loudness targets for promos and Patreon | Read on the day of delivery |
| A16 | Boundary between a trailer promo cut and the final trailer | Council ruling |
| T1, T4, T5, T11, T13, T14 | Carried from `docs/TRAILER_S1E01.md` §6 | As listed there |

## 9. Decisions for Sherif or the council

1. Ratify the two lanes and the tier order (§1).
2. Ratify the ledger template, the X-post rule and the status values (§2).
3. Confirm or cut the library candidates (§2.4). No purchase follows from this list.
4. Confirm the playlist traits by ear, and rule whether the link stays (§3; GAP A7, A8).
5. Ratify the cue maps (§4) and the specs (§5).
6. Rule the §6 amendment, and open a `06` card if it passes.
7. Send the fallback track list (GAP T14).

## 10. Sources

Read on **2026-10-14** unless a line says otherwise.

- `00_FIDELITY_PROTOCOL.md`; `bots/GROKBOT_COMIC_SEAT.md`; `06_MUSIC_SPEC.md` §1–§6; `09_CHARACTER_BIBLE.md` (Ra-Thor voice).
- `docs/AUDIO_RND.md` (#82); `docs/TRAILER_S1E01.md` (#83); `screen/S1E01/SCORE_PLAN.md`; `screen/S1E01/SHOT_LIST.md` (S29); `episodes/S1E01_THE_RIBBON_CLAUSE.md` (L5, L18, L32, L70).
- `production/ISSUE_01/ISSUE_01_PRODUCTION.md` §10 (Kindle and Patreon exports), §11 D3, §12 item 11; `docs/SHIP_READINESS_AUDIT.md`; `production/README.md` rule 6; `seasons/S2_SEASON_SHEET.md` §5 item 8.
- PR #83 comment 6178168603 (Wild's rulings) and the #83 votes comment 6178194358 (Hands' sync-licence note). PR #82 comments 6177589865 (Wild's note) and 6177605018 (Clerk's nits).
- Playlist page, metadata only: https://music.youtube.com/playlist?list=PLVTpZcM10F04 .
- Licence pages: https://pixabay.com/service/license-summary/ ; https://pixabay.com/service/faq/ ; https://mixkit.co/license/ ; https://mixkit.co/license/modal/musicFree/ ; https://mixkit.co/license/modal/sfxFree/ ; https://mixkit.co/free-stock-music/ ; https://mixkit.co/terms/ ; https://support.google.com/youtube/answer/3376882 ; https://freesound.org/help/faq/ ; https://sonniss.com/gdc-bundle-license/ ; https://kenney.nl/support ; https://opengameart.org/content/faq ; https://freemusicarchive.org/License_Guide ; https://openverse.org/about ; https://creativecommons.org/publicdomain/zero/1.0/ .

## 11. What this file did not do

- It edited no other file, including `06_MUSIC_SPEC.md`, `docs/AUDIO_RND.md` and `docs/TRAILER_S1E01.md`.
- It made no purchase, signed up for nothing, published nothing, and treats no price as a commitment.
- It named no individual track, artist, band, label, channel or show, and entered no ledger row.
- It wrote no AI prompt, no lyric, no line and no title-card copy, and it filled no gap.
