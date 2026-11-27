# Review Handoff｜Roll Pipeline v3

> Status: DESIGN ONLY / NOT APPROVED FOR LIVE RUNTIME
> Target branch: design/roll-resolution-and-triangle-dice-ui-2026-11-27-v3-final
> Base: current main at branch creation; verify PR base/head before review
> Supersedes: PR #52 original draft design (rejected review)

## Scope of this revision

This revision processes the parts that do not require Playwall-specific ability adjudication.

Included:
- remove mandatory activation of the unapproved roll protocol from the main GM Skill;
- generic rule routing order and explicit requirement for a real, verified system Rule Access Map;
- Ask the Agency base request gates and base 6d4 flow;
- ordinary Anomaly Ability base flow only when the complete ability text and eligibility are verified and no deferred override applies;
- natural triple ascension as a distinct raw-dice branch;
- ordinary Burnout / QA / final dice / Chaos path when natural ascension did not trigger;
- Conflict Resolution as a distinct multi-participant, multi-round path;
- separation of adjudication, resource application, publication and read-back verification;
- idempotency evidence and interruption recovery requirements;
- recipient-authorized player projection using view_id + monotonic revision;
- schema v2 excludes internal event IDs and ledger Entry IDs;
- explicit Playwall deferral register.

## Explicit non-goals

No Playwall-specific ability, unlock tier, special dice pool, extra die/3, special cost timing, no-roll clause, alternate success condition or override is implemented. These must remain marked:

UNSUPPORTED_PENDING_RULE_REVIEW

Conflict Resolution is rule-routed but intentionally text-fallback-only until a dedicated multi-participant/multi-round projection exists.

## Required review files

1. GM_Training/SKILL.md
2. GM_Training/ROLL_RESOLUTION_PROTOCOL.md
3. Systems/Triangle_Agency/Rule_Reference/02_DICE_RESOLUTION_PROTOCOL.md
4. Systems/Triangle_Agency/Rule_Reference/03_ROLL_RULE_ACCESS_MAP.md
5. Systems/Triangle_Agency/Rule_Reference/PLAYWALL_DEFERRED_REGISTER.md
6. Systems/Triangle_Agency/Dice_UI/README.md
7. Systems/Triangle_Agency/Dice_UI/roll-event.schema.json
8. Systems/Triangle_Agency/Rule_Reference/README.md
9. Systems/Triangle_Agency/README.md
10. Runtime protocol sections referenced by the prior review, especially §14.14, §14.19 and §14.20, plus current Resource Ledger and Session Log standards.

## Required checks

### P0
- Confirm main Skill no longer mandates an unapproved design protocol.
- Confirm raw natural triple ascension branches directly to success, zero Chaos and player reward choice; it must not fall through ordinary Burnout/QA/Chaos.
- Confirm resource writes have a field-level idempotency key and proof; Entry ID alone is not proof.
- Confirm player projection contains no internal event IDs, Session/Event IDs, ledger Entry IDs, transaction keys, batch IDs or GM-only content.

### P1
- Confirm Ask request legality, causal-chain and freedom-of-will gates; location exhaustion is tied to the actual location and remaining task time.
- Confirm ordinary Anomaly Ability 6d4 only where the complete text says so; unsupported overrides stop safely.
- Confirm Conflict Resolution remains separate, tracks participants and synchronous rounds, and is not represented by the single-pool schema.
- Confirm Zarek Q04 desk ruling is campaign-scoped, not global.
- Confirm no trusted random source means player-roll path or explicit consent to MODEL_GENERATED; never silently switch.
- Confirm latest Resource Ledger topology and current main Runtime are not contradicted.

### Schema and UI
- Validate JSON Schema Draft 2020-12.
- Reject empty/invalid dice, invalid d4 faces, duplicate slot numbers (upstream semantic validator), phase contradictions, missing choices in AWAITING_PLAYER_CHOICE, and pending resources with numeric after values.
- Ensure private information cannot enter through a legal string: authorization must occur upstream in player_reply_payload projection.
- Reject stale revisions; same revision with different content is conflict.
- UI failure must fall back to text from the exact same projection.
- Keyboard, screen reader and reduced-motion checks remain required before UI release.

### Recovery
Test at least:
1. adjudication frozen, before any transaction;
2. ledger applied, Session Log not yet published;
3. transaction submission timed out / receipt lost;
4. publication receipt lost;
5. partial resource-field application;
6. read-back mismatch or unavailable evidence.

Expected: no reroll, no repeated resource application, no false persistence claim; isolate only affected fields and retain independently confirmed results.

## Decision requested

Return APPROVE / APPROVE WITH CHANGES / REJECT for this design revision, with P0/P1/P2/P3 findings. Do not merge, do not enable runtime, do not modify main. A passing design review does not itself authorize live activation; user approval and separate implementation/acceptance remain required.
