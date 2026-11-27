# QA System Acceptance v1｜START

> Test ID: QA-SYS-ACCEPTANCE-v1
> Type: QA framework version acceptance / SINGLE_SESSION_SELF_TEST
> Status: TEST_ONLY_NON_CANON
> Target: Training & Runtime QA + Self Testing Protocol as a testing system, not the GM narrative skill itself.

## 1. 固定范围

被测对象：
- `GM_Training/QUALITY_ASSURANCE_AND_NARRATIVE_RUNTIME_QA.md`
- `GM_Training/SELF_TESTING_PROTOCOL.md`
- `GM_Training/Testing/README.md`
- `GM_Training/Testing/QA_System_Acceptance/`

同时参考：
- `GM_Training/NARRATIVE_QUALITY_BASELINE.md`
- `GM_Training/04_EVALUATION_FRAMEWORK.md`
- `GM_Training/Training_Logs/OPEN_TRAINING_BACKLOG.md`
- `tests/README.md`

执行时记录：
- Repository: `zzhhaannggddii22-hash/Trpg-gm-workbench`
- 被测 commit SHA；
- 上述文件的实际 ref 与 Blob SHA；
- 测试执行方式和审核方式。

不得把历史报告中的旧基线 SHA 当作当前被测版本。不得省略实际未读取的文件。

## 2. 角色与信息边界

你是被测 QA 系统的执行者。逐项处理 CASES.md 中的挑战记录，针对每项给出：
- 测试目标；
- 是否可在同会话有效验证；
- 推荐执行模式；
- 执行有效性状态；
- 测试结果状态；
- 硬门槛结果；
- 证据等级及边界；
- 需要的后续动作。

本轮是 QA 体系的同会话版本校准自测。不得声称这是独立盲审或真实目标 Chat 测试。

**执行阶段不得读取 ORACLE.md。** 只有全部案例完成并冻结结论后，才可读取 ORACLE 对照。

## 3. 执行纪律

1. 逐项读取 CASES.md 的案例，不跳过、不合并。
2. 先判断执行模式，再判断测试结果；不可因“测试重要”而自动升级独立会话。
3. 依赖缺失、版本不符或无法读取时，标 BLOCKED / NOT TESTABLE，不补造。
4. 先检查硬门槛，再评估交互/表现质量；硬失败不可补偿。
5. 区分案例自身的测试结果与 QA 系统版本验收结果。
6. 未覆盖维度标 N/A / UNKNOWN，不推定 PASS。
7. 全部案例完成后，读取 ORACLE.md 进行对照，列出命中、偏差、误判与修订建议。

## 4. 总体验收判定

使用 QA 系统验收状态：
- ACCEPTED
- ACCEPTED_WITH_LIMITATIONS
- REVISE
- REJECTED

若任一关键硬门槛样本被错误放行、缺失依赖仍被评分、同会话结果被冒充独立证据，或跨会话目标被错误判为同会话已验证，则不得 ACCEPTED。

## 5. 输出报告

报告至少记录：
- 被测 commit 与文件 SHA；
- 每个 QA-SYS 案例的模式路由、状态分类与理由；
- 与 Oracle 的逐项对照；
- 误报、漏报和未覆盖项；
- 对性能/执行成本的观察；
- QA 系统验收状态及限制；
- 是否需要更新 QA 规范、Self Testing Protocol、夹具或 Backlog。

报告只记录本次真实执行。未执行的独立会话部分必须保留 NOT TESTED / NOT TESTABLE。
