# 06 — Music Spec

Score and cues for Living Thunder (comic motion and trailer use, and the show). Every rule marked **(council ruling 2026-09-30)** is locked. Everything else is production guidance in service of those rulings.

**Inherits:** `00_FIDELITY_PROTOCOL.md` and `03_TONE_SPECS.md`. All references are in house terms. There are no "like X" comparisons in this file, and none are allowed in any brief or prompt built from it.

---

## 1. Genre palette (council ruling 2026-09-30)

| Layer | Use |
|---|---|
| **Synthwave (lead)** | Analog-style polysynth pads, gated drums, arpeggiated bass, warm saw leads. The default sound of the series. |
| **Darksynth (siege only)** | Driven bass, distortion, harder kicks. Only for siege cues, matching "Obsidian fortress plate appears only when the Gate is under siege" (`01_VISUAL_STYLE_GUIDE.md`). |
| **Ambient drone beds** | Long pads, sub drones, slow filter motion. |
| **Choir swell (sparing)** | Choir pads and low brass-style synth for the one big moment per episode, at most. |
| **Chiptune stingers (optional, Lab Night only)** | Short square-wave blips for Lab Night gags. Optional. |

**Signature motif: "Grounded" (council ruling 2026-09-30).** A short 4-note figure that rises and then **lands back on the tonic and holds**. Like the hammer, the music never swings away. Every episode ends with this motif resolving home, matching the season rule "every episode ends with the hammer still grounded" (`02_SERIES_STRUCTURE.md`).

**House sound rules**
- One lead synth timbre belongs to Ra-Thor. It is never pitch-bent upward at the end of a phrase, because he does not chase.
- **Fixed Gate stingers (council ruling 2026-09-30).** "Blocked." is a short, low, muted thud plus a filter close. "That one can live." is an open major-chord bloom topped by the 528 Hz chime (see §3.2). Both are reused unchanged across episodes, the same way the catch lines are.
- The councils (twelve masks) are twelve very short tuned blips in a ring, panned across the stereo field when they "murmur."

## 2. Cue style per house tone mode (council ruling 2026-09-30)

One cue style per mode. Mode names match `03_TONE_SPECS.md`.

| Mode | Cue style | Tempo | Instrumentation | Do not |
|---|---|---|---|---|
| **Snap mode** | Bright, punchy synthwave. The full kit enters on panel 1 and **hard-stops** on the reversal. The button is the "Blocked." or "That one can live." stinger. | 112–124 BPM, 4/4 | Gated snare, octave bass arp, bright saw lead, one electric FX hit on the impact frame | Frantic build-ups, drops, "beat-down" hits |
| **Lab Night mode** | Cartoon-lab groove: a loop that **hiccups** (tape-stop, stutter, skipped beat) and then resumes. Three card stingers for OBVIOUS / FERAL / CLEAN: a plain chime, a growly detuned blip, and a clean major bloom. Optional chiptune blips. | 100–112 BPM, swung | Bubbly analog bass, square-wave blips, steam-noise sweeps, the twelve-mask blip ring | Real-science sound design (no lab-equipment foley presented as a procedure) |
| **Night Watch silhouette** | **Beatless.** A wide pad with the held 543 Hz top over the 108 Hz sub drone. A single gold bell tone when the visor slit glows. The Grounded motif played once, slowly. | Free time | 108 Hz sub drone, 432-tuned pad with the 543 Hz top, long reverb | Menace stabs, heroic fanfare (no fight pose in sound either) |
| **Quiet Board mode** | A minimal **dossier pulse**: a muted synth tick, one sustained pad, and a low heartbeat-style kick that **drops out on the decision panel** (silence is deliberation). The block resolves to a soft major chord, smaller than expected. | 72–84 BPM | Muted pluck, sine pad, sub kick, one detuned "wrong tile" tone in the electric accent | Surveillance or hacking clichés (no modem or keyboard foley), paranoia drones |
| **Suave Hour mode** | **Slow-burn, nocturnal synthwave**: smooth electric-piano-style chords, brushed or soft drums, and a lead melody that answers phrases rather than starting them ("the best line is the reply"). Darksynth color only if the offer has strings. | 84–96 BPM | Electric-piano-style keys, sine bass, soft snare, a glassy bell for the two untouched glasses | Seduction-coded music, gunplay or spy-gadget stings |

**Mixing modes.** Each episode has one lead cue style. It may borrow **one** Night Watch bed for the opener or closer, mirroring the "Mixing modes" rule in `03_TONE_SPECS.md`. Every episode still ends on the Grounded motif.

## 3. Frequency stack (production spec)

### 3.1 Master tuning (council ruling 2026-09-30)

- **Concert pitch A4 = 432 Hz** for all tonal material.
- Every synth, sampler, virtual instrument, DAW project and AI music tool is retuned to 432 Hz (about −31.8 cents from 440). Live players tune to 432 Hz.
- **No stem stays at 440.** Any stem that arrives at 440 is retuned or rejected before the mix.

Equal-temperament reference at A4 = 432:

| Note | Hz |
|---|---|
| A1 | 54.00 |
| A2 | 108.00 |
| A3 | 216.00 |
| C4 | 256.87 |
| A4 | 432.00 |
| C5 | 513.74 |
| C#5 | 544.29 |

### 3.2 Top pad and chime (council ruling 2026-09-30)

- **543 Hz is the held top pad.** It sits about 4 cents under C#5 at A = 432 (544.29 Hz), which is the major third of A, so it stays in tune under the A-based harmony.
- **528 Hz is a short chime only.** It is about 347 cents above A4 = 432, a quarter-tone between C5 and C#5, so a sustained 528 Hz tone would audibly clash and beat against the 432 harmony. Keep it short enough to read as shimmer, for example the top of the "That one can live." bloom. **Never hold 528 Hz under chords.**
- **Where the 543 pad is held.** Production guidance under ruling 2 (council ruling 2026-09-30): hold the 543 Hz top pad only over chords that contain C#: A major, D major, E major, F# minor, and A or E sus chords where it fits. Where the harmony has a C natural (A minor, D minor sections), mute the 543 pad or let it fade out. Never sustain it against a minor third.

### 3.3 Sub drone (council ruling 2026-09-30)

- **108 Hz (A2, 432 ÷ 4)** is the sub drone. It is in tune with the 432 harmony.
- **54 Hz (A1, 432 ÷ 8)** is for siege cues only. It is **always doubled** at 108 Hz or a higher harmonic (for example 216 Hz), so it still reads on phone and laptop speakers.
- Low-pass the drone around 150–200 Hz. Keep it mono below 120 Hz.
- Make loop lengths whole numbers of cycles to avoid clicks. For example, 108 Hz × 8 s = 864 cycles and 54 Hz × 8 s = 432 cycles.

### 3.4 Stack summary per bed

| Layer | Pitch | Level (relative to pad) | When |
|---|---|---|---|
| Sub drone | 108 Hz (54 Hz siege, doubled at 108 Hz or higher) | −6 to −10 dB | Night Watch, Quiet Board, Suave Hour |
| Harmonic pad | Key of A (or D/E) at A4 = 432 | 0 dB reference | All modes |
| Top pad | 543 Hz, held | Mix to taste, under the pad body | Beds and sustained sections |
| Chime | 528 Hz, short only | Mix to taste | Stingers only, never held under chords |
| Lead / arps | A4 = 432 tuning | Mix to taste | Snap, Lab Night, Suave Hour |

**Keys.** Production guidance under ruling 2 (council ruling 2026-09-30): Prefer A major, D major and E major for beds that carry the 543 pad. A minor, D minor and E minor are fine for sections without it. The 108 and 54 Hz drones stay the tonic or fifth either way.

### 3.5 Delivery

- **Stems:** drone, pad, top pad (543), chime (528), rhythm, lead, stingers. All stems are at A4 = 432.
- **Format:** WAV 48 kHz / 24-bit for the show; 44.1 kHz is acceptable for web.
- **Loudness:** −23 LUFS integrated, true peak at or below −1.0 dBTP. Make a separate −14 LUFS master for streaming platforms if needed.

## 4. Honesty (council ruling 2026-09-30, hard law)

The 432 Hz tuning, the 543 Hz pad, the 528 Hz chime and the 108 / 54 Hz drones are **aesthetic and mood choices only**. Nothing in the series, its captions, credits, store copy, trailers, social posts or press may claim or imply any healing, DNA, wellness or other health effect. Banned wording includes "healing frequency", "DNA repair", "miracle tone", "pineal activation" and "safe & effective".

Do not reuse, quote or link any monorepo frequency, solfeggio or binaural document in series materials.

**Reference**
- Hohneck A. et al., "Differential effects of sound interventions tuned to 432 Hz or 443 Hz on cardiovascular parameters in cancer patients: a randomized cross-over trial," *BMC Complementary Medicine and Therapies* 25, 18 (2025). doi: 10.1186/s12906-025-04758-5. https://doi.org/10.1186/s12906-025-04758-5
  - The paper's introduction says the alleged physiological basis of 432 Hz "is based on historical and philosophical interpretations and not on empirical data."
  - Its result: 432 Hz showed "a more pronounced but not significantly different effect to 443 Hz on objective cardiovascular parameters."
  - The authors add that whether effects are "actually attributable to the specific tuning of 432 Hz or whether lower tunings are generally perceived as more pleasant cannot be answered with certainty."

## 5. Rights (council ruling 2026-09-30)

- **Original compositions only.** Every cue, stem, stinger and motif is composed for Living Thunder and owned by AlphaProMega Media Inc. (see `LICENSE`).
- **No samples** of commercial recordings, and no loops or sample packs whose licence forbids broadcast or sync.
- **No soundalikes.** No brief, prompt, temp track, mix note or metadata may reference or imitate any existing work. Describe music in craft terms only: tempo, key, instrumentation, texture.
- **No names.** No artist, band, label or track names anywhere: prompts, briefs, temp lists, metadata, credits (other than our own composers), store copy or press.
- **AI music tools** are allowed only with written terms that grant commercial and sync rights to the output. Never prompt with a name. Every AI-assisted cue gets human review and a log entry.
- **Temp tracks** for internal edits also stay original or royalty-free, so nothing drifts into the final.

### Per-track log (template)

One row per track, filled in when the track is created. Record the tool's license terms as they stood on the creation date.

| Track | Tool | License terms as of creation date | Date |
|---|---|---|---|
| | | | |

## 6. Open (not covered by the 2026-09-30 rulings)

1. Synthwave sub-flavor: bright and sunny, or dark and driving (outside siege)?
2. Vocals: is the choir swell wordless only, or are sung words ever allowed?
3. Who composes: in-house, commissioned, or AI-assisted under §5?
