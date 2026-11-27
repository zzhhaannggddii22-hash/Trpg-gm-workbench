# Bower Street｜模组资源账本

> 权限：GM-only
> 适用范围：Zarek Campaign / Bower Street 模组全生命周期，覆盖所有 Session。
> 职责：记录本模组实际发生的资源变化、待核交易和余额对账；不替代系统规则、人物卡或 Runtime State。

## 1. 权威职责与文件分工

本文件是 **Bower Street 模组资源交易历史的唯一权威账本**。

- **Session Log**：记录资源变化发生于什么行动/事件、玩家看到了什么；引用本账本的 Entry ID，不另建第二套资源流水。
- **本账本**：记录每笔资源交易的字段、前值、变化量、依据、后值、应用状态及对账结果。
- **Runtime State**：只保留开团和续接所需的当前资源快照，并注明对应账本版本/条目；不得独立推算或修订交易历史。
- **Campaign 正式人物卡**：仍是跨模组持续性人物资源当前余额的权威来源。本账本记录本模组造成的变化和同步结果，不取代人物卡。
- **模组级公共资源**（例如本模组 Chaos Pool、天气事件计数）：其模组内交易历史与当前对账状态以本账本为准。

资源规则与结算顺序仍以当前系统规则、已批准桌规及 GM Training Runtime Protocol 为准。本文件只记录实际交易，不复制规则全文。

## 2. 记账纪律

1. 每次资源变化必须在触发行动的同一轮完成记录、余额更新和玩家可见说明；不得延后到 Session 结束补记。
2. 一次行动改变多个资源字段时，每个字段独立一笔 Entry；可共享同一 Session Event ID。
3. 每笔记录至少包含：Entry ID、Session/Event ID、资源准确字段名、变化前值、变化量、原因与规则依据、变化后值、应用状态、证据来源。
4. 前值未核实：标记 UNKNOWN / PENDING。可以登记已确认的变化量或未经核实的报告值，但不得计算或伪装成已确认后值。
5. 余额待核只暂停依赖该余额的后续行动，不冻结无关互动。
6. 同一事件重试前先核对 Entry ID 和应用状态，防止重复入账。
7. 纠错采用追加修订/冲正记录，保留原始条目及其错误状态；不得静默删除或覆盖历史。
8. Session Log 记事件，账本记交易；Runtime State 是快照。三者通过 Event ID / Entry ID 互相引用，不各自维护独立流水。
9. 模组结团时，逐项核对账本与人物卡；人物资源的模组增量须按权威证据同步至正式人物卡后，才标记同步完成。

## 3. 当前资源快照与对账状态

> 本表是本账本的当前核验视图。未知值必须保持 UNKNOWN；不得用历史开局值、临时报数或人物卡中不同概念的字段替代。

| 资源/字段 | 模组开局/已知基线 | 当前已核实状态 | 对账说明 |
|---|---:|---|---|
| 普通 Chaos Pool | 0（SESSION 01 Preflight 记录） | **UNKNOWN / NEEDS RECONCILIATION** | SESSION 01 的 Ask the Agency 结算遗漏；曾临时补报 +5，但未独立核验，不能作为已应用交易或当前余额 |
| 天气事件 | 0（SESSION 01 Preflight 记录） | 0（截至 SESSION 01 最后确认） | SESSION 01 未记录变化；后续 Session 如有变化，按事件即时记账 |
| Ternion City 分部 Loose Ends 追踪 | 1（Campaign 基线） | 1（仅为已知基线；本模组增量未确认） | 属于 Campaign/分部追踪，不得将其与普通 Chaos Pool 合并 |
| 扎雷克 Harm / QA / Burnout | 以正式人物卡和 SESSION 01 实际记录为准 | SESSION 01 未记录确认变化 | “未记录确认变化”不等于推断出数值或证明从未变化 |
| Demerits / Commendations / Time | 以正式人物卡、Campaign 规则裁定及已确认事件为准 | SESSION 01 未记录确认变化 | 不从其他模组历史快照推算本模组余额；Time 仅在完整模组结团时按 Campaign 规则处理 |
| 装备充能/可用次数 | 以人物卡与 Runtime State 的已核验快照为准 | Ripple Gun 最后已知满充 1 发；SESSION 01 未记录使用 | 装备状态与角色资源字段分开记录 |

## 4. 交易流水

每笔已确认交易使用独立 Entry ID（格式：BOWER-RES-NNN）。同一行动若改变多个字段，为每个字段建立独立条目，并共用 Session Event ID。

| Entry ID | Session / Event ID | 资源字段 | 变化前 | 变化量 | 变化后 | 原因与依据 | 应用状态 / 证据 |
|---|---|---|---:|---:|---:|---|---|
| BOWER-RES-001 | SESSION_01 / BS-003 | 普通 Chaos Pool | 0（开局基线） | 曾临时报告 +5（未核实） | UNKNOWN | Ask the Agency 用于形成派对闪粉追踪效果；原始结算遗漏，临时补报未独立核验 | **PENDING / NOT VERIFIED**；不得计入已确认余额。来源：SESSION_01「规则与资源状态」、03_RUNTIME_STATE |

当前没有其他可从已核验 SESSION 01 记录中确认的资源交易。不得为了填满表格而创建零变化条目或补造数值。

## 5. 新交易记录模板

复制以下结构追加新条目；一笔资源字段一条记录：

### BOWER-RES-NNN｜简短交易名称

- Session：
- Session Event ID：
- 资源准确字段名：
- 变化前：
- 变化量：
- 变化后：
- 原因：
- 规则/桌规依据：
- 应用状态：VERIFIED_APPLIED / PENDING / PARTIAL / NOT_APPLIED / REVERSED
- 玩家可见说明：
- 证据来源（Session Log、规则条文、人物卡或用户明确确认）：
- Runtime State 同步：
- Campaign 人物卡同步（如适用）：

## 6. 待核与修订

### PENDING-001｜SESSION 01 Ask the Agency / Chaos Pool

- 待核事项：原始 Ask the Agency 资源结算及临时 +5 的依据、实际应用状态。
- 已知边界：开局记录为 0；临时报出的 +5 未独立核验；SESSION 01 结束余额 UNKNOWN。
- 允许处理：取得足够的原始行动/规则证据后，追加核验结果或冲正条目。
- 禁止处理：直接把 0、+5 或两者相加当作 SESSION 01 结束余额；用开局值覆盖未知余额；在没有证据时推算后续余额。
- 状态：OPEN。

## 7. Session 与模组结团检查

每次 Session 结束：
- 核对本场所有资源变化是否已有账本 Entry ID。
- 确认每笔交易的前值、变化量、依据、后值和应用状态。
- 对 UNKNOWN / PENDING 明确保留未知，不以猜测补账。
- 更新 Runtime State 的资源快照并引用账本条目。

完整模组结团时额外执行：
- 对账所有 Session 的交易流水与模组级资源余额。
- 将角色资源的已确认模组增量同步至 Campaign 正式人物卡。
- 核对奖励、成长、购买、Time 和消耗是否被正确区分且未重复应用。
- 回读本账本、Runtime State、相关 Session Logs 和人物卡，确认交易历史与当前快照一致。
