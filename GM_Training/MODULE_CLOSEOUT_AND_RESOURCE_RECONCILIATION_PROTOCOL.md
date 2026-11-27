# Module Closeout & Resource Reconciliation Protocol v0.3
## Recoverable Closeout Contract

> 状态：设计基线（v0.3）
> 适用层级：通用工作台流程；系统专属结算规则由适配器提供。
> 设计目标：在不新建资源引擎、快照引擎或第二套事务机制的前提下，使 Module 结团具备可发现、可恢复、可核验、可幂等发布的闭环。
> 架构固定为：Campaign → Module → Session。允许一对一，不引入 Play Unit。

---

## 0. 规范效力与不变量

本协议定义 Module 结团的事务、证据、发布和交接契约；不定义任何具体 TRPG 的奖励、成长、资源恢复或剧情结束条件。

必须维持以下不变量：

1. **唯一字段权威。** 每个可变字段在任一生命周期阶段只有一个权威写入所有者；其他文件是历史证据、候选、投影或索引。
2. **事实先于结算。** 结算只消费已冻结的事件、裁定和玩家选择；不能把推断或未发生计划写成事实。
3. **规则依赖显式化。** 通用层不硬编码奖励、成长、恢复的先后顺序；适配器声明依赖图。
4. **一次操作，一个身份。** 同一 Module 的同一次合法结团重试沿用同一 Operation Identity；不得以新聊天、新模型或重试生成新结团。
5. **先准备，后应用，核对后发布。** 复用 Runtime §14.4-A 的 PREPARE → APPLY → RECONCILE → PUBLISH；不另建事务引擎。
6. **CLOSED 与最终发布同界。** Module CLOSED 只在包含结团结果和 CLOSED 状态的最终发布指针成功提交后生效。
7. **未知不是零，无法证明不是未执行。** UNKNOWN、DISPUTED、UNVERIFIABLE 必须保留；不得猜测余额、伪造 NOT_APPLIED 或静默跳过。
8. **局部阻塞。** 未知字段只阻止依赖该字段的结算、购买或行动，不冻结有独立依据的互动。
9. **复盘独立。** Postmortem 是可选、只读、非阻塞工作，不属于结团事务，不改变资源、奖励、成长、人物卡或生命周期。
10. **玩家/GM 信息隔离。** GM 核验包与玩家摘要分别生成；玩家摘要沿 Runtime §14.19 投影，不泄露内部身份、未呈现事实或过滤原因。

## 1. 分层与职责

| 层 | 职责 | 禁止事项 |
|---|---|---|
| Generic（GM_Training） | 事务阶段、身份、证据、幂等、恢复、发布、交接契约 | 写入系统专属资源名、奖励数值、恢复机制 |
| System Rules（Systems/<System>） | 规则事实、奖励资格、资源作用域、恢复规则、成长、依赖图、申诉/封账要求 | 改写通用事务语义 |
| Campaign / Module | 选择适配器开放的配置项；记录批准桌规、适用范围与有效期 | 自行发明系统规则或覆盖系统硬性规则 |
| Runtime Instance（Campaigns） | 实际事件、资源 Entry、玩家选择、应用证明、当前状态 | 把聊天意图、旧摘要或 GM 推断当成已发生事实 |

Campaign 桌规记录必须包含：规则依据、偏离内容、批准者、适用 Campaign/Module、Effective Period、触发条件、继承规则。未明确的桌规不参与结算。

## 2. 字段权威与阶段交接

字段权威按字段而非文件整体确定。通用字段分类如下；实际字段清单必须在系统适配器和 Campaign 运行记录中细化。

| 字段类别 | 活动期权威 | PREPARE / APPLY 阶段 | 最终发布后 |
|---|---|---|---|
| Session 事实事件 | 对应 Session Log（追加历史） | 原始事件不改写；纠错追加有谱系的修订事件 | Session Log 保留历史 |
| Module 当前场景状态 | Module Runtime State | 旧已发布值仍是读者当前值；候选写入按批次标识 | Module Runtime State 新修订生效；随后 CLOSED |
| Module 资源流水 | Module Resource Ledger（若启用） | 已发布流水 + PREPARE 中冻结的增量/应用证明 | Ledger 保留全流水；不得删除消耗或恢复事件 |
| 角色跨模组持续资源 | Campaign 正式人物卡/指定 Campaign State | 旧值继续有效；待应用增量与候选值仅属于原批次 | 最终批次发布后新版本生效 |
| 自动恢复型资源 | 适配器指定的当前角色状态与 Module Ledger 历史 | 按规则生成恢复事件和候选快照 | 恢复后的角色状态成为跨模组值 |
| 模组临时资源 | Module Ledger | 保留历史；生成规则要求的 reset/expiry 事件 | 终止/清零，不向下个 Module 继承 |
| Campaign 累计指标 | Campaign State | 旧值 + 冻结增量，独立核对 | 新 Campaign 修订生效 |
| 关键道具持有人/状态 | 其专属物品记录或规定的 Runtime 字段 | 保留事件与待应用候选 | 以指定权威记录的新修订生效 |
| Module 生命周期 | Module 唯一生命周期字段（指定在 Runtime/Module Record） | 仍为 CLOSEOUT_PENDING；CLOSED 只能在最终批次中成为候选 | 最终发布指针确认后 CLOSED |
| README、Campaign 索引、Handoff | 非权威投影 | 仅准备引用/摘要，不作状态裁判 | 与已发布检查点一致；不单独授权推进 |

Session Log 是事件历史，不是当前余额权威。Runtime State 是当前场景状态，不复制资源流水或余额。人物卡是 Session/Module 边界快照，不承担逐笔交易账本。README 和索引不得维护第二套可变生命周期事实。

如果当前仓库某字段已有更具体的唯一所有者，迁移时保留该所有者，不因本表而机械搬迁数据。

## 3. 结团入口与生命周期

Module 生命周期最少区分 PREP / READY / ACTIVE / PAUSED / CLOSEOUT_PENDING / CLOSED / ARCHIVED。

- Session CLOSED 不等于 Module CLOSED。
- Module CLOSED 不等于 Campaign CLOSED。
- ARCHIVED 是归档/入口退役状态，不是结算成功证明。
- 结团触发来自系统/模组定义的结束条件，或用户明确决定结束当前 Module。次要线索未解不自动阻塞；奖励也不得因次要线索未解而被无依据延迟。
- 当唯一有效 PREPARE Manifest 已持久化并独立读回后，Module 进入逻辑上的 CLOSEOUT_PENDING：该状态由活动 Operation/Manifest 派生，旧已发布检查点仍保持原值，不另做一次未发布的生命周期写入。此后冻结会影响结团的普通推进和相关资源/奖励写入；允许只读查询、独立复盘准备，以及不依赖冻结字段的安全互动。若用户撤销结团意图，必须以独立、可审计的取消操作关闭该 Operation；不得直接删除 Manifest 或把状态静默改回 ACTIVE。
- 结团入口只确认合法触发、授权、身份和范围，不提前计算结果、不执行恢复、不发奖励。

## 4. 稳定身份与并发首次启动

每次结团必须建立独立的 Closeout Operation Identity：

`closeout_operation_id` 在同一 Campaign + Module + Run Identity + Module Revision 的一次合法结团中保持稳定。

它不同于：
- `settlement_event_id`：某一项实际结算事件；
- `reward_eligibility_id`：一项奖励资格的稳定身份；
- `field_operation_id`：对一个权威字段的应用操作；
- `save_batch_id`：一次持久化批次；
- `revision_id`：同一操作计划的合法修订版本。

身份至少绑定 Campaign ID、Module ID、Run/Branch Identity、Closeout Trigger Evidence、初始 Module Revision。不得只用文件名、日期或聊天 ID 充当身份。

**首次并发启动：**
1. 首次启动者先读取当前 Runtime State、既有 GM-only Operational Diagnostics 与最新已发布 checkpoint，确认该 Module/Run/Scope 没有活动结团操作。
2. 以预期 Git branch HEAD 为基准，在 Runtime §14.4-A 既有 GM 批次记录 / Operational Diagnostics 中条件创建本次 PREPARE 记录，并生成稳定 closeout_operation_id 与唯一 batch_id。
3. 将不可变 PREPARE Manifest 独立保存并读回；在 Runtime State 的 persistence.prepare_manifest_ref 与批次记录中登记其引用。
4. 并发启动者若基于旧 HEAD 提交失败，必须重新读取 Runtime State、Operational Diagnostics 与 Manifest，复用已创建的 Operation ID；不得另建平行操作。
5. 宿主不支持 branch HEAD 条件更新/等价原子提交，或无法证明唯一性与独立读回时，标记 IDENTITY_UNVERIFIABLE，停止自动结算，交付人工待处理项。
6. 已存在多个活动记录、分支身份不一致或范围冲突时，停止受影响操作；不按“最新文件”任选一个。

同一 Operation ID 下可有多个计划修订，但任何时刻只能有一个明确的当前有效计划版本。旧版本保留且标记 SUPERSEDED，不得删除。

## 5. 奖励资格与防重

适配器必须为每种奖励定义资格粒度：每 Module、每个合格事件、每个角色、每个报告等级，或其他规则认可的单位。

每个资格建立稳定 `reward_eligibility_id`，并绑定：
- 规则条款与规则版本；
- 触发条件；
- 合格事件身份/修订；
- 角色或接收者范围；
- 可否与其他奖励叠加；
- 玩家事前是否已获知条件；
- 是否已裁定、已领取、已应用。

多个入口/多个事件若实质上指向同一资格，必须归并为同一 Eligibility ID。只有适配器明确允许多次奖励时才生成多个资格。奖励事件的重复重试不得重复发放。

未向玩家事前公开的可选目标不得事后生成奖励资格。任务结果、任务报告评级、可选目标、授权行为、MVP、免费成长、玩家成长选择和实际购买必须分别核验，不能合并为一个“通关奖励”。

## 6. 计划冻结与依赖图

PREPARE 必须冻结本次计算使用的完整输入。最低字段：

- `system_id`、System Rules Revision；
- Adapter Revision；
- Campaign Rules Revision；
- Module Rules Revision；
- Adjudication References（含批准桌规及适用范围）；
- Source Event Revision / Event Set Fingerprint；
- 玩家已确认的选择及其来源；
- 奖励资格集合与触发证据；
- 字段基准修订、目标修订；
- 结团范围、已知 UNKNOWN / DISPUTED；
- Settlement Plan 与计划版本；
- Closeout Operation ID、PREPARE Manifest ID、创建者/时间。

冻结不代表每项事实都已知。未知项必须明确列入计划，并标明阻塞哪些步骤。

**依赖顺序由适配器声明。** 通用层只执行有向无环图（DAG），不规定“成长必须先于恢复”或相反。例：若 MVP 提高 QA 上限，而规则要求任务间恢复按新上限恢复，则依赖为 MVP 资格确认 → 玩家成长选择/上限应用 → QA 恢复。其他系统可以声明不同合法顺序。

每个步骤声明：
- step_id、输入字段、前置步骤；
- 适用规则版本/条款；
- 计算方法与输出字段；
- 证据要求；
- 玩家是否需要确认；
- 是否会产生资源/奖励/成长事件；
- 失败时的阻塞范围。

发现循环、缺少前置、规则版本不匹配或存在未解析分支时，暂停受影响步骤，不由 Generic 层猜测顺序。可独立执行且不依赖该步骤的项目继续。

**重试规则：** 重试只验证并继续执行冻结的原计划，不按最新规则、最新人物卡或新聊天上下文重算。若计划本身错误，必须停止受影响步骤，追加有依据的计划修订，保留旧计划及修订关系，重新冻结新版本；已正确应用的字段不重复应用。

## 7. 结团事务：PREPARE → APPLY → RECONCILE → PUBLISH

复用 Runtime §14.4-A 的批次机制，不创建新的保存引擎。

### 7.1 PREPARE

1. 核验 Operation Identity 唯一且处于正确 Run/Branch。
2. 固定规则/适配器/桌规版本、事件修订、玩家选择和依赖图。
3. 汇总所有 Session 的适用事件与结团裁定证据。
4. 逐项计算奖励资格、资源变化、恢复/清零、成长选择和后果；按依赖图排序。
5. 建立完整 Settlement Plan、字段目标、应用操作 ID 和证据要求。
6. 将 PREPARE Manifest 独立持久化并读回；清单必须能在目标文件尚未更新、发布指针仍指向旧检查点时被发现。
7. PREPARE Manifest 独立读回成功后，活动 Operation 即使 Module 逻辑状态进入 CLOSEOUT_PENDING；读者通过发现该 Manifest 派生待结团锁定，不另写一份未发布的 Module 状态。PREPARE 尚未成功读回前，不得开始任何结团字段写入。

PREPARE Manifest 至少包括：Operation ID、Manifest ID、Batch ID（如 Runtime 批次机制要求）、Campaign/Module/Run 身份、分支、基准检查点、规则与计划版本、来源事件集合、目标字段清单、每字段基准/目标修订、依赖顺序、各步骤状态、可见性/接收者范围、候选文件定位、创建时间和校验指纹。

### 7.2 APPLY

- 按冻结依赖图逐字段应用。
- 每个字段操作使用稳定 Field Operation ID，重试时先读取实际目标，不重复应用已正确写入的增量。
- 对余额/计数使用可证明的目标值或事件增量语义；禁止在部分成功后再次无条件执行“+1”。
- 保留原始消耗、奖励和恢复事件；恢复满额不等于此前没有消耗。
- 每个目标分别记录应用结果与读回证据，不把多文件部分成功合并为整体成功。
- 玩家尚未作出选择的成长/购买不得代替玩家执行。

### 7.3 RECONCILE

独立重新读取：
- PREPARE Manifest；
- 最新可验证发布检查点；
- 所有被写入的权威目标；
- 相关 Session Logs / Resource Ledger；
- 角色人物卡、Campaign State；
- Module 生命周期字段；
- 目标投影/玩家侧摘要（如本批次包含）。

逐字段对比基准值、目标值、操作 ID、事件身份、内容修订和应用证明。文件存在、行数一致、调用回执或旧缓存都不是应用证明。

### 7.4 PUBLISH（唯一 CLOSED 生效点）

最终发布批次必须同时包含：
- 结团结果与适用的结算/奖励/成长/恢复结果；
- 所有必需字段的独立应用证明；
- Module 生命周期状态 CLOSED；
- 结团关闭原因/结果摘要；
- 下一 Module 所需的源 Module 交接字段；
- 发布清单、版本指针和必要的玩家投影版本。

**最终发布指针成功提交时，以上结果与 CLOSED 一起生效。** 不得先发布结算，再单独写 CLOSED；不得在发布前把候选文件当成正式状态。

若 Git/宿主可用原子提交：把最终清单、所有必需目标和内部发布指针放在同一提交中，并以预期分支 HEAD 做条件更新。内部指针记录 Batch ID/Domain Revision；读取端再确认实际 commit 包含该指针与目标。不得要求提交预写自身 commit hash。

若宿主只能分次写入：先准备候选和证明，最后以条件更新/等价原子操作推进唯一发布指针。读者只读取该指针引用的目标版本；未被引用的候选文件不构成正式状态。若宿主没有条件发布能力，保持 UNPUBLISHED，交付待保存增量，不得声称 CLOSED 已正式发布。

README、Campaign 索引和 Handoff 是投影，可在发布后更新；它们不决定 CLOSED 是否生效。若其更新失败，发布状态仍按权威指针判断，但标记 projection repair pending，并阻止依赖这些投影的入口误导用户。

## 8. 冷恢复：新会话无历史恢复流程

新 Chat/新模型/新操作者不得依赖旧聊天记录或助手回忆。按以下顺序：

1. 固定仓库提交、当前分支和运行身份。
2. 读取 Module 当前权威生命周期字段及最新可验证已发布检查点。
3. 按 Campaign ID + Module ID + Run/Branch Identity 查询关联 Closeout Operation。
4. 读取 Runtime State 的 persistence.batch_id、status、prepare_manifest_ref、previous_published_checkpoint_ref，以及 reconciliation_manifest_refs[]；同时查询 Module 现有 GM-only Operational Diagnostics 中按 Run/Module Identity 记录的活动结团操作。必须能找到未发布清单；不得只从旧发布指针向前推断。
5. 校验 Operation ID 唯一性、Manifest/Batch ID、规则版本、计划修订、来源事件集合和基准检查点。
6. 逐字段读取权威目标，核验应用证明与当前值。
7. 判断事务阶段及发布状态。
8. 只执行证据支持的缺项修复或原计划重试；存在多候选、身份冲突、规则/事件漂移、内容冲突时停止受影响范围。

**发现入口要求：** PREPARE Manifest 必须独立于目标覆盖文件保存，作为 Runtime §14.4-A 既有 GM 批次记录 / Module GM-only Operational Diagnostics 中的不可变记录，按 Run Identity + Module ID + batch_id 定位。Runtime State 的 persistence.prepare_manifest_ref 指向该 Manifest；最终发布后的 reconciliation_manifest_refs[] 保留完整不可变 Manifest 权威引用。applied_event_ids[] 仅是定位索引，不构成应用证明。Operational Diagnostics 与 Runtime State 引用共同构成现有发现路径；不得新建独立 Operation Index、索引服务或第二套 Manifest 注册表。

如果新会话无法证明“没有待处理操作”，不得按旧检查点重新结算。无法读取 Operational Diagnostics、Runtime State 的 prepare_manifest_ref / reconciliation_manifest_refs[]，或其完整性与运行身份无法核验时，标记 PENDING_DISCOVERY / UNVERIFIABLE，阻止依赖结团状态的推进；允许不依赖未知字段的只读和安全互动。

## 9. 独立状态维度

不得用单一 STATUS 混合事实、应用、发布和交接。

| 维度 | 允许值 | 含义 |
|---|---|---|
| Value Evidence | KNOWN / UNKNOWN / DISPUTED | 字段当前事实是否可知、是否冲突 |
| Application | NOT_APPLIED / APPLIED / PARTIAL / UNVERIFIABLE | 该操作是否已应用；NOT_APPLIED 必须有证据 |
| Publication | PUBLISHED / UNPUBLISHED / UNKNOWN | 最终批次是否正式发布 |
| Handoff | READY / BLOCKED / NOT_CHECKED | 对指定目的 Module 的交接是否通过 |
| Discovery | FOUND / NOT_FOUND_VERIFIED / PENDING_DISCOVERY / UNVERIFIABLE | 是否能通过既有 Operational Diagnostics 与 Runtime Manifest 引用发现关联 PREPARE/Operation |

UNKNOWN 是值状态；UNVERIFIABLE 是证据/核验能力状态。不能把无法读取写成 UNKNOWN=0，也不能把未核验写成 NOT_APPLIED。

Handoff READY 必须绑定：
- Published Checkpoint ID；
- Destination Module ID；
- 该目的 Module 所需字段集合及规则版本；
- 每字段证据/应用状态；
- 该 Module 的独立 Preflight 结果。

CLOSED 只证明源 Module 最终批次已发布，不证明目的 Module READY。目的 Module 的 READY 由它自己的依赖清单判断。

## 10. 两种中断的强制恢复语义

### A. 部分字段写入

例：Time 的一个配对字段 +1 已写入，另一字段 -1、人物卡和发布指针尚未完成。

- 新会话找到原 Operation/Manifest/Batch。
- 独立读回已写目标，确认 +1 的 Field Operation ID、内容和修订确属原计划。
- 已正确应用字段标记 APPLIED，不再重复 +1。
- 缺失字段按原计划应用；对账配对方向和目标值。
- 人物卡候选只应用一次。
- 所有必需目标核验通过后才允许 PUBLISH。
- 如果已写值无法归因、基准漂移或出现多个候选，标记 DISPUTED/UNVERIFIABLE，停止相关字段；不猜测、不重复加减。

### B. 最终发布回执丢失

- 发布指针已指向原批次，且目标版本均可独立验证：认定原批次已发布，不重复。
- 指针仍在原基准，Manifest 与目标候选未变化，且条件更新仍成立：只重试原批次发布。
- HEAD 已推进、目标被其他批次修改或发布历史无法证明：查询发布历史和当前目标；不确定则停止，不覆盖。
- 宿主不支持条件发布/独立读回：标记 UNPUBLISHED/UNVERIFIABLE，交待待保存增量，不声称 CLOSED 生效。

## 11. 未决项与阻塞范围

每个未决项记录：
- issue_id、字段/事件、证据；
- Value Evidence、Application、Publication；
- 影响的依赖步骤；
- 是否阻塞 Module CLOSED；
- 是否阻塞特定 Destination Module READY；
- 是否只阻塞某类成长/购买/资源支出；
- 可继续的独立互动；
- 解除条件与所需证据。

例：历史普通 Chaos Pool 属于模组内临时资源，规则规定结团清零时，历史绝对余额缺口可以是 AUDIT_ONLY，不阻止结团；跨模组持续 Demerits 精确余额未知，则阻止依赖该余额的扣减/购买/人物卡准确同步，但不自动阻止叙事结团或不依赖该值的幕间互动。具体判断由适配器给出。

## 12. 结团保障清单

以下检查不得因流程简化而删除：

1. 最终任务结果与报告评级分别判定。
2. 奖励资格逐项对应触发证据、规则条款和玩家事前知情状态。
3. 未公开的可选目标不得事后发奖。
4. 申诉窗口、复核、封账和合法纠错路径遵循系统规则。
5. MVP/特殊奖项与普通奖励分开核验。
6. 玩家成长选择、免费成长格、轨迹收益、实际购买/消费分开记录。
7. Time 与其他配对资源字段分别记账、核对方向，不以一字段推算另一字段绝对余额。
8. 自动恢复/清零只按规则适用范围执行，保留历史消耗与恢复事件。
9. 关键道具跨模组一次性限制单独核验。
10. 玩家摘要只含其已知/获准内容；GM 审计资料独立保存。

## 13. Postmortem、归档与下一 Module

**Postmortem：**
- 独立、可选、只读；不属于结团事务，不是 CLOSED 门槛。
- 不得写入或改变资源、奖励、成长、人物卡、Campaign State、Module 生命周期或下一 Module READY。
- 发现事实/状态错误时只提交证据与纠错建议；实际更正走独立授权纠错流程：追加修订事件 → PREPARE → APPLY → RECONCILE → PUBLISH。
- Postmortem 未完成不阻止幕间互动、下一 Module 备团或开团。

**归档：**
- ARCHIVED 是独立归档状态，不与 CLOSED 合并。
- 归档不改写旧事件、检查点或批次。

**下一 Module：**
- 允许与源 Module 结团并行备团。
- 目的 Module 只能在其自身 Preflight 核验所需源字段后 READY。
- CLOSED 与 READY 分开；源 Module 关闭不自动授予目的 Module 开团许可。
- 用户选定新 Module 后，Campaign README、模组索引、战役交接、新 Module README/Runtime/Player Notes/Resource Ledger 入口应按既有 handoff 交付契约同步；必要项作为目的 Module 入口检查，不反向改变源 Module 已发布 CLOSED。

## 14. 规则适配器契约

每个系统适配器最少声明：

- System ID / Ruleset Revision；
- 资源字段、作用域、唯一权威、单位和可否负值；
- 触发身份与奖励资格粒度；
- 任务结果/报告评级/奖励/处分/MVP/成长/购买定义；
- 申诉与封账规则；
- 自动恢复、重置、持续资源与关键道具规则；
- 结团依赖 DAG；
- 未知字段对各步骤的阻塞范围；
- 必须保存的证据及玩家确认点；
- 最终交接字段集合。

Generic 层只验证适配器契约完整、版本匹配、依赖无环、目标字段有唯一所有者；不理解系统机制本身。

## 15. 首版最小实施范围

首版只做：
1. 本协议作为 Generic 规范入口。
2. 在现有 Runtime §14.4-A 批次契约中补齐结团 Operation/Manifest 的可发现性与最终 CLOSED 发布边界。
3. 增加 Triangle Agency 适配器文件，明确其资源分类、结团依赖、奖励/成长/恢复和证据要求。
4. 在现有 02、09、13 文件中以引用和必要流程修订接入，不复制本协议全文。
5. 为 Bower Street 既有结团记录标记 LEGACY_UNMIGRATED / LEGACY_CLOSEOUT；只做证据标注，不伪装成 v0.3 原子发布，不重做历史结算。
6. 建立最小冷恢复夹具和验收记录。

首版不做：
- 新资源引擎、数据库、迁移引擎、第二套事件系统；
- 新建独立快照文件或复制余额到 Runtime；
- 把全部历史 Module 批量迁移；
- 强制所有资源逐笔核算到结团绝对余额；
- 将 Postmortem 加入关闭门槛；
- 将 Triangle Agency 专属机制写入 Generic。

## 16. 最小验收矩阵

| ID | 场景 | 必须结果 |
|---|---|---|
| C01 | 正常单 Session Module | 完整结算并发布 CLOSED；Session CLOSED 与 Module CLOSED 区分 |
| C02 | 多 Session Module | 聚合正确 Session 证据；历史日志不覆盖 |
| C03 | MVP 改变资源上限 | 依适配器 DAG 决定成长与恢复顺序；结果正确 |
| C04 | 规则/桌规版本冻结 | 重试不读取新规则重算 |
| C05 | 同一奖励从多个入口触发 | 归并同一 Eligibility ID，不重复发奖 |
| C06 | 部分字段已应用 | 冷恢复定位原 Manifest；已应用字段不重复，缺项补齐 |
| C07 | PREPARE 已写、发布指针旧 | 新会话仍能发现未发布 Manifest，不从旧指针误判无事务 |
| C08 | 最终发布回执丢失 | 依据指针与独立读回判断已发布/重试/停止 |
| C09 | CLOSED 与最终批次 | 未发布前不 CLOSED；最终发布同时生效 |
| C10 | 未知持续资源 | 不猜零；只阻塞依赖该字段的步骤 |
| C11 | Postmortem 未完成 | 不阻塞 CLOSED、幕间或目的 Module Preflight |
| C12 | CLOSED 源 Module / 目的 Module | CLOSED 不自动推导 READY；按目的 Module 依赖独立核验 |
| C13 | 无条件写入能力的宿主 | 降级为人工待保存增量，不宣称已发布 |
| C14 | 多个 Operation/Manifest 候选 | 停止自动处理，要求解决身份冲突 |
| C15 | 复盘发现错误 | 只提交纠错建议；实际更正走独立授权和新批次 |

## 17. 迁移映射

| 现有文件 | 迁移动作 |
|---|---|
| `GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md` §14.4-A | 复用批次事务；补充 Operation/Manifest 可发现入口、条件唯一创建、最终 CLOSED 指针语义 |
| `GM_Training/02_WORKFLOW_AND_PREFLIGHT.md` §C | 结团步骤改为引用本协议；Postmortem 从关闭门槛移出；保留结果/奖励/成长保障 |
| `GM_Training/09_MODULE_FOLDER_STANDARD.md` §12–13 | 保留资源作用域与账本唯一权威；补充结团状态和交接引用，不另造资源账本 |
| `GM_Training/13_PREP_TO_RUNTIME_HANDOFF_STANDARD.md` | 增加结团前源字段交接、最终发布后目的 Module 独立 READY 检查；保留并行备团 |
| `Systems/Triangle_Agency/Rule_Reference/` | 新增 Triangle Agency Closeout Adapter；放置系统专属资源、奖励、成长、恢复和结团 DAG |
| `Campaigns/Zarek/模组/<Module>/09_RESOURCE_LEDGER.md` | 保留流水权威；历史结团只追加 Legacy/证据状态，不重写 |
| `Campaigns/Zarek/模组/<Module>/03_RUNTIME_STATE.md` | 保留场景与生命周期权威；不复制余额；标记旧结团批次未迁移 |
| Campaign 人物卡 / Campaign State | 最终发布后才接受新边界快照；保留旧版本和来源 |

## 18. 实施前自审与能力声明

本版已覆盖：唯一字段权威、系统依赖 DAG、冻结计划、稳定操作身份、奖励资格防重、独立 PREPARE 发现、部分写入恢复、最终发布回执丢失、CLOSED 单一生效点、目的 Module READY、局部阻塞、独立 Postmortem、玩家/GM 信息隔离及最小迁移范围。

本文件本身属于设计产物，不证明仓库已完成迁移，不证明 Runtime 宿主支持条件创建/条件发布/独立读回，也不证明新会话能成功发现未发布 Manifest。上述能力必须通过实际仓库实现检查、合成冷恢复测试和宿主持久化故障注入分别验证。

任何未执行测试标记 NOT STARTED / NOT TESTED；不得把静态设计推演写成运行 PASS。
