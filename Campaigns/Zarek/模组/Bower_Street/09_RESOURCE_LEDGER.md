# Bower Street｜模组资源账本

> 权限：GM-only
> 适用范围：Zarek Campaign / Bower Street 模组全生命周期，覆盖所有 Session。
> 职责：记录本模组实际发生的资源变化、待核交易和余额对账；不替代系统规则、人物卡或 Runtime State。

## 1. 权威职责与文件分工

本文件是 **Bower Street 模组资源交易历史的唯一权威账本**。

- **Session Log**：记录资源变化发生于什么行动/事件、玩家看到了什么；引用本账本的 Entry ID，不另建第二套资源流水。
- **本账本**：记录每笔资源交易的字段、前值、变化量、依据、后值、应用状态及对账结果。
- **Runtime State**：只保留必要的场景连续性和关键物品快照；不重复维护资源余额或交易历史。
- **Campaign 正式人物卡**：Session 边界上的角色状态快照。Session 开始时读取；Session 结束后依据本账本完成对账并更新。它不是 Session 内实时资源来源，也不与账本并行计算。
- **模组级公共资源**（例如本模组 Chaos Pool、天气事件计数）：其模组内交易历史与当前对账状态以本账本为准。

资源规则与结算顺序仍以当前系统规则、已批准桌规及 GM Training Runtime Protocol 为准。本文件只记录实际交易，不复制规则全文。

### Session 边界同步协议

1. **Session 开始**：读取正式人物卡的最新 Session 结束快照。新模组以该快照建立本账本的开局余额；同一模组续场则沿用本账本上一场已核实的结余。两者不一致时标记 DISPUTED，先核对，不得任选一个继续计算。
2. **Session 进行中**：所有资源变化只写入本账本；以账本最新已确认余额作为后续资源裁定依据。正式人物卡不逐笔更新，场次副本也不另记资源流水。Runtime State 不复制资源数值。
3. **Session 结束**：核验本场所有 Entry、未结交易和规则结果；计算可确认的期末余额。再将角色资源与符合记录范围的关键物品状态一次性同步到正式人物卡，并标注 Session ID、账本最后 Entry ID 和同步日期。
4. **未知/争议**：不能用人物卡旧快照覆盖账本中较新的记录；也不能用未核实的账本值覆盖人物卡。冲突字段标记 UNKNOWN / DISPUTED，保留最后已确认值及待核原因。
5. **跨模组**：新模组账本从最近一次正式人物卡 Session 结束快照初始化；上一模组账本归档为历史流水，不跨模组继续追加。

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
| Ternion City 分部 Loose Ends 追踪 | 1（Campaign 基线） | 本模组当前增量 UNKNOWN / NOT SETTLED | 1 仅为已知 Campaign 基线；不得将其写成模组结团后的最终余额，也不得与普通 Chaos Pool 合并 |
| 扎雷克 Harm / QA / Burnout | 以本模组开局时从正式人物卡复制的快照为基线；当前各字段如未完成核验则保持 UNKNOWN | SESSION 01 未记录确认变化 | 人物卡只提供 Session 边界开局快照；本模组内后续变化及余额以本账本为准 |
| Demerits / Commendations / Time | 以本模组开局时从正式人物卡复制的快照为基线；未能确认的字段保持 UNKNOWN | SESSION 01 未记录确认变化 | 本模组内后续变化及余额以本账本为准；Time 仅在完整模组结团时按 Campaign 规则处理 |
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
- 不更新 Runtime State 中的资源余额；只同步必要的场景状态和关键物品持有人/状态。
- 对账完成后，将角色资源快照一次性写回正式人物卡；记录本次同步的 Session ID 与最后 Entry ID。

完整模组结团时额外执行：
- 对账所有 Session 的交易流水与模组级资源余额。
- 将角色资源的已确认期末余额同步至 Campaign 正式人物卡；正式人物卡是 Session 边界快照，不是第二份资源流水。
- 核对奖励、成长、购买、Time 和消耗是否被正确区分且未重复应用。
- 回读本账本、相关 Session Logs 和人物卡，确认期末余额与同步标记一致；Runtime State 不复制资源余额。

## 8. 道具记录范围

本账本只为具有资源属性的道具建立交易记录，例如可消耗次数、弹药、充能、耐久、限次使用或其他会影响机制裁定的状态。道具本体是否列入人物卡/关键物品记录，按以下标准判断：

- **必须记录**：关键任务道具；具有明确机制意义的嘉奖/奖励道具；重要资源道具（稀缺、限量、消耗后难以补充，或其持有/使用会改变规则裁定）。
- **不记录为长期库存**：普通易获取、可替代、无特殊机制意义的日常物品、临时杂物和常规消耗品。它们可在当前叙事中自然使用，不建立库存条目。
- **分工**：人物卡记录 Session 结束时仍持有的关键道具快照；Resource Ledger 记录其资源数值/充能/次数的增减；Session Log 记录取得、交付、使用或丢失事件；Runtime State 只在当前场景确有必要时记录持有人和位置。
- 道具的获得、消耗、转移、归还或损毁若不影响资源数值，也应在发生时作为事件写入 Session Log；只有达到上述重要性标准时才更新关键物品状态。


## 9. 2026-11-27｜SESSION 02 与模组结团结算（最新核验视图）

> 本节是当前最新结算覆盖层；若与 §3–§6 的 SESSION 01 历史快照描述冲突，以本节逐笔交易状态为准。未恢复的原始记录继续标记 UNKNOWN，不用推算填补。

### 9.1 已确认交易

| Entry ID | Session / Event ID | 资源字段 | 变化前 | 变化量 | 变化后 | 应用状态与证据 |
|---|---|---|---:|---:|---:|---|
| BOWER-RES-002 | SESSION_02 / BS2-ROLL-001 | 普通 Chaos Pool | UNKNOWN（SESSION 01 未结余额） | +5 | UNKNOWN | PARTIAL：+5 变化量可恢复；因 BOWER-RES-001 未结，不能计算余额 |
| BOWER-RES-003 | SESSION_02 / BS2-ROLL-001 | Attentiveness QA | 1/1 | -1 | 0/1 | VERIFIED_APPLIED：6d4 骰面与玩家使用 QA 调整首骰的记录 |
| BOWER-RES-004 | SESSION_02 / CLOSEOUT-MVP | Competency 职能轨迹 | 历史累计 4 格 | +1 格 | 累计 5 格 | VERIFIED_APPLIED：玩家确认 Mission MVP 免费职能格 |
| BOWER-RES-005 | SESSION_02 / CLOSEOUT-MVP | Attentiveness QA 上限 | 1 | +1 | 2 | VERIFIED_APPLIED：玩家明确选择 Negatives 对应的 Attentiveness |
| BOWER-RES-006 | SESSION_02 / CLOSEOUT-REWARD | Commendations | 7 | +3 | 10 | ACCEPTED_BY_DEFAULT：收容异常奖励，结团报告获玩家无异议默认通过 |
| BOWER-RES-007 | SESSION_02 / CLOSEOUT-REWARD | Commendations | 10 | +3 | 13 | ACCEPTED_BY_DEFAULT：报告 Complete 奖励 |
| BOWER-RES-008 | SESSION_02 / CLOSEOUT-REWARD | Commendations | 13 | +2 | 15 | ACCEPTED_BY_DEFAULT：R&D 两项授权行为奖励 |
| BOWER-RES-009 | SESSION_02 / CLOSEOUT-MVP | Commendations | 15 | +3 | 18 | ACCEPTED_BY_DEFAULT：Mission MVP 奖励 |
| BOWER-RES-010 | SESSION_02 / MODULE-CLOSE | 可使用 Time | UNKNOWN | +1 | UNKNOWN | VERIFIED_DELTA：玩家明确纠正为完整模组结团 +1；绝对余额无可靠基线 |
| BOWER-RES-011 | SESSION_02 / MODULE-CLOSE | 剩余可用 Time | UNKNOWN | -1 | UNKNOWN | VERIFIED_DELTA：按玩家确认的双字段反向记账规则；绝对余额无可靠基线 |

### 9.2 结团后已知状态

| 字段 | 当前核验结果 | 说明 |
|---|---|---|
| Module | CLOSED | 玩家确认核心异常收容完成；次要线索未解不阻碍结团 |
| Commendations | **18** | 结团前报告余额 7，已接受奖励合计 +11 |
| Competency | **累计 5 格** | MVP 免费职能格 +1；本次选择 Attentiveness |
| QA 上限总和 | **14** | 原总上限 13；本次 MVP 选择 Attentiveness +1 |
| 任务间恢复后的 QA | **专业 3/3、共情 3/3、低调 3/3、缜密 2/2、欺瞒 1/1、活力 1/1、主动 1/1、坚持 0/0、气质 0/0** | 按正式人物卡历史上限 + 本次 Attentiveness 成长；任务间 QA 完全恢复 |
| 普通 Chaos Pool | **UNKNOWN** | SESSION 01 BOWER-RES-001 未结；SESSION 02 已知 +5 变化量，不代表最终余额 |
| Harm / Burnout | **UNKNOWN / INCOMPLETE** | 完整 SESSION 02 检定记录未恢复；QA 当前值已按任务间完全恢复规则结算，历史使用次数仍未知 |
| Demerits | **UNKNOWN / INCOMPLETE** | 无完整逐轮记录，不写成 0 |
| 天气事件 | **UNKNOWN / INCOMPLETE** | SESSION 01 末次确认 0；SESSION 02 未核 |
| Ternion City 分部 Loose Ends 模组增量 | **UNKNOWN / NOT SETTLED** | Campaign 基线 1 不等于本模组结团余额 |
| Ripple Gun | **UNKNOWN / NOT RECONCILED** | SESSION 01 最后已知满充 1 发；SESSION 02 使用情况未恢复 |
| 其他关键道具 | **UNKNOWN / NOT RECONCILED** | 不把未恢复的道具转移或使用写成事实 |

### 9.3 未结事项

#### PENDING-001｜SESSION 01 Ask the Agency / Chaos Pool
- 开局基线 0；原始结算遗漏；临时补报 +5 未独立核验。
- SESSION 02 的 BOWER-RES-002 另有一笔可恢复的 +5 变化量；不能用它反推 SESSION 01 的结余或合并成一个未经核实的余额。
- 状态：OPEN；只影响历史普通 Chaos Pool 的绝对余额核对，不阻止 Bower Street 叙事结团或进入幕间。

#### PENDING-002｜SESSION 02 缺失的逐轮资源记录
- 原始完整玩家输入、GM 回复和全部检定序列未恢复；目前只有一项完整检定（BS2-ROLL-001）及结团奖励摘要。
- Harm、Burnout、其他 QA 使用、Demerits、天气事件、分部 Loose Ends 增量和装备消耗均不能确认为 0。
- 状态：OPEN / SOURCE RECORD INCOMPLETE。若将来恢复原始对话，采用追加修订，不覆盖本节已确认交易。

### 9.4 幕间使用边界
- 可用 Commendations 当前报告余额：18；影像女孩能力设计目标约 20 嘉奖上下，但不得在当前余额 18 下购买超过 18 的能力。
- 已确认的 MVP 免费职能格：Attentiveness QA 上限 +1；已确认的结团 Time 增量：+1。
- 本次 Time 尚未实际投入具体成长；影像女孩互动尚未演出；能力尚未设计、定价或购买。
- 不将旧人物卡的 Work/Life Balance 轨迹“总量30／已花费2／剩余28”当作当前可使用 Time 余额。
