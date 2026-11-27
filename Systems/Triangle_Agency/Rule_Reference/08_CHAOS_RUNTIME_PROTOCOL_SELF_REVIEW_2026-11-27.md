# Triangle Agency Chaos Runtime｜单会话协议自测报告

> 类型：SINGLE_SESSION_SELF_TEST / PROTOCOL WALKTHROUGH
> 结果：19/19 PASS（协议逻辑覆盖）；NOT INDEPENDENT REVIEW / NOT PRODUCTION ACCEPTANCE
> 被测协议：`03_CHAOS_RUNTIME_PROTOCOL.md`
> 测试夹具：`06_CHAOS_RUNTIME_REGRESSION_v1.md`
> 共享契约：`Systems/SYSTEM_RULE_RUNTIME_INTEGRATION_PROTOCOL.md`
> 本次工作分支：`feat/triangle-agency-rule-runtime-integration-v1`
> 说明：本报告由同一助手读取协议并逐项推演预期输入/输出，不是独立模型盲测、真实多轮平台测试或生产 Runtime 测试。

## 1. 执行范围

- 已逐项检查 C-01 至 C-19 的初始状态、触发条件、预期资源变化、世界状态结果、可见信息和停止条件。
- 依据：Triangle Agency 中文 v22 固定版本 Markdown、当前系统基础规则笔记、Chaos Runtime Protocol、Campaign Binding / adjudication、Bower Street 现有历史账本与 Session 记录。
- 本轮修改了 Campaign Binding、规则协议、回归夹具、自测报告、Bower Street GM Prep 与 Resource Ledger 的初始化来源说明；没有改写人物卡、Session Log 或历史游戏事件，也没有补造任何历史 Chaos 交易。
- 没有执行真实骰子、真实 Runtime 写入、工具级计时或独立宿主交互。

## 2. 逐项结果

| Case | 结果 | 自测观察 |
|---|---|---|
| C-01 No-trigger ordinary action | PASS | 普通行动不触发 Chaos 子系统；不读取 Chaos 文件、不轮询 Pool、不延迟行动。 |
| C-02 Roll generation handoff | PASS | 消费掷骰模块已提交的 +5 delta；同一 event 重试不重复加值；不重算骰子。 |
| C-03 Special Rule generation | PASS | 明确 Special Rule 触发 +10；作为独立生成事件，不误记为消费。 |
| C-04 Disruptive Minor Anomaly | PASS | 在生成事件上应用附近 Disruptive Minor Anomaly 的额外 +1；不重复计算基础骰面。 |
| C-05 Anomaly near Agents | PASS | 识别近旁超自然行动的 Chaos 支付要求；要求有实际行动、动机、目标与效果，不自动强制花费。 |
| C-06 Beyond Focus | PASS | 超出 Focus 时识别汲取环境 Chaos 的规则依赖；具体效果/成本仍由系统规则与当前状态决定。 |
| C-07 Domain cost handling | PASS | 1/2/3 成本免费；4 成本按 12 处理；8 成本按 24 处理，Pool 20 不足时拒绝。 |
| C-08 Outside Domain | PASS | 域外 4 成本按 4 处理，不应用三倍成本或免费阈值。 |
| C-09 Domain free repeatability | PASS | 域界内费用 ≤3 的效果免费且可重复使用；费用 >3 按三倍成本。 |
| C-10 No target Anomaly | PASS | 仍追踪 Pool；只允许有已建立来源/行动者/因果依据的效果，不补造幕后操纵者。 |
| C-11 Human-caused analogue | PASS | 人类行为可产生类似效果而不扣 Chaos；仅按已建立动机与行为解决。 |
| C-12 Effect materialization | PASS | 资源从 5 减至 4，同时门锁/通行状态确实更新；不是只改余额或只写氛围。 |
| C-13 Public Pool / secrecy | PASS | 当前 Pool 与效果说明可公开；隐藏动机、未发现的特殊规则和 GM-only 信息继续隔离。 |
| C-14 Unknown balance | PASS | 当前余额待核时暂停依赖 Pool 的效果；无关互动继续。 |
| C-15 Mission close reset | PASS | 记录 13 未使用 Chaos 被丢弃，关闭任务池为 0；不影响 Loose Ends 等持续状态。 |
| C-16 No arbitrary adversity | PASS | Pool 高达 30 但没有有效机会时不花费，不制造惩罚性事件或强制掷骰。 |
| C-17 synthetic Campaign Branch total = 1 | PASS (historical self-walkthrough only) | 合成输入 1 落在 0 档；不代表 Zarek Campaign 当前数据，也不把该值存入 Systems。
| C-18 Threshold transition 10 → 11 | PASS | 在任务真正开始时重读总数；11 进入 11 档，初始 Chaos 5、Weather Event count 1。 |
| C-19 Branch / mission resource separation | PASS | 分部 Loose Ends 与任务 Chaos Pool 独立；任务清零不重置分部总数。 |

## 3. 发现并保留的待审查项

### 3.1 Campaign data ownership

- The current Branch Loose Ends total is Campaign-owned dynamic state, not system-rule data.
- The former Zarek-specific value has been removed from this system-layer self-review and runtime protocol. Campaign state remains in the Campaign handoff; Module ledgers retain historical snapshots and module deltas.
- The old C-17 walkthrough used a confirmed Campaign input as an example. It is retained only as historical evidence of the prior walkthrough and is not a system-layer default or current runtime input.

### 3.2 Domain 免费效果的重复使用口径

- 印刷页 156 明确费用 3 或更低的 Chaos Effects 在 Domain 内免费显现。
- 本协议采用执行口径：费用 ≤3 的效果在 Domain 内免费且可重复使用；费用 >3 的效果按三倍费用支付。
- 这是一项为运行选择的明确口径，不再把恰好 3 的重复使用边界作为阻塞项。

### 3.3 历史团可恢复程度

- Bower Street SESSION 01 有一笔 Chaos 生成未完成独立核验。
- SESSION 02 只恢复了一笔完整 +5 生成事件，不能由此计算 SESSION 02 的最终历史余额。
- 模组结团后 Pool 按规则清零；旧账本不回填虚构的消费或效果事件。
- 用户反馈确认当时 GM 没有充分利用 Chaos 制造局势变化；现存 Session 记录不足以逐一定位每次漏掉的效果机会。

## 4. 自测结论

**PASS：协议已覆盖生成接入、有效触发识别、主动但受规则约束的效果使用、Domain 成本、世界状态落地、信息公开/保密、任务清零和 Campaign 作用域隔离。**

**NOT INDEPENDENT REVIEW：** 同一助手完成设计与推演，存在自我审查偏差。高级 AI 仍需独立检查协议的规则解释、触发覆盖、测试 Oracle 和 Campaign 作用域。

**NOT PRODUCTION ACCEPTANCE：** 本次未证明真实宿主会自动识别触发、写入 Resource Ledger、恢复事件或实际改变平台持久化状态。现有 Roll Runtime Adapter 仍是本地参考实现；Dice Resolution 路由和 Triangle 专属协议的仓库状态仍须按各自 DESIGN / NOT ENABLED 标记处理。

## 5. 建议的独立审查重点

1. 是否完整区分系统规则、Campaign override、模组特例和 GM 操作建议。
2. Chaos 机会信号是否足够覆盖，但不会让每轮普通行动产生额外轮询。
3. Anomaly 超出 Focus、近旁行动、Domain 内免费效果及自定义 Special Rule 的解释是否准确。
4. Domain 内费用 ≤3 的免费与重复使用执行口径是否与原文及桌面目标一致。
5. 每次任务按当前 Branch Loose Ends 读取表格的初始化流程，是否正确处理阈值、天气事件数量与分部限制。
6. 19 个测试案例是否能有效区分“正确不触发”“应主动评估”“允许效果但不能擅自消费”和“消费后必须改变世界状态”。
7. 是否应补充多轮/多 Session 的真实 Runtime 事件链测试，以及如何避免引入第二套资源账本。


## 6. Independent-review remediation status (2026-11-27)

- The earlier 19/19 result remains a same-session protocol walkthrough only. It does not validate the revised contract and is not promoted to independent or production acceptance.
- C-17 has been changed to a synthetic Campaign fixture; the real Branch Loose Ends value is maintained only in Campaign-owned state.
- Weather handling now distinguishes ordinary weather records from a specific weather result that explicitly changes Branch Loose Ends. A threshold-table rerun is not triggered by ordinary weather.
- Mission Pool lifecycle now distinguishes old mission closeout reset, new mission Pool creation at 0, and the separate table-based Starting Chaos grant.
- New R-01–R-24 fixtures are defined in the regression file. They are pending execution; no result is claimed.
- The updated protocol and fixtures still require independent blind behavior tests, multi-turn recovery, and host-level failure injection. The production activation gate remains closed.