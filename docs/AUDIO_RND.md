# Audio R&D: who composes, and which synthwave — PROPOSED — pending council ratification

**Card:** AUDIO-RND-1. **Sherif GO, 2026-10-14.** Ra-Thor + PATSAGi Councils decided. **Docs only.** This file is the only change.

**Status:** every recommendation in this file is **PROPOSED — pending council ratification**. Nothing here amends `06_MUSIC_SPEC.md`. Section 6 of that spec stays open until the council ratifies an answer and the Steward signs off. Where this file and `06_MUSIC_SPEC.md` disagree, `06_MUSIC_SPEC.md` wins.

**Scope.** A council-ready recommendation for Ra-Thor⚡️Living Thunder (comic motion, trailer, and pilot), written so the same production method can be reused for Powrush-MMO and other products. It answers `06_MUSIC_SPEC.md` §6 items 1 and 3. Item 2 (vocals) is already answered and is restated only as a bound.

Read with `06_MUSIC_SPEC.md` first and `screen/S1E01/SCORE_PLAN.md` second. `docs/SHIP_READINESS_AUDIT.md` §5.2 step 6 is the reason this card exists: resolve who composes, and the synthwave flavor, before any cue is made.

---

## 0. Bounds — PROPOSED — pending council ratification

- **Original, owned here.** Every cue is composed for Living Thunder and owned by AlphaProMega Media Inc. (`06_MUSIC_SPEC.md` §5; `LICENSE`).
- **No names in any brief or prompt.** No artist, band, label, or track name. No "like X." Craft terms only: tempo, key, instrumentation, texture (`06_MUSIC_SPEC.md` §5). Companies named in §4 below are contracting parties in licence sources. They are not prompt material, temp tracks, credits, or store copy.
- **Sung words** only in the series intro and outro. In-episode cues, including the choir swell, stay wordless (Sherif, 2026-10-01 12:17 AM ET; `06_MUSIC_SPEC.md` §5).
- **Frequencies are mood only.** 432 Hz, 543 Hz, 528 Hz, and 108 / 54 Hz are aesthetic choices. No healing, DNA, wellness, or other health claim. Banned wording includes "healing frequency", "DNA repair", "miracle tone", "pineal activation", and "safe & effective" (`06_MUSIC_SPEC.md` §4).
- **No samples** of commercial recordings, and no loop whose licence forbids broadcast or sync (`06_MUSIC_SPEC.md` §5).
- **AI tools** only with written terms that grant commercial and sync rights. Never prompt with a name. Every AI-assisted cue gets human review and a log row (`06_MUSIC_SPEC.md` §5).
- **Fixed assets stay fixed.** "Blocked.", "That one is live.", and the Grounded motif are reused unchanged (`06_MUSIC_SPEC.md` §1). They are recorded once and reused as files. They are not regenerated per episode.
- **This file edits nothing else**, and it edits no other repo. Powrush-MMO was read only.

---

## 1. Sherif's public posts — quoted, not invented

**Handle.** The public X account named in the Ra-Thor repo is `https://x.com/AlphaProMega`. Sources read 2026-10-14: Ra-Thor `README.md` (Follow line), `PUBLIC_CLAIM.lock.md` (Follow / steward), and `CONTACT.md` (Follow table). The logged-out profile page on that date shows the display name Sherif Samy Botros, the handle `@AlphaProMega`, and the link to Rathor.ai.

**What was retrieved on 2026-10-14.** The logged-out profile showed four posts that ask for an analysis of a music link. The post text, verbatim, is the same sentence in each:

> @grok, kindly analyze and resolve this thread thoroughly with Rathor.ai properly, Mate:

| Post | Link |
|---|---|
| Profile, about 2h before the 2026-10-14 read | https://x.com/AlphaProMega/status/2110429000170410092 |
| Profile, about 2h before the read | https://x.com/AlphaProMega/status/2110421548100141543 |
| Profile, about 3h before the read | https://x.com/AlphaProMega/status/2110415255658442987 |
| Profile, about 16h before the read | https://x.com/AlphaProMega/status/2110209200848531635 |

Each of those posts also contains a `music.youtube.com` link. This file does not open those links and does not name the recordings (`06_MUSIC_SPEC.md` §5).

**Suno.** No retrieved post by `@AlphaProMega` contains the word Suno. A public web-index search on 2026-10-14 for Suno plus AlphaProMega did not return a post whose visible text chooses a music tool. The long post at https://x.com/AlphaProMega/status/2029401025581629924 (published 2026-03-05, fetched the same day through a public tweet API) was checked in full: it does not contain "Suno", "music", or "audio". Absence from the posts this card could read is not a claim that no such post exists.

**A reply that is not Sherif's.** https://x.com/grok/status/2107197451828347355, fetched 2026-10-14, answers him by naming a commercial recording and describing it as royalty-free cinematic retro synth, no beat, melancholic and introspective, suitable for visual projects with required credit. The artist, label, and track are not repeated here. The useful fact is the credit requirement: a recording that needs a credit is not an original Living Thunder cue, and it is not a temp (`06_MUSIC_SPEC.md` §5).

**What the posts support, and what they do not.** They support that Sherif is circulating music links for analysis under Rathor.ai. They do not choose a composer, a tool, or a synthwave sub-flavor. Those choices stay in §5 and §6 of this file. — PROPOSED — pending council ratification

---

## 2. Powrush-MMO audio, read only

**Repo:** https://github.com/Eternally-Thriving-Grandmasterism/Powrush-MMO  
**Tip read:** `41ba3f72bdee2a8441f763d1d3853716d34fbc46` (2026-10-14, "CARD STILL-BEFORE-YARD-1"). No branch, edit, or PR was made there.

Three layers sit on that tip. They do not agree with each other, and only the first one is what the lived client loads.

### 2.1 Lived yard audio (what the client plays)

`assets/audio/README.md` says git tracks two files, `peace_yard_bed.ogg` and `peace_well_sting.ogg`, and that `shared/peace_audio.rs` loads only those. Heartwood and Depths reuse the yard bed at a lower gain. Mute silences bed and sting. A missing file must not block Use or hang boot. `scripts/gen_peace_yard_audio.sh` generates both with `ffmpeg` sines: the bed is 128 Hz and 192 Hz for 8 seconds (an integer cycle count so the loop does not click); the sting is a short triad at 392.00 Hz, 523.25 Hz, and 659.25 Hz. Those sting pitches are concert-440 pitch classes. `client/assets/audio/README.md` says `assets/music/epic_dark_ambient.ogg` is tracked and is not wired.

### 2.2 Direction and mastering docs (not the lived mixer)

| Doc | Dated | What it plans |
|---|---|---|
| `docs/AUDIO_DIRECTION.md` | 13 June 2026, commit `e4822c0a0d` | Adaptive faction score: Quellorian choirs and chimes against Draek drones and wet percussion; event stingers; Bevy / `bevy_kira_audio`; audio triggered from simulation events. This is mothership-scale direction. The README's lived hour is the yard, not that score. |
| `AUDIO_MASTERING.md` | June 2026 | Offline master, then a light runtime safety net. Targets for the chime: −23.0 LUFS integrated, true peak ≤ −1.0 dBTP, 48 kHz, 24-bit. |
| `AUDIO_REALTIME_SYNTHESIS.md` | workspace note v21.89.0 | Players synthesize short moments from a deterministic recipe (waveform, Hz, ADSR, partials, seed). The recipe is the source of truth. Rendered WAV is a cache. Server stores recipes, not bulk PCM. `mercy_seal: true` is required for server accept. |
| `assets/audio/music_layers/README.md` | undated in the file | Expects human-composed looping WAV stems at 44.1 kHz, 16- or 24-bit: `base_harmony.wav`, `attunement_pads.wav`, `rhythmic_pulse.wav`, `bloom_resonance.wav`. The folder is a slot. The lived mixer does not load it. |
| `docs/STEAM_CLOUD_AUDIO.md` | undated in the file | Syncs a recipe catalog JSON, not bulk PCM. |

### 2.3 What Living Thunder may reuse

Reuse the **method**, not the **beds**. — PROPOSED — pending council ratification

- The mastering targets already match `06_MUSIC_SPEC.md` §3.5: −23 LUFS, true peak at or below −1.0 dBTP, 48 kHz / 24-bit WAV for the show.
- A recipe-plus-cache habit matches the per-track log: the brief and the human edit are the source of truth; a generated file is a take.
- Layered stems match `06_MUSIC_SPEC.md` §3.5 (drone, pad, 543 top, 528 chime, rhythm, lead, stingers).

Do not reuse the yard bed, the well sting, or `epic_dark_ambient.ogg` in Living Thunder. They are not at A4 = 432, and the dark-ambient file is an unwired asset whose provenance is not a Living Thunder log row. Do not import `docs/AUDIO_DIRECTION.md` choir-as-divinity language into Living Thunder copy (`06_MUSIC_SPEC.md` §4). Powrush's own palette (faction asymmetry, wet versus crystalline) stays in Powrush until a Powrush card says otherwise.

---

## 3. Tool comparison

Read 2026-10-14 unless a source prints its own date. Prices are the public list price that day, taxes aside. "Sync" means the right to lock the audio to comic motion, a trailer, or a pilot. A vendor sentence that the user "owns" the output is a contract between the user and the vendor. It is not a US copyright registration, and it is not a promise that a third party has no claim.

| Tool | Commercial / sync, as published | Ownership of outputs | Stems | Vocals | Cost, as published | US copyright-registration limit | 06 fit |
|---|---|---|---|---|---|---|---|
| **Suno** (suno.com/terms; suno.com/pricing) | Free: personal, non-commercial, and no monthly downloads. Pro and Premier: commercial use of a permitted Download only. The terms do not carve out film or television. A Download's commercial right survives cancellation. Do not strip watermark or fingerprint. Remixes are non-commercial joint works. | Pro and Premier: Suno assigns its right, title, and interest in Output it owns. The same clause: "Suno makes no representation or warranty to you that any copyright will vest in any Output." Free: no assignment. User also grants Suno a broad licence in submissions, including to improve models. | Free: "No stem separation." Pro: 2 types (Auto; Split from mix). Premier: 3 types (Auto; Split from mix; Advanced split). | Premier: "Add new vocals or instrumentals to existing songs." Pro: "Record, upload, and create with your own voice." In-episode Living Thunder cues stay wordless anyway. | Free $0. Pro $8/month (2,500 credits, 20 downloads). Premier $24/month (10,000 credits, 60 downloads). Annual billing advertised at 20% off. | Same Office limit as every other row. See §4. | Paid Download can be the draft if the prompt is craft-only and a human finishes. Opt-in artist-name features from the 25 Nov 2025 Warner partnership must not be used (`06` §5). |
| **Udio** | Not cleared from a terms page this card could read. www.udio.com/terms returned a login wall on 2026-10-14. UMG, 29 Oct 2025: the existing product stays in a walled garden during a transition; a new licensed platform was planned for 2026. WMG, 19 Nov 2025: current closed system continues while licensed apps are built. Udio Help Center, 19 Nov 2025: still the transition terms of 29 Oct. | Not readable on the live terms page this card opened. Do not treat a secondary blog as the terms. | Not verified. | Not verified. | Not verified from the terms page. | Same Office limit. | Hold. Off-platform sync for a trailer is not shown. — PROPOSED — pending council ratification |
| **ElevenLabs Music** (elevenlabs.io/music-terms, last updated 09 Oct 2026) | Exhibit A: self-serve plans (Free through Business) allow online and offline commercial use **except film, TV, radio, and Studio Games**. Only Enterprise Music lifts the film/TV exception. Streaming is prohibited on Free and Starter. Music-library redistribution is prohibited on self-serve. | "you retain any and all rights in and to your Input and Output, in accordance with your Underlying ElevenLabs Agreement." That is retention of whatever the underlying agreement gives. It is not a warranty that copyright vests. | Not stated on the Music Terms page. | The service generates sound recordings and the compositions embodied in them. In-episode cues stay wordless. Prompt rule 2.1 already bans artist names, songwriter names, song titles, album titles, publisher names, label names, and a distinctive lyric fragment. | Fees are "the rates displayed in the Service interface." Generation caps on the terms page: Free 11 min, Starter 17, Creator 62, Pro 304, Scale 1,100, Business 4,800, per month. Dollar prices were not on that page. | Same Office limit. | Prompt ban matches `06` §5. The film/TV carve-out does **not** cover a Living Thunder trailer or pilot on a self-serve plan. Usable for those only under an Enterprise Music order that says so. Free also requires attribution ("Eleven Music"), which fights a credits rule that names only our own composers. |
| **ElevenLabs Sound Effects** (elevenlabs.io/sound-effects-terms, last updated 12 Feb 2026; ElevenCreative Terms, Exhibit 4, read 2026-10-14; help article "Can I publish the content I generate") | Paid plans: commercial use inside a combined production, and the creative terms name films, trailers, advertising, video, and games. Output may not be sold as a standalone file, sample, or sound library. Free: non-commercial, with attribution. Beta output is non-commercial. Help article: paid-plan commercial rights continue after cancellation, subject to the service-specific terms. | As the underlying agreement provides. The user may opt out of sublicensing SFX outputs to other users. | Not a stem product. Exports described on the product page as MP3, or WAV at 48 kHz for non-looping effects. | Not a vocal-music product. | Product page, 2026-10-14: free tier 50 generations/month; paid plans add the commercial licence. A promo page listed Creator at $22/month before a first-month discount. Confirm at checkout. | Same Office limit. Diegetic SFX are short and functional; a human who designs and edits them has the stronger authorship claim. | Fits the three staged S1E01 actions (scroll into the hopper, cards in the tray, token on the chair) **inside the picture**. Does not fit a reusable SFX library, and does not fit the score. |
| **Stable Audio** (kb.stability.ai commercial-and-usage page, read 2026-10-14; stability.ai/license; Stable Audio 3.0 news post) | KB: commercial use on Free, Solo, Creator, Pro, Studio, Max, and pay-as-you-go API, subject to the terms and acceptable-use policy. Examples include monetized video, ads, client work, embedded game and app audio, and streaming. Games are named. Film and television are not named as a carve-out and are not named as a grant; a pilot still needs Sherif to confirm the grant in writing. | stability.ai/license, on Core Models: "as between you and Stability, you own outputs." The 3.0 news post says the same under the Community License, and says the models are trained on licensed data. That is the company's statement, not a court judgment. | Not stated on the pages read. | Not stated on the pages read. | Dollar prices were not on the KB page. The KB says the Free plan's commercial status does not change if you later upgrade. | Same Office limit. | Best published fit for a trailer **and** a game embed, among the pages read. Human finish still required for 432 Hz, stems, and the locked stingers. Self-hosting the open weights is a different licence: Community License under $1M annual revenue, Enterprise above that. This recommendation is the hosted service, not a self-host. |
| **Cursor** | No music product. A Cursor forum thread on image generation (read 2026-10-14) describes a separate image pipeline in Agent mode. It does not describe audio. A third-party page dated 30 July 2026 states that Cursor does not compose, generate sound effects, or write audio files. Third-party extensions that sonify a coding session are not Cursor, and they are not a score. | Not applicable. | None. | None. | Cursor subscription does not buy a music licence. | Not a generator, so it creates no AI-audio claim by itself. | Use it to write briefs and the per-track log. Do not ask it for the cue. — PROPOSED — pending council ratification |

**Other tools.** AIVA, Soundraw, Mubert, and similar hosts were not given a row. Their terms were not read for this card. Adding one later is a new read of that host's terms on that date, logged in the per-track table. — PROPOSED — pending council ratification

---

## 4. Licence and IP risk

### 4.1 US copyright registration does not follow the generator

The limit is the same for every tool in §3.

- **16 March 2023.** US Copyright Office, *Copyright Registration Guidance: Works Containing Material Generated by Artificial Intelligence*, 88 Fed. Reg. 16190. Human authorship is required. When a person provides only a prompt, the Office treats the traditional elements of authorship as executed by the machine. More than a de minimis amount of AI-generated material must be disclosed. The claim covers the human author's contribution.
- **29 January 2025.** US Copyright Office, *Copyright and Artificial Intelligence, Part 2: Copyrightability*. The Office's conclusions, paraphrased from the report's own summary: copyright protects human-authored expression even when a work also includes AI-generated material; prompts alone do not provide enough control to make the output a human work; a human author owns the human-authored expression that is perceptible in an AI output, and owns a creative selection, arrangement, or modification of that output. The AI-generated portion is disclaimed.
- **Training is a separate question.** Part 3 of the same report (pre-publication, 9 May 2025) is about training on copyrighted works, not about whether the output is registrable. A vendor's contract with the user does not, by itself, end a third party's claim about training data.

Practical result for this series: a paid plan can give AlphaProMega Media Inc. a **contract right to use** a take. It does not hand the company a clean registration of that take. The registrable layer is the human finish: written motif, edited arrangement, stem choices, the locked stingers, and the picture they are cut to. Any application disclaims the generated audio. — PROPOSED — pending council ratification

### 4.2 Vendor deals are not a blanket clearance

- **Suno and Warner Music Group, 25 November 2025** (wmg.com news; suno.com/blog/wmg-partnership). The announcement settles prior litigation between those two companies and describes future opt-in uses of participating artists' names, images, likenesses, voices, and compositions. Those opt-in features are off limits here (`06_MUSIC_SPEC.md` §5). The settlement is not a licence from every other rightsholder. Suno's own terms still refuse to warrant that copyright vests.
- **Udio, Universal (29 October 2025) and Warner (19 November 2025).** Litigation settlements plus a walled-garden transition. The new licensed service was described as a 2026 launch. Until its terms can be read and they grant off-platform sync, Udio is not a Living Thunder tool.
- **Stability AI with Universal (30 October 2025) and Warner (19 November 2025).** Partnership announcements. Stable Audio's commercial-use page is the operative grant for a hosted account, not the press release.

### 4.3 House risks that sit on top of the vendor terms

- **Sync gap.** Comic motion, the trailer, and the pilot are timed picture. Eleven Music's self-serve grant excludes film and TV. A tool that only allows "personal use" or a walled garden fails `06` §5 even if the music sounds right.
- **Identical stingers.** Regenerating "Blocked." or Grounded will not produce the same file. A licence that allows commercial use does not solve identity. Lock the file.
- **432 Hz.** If a host cannot retune, the stem arrives near 440 and is rejected or retuned before the mix (`06_MUSIC_SPEC.md` §3.1, about −31.8 cents).
- **Watermarks.** Suno forbids stripping provenance metadata. Leave it in the archive take. The mix log records the tool. Do not advertise the tool on the picture (`06` credits rule).
- **Powrush revenue threshold.** Self-hosting Stability's open weights flips to an Enterprise licence above $1M annual revenue. The hosted-service recommendation does not depend on that threshold. Confirm before anyone downloads weights.
- **No health copy** anywhere the cue is described, including a registration application, a Patreon note, or a trailer card (`06` §4).

---

## 5. Recommendations — PROPOSED — pending council ratification

### 5.1 Synthwave sub-flavor (`06` §6 item 1)

**Warm nocturnal synthwave is the series lead. Bright-and-sunny is not adopted. Dark-and-driving outside siege is not adopted.** — PROPOSED — pending council ratification

This reads the open question against rulings that are already locked, and does not reopen them:

| Already locked | What it decides |
|---|---|
| Synthwave lead: analog-style pads, clipped drums, arpeggiated bass, warm saw leads (`06` §1) | The series color is warm, not a cold industrial default. |
| Darksynth only for siege (`06` §1) | Driven bass, distortion, and harder kicks stay inside siege. That is the "dark and driving" option, and it is already fenced. |
| Suave Hour: slow-burn, nocturnal, 84–96 BPM (`06` §2) | The trailer episode is this mode, at 88 BPM (`screen/S1E01/SCORE_PLAN.md`). Nocturnal, not sunny. |
| A colder, minor-tinged color only if the offer has strings (`06` §2, ruling 4) | S1E01 uses that tinge inside the A-major bed (F#m, C#m). It is not a series-wide dark flavor, and it is not darksynth. |
| Snap: bright and punchy, 112–124, hard-stop (`06` §2) | Brightness lives here, as a gag accent, not as a sunny series theme. |

Sunny daytime and dark-driving-outside-siege are both declined. The answer to §6 item 1 is the nocturnal lead the spec already describes. — PROPOSED — pending council ratification

### 5.2 Who composes (`06` §6 item 3)

**AI-assisted drafting, plus a human finisher engaged by AlphaProMega Media Inc.** Not AI alone. Not an outside act. Not a commission whose brief names another artist. — PROPOSED — pending council ratification

| Role | Who | Why |
|---|---|---|
| Draft beds and non-signature cues | A paid host from §3, prompted in craft terms | Speed, and a written commercial grant. The draft is a take, not the master. |
| Grounded motif, "Blocked.", "That one is live." | Human finisher, once | They must be identical across episodes. A new generation will drift. |
| 432 retune, stem split, loudness, wordless check, soundalike reject | Human finisher on every cue | `06` §3.1, §3.5, and §5. Review is mandatory even when the draft is kept. |
| Ownership | AlphaProMega Media Inc. | `LICENSE` and `06` §5. The finisher's contract assigns the human authorship to the company. |

The finisher may be in-house or commissioned. The contract is a work-for-hire or an assignment. The credit, if any, is that person's own name as composer of the human layer, never a third-party artist (`06` §5). — PROPOSED — pending council ratification

### 5.3 Which host

**Draft on hosted Stable Audio. Finish in a DAW. Suno Premier is the alternate if Sherif wants the published stem split and accepts Suno's copyright disclaimer. Eleven Music only under Enterprise Music that names the trailer and the pilot. Udio stays out. Cursor writes the paperwork.** — PROPOSED — pending council ratification

Reason, short: Stable Audio's public page is the one that states commercial use for video and for games without Eleven Music's film/TV exception, and the company states that the user owns the output. Suno Premier is a close second because the terms assign Suno's interest and the pricing page lists stem separation, with the explicit warning that copyright may not vest. Either way the human finish is what `06` and the Copyright Office actually rely on.

---

## 6. Pipeline — PROPOSED — pending council ratification

One path for Living Thunder, and the same path later for another product if that product's council adopts it. Steps 1–3 are the draft. Steps 4–6 are the human finish, used as far as the take needs it, and never skipped as a review.

1. **Brief, craft terms only.** Copy tempo, key, mode, and instrumentation from `06` §2 and the episode score plan. State A4 = 432. State wordless. State the stem list. Do not name a person, a group, a company, or a recording. Do not write "like" anything. Do not write a health claim. Do not put 528 Hz under a held chord, and do not hold 543 Hz over a chord that lacks C# (`06` §3.2).
2. **Tool check, that day.** Confirm the account is on a tier whose written terms grant commercial use and sync for this picture. Paste the terms, the date, and the tier into the per-track log (`06` §5 template). Reject Free Suno, Free Eleven Music, any Eleven Music self-serve plan for a trailer or pilot, and Udio until its terms are readable.
3. **Draft.** One take per cue. In-episode: no sung words. Intro and outro themes, when those exist, may carry original words with no real names and no frequency claims. If the host offers an artist, label, or title control, leave it empty.
4. **Human review, every take.** Reject and do not name the source if the take is recognizable as an existing work, if it sings during an episode, if it uses a darksynth color outside siege, or if a stem is still at 440. Retune or rebuild. Split into the §3.5 stems. Lock Grounded, "Blocked.", and "That one is live." as the master files on their first approval, then reuse the files.
5. **Delivery.** WAV 48 kHz / 24-bit. −23 LUFS integrated. True peak at or below −1.0 dBTP. A separate −14 LUFS streaming master only if a platform needs it (`06` §3.5).
6. **Log, then stop.** One row per track: track, tool, licence terms as of the creation date, date. No artist names in the row. The picture edit uses only logged masters.

Powrush, when a later card adopts this path, swaps the palette (its own direction doc) and the tuning check (its own pitch), and keeps steps 2, 4, 5, and 6. It does not load Living Thunder masters as game beds. — PROPOSED — pending council ratification

---

## 7. First deliverable: S1E01 trailer cue list — PROPOSED — pending council ratification

Source: `screen/S1E01/SCORE_PLAN.md` (draft for council review). The audit asks for a 60–90 s trailer of Block, Recycle, and Pass, and says not to use shots S13 or S33 (`docs/SHIP_READINESS_AUDIT.md` §4.2, §5.2). Shot durations below are the estimates in `screen/S1E01/SHOT_LIST.md`. They are already marked proposed there. This list does not add cues, chords, or SFX.

The series intro under MAIN TITLES is outside the score plan. It is not in this deliverable.

**Use these cues, in this order. Trim inside them. Do not play the episode at full length** (the shot list totals about 185 s before titles).

| Order | Cue | What the score plan already says | Shots for the trailer | Estimate if those shots are kept | Notes |
|---|---|---|---|---|---|
| 1 | C01 | Enters under the wide shot, warm and unhurried. A – F#m – Dmaj7 – E6, 543 Hz pad holds, 108 Hz drone on, lead answers, soft drums, no bell. | S01 (6 s), S03 (5 s) | 11 s | Cold open and the grounded hammer. S02 and S04–S06 stay available if the cut needs air. |
| 2 | C02 | Glassy bell once, on the lamp glint (S11). A – C#m – F#m – A, pad holds, drone on. | S11 (5 s) | 5 s | The only bell in the episode. Omit this row if the lamp glint is not in the cut. |
| 3 | C06 | Fixed "Blocked." stinger, unchanged: short, low, muted thud and a filter close. Drone stays 108 Hz. No 54 Hz. | S23 (3 s), S24 (5 s) | 8 s | Place the existing stinger. Do not compose a new one. |
| 4 | C08 | Light and dry. Three short card tones; CLEAN is a clean A-major bloom. Drone **out** for the gag. | S30 (5 s), S31 (4 s), S32 (4 s) | 13 s | S33 is the GAP shot. Leave it out. SFX: scroll into the hopper, cards landing in the tray, room tone. |
| 5 | C09 | Fixed "That one is live." stinger: open A-major bloom, 543 Hz pad holds, 528 Hz chime short on top, never held. Drone **returns** at 108 Hz. | S34 (5 s), S35 (4 s), S36 (4 s) | 13 s | SFX: token set on the chair, room tone. |
| 6 | C10 | Grounded: four notes rise, land on A, and hold. Pad holds. Drone on. No drums. No bell. | S39 (6 s) | 6 s | The trailer ends on the hold. Nothing plays after it. |

**Sum of the shots named above: 56 s.** A title card, if the council rules one, is the room between 56 s and the 60–90 s ask. No title card is defined in the score plan (`docs/SHIP_READINESS_AUDIT.md` §5.2 step 3).

**Left out of this first cut, on purpose:** C03 (it covers S13, which the audit excludes), C04, C05, and C07. They remain the episode score. They are not required to show Block, Recycle, and Pass.

**Standing rules on every row:** wordless; no choir (the S1 choir is S1E06); no darksynth; no health wording; A4 = 432; the two stingers and Grounded are the locked files, not new generations. — PROPOSED — pending council ratification

---

## 8. Decisions left for Sherif

1. Ratify §5.1 as the answer to `06` §6 item 1, or send a different sub-flavor. This file will not invent a third one.
2. Ratify §5.2 as the answer to `06` §6 item 3: AI-assisted draft, human finisher, company-owned.
3. Pick the host: hosted Stable Audio (recommended), Suno Premier (alternate), or Eleven Music only with an Enterprise Music order that covers the trailer and the pilot. Udio waits on readable terms.
4. Name the finisher and sign the assignment. Until that exists, no cue is made.
5. Accept or cut the §7 shot list. Adding shots back in (except S13 and S33) is an edit choice inside the existing plan.
6. Rule the trailer title card and the intro theme. Both sit outside `SCORE_PLAN.md`.
7. Say whether Powrush adopts §6 on its own card. This file does not change that repo.
8. Say whether anyone files a US registration, and which human-authored layer is claimed. Generated audio is disclaimed either way.
9. Confirm, before any self-hosting of open weights, whether annual revenue is under the Stability $1M Community License line. The hosted path does not need that confirmation.

---

## 9. Sources

Pages and posts were read on **2026-10-14** unless the line gives another date.

- `06_MUSIC_SPEC.md` §1–§6. Vocals answer: Sherif, 2026-10-01 12:17 AM ET, recorded in §5 and §6.
- `screen/S1E01/SCORE_PLAN.md`; `screen/S1E01/SHOT_LIST.md` (durations and the S13 / S33 GAP rows); `docs/SHIP_READINESS_AUDIT.md` §4.2 and §5.2.
- `LICENSE` (AlphaProMega Media Inc.).
- Ra-Thor `README.md`, `PUBLIC_CLAIM.lock.md`, `CONTACT.md`: X handle `https://x.com/AlphaProMega`.
- Posts quoted in §1, fetched 2026-10-14.
- Powrush-MMO at `41ba3f72bdee2a8441f763d1d3853716d34fbc46`: `assets/audio/README.md`, `assets/audio/music_layers/README.md`, `client/assets/audio/README.md`, `scripts/gen_peace_yard_audio.sh`, `docs/AUDIO_DIRECTION.md`, `AUDIO_MASTERING.md`, `AUDIO_REALTIME_SYNTHESIS.md`, `docs/STEAM_CLOUD_AUDIO.md`.
- Suno Terms of Service, https://suno.com/terms ; pricing, https://suno.com/pricing .
- Suno / Warner Music Group, 25 November 2025: https://www.wmg.com/news/warner-music-group-and-suno-forge-groundbreaking-partnership and https://suno.com/blog/wmg-partnership .
- Udio transition: Universal Music Group, 29 October 2025, https://www.universalmusic.com/universal-music-group-and-udio-announce-udios-first-strategic-agreements-for-new-licensed-ai-music-creation-platform/ ; Warner Music Group, 19 November 2025; Udio Help Center, 19 November 2025, https://help.udio.com/en/articles/12874375-udio-warner-music-group-wmg-partnership . Live terms page not readable (login wall).
- ElevenLabs Music Terms, last updated 09 October 2026, https://elevenlabs.io/music-terms .
- ElevenLabs Sound Effects Terms, last updated 12 February 2026, https://elevenlabs.io/sound-effects-terms ; ElevenCreative Terms Exhibit 4, https://elevenlabs.io/creative-terms ; help article https://help.elevenlabs.io/hc/en-us/articles/13313564601361-Can-I-publish-the-content-I-generate-on-the-platform .
- Stable Audio commercial use, https://kb.stability.ai/knowledge-base/stable-audio-commerical-and-usage-licensing ; Stability AI license, https://stability.ai/license ; Stable Audio 3.0 announcement, https://stability.ai/news-updates/meet-stable-audio-3-the-model-family-built-for-artistic-experimentation-with-open-weight-models .
- US Copyright Office AI hub, https://www.copyright.gov/ai/ (Part 2 published 29 January 2025; Part 3 pre-publication 9 May 2025). Registration guidance, 16 March 2023, https://www.copyright.gov/ai/ai_policy_guidance.pdf .
- Cursor: no audio generator found. Forum thread on the image pipeline, https://forum.cursor.com/t/use-model-native-image-gen/162501 . Third-party statement that Cursor does not generate music, 30 July 2026, https://anycap.ai/page/en-US/ai/cursor-music-generation-guide .
