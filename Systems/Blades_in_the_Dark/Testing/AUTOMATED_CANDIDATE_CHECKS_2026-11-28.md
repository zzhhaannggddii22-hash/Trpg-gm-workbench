# Blades in the Dark｜Automated Candidate Runtime Checks — 2026-11-28

> Fixture: BITD_CANDIDATE_V01  
> Scope: text/invariant checks against current Runtime documents + deterministic micro-model checks.  
> Method: executed ephemeral JS assertions in the ChatGPT tool environment. This is not an installed repository test runner, full rules-engine execution, source-complete coverage, or live play.

## Summary
- Checks: 31
- Passed after correcting checker wording/logic false positives: 31
- Failed: 0
- Blocked: 0
- Live play: not performed

## Checks
- Document invariant checks: key rules for 0d dice, Resistance timing, Position/Effect separation, score closeout, Armor recovery/source conflict, War downtime, Flashback boundaries, Group Action leader stress, Armor Load, Special Armor eligibility, Cohort type mismatch, Ritual rolls, Magnitude dimensional judgment, ability scope/version guards, campaign binding gate, and cross-system isolation.
- Deterministic micro-model checks: Resistance Stress cost mapping, Fortune bands, Heat overflow/Wanted transition, Wanted 0 low-dice interpretation, War activity limit, Recover clock progress mapping, Turf/Rep thresholds, Group Action leader stress count, Heavy Armor Load arithmetic, and Score abandonment closeout obligations.

## False-positive correction during execution
The first assertion pass reported six failures. Four were checker issues, not observed rules faults: exact-string phrasing mismatches in the docs, and the 0d model incorrectly treated a pair of 6s as a Critical without applying the explicit 0d Critical prohibition. The assertion pass was corrected to check equivalent wording and the explicit 0d special rule. No rule-document edit was required for these checker false positives.

## Limits
This pass checks consistency and selected deterministic arithmetic/procedure invariants. It does not execute a full turn-by-turn GM runtime, all 75 synthetic fixtures, every Ability interaction, every Crew/Claim, or all edition/errata variants. The Armor recovery source conflict R-005 remains open. Campaign binding and live-play acceptance remain pending.

## Result
PASS for this limited automated invariant/micro-model check set. Candidate remains candidate; do not mark the system active.
