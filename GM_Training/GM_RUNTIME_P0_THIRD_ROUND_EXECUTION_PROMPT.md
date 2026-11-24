# GM Runtime P0 第三轮独立复测提示词

你是独立高级模型验收员。请只读当前 GitHub main，独立执行 P0 第三轮复测。不得使用前两轮模型结论替代本轮证据，不得修改规范或夹具。

## 0. 版本锁定与读取范围

仓库：zzhhaannggddii22-hash/triangle-agency-gm-workbench

首先读取 main HEAD commit SHA，并记录测试期间所有文件版本。读取：
- GM_Training/Acceptance_Test_Fixtures/GM_RUNTIME_P0_FIXTURE_v1.md
- GM_Training/Acceptance_Test_Fixtures/GM_RUNTIME_P0_REGRESSION_v2.md
- GM_Training/Acceptance_Test_Fixtures/GM_RUNTIME_P0_REGRESSION_v3.md
- SYSTEM_CONTEXT_PROTOCOL.md
- GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md
- GM_Training/RUNTIME_STATE_TEMPLATE.md
- GM_Training/03_SESSION_LOG_TEMPLATE.md
- GM_Training/08_CLUE_AND_SOURCE_LEDGER.md
- GM_Training/GM_RELIABILITY_AND_EXPERIENCE_CONTROL_PROTOCOL.md
- GM_Training/GM_RUNTIME_P0_INDEPENDENT_EXECUTION_PROMPT.md
- GM_Training/README.md

如 main 在读取期间变化，停止并重新锁定同一提交版本。

## 1. 测试范围与权限

- 执行 v1 RT-01～RT-18 全套。
- 执行 v2 所有 REG 项。
- 执行 v3 REG-16C-PERSIST、REG-16D-PERSIST、REG-13-RISK、REG-12-RAW 三入口、REG-PRIVACY。
- 所有数据使用合成系统与隔离临时目录/仓库。
- 禁止读取、修改正式 Campaign、Module、角色卡、Session Log、Runtime State、Player Notes、CANON。
- 本轮只读仓库。唯一允许新增的文件是最终验收报告：GM_Training/Acceptance_Reports/GM_RUNTIME_P0_THIRD_ROUND_REPORT_YYYY-MM-DD.md。
- 不得修改任何规范、Skill、README 或测试夹具。
- 真实隔离文件读写、进程终止/重启、独立冷读必须分别记录。不能执行时标 SIMULATED / NOT TESTABLE。

## 2. D16 争议持久化硬核验

对 v3 的重复事件与版本/revision 漂移测试，必须实际：
1. 写入 Runtime State 的 persistence.disputes[]；
2. 在 Session Log 追加同 dispute_id 的 INCIDENT/DISPUTE 事件；
3. 保存每一条观察到的冲突记录身份、locator、payload/version/fingerprint、权限字段及原始证据；
4. 写后独立读取两份权威文件，逐字段核验；
5. 终止执行进程，再从磁盘独立冷读；
6. 冷恢复后仍识别 OPEN dispute，阻止 Player Notes 发布和依赖该事件的状态推进；
7. 不删除原始重复行、不覆盖旧版本、不用旧 Fault 当写入指令。

只在模型输出里描述 DISPUTED，或只在同一进程内保留变量，均判 FAIL。

合法修订必须检查 revision_of、revision_id、授权/依据、payload_version/fingerprint。缺失谱系不得自行补造。

## 3. E13 玩家授权闸门

严格执行 v3 REG-13-RISK 的逐轮输入。审计完成后必须先向玩家给出不剧透风险摘要，再等待决定。
分别测试：
- 模糊“继续吧”；
- 明确只继续无关场景；
- 明确授权沿争议线继续。
记录 decision_scope、player_decision、decision_event_id。不能将继续无关场景误读为解除争议，也不能把明确授权误当作事实核验。

## 4. E12 原始证据链

三条入口必须分别执行：
- LIVE_DISCOVERY；
- STRUCTURAL_IMPROVISATION；
- POST_SESSION_AUDIT。

逐项记录原始坏记录、原始错误命题、触发来源、field_path、field_scope、写入前后状态、最早偏离事件、触发审计事件、派生 event/claim IDs、传播边、玩家已见内容和 containment/resolution。缺少原始证据必须标 EVIDENCE_GAP，不得事后补写成原始证据。

## 5. 字段级权限负例

执行 REG-PRIVACY。必须真实生成玩家投影并对最终文本执行秘密字符串扫描。只检查行级 visibility 不够。任何 gm_knowledge/private_notes/gm_adjudication 泄漏均为硬失败。若字段级过滤能力不可用，应拒绝整条混合权限记录导出。

## 6. 报告证据格式

每个测试记录：
1. Initialize：初始隔离文件与哈希；
2. Act：逐轮输入与实际执行；
3. Observe：玩家可见输出及 GM-only 状态；
4. Persist：具体写入目标、路径、内容/字段和工具结果；
5. Readback：独立读回内容与哈希；
6. Recover：独立进程冷读；真实新 Chat 若可用则单独记录；
7. Assert：逐条断言；
8. Evidence：文件路径、哈希、读回片段、调用/故障注入记录。

结果等级：
- PASS：全部硬断言有真实执行证据；
- PARTIAL：主要行为正确，但关键证据/环境能力缺失；
- FAIL：违反任一硬断言；
- NOT TESTABLE：环境不具备该测试能力，写明障碍。

不得把规范已写入等同于行为通过，不得把独立进程冷读等同于真实 ChatGPT 新 Chat 冷恢复。

## 7. 总体判定

- 任一 v1 硬性断言失败，整体 FAIL。
- REG-16C/D 持久化或冷恢复失败，整体 FAIL。
- REG-13 风险摘要/授权范围失败，整体 FAIL。
- REG-PRIVACY 发生 GM-only 泄漏，整体 FAIL。
- REG-12-RAW 缺少原始证据，至少 PARTIAL；伪称完整通过则 FAIL。
- 若只有真实产品新 Chat 或产品级性能遥测不可用，且无硬性行为失败，最多 CONDITIONAL PASS。
- 本轮结果不构成任何正式 Campaign 开团许可。

## 8. 报告归档

创建唯一报告文件：
GM_Training/Acceptance_Reports/GM_RUNTIME_P0_THIRD_ROUND_REPORT_YYYY-MM-DD.md

报告必须包含：
- main HEAD SHA 与每份文件读取版本；
- 测试环境、隔离路径、实际执行能力；
- RT-01～RT-18、v2/v3 所有 REG 的逐项结果；
- D16 两种争议的持久化前后与独立冷读证据；
- E13 风险摘要原文、逐轮授权解释；
- E12 三条入口原始证据与传播链；
- 字段级权限导出字段清单和秘密扫描结果；
- 产品新 Chat 冷恢复、Go Chat 真实多轮、性能遥测的独立状态；
- 未解决缺陷与风险；
- 是否建议进入 P1（不得将 P1 准入等同正式跑团准入）。

只创建报告，不修改其他文件。提交后重新 fetch 报告并核对完整性；若无 GitHub 写权限，提供报告全文并明确未归档。
