# Runtime State 模板｜当前运行状态快照

> 本文件记录当前有效状态，不是完整历史。完整事件经过写入编号 Session Log；长期固定事实仍以规则、模组、角色与战役权威档案为准。

## 状态头信息

- Campaign：
- Module：
- Session：
- Ruleset / Version：
- State Version：
- Last Updated：
- Last Confirmed Event ID：
- Resume Mode：NEW START / CONTINUE
- Current Scene ID：
- Current Scene Status：NOT ENTERED / ENTERED / ACTIVE / CLOSED / NON-CANON

## 场景续接锚点

- 入口描述是否已向玩家呈现：是 / 否
- 已呈现的入口/关键叙事节点 ID 或简述：
- 最近一次有效 GM 回应：
- 玩家最近一次行动：
- 当前尚待回应的玩家意图/选择：
- 当前场景中已完成、正在进行、尚未触发的事件：

> CONTINUE 必须从最后一个已确认的叙事节点继续。若入口已呈现，不得重新播放开场或首次接触。回顾/重播须明确标注为回顾，不作为新 CANON 事件。

## 当前时间与空间

- 游戏内日期/时间：
- 当前地点 / 场景：
- 玩家角色位置：
- 当前在场者及其位置：
- 重要空间关系、门/出口、阻隔或正在发生的变化：

## 玩家角色状态

- 伤害 / 状态效果：
- 系统资源：
- 当前装备与关键物品：
- 关键物品持有人、数量、充能与状态：
- 本场已经消耗、转交、归还或获得的项目：

## 玩家已知信息

| 信息 ID | 玩家已获得的事实/线索 | 来源 | 获得时间/事件 | 可信度或限制 |
|---|---|---|---|---|
| | | | | |

只记录角色实际知道且能够据此行动的信息。GM-only 真相不得放入本节。

## NPC 当前状态与知识

| NPC ID | 位置 / 状态 | 当前目标/策略 | 实际知道的信息及来源 | 与玩家的关系变化 |
|---|---|---|---|---|
| | | | | |

不要把 GM 掌握的信息自动赋予 NPC。没有变化且不会影响后续的日常细节不必重复登记。

## 世界事件与待办

| Event / Thread ID | 状态 | 触发条件/期限 | 当前进展 | 责任人/下一次相关节点 |
|---|---|---|---|---|
| | | | | |

区分 ACTIVE、RESOLVED、NOT TRIGGERED、CANCELLED 与 NON-CANON。已经解决的事件不得在续团时重新启动，除非新的因果条件成立。

## 连续性检查点

在场景切换、重要状态变化、Session 暂停/结束时，至少核对：

- [ ] 游戏时间与事件顺序一致。
- [ ] 人物位置与移动过程一致。
- [ ] 关键物品持有人、数量、消耗与转交一致。
- [ ] 玩家和 NPC 的知识均有实际来源。
- [ ] 资源、伤害、关系、承诺与事件阶段一致。
- [ ] 场景入口和关键内容是否已经向玩家呈现有明确标记。
- [ ] 当前待处理行动没有被误当成已完成。
- [ ] 回滚分支已标记 NON-CANON，且未残留在有效状态中。

## 自上次检查点以来的增量

只写自上次快照以来新发生、尚未反映在上方状态中的事实。完成核对后，将其合并进当前状态并清空本节。

| Event ID | 触发行动 | 变化前 → 变化后 | 依据/来源 | 是否已对玩家呈现 |
|---|---|---|---|---|
| | | | | |

## 来源与未知项

- 待核验的规则/模组事实：
- 尚未确认的推断：
- 明确 UNKNOWN：
- 相关权威文件与定位：

> 不要为了填满模板而编造字段。没有信息就留空或标记 UNKNOWN。普通绿色互动无需为每轮单独建立完整快照；状态变化时更新受影响字段即可。

## 2026-11-24 补充｜系统锁、检查点与保存状态

在现有状态头中按需补充以下字段；旧存档缺字段时必须标记为历史/未迁移，不得凭空补齐：

~~~yaml
active_system:
  system_id: "<exact-system-id>"
  ruleset_version: "<exact-version>"
  campaign_id: "<campaign-id>"
  module_id: "<module-id>"
checkpoint:
  revision: "<monotonic-revision>"
  branch: "ACTIVE | CLOSED | NON-CANON | DISPUTED"
  last_event_id: "<event-id>"
  unapplied_event_ids: []
  applied_event_ids: []
  reconciliation_manifest_refs: [] # immutable manifest refs; authoritative application proof
resume:
  mode: "NEW START | CONTINUE"
  can_advance: true
  scene_id: "<scene-id>"
  entry_presented: true
  last_presented_event_id: "<event-id>"
  last_answered_event_id: "<event-id>"
  pending_player_action: null
persistence:
  batch_id: "<batch-id>"
  status: "PUBLISHED | PREPARED | INCOMPLETE | PENDING_EXTERNAL_WRITE"
incident:
  status: "CLEAR | T0 | DISPUTED | CONTAINED"
  affected_scope: []
  player_decision: null
~~~

### 跨文件批次清单（重要事件保存时填写）

```yaml
persistence:
  batch_id: "<stable-batch-id>"
  status: "PREPARED | INCOMPLETE | PENDING_EXTERNAL_WRITE | DISPUTED | PUBLISHED"
  base_revision: "<published-revision>"
  target_revision: "<expected-revision>"
  required_targets:
    - target: "SESSION_LOG"
      event_id: "<event-id>"
      status: "PENDING | APPLIED | VERIFIED | DISPUTED"
    - target: "RUNTIME_STATE"
      event_id: "<event-id>"
      status: "PENDING | APPLIED | VERIFIED | DISPUTED"
    - target: "PLAYER_NOTES"
      event_id: "<event-id>"
      status: "PENDING | APPLIED | VERIFIED | DISPUTED"
  reconciliation:
    checked_event_ids: []
    unresolved_targets: []
    mismatch_reasons: []
```

- 上述清单是模板示例；按实际需要列出目标，不适用的目标不得强行创建。
- 每个目标记录必须能反向定位同一 event_id 与 batch_id；Player Notes 还必须匹配 visibility 与 recipient_scope。
- 不得仅凭写入成功、文件条数、旧故障记录或缓存结果将目标标为 VERIFIED。

### 保存与恢复规则
- Runtime State 是当前值权威；Session Log 是事件历史；正式人物卡只在任务/Session 规定结点核验回写；Player Notes 是角色知识投影。
- 已呈现但尚未合并的事件必须列入 unapplied_event_ids。已合并事件必须能在 checkpoint.reconciliation_manifest_refs 指向的不可变 manifest 中逐项定位；applied_event_ids 仅为索引；仅凭 revision 较新、PUBLISHED 或 unapplied_event_ids 为空，不得推断某个事件已合并。恢复时先核对未合并及存在冲突的事件，不得用旧快照覆盖。
- 多文件写入时先准备批次，按字段所有者应用，再读回核对，最后标记 PUBLISHED。任何环节失败均保留 INCOMPLETE，不声称保存完成。
- 对同一 event_id 的重试必须幂等：先查是否已应用；不得重复扣资源、发奖励、转移物品或推进事件。
- 旧记录缺少系统锁、版本或检查点时，标记 LEGACY_UNMIGRATED，并走完整 Preflight；不能用摘要推断。
- 新对话必须验证系统、Campaign、Module、规则版本、活动分支、场景入口状态、最后已呈现/已回应事件、待回应行动、物品资源、知识权限和事故授权。


### 开放争议与持久化冲突（无争议时保留空数组）

~~~yaml
persistence:
  disputes:
    - dispute_id: "<stable-dispute-id>"
      batch_id: "<affected-batch-id>"
      affected_event_ids: []
      affected_targets: []
      status: "OPEN | CONTAINED | RESOLVED"
      conflict_type: []
      observed_records:
        - target: "<target>"
          record_locator: "<exact locator>"
          event_id: "<observed id>"
          batch_id: "<observed batch>"
          revision: "<observed revision>"
          payload_version: "<observed version>"
          payload_fingerprint: "<observed fingerprint or NOT_AVAILABLE>"
          visibility: "<observed value>"
          recipient_scope: "<observed value>"
          raw_record_ref: "<immutable evidence ref>"
      prepare_evidence_ref: "<PREPARE ref>"
      prior_fault_evidence_ref: "<diagnostic-only ref>"
      detected_at: "<timestamp or UNKNOWN>"
      resolution:
        status: "UNRESOLVED | RESOLVED"
        resolved_by: null
        basis_ref: null
        resolution_event_id: null
~~~

- 争议对象是权威状态的一部分，不是临时审计备注。每次恢复先读取开放争议，再读取其原始证据。
- 发现冲突后，必须将争议对象写入 Runtime State，并在 Session Log 追加同 dispute_id 的事件；分别读回核验。任何一个目标未成功，整体仍 INCOMPLETE。
- 不删除冲突记录。解除争议时追加 resolution 事件并保留原始对象及证据链。
- DISPUTED 状态阻断受影响事件的玩家投影与依赖该事件的推进；不相关且能证明隔离的内容可继续。


### Runtime / Session Log 事件合并证明（P1）

每个会改变 Runtime 字段的 Session Log 事件，必须在事件记录中增加：

~~~yaml
runtime_application:
  status: APPLIED | NOT_APPLIED | UNKNOWN
  applied_to_revision: <exact runtime revision or null>
  reconciliation_ref: <same immutable reconciliation manifest referenced by Runtime checkpoint>
~~~

规则：
- APPLIED 必须同时满足：Session Log 有上述完整标记；Runtime checkpoint 的 applied_event_ids 或 reconciliation manifest 包含该 event_id；revision 与事件顺序相容。
- 任一侧缺失、引用不可读取、event_id 不匹配或 revision 冲突，均按 UNKNOWN 处理。
- NOT_APPLIED 事件必须留在 unapplied_event_ids；UNKNOWN 不得自动归入已应用或未应用。
- 对旧存档不得补造历史应用标记。无法回溯证明时保留 UNKNOWN，并按运行协议 §14.10 处理字段级争议。


## P1-0C 补充｜规范 Runtime 状态契约（C2/C3）

~~~yaml
checkpoint:
  revision: "<immutable-revision-id>"
  reconciliation_manifest_refs: [] # 完整应用证明；权威
  applied_event_ids: []             # 可选索引，不构成应用证明
  unapplied_event_ids: []
  manifest_chain_head: "<manifest-id-or-UNKNOWN>"

state_disputes:
  - dispute_id: "<stable-id>"
    object_id: "<object>"
    field_path: "<canonical.path>"
    runtime_value_ref: "<immutable-ref>"
    log_value_ref: "<immutable-ref>"
    source_refs: []
    related_event_ids: []
    dependency_refs: []
    status: OPEN | CONTAINED | RESOLVED
    detected_at: "<timestamp-or-UNKNOWN>"
    resolution_ref: null

t0_incidents:
  - incident_id: "<stable-id>"
    status: OPEN | CONTAINED | RESOLVED | TERMINATED
    affected_claim_ids: []
    affected_field_paths: []
    affected_threads: []
    dependency_edges: []
    allowed_threads: []
    blocked_threads: []
    last_valid_authorization_event_id: "<event-id-or-UNKNOWN>"
    authorization_scope: "<exact-scope-or-NONE>"
    player_choice: CONTINUE_SAFE_SCOPE | PAUSE_AUDIT | TERMINATE | UNKNOWN
    resolution_ref: null
~~~

- reconciliation_manifest_refs 指向不可变 manifest；applied_event_ids 仅为索引。索引存在但 manifest 缺失/不可读时，应用状态 UNKNOWN。
- Manifest 必须绑定 event_id、event_revision_id、payload_version/fingerprint、batch_id、base/target revision、sequence、精确 applied_fields（object_id、field_path、before/after value ref）和 application_status。
- Manifest 不可原地修改；修订产生新 manifest_id 并通过 supersedes_ref 建立谱系。部分字段应用标 PARTIAL。
- 当前值必须与从 checkpoint 基线起按 sequence 应用的有效 manifest 链相符。断链、跳 revision、字段缺项或值不符均建立 state_disputes。
- state_disputes 是领域字段争议；persistence.disputes 仅记录跨文件持久化冲突，不可混用。
- T0 授权只在相同 incident_id、相同范围、依赖未变化且未撤销时延续。旧存档缺字段保持 UNKNOWN，不得从聊天摘要或模型印象回填。
