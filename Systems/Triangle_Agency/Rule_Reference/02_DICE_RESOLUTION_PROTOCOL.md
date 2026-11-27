# Triangle Agency｜掷骰与结果结算专属协议

> system_id: triangle_agency；ruleset_version: 中文 v22
> 本文只属于 Triangle Agency，不是通用掷骰规则。DESIGN / 未启用。

## 权威入口

沿用本目录的 `00_规则检阅协议.md`、`01_基础规则与现场裁定.md` 与 `../Research/triangle-agency-rules-index.md`。索引只定位，裁定必须回查中文 v22 完整原文。Campaign 桌规必须通过当前 `SYSTEM_BINDING.md` 的 `adjudications_entry` 核验作用域；Zarek Q04 不得推广到其他 Campaign。

## 机制路由

### Default Failure
《三角机构》没有通用技能检定。危险或困难的常人行动按 Default Failure 处理，不创造 D20、百分骰或其他系统的通用检定。玩家可以选择 Ask the Agency、已解锁异常能力或规则允许的其他路径。玩家发起掷骰；GM 不得强迫掷骰，也不得替玩家决定如何使用结果。

### Ask the Agency
进入流程需要玩家明确提出：
1. 希望发生的效果；
2. 可信、可能发生的常人因果链（Causality Chain）；
3. 一项相关 Quality。
GM 可要求补充因果链，并对相关 Quality 有最终决定权。满足请求门槛后掷 6d4。
请求只能调整尚未确立的事实，不能直接干涉人的自由意志。成功后效果及新事实成立，并承担后续涟漪；失败时现实反击。失败后，在当前任务剩余时间内，该特工在当前位置继续尝试现实改写会承受一层 Burnout。位置和任务剩余时间必须来自已核验状态。

### Anomaly Ability
每次必须读取具体能力完整条文，核对当前角色 ARC、解锁资格、Trigger/Cost、Quality、成功/失败、额外 3、范围、持续时间和例外。资料或资格未核验时标记 `UNSUPPORTED_PENDING_RULE_REVIEW`，不得套用 Ask 的因果链或失败后果。
中文 v22 当前可用能力规则页已删除能力额外效果中的 `On Triscendence`，不得擅自恢复该项能力专属效果。基础 Triscendence 与能力额外效果分开核验。

### Conflict Resolution
直接冲突迹象包括能力阻止对方达成目标、破坏对方目标、循环争执无法推进或特工间暴力。直接冲突期间手册其他规则不再适用：
1. 时间停止；
2. 所有参与者分别陈述目标；
3. 每位参与者同时掷 6d4，独立记录本轮 3 的数量；目标相同也不合并；
4. 逐轮累计，直到某参与者累计至少 6 个 3 且严格多于其他所有参与者；
5. 多人达到 6 但并列最多则继续；
6. 唯一领先者的目标实现，时间恢复，参与者共同描述过程。
冲突骰不引导机构力量，不产生 Chaos，也不触发 Triscendence。冲突期间能力不受通常限制，不产生 Chaos 或 Loose Ends；最终结果本身造成的 Loose Ends 除外。不得接入普通单次检定的 QA/Burnout/Chaos 结算器。当前单骰池 UI 不支持多轮冲突，使用文本回退。

## 基础 6d4 结果分流

- 原始骰面在任何调整前恰好出现三个 3：触发 Triscendence，直接成功、0 Chaos，等待玩家从三项效果中选择；不进入普通 Burnout/QA/Chaos 路径。三项为 All Hands（为此次掷骰加入任意数量的 3）、Circle Back（恢复任意 3 点已消耗的 QA）、Employee of the Moment（获得 3 点 Commendations）。
- 未触发自然 Triscendence 时，按原文和适用 Campaign 桌规处理 Burnout 与 QA。
- 每层 Burnout 移除一枚 3（若有），并增加 1 Chaos；没有可移除的 3 仍增加该层 Chaos。
- 每点 QA 改变一枚骰子；玩家看过原始骰面后决定是否花费、花费多少、选择哪些骰位与目标面。
- 最终有效结果恰好三个 3 时触发 Stability：0 Chaos，即使通过 QA 调整形成或应用过 Burnout；这不触发自然 Triscendence。
- 其他结果按 v22 掷骰速查表结算；逐骰保留原位、移除和修改轨迹。

### Campaign 桌裁
Zarek Q04 仅当当前绑定为 `triangle_agency` / `中文 v22` / `zarek` 且 Binding 指向对应桌裁清单时生效：先检查 Burnout，再检查 QA；同次 QA 消耗不即时产生 Burnout。其他 Campaign 不得继承 Q04，必须读取自己的批准桌规或核验原文。

## Runtime 与资源
不建立 Dice Ledger。沿用 Runtime §3 稳定事件、当前模组 Resource Ledger、Session Log Entry ID 引用、Runtime State 不存资源余额、Session 结束更新正式人物卡快照，以及 Runtime §14.14 字段级持久化证明。重试不重掷、不重复扣费/发奖。玩家投影按 Runtime §14.19 单一 `player_reply_payload`。

## Playwall 暂缓
本轮不实现依赖 Playwall 解锁或专属条文的资格、特殊骰型、额外骰/3、成本时点、免掷、替代成功条件及覆盖。依赖此范围时使用 `UNSUPPORTED_PENDING_RULE_REVIEW`，不得以基础能力路径回退。待办见 `PLAYWALL_DEFERRED_REGISTER.md`。
