# Blades in the Dark｜Integrated Engine Simulation (Subset) v1

> Date: 2026-11-28  
> Status: limited PASS; system remains candidate  
> Harness: `Testing/ENGINE_SIMULATION_V1.js`

## Result
- Harness test cases: 26 declared in the committed standalone script (the standalone script itself has not been executed via a Node runtime in this chat).
- Independent inline replay: 23 assertions/groups executed; 23 passed; 0 failed.
- Fuzz: 1,000 Heat boundary inputs included in the inline replay.
- This is a deterministic procedure/state model subset, not a complete Blades rules engine, automated campaign simulator, or proof of all source rules.

## Coverage exercised in inline replay
Action/Fortune result bands and Critical; 0d and negative pools; Effect progress and Critical increase; Resistance stress cost; Load threshold gates; Heat threshold/reset and fuzzed boundary inputs; War Downtime budget; Clock gain mapping; Rep/Turf arithmetic; Claim income during War; Cohort Quality and type gate; Engagement result bands; independent Ritual danger/manifestation rolls; Magnitude dimensions; Invention/Crafting/Modification routing; Special Armor permission gate; cross-system state isolation; Flashback cost mock; Score closeout order; Healing Clock threshold mock; Harm bounds; Downtime activity budget consumption.

## Limits and cautions
- A repository harness file has been added, but execution of that exact file by Node is not available in this chat environment. The inline replay was independently run against the same intended test logic; it is not a proof that the committed source runs without syntax/runtime errors.
- Heat model uses threshold crossing (Heat 9+) to increase Wanted and reset Heat to 0, with no excess carry in this simplified model; verify against campaign's exact version before binding.
- Several tests validate routing/invariants rather than complete fictional procedures. Healing Clock, Flashback, Group Action, Magnitude, Position/Effect, and crafting flows are partial mocks.
- Resistance, Position, Effect, Armor and ability interactions are not comprehensively modeled.
- Armor recovery R-005 remains an open source conflict.
- No GM narrative quality, information fairness, campaign persistence, or live play validated.

## Acceptance
PASS for the bounded subset represented by the inline replay. Not a full engine certification; Campaign preflight and live play remain the next meaningful validation.
