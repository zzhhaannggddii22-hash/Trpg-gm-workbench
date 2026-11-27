# PR #67｜独立审查修订执行记录

> 日期：2026-11-27
> 范围：PR #67 的独立审查 CF/MF/P 项修订跟踪
> 状态：DOCUMENTATION / CONTRACT REMEDIATION COMPLETE；BEHAVIORAL ACCEPTANCE PENDING
> 本记录不构成生产 Runtime 验收。

## 用户确认的执行口径

1. Weather Events：Zarek Campaign 按用户确认新增 Q06：只有特别极端且与当前任务相关的天气才执行 Weather Events 掷骰程序；普通天气不掷。此为 Campaign-scoped ruling，不改写 v22 默认程序。触发后严格遵循 v22：若结果使 Loose Ends 变化，立即更新 Campaign 状态并重新计算剩余天气骰次数；不回滚或重做已提交的 Starting Chaos。
2. Loose Ends：当前数值属于 Campaign 动态状态，不属于任何系统规则层。Campaign 交接文件 §“Campaign 分部 Loose Ends 权威状态”拥有当前值（当前 1）；Module Ledger 仅记录历史快照和模组增量；Systems 只保留规则表和执行方法。
3. Chaos Pool：旧任务结团时清零并关闭；新任务建立时创建独立 Pool，先初始化为 0，再按当前 Campaign Loose Ends 查表发放 Starting Chaos。旧任务清零与新任务 grant 是不同任务 ID、不同事件。

## P0 修订状态

| Finding | 修订 | 剩余验收 |
|---|---|---|
| CF-01 Weather Events feedback | 新增 Zarek Q06：仅特别极端且与任务相关的天气触发天气骰；触发后若 Loose Ends 改变，按 v22 重新计算剩余天气骰数，不重做 Starting Chaos；新增 R-17/R-18/R-25 | 独立行为执行待完成 |
| CF-02 generation handoff | 明确 roll adapter 提交 base_delta；Chaos Runtime 唯一应用系统修正并提交 final_delta；保留修正快照、提交状态和语义来源身份 | 独立生成/重放行为测试待完成 |
| CF-03 66/77 lifecycle | 补齐 66 当前任务结束强制退休、分部 Loose Ends -11，以及每名使用职能退休选项的特工额外 -11；77 进入 W7 指向的 Unraveling / Branch removal；特殊档位不转成 0 | 阈值回落是否取消退休仍保留 PENDING；R-19/R-20 待执行 |
| CF-04 transaction recovery | 要求复用 Runtime Control / Module Closeout 字段级提交机制；资源、世界状态、可见性、呈现、持久化分别记录，恢复只补未完成字段 | 当前宿主故障注入与跨 Session 持久化仍未验证 |
| CF-05 activation gate | Chaos Protocol 保持 DRAFT / PENDING BEHAVIORAL VALIDATION；输入与 GM-only Oracle 分离；增加 R-01–R-24 | 独立盲测、真实多轮、宿主集成尚未执行；不得宣称生产启用 |

## P1 修订状态

| Finding | 修订 |
|---|---|
| MF-01 Campaign data in Systems | 已移除系统协议中的 Zarek 当前 Loose Ends 输入；当前值位于 Campaign handoff |
| MF-02 Domain cost 3 repeatability | 免费 ≤3 来自规则处理；重复使用作为 Zarek Campaign Q01 桌裁，不再作为跨 Campaign 通用默认 |
| MF-03 UNKNOWN balance overblocking | UNKNOWN 仅阻塞依赖余额的操作；免费 Domain 效果、无资源行为和独立被动规则继续；已知增量可记录但不伪造绝对余额 |
| MF-04 UNKNOWN closeout | 未知的结团前余额与 discarded amount 保留 UNKNOWN；关闭后的旧 Pool 状态可确定为 0；新任务另建 Pool |
| MF-05 semantic duplicate events | 要求事件 ID 绑定原始行动/骰子/世界事件、任务 ID、触发与裁决状态；恢复时先匹配来源事件 |
| MF-06 mechanism registry | 通用契约新增 NOT_APPLICABLE / DISABLED / ENABLED / UNKNOWN / PENDING 状态语义 |
| MF-07 persistent world effects | 要求写入受影响实体和字段，并记录各字段提交状态；不以叙事文字代替状态变化 |
| P1-08 / P1-09 | 新增无资源系统及异构系统测试输入；将 target inputs 与 GM-only Oracle 分离 | 真实第二系统接入与独立盲测仍待执行 |

## P2 / P3 状态

- P2-01 / P2-05：沿用既有常规规则调用路由与触发式运行路径；本次未增加逐消息轮询。
- P2-02 / P2-03：沿用 Session 绑定、规则版本和静态资料复用；规则页码继续同时保留印刷页与 PDF 物理页。
- P2-04：没有可用的同宿主 Base/Head 延迟与 Token 对照数据，未声称性能提升；普通行动验收目标保留为零新增 Chaos 专项检索、状态读取、余额轮询和无意义写入。
- P3：自动化宿主、跨 Session 故障注入和多系统真实集成基础设施尚未建立；不在本 PR 通过文档声称已完成。

## 测试资产与执行状态

- `06_CHAOS_RUNTIME_REGRESSION_v1.md`：GM-only Oracle。
- `10_CHAOS_RUNTIME_TEST_INPUTS_v1.md`：提供给被测 GM 的无 Oracle 输入。
- C-01–C-19：历史单会话推演结果不能自动继承为新协议的 PASS，必须重跑。
- R-01–R-25：已定义，全部 NOT EXECUTED；新增 R-25 专门验证 Zarek Q06 的普通天气不触发天气骰。
- 仓库回归套件与 Roll Runtime adapter harness 可以由 PR validation 执行；它们不等于 Chaos 多轮行为验收。

## CI 记录

- PR validation #329：在较早修订 Head 上 PASS。
- PR validation #345：repository regression suite 16/16 PASS，Roll Runtime adapter harness 12/12 PASS；`git diff --check` 因 Oracle fixture 第 41 行尾随空格失败。
- 尾随空格已在后续提交中修复；修复后最新 Head 尚未获得新的 workflow 结果，因此不得把 #345 标为最新 Head PASS。

## 当前限制

- 66 阈值已按 v22 明确退休与 Loose Ends 减少；阈值回落是否取消已触发退休，规则未明确，仍保留 PENDING。
- 真实宿主是否自动发现触发、跨 Session 保存效果、部分提交恢复和实际响应延迟仍 NOT VERIFIED。
- 本记录只追踪协议修订，不回写历史 Session，不补造 Bower Street Chaos 消费或效果，不改变正式战役 CANON。
- PR #67 保持 OPEN / NOT MERGED，等待独立复审与行为验收。