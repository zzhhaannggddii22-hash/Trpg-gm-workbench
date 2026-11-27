# NQB-01 v0.3｜Runtime State

> TEST_ONLY / NON_CANON｜初始检查点；不是已发生的 Session 记录。

## 状态头信息
- Campaign: `nqb01_v03_test`
- Module: `nqb01_v03`
- Session: `S01`
- Ruleset / Version: `triangle_agency / 中文 v22`
- State Version: `0`
- Last Updated: `2026-11-27`
- Last Confirmed Event ID: `NONE`
- Resume Mode: `NEW START`
- Current Scene ID: `INN-01`
- Current Scene Status: `NOT ENTERED`

```yaml
active_system:
  system_id: triangle_agency
  ruleset_version: "中文 v22"
  campaign_id: nqb01_v03_test
  module_id: nqb01_v03
checkpoint:
  revision: "0"
  branch: "ACTIVE"
  last_event_id: null
  unapplied_event_ids: []
  applied_event_ids: []
  reconciliation_manifest_refs: []
resume:
  mode: "NEW START"
  can_advance: false
  scene_id: "INN-01"
  entry_presented: false
  last_presented_event_id: null
  last_answered_event_id: null
  pending_player_action: null
persistence:
  batch_id: null
  status: "NOT_STARTED"
  repository_commit_read: "UNKNOWN_AT_INITIAL_CHECKPOINT_CREATION"
  published_checkpoint_ref: "Campaigns/NQB01_Runtime_Test/Modules/NQB01_V03/03_RUNTIME_STATE.md@revision-0"
  t0_mode: "UNKNOWN"
  t0_mode_authority_ref: "UNKNOWN"
```

## 场景状态
- 场景尚未向玩家呈现。
- 游戏内时间、天气、NPC 位置和物件状态以 GM Packet 的初始状态为准；尚未发生任何测试事件。
- 玩家位置：场景入口外；尚未进入。
- 当前待回应玩家行动：NONE。

## 玩家已知信息
尚无。本节只在信息实际呈现并有事件锚点后更新。

## NPC 当前状态与知识
尚无已运行状态。开场前从 GM Packet 装配初始状态；NPC 知识不得超出各自来源边界。

## 世界事件与待办
尚无已触发事件。场景中预置的日常事务不等于已发生的玩家事件。

## 来源与未知项
- 场景来源：`GM_Training/Testing/Baselines/NQB01_V03_GM_PACKET.md`
- 规则权威：`Systems/Triangle_Agency/README.md` 与中文 v22 原文。
- 角色机械档案：已建立于 Campaign 根目录 `TEST_CHARACTER_SHEET.md`；目标 Preflight 尚未独立核验，依赖角色数据的裁定须在 Preflight 确认后才可进行。
- 测试 Session 尚未获准启动。
