# Blades in the Dark｜Synthetic Runtime Execution Report

> Date: 2026-11-28  
> Fixture: `BITD_CANDIDATE_V01`  
> Status: SELECTED SYNTHETIC CASES EXECUTED / LIVE PLAY NOT PERFORMED  
> Scope: The cases below were desk-executed against the current Rule Index, Runtime Manual and Runtime Protocol using fixed inputs. This is a manual deterministic consistency check, **not** automated code testing, independent peer review or a real table-play acceptance.

## 1. Execution result

- Executed: 16 selected cases.
- Passed: 16.
- Failed: 0.
- Deferred: Full 54-case regression matrix, actual character/crew sheet audit, and real session.
- Campaign state: none. All examples are synthetic and TEST_ONLY_NON_CANON.

A pass means the declared procedure and state arithmetic were applied consistently in that scenario. It does not prove the rule summary is complete or correct for every exception.

## 2. Executed traces

| Test ID | Fixed input | Runtime trace | Result |
|---|---|---|---|
| BLD-T01 | PC crosses a low fence with no danger or troublesome obstacle | No Action Roll. The GM simply resolves the movement in the fiction. | PASS |
| BLD-T05 | PC and NPC directly oppose each other; Action Roll = 2 | The NPC wins the exchange. Its action manifests as a consequence for the PC. No second NPC Action Roll is generated for the same exchange. | PASS |
| BLD-T07 | Base Position/Effect = Risky/Standard; PC proposes Desperate/Great | GM has already announced the base values. The trade is accepted only because the described route genuinely increases danger and potential reach; no numerical conversion formula is applied. | PASS |
| BLD-T08 | Resistance attribute pool = 3d; highest die = 4 | Stress cost = 6−4 = 2. The GM reduces the stated consequence by one level; the consequence is not erased unless the GM's chosen resistance outcome says so. | PASS |
| BLD-T10 | PC has relevant Standard + Heavy Armor loaded; incoming Level 2 Harm | Standard Armor reduces Level 2 to Level 1; Heavy Armor can be marked as a second reduction to Level 0. The same consequence is not also resisted. | PASS |
| BLD-T12 | 0d Action Roll; dice are 2 and 6 | Roll 2d and take the lower result: 2. No Critical is produced from the 0d rule. | PASS |
| BLD-T21 | Long-Term Project Roll = Critical | Advance 5 clock segments. This uses the official v8.2 figure and the locally logged correction for the conflicting Chinese SRD line. | PASS |
| BLD-T22 | PC has used both formal Downtime Activities, then visits a contact and asks questions | Visit, conversation and ordinary information gathering remain available; they do not consume a third formal Downtime Activity. | PASS |
| BLD-T23 | Crew Heat = 7; new Score adds 5 Heat | Total = 12. Wanted Level rises by 1; 9 Heat is cleared and 3 excess Heat carries over. | PASS |
| BLD-T24 | Wanted Level = 0; Entanglement roll | Roll 2d and take the lower die, then consult the Heat band. | PASS |
| BLD-T25 | Crew has 3 Turf and Strong Hold; Rep reaches 9 | Required Rep = 12−3 = 9. Pay new Tier × 8 Coin to advance one Tier; reset Rep and reduce Hold to Weak. | PASS |
| BLD-T26 | Crew enters War at Faction Status −3; no War-protecting Crew Ability | Each Score adds +1 Heat; Crew temporarily loses 1 Hold; each PC receives only 1 Downtime Activity. If pre-war Hold was Weak, Tier temporarily falls and is restored after War ends. | PASS |
| BLD-T38 | PC accepts Devil's Bargain for +1d and Pushes for +1 Effect | Legal combination: the Devil's Bargain provides the extra die; Push for +1 Effect costs 2 Stress. | PASS |
| BLD-T46 | PC loads Standard Armor and Heavy Armor | Standard Armor costs 2 Load; Heavy adds 3 Load (5 total). The PC cannot claim this protection without carrying it in the current Score Loadout. | PASS |
| BLD-T48 | PC recovers without a separate healer | The recovering PC spends their own Recover Activity, takes 2 Stress for self-treatment, and makes the normal recovery roll. | PASS |
| BLD-T50 | PC A treats PC B's Harm | PC B spends the Recover Activity. PC A does not spend one of their own Downtime Activities to provide the treatment. | PASS |
| BLD-T54 | Lurk with Shadow faces a consequence from detection/security measures | Special Armor can resist the specified kind of consequence; alternatively Push Yourself can be used for athletics/stealth as written. The ability is not treated as general-purpose armor. | PASS |

## 3. Corrections made during validation

1. Corrected the interaction between Push Yourself and Devil's Bargain: a Devil's Bargain die can accompany a Push for +1 Effect, but cannot accompany a Push for the same +1d.
2. Added the Lurk's Shadow ability after re-reading the source Playbook list.
3. Corrected Coin state into three separate locations: loose personal Coin, Crew Lair/Vault capacity, and personal Stash. Bulk Coin carried physically occupies Load.
4. Clarified that Heavy Armor is additional Load on top of Standard Armor, and that armor must be in the current Loadout.
5. Added Crew Creation, Hunting Grounds, Claims and Coin storage to the runtime contract and regression suite.

## 4. Remaining validation work

- Execute the rest of `CORE_RULE_RUNTIME_REGRESSION.md` (including Cohort, faction status, full score/downtime transitions and ability edge cases).
- Lock the exact ruleset version for a future Campaign. The Chinese SRD page does not clearly identify its revision number; the official Full Player's Kit v8.2 is a cross-check aid, not a substitute for choosing a precise rules edition.
- Before play, verify the actual PC Playbook, Crew Type, selected abilities, Crew upgrades, claims, gear and any optional playbook against the exact sheet used by that Campaign.
- Validate the Solo/one-player table adaptations separately. No official one-player rules variant has been confirmed.
- Run a short live session and review pacing, clarity, consequence fairness, bookkeeping load, faction continuity and how often rule lookup interrupts play.

## 5. Activation gate

**Current state remains `candidate`.** Selected synthetic cases pass, but this report does not authorize a formal Campaign and does not claim successful live-play validation.
