# Triangle Agency Dice UI｜玩家掷骰视图规范

> System: triangle_agency / 中文 v22
> Status: DESIGN ONLY；纯展示契约，不是已部署组件。
> Rule authority: Rule_Reference/02_DICE_RESOLUTION_PROTOCOL.md + 中文 v22 原文。
> Runtime authority: GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md §14.19。

## 1. 组件职责

Dice UI 只把当前玩家可见掷骰结果呈现得清晰、可读、可回顾。它不是规则引擎、随机数生成器、资源账本、Session Log、Runtime State 或发布权限系统。

规则判定、随机骰面、Burnout/QA 计算、玩家选择、资源交易与玩家信息过滤均在 Runtime/系统规则流程完成。UI 不得自行决定成功、Chaos、资源余额或隐藏信息可见性。

## 2. 输入边界

唯一输入为 Runtime §14.19 生成的单份 `player_reply_payload` 中已授权的骰子视图子集。正文、状态栏、UI、Player Notes 和回顾必须从同一份玩家投影生成。

禁止输入：
- GM-only 规则注释、Playwall 未授权内容、NPC 秘密或隐藏事实；
- 内部 roll/event/session ID、Resource Ledger Entry ID、Manifest、批次号、审计标签；
- 角色未解锁能力的隐藏描述或待公开内容。

UI 不承担授权过滤。上游若无法证明玩家投影范围，禁止把资料传入 UI。

## 3. 展示内容

- 标题、机制名称与当前阶段；
- 固定骰位 1–6，原始骰面；
- 每枚骰的逐步修改轨迹（修改类型、前值、后值）；
- 被 Burnout 移除的骰仍保留原始位置；
- 最终有效骰面与成功/失败、Chaos；
- 自然 Triscendence、Stability 等已确认的公开特殊结果；
- 等待玩家选择时，只展示玩家有权选择的选项；
- 资源变化只显示获准公开的资源名、增量、已核验当前值或“当前待核”，不显示任何内部账本引用。

UI 必须区分“原始骰面自然三重升华”与“调整后最终恰好三个 3 的 Stability”；二者不可用同一个图标/文案混淆。

## 4. 视图阶段

- `DECLARED`：规则已确认要掷骰，尚无骰面；不显示假骰面。
- `ROLLED`：已收到原始骰面，尚在规则结算中。
- `AWAITING_PLAYER_CHOICE`：结果已确认，但仍有玩家选择（例如 Triscendence 奖励）；不显示为完全结算。
- `RESOLVED`：桌内规则结果和玩家选择均已完成。
- `PENDING`：受影响字段/依赖待核；只显示允许公开的待核说明，不猜当前值。

`RESOLVED` 不代表外部持久化已经通过 Runtime §14.14 验证。

## 5. 交互与更新

- UI 不掷骰、不修改骰面、不花费 QA、不选择 Triscendence 奖励、不写资源。
- 玩家需要作选择时，选择必须由真实对话/Runtime 行动接收；UI 按新 payload 更新，不直接更改游戏状态。
- 每个接收者视图使用不透明 `view_id` 与递增 `revision`；拒绝旧 revision 覆盖新 revision。相同 revision 不同内容视为冲突。
- 不得让 view_id 编码或可逆推导内部事件/账本 ID。
- 同一 view 重渲染不得创建新检定或重复资源交易。

## 6. 特殊机制与回退

当前单骰池 UI 只支持 Ask the Agency 与已核验、可用单骰池表达的 Anomaly Ability 结果。

Conflict Resolution 是多人多轮独立机制，当前 Schema 不表达该结构；使用文本回退，不压缩成单次骰池。Playwall 未核验能力也不进入已支持 UI 状态。

UI 不可用时，文本回退从同一份 player_reply_payload 生成；UI 故障不能中断跑团或触发重掷。

## 7. 可访问性与验收

实现时须验证：键盘可操作、屏幕阅读器能读出骰位与修改、色彩不是唯一信息编码、减少动态效果设置有效、窄屏布局不丢骰位、资源待核状态不显示旧余额为当前值。

当前仓库没有已部署的 UI 宿主组件；本文件与 Schema 只构成实现契约。

## 8. 上游语义校验

JSON Schema 之外，Runtime 投影器/渲染入口必须执行语义校验：
- 已掷骰阶段必须有 6 个骰位，slot 恰为 1–6 且不重复；不得排序或压缩位置。
- raw_value 必须是 1–4 的整数；current_value 只能来自规则流程已确认的最终状态。
- REMOVED 骰必须保留原始 slot 与 raw_value，且不得参与最终有效骰面。
- 修改轨迹必须按真实发生顺序排列，before/after 与前一状态连续；不能仅凭 UI 输入自行重算。
- revision 单调递增；拒绝旧 revision，同 revision 内容冲突时拒绝覆盖。
- 对 PLAYER 投影之外的字段一律拒收；Schema 不承担上游授权替代品的职责。
