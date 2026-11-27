# GM PACKET｜Synthetic test-only state

> TEST_ONLY_NON_CANON. Nothing in this packet is a real Campaign fact or character state.

## Binding
yaml:
  active_system:
    system_id: triangle_agency
    ruleset_version: 中文 v22
    campaign_id: zarek
    module_id: ROLL_TEST_ONLY
  binding_status: active
  system_entry_verified: true
  adjudications_entry: Campaigns/Zarek/RULE_ADJUDICATIONS.md

The fixture uses the real Zarek Q04 scope only as a rule-binding test. No real Zarek resource or character value is read or changed.

## Synthetic state
- A fictional Agent is in a fictional test location.
- Current QA before the test: Empathy 0/3 (2 QA previously spent), Initiative 0/1 (1 QA previously spent), Subtlety 1/3.
- Current Chaos Pool: 0.
- For the burnout example, the applicable test-only Q04 binding is active.
- The Agent has a test-only set of three already-spent QA points eligible for Circle Back.
- No real Playwall-specific ability is authorized in this fixture; only the synthetic A7 document defined below is authorized for ACTION_10.
- No module, NPC, clue, map or story content exists beyond the action statements.

## Test-only event rules
- All dice are deterministic test inputs, not actual random rolls.
- All resource changes are in-memory only. Do not write to Campaign Resource Ledger, Session Log, Runtime State or character card.
- The test state is discarded after ORACLE review.
- The UI is tested as a player projection contract only; no live component is deployed.


## Synthetic unlocked Playwall document for ACTION_10 only

- A test-only authorization record confirms code A7 is unlocked and its exact synthetic document has been retrieved and version-checked.
- Synthetic document rule (invented only for this test; NOT real Triangle Agency content): this ability requires a special 2d6 dice pool and a separate success threshold instead of the normal pool.
- The synthetic document is available only to test the pipeline boundary. Do not treat it as a real Playwall code, ability, rule, or Campaign fact.
