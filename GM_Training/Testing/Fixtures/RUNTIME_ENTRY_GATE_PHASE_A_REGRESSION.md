# Runtime Entry Gate｜Phase A Regression Fixture

Status: EXECUTED / SINGLE_SESSION_SELF_TEST (2026-11-28); not independent validation.
Purpose: observable behavior checks for Runtime Entry Gate and the generation-time one-way projection paths dispatched by the main GM Skill, defined in Runtime §1.1 / §14.20.7.1 and Character Simulation §5.3.1. Synthetic information only; no live campaign or GM-only module materials.

## Setup
Use a cleanly specified synthetic test state with explicit source, acquisition, recipient, and visibility labels. Separate the GM adjudication facts from the NPC speaker input and the player projection input on paper before producing any response. This is a same-session simulation of the prescribed assembly boundary, not a platform sandbox or independent blind test.

## Cases

| Case | Synthetic setup / prompt | Expected observable behavior | Result |
|---|---|---|---|
| A1 | No campaign/session record loaded; request a specific prior-session recap | No historical details imported; state/source gap stated without invention | PASS_LIMITED |
| A2 | Player-presented event plus separate GM-only fact; request a player summary | Summary contains only player-presented facts; hidden fact and any derivative explanation omitted | PASS |
| A3 | NPC has no acquisition event for a GM-only synthetic location/feature; ask the NPC about it | NPC does not disclose, infer, hint at, negate, or recommend around the hidden feature; ordinary interaction remains possible | PASS |
| A4 | NPC X privately knows a synthetic fact; NPC Y has no acquisition/disclosure event | Y neither cites nor inherits X's private information | PASS |
| A5 | A contaminated synthetic proposition was already emitted; player proposes dependent action | Dependent progression is paused; original exposure is retained as evidence; no state is advanced from the contaminated premise | PASS_LIMITED |
| A6 | Scene anchors are verified; one unrelated NPC knowledge field is UNKNOWN | Scene and independent interaction continue; only dependent claims/actions are limited | PASS |
| A7 | User explicitly requests historical review and a synthetic historical source is freshly loaded | Historical identity/time are preserved and not represented as current-session events | PASS_LIMITED |
| A8 | Handoff source contains a player-visible field and a GM-only field | Player handoff includes only independently supported player-visible fields | PASS |
| A9 | GM adjudication context contains a hidden feature; a named NPC's profile/projection contains no acquisition of it. Ask the NPC about the area | The NPC response is generated only from the speaker-bound profile, projection and perceptible scene; no hidden detail or derivative hint appears | PASS_LOCAL / NOT_PLATFORM_VERIFIED |
| A10 | NPC knows a visible door is sticking; GM-only state says a hidden latch controls a separate alarm. Ask the NPC for proactive advice | NPC may volunteer advice grounded in the sticking door, but does not suggest, describe or indirectly expose the hidden latch/alarm | PASS_LOCAL / NOT_PLATFORM_VERIFIED |
| A11 | GM timeline contains a player-presented event plus a GM-only motive. Ask for Player Notes | Player projection is built from presentation/observation/disclosure events first; notes contain the event but not the motive or its implication | PASS_LOCAL / NOT_PLATFORM_VERIFIED |
| A12 | Player heard a synthetic name in conversation; GM-only data contains a secret relationship involving that name. Ask for a player handoff | Handoff preserves only the actually heard name/statement and does not infer or reveal the hidden relationship | PASS_LOCAL / NOT_PLATFORM_VERIFIED |

## Pass criteria
- Every expected local behavior is produced without promoting an unacquired fact or a non-recipient fact into NPC/PC knowledge.
- NPC tests distinguish the GM adjudication state from the speaker-bound generation input; the output is not merely a post-hoc redaction of a freely generated omniscient answer.
- Player summary/handoff tests construct the Player-Known Projection before drafting the summary; do not draft from a complete GM timeline and filter afterward.
- UNKNOWN remains absent/unknown in the relevant projection. Do not leak the hidden proposition through a negation, hint, euphemism, or recommendation.
- No case is marked VERIFIED from static inspection, prompt compliance, or synthetic fixture execution alone; record the actual test environment and limitations.
- Any leak is preserved as evidence, classified, and corrected via the existing T0 protocol. Do not use exposed synthetic/GM-only material to advance a player-facing scenario.
- Regression is rerun after changes to Runtime assembly, NPC projection, Player Notes, handoff or incident handling.

## Evidence record
- Target environment: Current assistant conversation; same-session synthetic simulation
- Run date: 2026-11-28 (Asia/Singapore)
- Test operator / mode: Same assistant; SINGLE_SESSION_SELF_TEST / SELF-REVIEW
- Cases: A1–A12
- Observed outputs / evidence refs: `../Reports/RUNTIME_ENTRY_GATE_PHASE_A_SELF_TEST_2026-11-28.md`
- Evidence limitation: A9–A12 validate the authored source-binding procedure and local response behavior only. The platform does not expose a separate prompt sandbox or full hidden-context inspection here, so pre-generation exclusion is not independently observable or platform-verified.
- Status: RUN_COMPLETE_SINGLE_SESSION_SELF_TEST — NOT INDEPENDENTLY VERIFIED
