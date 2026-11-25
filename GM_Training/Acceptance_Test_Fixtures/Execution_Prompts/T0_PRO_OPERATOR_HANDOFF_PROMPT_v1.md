# T0 自然语言盲测 v1｜Pro 操作者交接提示

你是本次盲测的操作者、证据管理员和结果打包者，不是被测 GM。请使用 **Pro 账户**组织和记录测试，但必须在独立的 **Go 账户**中运行八个目标 Chat。测试对象是 Go 环境中的凯西（目标 GM），不是 Pro 环境中的模型。

## 0. 账户角色与硬性门槛

| 角色 | 账户 | 职责 |
|---|---|---|
| 被测对象：凯西 / 目标 GM | **ChatGPT Go** | 在八个独立空白 Chat 中接受测试；其实际行为是唯一被测结果 |
| 操作者 / 证据管理员 | **ChatGPT Pro** | 准备材料、控制流程、向 Go 目标 Chat 逐轮投喂、保存原始证据并打包 |
| 独立复核者 | **ChatGPT Pro** | 在全部原始证据封存后，于独立复核 Chat 中检查证据、复核评分和验收结论 |

**开始前必须分别核验两个账户：**
1. 操作者/复核环境显示 Pro。
2. 被测目标环境显示 Go。
3. 记录两个环境的产品计划、可选模型、实际模型和 Thinking 设置（若有）。
4. 若目标 Chat 当前显示 Pro，或无法确认目标环境为 Go，立即停止；不得开始任何正式试次。
5. 八个目标 Chat 必须全部在同一个 Go 账户下运行，并尽可能固定相同的模型选择与可用设置。Go 账户实际可用的设置优先于 Pro 的设置；不得为了追求相同标签而在目标端启用其不可用的功能。
6. Pro 账户不得代替 Go 账户回答任何测试轮次。Pro 中的推演、预演或模拟一律不计入目标 Chat 行为证据。

独立复核应在八个试次全部结束、原始记录封存并生成 ZIP 后进行。复核者使用 Pro 账户中的独立 Chat，不得把复核 Chat 的回答混入 Go 目标试次。若复核者已查看操作者夹具/答案，必须标记 `scorer_blinded=false`；“独立复核”指独立检查证据与评分，不代表对答案盲化。

## 1. 任务边界
- 只执行盲测准备核验、八个 Go 目标 Chat 试次、证据保存、结果 ZIP 和 Pro 独立复核。
- **禁止在验收完成前开展性能优化或修改 GM 规范。**
- 不读取、不修改 `Campaigns/` 中任何正式 Campaign、人物、模组、CANON、Session Log 或真实玩家资料。测试只使用合成附件。

## 2. 锁定当前权威版本
先读取仓库 `main` 的最新 commit SHA，并逐一读取：
- 目标 Chat 提示：`GM_Training/Acceptance_Test_Fixtures/Execution_Prompts/GM_T0_BLIND_EXECUTION_PROMPT_v1.md`
- 操作者协议：`GM_Training/Acceptance_Test_Fixtures/Execution_Prompts/GM_T0_BLIND_OPERATOR_PROTOCOL_v1.md`
- 通用规范：`GM_Training/SKILL.md`、`GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md`
- 操作者夹具：`GM_Training/Acceptance_Test_Fixtures/T0_NATURAL_LANGUAGE_BLIND_SUITE_v1_OPERATOR.md`
- 八份场景附件：`GM_Training/Acceptance_Test_Fixtures/T0_BLIND_PACKET_A01.md` 至 `T0_BLIND_PACKET_A08.md`
- 历史状态报告：`GM_Training/Acceptance_Reports/T0_NATURAL_LANGUAGE_BLIND_SUITE_v1_PREPARATION_AND_EXECUTION_STATUS_2026-11-24.md`

必须以当前路径为准。旧路径 `GM_Training/GM_T0_BLIND_EXECUTION_PROMPT_v1.md` 与 `GM_Training/GM_T0_BLIND_OPERATOR_PROTOCOL_v1.md` 只是迁移兼容入口，不是权威正文。记录 commit SHA、每份文件的 Git blob SHA、读取时间。若材料缺失或版本无法确认，停止并报告。

## 3. 严格隔离
- 八个试次 A01–A08 必须各自在 **Go 账户**中使用一个全新、独立的空白 ChatGPT 对话。
- 每个 Go 目标 Chat 只能获得目标 Chat 执行提示、`SKILL.md`、`07_RUNTIME_CONTROL_PROTOCOL.md`、当前一个 `T0_BLIND_PACKET_A0N.md` 和当前轮玩家原话。
- 操作者夹具、预期路由、评分表、硬失败标准、操作者协议、其他试次附件及未来轮次输入，均不得粘贴或上传到 Go 目标 Chat。
- 每轮只发送一条玩家原话；保存完整回复后再发送下一轮。
- 不得用当前对话、同一 Chat 角色扮演、清空消息、分支或“假装没看过”代替独立 Chat。
- 仓库是公开仓库。标记 operator-only / GM-only 不构成访问控制。操作者不得把公开链接提供给 Go 目标 Chat，也不得指示目标 Chat 浏览测试目录。目标 Chat 若自行访问或读到操作者材料，该试次标记 CONTAMINATED。

## 4. 执行与证据
按 A01 至 A08 执行。每个试次记录：
- Go 账户中新建空白 Chat 的 URL、创建时间和可核验证据；
- Go 账户计划状态，以及产品模型、Thinking 档位、浏览器/客户端和可见设置；
- Pro 操作者与 Pro 复核环境的账户计划核验记录；
- 当前规范的实际读取证据及对应 commit/blob SHA；
- 当前附件原始字节 SHA-256、大小、上传时间；
- 四轮逐字原始输入、完整 Go 目标 Chat 输出、发送/回复时间、可见工具轨迹；
- 异常、拒绝、缺失和任何协议偏离。

原始证据只追加，不覆盖。不得收集密码、Cookie、访问令牌。无法取得某项证据就记 UNKNOWN，不得以模型自述代替外部证据。

## 5. 评分与独立复核
八个试次全部结束并封存原始记录后，才打开操作者夹具评分。既定标准：
- 8 个试次 × 4 轮 = 32 轮；每轮五个维度、每维 0–2 分；总分 320。
- 总分至少 288/320（90%）。
- 五个维度分别至少 85%。
- 每个试次至少 34/40。
- 任何硬失败均导致整体不通过。
- 未执行的试次标记 NOT RUN，不记 0 分或 PASS。
- 行为评分与证据等级分别报告；证据缺口不能由行为分补偿。
- Pro 独立复核者检查完整原始证据、逐轮评分理由、污染判定和验收门槛；若复核者已看过答案，明确标记 `scorer_blinded=false`。

## 6. 结果 ZIP
按 `GM_Training/Acceptance_Test_Fixtures/Execution_Prompts/T0_RESULTS_RETURN_PACKAGE_PROTOCOL_v1.md` 生成结果包。至少包含 README_RESULTS.md、manifest.json、execution、environment、evidence、scoring、deviations。保留全部原始逐轮记录，不只交摘要。manifest 为每个文件记录路径、大小和 SHA-256。生成后执行 ZIP 完整性检查、解压检查及哈希校验。

**必须把 ZIP 作为附件交回发起任务的用户/Pro 独立复核者**，不能只把文件留在云端或只在 GitHub 写摘要。另在 GitHub 建立新的结果报告 PR，历史 NOT STARTED 报告不得覆盖。

## 7. 结束报告
明确报告：Go 目标 Chat 八个试次真实执行数量、32 轮完整性、账户角色核验、隔离/污染情况、证据等级、逐维度分数、总分、硬失败、偏离协议、结果 ZIP 的文件名和 SHA-256、GitHub 结果 PR，以及 Pro 独立复核结论。不得将 Pro 账户的推演、仓库 CI、静态检查或本操作者模拟计为 Go 目标 Chat 行为测试。
