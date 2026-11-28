# GM 专项桌面模拟记录 01

> 测试范围：DH-GM-01–10、DH-GD-01–09  
> 规则范围：Daggerheart Core Set / SRD 2.0  
> 执行方式：桌面逻辑模拟（非代码自动化、非真实桌面测试）  
> 结果：19/19 通过本轮逻辑模拟；仍需实际短场景验证  
> 关联文档：GM_RUNTIME_FIELD_GUIDE.md、GM_DESIGN_FIELD_GUIDE.md、CORE_RULE_RUNTIME_REGRESSION.md

## A. GM Move / Fear / Spotlight

| ID | 输入情境 | 结算检查 | 结果 |
|---|---|---|---|
| DH-GM-01 | PC 在无人看守的空房间成功完成一项高风险操作，结果 Success with Fear | 保留成功；GM 获得 Fear；没有敌人也可选择环境变化、噪音暴露或时间压力，不凭空生成攻击者 | PASS |
| DH-GM-02 | PC Failure with Hope | PC 未达成意图并获得 Hope；GM 可执行较轻 Move；GM 不因 Hope 获得 Fear | PASS |
| DH-GM-03 | PC Critical Success | 自动成功、PC +1 Hope、清除 1 Stress；该结果按 Hope 处理，不额外给 GM Fear | PASS |
| DH-GM-04 | PC Reaction Roll Critical Success | 忽略本会承受的影响；不获得 Hope、不清除 Stress、不触发额外 GM Move | PASS |
| DH-GM-05 | GM 花 1 Fear 抢夺 Spotlight，随后使用成本 1 Fear 的 Fear Feature | 抢夺 Spotlight 与 Fear Feature 分开记账，总支出 2 Fear | PASS |
| DH-GM-06 | GM 已聚焦一个敌人，随后希望让第二个敌人也行动 | 第二名敌人是额外 Spotlight，另行支付 Fear；不能把首次敌人聚焦当作整队免费行动 | PASS |
| DH-GM-07 | 敌人拥有 Relentless (2)，本 GM Turn 已获得一次 Spotlight | 最多可再获得一次 Spotlight；额外重复聚焦按规则支付 Fear；不得超过特性上限 | PASS |
| DH-GM-08 | GM 当前有 12 Fear，触发新的 Fear 收入 | 资源不得超过上限 12；不保留隐形溢出 | PASS |
| DH-GM-09 | PC 已看见并忽略环境即将坍塌的明确警告 | 可按已建立危险兑现 Hard Move；后果范围与强度必须符合预告，不追加未建立的额外惩罚 | PASS |
| DH-GM-10 | PC 获得 Success with Hope，但战场仍存在高强度敌方威胁 | 对本次 Hope 结果优先使用 Soft Move；若之后发生独立触发/已成立的不可避免后果，再按其条件处理强硬后果 | PASS |

## B. 后果与遭遇设计

| ID | 输入情境 | 结算检查 | 结果 |
|---|---|---|---|
| DH-GD-01 | PC 成功打开锁门，巡逻队正在接近，结果 Success with Fear | 门已打开；巡逻压力升级或声音暴露，但不得把开门改判为失败 | PASS |
| DH-GD-02 | PC 成功说服守卫放行，守卫记住其面孔，结果 Success with Fear | 放行成功保留；代价为后续关注/身份暴露，不直接撤销许可 | PASS |
| DH-GD-03 | PC 调查失败但掷出 Failure with Hope | 目标证据未取得；产生轻度新信息/时间变化/可继续行动的后果；不额外增加 GM Fear | PASS |
| DH-GD-04 | 敌人开始蓄力并明确预告下一次攻击 | 玩家获得可理解的回应窗口；后续兑现时依据已建立机制与位置结算 | PASS |
| DH-GD-05 | 敌人 Motives & Tactics 为“保护祭司、拖延时间” | 敌人优先保护祭司、阻挡路线或拖延仪式，而不是默认攻击最近 PC | PASS |
| DH-GD-06 | Reaction 触发条件满足，但该敌人当前没有 Spotlight | Reaction 按其触发条件发生；不要求敌人先取得行动聚焦 | PASS |
| DH-GD-07 | GM 想无成本打断 PC 当前 Spotlight 并执行 Move | 先区分当前 GM Turn 与玩家 Spotlight；若要打断玩家并夺取 Spotlight，按规则支付 Fear | PASS |
| DH-GD-08 | Environment Feature 产生烟雾遮蔽并改变路线 | 环境改变视线、移动与选择；不把环境特性一律转换成伤害 | PASS |
| DH-GD-09 | PC 成功完成行动，但 Success with Fear 的后果直接兑现 | 成功成果保留；后果严重度仍为次要，但可采用 Hard Move 形式；严重度与回应窗口分别判断 | PASS |

## C. 本轮发现与修正

1. **Hope 结果的严重度**：官方 Core GM Guidance 明确建议 Hope 结果使用 Soft Move、Fear 结果使用 Hard Move。必须将回应窗口与后果严重度分开：Success with Fear 仍是次要后果，但可采用更直接的 Hard Move 形式；Failure with Hope 是次要后果，并优先留出回应窗口。
2. **Relentless 的 Fear 成本**：不能把特性上限理解为免费额外行动。首次敌人聚焦与后续重复/额外聚焦要区分；后续重复聚焦按规则支付 Fear，并受 X 次上限限制。运行手册已修正措辞。
3. **GM 文章中的无成本打断观点**：社区战斗文章将 GM 的灵活叙事权解释得较宽；官方 Core GM Mechanics 明确列出花费 Fear 打断玩家、夺取 Spotlight。工程采用官方资源规则，不把社区作者解释升格为 Core 规则。
4. **Success with Fear 的“不能比不行动更差”**：保留为社区主持建议，而不是硬性规则。正式运行检查的是成功成果是否保留、代价是否属于次要后果，以及重大后果是否有独立赌注/触发支持。

## D. 验收边界

- 本批 18/18 通过的是规则逻辑桌面模拟，说明文档中的流程彼此一致。
- 这不证明生产 GM Runtime 已自动实现这些流程。
- 仍需实际主持场景观察：GM 是否能在不打断玩家节奏的情况下选择后果、敌人是否按动机行动、Fear 是否在有意义的窗口支出、战斗是否避免机械轮转。
