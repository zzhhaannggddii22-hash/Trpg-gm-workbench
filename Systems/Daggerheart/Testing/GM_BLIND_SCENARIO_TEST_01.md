# Daggerheart GM Blind Scenario Test — Round 1

- Date: 2026-11-28
- Binding: Core Set / CORE_ONLY; Level 1 hypothetical PC; no expansions
- Method: blind prompt scenario GM simulation against local GM Skill and runtime rules, without pre-scripted solution; assess adjudication, information clarity, risk framing, rule invocation and player agency.
- Scope caveat: internal simulation, not an independent external blind tester or actual player session.

## Scenario A — Social leverage / uncertain outcome

**Setup:** PC tries to persuade a gatekeeper to delay a patrol. The PC has a plausible but incomplete explanation and offers a small favor. Gatekeeper is anxious, not malicious.

**Observed GM behavior:** The simulation identified stakes and a plausible consequence; it did not require a roll for merely asking factual questions, but used a roll for the consequential persuasion attempt. It offered a consequence framed around patrol timing and the gatekeeper's risk rather than a flat denial.

**Assertions:** no forced roll for low-risk dialogue; roll when stakes are uncertain; clear consequence; NPC motive-based response; player choice preserved.

**Outcome:** Pass.

## Scenario B — Exploration / investigation

**Setup:** PC searches a warehouse for signs of a recent unusual event. The scene has three observable leads, one hidden danger and a noisy environment.

**Observed GM behavior:** The simulation directly provided perceptible facts, separated inference from confirmed facts and presented multiple ways to investigate. A failed roll changed time/noise exposure while leaving another avenue available. No single clue was hard-locked behind one roll.

**Assertions:** direct observation is not gated; uncertainty is localized; failure moves situation; multiple paths; no excessive document micro-investigation.

**Outcome:** Pass.

## Scenario C — Tactical encounter / non-combat objective

**Setup:** A Tier-appropriate adversary guards a moving target. PC objective is to recover an object and escape, not defeat all enemies. Environmental obstacle and countdown are present.

**Observed GM behavior:** GM simulation tracked Spotlight, described enemy motive and objective, made the environment actionable, and used a meaningful threat. It avoided a static HP race. Encounter setup requires checking BP and exact stat blocks before live use; this scenario did not claim numeric balancing was validated.

**Assertions:** objective beyond defeating enemies; environment matters; Fear use has motive; movement and reactions remain rules-consistent; no fabricated stat-block details.

**Outcome:** Pass with numeric balancing unverified.

## Review findings

1. Scenario-level GM guidance is reasonably coherent, but live state tracking and exact rules are not tested by this simulation.
2. Current runtime has no session-state template specifically optimized for tracking HP/Stress/Armor/conditions/Countdown/domain-card uses and enemy Pools. Preflight asks for snapshots, but a lightweight session ledger would reduce omission risk.
3. Core README and index metadata still said testing was pending/0 executed after desk tests; these are stale. Corrected in the accompanying documentation update.
4. Next phase: create a compact runtime ledger and do a controlled short-scene test with real user interaction. Avoid building a large test framework.

## Test status

- A: Pass
- B: Pass
- C: Pass (numeric encounter validation not covered)
- External player blind test: not yet
- Actual live short-session: not yet
