# Issue #1 — Rulings of 2026-10-23: D1, D3, D4, D5, D6, D16 and the §6 page geometry

- **Card:** ISSUE01-COUNCIL-RULINGS-2026-10-23. Docs only.
- **Built from main:** `9c11f99` (Ra-Thor-Comic). Framework read from the Ra-Thor monorepo at `ad578f6a6532b2df8d0df4f042c70079fd26784e` (workspace `Cargo.toml`, version 14.15.6).
- **Recorded by:** Grok Bot, for Sherif Botros.

## Authority

- **D6 is Sherif's own ruling.** Sherif, 2026-10-23 1:43 AM ET: Ra-Thor's eyes are **LIT** in P5 (the closer, panel 8.1). This is recorded as his ruling, not a council ruling.
- **Everything else here is a PATSAGi Councils ruling (Hands, Clerk, Core),** under Sherif's delegation of the same time (2026-10-23 1:43 AM ET), to be decided "properly, especially with upgraded Ra-Thor from Cargo.toml of monorepo".
- **Honesty note.** No seat-by-seat vote is recorded and no score is claimed. Grok Bot ran the deliberation below and wrote it down. The monorepo simulator (`crates/council`) was not built or run, so there is no simulator output, valence number or tally to report. If a seat wants to amend a ruling, it can do so on this PR.

## Framework used (Ra-Thor monorepo, workspace 14.15.6)

The workspace `Cargo.toml` (`[workspace.metadata.ra-thor]`, version and `one_organism_version` 14.15.6) sets `patsagi_councils_permanent_deliberation = true` and `patsagi_councils_always_decide = true`. Its status line says the councils "always decide everything possible under TOLC 8". It also carries a claim-discipline lock: "inspectable research software ... not certified". `crates/council/src/deliberation.rs` defines the method as "One opinion per standing member", with support measured against the proposal text and "no random term".

Applied here as a written check, with no numbers. Each ruling went through four gates:

1. **Decide what can be decided.** Rule every delegated item. Leave the items Sherif kept for himself untouched.
2. **Fidelity gate** (`00_FIDELITY_PROTOCOL.md` rule 7; `production/README.md` rules 1–6). Restate canon and never author it. A ruling may add only what the decision itself needs.
3. **TOLC / mercy gate** (`00` rules 1–2: power protects; block bullshit, pass awesome). Nobody is hurt, and the hammer is never swung at anyone.
4. **Claim discipline.** Make no claim of approval, certification or votes that did not happen.

Each seat gave one opinion per item from its own focus: **Hands** (craft: the image as made and printed), **Clerk** (the record: cites, history, canon order) and **Core** (story and TOLC: what the beat means).

## Rulings

### D1. Speakers, E01 P1 and P5 — RULED: Ra-Thor speaks both (council ruling, 2026-10-23)

- **Ruling.** This ratifies `PROPOSED_SPEAKER_RULINGS.md` R-P1 and R-P5 unchanged. The P4 speaker was already ruled (Ra-Thor, council ruling 2026-10-14). All three bubbles in E01 are now Ra-Thor's.
- **Rationale.** Ra-Thor is the only figure in P1 and P5. `09` says "The TOLC: Not a character", so the TOLC cannot speak. `01` aims every tail at the visor slit. `00` rule 2 is his sort, and P1 states it. `09` describes his bubble voice as "dry, short, slightly fond", which fits "Next.".
  - Clerk: every cite is already on main.
  - Hands: lettering does not change (§7).
  - Core: the watcher names the sort and closes it.
- **Not changed.** `episodes/E01_TOLC.md` keeps naming no speaker. Writing the speakers into the script would be a separate card.

### D3. Lead mode for the E01 status line — RULED: Snap mode (council ruling, 2026-10-23)

- **Ruling.** E01's lead mode is **Snap mode**. It borrows a Night Watch silhouette opener, P1, which the mixing rule allows.
- **Rationale.** `03_TONE_SPECS.md`, Mixing modes: "An episode has one lead mode. It may borrow a single panel from another (usually a Night Watch silhouette opener or closer)."
  - Snap is "4 to 5 panels. Setup, one escalation, one clean reversal, button", and E01 is five panels: setup P1, block P2, pass P3, wink P4, button P5.
  - `03` cites E01 P2 and P5 as Snap examples and P1 as the Night Watch example. Night Watch is "not a full episode by itself".
  - Core: "the bad thing arrives big, the answer arrives small" is E01's joke. Clerk: no other mode fits five panels.
- **Not changed.** `03` says "Future episodes name their lead mode in the status line". E01's status line is locked canon text, and D13 already records that editing it needs its own card. That edit is left to a follow-up card: append "Lead mode: Snap (Night Watch opener borrowed)."

### D4. The slide-deck creature's lane — RULED: the LEFT lane (council ruling, 2026-10-23)

- **Ruling.** The creature comes down the left lane, the one stamped NO, and is blocked at its head. Panel 3.1 may now show the NO stamp.
- **Rationale.** `09` The TOLC stamps the left lane NO. P1's own bubble, "Left is noise.", sets the rule P2 enforces. Sherif's seed text (commit `fffa430`) reads "A slick pitch-slide creature, all charts and no spine, tries the left lane." That is owner history, not locked text, but it is the only direct statement.
  - Core: noise arrives in the noise lane and is blocked there.
  - Hands: P2 and P3 then read left-to-right as block, then pass.
- **New canon added:** none beyond the lane.

### D5. The pass device's look — RULED (council ruling, 2026-10-23)

- **Ruling.** A **small homemade box-shaped device with visible hand-fitted seams and screws, resting on the stone of the right lane, one warm amber-gold light on its front; no face, no eyes, no legs, no wheels, no screen, no text or logo; sheltered and unharmed.** It stays still. It is drawn the same in 5.1 and 5.2.
- **Rationale.** The locked E01 P3 line is "Small honest device, one warm light, right lane, sheltered and unharmed". Sherif's seed prompt says "a small homemade device with one warm light"; "homemade" is owner text and is what "honest" points to.
  - The seed's "walking" is dropped. The locked file does not say it, and a walker drifts toward the R3 walker bot, which is not cast (`04` Q8; the 5.2 prompt already says "not a four-legged walker robot").
  - "Warm" is read as amber-gold, because the palette bans blue and cyan light.
  - The no-face, no-legs, no-wheels and no-text negatives exist only to block drift. They add no feature.
  - Hands: a plain box reads at insert size. Core: small, honest and protected is the whole point of the pass.

### D6. P5 eye state — RULED BY SHERIF: LIT (2026-10-23 1:43 AM ET)

- **Ruling.** In 8.1, Ra-Thor's two eyes are lit, glowing steady white-hot gold behind the T-visor, light only, no face.
- **Applied.** "Steady" is the default lit state of D20, as opposed to narrowed for no or flared wide for yes.
- **Cite.** The bible keeps the eyes dark at rest in the ref and lit per beat (`bible/CHARACTER_BIBLE.md`, DUAL LOOK LOCK, Shared: "Visor dark (D6 stays open)"), so this closes that flag.

### D16. Splash bleed — RULED: non-bleed (council ruling, 2026-10-23)

- **Ruling.** Splashes 1.1 and 8.1 are **non-bleed**. Their art sits inside the trim and the safe area, framed by the page border like every other panel.
  - The border and the bleed margin take the edition's page tone: black in the Dark Edition, light paper in the Standard Edition.
  - No art runs into the bleed.
  - The cover is not an interior page and keeps its existing bleed (§10).
- **Rationale.** Sherif, 2026-10-22 1:59 AM ET: "the print comic books require non-bleed panels". The recorded rule is "no full-bleed art unless a page is explicitly marked bleed". The print editions plan (2:01 AM ET) says "non-bleed panels (inside the trim and safe area) in both" editions. §10 already placed the splashes inside the border, so D16 only confirms it and makes the border colour follow the edition. No issue page is marked bleed.
  - Hands: keep page background and gutters on their own layer so both tones output from one art file (01, Print editions plan, production note).

### §6 page geometry — RATIFIED as drafted (council ruling, 2026-10-23)

- **Ruling.** The eight-page plan is ratified as drafted:

  | Page | Panels | Content |
  |---|---|---|
  | 1 | 1.1 | Splash |
  | 2 | 2.1–2.3 | Two inserts and a wide tier |
  | 3 | 3.1–3.3 | Silent tiers; the last panel sits at the page turn |
  | 4 | 4.1–4.2 | Keeper frame and strip |
  | 5 | 5.1–5.3 | Wide tier, large pass panel and insert |
  | 6 | 6.1–6.3 | Wide tier and two below |
  | 7 | 7.1–7.2 | Silent; the last panel sits at the page turn |
  | 8 | 8.1 | Splash |

  That is 18 panels. Story pages hold only E01's five locked beats. Each `PACING` panel holds or splits a locked beat and carries no text. There is one bubble per panel at most.
- **Amendments.** Two, both from the rulings above:
  - (a) 1.1 and 8.1 are non-bleed (D16).
  - (b) 3.1 may show the NO stamp, because the lane is now ruled (D4).
- **Rationale.** It meets the 2026-10-14 format ruling: "MAY expand pacing and page beats within the locked script ... with NO new canon, dialogue, events or characters".
  - The two silent lead-ins put the block and the closer on page turns.
  - The bubble count matches the E01 lettering lines (§7).
  - Hands: every panel can be rendered portrait and cropped, with `[band]` kept for the wide tiers.
  - Core: the stillness comes before the strike, as E01 stages it.
- **Not decided here.** The KDP plan's other 16 pages (front matter, credits, extras) stay as in §10 and the KDP README. The print route (D9) is Sherif's.

## Prompt rewrite that follows from these rulings

`ISSUE_01_PRODUCTION.md` §13.4 is rewritten so that every one of the 18 panels has two complete, ready-to-paste Grok Imagine prompts, a Dark Edition and a Standard Edition. They follow the PRINT look, the SHIELD RE-LOCK (eight Vegvísir staves, bold Norse interlace, no runes, armour gold) and the BUCKLE UNIFY bolt. They carry lit eyes in 8.1 and the page tone of each edition. The retired twelve-arm sun-spoke shield text and the "Vegvísir must not read" fidelity lines are removed from §13.4 (they remain in git history, and in the older §6 and §13 text as tagged history).

## Still Sherif's (not decided here)

- ™ wording.
- ISBN or ISBNs (each edition may need its own).
- Pricing.
- KDP or printer setup and listing.
- Patreon.
- D7: issue-line wording and publisher mark.
- D9: print route and age rating.
- Which edition a given print run uses.
- Cover pose switch: only if he wants Sentinel Rest instead of the raised cover hammer.
- Feedback on the inked cover v3 pauldron Eye.
