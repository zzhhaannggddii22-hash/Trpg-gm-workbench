# Bower Street｜Runtime State

> 当前状态：ACTIVE / SESSION 01 / READY WITH LIMITS
> 本文件是唯一有效的当前运行快照。正式 Preflight 后填写；不把备团后台状态伪装成玩家已知信息。

## Session 状态
- Module：Bower Street
- Campaign：Zarek
- System：triangle_agency / 中文 v22
- Lifecycle：ACTIVE
- Session：SESSION 01 已开始
- Last confirmed event ID：BS-002（桌外 GM 失误记录；最近游戏内事件仍为 BS-001）
- Current scene/location：Ternion City 大都会分部｜任务简报室
- In-game time：未设定（等待模组开场时间或玩家确认）
- Player last action / GM last response：玩家明确下达“开始”；GM 已呈现任务简报。其后发生一次 GM-only 地点索引泄露，已按 BS-002 登记并纠正；当前等待扎雷克选择调查入口。

## 玩家角色
- 角色卡权威来源：Preflight 时读取 Campaign/Zarek 当前正式人物卡
- 当前场次副本：未建立
- ARC / Rank / QA / Burnout / Harm / Demerits / Commendations / Time：Preflight 待核
- 当前装备、持有人、充能：Preflight 逐项点交
- 不继承 F-33 测试团的资源、关系、装备消耗或世界后果

## 公开资源
- 普通 Chaos Pool：**0（已完成 Preflight 核算）**。分部：Ternion City 大都会分部。分部 Loose Ends 追踪基线：**1**，口径为目前可核实的扎雷克战役贡献，不声称覆盖该分部其他历史小组。按中文 v22 分部累计规则，1 未达到首个 11 点阈值；开局普通 Pool 为 0，天气事件为 0。玩家开场时公开当前 Pool。双猫显现/囚禁的具体资源适用规则仍 UNKNOWN：不擅自扣费或免费施加；争议效果暂停，但其他合法调查继续。
- 发生资源变化时：记录变化来源、数值、当前余额，并在游戏中向玩家公开。

## 地点与 NPC 状态
- 所有模组地点：NOT ENTERED（当前仅在机构简报室）
- Justin / Fumiko / Rebecca / Jodie / Caitlin / Evie：模组初始状态，尚未与 PC 互动
- NPC 知识：只按各自角色卡与实际事件更新，不因 GM-only 事实自动公开

## 调查与信息
- 玩家已获得信息：BS-001 任务简报（详见 Sessions/SESSION_01.md）；仅包括简报实际呈现的报警录音、宠物失踪趋势、1058 寻宠启事、任务目标与附加任务。
- 玩家提出的假设：无
- 已交叉验证事项：无
- 未确认事项：门牌住户对应关系（简报明确出现的 Justin Hamamoto 除外）、1063 的身份/重要性、Domain 位置、地下室与隐藏机制均未向角色披露。
- GM 信息泄露：BS-002；泄露内容不进入角色知识或 Player Notes，但承认玩家已在对话中看到。

## 异常状态（GM-only）
- 当前模组初始状态：异常活动并向社区扩张；地下室为初始 Domain。
- 已触发 Chaos Effects：无
- Domain 扩张记录：初始仅地下室；每次合法 Expand 后，记录新增地点、效果实际生效时间及当前仍纳入 Domain 的地点。判定 Corrupt 等域内费用时，读取事件发生当刻的实际地点集合，不以“首次进入”或后续阶段描述覆盖历史状态。
- 受害者状态：以模组初始状态为准，尚未因玩家行动改变
- 当前触发条件/进度：尚无桌面事件

## Preflight 待办
- [x] 读取当前正式人物卡与战役交接。
- [x] 核对系统绑定、规则版本与 Campaign 桌裁。
- [x] 核对角色 QA/Burnout/Harm/资源；正式人物卡 §6 当前记录 Dynamism 1/1、Initiative 1/1，交接历史快照的 0/1 与 0/0 记录已过时，除非存在更新的实际消耗事件。
- [x] 逐件核对公文包、涟漪枪、充能及当前装备持有人。
- [x] 确认单人桌适配边界。
- [x] 已确认玩家可见信息边界；开场简报已记录于 SESSION_01。
- [x] 已启用 08_PLAYER_FACING_GATE.md；每轮玩家可见回复前执行来源、知识权限、表达三步检查。
- [x] 已登记 BS-002 GM-only 信息泄露；泄露内容排除出角色知识，后续不得以此引导。
- [x] 已确认扎雷克隶属 Ternion City 大都会分部；分部 Loose Ends 追踪基线为 1（仅含可核实的扎雷克战役贡献）；按 v22 核算开局普通 Chaos Pool 为 0，天气事件为 0。
- [x] Preflight 完成；玩家已明确说“开始”，SESSION 01 ACTIVE。
