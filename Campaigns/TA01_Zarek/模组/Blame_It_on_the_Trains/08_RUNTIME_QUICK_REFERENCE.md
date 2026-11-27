# Runtime Quick Reference｜Blame It on the Trains

> GM-only. Field navigation only; does not replace source text, rules, Campaign Binding, or the Player-Facing Gate.

## Readiness

- Artifact：DELIVERED
- Source / Rule Validation：BLOCKED
- Single-player feasibility：PARTIAL / RULE-MAPPED v2; see 07 §10
- Runtime：NOT STARTED
- Preflight：NOT STARTED / WAITING FOR USER “开始”
- User start authorization：WAITING FOR “开始”

## Mandatory assembly order (before any player-facing scene)

1. `Campaigns/TA01_Zarek/SYSTEM_BINDING.md` — confirm triangle_agency / Chinese v22.
2. `Campaigns/TA01_Zarek/RULE_ADJUDICATIONS.md` — load only Campaign-approved Q01–Q05 rulings and scope.
3. Current formal character card — verify current character state and equipment.
4. Campaign handoff / Campaign README — recover only confirmed cross-module facts and pending disputes.
5. This module README and `07_SOURCE_AND_RULE_CROSSCHECK.md` — verify lifecycle and open validation gates.
6. `10_PLAYER_FACING_GATE.md` — mandatory resident output constraint for the entire active Session.
7. `01_GM_PREP.md` and `02_NAME_INDEX.md` — load only the materials needed for the current action. For first contact, use 01 §4–§5; for single-agent adaptation and source alternatives, use 01 §7–§8; for rescue/encounter, use 01 §13; for station Chaos/d44 effects, use 01 §15. Mechanical mapping and solo-path test evidence: `07_SOURCE_AND_RULE_CROSSCHECK.md` §10.
8. `03_RUNTIME_STATE.md`, latest Session Log and `05_PLAYER_NOTES.md` — restore actual dynamic state and player knowledge.
9. `09_RESOURCE_LEDGER.md` — reconcile only resources required for the current action; never copy its balances into Runtime State.
10. Resolve blockers and run Preflight for this specific Session. Wait for the user's explicit “开始”.

## Authority map

| Need | Authority |
|---|---|
| Fixed module facts / GM preparation | `01_GM_PREP.md` |
| Entity IDs and aliases | `02_NAME_INDEX.md` |
| Current scene / spatial state / NPC dynamic state | `03_RUNTIME_STATE.md` |
| Event history | `04_SESSION_LOG.md` / `Sessions/` |
| Player-known facts | `05_PLAYER_NOTES.md` |
| Resource transactions | `09_RESOURCE_LEDGER.md` |
| Source/rule validation | `07_SOURCE_AND_RULE_CROSSCHECK.md` §1–§7 |
| Disclosure permissions | `10_PLAYER_FACING_GATE.md` §1–§5 (resident constraint) |
| System rules | Campaign System Binding + Chinese v22 original |
| Campaign rulings | Campaign RULE_ADJUDICATIONS.md |

## Live execution reminders

- Follow the player's actual route; never force a prepared route.
- Do not infer NPC knowledge from GM knowledge.
- Keep fixed source facts, Campaign rulings, GM adaptation, inference and UNKNOWN separate.
- Do not use unverified dice tables, Chaos effects, ability rules, Harm/Domain thresholds or resource values.
- Ordinary resource balances must be publicly reported where the system requires; hidden facts remain GM-only.
- Player Notes only records facts actually learned by the character.
- Runtime State references the latest verified ledger checkpoint; it does not maintain a second resource balance.
- Every state-changing event gets a stable Event ID; cross-file persistence is idempotent and readback-verified.

## Runtime update triggers

- Scene/location/layer movement, NPC position/knowledge changes, key item transfer, commitments, trigger changes: update Runtime State + Session Log.
- Resource changes: Resource Ledger only; Session Log references Entry ID.
- Player learns a fact: update Player Notes with source, event and confidence.
- A correction never silently erases what was already presented; preserve the event and record the remedy.
