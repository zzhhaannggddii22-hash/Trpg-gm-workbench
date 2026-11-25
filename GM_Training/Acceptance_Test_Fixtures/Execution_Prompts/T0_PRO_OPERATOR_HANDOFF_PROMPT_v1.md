# T0 自然语言盲测 v1｜Pro 操作者交接提示

你是本次盲测的操作者、证据管理员和结果打包者，不是被测 GM。请在 ChatGPT Pro 账户及其可用的独立浏览器会话中执行仓库 `zzhhaannggddii22-hash/Trpg-gm-workbench` 的 T0 Natural Language Blind Suite v1。

## 0. 任务边界
- 只执行盲测准备核验、八个目标 Chat 试次、证据保存、评分和结果 ZIP。
- **禁止开展性能优化或修改 GM 规范。** 只有盲测证据完成、结果由独立复核者检查且达到既定门槛后，才可另行启动优化。
- 不读取、不修改 `Campaigns/` 中任何正式 Campaign、人物、模组、CANON、Session Log 或真实玩家资料。测试只使用合成附件。

## 1. 锁定当前权威版本
先读取仓库 `main` 的最新 commit SHA，并逐一读取：
- 目标 Chat 提示：`GM_Training/Acceptance_Test_Fixtures/Execution_Prompts/GM_T0_BLIND_EXECUTION_PROMPT_v1.md`
- 操作者协议：`GM_Training/Acceptance_Test_Fixtures/Execution_Prompts/GM_T0_BLIND_OPERATOR_PROTOCOL_v1.md`
- 通用规范：`GM_Training/SKILL.md`、`GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md`
- 操作者夹具：`GM_Training/Acceptance_Test_Fixtures/T0_NATURAL_LANGUAGE_BLIND_SUITE_v1_OPERATOR.md`
- 八份场景附件：`GM_Training/Acceptance_Test_Fixtures/T0_BLIND_PACKET_A01.md` 至 `T0_BLIND_PACKET_A08.md`
- 历史状态报告：`GM_Training/Acceptance_Reports/T0_NATURAL_LANGUAGE_BLIND_SUITE_v1_PREPARATION_AND_EXECUTION_STATUS_2026-11-24.md

必须以当前路径为准。旧路径 `GM_Training/GM_T0_BLIND_EXECUTION_PROMPT_v1.md` 与 `GM_Training/GM_T0_BLIND_OPERATOR_PROTOCOL_v1.md` 只是迁移兼容入口，不是权威正文。记录 commit SHA、每份文件的 Git blob SHA、读取时间。若材料缺失或版本无法确认，停止并报告。

## 2. 严格隔离
- 八个试次 A01–A08 必须各自使用一个全新、独立的空白 ChatGPT 对话。
- 目标 Chat 只能获得目标 Chat 执行提示、`SKILL.md`、`07_RUNTIME_CONTROL_PROTOCOL.md`、当前一个 `T0_BLIND_PACKET_A0N.md` 和当前轮玩家原话。
- 操作者夹具、预期路由、评分表、硬失败标准、操作者协议、其他试次附件及未来轮次输入，均不得粘贴或上传到目标 Chat。
- 每轮只发送一条玩家原话；保存完整回复后再发送下一轮。
- 不得用当前对话、同一 Chat 角色扮演、清空消息、分支或“假装没看过”代替独立 Chat。
- 仓库是公开仓库。标记 operator-only / GM-only 不构成访问控制。操作者不得把公开链接提供给目标 Chat，也不得指示目标 Chat 浏览测试目录。目标 Chat 若自行访问或读到操作者材料，该试次标记 CONTAMINATED。

## 3. 执行与证据
按 A01 至 A08 执行。每个试次记录：
- 新建空白 Chat 的 URL、创建时间和可核验截图/证据；
- 产品模型、Thinking 档位、浏览器/客户端和可见设置；
- 当前规范的实际读取证据及对应 commit/blob SHA；
- 当前附件原始字节 SHA-256、大小、上传时间；
- 四轮逐字原始输入、完整原始输出、发送/回复时间、可见工具轨迹；
- 异常、拒绝、缺失和任何协议偏离。

原始证据只追加，不覆盖。不得收集密码、Cookie、访问令牌。无法取得某项证据就记 UNKNOWN，不得以模型自述代替外部证据。

## 4. 评分
八个试次全部结束并封存原始记录后，才打开操作者夹具评分。既定标准：
- 8 个试次 × 4 轮 = 32 轮；每轮五个维度、每维 0–2 分；总分 320。
- 总分至少 288/320（90%）。
- 五个维度分别至少 85%。
- 每个试次至少 34/40。
- 任何硬失败均导致整体不通过。
- 未执行的试次标记 NOT RUN，不记 0 分或 PASS。
- 行为评分与证据等级分别报告；证据缺口不能由行为分补偿。
- 若评分者已看过答案，明确标记 scorer_blinded=false。

## 5. 结果 ZIP
按 `GM_Training/Acceptance_Test_Fixtures/Execution_Prompts/T0_RESULTS_RETURN_PACKAGE_PROTOCOL_v1.md` 生成结果包。至少包含 README_RESULTS.md、manifest.json、execution、environment、evidence、scoring、deviations。保留全部原始逐轮记录，不只交摘要。manifest 为每个文件记录路径、大小和 SHA-256。生成后执行 ZIP 完整性检查、解压检查及哈希校验。

**必须把 ZIP 作为附件交回发起本任务的用户/独立复核者**，不能只把文件留在云端或只在 GitHub 写摘要。另在 GitHub 建立新的结果报告 PR，历史 NOT STARTED 报告不得覆盖。

## 6. 结束报告
明确报告：八个试次真实执行数量、32 轮完整性、隔离/污染情况、证据等级、逐维度分数、总分、硬失败、偏离协议、结果 ZIP 的文件名和 SHA-256、GitHub 结果 PR。不得将仓库 CI、静态检查或本操作者推演计为目标 Chat 行为测试。
