# P0/P1 场景上下文与调查记录修复｜实施记录

- 日期：2026-11-25
- 目标基线：`315658d85a4925c3e12dd72d1371915b1b7f120e`
- 实施分支起点：`main` at `4e85fc5f2c1ec4343099326b54d5d930894695db`（该提交包含目标基线及其后一个 Bower Street 模组资料/目录规范提交）
- 实施分支：`fix/p0-p1-scene-context-evidence-integrity-2026-11-25`
- 状态：文档/规范修订已写入分支；目标 Chat 行为回归尚未执行；未合并 main

## 1. 盘点结论

本次盘点确认，目标基线已经具备较完整的底层机制，本轮不应另建平行架构：

- Runtime §13 已区分静态权威事实、Runtime State、Session/Event Log 与玩家可见记录，并定义场景进入状态、续接锚点与错误恢复。
- Runtime §14.2 / §14.20 已定义 Claim、NPC Knowledge、Player Knowledge、权限分区、Context Manifest、READY / READY_WITH_LIMITS / BLOCKED 与局部阻断。
- Source Ledger §9.2、§9.5–9.9 已定义证词呈现锚点、认知获取、主体认知态度、陈述与客观命题分离，以及 NPC Knowledge Projection。
- Workflow §A 已定义新对话 Preflight、健康续接快路径与依赖驱动的 Context Assembly。
- Session Log 模板已要求按实际发生顺序记录行动与信息，但未把访谈追问顺序、提示污染和引文精度写成足够明确的操作要求。
- 现有 Context Assembly 回归夹具覆盖资料缺失、NPC 知识、来源和局部阻断，但没有直接覆盖本轮 H1-4 的“场景已建立、NPC 关键认知缺失时仍应继续普通互动”缺陷，也没有完整覆盖 H2 的访谈提示污染和引文重构问题。

因此，本轮采用最小增量：明确分离场景连续性与 NPC 认知依赖；补充重要访谈的行动顺序、提示上下文和引文精度规则；增加独立回归夹具。没有新增数据库、第二套 Preflight 或每轮审计机制。

## 2. 已实施修改

| 文件 | 修改 |
|---|---|
| `GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md` | 新增 §13.1.1，明确跨会话信息恢复必须回溯有效 Runtime、Session Log 与玩家呈现锚点；新增 §14.20.13，明确场景状态与 NPC Knowledge 是独立依赖，NPC 资料缺失只限制相关事实断言/子行动，不自动阻断 ACTIVE 场景。 |
| `GM_Training/08_CLUE_AND_SOURCE_LEDGER.md` | 新增 §9.10，明确访谈行动顺序、玩家提示造成的来源污染、NPC 陈述与独立佐证的区别，以及直接引语/忠实转述/未核实重构的处理。 |
| `GM_Training/03_SESSION_LOG_TEMPLATE.md` | 增加重要访谈记录提示，要求保留追问顺序；玩家问题无法逐字核实时用间接叙述；NPC 原话必须有逐字记录支持。 |
| `GM_Training/02_WORKFLOW_AND_PREFLIGHT.md` | 在 Preflight 中加入跨会话信息准入边界，并明确活动场景已确认而 NPC Knowledge 缺失时优先 READY_WITH_LIMITS，不将整场 BLOCKED。 |
| `GM_Training/SKILL.md` | 在运行入口加入 §14.20.13 的定向引用，确保现场执行入口可发现该规则。 |
| `GM_Training/Acceptance_Test_Fixtures/SCENE_CONTINUITY_AND_EVIDENCE_RECORD_REGRESSION_v1.md` | 新增 SC-01 至 SC-18 合成回归夹具，覆盖场景连续性、NPC 认知缺口、玩家提示污染、行动顺序与引文精度。 |
| `GM_Training/Acceptance_Test_Fixtures/README.md` | 登记新夹具。 |
| `GM_Training/README.md` | 登记新夹具入口。 |

## 3. 修复后预期行为

### 场景与认知

- Scene State 已确认 ACTIVE、NPC 在场且互动已建立时，NPC Knowledge 单项缺失不使场景失效。
- 普通对话、澄清、倾听和不依赖缺失事实的互动可以继续。
- NPC 可以自然表达不确定或暂时无法回忆，但不得为填补缺口而新增关键目击、个人经历、时间、地点、投诉或报修事实。
- 不把 NOT_LOADED / UNKNOWN 解释为“NPC 从未知道”或“事件没有发生”。
- BLOCKED 只限制真正依赖缺失前提的断言或子行动。

### 证据与访谈记录

- 玩家提示仍是玩家提示；NPC 随后作出的实际回答仍可记录为 NPC_STATEMENT，但在相关情况下标记为受提示影响，不能当作独立佐证。
- 重要访谈保留提问、回答、追问、后续回答与收尾的实际顺序。
- 有逐字来源才使用直接引语；只有摘要或记忆时改用间接引述。
- 不把玩家行动、GM 衔接或整理性概括包装成 NPC 原话。
- 不把后续新披露回填成此前已经获得的证言。

## 4. 验证状态

| 验证层级 | 状态 | 说明 |
|---|---|---|
| 仓库结构与现有规范盘点 | DONE | 已读取目标基线关键架构、运行协议、来源账本、Runtime State、Session Log、Context Assembly 设计与既有夹具 |
| 分支隔离 | DONE | 从当前 main 的后继提交创建独立分支；未修改 main |
| 文档修改写入 | DONE | GitHub 已返回各文件提交 SHA |
| 修改后回读与链接检查 | PASS | 10 个变更文件均已从修复分支重新读取；RT-16 Markdown 检查为 215 个 Markdown 文件、352 个本地链接、0 个缺失路径、0 个锚点候选 |
| 仓库自动化测试 | PASS | GitHub Actions PR validation run `45618724577`：12 项 unittest 全部通过；`git diff --check` 通过；测试 head `8a8335f5ca0397a1afbe5d96a47c279dcb81309c` |
| 目标 Chat 独立回归 | NOT STARTED | SC-01–SC-18 尚未交给独立目标 Chat 执行 |
| 真实跑团综合验证 | NOT STARTED | 不以文档更新代替实际运行证据 |

**不得将本次文档修订报告为运行行为 PASS。** 本次只能确认修复规范和测试材料已经写入分支；目标 Chat 的过度阻断、NPC 认知漂移和记录精度是否改善，仍需独立验证。

## 5. 范围与风险

- 没有修改 Campaign CANON、角色档案、模组内容或系统规则。
- 没有修改 T0 事故处置、跨文件持久化、Context Manifest 或现有 Claim Ledger 的权威归属。
- 没有新增每轮检查、全量读取、NPC 记忆数据库或强制 Benchmark。
- 仓库为公开仓库；夹具中的“操作者侧”是执行纪律，不构成 GitHub 访问控制。执行盲测时不得将预期结果提供给目标 Chat。
- 当前最大剩余风险是：规范已明确但模型现场仍可能过度阻断，或在继续互动时无依据地补造 NPC 过去经历。SC-01–SC-10 专门用于区分这两类相反错误。
