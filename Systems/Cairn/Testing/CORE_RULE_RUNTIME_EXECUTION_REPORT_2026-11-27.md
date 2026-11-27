# Cairn 2e 核心规则运行回归执行报告

- 执行日期：2026-11-27
- 仓库：`zzhhaannggddii22-hash/Trpg-gm-workbench`
- 分支：`feat/cairn-second-system-integration`
- 测试矩阵：`Systems/Cairn/Testing/CORE_RULE_RUNTIME_REGRESSION_MATRIX.md`
- 规则手册：`Systems/Cairn/Rule_Reference/CORE_RULES_RUNTIME.md`
- 执行协议：`Systems/Cairn/RUNTIME_PROTOCOL.md`
- 测试类型：GM 自执行的确定性用例/状态差分回归；不是独立盲测，也不是自动化 CI。

## 1. 结果摘要

**Manual Runtime Regression: PASS**

| 指标 | 结果 |
|---|---:|
| 用例总数 | 65 |
| PASS | 65 |
| FAIL | 0 |
| BLOCKED | 0 |
| 带未决规则注记 | 1（CRT-40） |

本报告的 PASS 指：在固定测试输入和当前规范化规则下，执行步骤、规则分支及预期状态变化一致。它不代表整套 Cairn 2e 已完成全部章节核验、自动化覆盖或真实玩家盲测。

## 2. 执行方法

1. 每个用例独立复位，不继承其他用例的 HP、属性、库存、时间或事件状态。
2. 按规则 ID 选择条目，依次检查触发条件、输入、执行顺序、结果与状态差分。
3. 对数值案例使用矩阵给出的固定骰值/状态；对程序案例使用明确的规则触发条件。
4. 将规则错误、状态账本错误和信息呈现错误分别检查。
5. 用官方 Cairn 2e Player's Guide / Procedures 的对应条目核验核心判定；未明确的地方不自行补造，转入未决项。

## 3. 逐项执行记录

| 用例 | 结果 | 执行结论 |
|---|---|---|
| CRT-01 | PASS | 无风险且工具充分；不调用 Save。 |
| CRT-02 | PASS | DEX 9：掷 8 成功；1 恒成功；20 恒失败。 |
| CRT-03 | PASS | 共同冒险行动由更处于风险的一方 Save；通常是相关属性较低者。 |
| CRT-04 | PASS | 明显可见陷阱线索直接呈现，不设感知门槛。 |
| CRT-05 | PASS | NPC 背景/经历无法支持的知识不凭空获得。 |
| CRT-06 | PASS | 伤害 5 - Armor 2 = HP 损失 3。 |
| CRT-07 | PASS | Impaired 将伤害骰改为 d4。 |
| CRT-08 | PASS | Enhanced 将伤害骰改为 d12。 |
| CRT-09 | PASS | 多名攻击者同一目标取最高单骰 5，不累加。 |
| CRT-10 | PASS | PC HP 3 承受 3 点实际伤害恰好归零，查 Scars 的 HP Lost 3。 |
| CRT-11 | PASS | HP 3 承受 5 点伤害，溢出 2；STR 10→8，再以 8 做 STR Save。 |
| CRT-12 | PASS | Critical Damage Save 成功后仍在战斗；再次承受伤害时再次进行 Save。 |
| CRT-13 | PASS | HP 0 后再受 1 点伤害进入 Critical Damage，不重复触发 Scars。 |
| CRT-14 | PASS | 库存无空格时增加 Fatigue，必须丢弃物品腾格，不得超过 10 格。 |
| CRT-15 | PASS | Deprived 期间不能恢复 HP、属性或清除 Fatigue。 |
| CRT-16 | PASS | Deprived 超过一天后按天增加 Fatigue；Fatigue 占库存格。 |
| CRT-17 | PASS | 在同一房间/地点花费超过一个 Dungeon Cycle，触发 Dungeon Event 检查。 |
| CRT-18 | PASS | 快速/草率移动、进入新区域、制造巨大动静均识别为 Dungeon Event 触发条件。 |
| CRT-19 | PASS | 同一角色每 Watch 仅一个 Wilderness Action；第二个行动需消耗后续 Watch 或有明确规则依据。 |
| CRT-20 | PASS | 夜间旅行进行两次 Wilderness Event 掷骰。 |
| CRT-21 | PASS | 4 人敌群：首次伤亡和减员至半数分别触发 Morale；PC 不做 Morale。 |
| CRT-22 | PASS | 孤立敌人 HP 恰好降至 0 时进行 WIL Morale Save；不误调用 HP<0 的 Critical Damage。 |
| CRT-23 | PASS | 撤退同时需要成功 DEX Save 与安全目的地；缺少安全目的地不能逃脱。 |
| CRT-24 | PASS | 战斗外伤害按适当属性损失处理，不误扣 HP。 |
| CRT-25 | PASS | STR 归零死亡；DEX 归零瘫痪；WIL 归零 delirious。 |
| CRT-26 | PASS | 库存不能超过 10 格；满格后需先处理负重。 |
| CRT-27 | PASS | 地城 Turn Rest 必须有光源且地点安全；存在/迫近危险时不能恢复全部 HP。 |
| CRT-28 | PASS | NPC 态度已由明确事实决定时不强制掷 Reaction。 |
| CRT-29 | PASS | Die of Fate 仅作为可选不确定性工具；不用于改写已确立事实或挡住可观察信息。 |
| CRT-30 | PASS | L3 NPC 交付资源时双方库存/数量同步更新，容量与用途可追溯。 |
| CRT-31 | PASS | 库存填满 10 格使 HP 降至 0；非伤害性归零不触发 Scars。 |
| CRT-32 | PASS | 两人共同风险行动只由更危险/相关属性较低者进行一次 Save。 |
| CRT-33 | PASS | Road + Short + Easy 的行程惩罚为 +1 Watch；道路不增加迷路概率。 |
| CRT-34 | PASS | Trail +1、Medium +2、Tough +1，合计 4 Watches；Trail 基础迷路风险 2-in-6。 |
| CRT-35 | PASS | 跳过 Make Camp：每人增加 Fatigue 并 Deprived；睡眠不足旅行使地形难度提高一级。 |
| CRT-36 | PASS | Make Camp：每名角色/坐骑消耗一份 Ration，安排守夜；能够休息者清除全部 Fatigue。 |
| CRT-37 | PASS | 夜间旅行必须掷两次 Wilderness Events。 |
| CRT-38 | PASS | 单人队伍不凭空生成守夜人；明确呈现无人守夜或跨日轮换的选择与后果。 |
| CRT-39 | PASS | 价值低于 100gp 的一袋钱币为 Petty，不占格。 |
| CRT-40 | PASS* | Panic：HP 降至 0、首轮不行动、攻击 Impaired；以行动 + WIL Save 克服。解除时 HP 恢复问题保留为官方未明确事项，不擅自恢复。 |
| CRT-41 | PASS | 谨慎角色获得足以避免陷阱的可观察线索。 |
| CRT-42 | PASS | 未察觉且结果未由虚构确定的陷阱按 2-in-6 触发。 |
| CRT-43 | PASS | 陷阱伤害通常作用于属性；Armor 仅在该伤害类型适用时减伤。 |
| CRT-44 | PASS | 火把最多点燃三次后损坏；提灯每罐油六次点燃，资源同步扣减。 |
| CRT-45 | PASS | Spellbook 双手持有并朗读，施法后增加 1 Fatigue；安全且有时间可增强效果。 |
| CRT-46 | PASS | Deprived 或危险中施法时 Warden 可要求 WIL Save，失败后果与法术效果相称。 |
| CRT-47 | PASS | Scroll 为 Petty、一次后消失且不加 Fatigue；Relic 不加 Fatigue，按 Recharge 条件管理。 |
| CRT-48 | PASS | Scars 1：部位骰 4=Chest；后续骰 6 高于最大 HP 5，最大 HP 提高至 6。 |
| CRT-49 | PASS | Scars 2：Rattling Blow；后续骰 5 高于最大 HP 4，最大 HP 提高至 5。 |
| CRT-50 | PASS | Scars 3：Walloped；Deprived 数小时，休息后最大 HP 增加 4。 |
| CRT-51 | PASS | Scars 4：骰 2=腿；治愈后 2d6=9，高于最大 HP 8，最大 HP 提高至 9。 |
| CRT-52 | PASS | Scars 5：Diseased；痊愈后 2d6=10，高于最大 HP 8，最大 HP 提高至 10。 |
| CRT-53 | PASS | Scars 6：骰 3=DEX；3d6=14 高于当前 DEX 12，DEX 提高至 14。 |
| CRT-54 | PASS | Scars 7：Hamstrung；恢复后 3d6=13 高于最大 DEX 12，最大 DEX 提高至 13。 |
| CRT-55 | PASS | Scars 8：Deafened；WIL Save 成功后最大 WIL 增加 1d4=3。 |
| CRT-56 | PASS | Scars 9：Re-brained；3d6=15 高于最大 WIL 14，最大 WIL 提高至 15。 |
| CRT-57 | PASS | Scars 10：Sundered；WIL Save 成功后最大 WIL 增加 1d6=4。 |
| CRT-58 | PASS | Scars 11：Mortal Wound；未在一小时内获救则死亡；获救恢复后 2d6 设为新最大 HP。 |
| CRT-59 | PASS | Scars 12：Doomed；下一次 Critical Damage Save 失败死亡，成功后按 3d6 检查最大 HP 提升。 |
| CRT-60 | PASS | 连续两天掷出 Extreme，第二次后升级为 Catastrophic。 |
| CRT-61 | PASS | Inclement：Fatigue 或 +1 Watch 二选一，并且地形难度提高一级。 |
| CRT-62 | PASS | Supply：两人参与时收获骰可由 d4 提高至 d6；每份 Ration 有 3 次使用。 |
| CRT-63 | PASS | Trail 2-in-6 迷路风险下掷出 2，触发迷路；按情境消耗额外 Wilderness Action 找路。 |
| CRT-64 | PASS | 一个 Turn 可彻底搜索一个物件/地点；大型复杂房间可持续多个 Turn，时间成本照常推进。 |
| CRT-65 | PASS | 巨大声响识别为 Dungeon Event 触发条件；符合虚构情境时可直接引发遭遇，不机械强制每次掷骰。 |

## 4. 执行中发现并已修正的问题

### F-01｜孤立敌人 HP 恰好为 0 的规则分支混淆

原矩阵曾把孤立敌人 HP 恰好降至 0 同时标为 Morale 与 Critical Damage。官方规则区分：孤立敌人降至 0 HP 时触发 Morale Save；Critical Damage 的触发条件是 HP 低于 0。已修正 CRT-22。

### F-02｜Die of Fate 测试输入不合适

原测试把“玩家询问一个无风险、未知的世界细节”作为 Die of Fate 用例，容易误导 GM 把随机骰当成世界事实生成器。现改为：仅在 Warden 确实需要决定偶然性时使用可选 Die of Fate；不得改写已确立事实，也不得挡住角色可直接观察的信息。

### F-03｜HP=0 的非伤害性来源没有独立分支

库存填满 10 格会使角色 HP 降至 0；Panic 也会使角色 HP 为 0。Scars 的触发依赖伤害造成 HP 恰好归零，不能把所有 HP=0 统一处理为 Scars。已增加独立规则说明和 CRT-31、CRT-40。

### F-04｜荒野程序过于概述化

原手册未充分落地 Watch、旅行惩罚叠加、路径迷路概率、季节天气表、Extreme 连续升级、夜间双事件、跳过扎营、守夜、口粮与 Supply 收获骰。现已补充到运行手册，并增加 CRT-33 至 CRT-38、CRT-60 至 CRT-63。

### F-05｜Scars 表依赖外部回查

Scars 是核心规则，不应每次触发时才上网查表。已将 1–12 项改写为自有结构化速查，并加入 CRT-48 至 CRT-59 的逐项确定性回归。

## 5. 保留的未决事项

1. **Panic 解除后的 HP 状态**：官方规则明确 Panic 期间 HP 为 0，并要求在回合中花费行动通过 WIL Save 克服 Panic；但当前规则条目没有明确写出解除时是否恢复 Panic 前的 HP。运行时不得擅自恢复，记录为 `GM_INFERENCE / unresolved`，等待更高层审核或进一步官方资料确认。
2. **属性恢复服务与具体治疗来源**：一般是一周休息并由医者/适当专业支持；不同治疗服务的费用、速度与效果仍需按具体来源核验（`CR-ATTR-REC: PARTIAL`）。
3. **Hireling 的角色表、费用与具体资源**：核心规则给出创建方向，但 Marketplace 的角色选项与个体条目仍需按需核对（`CR-HIRELING: PARTIAL`）。
4. **模组/生物/法术/遗物的专属规则**：属于 `MODULE_DEPENDENT`，不能用通用核心规则摘要替代。

## 6. 本轮验收判断

- 核心 Save、攻击、Armor、Critical Damage、Scars、Morale、Inventory、Fatigue、Panic、Traps、Light、Magic、Dungeon 与 Wilderness 的常规调用路径已覆盖。
- HP 恰好 0 / HP 低于 0 / 非伤害性 HP 归零已有明确分流。
- 状态差分和事件触发已有运行时提交检查。
- 仍有 PARTIAL 与 MODULE_DEPENDENT 条目，不得声称 Cairn 2e 全部规则已本地化。
- 本报告是自执行回归证据，必须交由独立审核者检查测试设计、规则解释、测试结果和报告是否存在自证循环。

**结论：核心规则运行回归在本轮自执行中 PASS（65/65）。系统状态继续保持 candidate；不因本报告自动升级 active。**
