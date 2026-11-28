# Daggerheart Combat Transaction Test — Round 2

- Date: 2026-11-28
- Binding: Core Set / CORE_ONLY; single PC, Tier 1 hypothetical; no single-PC house-rule changes
- Source stat block: Acid Burrower, Tier 1 Solo, local Core Set adversary JSON
- Method: deterministic scene/transaction simulation. This validates tracking and adjudication sequence, not encounter balance or player experience.

## Encounter setup

Single PC versus Acid Burrower. Objective is to recover a marked object and escape, not kill the adversary. Scene includes an unstable floor and a short Standard Countdown. The solo adversary is a 5-BP option against a one-PC baseline budget of 5 (3×1+2); this equality is a budget match only, not evidence of balanced difficulty for a single PC.

The Acid Burrower local stat block contains Difficulty 14, 8 HP, 3 Stress, thresholds 8/15, Claws +3 (1d12+2 physical), Relentless (3), Earth Eruption, Spit Acid and Acid Bath.

## Transaction sequence

### T1 — PC Action Roll
- Player declares objective, approach and risk.
- GM identifies trait and difficulty, confirms any Experience/feature before roll.
- Deterministic test input: total 15 against Difficulty 14, Fear die higher.
- Result: success with Fear. PC succeeds; GM receives Fear; consequence must alter position/time/pressure rather than cancel success.
- Countdown: one action-roll advance, once.
- Assertion: no duplicated countdown advance; transaction logged.

**Outcome:** Pass.

### T2 — Adversary feature use
- GM chooses Earth Eruption only if it fits the established scene.
- The Burrower marks Stress for its feature; affected creatures make Agility Reaction Rolls.
- If the PC fails, knockdown/Vulnerable consequence is applied as written; Reaction result does not generate Hope/Fear.
- Assertion: feature cost and Reaction result are tracked separately; avoid rolling a separate adversary Action Roll.

**Outcome:** Pass.

### T3 — PC response and escape objective
- PC uses scene geometry and a consequential Action Roll to reach/secure the object and withdraw.
- GM resolves the declared intent, range and obstacle; does not require defeating all adversary HP.
- Countdown advances once for this Action Roll.
- If escape objective is fulfilled, scene may end without forcing further attacks.

**Outcome:** Pass.

## Review

- The local Solo stat block can be selected within the nominal one-PC BP baseline, but BP alone does not demonstrate balance.
- A single-PC battle with a Tier 1 Solo is still a potentially lethal design. For future single-PC test sessions, objective, terrain, escape route, enemy feature exposure and pre-telegraphed risk matter; don't silently adjust baseline rules.
- Runtime transaction tracking worked conceptually across roll, resource, reaction and countdown. No executable software or actual table session was involved.
- Outcome: transaction flow Pass; encounter balance and real play feel NOT VERIFIED.
