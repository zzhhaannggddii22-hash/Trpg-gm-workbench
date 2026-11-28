# Blades in the Dark｜Synthetic Runtime Execution Report — Round 4

> Date: 2026-11-28  
> Fixture: `BITD_CANDIDATE_V01`  
> Scope: 14 additional cases covering Magnitude, Ritual learning/performance, Invention/Crafting/Modification, Drawbacks, PC/Crew ability triggers, and Armor recovery timing.  
> Status: 14/14 desk-executed; live play not performed.  
> Method: Manual deterministic trace against the updated local runtime references and official Blades SRD / Full Player's Kit v8.2. This is not automated testing, independent review, or live-play acceptance.

## 1. Result

- Newly executed this round: 14
- Passed: 14
- Failed: 0
- Combined fixed regression matrix: 75/75 synthetic cases passed.
- Live play, exact campaign edition/errata lock, and actual selected-sheet audit remain open.

A pass means the fixed scenario was resolved consistently with the documented procedure and checked official source. It does not establish exhaustive coverage of every ritual, formula, item, ability, or cross-ability interaction.

## 2. Execution traces

| Test ID | Trace / expected handling | Result |
|---|---|---|
| BLD-T62 | A magnitude-6 sea demon creates a crushing wave at a dock. The wave naturally affects vessels and crews in the area. | PASS — assess the relevant force dimension; do not automatically add Area as another magnitude level when it is naturally part of the effect. Combine dimensions only where the effect truly requires it. |
| BLD-T63 | A Whisper acquires a ritual book and wants to learn a new ritual. | PASS — source must be secured first; then use a Long-Term Project, usually an 8-segment clock, and define effect/weirdness, method/price, and the belief/fear gained. |
| BLD-T64 | A ritual is dangerous to perform and its degree of effect is uncertain. | PASS — Action Roll (usually Attune) resolves danger/troublesome performance; Fortune Roll resolves uncertain manifestation. Both may be required because they answer different questions. |
| BLD-T65 | A caster extends ritual casting time to reduce Stress cost. | PASS — use Magnitude duration examples to negotiate lower cost, generally not below about an hour; account for exposure, delay, or the target's opportunity to react. |
| BLD-T66 | A PC invents a special alchemical formula; another PC crafts a common ordinary item. | PASS — special formula/design normally needs an invention project (usually 8 segments); known design crafting costs one Downtime Activity; common alchemicals/ordinary items using common instructions need no special invention. |
| BLD-T67 | Tier II Crew has Workshop; Leech with Alchemist crafts an alchemical creation and rolls 4/5. | PASS — Workshop raises effective Tier by one; Alchemist raises the roll's result level by one. Apply effective Tier and result level in their own steps; do not convert either into an extra die. |
| BLD-T68 | PC adds an arcane ability to an existing weapon so it can harm a demon. | PASS — this is an item modification, not automatically a new invention project; arcane/spark-craft/alchemical modification normally requires Tier+3 Quality. |
| BLD-T69 | A creation has Conspicuous, Consumable, Unreliable, Volatile, Complex, and Rare drawbacks. | PASS — Conspicuous adds +1 Heat per Score in which it is used; alchemicals must be consumable; Unreliable uses a Quality Fortune Roll; Volatile creates a resistible consequence; Complex requires multiple stages/activities/rolls; Rare requires its material. |
| BLD-T70 | Cutter uses Bodyguard to Protect a teammate, then gathers information about threats in the current situation. | PASS — +1d applies to Resistance for the Protect consequence; +1 Effect applies to the specified current-threat information. Neither bonus becomes universal. |
| BLD-T71 | Crew selects Deadly during initial creation and applies it to a PC's Hunt rating. | PASS — this adds +1 Action rating up to 3, not +1d; if chosen during initial character/Crew creation, its text supersedes the normal starting Action rating limit. |
| BLD-T72 | Bravos with Fiends calculates Turf and Tier advancement costs. | PASS — Wanted levels count as Turf, Wanted Level maximum is 4, and minimum Rep cost to advance Tier remains 6 regardless of Turf. |
| BLD-T73 | Spider uses Foresight to Assist teammates during a Score. | PASS — maximum two uses per Score without Stress; each use still requires a description of prior preparation and a valid Assist contribution. |
| BLD-T74 | A PC uses an eligible Special Armor ability, then enters Downtime. | PASS — ability must be owned and its trigger must match; mark Special Armor. Armor uses recover during Downtime; if the ability text says beginning of Downtime, honor that more specific timing. |
| BLD-T75 | Shadows have Synchronized; two different PCs in a Group Action each roll a 6. | PASS — multiple 6s from different participant rolls count as a Critical. Do not use multiple 6s from one PC's single roll as a substitute for the stated different-roll condition. |

## 3. Corrections and implementation notes

- Added a dedicated `ARCANE_AND_CRAFTING_RUNTIME.md` with Magnitude, Ritual source/learning/performance, Invention, Crafting, Modification, Drawbacks, and Alchemical item runtime procedures.
- Added `ABILITY_RUNTIME_MATRIX.md` with trigger, effect, cost/scope, and boundary summaries for the seven core PC Playbooks and six core Crew Types.
- Added runtime dispatch in `RUNTIME_PROTOCOL.md`: load ability/arcane references only when the relevant event occurs; do not scan the full catalogue on every player utterance.
- Corrected the prior Armor timing mistake: Full Player's Kit v8.2 places Armor recovery in Downtime; several Special Armor abilities specify restoration at the beginning of Downtime. The earlier claim that Downtime itself does not restore Armor was withdrawn. The official SRD Resistance & Armor webpage instead says recovery occurs when Load is chosen for the next Score; this source conflict is now explicitly left OPEN in R-005. The candidate baseline provisionally follows Player's Kit v8.2, not a claim that the two texts are equivalent.
- Clarified Deadly's initial-creation exception and Fiends' Wanted/Turf/Rep limits.

## 4. Official source cross-checks

- [Magnitude](https://bladesinthedark.com/magnitude): dimensions, examples, Fortune Roll use, non-additive judgment.
- [Rituals](https://bladesinthedark.com/rituals): source, learning, ritual questions, performance cost, danger/effect rolls.
- [Crafting](https://bladesinthedark.com/crafting): invention, crafting roll, modification thresholds, drawbacks.
- [Resistance & Armor](https://bladesinthedark.com/resistance-armor): Armor vs Resistance and next-Score Load recovery reference.
- [Full Player's Kit v8.2](https://bladesinthedark.com/sites/default/files/blades_playerkit_v8_2.pdf): Downtime Armor recovery, PC/Crew abilities, action rating and special ability text.

## 5. Validation boundary

75/75 is a pass for the fixed synthetic matrix only. It is not a live-play pass and does not validate every selected ability combination, every formula/ritual, optional content, or campaign-specific interpretation. The system remains `candidate`.