# Bower Street｜模组资源账本

> 权限：GM-only
> 结团性质：LEGACY_CLOSEOUT / LEGACY_UNMIGRATED；本文件保留历史资源流水和结团核验视图，但没有 v0.3 PREPARE Manifest / 最终发布批次证明，不得宣称具备 v0.3 原子发布或冷恢复保证。
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
| 普通 Chaos Pool | 0（开局：Branch Loose Ends = 1，对照 v22 印刷页 165 的 0 阈值行） | **0 / RESET AT MODULE CLOSE** | 模组内临时资源；SESSION 01/02 的增减流水保留审计，结团自动清零，不向下一模组结转。该 0 是本次任务初始化结果，不是固定 Campaign 默认值 |
| 天气事件 | 0（SESSION 01 Preflight 记录） | 0（截至 SESSION 01 最后确认） | SESSION 01 未记录变化；后续 Session 如有变化，按事件即时记账 |
| Ternion City 分部 Loose Ends 追踪 | 1（Campaign 基线） | **本模组增量 0；Campaign 基线仍为 1** | 用户明确确认 Bower Street 未增加 Loose Ends |
| 扎雷克 Harm / QA / Burnout | 以本模组开局时从正式人物卡复制的快照为基线；当前各字段如未完成核验则保持 UNKNOWN | SESSION 01 未记录确认变化 | 人物卡只提供 Session 边界开局快照；本模组内后续变化及余额以本账本为准 |
| Demerits / Commendations / Time | 以人物卡快照与规则为基线 | Demerits：**NONZERO / exact value pending**；Commendations：18；Time：本次结团 +1（绝对余额 UNKNOWN） | Demerits/Commendations/Time 是持续字段；即时记账，结团时核对 |
| 装备充能/可用次数 | 以人物卡与模组开局快照为准 | **模组结束恢复满额；Ripple Gun 1/1** | 当前无跨模组一次性资源；模组内使用流水留作审计 |

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

### CLOSED-BY-RESET｜SESSION 01 Ask the Agency / Chaos Pool

- 待核事项：原始 Ask the Agency 资源结算及临时 +5 的依据、实际应用状态。
- 已知边界：开局记录为 0；临时报出的 +5 未独立核验；SESSION 01 结束余额 UNKNOWN。
- 允许处理：取得足够的原始行动/规则证据后，追加核验结果或冲正条目。
- 禁止处理：直接把 0、+5 或两者相加当作 SESSION 01 结束余额；用开局值覆盖未知余额；在没有证据时推算后续余额。
- 状态：CLOSED FOR CROSS-MODULE ACCOUNTING。原始交易应用情况仍保留历史待审状态；模组结束自动清零后不再影响当前余额或幕间。

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
| BOWER-RES-012 | SESSION_02 / MODULE-CLOSE | 普通 Chaos Pool | 模组内余额不再追算 | RESET | 0 | VERIFIED_BY_RULE：用户确认每次模组结束自动清零；此前 +5 等历史流水保留审计 |
| BOWER-RES-013 | SESSION_02 / MODULE-CLOSE | QA（全部素质） | 任务中消耗后状态 | RESTORED_TO_FULL | 各项当前上限 | VERIFIED_BY_RULE：任务间 QA 完全恢复；缜密上限已由 MVP 提升至 2 |
| BOWER-RES-014 | SESSION_02 / MODULE-CLOSE | Ripple Gun | 模组内使用状态未完整恢复 | RESTORED_TO_FULL | 1/1 | VERIFIED_BY_RULE：用户确认当前无跨模组一次性资源，模组结束恢复满额 |
| BOWER-RES-015 | SESSION_02 / MODULE-CLOSE | Ternion City Branch Loose Ends | Campaign 基线 1 | +0 | 1 | USER_CONFIRMED：本模组增量 0；Campaign 基线不变 |

### 9.2 结团后已知状态

| 字段 | 当前核验结果 | 说明 |
|---|---|---|
| Module | CLOSED | 玩家确认核心异常收容完成；次要线索未解不阻碍结团 |
| Commendations | **18** | 结团前报告余额 7，已接受奖励合计 +11 |
| Competency | **累计 5 格** | MVP 免费职能格 +1；本次选择 Attentiveness |
| QA 上限总和 | **14** | 原总上限 13；本次 MVP 选择 Attentiveness +1 |
| 任务间恢复后的 QA | **专业 3/3、共情 3/3、低调 3/3、缜密 2/2、欺瞒 1/1、活力 1/1、主动 1/1、坚持 0/0、气质 0/0** | 按正式人物卡历史上限 + 本次 Attentiveness 成长；任务间 QA 完全恢复 |
| 普通 Chaos Pool | **0（模组结束自动清零）** | SESSION 01/02 历史增减保留审计，不向下一模组结转 |
| Harm / Burnout | **UNKNOWN / INCOMPLETE** | 完整 SESSION 02 检定记录未恢复；QA 当前值已按任务间完全恢复规则结算，历史使用次数仍未知 |
| Demerits | **NONZERO / exact value pending** | 用户确认结团后非零；精确值待历史事件流水核实，不得沿用旧快照 0 |
| 天气事件 | **UNKNOWN / INCOMPLETE** | SESSION 01 末次确认 0；SESSION 02 未核 |
| Ternion City 分部 Loose Ends 模组增量 | **0** | Campaign 基线 1 保持不变 |
| Ripple Gun | **1/1（恢复满额）** | 模组结束按规则恢复满额；当前无跨模组一次性资源 |
| 其他关键道具 | **按规则恢复满额** | 保留关键道具历史事件；没有已知跨模组一次性消耗项 |

### 9.3 未结事项

### CLOSED-BY-RESET｜SESSION 01 Ask the Agency / Chaos Pool
- 开局基线 0；原始结算遗漏；临时补报 +5 未独立核验。
- SESSION 02 的 BOWER-RES-002 另有一笔可恢复的 +5 变化量；不能用它反推 SESSION 01 的结余或合并成一个未经核实的余额。
- 状态：OPEN；只影响历史普通 Chaos Pool 的绝对余额核对，不阻止 Bower Street 叙事结团或进入幕间。

### AUDIT-ONLY｜SESSION 02 缺失的逐轮资源记录
- 原始完整玩家输入、GM 回复和全部检定序列未恢复；目前只有一项完整检定（BS2-ROLL-001）及结团奖励摘要。
- Harm、Burnout、其他 QA 的历史使用次数仍无法完整恢复；QA 已按任务间恢复规则回满。Demerits 确认非零但精确数值待核。Loose Ends 本模组增量明确为 0。装备按模组结束规则恢复满额。
- 状态：AUDIT-ONLY / SOURCE RECORD INCOMPLETE。若将来恢复原始对话，追加修订，不覆盖已确认交易；除 Demerits 精确数值外，本项不阻止幕间。

### 9.4 幕间使用边界
- 可用 Commendations 当前报告余额：18；影像女孩能力设计目标约 20 嘉奖上下，但不得在当前余额 18 下购买超过 18 的能力。
- 已确认的 MVP 免费职能格：Attentiveness QA 上限 +1；已确认的结团 Time 增量：+1。
- 本次 Time 尚未实际投入具体成长；影像女孩互动尚未演出；能力尚未设计、定价或购买。
- 不将旧人物卡的 Work/Life Balance 轨迹“总量30／已花费2／剩余28”当作当前可使用 Time 余额。


## 10. 模组结束恢复与跨模组资源分类（2026-11-27）

> 核心修订：资源流水用于保留历史事件和审计证据；模组结团时不要求把所有临时资源都推算成一个跨模组余额。先判断资源的作用域和恢复规则，再决定是否需要计算结余。

### 10.1 分类原则

每个资源在 Preflight / 运行时按规则明确分类，不得把所有资源一律当作跨模组账户：

1. **模组内临时资源**：仅在当前模组有效，模组结束时自动清零/重置。保留 Session 内每笔增减供审计；结团时记录重置事件与规则依据，不必追溯一个对下一模组没有意义的最终余额。
2. **自动恢复型角色资源**：规则规定在任务间或模组结束后恢复满额。Session 内仍记录实际消耗；恢复节点记录一次 RESTORED_TO_FULL，不要求为了结团再逐项重建每次消耗后的最终数字。若具体上限已知，记录恢复后的满额状态。
3. **跨模组持续资源**：规则没有规定自动清零/恢复，且会跨模组保留的资源（例如 Commendations、Demerits、Time 等，按各自规则分别处理）必须核实变化并同步人物卡。不得套用临时资源的重置逻辑。
4. **模组级累计指标**：如 Loose Ends，记录本模组增量及结团值；若没有增加，明确记录增量 0，并与 Campaign 基线区分。
5. **关键道具**：保留关键道具取得、失去和重要状态变化的历史。若道具的使用次数/充能按规则在模组结束后恢复满额，结团时记恢复事件；只有规则明确规定跨模组一次性或不可恢复的道具/资源才保留消耗后的状态。

### 10.2 结团执行顺序

- 回看 Session 内 Resource Ledger，保留实际消耗、奖励和纠错的逐笔历史；不删除流水。
- 对每项资源查明作用域：Session、任务间、模组、Campaign/角色长期。
- 按规则执行自动清零或恢复满额，并记录重置时间点、恢复后状态和规则/桌规依据。
- 对持续资源（如 Commendations、Demerits、Time）完成增减与最终余额核算；不能把 UNKNOWN 视作 0。
- 对模组累计指标（如 Loose Ends）记录本模组净增量；0 也是有效结算结果。
- 对装备/关键道具确认是否存在跨模组单次使用限制。没有此类限制、且规则规定模组结束恢复的，恢复满额；不得把 SESSION 末次消耗快照直接复制成下一模组开局状态。
- 最后才更新人物卡的 Session/Module 边界快照。账本保留流水，人物卡只保存跨模组持续状态与恢复后的关键道具快照。

### 10.3 本 Campaign 当前已明确的结算规则

- **普通 Chaos Pool**：Bower Street 属于模组内资源，模组结束自动清零。SESSION 01 的 BOWER-RES-001 不再阻塞结团余额；历史交易应用情况仍保留原始证据状态，模组关闭重置后不向下一模组结转。
- **QA**：任务间按规则完全恢复至各自上限；本次 Mission MVP 将 Attentiveness 上限提高至 2，因此模组结团后的可用值为 2/2。
- **Demerits**：跨模组持续记录，不自动视为 0；本次 Bower Street 结团后确认非零，但确切数值须以实际事件流水核对。不能从旧人物卡的 0 沿用，也不能凭空猜数。
- **Commendations**：跨模组持续；本次结团报告余额 18。
- **Time**：按完整模组结团规则增加可使用 Time +1，并同步记录“剩余可用 Time”字段 -1；绝对余额没有可靠基线时仍保留 UNKNOWN。
- **Loose Ends**：记录 Campaign 基线与本模组增量。本次 Bower Street 增量为 0；Campaign 基线 1，故不因本模组增加。
- **关键道具/装备充能**：当前没有跨模组只能使用一次的资源；按模组结束恢复规则，结团时恢复满额。Ripple Gun 恢复为满充 1 发。未来若出现明确跨模组一次性/不可恢复资源，再单独登记并保留消耗状态。

### 10.4 Bower Street 最终结算视图

| 项目 | 结团处理 | 结团后状态 |
|---|---|---|
| 普通 Chaos Pool | 模组结束自动清零 | 0；SESSION 01/02 逐笔流水保留审计 |
| QA | 任务间完全恢复；MVP 增加 Attentiveness 上限 +1 | 缜密 2/2；其他素质按人物卡上限恢复满额 |
| Commendations | 跨模组持续，按报告核算 | 18 |
| Demerits | 跨模组持续；确认非零 | NONZERO；确切数值待恢复/核账，不得写 0 |
| Time | 完整模组结团 +1；剩余可用 Time -1 | 增量已确认；绝对余额 UNKNOWN |
| Loose Ends | 记录本模组净增量 | +0；Campaign 基线 1 不变 |
| Ripple Gun | 模组结束恢复满额 | 1/1 |
| 其他当前关键道具 | 按模组结束恢复规则 | 恢复满额；无已知跨模组一次性消耗项 |
| Harm / Burnout | 依各自规则处理，不凭空套用通用恢复 | 若规则/基线未核实，保留相应状态；不阻止不涉及该资源的幕间叙事 |

### 10.5 审计与运行边界

- “恢复满额”不等于“本模组没有消耗”。必须保留原始消耗 Entry，另记恢复事件。
- 对自动重置的模组资源，不因 SESSION 01 的旧账缺口阻止结团；其历史记录仍可用于事后审查。
- 持续资源的精确数值仍须记账。尤其 Demerits：发生时即时登记，不能等到结团才回忆；发现遗漏时从 Session Log / 事件证据补记，不允许静默填 0。
- 以后 Preflight 必须加载资源分类表；Session 中每次变更即时记账；结团按分类执行，而不是对每一项资源一概进行“余额清零式对账”。


## 11. 2026-11-27｜幕间成长与 Requisition 购买（玩家确认）

> 本节追加在模组结团后的幕间交易。Bower Street 已 CLOSED；以下仅延续该模组账本，供结团后成长审计，不改变已关闭的模组内 Chaos Pool、Loose Ends 或 SESSION 历史。

### 11.1 已确认交易

| Entry ID | Session / Event ID | 资源字段 | 变化前 | 变化量 | 变化后 | 应用状态与证据 |
|---|---|---|---:|---:|---:|---|
| BOWER-RES-016 | INTERMISSION / GROWTH-COMPETENCY | 可使用 Time | +1（Bower Street 结团奖励） | -1（投入成长） | 该次奖励已使用 | VERIFIED_APPLIED：玩家明确选择将结团 +1 Time 投入 Competency；绝对 Time 余额仍 UNKNOWN |
| BOWER-RES-017 | INTERMISSION / GROWTH-COMPETENCY | Competency 职能轨迹 | 累计 5 格 | +1 格 | 累计 6 格 | VERIFIED_APPLIED：投入 Bower Street 结团 Time；第 6 格按已核实轨迹顺序为 D4 |
| BOWER-RES-018 | INTERMISSION / GROWTH-COMPETENCY | Duplicity QA 上限 | 1 | +1 | 2 | VERIFIED_APPLIED：玩家明确确认选择 Duplicity；任务间 QA 按规则恢复至新上限 |
| BOWER-RES-019 | INTERMISSION / GROWTH-COMPETENCY | Commendations | 18 | +3 | 21 | VERIFIED_APPLIED：Competency 成长奖励 |
| BOWER-RES-020 | INTERMISSION / VAULT-REQUEST-BLANK-INTERVAL | Commendations | 21 | -20 | 1 | VERIFIED_APPLIED：玩家确认购买「空白片段（Blank Interval）」Requisition，价格 20 |
| BOWER-RES-021 | INTERMISSION / VAULT-REQUEST-BLANK-INTERVAL | Vault Requisition | 未持有 | +1 | 持有：空白片段（Blank Interval） | VERIFIED_APPLIED：A3 Vault Request 权限；玩家确认购买；能力设计边界见人物卡幕间成长记录 |

### 11.2 幕间成长后状态

| 字段 | 当前核验结果 | 说明 |
|---|---|---|
| Competency | **累计 6 格** | 第 6 格 D4；Playwall 授权状态另见 Playwall Unlock Ledger |
| QA 上限总和 | **15** | Duplicity 由 1 提升至 2；Attentiveness 保持 2 |
| 任务间恢复后的 QA | **专业 3/3、共情 3/3、低调 3/3、缜密 2/2、欺瞒 2/2、活力 1/1、主动 1/1、坚持 0/0、气质 0/0** | 任务间 QA 完全恢复 |
| Commendations | **1** | 结团余额 18 + 成长奖励 3 - Requisition 价格 20 |
| Requisition | **空白片段（Blank Interval）已购买** | 20 Commendations；具体效果边界见正式人物卡 |
| Time | **本次结团 +1 已投入** | 绝对可使用 Time 余额仍 UNKNOWN；不从旧轨迹总量推算 |

### 11.3 尚待核验，不得补造
- 第 6 格 D4 已标记；按规则该代码的 Playwall 文档授权成立。文档正文读取/核对状态另记于 Playwall Unlock Ledger；本账本不复述隐藏资料。
- 两次历史 Time 支出导致的 Reality / Anomaly 轨迹末端划除坐标仍未从原始视觉轨迹表恢复。本次成长的对应划除位置也不在现有文字账本中；保持坐标 UNKNOWN，待恢复原始 Work/Life Balance 表后追加核验，不凭空指定。
- 本 Requisition 的恢复方式分支尚待玩家最终选择；购买本身已确认，不能把未选分支写成既定效果。


## 12. 2026-11-27｜Work/Life Balance Time 轨迹计数与划除坐标核验

> 本节覆盖 §11.3 中“跨轨迹划除坐标待恢复”的旧状态。具体格位的规则推导与证据等级见 [Zarek Playwall Unlock Ledger §8](../../PLAYWALL_UNLOCK_LEDGER.md)。

| Entry ID | 字段 | 变化前 | 变化 | 变化后 | 核验 |
|---|---|---:|---:|---:|---|
| BOWER-RES-022 | Work/Life Balance Time 轨迹已投入格数（不是可使用 Time 余额） | 2/30（剩余 28） | +1 次 Time 支出 | **3/30（剩余 27）** | VERIFIED：本次结团 +1 Time 已投入 Competency 第 6 格；与 Dead Quiet、Ice Cream Truck 两次历史 Time 支出合计三次 |

- 本次 Bower Street Time 支出对应 Reality 与 Anomaly 各划除第 28 格（下排左起第 3 格）。
- 前两次 Time 支出的划除位置分别为两轨第 30 格、第 29 格（下排左起第 1、2 格）。
- 以上坐标由官方 Work/Life Balance 轨迹路径与已记录成长事件顺序确定，状态为 RULE-DETERMINISTIC RECONSTRUCTION；不是声称已从扎雷克原始填表图片直接读取。
- “可使用 Time”的绝对余额仍为 UNKNOWN；本节 3/30 只记录 Work/Life Balance 轨迹格数，不用于推算可使用 Time 余额。
- D4 已读取；读取范围与收益记录见 Playwall Unlock Ledger §8。


### 12.1 官方轨迹版面证据

出版方官方可打印人物表第 3 页已目视核验：三条轨迹均为两排各 15 格，路径上排左→右、下排右→左。故本次 Reality / Anomaly 下排左起第 3 格（轨迹第 28 格）的物理位置有官方空白模板视觉依据；前两次对应下排左起第 1、2 格。扎雷克本人填写版未找到，个人标记状态仍以本账本与 Playwall Unlock Ledger 的事件记录重建。

来源：https://cdn.shopify.com/s/files/1/0581/0464/3719/files/Triangle_Agency_-_Character_Organization_Sheets_-_For_Print.pdf#page=3
