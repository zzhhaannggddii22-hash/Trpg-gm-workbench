# Context Assembly & Trace｜设计决策与实施记录

- 状态：本分支实施候选；运行规则以合并后的 `GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md §14.20` 为准
- 基线：P1-1 Preflight read consolidation 已进入 main（基线提交 `c0ba307140160c6398fc8694d2e0a562ef9fb451`）
- 目标：在优化后的按需读取与健康续接快路径上，补足行动依赖装配、可核验上下文清单和运行可观测性
- 非目标：重建 Runtime、第二套记忆库、全量逐轮审计、Token 压缩或平台完整 Prompt 检查

## 1. 基线审查结论

当前架构已经明确：

- 静态权威事实、Runtime State、Session/Event Log、玩家可见记录各司其职；
- Preflight 有完整路径与健康续接快路径；
- 同次读取可按精确路径、版本/Blob、检查范围复用；
- 活动对话持续维护快照，只有关键规则不确定、质疑、状态冲突、高影响变化、新实体或错误回滚时才回查；
- Runtime 已有绿/黄/红/T0 路由、字段级争议、不可变 Reconciliation Manifest、接收者片段呈现与玩家信息权限门禁。

因此，本次不是另建“上下文系统”，而是在既有流程上增加一层**行动依赖解析与装配证明**。

## 2. 关键设计决策

### 2.1 Context ID 生命周期

- 一个 Context ID 对应一个可识别的执行单元：一次 Preflight，或一次玩家行动的 GM 处理过程。
- 复杂/复合行动使用一个父 Context ID，并为需要独立裁定的子行动分配 child_action_id；不把同一玩家意图拆成多个互不关联的上下文。
- 对同一行动的补充读取、澄清后仍属同一意图的重试、失败后恢复，沿用 Context ID；以递增的 attempt/revision 追加记录。
- 玩家明确改变目标、撤回原行动并提出新行动，或原行动已结束后提出新行动，才创建新 Context ID。
- Context ID 是追踪身份，不是游戏事件 ID；不得替代 event_id、action_id、batch_id 或 checkpoint revision。
- ID 格式由运行环境按当前 Session 范围生成稳定唯一值；不得依赖时间戳唯一性，也不得把 ID 本身当作证据。

### 2.2 Trace 持久化位置

不创建平行 Trace 数据库，也不把 Trace 塞进 Runtime State 主体。

- 对应真实游戏事件：将最小 Trace Envelope 作为该 Session Log 事件的 GM-only 元数据。
- 重要行动被阻断、恢复或出现装配争议，但没有产生领域事件：仅在需要跨对话追溯时，向现有 Session Log 追加 GM-only 的诊断事件；它不得伪装成世界事件或改变领域状态。
- Preflight 尚无可用 Session Log 时：Trace 随本次 Preflight/Handoff 记录；不为一次正常 Preflight 强制创建新审计文件。
- 绿色普通互动：不要求持久化 Trace。
- Runtime State 仅在某个装配问题已成为影响当前推进的开放争议/阻断状态时，按既有争议机制保存状态；不保存完整 Trace。
- Trace 不进入 Player Notes 或玩家导出。

### 2.3 Manifest 版本管理

- Manifest 使用显式 schema_version 和 manifest_revision。
- 已生成 Manifest 不可原地修改；修订产生新 revision，并通过 supersedes_ref 指向被替代版本。
- 同一 Context ID 的后续装配尝试可产生新 Manifest revision；旧版仍可追溯。
- 旧版本缺少字段时保留 UNKNOWN / NOT_RECORDED；不得从当前状态、摘要或模型印象回填历史。
- Manifest 是装配记录，不是权威事实、Runtime 快照或 Reconciliation Manifest。命名与字段必须避免与现有 Runtime Reconciliation Manifest 混淆。
- 运行中可使用轻量的临时装配清单；只有黄色/红色、恢复、冲突或需要跨轮追溯时，才将 Manifest 作为持久引用。

### 2.4 Context Diff 触发

默认采用**依赖失效触发**，而不是按消息数或每轮触发：

- 新对话/新 Session 的 Preflight：与可用的上次有效装配基线比较相关依赖；没有可靠旧基线时标记 NO_BASELINE，不推断“无变化”。
- 同一活动对话：仅在当前行动依赖可能被改变时，对受影响依赖做局部 Diff。
- 触发条件包括：系统/版本/Campaign/Module 绑定改变；相关 Runtime checkpoint 或事件改变；依赖来源版本/内容改变；相关 Claim 状态或证据根改变；NPC 知识/披露、玩家呈现/接收者权限改变；开放争议/T0 范围改变；行动依赖集合改变。
- 新行动本身不自动要求全量 Diff；只比较与该行动实际依赖相交的已有上下文。
- 不扫描整个仓库，不比较无关历史，不按 Token 或消息轮次设置固定审计频率。
- 如果用户原本想表达的“同一……”触发条件与以上不同，后续可以调整；当前实现先采用这一保守默认。

## 3. 结构与职责

### 3.1 Context Manifest

Manifest 记录一次装配的身份、范围、行动依赖、来源定位、读取状态、核验结果、允许/阻断范围和 Trace 引用。

它只保存引用和结果，不复制权威文件正文，不保存完整聊天，不存放模型思维链。

建议最小结构：

```yaml
context_manifest:
  context_id: "<stable-id>"
  schema_version: 1
  manifest_revision: 1
  supersedes_ref: null
  scope:
    session_id: "<session-id-or-UNKNOWN>"
    action_id: "<action-id>"
    parent_context_id: null
    attempt: 1
    mode: NEW_START | CONTINUE | ACTIVE_SESSION
    risk_level: GREEN | YELLOW | RED | T0
  binding:
    system_id: "<exact-id>"
    ruleset_version: "<exact-version>"
    campaign_id: "<campaign-id>"
    module_id: "<module-id>"
    status: VERIFIED | UNKNOWN | DISPUTED
  runtime_anchor:
    checkpoint_revision: "<revision-or-UNKNOWN>"
    branch: "<branch-or-UNKNOWN>"
    last_event_id: "<event-id-or-UNKNOWN>"
    status: VERIFIED | UNKNOWN | DISPUTED
  dependencies:
    - dependency_id: "<stable-id>"
      type: RULE | FACT | STATE | NPC_KNOWLEDGE |
            PLAYER_KNOWLEDGE | LOCATION | ITEM | RESOURCE |
            PRESENTATION | PERMISSION
      target_ref: "<exact-ref>"
      necessity: REQUIRED | CONDITIONAL | SUPPORTING
      status: RESOLVED | MISSING | UNKNOWN | DISPUTED |
              NOT_APPLICABLE
  sources:
    - source_ref: "<authoritative-ref>"
      locator: "<path/section/record-id>"
      version_ref: "<commit/blob/revision-or-UNKNOWN>"
      load_mode: REQUIRED | ACTION_DEPENDENT | SUPPORTING
      retrieval: FOUND | NOT_FOUND | NOT_ACCESSIBLE |
                 VERSION_MISMATCH | UNKNOWN
      read_scope: "<actual-scope>"
      read_status: FULL_REQUIRED_SCOPE | PARTIAL |
                   LOCATOR_ONLY | NOT_READ
      validation: VERIFIED | FAILED | UNKNOWN |
                  DISPUTED | NOT_APPLICABLE
      dependency_refs: []
  decision:
    status: READY | READY_WITH_LIMITS | BLOCKED
    allowed_scope: []
    blocked_scope: []
    unresolved_refs: []
    basis_refs: []
  trace_ref: "<trace-ref-or-NULL>"
```

字段按行动适用性填写；不适用字段标 NOT_APPLICABLE，缺失历史信息不得补造。

### 3.2 资料状态必须分层

检索状态、读取状态、核验状态是三个独立维度：

- 检索：FOUND / NOT_FOUND / NOT_ACCESSIBLE / VERSION_MISMATCH / UNKNOWN。
- 读取：FULL_REQUIRED_SCOPE / PARTIAL / LOCATOR_ONLY / NOT_READ。
- 核验：VERIFIED / FAILED / UNKNOWN / DISPUTED / NOT_APPLICABLE。

NOT_FOUND 不等于事实不存在；NOT_ACCESSIBLE 不等于空文件；LOCATOR_ONLY 不等于已读取正文；PARTIAL 不得伪装成完整核验。

### 3.3 依赖等级

- REQUIRED：当前行动的必要前提。未解决时阻断依赖它的子行动。
- CONDITIONAL：仅当某个已明确条件成立时才成为必要依赖；条件未触发时不强制读取。
- SUPPORTING：辅助解释或背景材料，不能替代 REQUIRED，也不能解决权威冲突。

SUPPORTING 不能因更容易检索或更短而取代权威来源。

## 4. Assembly 流程

1. Resolve Binding：沿 SYSTEM_CONTEXT_PROTOCOL 确认唯一系统、规则版本和 Campaign Binding。
2. Resolve Runtime：沿现有 Preflight 快慢路径读取有效检查点、分支、场景、未合并事件和开放争议。
3. Classify Action：识别桌外提问、玩家意图、角色发言、已提交行动、GM 建议和 NPC 行动；不把它们互相转换。
4. Resolve Dependencies：从行动目标识别必要规则、事实、状态、人物知识、呈现记录和权限。
5. Retrieve Authority：通过现有索引定位，读取必要原文/记录范围；摘要和检索候选不能代替权威。
6. Validate：核验身份、版本、权威、读取范围、状态一致性、证据来源、NPC 知识、玩家呈现和接收者权限。
7. Assemble：将权威事实、当前状态、历史事件、NPC 知识、玩家已知、未知/争议和输出权限分区。
8. Decide：READY / READY_WITH_LIMITS / BLOCKED，只限制受影响行动。
9. Respond & Trace：回应后记录重要状态变化、玩家可见呈现和最小 Trace Envelope。

这是一套按需装配流程，不是每轮额外 Preflight。绿色普通互动沿用现有零新增文件读取目标。

## 5. READY 判定

- READY：所有当前行动 REQUIRED 依赖均已解决，适用核验通过。
- READY_WITH_LIMITS：缺口已明确隔离，仍允许的行动有独立依据，不依赖争议内容，也不会把争议内容转化为新佐证。
- BLOCKED：至少一项 REQUIRED 依赖缺失、不可访问、版本不符、无法核验或存在相关争议；只阻断依赖该项的行动。

任何状态都不能把 UNKNOWN、DISPUTED 或 NOT_ACCESSIBLE 改写成事实。无关安全互动可继续。

## 6. Context Trace

Trace 只记录工程上可观察的事实，不记录思维链。

建议记录：
- context_id / action_id / attempt / manifest_revision；
- system/campaign/module/ruleset 和 Runtime checkpoint；
- 实际读取的来源定位、版本和读取范围；
- 执行的核验类别、结果和证据引用；
- READY 状态、允许范围和阻断范围；
- 对应事件 ID、状态变化字段、玩家呈现事件/接收者；
- persistence/readback 状态（仅当发生持久化）。

Trace 只能证明明确记录的事项。READ 不等于 VERIFIED；PRESENTED 需要交付证据；PERSISTENCE VERIFIED 需要独立读回。

当前 ChatGPT 环境不能读取平台完整隐藏 Prompt。Trace 只能声称记录了工作台可观察的显式资料定位、读取返回、核验和输出，不得宣称完整模型输入审计。

## 7. Trace 持久化规则

- 重要 Session Log 事件内嵌最小 Trace Envelope，引用 Manifest 和证据，不复制完整资料。
- 需要跨对话追溯的阻断/恢复/争议，在现有 Session Log 追加 GM-only 诊断事件；不得把诊断事件伪装成世界 CANON。
- Preflight 记录可承载启动阶段 Trace；没有现成 Session Log 时不为普通启动额外建库。
- 绿色互动不强制落盘。
- Runtime State 不保存完整 Trace；仅在现有状态协议要求时保存争议/阻断状态及相关引用。
- Player Notes 不保存 GM Trace，也不暴露 GM-only 来源、隐藏事实或内部路由。

## 8. Context Diff

Diff 比较的是语义依赖与来源变化，不是普通文本差异。

比较项：
- 系统/规则/Campaign/Module 绑定；
- checkpoint、活动分支、相关事件和未合并状态；
- 依赖来源的版本、内容指纹、读取范围；
- Claim 状态、证据根与来源谱系；
- NPC 知识、披露片段、玩家呈现和 recipient_scope；
- 开放争议、T0 冻结和授权范围；
- 当前行动依赖集合；
- 上次存在而本次无解释消失的事实、限制、否定信息、精度或权限条件。

结果分类：ADDED / REMOVED / REPLACED / CHANGED / NARROWED / EXPANDED / DISPUTED / UNKNOWN / UNCHANGED。

REMOVED 必须说明移除原因；不能将“新装配没有加载”误判为“事实已失效”。无可靠旧基线时输出 NO_BASELINE。

触发规则见 §2.4 与 Runtime §14.20；不按消息数逐轮执行，不做全仓扫描。

## 9. 与现有文件的职责边界

| 文件/体系 | 继续拥有的职责 | 本次集成方式 |
|---|---|---|
| SYSTEM_CONTEXT_PROTOCOL | 系统身份、规则版本、系统隔离 | Manifest 引用其核验结果，不复制规则 |
| 02_WORKFLOW_AND_PREFLIGHT | 新对话/新 Session 恢复和读取深度 | Preflight 建立启动 Context；复用现有快慢路径 |
| 07_RUNTIME_CONTROL_PROTOCOL | 风险路由、连续性、权限、争议、T0 | 新增 §14.20 作为装配/Trace 执行规范 |
| Runtime State | 当前值与开放运行争议 | 不保存完整 Manifest/Trace |
| Session Log | 事件历史 | 重要事件附 Trace Envelope；必要诊断追加 GM-only 记录 |
| Claim / Source Ledger | 命题、来源、证据根、呈现与知识传播 | Manifest 引用现有 ID，不另建知识账本 |
| Player Notes | 玩家实际获知信息 | 不写入 GM Trace |
| GM Skill | 现场综合执行入口 | 引用 §14.20，不复制完整流程 |

## 10. 验收计划

测试夹具见 [CONTEXT_ASSEMBLY_TRACE_REGRESSION_v1.md](../Acceptance_Test_Fixtures/CONTEXT_ASSEMBLY_TRACE_REGRESSION_v1.md)。

硬门槛：
- 系统身份/版本错误不得通过；
- REQUIRED 依赖遗漏不得 READY；
- LOCATOR_ONLY/PARTIAL 不得冒充完整核验；
- UNKNOWN/DISPUTED 不得升级为事实；
- NPC/玩家知识与接收者权限不得越界；
- Runtime/Log 应用链冲突不得静默裁定；
- 无关安全互动不得被整体冻结；
- Trace 不得声称不可观察的平台完整 Prompt；
- Context Diff 不得把未加载误判为事实删除。

性能门槛：
- 绿色普通互动不新增强制读取或持久化；
- 同一活动对话复用仍有效的静态来源和快照；
- Diff 只覆盖失效或当前行动相关依赖；
- 黄色/红色按现有风险路由扩大核验；
- 不以删减必要事实、否定信息、例外、精度和权限条件换取效率。

本文件和夹具通过静态检查不代表目标 Chat 行为通过；真实模型行为须另行实测。当前 P1-0C 暂缓状态与 Runtime §14.1.2 临时 T0 告警配置不由本次修改自动改变。
