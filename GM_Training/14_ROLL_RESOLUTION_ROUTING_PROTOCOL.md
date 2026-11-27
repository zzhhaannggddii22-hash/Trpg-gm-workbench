# 通用掷骰调用与执行路由协议

> 跨系统执行框架；不定义任何系统的骰型、检定触发、成功条件、资源或结算公式。
> 权威架构：`SYSTEM_CONTEXT_PROTOCOL.md`。运行依赖：`GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md`。
> 状态：DESIGN / 自测中；未启用为主 Skill 强制入口。

## 1. 职责

本协议只负责：核验当前 Campaign 系统绑定；区分玩家提问、行动意图、已承诺行动和系统规定的掷骰发起权；把机制路由到当前系统专属索引与完整原文；保留玩家选择；将结果交给现有 Runtime 的事件、资源和玩家投影流程。

本协议不建立第二套规则库、状态账本、事件日志、资源流水或 Manifest。它不得规定所有系统的骰型、骰数、成功阈值、修正、行动经济、资源或结果等级；不得把任何系统的机制复制进通用 Skill；不得跨系统填补规则缺口。

## 2. 调用顺序

1. **Resolve Binding**：按 `SYSTEM_CONTEXT_PROTOCOL.md` 核验唯一 `system_id`、精确规则版本（按当前 Binding schema 的实际字段读取，例如 Zarek 使用 `rules.edition`，不得假定字段名统一）、Campaign Binding、系统登记与精确 `system_entry`。缺失、冲突、candidate 或路径不符时阻断依赖该系统规则的行动，不默认回退。
2. **Classify Player Input**：遵循 Runtime §14.15，区分 `PLAYER_QUESTION_TO_GM`、`PLAYER_INTENT`、`PC_DECLARED_SPEECH`、`PC_ACTION_COMMITTED`。询问可行性不等于承诺执行。
3. **Determine Roll Initiation**：只按当前系统原文确认谁有权发起掷骰、触发条件和是否需要掷骰。通用协议不授予 GM 新的发起权。
4. **Route Mechanic**：使用当前系统入口的导航/索引定位候选机制；索引只定位，不替代原文。不得加载其他系统机制来补足缺口。
5. **Verify Authority**：读取完整适用原文，并核对当前 Campaign 桌规/适配清单。桌规须匹配 system、版本、Campaign、Module、触发条件和批准依据。
6. **Resolve Preconditions**：资格、能力解锁、触发/代价、属性/Quality、骰型、修正、结果和后果均由系统专属协议定义。
7. **Explain Choices**：掷骰前说明玩家需要知道的流程、风险、成本与保留给玩家的选择，不泄露 GM-only 信息。
8. **Execute Roll**：用户偏好是默认由助手执行，除非用户明确说自己掷骰；但执行者与发起者是不同维度。用户选择自掷时记录为玩家报告，不伪装成工具随机结果。
9. **Resolve System-Specific Result**：按专属协议处理原始骰面、特殊触发、修改、玩家选择、资源、结果与后果。通用层不重算。
10. **Commit Through Existing Runtime**：沿用 Runtime 稳定事件和当前模组 Resource Ledger。Session Log 引用 Entry ID；Runtime State 不复制资源余额；正式人物卡按 Session 边界对账更新。跨文件持久化证明按 Runtime §14.14，不另建骰子账本。
11. **Project and Respond**：按 Runtime §14.19 先形成唯一 `player_reply_payload`。叙事、状态栏、骰子 UI、回顾和 Player Notes 均从同一份获准投影生成。UI 只渲染，不裁定、不掷骰、不修改资源。
12. **Recover**：重试先核对同一稳定事件的已完成结果和同桌后续变化；不得重掷或重复应用资源。跨文件/持久化应用按 Runtime §14.14 核对字段级 manifest。

## 3. 发起权与执行者

- `roll_initiator` 由当前系统规则决定。
- `roll_executor` 默认助手，除非用户明确说自己掷骰。
- 助手代掷不代表可以替玩家决定是否采用方案、花费资源、选择骰位或接受结果。
- 不得把 GM 代掷误称为玩家发起，也不得把模型生成数字伪称为外部随机源。
- 优先使用当前环境可调用、可说明的工具级 CSPRNG，并记录为对应工具来源。若当前环境没有可用工具级随机源，仍按用户已设定的默认偏好由助手掷骰，明确标记 `MODEL_GENERATED` 并披露其可审计性限制；不得伪称外部随机源。用户明确说自己掷骰时才改为玩家报告骰面。

## 4. 系统专属路由契约

每个已登记系统在 `Systems/<system_id>/` 维护专属入口、规则索引、检阅协议与系统专属执行说明。通用层只调用该入口，不复制规则正文。

专属入口应说明实际掷骰机制、无骰行动、掷骰发起权、原文版本定位、资格/成本/修正/结果依赖、Campaign 桌规入口及未核验分支。索引未命中、原文不可读或版本不符时标记 `MAP_GAP` / `RULE_SOURCE_NOT_VERIFIED`；未核验专属能力标记系统规定的暂缓状态。不得用 D20、6d4 或其他系统机制作为通用回退。

## 5. 资源与投影

资源变化按 Runtime §3/§4 在同一轮完成流水、余额和玩家可见说明；前值未知时记录已确认增量，当前值保持 PENDING。Resource Ledger 是 Session 内资源交易权威；Session Log 引用 Entry ID；Runtime State 不复制余额。Entry ID、event_id 或 batch_id 本身不单独证明持久化字段已应用。重试不重复扣费/奖励。

Dice UI 只接收 Runtime §14.19 生成的 `player_reply_payload`，不得接收 GM-only 内容、内部事件/Session 编号、Ledger Entry ID、Manifest 或审计标签。UI 与文本回退共用同一份投影。

## 6. 状态

- `BLOCKED_BINDING`：绑定缺失/冲突/未激活。
- `NO_ROLL`：当前系统专属流程确认不需要掷骰，或该机制的触发条件尚未满足。玩家提问/未承诺意图不自动变成行动；但不得排除某系统明确允许的自动或 GM 发起触发。
- `ROUTE_FOUND`：已找到当前系统候选机制。
- `RULE_SOURCE_NOT_VERIFIED`：完整原文或版本未核验。
- `MAP_GAP`：当前系统索引缺失或机制不明。
- `UNSUPPORTED_PENDING_RULE_REVIEW`：专属能力/解锁/覆盖未核验。
- `ROLL_READY`：规则和资格核验通过，且当前系统规定的发起条件已满足；发起者可以是玩家、GM 或规则触发。
- `RESOLVED`：桌内规则结果已确定；不表示外部保存已验证。

## 7. 性能与启用门槛

新对话/新 Session 的绑定核验属于既有 Preflight；同一活动对话复用已核验系统锁和静态来源。普通行动不加载其他系统、不扫描全仓。只按当前行动依赖定向读取。

本文件不自动成为正式 Skill 强制入口。启用前需通过系统路由隔离、发起权/执行权、玩家自掷、资源同轮结算、Runtime 恢复和玩家投影测试，并经用户批准。
