# Daggerheart Core Runtime Desk Test — Batch 1

- Date: 2026-11-28
- Baseline: Daggerheart Core Set; SRD 2.0 (2026-08-25)
- Scope: CORE_ONLY
- Method: manual deterministic desk simulation / logic audit of DH-T01–DH-T15 against the local runtime procedure and SRD 2.0 reference; not executable software tests and not a full Core Rulebook audit.
- Outcome: 15/15 test cases passed as written in the test matrix; no runtime code was executed. These results validate consistency of the reviewed procedure at these test boundaries only.

## Cases

| ID | Test input (deterministic) | Result |
|---|---|---|
| DH-T01 | Difficulty 12; total 13; Hope Die 8, Fear Die 5 | Pass: Success with Hope; PC Hope +1; no automatic GM Move. |
| DH-T02 | Difficulty 12; total 13; Hope Die 4, Fear Die 9 | Pass: Success with Fear; GM Fear +1; success retained; consequence and spotlight shift. |
| DH-T03 | Difficulty 12; total 11; Hope Die 8, Fear Die 5 | Pass: Failure with Hope; PC Hope +1; softer consequence. |
| DH-T04 | Difficulty 12; total 11; Hope Die 4, Fear Die 9 | Pass: Failure with Fear; GM Fear +1; major consequence. |
| DH-T05 | Hope Die 7, Fear Die 7 | Pass: Critical; automatic success, PC Hope +1, clear Stress 1; attack-critical damage handled separately. |
| DH-T06 | Reaction roll with Hope Die higher | Pass: no Hope/Fear resource change and no extra GM Move solely from die polarity. |
| DH-T07 | Reaction Critical | Pass: ignore the effect being avoided; no Hope gain or Stress clearing. |
| DH-T08 | Stress slots full; consequence requires marking Stress | Pass: overflow follows the general Stress procedure and marks HP; source recorded. |
| DH-T09 | Stress full; move explicitly requires Stress payment | Pass: cannot pay; HP-marking overflow does not substitute for payment. |
| DH-T10 | Mark final Stress slot | Pass: Vulnerable applies; fullness-derived Vulnerable ends after clearing at least one Stress. |
| DH-T11 | One Advantage, two Disadvantages | Pass: pairwise cancellation leaves one Disadvantage die; never roll both. |
| DH-T12 | Multiple Help an Ally contributors | Pass: each contributor rolls their d6; action-taker adds only the highest applicable Advantage die. |
| DH-T13 | Group Action: one helper success, one helper failure | Pass: +1 and -1 net to Leader's roll; helper Reactions do not generate Hope/Fear. |
| DH-T14 | Tag Team chooses one of two results | Pass: chosen result governs; resource polarity uses participant count; Countdown counts one Action Roll. |
| DH-T15 | Successful Tag Team attack with mixed damage | Pass per current matrix: damage combined as one source; damage-type selection follows the matrix assertion. This boundary should be rechecked against the official source if disputed. |

## Limits / follow-up

- No code-level automated execution; this is a human-readable deterministic audit.
- The underlying official Core Rulebook has not been supplied and is not fully cross-checked.
- Continue with DH-T16–T30, focusing attack, damage, range, domain cards, rest and recovery.
- Then DH-T31–T45, countdown, enemy features, Core/expansion binding and final HP.
- Do not promote the system from candidate based on this batch alone.
