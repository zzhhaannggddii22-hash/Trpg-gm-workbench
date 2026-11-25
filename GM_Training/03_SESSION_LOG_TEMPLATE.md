# Session Log 模板

> 只记录实际发生的游戏内容。不要把预案、推测或尚未确认的解释写成事实。

## 基本信息

- Session 编号：
- 日期：
- TRPG 系统与版本：
- 模组/章节：
- 玩家角色：
- 实际游玩时长：
- 本次训练重点：

## 事实记录

### 场景与事件
按实际发生顺序记录场景、事件和结果。

### 玩家行动与选择
记录重要行动、非预设解法、关键决定及其后果。避免替玩家补写未表达的动机。

### NPC 与对手行动
记录实际行动、公开表达、关系变化、受伤/资源/位置等状态变化。

### 判定与规则
记录重要判定：行动、适用规则、结果、代价及是否存在争议。无需逐字记录所有无关紧要的骰子。

### 线索与信息
分别记录玩家已经获得的信息、尚未发现的信息，以及 GM 侧仍待核实的解释。

**重要证词/线索进入玩家记录前的最小核验（只在新增证词、细节升级、线索升级或总结时触发）：**
- 来源类型：NPC_STATEMENT / FILE_RECORD / DIRECT_OBSERVATION / PLAYER_CLAIM / GM_INFERENCE。
- 说话者/来源及其知识依据：
- 实际呈现事件 ID 与接收者：
- 原话或忠实摘要的定位：
- 本次内容实际支持的细节（时间、地点、人物、动作、顺序、数量、否定观察）：
- 原始精度与限制（例如“约九点”不得改写为“21:08”）：
- 如分次披露：各次呈现事件分别支持了哪些新增/修订字段；不得将后续细节回填为早先原话：
- 当前状态：SUPPORTED / UNVERIFIED / DISPUTED / REFUTED / UNKNOWN。

没有实际呈现事件的玩家转述，保留为 PLAYER_CLAIM / 待核实线索；不得写成 NPC 已经作出的证词。GM-only 时间线只能留在隐藏信息区，不得补入玩家已知记录。

### 资源与世界状态
记录角色资源、任务进度、NPC 状态、机构/阵营状态和其他会影响后续游戏的变化。

## 未解决事项

- 尚未处理的威胁：
- 未验证的线索或解释：
- 需要查证的规则/模组内容：
- 下一场可能承接的事项：

## GM 自我复盘（与事实记录分开）

- 本场做得好的处理：
- 发生的失误：
- 失误的具体原因：
- 对玩家能动性/世界一致性/规则公平/模组忠实度/节奏的影响：
- 哪些临场补充需要保留，哪些不应成为既定事实：
- 下一场 1–3 个可执行改进目标：

## 玩家反馈（如有）

记录玩家明确表达的评价与建议，不将沉默解释为认可，也不将疑问自动解释为不满。


## 关键状态变化（仅记录有持续影响的项目）

| 对象/字段 | 变化前 | 变化后 | 触发原因/行动 | 依据或来源 |
|---|---|---|---|---|
|  |  |  |  |  |

来源/性质可标记为：用户规则、模组原文、已发生的桌面事实、GM 即兴补充、推断、未知。推断不得写成已经确认的事实。

## Session 结束时的状态快照

只保存下一场或后续判断确实需要的信息；不需要把所有临时细节重新抄一遍。

- **玩家角色**：位置、关键状态/资源、伤势、实际持有装备及变化。
- **关键 NPC**：存活/状态、位置、目标或当前计划、与玩家的关系，以及其实际知道的信息（仅记录有变化或后续重要者）。
- **世界与事件**：仍活动的威胁、事件阶段、触发条件/时间条件、已发生的后果。
- **玩家已知信息**：只收录有实际呈现事件、明确接收者和可追溯内容范围的线索与事实；玩家转述但无呈现锚点的内容保留为 PLAYER_CLAIM / 待核实，不列为已获 NPC 证词。每项精确时间、地点、人物和否定细节不得超过原始呈现的精度。
- **GM 隐藏信息**：仍未揭示但会影响后续主持的事实，单独保存在 GM-only 档案，绝不混入玩家可见摘要。
- **未解决事项**：尚未处理的威胁、未验证的线索/解释、需要查证的规则/模组内容、可能承接的事项。


## 调查信息与来源增量（GM-only 索引，玩家侧只保留已知内容）

每场记录本次信息变化，不必复制完整线索库：
- 新获得的信息 ID 与简述；
- 已知信息的再次确认及新来源；
- 同一来源重复回答（玩家再次询问）；
- 新增细节、不同解释、矛盾或纠正；
- 来源实际知道什么、依据何在；
- 本次没有新增信息的调查结果（若对后续判断有意义）。

同一信息可以来自多个来源；同一 NPC/地点也可在不同问题或新事件下提供新信息。不要把“某来源曾经说过 A”记成“该来源已探索完毕”。重复信息简短记录，不重新完整叙述首次发现。

## 装备与资源持有人

对关键装备记录“规范物品名｜当前持有人｜数量/充能｜状态｜最后一次转移依据”。物品交接时同时更新双方记录。普通弹药与日常耗材按系统规则和实际稀缺程度选择精度，不为无关紧要的普通物品逐发记账。


## 多 Session 模组补充

- 同一模组可由多个 Session 构成；每个 Session 使用独立编号日志，按发生顺序保存，不覆盖历史。
- Session 日志记录本次新增事实与变化，不重复复制模组全部线索、完整人物卡或前次 Session 全文。
- Session 结束时必须给出可用于下一对话恢复的状态快照；模组最终奖励和完整复盘留到 Module 结团。
- 下一 Session 以最新 Runtime State 为当前状态权威，最近 Session Log 作为变更依据；更早日志仅在需要追溯时读取。


## 场景续接信息（供下一次 CONTINUE 恢复）

- 当前场景 ID：
- 场景状态：NOT ENTERED / ENTERED / ACTIVE / CLOSED / NON-CANON
- 本场模式：NEW START / CONTINUE
- 入口描述是否已向玩家呈现：
- 最后一个已确认的叙事节点 / Event ID：
- 最近一次有效 GM 回应：
- 玩家最近一次行动：
- 当前尚待回应的玩家意图/选择：
- Session 结束时游戏内时间与地点：
- 在场人物及重要位置关系：
- 是否存在尚未合并进 Runtime State 的事件增量：

下一场恢复时以最新 Runtime State 为当前值权威，以本日志及其后的 Session Log 追溯变化。CONTINUE 从最后一个已确认叙事节点接续；不得重新演出已经呈现的开场、首次接触或已结束场景。

## 2026-11-24 补充｜事件发布与认知来源字段

对重要事件追加记录时，按需增加以下字段；普通闲谈不强制逐条记录：
- event_id：稳定事件 ID；重试/修订沿用原 ID 并追加版本，不重复结算。
- base_revision：事件基于哪个已发布 Runtime checkpoint revision；如需兼容旧记录，旧字段 base_rev / checkpoint_rev 仅作为历史别名读取，不在新记录中混用。
- occurred_at：游戏内时间；未知则 UNKNOWN，不推算绝对日期。
- presentation_status：NOT_PRESENTED / PRESENTED / PARTIALLY_PRESENTED / UNKNOWN。
- response_status：NOT_AWAITING_PLAYER / AWAITING_PLAYER / RESPONDED。
- visibility：GM_ONLY / PLAYER_VISIBLE / RECIPIENT_SCOPED。
- affected_entities：实际发生变化的对象与字段。
- source_ref / claim_id：依据与关键命题 ID。
- commit_status：DRAFT / PREPARED / PUBLISHED / INCOMPLETE。
- batch_id：所属跨文件保存批次；同一事件在各目标文件中必须保持一致。
- target_revision：该批次预期生成的 Runtime revision。
- recipient_scope：玩家侧投影的目标接收者；无定向接收者时标 NOT_APPLICABLE。
- projection_targets：本事件应出现的文件/视图及预期记录身份。
- payload_version / payload_fingerprint：事件内容版本或稳定摘要；无法生成时明确标 NOT_AVAILABLE。

玩家已经看到/听到的内容即使尚未写入 Runtime，也必须在恢复时作为待合并事件保留。无法确认是否已呈现时，标记 DISPUTED 并核对，不得重演或擅自补完。


## 2026-11-24 补充｜争议事件、字段级权限与安全投影

### 争议/事故事件记录

发现跨文件重复、版本漂移、revision 漂移或权限冲突时，追加记录，不覆盖原事件：

| 字段 | 内容 |
|---|---|
| dispute_id | 稳定争议 ID |
| affected_batch_id / event_ids / targets | 受影响批次、事件和目标 |
| conflict_type | DUPLICATE_EVENT / PAYLOAD_VERSION_DRIFT / REVISION_DRIFT / RECIPIENT_MISMATCH / VISIBILITY_MISMATCH / OTHER |
| observed_records | 每条冲突记录的精确定位、身份字段、版本、权限字段 |
| raw_record_refs | 原始记录/写入前后证据的不可变引用 |
| prepare_evidence_ref | 原始 PREPARE 清单 |
| prior_fault_evidence_ref | 旧 Fault，仅作诊断证据 |
| detection_event_id | 本次发现事件 |
| persistence_readback | Runtime State 与 Session Log 的独立读回结果 |
| resolution | UNRESOLVED，或追加记录 resolved_by、basis_ref、resolution_event_id |

重复项必须分别保留，禁止只记“有重复”。版本变化必须保存旧、新 payload 版本与 fingerprint；revision 变化必须保存旧、新 base/target revision。争议解除只能追加，不删除原始异常。

### 玩家投影字段白名单

整行 visibility 不足以授权整行导出。一条记录包含不同权限字段时，必须逐字段筛选，或拆成彼此关联的公开记录与 GM-only 记录。

推荐结构：
- public_utterance：NPC 实际说出且玩家听见的原文/摘要；
- public_observation：玩家角色实际观察到的内容；
- player_known_claims：角色已获得的命题及来源；
- gm_knowledge：NPC 客观知识、隐藏真相、谎言意图、GM 裁定与幕后备注，只保留在 GM-only；
- private_notes：内部准备和审计信息，只保留在 GM-only。

Player Notes / 玩家导出只允许投影：
- 写入前沿用 Runtime §14.19 与线索账本 §9.2 的同一证据门槛：核对实际呈现事件、接收者、来源类型、原始内容范围与细节精度。
- PLAYER_CLAIM 可以作为“玩家提出/转述、尚待核实”的条目保存，但不得改标为 NPC_STATEMENT、FILE_RECORD 或 DIRECT_OBSERVATION；不得补入 GM-only 时间、地点或其他细节。
- 同一证词分次披露时，Player Notes 可以整合各次实际呈现的字段，但每个重要字段都必须回指支持它的呈现事件并保留原始精度；未披露字段继续未知。旧 Player Notes 只是既有投影，重复粘贴或引用不构成新证据，也不授权补齐未知字段。
- public_utterance
- public_observation
- player_known_claims 中已实际呈现且属于目标 recipient_scope 的条目
- 与上述内容直接相关、玩家有权知道的时间/地点/行动结果

默认拒绝投影：
- gm_knowledge
- private_notes
- GM adjudication / hidden truth / undisclosed clue / NPC deception intent
- 未实际呈现的 claim、其他玩家/角色的 recipient-scoped 内容

如果记录混合权限且无法可靠拆分，整条记录不得进入玩家投影；先拆分并逐字段核验。仅在独立 GM Audit 记录 projection_schema_version、recipient_scope、源 event_id、实际导出字段清单与过滤理由。玩家成品只含该接收者实际获知的白名单内容及安全必要引用。发布、附件与预览按 Runtime §14.12、§14.17。导出前后检查字段白名单，不能只检查行级 visibility。


### 2026-11-24 补充｜事件回应、呈现与 Runtime 合并标记（P1）

重要事件按实际情况增加以下关联字段：

~~~yaml
event_id: <stable-event-id>
responds_to_event_id: <player-action-or-prior-event-id, if applicable>
presentation_status: NOT_PRESENTED | PRESENTED | PARTIALLY_PRESENTED
response_status: NOT_AWAITING_PLAYER | AWAITING_PLAYER | RESPONDED
gm_response_ref: <exact player-visible response locator or UNKNOWN>
runtime_application:
  status: APPLIED | PARTIAL | NOT_APPLIED | UNKNOWN
  applied_to_revision: <exact revision or null>
  reconciliation_ref: <immutable reconciliation manifest ref or null>
~~~

- RESPONDED 表示玩家行动已获得有效 GM 回应；PRESENTED 表示该回应/信息确实已向目标接收者呈现。二者不可互相替代。
- gm_response_ref 应定位实际玩家可见内容，而不是仅引用 GM 内部摘要。
- 事件已呈现但未合并进 Runtime 时，保留在 unapplied_event_ids；应用状态未知时不得自行推断。
- 新记录按本结构填写；旧记录缺少字段时按 UNKNOWN 处理，不回填猜测。


## P1-0C 补充｜事件修订、应用和接收者片段契约（C2/C3/C5）

~~~yaml
event_id: "<stable-id>"
event_revision_id: "<immutable-revision-id>"
revision_of: "<prior-event-id-or-null>"
batch_id: "<batch-id-or-NOT_APPLICABLE>"
base_revision: "<exact-runtime-revision-or-UNKNOWN>"
target_revision: "<exact-runtime-revision-or-UNKNOWN>"
payload_version: "<version>"
payload_fingerprint: "<fingerprint-or-NOT_AVAILABLE>"
runtime_application:
  status: APPLIED | PARTIAL | NOT_APPLIED | UNKNOWN
  applied_to_revision: "<exact-revision-or-null>"
  reconciliation_ref: "<immutable-manifest-id-or-null>"
  applied_field_paths: []
presentation_segments:
  - segment_id: "<stable-segment-id>"
    content_ref: "<exact-message-span-or-content-ref>"
    recipient_scope: "<recipient-id-or-scope>"
    delivery_channel: "<channel>"
    delivery_state: PRESENTED | NOT_PRESENTED | UNKNOWN
    presented_at: "<timestamp-or-UNKNOWN>"
    evidence_ref: "<message-or-delivery-evidence>"
action_semantics: PLAYER_QUESTION_TO_GM | PLAYER_INTENT | PC_DECLARED_SPEECH | PC_ACTION_COMMITTED | GM_PROPOSED_ACTION | NPC_FUTURE_INTENT | NPC_ACTION_EXECUTED
incident_id: "<incident-id-or-NOT_APPLICABLE>"
dependency_refs: []
action_id: "<stable-action-id>"
decision_scope: "<exact-authorized-scope-or-NONE>"
player_decision: CONTINUE_SAFE_SCOPE | PAUSE_AUDIT | TERMINATE | UNKNOWN
decision_event_id: "<event-id-or-UNKNOWN>"
~~~

- Runtime 应用证明遵循 Runtime §14.14；事件 ID 相同不代表修订相同或全部字段已应用。
- PARTIALLY_PRESENTED 按接收者和内容片段记录；未知送达片段为 UNKNOWN。
- RESPONDED 不证明每个回应片段均已送达。gm_response_ref 定位实际可见回复，并与片段记录对应。
- 行动语义按 Runtime §14.11.1、§14.15。不要把桌外提问、玩家意图、GM 建议或 NPC 意向写成实际发言或执行；仅为实际发生且需要记录的领域事件生成相应记录。
- 旧记录缺字段按 UNKNOWN，不补造历史应用、呈现或授权证据。


## P1-0C 补充｜字段级应用和接收者片段
新事件应用证明必须按 Runtime §14.14 的不可变 reconciliation manifest 记录 event_revision_id、payload_version/fingerprint、batch_id、base/target revision、sequence 和精确 applied_field_paths。checkpoint 的 applied_event_ids 仅为索引，不是证明。部分应用标 PARTIAL。

对 PARTIALLY_PRESENTED 事件按 Runtime §14.16 记录 presentation_segments[]，每个片段绑定内容定位、recipient_scope、delivery_channel、delivery_state、presented_at 和 evidence_ref。RESPONDED 不代表所有片段已送达；未知送达状态保持 UNKNOWN。

新事件按上方契约标注适用的 action_semantics。对有后续影响的请求、接受、执行或结果，使用现有 action_id 和事件引用关联各阶段；仅记录已实际发生的阶段，不为桌外问句或未执行的行动虚构领域事件。

## Context Assembly / Trace 关联字段（P1）

Context Trace Envelope 以 [Runtime §14.20.8](./07_RUNTIME_CONTROL_PROTOCOL.md#14208-context-trace-与持久化) 为唯一字段规范。按该节在重要领域事件上附加 GM-only 元数据；没有领域事件且确需跨对话追溯时，使用下方 Operational Diagnostics 附录，不生成领域事件、不推进游戏时间或 CANON。Preflight 与绿色互动的放置和省略条件也以 Runtime 为准。

- Trace 不进入 Player Notes，不替代 Reconciliation Manifest、实际执行、交付或独立读回证据。
- 旧记录原样保留，缺失字段标 NOT_RECORDED / UNKNOWN，不补造历史。旧 `source_refs` 只作来源定位；没有实际读取证据时不得转换成 `retrieval_refs`。

## GM-only Operational Diagnostics Appendix（非领域事件）

仅当装配阻断、恢复或争议需要跨对话追溯，且没有可附着的领域事件时使用。此附录与事实型 Session/Event Log 分开；记录的是工作台运行诊断，不是游戏世界中发生的事件。

~~~yaml
operational_diagnostic:
  diagnostic_id: "<stable-diagnostic-id>"
  record_type: CONTEXT_ASSEMBLY_BLOCKED | CONTEXT_RECOVERY |
               CONTEXT_DIFF_DISPUTE
  context_id: "<context-id>"
  manifest_ref: "<immutable-manifest-record-ref>"
  trace_ref: "<trace-record-ref>"
  related_event_ids: []
  affected_dependency_refs: []
  status: OPEN | CONTAINED | RESOLVED
  created_at: "<wall-clock-timestamp-or-UNKNOWN>"
  does_not_create_domain_event: true
  does_not_advance_game_time: true
  does_not_create_canon: true
~~~

- 不分配领域 event_id，不进入 Runtime 的领域事件应用链，不改变游戏时间或 CANON。
- 只有确需跨对话追溯时才写入；普通绿色互动和一般无风险缺口不建立诊断记录。
- 诊断记录保持 GM-only，不进入 Player Notes 或玩家导出。
