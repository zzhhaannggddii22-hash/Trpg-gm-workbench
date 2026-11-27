# Runtime State｜Blame It on the Trains

> GM-only。当前为未开团基线，不代表任何场景、事件或玩家行动已经发生。动态角色资源只引用人物卡/Resource Ledger，不在本文件维护第二份余额。

## 1. Identity and lifecycle

- Campaign ID：zarek
- System ID：triangle_agency
- Ruleset：中文 v22
- Module ID：blame_it_on_the_trains
- Module lifecycle：DELIVERED / VALIDATION BLOCKED / NOT STARTED
- Session：NONE
- Resume Mode：NEW START（仅在未来通过 Preflight 后建立）
- Preflight：NOT STARTED / BLOCKED
- Start authorization：WAITING FOR USER “开始”
- Runtime Revision：R0 / BASELINE
- Last confirmed event ID：NONE
- Last presented narrative node：NONE
- Last answered event ID：NONE
- Pending player action：NONE

## 2. Readiness vector

| Dimension | State | Authority |
|---|---|---|
| Artifact delivery | DELIVERED | 固定仓库 Commit 与交付清单 |
| Source validation | BLOCKED | 07_SOURCE_AND_RULE_CROSSCHECK.md |
| Prep rule validation | BLOCKED | 07_SOURCE_AND_RULE_CROSSCHECK.md |
| Single-player feasibility | NOT TESTED | 07_SOURCE_AND_RULE_CROSSCHECK.md |
| Runtime schema | BASELINE / NOT ACTIVE | 本文件与通用 Runtime State Template |
| Prep QA | NOT RUN | 07_SOURCE_AND_RULE_CROSSCHECK.md |
| Preflight | NOT STARTED / BLOCKED | 每次实际开团时单独记录 |
| Player authorization | WAITING | 用户明确“开始” |

## 3. Authority references (no duplicated mutable balances)

| State | Authoritative source | Runtime reference |
|---|---|---|
| Character attributes, QA caps/current QA, persistent resources, harm, demerits, equipment | `Campaigns/Zarek/人物档案/扎雷克_正式人物卡.md` | Record source version and checkpoint only |
| Module resource transactions and module-scoped balances | `09_RESOURCE_LEDGER.md` | Record last verified Entry ID / ledger checkpoint only |
| Campaign rulings | `Campaigns/Zarek/RULE_ADJUDICATIONS.md` | Q01–Q05 binding; do not copy rulings |
| System and ruleset | `Campaigns/Zarek/SYSTEM_BINDING.md` | triangle_agency / 中文 v22 |
| Player-known information | `05_PLAYER_NOTES.md` plus source event | Projection only; no GM-only truth |
| Fixed module facts | `01_GM_PREP.md` and source references in 07 | Reference IDs only |

Current known carry-over facts are not a substitute for Preflight reconciliation. Commendations 18, QA task-restored, Attentiveness 2/2, Ripple Gun 1/1 and the confirmed Bower Street Time award may be used only as provisional references until their authoritative snapshots are read at Preflight. Demerits, Harm and absolute available-Time balance remain UNKNOWN.

## 4. Runtime checkpoint contract

The first real Session checkpoint must instantiate the common `GM_Training/RUNTIME_STATE_TEMPLATE.md` contract and fill, where applicable:

```yaml
active_system:
  system_id: triangle_agency
  ruleset_version: "中文 v22"
  campaign_id: zarek
  module_id: blame_it_on_the_trains
checkpoint:
  revision: "R1"
  branch: "ACTIVE"
  last_event_id: "NONE"
  applied_event_ids: []
  unapplied_event_ids: []
  reconciliation_manifest_refs: []
resume:
  mode: "NEW START"
  can_advance: false
  scene_id: "NONE"
  entry_presented: false
  last_presented_event_id: "NONE"
  last_answered_event_id: "NONE"
  pending_player_action: null
persistence:
  batch_id: "NONE"
  status: "NOT_STARTED"
  repository_commit_read: "UNKNOWN"
  published_checkpoint_ref: "UNKNOWN"
  t0_mode: "UNKNOWN"
  t0_mode_authority_ref: "UNKNOWN"
```

Do not create actual event IDs, revisions, or published checkpoints before a real event occurs. The example above is a schema contract, not a claim that a Session has started.

## 5. Scene and world state (NOT STARTED)

| Field | Current value |
|---|---|
| Scene ID / status | NONE / NOT ENTERED |
| Game time | UNKNOWN |
| Location | UNKNOWN |
| Player character position | UNKNOWN |
| Present characters and positions | UNKNOWN |
| Spatial relationships / exits / barriers | UNKNOWN |
| Active threats / timers | NONE |
| Current commitments / pending tasks | NONE |

## 6. NPC knowledge and continuity

No NPC has interacted with the player in this module. Do not instantiate dynamic NPC knowledge, location or relationship changes from GM Prep alone.

| NPC ID | Position/status | Current goal/strategy | Knowledge actually acquired | Source event |
|---|---|---|---|---|
| NONE | — | — | — | — |

When play begins, update only on an actual event. Knowledge must retain its source and recipient; GM knowledge is never copied automatically to an NPC or Player Notes.

## 7. Spatial state ledger (GM-only; empty until play)

| Entity/Layer ID | State | Entry count | Change roll/event | Current occupants | Last event ID |
|---|---|---:|---|---|---|
| NONE | NOT ENTERED | 0 | NONE | NONE | NONE |

## 8. Narrative resume anchors

- Opening scene presented：NO
- Presented narrative node IDs：NONE
- Last GM response event：NONE
- Last player action event：NONE
- Pending intent：NONE
- Previously presented information requiring continuity：NONE

A CONTINUE restore must resume after the last verified presented node. It must never replay an already-presented opening as a new event.

## 9. Persistence and idempotency

- Session Log is the event history; this file is the current non-resource runtime snapshot; Resource Ledger is the only resource transaction ledger.
- Every state-changing event must have a stable Event ID and an explicit application status.
- Cross-file writes require a PREPARE manifest, owner-specific writes, independent readback, reconciliation, and a PUBLISHED checkpoint.
- A failed or partial write remains INCOMPLETE / DISPUTED. Never promote it to PUBLISHED or READY.
- Retrying the same Event ID must be idempotent; inspect existing application evidence before any repeated mutation.
- Do not store duplicate resource balances here. Store only the last verified ledger checkpoint reference.
- If any record conflicts, preserve both evidence sources, open a dispute, and block only dependent actions.

## 10. Update discipline

1. Do not write planned, hypothetical or test-only events as CANON.
2. Append actual events to Session Log; update this file only for current-state changes.
3. Resource changes go only to Resource Ledger; this file references the latest verified ledger checkpoint.
4. Player Notes contains only facts the player character actually learned, with source and confidence.
5. At Session close, record a checkpoint; at Module close, record CLOSED without erasing history.
6. Preflight and player authorization are separate gates. No file status grants permission to start.
