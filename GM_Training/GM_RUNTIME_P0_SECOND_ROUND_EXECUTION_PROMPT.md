# GM Runtime P0 第二轮独立复测提示词

你是独立的高级模型验收员。请在本轮重新读取 GitHub 当前 main，对 P0 修复进行独立复测。不得使用上一轮模型的结论替代证据，也不得因为本轮新增了规范就默认行为已经正确。

## 0. 测试目标与版本

仓库：`zzhhaannggddii22-hash/triangle-agency-gm-workbench`

先读取当前 main HEAD commit SHA。然后读取：
- `GM_Training/Acceptance_Test_Fixtures/GM_RUNTIME_P0_FIXTURE_v1.md`
- `GM_Training/Acceptance_Test_Fixtures/GM_RUNTIME_P0_REGRESSION_v2.md`
- `SYSTEM_CONTEXT_PROTOCOL.md`
- `GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md`
- `GM_Training/RUNTIME_STATE_TEMPLATE.md`
- `GM_Training/03_SESSION_LOG_TEMPLATE.md`
- `GM_Training/08_CLUE_AND_SOURCE_LEDGER.md`
- `GM_Training/GM_RELIABILITY_AND_EXPERIENCE_CONTROL_PROTOCOL.md`
- `GM_Training/GM_RUNTIME_P0_INDEPENDENT_EXECUTION_PROMPT.md`
- `GM_Training/README.md`

记录每个文件实际读取的版本/提交；若主分支在读取期间变化，停止并重新锁定测试版本。

## 1. 独立性、隔离与写入权限

- 你必须独立执行 v1 的 RT-01～RT-18 全套测试，以及 v2 的 REG-01、REG-02、REG-16A～G、REG-18、REG-11～14、REG-17、REG-03。
- 不向原设计者询问预期答案；先按输入与现行规范执行，再对照夹具断言。
- 所有测试使用独立合成状态空间。禁止读取或修改任何正式 Campaign、Module、Session Log、Runtime State、Player Notes、人物卡或战役 CANON。
- 本轮仓库只读。唯一允许新增的是最终报告文件：`GM_Training/Acceptance_Reports/GM_RUNTIME_P0_SECOND_ROUND_REPORT_YYYY-MM-DD.md`。不得修改规范、Skill、夹具或其他文件。
- 如果真实隔离文件写入能力不可用，可在本地临时目录执行；必须记录实际读写与读回证据。只能模拟时必须标 SIMULATED。
- 不得把同一对话中的上下文延续称为独立新 Chat 冷恢复。

## 2. 第一轮缺陷的专项复测

### D01 / RT-01
验证是否识别 Resolve 属于 `iron_dice 3.2`，同时保持当前桌 `ember_protocol 0.9.4` 锁定。只识别归属不代表加载规则。记录术语归属来源；若无可用索引，明确标缺口，不得猜。

### D02 / RT-02
验证是否保留死亡规则 UNKNOWN，并记录当前 system_id、ruleset_version、具体缺口主题、已检索权威来源与检索结果。区分“当前夹具未提供完整规则书”与“完整规则书检索后仍无条文”。

### D16 / RT-16
必须执行 REG-16A～G 全矩阵。核心硬断言：
- 旧 Fault 记录不是恢复写入的权威指令；
- 当前 Session Log 必须与原始 PREPARE 批次逐事件核对；
- 不能只核对条数、batch_id 或旧 event_id；
- 错 event_id、重复行、版本漂移、revision 不一致、recipient_scope/visibility 不一致均不得 PUBLISHED；
- 只有身份与内容完全匹配的单纯缺失投影可以定向补写；
- 逐目标读回通过后才能 PUBLISHED。
报告必须列出每个目标的实际读回值及 VERIFIED / MISSING / MISMATCH / DISPUTED 状态。

### D18 / RT-18
验证模糊“继续”被拒绝后，明确说明需要用户授权创建新运行/Session；明确新运行授权不等于奖励结算授权。旧 CLOSED 分支必须保持不变。

## 3. PARTIAL 补测

- E11 / REG-11：逐轮输入，不能一次性喂入完整错误前史。
- E12 / REG-12：保存原始坏记录、触发记录、最早偏离事件和传播链。
- E13 / REG-13：审计完成前尝试继续必须拒绝；审计后仍需玩家明确决定。
- E14 / REG-14：区分同对话重载、独立进程重载、无历史新 Chat 读取权威文件。
- E17 / REG-17：在新会话条件下恢复冲突状态；环境不支持则 NOT TESTABLE。
- REG-03：验证 last_presented_event_id / last_answered_event_id / checkpoint.last_event_id 的语义与递进。

PARTIAL 补测是为了区分功能缺陷与证据缺口；不得为追求 PASS 把不可测试项降格为通过。

## 4. 执行与证据格式

每项测试依次记录：
1. Initialize：初始状态与隔离空间；
2. Act：逐轮实际输入；
3. Observe：玩家可见输出与 GM-only 状态；
4. Persist：写入了哪些文件/记录，或明确 SIMULATED；
5. Recover：从何种介质/进程/会话重新读取；
6. Assert：逐条断言结果；
7. Evidence：路径、文件哈希/版本、读回片段、调用记录或其他可复核证据。

结果等级：PASS / PARTIAL / FAIL / NOT TESTABLE。
- PASS：所有相关硬断言均有实际执行证据。
- PARTIAL：主要行为正确，但缺少必要执行或读回证据。
- FAIL：违反硬断言。
- NOT TESTABLE：环境确实不具备执行条件，说明具体障碍。

总体判定：
- FAIL：任一硬性断言失败，包括错误投影被发布、GM-only 泄漏、错误续接、重复结算、规则串台。
- CONDITIONAL PASS：无硬性行为失败，但真实工具写入/无历史新 Chat 冷恢复/产品级遥测有 NOT TESTABLE。
- PASS：全部测试通过，且真实工具持久化与独立冷恢复证据达到夹具要求。

## 5. 报告与提交

报告必须保存至：
`GM_Training/Acceptance_Reports/GM_RUNTIME_P0_SECOND_ROUND_REPORT_YYYY-MM-DD.md`

至少包含：
1. 日期、模型/环境（可确认时）、main HEAD SHA、测试范围与限制；
2. 总判定与判定理由；
3. RT-01～RT-18 与所有 REG 测试逐项结果；
4. D01、D02、D16、D18 缺陷关闭状态及证据；
5. E11、E12、E13、E14、E17 的补测结果；
6. REG-16 每个子测试的逐目标读回矩阵；
7. 硬性断言总表；
8. 性能指标：只能报告真实可观测值，其他标 UNKNOWN / NOT TESTABLE；
9. 剩余缺陷、风险与修复建议；
10. 是否建议进入 P1 基准测试；不得把本轮结果视为正式 Campaign 开团许可。

只创建报告，不修改其他文件。提交后重新 fetch 报告，核对完整性。若没有 GitHub 写权限，提供完整报告文本并说明未归档；不得声称已提交。
