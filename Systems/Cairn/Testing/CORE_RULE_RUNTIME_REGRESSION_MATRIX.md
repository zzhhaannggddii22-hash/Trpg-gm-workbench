# Cairn 2e 核心规则运行回归矩阵

> 状态：v0.1 测试设计；尚未执行。
> 规则基准：Cairn Second Edition 官方规则。
> 目的：验证规则规范化条目是否能被 GM 正确调用，尤其是顺序、边界和状态差分，而不只是背诵规则摘要。

## 1. 执行要求

- 每个用例独立从指定初始状态开始；不得继承上一个用例的状态。
- 测试者只在完成行动声明后读取预期结果（Oracle），避免提前引导。
- 保存原始行动、规则 ID、骰值、步骤、中间值、状态前后差分。
- 结果分为 PASS / FAIL / BLOCKED；BLOCKED 必须指出缺失来源或资料。
- 规则错误、状态错误、信息呈现错误分别记录，不能用文笔或其他维度抵消。
- 本矩阵仅是核心机制回归，不替代模组实战和玩家盲测。

## 2. 核心用例

| ID | 初始条件 / 行动 | 预期规则调用 | 关键验收点 |
|---|---|---|---|
| CRT-01 | 无风险且有足够工具的简单行动 | 不调用 Save | 不为每个动作强行掷骰 |
| CRT-02 | 有真实负面风险的攀爬 | CR-SAVE / DEX | d20 ≤ DEX 成功；1 恒成功、20 恒失败 |
| CRT-03 | 两名角色共同搬运，风险分配不均 | CR-SAVE | 由更处于风险中的一方 Save，而非机械要求双方都掷 |
| CRT-04 | 角色观察明显可见的陷阱痕迹 | CR-INFO | 直接提供基本感官可见信息，不设置感知检定 |
| CRT-05 | NPC 被问及其背景无法支持的知识 | CR-INFO | 不全知；可说明不知道或使用适当的不确定性程序 |
| CRT-06 | Armor 2 承受伤害骰 5 | CR-ARM / CR-ATTACK | HP 扣 3；Armor 不重复减伤 |
| CRT-07 | Impaired 攻击，武器原伤害骰 d8 | CR-MOD | 改掷 d4，不是 d8 后再减半 |
| CRT-08 | Enhanced 攻击，武器原伤害骰 d8 | CR-MOD | 改掷 d12 |
| CRT-09 | 多名攻击者攻击同一目标，伤害骰 2、5、4 | CR-ATTACK | 只取最高 5，不求和 |
| CRT-10 | PC HP 3，承受最终伤害 3 | CR-SCARS | HP 恰好 0，按本次 HP 损失量 3 查 Scars；不进入 Critical Damage |
| CRT-11 | PC HP 3，承受最终伤害 5，STR 10 | CR-CRITICAL | 溢出 2，STR 先降至 8，再以 8 做 STR Save |
| CRT-12 | Critical Damage 成功后再次承受使 HP 低于 0 的伤害 | CR-CRITICAL | 每次再次承受 Critical Damage 都再次 Save |
| CRT-13 | PC HP 0，之后受到 1 点伤害 | CR-CRITICAL | HP 低于 0，进入 Critical Damage；不重复触发“恰好到 0”的 Scars |
| CRT-14 | Fatigue 增加但库存已满 | CR-FAT / CR-INV | 必须丢弃物品腾格，不能超 10 格 |
| CRT-15 | Deprived 期间尝试恢复 HP/Fatigue | CR-FAT / CR-HP | Deprived 阻止相应恢复 |
| CRT-16 | Deprived 超过一天 | CR-FAT | 按每一天增加 Fatigue；Fatigue 占格 |
| CRT-17 | 地城同一地点连续第二个 Cycle | EX-DUNGEON-EVENT | 满足超过一个 Cycle 条件时触发事件检查 |
| CRT-18 | 地城快速移动/进入新区/制造噪音 | EX-DUNGEON-EVENT | 对应触发原因被识别并记录，不漏检 |
| CRT-19 | 荒野一个 Watch 中同一角色尝试两个 Wilderness Actions | EX-WILDERNESS | 每角色每 Watch 一个 Action；第二个需推进 Watch 或有规则依据 |
| CRT-20 | 荒野夜间旅行 | EX-WILDERNESS | Wilderness Event 掷两次，且结合夜间风险 |
| CRT-21 | 敌方首次伤亡与损失半数成员 | CR-MORALE | 两个触发点各自正确处理；PC 不做 Morale |
| CRT-22 | 孤立敌人 HP 恰好降至 0 | CR-MORALE | 孤立敌人触发 WIL Morale Save；此时并未因伤害使 HP 低于 0，不调用 Critical Damage |
| CRT-23 | 危急战斗中撤退但没有安全目的地 | CR-RETREAT | 不允许只靠成功 DEX Save 宣称逃脱 |
| CRT-24 | PC 战斗外遭受毒素伤害 | CR-ATTR-LOSS | 作用于适当属性，不误扣 HP |
| CRT-25 | 属性降至 0 | CR-ATTR-LOSS | STR 死亡、DEX 瘫痪、WIL delirious |
| CRT-26 | 角色满 10 格又获得普通物品 | CR-INV | 不能超过 10 格，必须先处理负重 |
| CRT-27 | 地城 Turn Rest，但有迫近危险或无光源 | CR-HP | 不允许恢复全部 HP |
| CRT-28 | NPC Reaction 已由明确事实决定 | CR-REACTION | 不强制随机掷骰；只有态度不明才使用表 |
| CRT-29 | Warden 已确认世界事实未知，且需决定一个非角色检定的偶然事件 | CR-DOF | 可选 1d6；4+ 通常有利于 PC，3- 通常不利。若问题涉及已确立事实或 PC 可直接观察的信息，不掷骰 |
| CRT-30 | L3 NPC 交出一份口粮/灯油/工具 | CR-INV + L3 Ledger | 交付方减少、接收方增加，容量与可用数量正确；不得只在对话中口头交付 |
| CRT-31 | PC 因装满 10 格而 HP 降至 0 | CR-INV | HP 降至 0；这是库存规则，不是攻击造成的归零，不触发 Scars |
| CRT-32 | 两名角色共同完成一项有风险的行动，相关属性分别为 STR 13 与 STR 8 | CR-SAVE | 通常由相关属性较低且风险更高的角色进行一次 Save；不要求两人机械地各掷一次 |
| CRT-33 | 一支队伍从道路、短距离、简单地形前往目标 | EX-WILDERNESS | 路径距离 +1 Watch；Road/简单地形无额外 Watch；不凭空加迷路风险 |
| CRT-34 | 一支队伍从 Trail、Medium 距离、Tough 地形前往目标 | EX-WILDERNESS | +1 Trail +2 Medium +1 Tough = 4 Watches；Trail 迷路风险 2-in-6，其他因素再独立修正 |
| CRT-35 | 角色跳过最后一个 Watch 的 Make Camp | EX-WILDERNESS / CR-FAT | 每名角色增加 1 Fatigue 并进入 Deprived；睡眠不足旅行时地形难度提高一级 |
| CRT-36 | 角色执行 Make Camp | EX-WILDERNESS / CR-INV | 每名 PC 和坐骑消耗 1 Ration；安排守夜；能够休息者移除全部 Fatigue |
| CRT-37 | 队伍夜间旅行 | EX-WILDERNESS-EVENT | Wilderness Events 掷两次；不可只掷一次，也不能把夜间旅行当作普通 Watch |
| CRT-38 | 单人 PC 在荒野扎营且没有同伴守夜 | EX-WILDERNESS | 不虚构完整轮值；向玩家呈现无人守夜/分段睡眠等真实选择及后果 |
| CRT-39 | PC 使用一袋价值 50gp 的钱币 | CR-INV | 属于 Petty，不占库存格；不得误计为普通 1 格物品 |

## 3. 关键状态断言

### HP 与伤害分支

- HP_after > 0：常规 HP 更新。
- PC HP_after = 0：调用 Scars，查表依据是本次 HP 损失量。
- HP_after < 0：计算溢出伤害，扣 STR，再以新 STR Save。
- HP 已为 0 后再次受到伤害：进入低于 0 的分支，不重复当作刚好降至 0。

### Fatigue 与库存

- Fatigue 是占格项目，不是独立于库存的抽象点数。
- Deprived 与 Fatigue 分开维护。
- Fatigue 增加时若无空格，必须丢物品；不能超载。
- Deprived 期间不得清除 Fatigue 或恢复 HP/属性。

### 时间程序

- 地城 Event Check 依触发条件，而不是每段叙述或每次对话都掷。
- 荒野 Watch 与每角色 Action 数量必须保持一致。
- 游戏内时间推进必须带来相应的资源与事件检查；现实消息间隔不推进世界。

## 4. 验收门槛

核心规则运行层只有在以下条件全部满足时才可标记为 `RUNTIME_REGRESSION_PASS`：

1. 所有适用用例通过；PARTIAL 规则相关用例如缺少原文必须标记 BLOCKED，不能假定通过。
2. 没有 HP=0 / HP<0 混淆、伤害结算顺序错误、Fatigue/库存状态错误等硬性错误。
3. 所有状态差分可追溯到行动和 Rule ID。
4. 同一用例在独立复测中得到一致机制结果。
5. GM 能向玩家清晰呈现可观察信息、显著风险和行动后果。
6. 不调用 Triangle Agency 或其他系统机制。

完成回归矩阵后，仍须在真实短团中检查节奏、机制负担与玩家理解度。
