# Daggerheart Core Runtime Desk Test — Batch 2

- Date: 2026-11-28
- Baseline: Daggerheart Core Set; SRD 2.0 (2026-08-25)
- Scope: CORE_ONLY
- Method: deterministic desk simulation / logic review of DH-T16–DH-T30 against the local procedure. Not software automation and not complete Core Rulebook verification.
- Outcome: 15/15 assertions reviewed and passed as written. See caveats below.

| ID | Test input | Result |
|---|---|---|
| DH-T16 | PC attack targets adversary with Difficulty 14 | Pass: attack roll uses adversary Difficulty. |
| DH-T17 | Adversary attack with modifier +3 vs Evasion 14; d20=11 | Pass: 14 total hits; GM d20 procedure, not Duality Dice. |
| DH-T18 | Adversary action is not an attack and PC can react | Pass: avoid defaulting to a separate adversary action roll; use PC reaction procedure where applicable. |
| DH-T19 | GM adjudicates high-risk adversary action not covered by attack procedure | Pass: single d20 against Difficulty can be used per GM procedure, with Fear spend for applicable Experience before roll. |
| DH-T20 | Damage 4; Major Threshold 5; damage after reductions 0 | Pass: below threshold marks 1 HP if positive; 0 or less marks none. |
| DH-T21 | Damage equals Major and is below Severe | Pass: marks 2 HP. |
| DH-T22 | Damage equals Severe | Pass: marks 3 HP; optional Massive Damage remains disabled unless binding enables it. |
| DH-T23 | Severe damage reduced by one Armor Slot | Pass: severity reduced one step only, Severe to Major; slot is not repeatedly applied. |
| DH-T24 | Physical Resistance before Armor Slot reduction | Pass: Resistance is applied before threshold/armor severity reduction in the local procedure. |
| DH-T25 | Direct Damage | Pass: Armor Slots cannot reduce Direct Damage. |
| DH-T26 | Multiple simultaneous damage sources | Pass according to local procedure: total simultaneous damage before threshold comparison; keep separate when timing/source rules require. |
| DH-T27 | Action Roll in danger includes movement up to Close | Pass: movement included in action; procedure not generalized to no-roll Very Far movement. |
| DH-T28 | Hidden PC attacks | Pass: attack breaks Hidden under standard rule; specific features may override. |
| DH-T29 | More than five Domain Cards | Pass: Loadout capped at five; Vault inactive; ancestry/subclass/community cards excluded from this limit. |
| DH-T30 | Recall card outside rest with full Loadout | Pass: pays Recall Cost in Stress and moves a card out if needed. |

## Caveats

- Results are deterministic desk simulation only, not code-level tests.
- Damage aggregation and mixed damage-type details should be checked against the official source when a specific ability/card creates an exception.
- Complete Core Rulebook text has not been supplied; SRD-based verification boundary remains.
- Continue DH-T31–DH-T45.
