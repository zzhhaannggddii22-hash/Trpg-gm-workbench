# Daggerheart Core Runtime Desk Test — Batch 3

- Date: 2026-11-28
- Baseline: Daggerheart Core Set; SRD 2.0 (2026-08-25)
- Scope: CORE_ONLY
- Method: deterministic desk simulation / consistency review DH-T31–DH-T45. Not software automation or full-book validation.
- Outcome: 15/15 assertions reviewed and passed as written in the test matrix. The matrix is now 45/45 desk-simulated; this is not equivalent to programmatic or full Core Rulebook acceptance.

| ID | Test input | Result |
|---|---|---|
| DH-T31 | After three consecutive short rests, party tries another short rest | Pass: next rest must be long. |
| DH-T32 | Short Rest interrupted | Pass: no short-rest benefits or downtime moves. |
| DH-T33 | Long Rest interrupted | Pass: short-rest benefits only; long-rest benefits not applied. |
| DH-T34 | Long Rest Fear increase with 3 PCs and roll 1d4=2 | Pass: gain 5 Fear, respecting cap 12. |
| DH-T35 | Standard Countdown advanced after one action transaction | Pass: advances once; no duplicate advance for one action transaction. |
| DH-T36 | Dynamic Countdown has distinct Progress / Consequence triggers | Pass: follow its separate progression triggers; don't apply both tracks to one result unless explicitly instructed. |
| DH-T37 | GM pays Fear to Spotlight and separately uses enemy Fear Feature | Pass: feature cost is separate; no double-counting prior payment. |
| DH-T38 | Two adversaries share a token Pool | Pass: tokens belong to shared Pool; clear at scene end as specified. |
| DH-T39 | Enemy Evolution condition occurs again after triggering | Pass: once per scene unless stat block explicitly overrides. |
| DH-T40 | PC marks last HP | Pass: choose Death Move (Blaze of Glory, Avoid Death, Risk It All) per procedure. |
| DH-T41 | Core Only character creation attempts an expansion class | Pass: blocked; expansion option not loaded. |
| DH-T42 | Core Only character selects Dread Domain | Pass: blocked; expansion cards not loaded. |
| DH-T43 | PC equips item above their Tier | Pass: blocked absent an explicit override. |
| DH-T44 | Two instances of same damage Resistance | Pass: same-type resistance doesn't stack. |
| DH-T45 | Hope Feature costs 3; action roll produces Hope +1 | Pass: newly gained Hope may be applied immediately to that same roll's feature timing as recorded in the local procedure. |

## Limits / follow-up

- All 45 tests are desk-simulated, not code-level automated tests.
- Test T15, T26 and T36 are higher-complexity boundaries and should be rechecked against exact official rule wording/cards when relevant.
- The Core Rulebook has not been supplied and full-book cross-check remains incomplete.
- Blind GM testing and short-scene testing remain required before moving from candidate.
