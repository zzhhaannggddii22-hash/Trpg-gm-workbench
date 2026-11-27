# QA System Acceptance v1｜初始版本校准报告｜2026-11-27

> Test ID: QA-SYS-ACCEPTANCE-v1
> Tested QA revision: branch `qa/qa-system-acceptance-foundation-2026-11-27`（本报告写入前 head：`394aa5523cf9f6761b59939321528054ba4ffdb1`）
> Base Workbench main: `99f41bd4dafd202c9d81430e4ca098356d8e3cc7`
> Execution: 同会话开放上下文校准；非独立盲测
> QA system acceptance: **ACCEPTED_WITH_LIMITATIONS**

## 1. 验收对象

版本登记：本次验收内容随后正式登记为 QA 治理规范 v0.2 与 Self Testing Protocol v1.3。版本号/状态头更新发生在挑战执行之后，不改变本轮已验收的模式路由、硬门槛或证据规则。

- `GM_Training/QUALITY_ASSURANCE_AND_NARRATIVE_RUNTIME_QA.md`
- `GM_Training/SELF_TESTING_PROTOCOL.md`
- `GM_Training/Testing/QA_System_Acceptance/`
- `GM_Training/Testing/Baselines/NARRATIVE_QUALITY_BASELINE_EXECUTION_PROMPT.md`
- G-16 低压/高压夹具的执行模式声明
- `tests/README.md` 中代码测试与模型行为测试的边界

## 2. 挑战案例结果

| Case | 本轮判定 | 是否符合 Oracle | 说明 |
|---|---|---|---|
| QA-SYS-01 常规可自动化回归 | A / RUN_COMPLETE_SINGLE_SESSION / 样本 PASS | PASS | 同会话自动化应为默认；证据明确标为合成自测。 |
| QA-SYS-02 优秀表现掩盖信息泄露 | FAIL | PASS | NPC 未说出口的私人记忆进入玩家旁白属于硬失败，不允许其他维度补偿。 |
| QA-SYS-03 关键规则依赖缺失 | BLOCKED | PASS | 旧摘要不能代替指定 ref 下的规则原文；受影响裁定不得凭经验评分。 |
| QA-SYS-04 分支隔离不可核验 | PARTIAL / UNKNOWN | PASS | 分支输出可分别记录，但整套隔离结论不得 PASS。 |
| QA-SYS-05 跨 Chat 记忆隔离 | A 模式 NOT TESTABLE；要求 B | PASS | 必须使用干净目标 Chat；没有回传原始结果时不声称通过。 |
| QA-SYS-06 普通局部 Skill 修订 | A 定向回归；不启动 QA 自身验收 | PASS | 只运行受影响的 NQB/综合样本，不做全量回归。 |
| QA-SYS-07 行动序列不完整 | PARTIAL | PASS | 未执行的 ACTION 不能计入完成或通过。 |
| QA-SYS-08 NQB 快速回归与正式玩家校准 | A 用于常规合成回归；B 用于干净环境合成抽检；C 用于真实玩家逐轮 | PASS | A/B 均不能冒充真实玩家回合；C 不属于自动化模式。 |

本轮是开放上下文自校准：挑战案例和 Oracle 由同一工作会话准备，执行与对照并非盲审。初始八项分类后，扩充 QA-SYS-09 检查审核标准是否污染目标 Chat，并扩充 QA-SYS-10 检查版本锁定；随后重新核对十项分类。此轮发现 NQB 执行提示把 Review Checklist 列为目标 GM 必读资料，随后已修正为审核者专用。结果证明当前 QA 规范能够形成一致、正确的分类，不证明独立审核者也会得到相同结果。

## 3. QA 标准审计发现及已处理事项

### 3.1 自动化模式定义不一致

原 NQB 执行提示将“真实玩家逐回合验证”定义为模式 B，与用户要求的第二种自动化模式不一致。

已修订为：
- A：同会话自动化，默认；
- B：干净目标 Chat 自动化，完成后回传原始结果给独立审核会话；
- C：真实玩家逐轮互动，作为非自动化补充证据。

并明确 NQB §6 的真实玩家回合要求只由 C 满足，A/B 都是合成证据。

### 3.2 测试资料迁移后的版本与路径

原 NQB 执行提示指向历史训练分支且没有要求固定精确 commit；同时其场景资料路径与当前 Testing 目录迁移后的权威路径不一致。

已修订为：
- 固定 `main` 作为基线 ref；
- 执行前必须填入精确 Workbench commit SHA；
- GM Packet、Player Prompt、Review Checklist 使用 `Testing/Baselines/` 当前路径。

### 3.5 精确版本锁定与历史夹具

模式路由盘点发现，L3 NPC 与 Narrative Runtime 单会话伴随夹具虽然适用 A 模式，但当前固定在旧 Workbench commit `83981a5f2a42d40170603804fc6995da21daaf61`。它们可验证该历史版本，不能作为当前 main 的回归结果。NQB 执行提示已改为 main + 执行前填入精确 commit SHA；G-16 START 的 commit 占位符也必须在执行前填好。不得只记录分支名，也不得静默替换历史 ref。

### 3.4 目标执行与审核标准隔离

初始审计发现 NQB 执行提示把 Review Checklist 列为所有执行模式的必读资料，与 B 模式“目标 Chat 不接触评分标准、审核者在收到结果后再读”的要求冲突。该问题可能污染目标 GM 的行为，削弱独立审核证据。进一步检查还发现，若目标 GM 在模式 B/C 中自行输出评分/自评，会把目标自评混入独立审核记录。

已修订：目标执行阶段只读取基准、GM Packet 和 Player Prompt；Review Checklist 由模式 A 在执行结束后自审，或由模式 B/C 的独立审核者在收到完整原始结果后读取。B/C 目标只交付原始行动/回应、必要状态账本、版本和读取证据，不自行评分或自评。Self Testing Protocol §11.2 同步明确目标 Chat 不得接触 Review Checklist / ORACLE，也不得自评。

### 3.3 夹具模式路由

已建立初步模式路由表：

| 测试 | 当前建议 |
|---|---|
| L3 NPC 单会话合成伴随夹具 | A |
| Narrative Runtime 单会话综合伴随夹具 | A |
| G-16 高压信息通道 | B（当前 README 要求空白 Chat，并回传独立审核） |
| G-16 低压分支回归 | A 检查各分支输出；B 可提供独立审核 |
| H1-3 跨会话知识泄露 v1/v2 | B 必须 |
| P1-0C 目标环境复测 | B 必须 |
| T0 自然语言盲测套件 | B 专项 |
| NQB-01 | A 常规合成回归；B 干净环境合成抽检；C 真实玩家校准 |
| Context Assembly / Trace | 按子项分流；真实目标工具读写与独立读回需 B |
| `tests/` + GitHub Actions | 独立的代码/仓库层 CI，不属于 A/B 模型行为测试 |

G-16 低压夹具已明确：同一回复中的 A/B/C 分支输出符合 Oracle，不足以证明跨分支重置隔离。历史总体 PARTIAL 保留。

## 4. 同会话自动化实测

本轮另执行 NQB-01 v0.2《雨停之前》8 轮合成自动化样本，报告见 [NQB-01 同会话自动化抽检报告](./NQB01_SAME_SESSION_AUTOMATED_RUN_2026-11-27.md)。

结果：
- 执行完成：8 轮；
- 基础正确性：PASS；
- 交互质量：各维度达到 3 分；
- 叙事表现：感官环境、对话自然度、情绪可读性、氛围发现感低于 3 分；
- 样本总评：PARTIAL；
- 发现服务价格/收费信息的无依据补充与回答含糊，作为修订反馈。

这证明 A 模式能在当前会话中完成一项真实的固定基准执行并暴露质量短板；它不证明独立审核或跨会话行为。

## 5. 必须单独保留的非 A 项目

以下目标不应强行用同会话模拟得出通过结论：

1. **H1-3 跨会话知识泄露**：必须由用户/操作者建立真正空白目标 Chat；Canary 保存在目标 Chat 外。
2. **P1-0C 目标环境复测**：必须观察目标 Chat 实际工具调用、文件写入、独立读回和真实状态恢复。
3. **T0 自然语言盲测**：需要多个独立目标 Chat、逐轮自然语言输入和操作者侧 Oracle。
4. **G-16 高压信息通道**：当前夹具声明要求空白目标 Chat；结果应回传独立审核。
5. **G-16 低压同会话分支重置隔离**：A 可检查各分支输出，B 可对原始输出做独立审核；但当前一条回复的夹具没有外部可观察的重置机制，A/B 都不能证明同一 Chat 内部的分支隔离。若该目标必须验收，需要新夹具或外部状态注入/读回机制。
6. **Context Assembly / Trace 的真实副作用项**：若验收目标是目标 Chat 的真实读写和独立读回，必须在目标环境验证。
7. **NQB-01 真实玩家校准**：需要模式 C 的真实玩家逐轮互动；不是自动化测试。

A 模式仍是绝大多数常规测试的默认方式。以上项目只是目标本身依赖独立环境或真实交互的专项例外。

## 6. 尚未完成的验证

- B 模式的完整端到端执行尚未在本轮实际运行：尚无用户新建目标 Chat、自动化执行、回传完整原始输出和独立审核的证据。
- C 模式真实玩家校准未执行。
- 仓库 Python/Node 回归套件已由 PR GitHub Actions 实际运行：12 项单元测试 PASS；Markdown 导航扫描 387 个文件、522 条本地链接，0 broken paths、0 candidate anchors；`git diff --check` PASS。
- 首次 CI 曾因 NQB 执行提示尾随空格和 Oracle 文件末尾多余空行失败；修复后重新触发，最终通过。这说明代码/仓库层测试能捕获并反馈真实格式缺陷。
- NQB-01 只运行一条行动序列；稳定性仍未验证。
- 公开仓库中的 ORACLE 不是秘密 Canary。若需要真正盲测，必须把隐藏 Oracle/Canary 保存在受控私有位置。

## 7. 结论与后续

**ACCEPTED_WITH_LIMITATIONS**：当前 QA 规范的默认模式、独立模式触发条件、硬门槛、证据边界和常规测试成本控制已经形成一致基线；挑战案例分类无关键偏差。限制在于 B 模式实际端到端执行、真实玩家 C 模式和代码 CI 尚未完成。

后续维护：
- 日常测试不重复执行本套 QA 自身验收；
- 普通 Skill/夹具变更按影响范围跑最小充分 A 模式回归；
- 只有 QA 架构、标准、执行协议实质变化或出现系统性误判时，才重跑 QA System Acceptance；
- 需要 B 模式时，用户创建干净目标 Chat 并回传完整结果，独立审核者再对照 Oracle；
- 不改变 G-16、P1-0C、NQB T3/T4 等历史状态，不用本报告替代专项验收。
