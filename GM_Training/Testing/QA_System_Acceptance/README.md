# QA System Acceptance｜QA 系统自身版本验收

> Version: v1
> Scope: 验收 GM Training & Runtime QA、Self Testing Protocol、测试模式路由、判定标准与证据纪律。
> Cadence: 事件触发；不随每次常规测试重复执行。
> Default execution: SINGLE_SESSION_SELF_TEST for the acceptance suite itself; independent execution is required only for test objectives that genuinely depend on separate Chat contexts or real platform behavior.

## 目的

本套件不是 GM 能力测试，也不是日常回归清单。它用于验证“负责测试 GM 的 QA 系统”是否仍能正确执行、分类、审核和报告测试。

它重点检查：
- 自动化测试是否按规定执行；
- 同会话与独立干净会话是否被正确选择；
- PASS、FAIL、PARTIAL、BLOCKED、NOT TESTABLE 是否被正确区分；
- 硬性失败是否会被优秀文笔或高体验分数掩盖；
- 同会话证据是否被错误提升为独立/真实运行证据；
- 测试成本是否与风险相称。

## 何时运行

只在以下情况启动版本级验收：
- QA 架构、硬门槛、证据等级或测试状态语义发生实质变化；
- SELF_TESTING_PROTOCOL 的执行流程或模式路由发生实质变化；
- Oracle/审核机制的通用结构发生变化；
- 更换模型、工具链或运行方式，可能实质影响执行/审核可靠性；
- 出现系统性漏检、误判、证据越界或过度测试；
- 用户明确要求。

普通 Skill 修改、单个夹具的局部更新、日常训练与常规回归不触发本套件。

## 文件

- [START.md](./START.md)：版本验收启动协议。
- [CASES.md](./CASES.md)：提供给被测 QA 的挑战样本；执行阶段不得提前读取 Oracle。
- [ORACLE.md](./ORACLE.md)：预期分类、硬性判据与版本验收门槛；只在所有案例完成后读取。

## 执行边界

1. 锁定 QA 相关文件的 Git commit 与 Blob SHA。
2. 本套件本身默认以同会话方式执行：逐项处理 CASES，先给出结论，再读取 ORACLE 对照。
3. 该过程是 QA 系统的版本校准自测，不是独立盲审；若需要独立确认，再按用户授权建立干净会话执行。
4. 本套件不能证明隐藏平台内部机制，也不能替代真实多轮平台测试或真实玩家 Session。
5. 本套件通过后，日常测试不再重复运行；只有触发条件成立才重验。

## 公开仓库与盲测限制

本仓库公开，因此本套件的 CASES/ORACLE 是可审计的公开校准材料，不是保密 Canary，也不能单独构成盲测。执行阶段仍不得主动向目标提供 ORACLE。若未来需要真正隐藏的盲测样本，必须将 Oracle/Canary 放在受控私有位置；不得把公开仓库中的答案称为秘密。

## 与仓库代码测试的区别

`tests/` 和 GitHub Actions 验证确定性的代码/仓库约束；本套件验证模型驱动的测试协议、执行模式和质量判定。两者互补，不互相替代。

## 验收状态

- `ACCEPTED`
- `ACCEPTED_WITH_LIMITATIONS`
- `REVISE`
- `REJECTED`

具体定义见 [QA 治理规范 §12](../../QUALITY_ASSURANCE_AND_NARRATIVE_RUNTIME_QA.md)。
