# 核心规则运行手册（Core Set）

> system_id: `daggerheart`  
> 来源基准：Official Daggerheart SRD 2.0（2026-08-25）  
> 规则范围：Core Set only。Hope & Fear 扩展默认关闭。  
> 状态：SOURCE_IMPORTED / 第一轮运行化；尚未通过完整回归与实际跑团验收。

本手册将基础规则规范为按触发条件调用的步骤，避免每次跑团重新搜索网页或重建机制。它是自写运行摘要，不替代完整官方规则书。角色、卡牌、敌人与环境的具体数值/特性优先查同目录本地 JSON。

## 0. 运行原则

1. **先虚构情境，后调用机制。** 行动轻而易举，或失败只会拖慢游戏而不会产生有趣变化时，直接成功。只有结果未知、行动困难或承担真实风险时才要求 Action Roll。
2. **每次重要掷骰都改变局势。** 推进信息、危险、资源、关系、位置或时机；不要以“失败但什么也没发生”结束重要行动。
3. **先明确赌注。** 在玩家作出不可逆决定前，说明角色能够理解的主要风险与资源成本。Difficulty 是否公开由 GM 决定，但风险应当可理解。
4. **没有固定先攻与固定行动次数。** Spotlight 随叙事自然流转；不要把游戏改成每人每轮只能做一次行动。
5. **叙事与规则往返。** 描述场景 → 提问和补充 → 行动 → 结算不确定结果 → 描述变化后的场景。
6. **不为规则而制造掷骰。** 普通交谈、观察、移动或没有实际风险的尝试，不应机械化切割成动作掷骰。
7. **状态变化有据可查。** Hope、Fear、HP、Stress、Armor Slots、Countdown、Conditions、休息次数和卡牌装载变化，记录触发来源和结算结果。
8. **不要把 Fear 当作惩罚额度。** Fear 用于推动对手、环境与场景压力；后果必须符合已建立的虚构事实。
9. **隔离系统与扩展。** 当前系统为 candidate；不得把其他 TRPG 的检定、资源、先攻或伤害流程导入本系统。默认只加载 Core Set。

## 1. 规则调用目录

| Rule ID | 触发条件 | 主要处理 |
|---|---|---|
| DH-LOOP | 场景开始、局势变化、玩家行动结束 | 核心桌面循环 |
| DH-SPOTLIGHT | 聚焦在 PC、GM、敌人或环境间转移 | 聚焦与行动经济 |
| DH-CREATE | 建立新 PC | 角色创建流程 |
| DH-ACTION | PC 行动有真实不确定性/风险 | Duality Dice 动作掷骰 |
| DH-HOPE-FEAR | 获得、消耗、检查上限 | Hope / Fear 资源 |
| DH-GM-MOVE | 失败、Fear 结果、不可避免后果、Golden Opportunity | GM Move 与后果 |
| DH-REACTION | PC 应对攻击或迫近危险 | 反应掷骰 |
| DH-GROUP | 多名 PC 协作解决同一行动 | Group Action Roll |
| DH-TAG-TEAM | 两名 PC 发起协同高光行动 | Tag Team Roll |
| DH-ADV | 存在优势/劣势来源 | d6 优劣势骰与抵消 |
| DH-SPELLCAST | 卡牌/能力明确要求 Spellcast Roll | 子职业施法属性掷骰 |
| DH-ATTACK | PC 攻击目标 | 攻击掷骰 |
| DH-ENEMY-ATTACK | 敌人攻击 PC | GM d20 攻击与 Evasion |
| DH-DAMAGE | 攻击/效果造成伤害 | 伤害骰、阈值、Armor、HP |
| DH-RANGE | 移动、目标范围、视线影响结算 | 距离、移动与范围效果 |
| DH-CONDITION | 获得/解除状态 | 标准条件与特殊条件 |
| DH-DOMAIN | 获取/使用/调换领域卡 | Loadout / Vault / Recall |
| DH-REST | 队伍休息 | Short / Long Rest、恢复与 Fear |
| DH-COUNTDOWN | 场景有时限、累积风险或进度 | Standard / Dynamic Countdown |
| DH-NPC | 普通 NPC 进入场景 | 动机驱动的轻量 NPC |
| DH-ENEMY-DATA | 选取、运行敌人 | 敌人数据结构与 Fear 特性 |
| DH-ENV-DATA | 场景需要环境机制 | 环境数据结构 |
| DH-ENCOUNTER | 准备战斗遭遇 | Battle Points 预算 |
| DH-GEAR | 装备、背包、消耗品、经济 | 武器/护甲/物品/Gold |
| DH-LEVEL-UP | 达到叙事里程碑 | 等级、Advancement、领域卡 |
| DH-DEATH | PC 标记最后一个 HP | Death Move |

## 2. DH-LOOP｜核心桌面循环

**触发：** 新场景开始、PC 行动改变局势、信息或威胁出现重要变化。

1. GM 描述角色能察觉的地点、角色、危险、行动机会和即时变化。
2. 玩家提问以深入探索场景；对角色可以直接观察或合理知道的内容，GM 直接回答。GM 也可以提出问题，让玩家共同补充世界。
3. 玩家说明意图和具体做法。没有真实风险时直接处理；结果未知或有风险时调用对应规则。
4. 按结果叙述世界反应，更新资源、状态、关系、威胁与位置。
5. 回到新的场景描述，直到场景自然结束或机制明确触发结束。

准备局势、人物动机、危险、时间压力和线索，不预写唯一正确解法。玩家选择应能改变真实局势。

## 3. DH-SPOTLIGHT｜聚焦与行动经济

- Spotlight 代表桌面当前注意力与叙事/机制焦点。
- 没有传统固定先攻顺序，也没有每名角色固定的行动次数。
- 聚焦随场景自然流转；当规则触发时，按机制转移。例如 PC 动作掷骰失败或掷出 Fear，GM 接管聚焦并采取 GM Move。
- GM Turn 完成后，聚焦通常回到 PC 一方。
- GM 可花费 Fear 抢夺聚焦、执行额外 Move，或让更多敌人获得聚焦。
- 可选 Spotlight Tracker：若桌面偏好更传统的行动经济，每名玩家在 Session 或场景开始时获得约 3 枚标记；每次获得行动机会消耗一枚，耗尽者暂不再获得聚焦；全员耗尽后补满。它是可选辅助，不是基础先攻规则。

## 4. DH-CREATE｜Core Set 角色创建

1. **职业与子职业：** 从九个 Core 职业中选择；选择其中一个子职业，取得其 Foundation 卡。登记职业 Class Feature 与 Hope Feature。
2. **Heritage：** 选择一个 Ancestry 与一个 Community，取得对应卡牌。两者合称 Heritage。
3. **Traits：** 六项属性为 Agility、Strength、Finesse、Instinct、Presence、Knowledge。将 +2、+1、+1、+0、+0、−1 任意分配。
4. **基础状态：** 从职业表读取 Evasion 与起始 HP；新角色从 Level 1 开始；所有 PC 有 6 Stress 槽、2 Hope。
5. **初始装备：** 选择 Tier 1 的双手 Primary Weapon，或一把单手 Primary + 一把单手 Secondary；选择一套 Tier 1 Armor。Proficiency 从 1 开始。记录职业指南要求的职业物品、火把、50 英尺绳索、基础补给、一把 Gold，以及 Minor Health Potion 或 Minor Stamina Potion 二选一。若职业需要法术载体，按角色指南取得。
6. **背景：** 回答角色指南的 Background Questions。背景没有独立固定数值效果，但会影响角色表达与 GM 备团；可以调整早先选择以贴合背景。
7. **Experiences：** 创造两个 +2 Experiences。它们是具体技能、经历、身份或习惯的概括，不应过于宽泛，也不能直接授予法术或超常能力。
8. **Domain Cards：** 从职业两个 Domains 中选择两张 1 级卡，可各选一张或都选同一领域。角色可选卡等级不得高于当前 Level。
9. **Connections：** 玩家介绍角色，并通过职业指南中的问题建立 PC 关系；单人游戏可将此步骤转化为 PC 与关键 NPC / 组织的关系锚点，但属于桌面适配，需在 Campaign Binding 记录。

Core Set 角色选项索引见 [CHARACTER_OPTIONS_INDEX.md](./CHARACTER_OPTIONS_INDEX.md)，数值与完整字段查 `Reference_Data/Core_Set/`。

## 5. DH-ACTION｜PC 动作掷骰

**骰子：** 两枚可区分颜色的 d12，分别代表 Hope Die 与 Fear Die。

**步骤：**
1. 识别行动适用 Trait。能力指定时按指定值；否则 GM 根据行动方式判断。存在多个合理属性时，GM 决定或让玩家选择。
2. 确定 Difficulty。能力指定时按能力；否则根据场景压力、危险、时间、阻碍与目标防备程度设定。攻击敌人时遵循 DH-ATTACK。
3. 掷骰前声明 Experiences、额外骰和修正；除非能力明确允许事后使用，不可在看到结果后补报。
4. 掷两枚 Duality Dice，合计并加 Trait、Experience、优势骰等适用修正。
5. 总值与 Difficulty 比较；相等视为成功。再比较 Hope Die 与 Fear Die，确定 Hope / Fear 倾向。
6. 与玩家共同确定后果、叙事变化和状态差分。

| 结果 | 成败 | 资源 | 聚焦/后果 |
|---|---|---|---|
| Success with Hope | 成功 | PC +1 Hope | 玩家侧保有聚焦；展示成功与世界回应 |
| Success with Fear | 成功 | GM +1 Fear | 有代价/复杂状况；GM 接管聚焦并作较轻 Move |
| Failure with Hope | 失败 | PC +1 Hope | 较轻后果/复杂状况；GM 接管聚焦 |
| Failure with Fear | 失败 | GM +1 Fear | 重大危险或机会损失；GM 接管聚焦 |
| Critical Success | 自动成功并有额外收益 | PC +1 Hope、清除 1 Stress | 双骰点数相同；视为 Hope 结果；攻击时额外造成暴击伤害 |

总值决定成功/失败；两枚骰子的相对大小决定 Hope/Fear 倾向。不要把 Hope/Fear 简化为成败骰。

## 6. DH-HOPE-FEAR｜资源

### Hope
- 每名 PC 创建时 2 Hope；上限 6；跨 Session 保留。
- 可用于 Help an Ally、Utilize an Experience、发起 Tag Team Roll、启用 Hope Feature。
- Class Hope Feature 成本为 3 Hope；其他能力按卡面文本。
- Help an Ally：描述协助方式，掷 d6 Advantage Die；多名协助者可分别花费 Hope，但行动者只加所有适用优势骰中的最高值。
- Utilize an Experience：在相关 Action / Reaction Roll 前花 1 Hope，加入 Experience 修正；可同时应用多个不同 Experience，按成本逐项支付。
- 超过资源上限时不保留超额点数。

### Fear
- Campaign 开始时 GM 获得每名 PC 1 Fear。
- PC 掷出 Fear 结果、队伍休息或能力明确给予时获得 Fear。
- 上限 12，跨 Session 保留。
- 花费 1 Fear 可：抢夺 Spotlight 并作 GM Move；作额外 GM Move；启用 Adversary Fear Feature；启用 Environment Fear Feature；为敌方掷骰加入适用 Experience。
- 休息 Fear 增量按 DH-REST：Short Rest 获得 1d4；Long Rest 获得 1d4 + PC 数量。

## 7. DH-GM-MOVE｜GM Move

**考虑作 Move 的时机：**
- PC 动作掷骰出现 Fear；
- PC 动作掷骰失败；
- 玩家行为产生不可避免后果；
- 玩家给出立即回应的明显机会（Golden Opportunity）；
- 玩家期待 GM 推进局势。

**结果导向：**
- Critical Success：让玩家描述成功，并给予额外机会/优势。
- Success with Hope：让玩家描述成功，GM 展示世界回应。
- Success with Fear：认可行动成功，同时加入较轻代价、复杂状况或压力；GM 获得 Fear 并接管聚焦。
- Failure with Hope：行动未达意图，但产生较轻代价、复杂状况或压力；PC 仍获得 Hope。
- Failure with Fear：局势明显恶化，带来重大危险、分离、失去重要机会或多名敌人聚焦；GM 获得 Fear。

Soft Move：呈现危险、线索或即将发生的影响，并留出反应窗口。  
Hard Move：后果更直接、更严重，PC 没有机会先阻止或改变结果。

GM Move 是推动场景的工具，不是惩罚玩家的任意权力。后果必须来自已建立的威胁、行动方式、局势或明确机制触发。

## 8. DH-REACTION｜反应掷骰

- 用于回应攻击或迫近危险，代表角色避免/承受即将发生的影响。
- PC Reaction Roll 使用动作掷骰的基础结构，但不产生 Hope / Fear、不触发额外 GM Move，其他 PC 不能通过 Help an Ally 协助该反应。
- PC Reaction Roll Critical Success：忽略该次成功时本会承受的影响，例如伤害或标记 Stress；不获得 Hope，也不清除 Stress。
- 不得把普通 Action Roll 的资源结算套给 Reaction Roll。
- 敌方 Reaction Roll 按敌人规则使用单 d20；可依特定规则花 Fear 添加 Experience。

## 9. DH-GROUP / DH-TAG-TEAM｜协作行动

### Group Action
1. 多名 PC 共同完成一项行动，队伍指定一名 Leader。
2. 其他参与者说明协助方式，各自进行适合情境的 Reaction Roll。
3. Leader 进行正常 Action Roll；每名成功协助者使结果 +1，每名失败者使结果 −1。
4. 协助者 Reaction Roll 不产生 Hope / Fear；Leader 的 Action Roll 正常结算。

### Tag Team Roll
- 每名玩家每 Session 可发起一次；花费 3 Hope，邀请另一名 PC 协同完成高光行动。
- 两名玩家分别作 Action Roll；结算前选择其中一组结果应用于两名角色的共同动作。
- 被选结果为 Hope 时，所有参与 PC 各获得 1 Hope；为 Fear 时，GM 按参与 PC 人数获得 Fear。
- 若为成功的 Tag Team 攻击，两名 PC 分别掷伤害并将伤害合计作为同一来源处理。

## 10. DH-ADV｜优势与劣势

- Advantage：掷 1d6，加到结果。
- Disadvantage：掷 1d6，从结果中扣除。
- 同一掷骰无论有多少来源，最多只掷一枚普通优势骰或劣势骰。
- 优势与劣势一对一抵消；最终不会同时投掷两者。
- Help an Ally 是特别情况：每名协助者独立掷 d6；行动者将自己和所有协助者的骰比较，只加最高一个结果。
- 敌人优势/劣势不同：GM 为敌方相关 d20 额外掷一枚 d20，优势取高、劣势取低。

## 11. DH-SPELLCAST｜施法掷骰

- Spellcast Roll 是使用 Spellcast Trait 的 Trait Roll。
- Spellcast Trait 由子职业决定；只有卡牌或特性明确要求时才掷 Spellcast Roll。
- 成功后按特性文本执行；不能把所有施法行为都自动视作 Spellcast Roll。
- 能造成伤害的 Spellcast Roll 同时属于 Attack Roll，适用攻击和伤害规则。
- 法术持续时间按卡牌文本处理；没有列明机械结束条件时，由控制效果的玩家、GM 或故事自然时机决定；GM 可依相关规则花 Fear 结束临时效果。

## 12. DH-ATTACK｜PC 攻击

1. 攻击是以造成伤害为目的的 Action Roll。
2. 使用武器/法术指定的 Trait；徒手攻击由 GM 在 Strength 或 Finesse 中选择。
3. 对敌人攻击的 Difficulty 等于目标 Adversary 的 Difficulty；其他针对敌人的动作通常以其 Difficulty 为基准，并在相关 Experience 适用时加上修正。
4. 成功后掷伤害；失败不掷普通伤害，除非能力文本另有规定。
5. 武器伤害骰数量等于 Proficiency；固定修正只加一次，不随 Proficiency 倍增。
6. 徒手攻击成功造成 Proficiency d4 伤害。
7. 特性写明按 Spellcast Trait 决定伤害骰数时，掷骰数等于该 Trait；Trait ≤ 0 时不掷伤害骰。
8. Attack Roll Critical Success：正常掷伤害，再加伤害骰可取得的最高总值；固定修正不乘算。
9. 一次能力允许攻击多个目标时，通常作一次攻击掷骰与一次伤害掷骰，再将结果分别应用于每个目标；按能力文本处理差异。
10. 同时来自多个来源的伤害先合计，再与阈值比较。

## 13. DH-ENEMY-ATTACK｜敌人攻击

- GM 使用单 d20，不使用 Duality Dice。
- 掷 d20 + 敌人 Attack Modifier；总值达到或超过 PC Evasion 则命中。
- 命中后掷 Stat Block 所列伤害骰。
- 自然 20 自动命中并增加伤害：正常掷伤害，再加伤害骰可能达到的最高点数；固定修正不重复加倍。
- GM 可在掷骰前给予敌人 Advantage / Disadvantage，或花 Fear 添加相关 Experience。
- 多目标攻击按敌人能力文本处理；若规则指定一次掷骰对比多个目标，应分别比较各自 Evasion，不把目标的伤害承受合并成一个事务。

## 14. DH-DAMAGE｜伤害、阈值与 Armor

### HP 结算
- 最终伤害 ≥ Severe Threshold：标记 3 HP。
- 最终伤害 ≥ Major Threshold 且低于 Severe：标记 2 HP。
- 最终伤害低于 Major：标记 1 HP。
- 伤害减至 0 或更低：不标记 HP。
- PC 的 Major / Severe Threshold = 角色等级 + 当前装备护甲的基础阈值。
- 未穿护甲时 Armor Score=0，Major Threshold=等级，Severe Threshold=等级×2。
- PC HP 槽位上限 12；可通过成长、特性等增加。

### Armor
- Armor Score 代表可标记的 Armor Slots 数量，上限 12。
- 受到伤害时可标记一个 Armor Slot，将伤害严重程度降低一级：Severe→Major→Minor→无 HP 损失。
- Armor Score 为 0 时不能标记 Armor Slot。
- 临时提升 Armor Score 时，获得对应额外 Armor Slots；效果结束时额外 Slots 同时消失。
- 换装后重算阈值；未穿护甲时按基础规则计算。

### 抗性、免疫与特殊伤害
- Resistance：该类型 Incoming Damage 先减半，再比较阈值；按系统通用向上取整规则处理小数。
- Immunity：忽略该类型伤害。
- 多个相同伤害类型的 Resistance 不叠加。
- 混合 Physical / Magic Damage 时，只有对两种类型都具备抵抗/免疫才能对整体伤害享受该防护。
- Direct Damage 不能通过标记 Armor Slot 降低。
- Incoming Damage 指同一次攻击或来源、标记 Armor Slots 前的伤害总值。

## 15. DH-RANGE｜范围、移动与视线

| Range | 场景距离参考 |
|---|---|
| Melee | 可触及，几英尺 |
| Very Close | 约 5–10 ft |
| Close | 约 10–30 ft |
| Far | 约 30–100 ft |
| Very Far | 约 100–300 ft |
| Out of Range | 超过 Very Far，通常不可指定 |

- 武器、法术、能力和物品的 Range 是最大距离；除非特指，可在更近距离使用。
- 处于压力/危险中并进行 Action Roll 时，通常可在该行动中移动到 Close 范围内的位置。
- 若没有同时进行 Action Roll，或希望移动超过 Close，则需成功完成 Agility Roll 才能安全重新定位。
- 敌人可将 Close 范围内移动作为行动的一部分；移动至 Very Far 通常需要独立行动。
- 远程攻击需要 Line of Sight。部分遮挡给予目标 Cover，使攻击带 Disadvantage；完全遮挡则没有视线。
- 默认 Area of Effect：受影响目标都须位于一个处于效果范围内的共同原点 Very Close 范围内。
- 可选方格映射：Melee 1 格、Very Close 3 格、Close 6 格、Far 12 格、Very Far 13 格以上、Out of Range 在地图外。它是可选辅助，不与默认距离混算。

## 16. DH-CONDITION｜条件状态

**标准条件：**
- Hidden：角色不在所有敌人视线内，且敌人不知道其位置；对 Hidden 目标进行的掷骰带 Disadvantage。敌人移动到可看见其的位置、角色进入其视线或角色发动攻击时，Hidden 结束。
- Restrained：不能移动，但仍可从当前位置行动。
- Vulnerable：所有以该目标为对象的掷骰带 Advantage。

**其他条件：**
- 除非能力另有说明，同一条件不能在同一目标身上重复叠加。
- Temporary：PC 通常须执行适当行动掷骰解除；敌人解除时，GM 将 Spotlight 给该敌人并描述其行动，占用它本次聚焦。
- Special Condition：满足能力文本规定的要求后才能清除。
- 状态记录包含来源、目标、开始事件、解除条件及是否已消费。

## 17. DH-DOMAIN｜领域卡、Loadout 与 Vault

- 每个职业开放两个 Domain；角色创建时获得两张 1 级领域卡，每次升级再获得一张角色等级或更低的领域卡。
- Domain Card 类型：Ability、Spell、Grimoire。
- 卡牌等级不得高于角色等级；选牌必须属于角色职业可用 Domain。
- Loadout 是当前可用领域卡，最多 5 张；其余已获得领域卡放入 Vault。
- 子职业、种族和社群卡不占 Loadout 上限，持续生效。
- 每次休息开始、Downtime Moves 前，可免费在 Loadout 与 Vault 间调换卡牌。
- 其他时间从 Vault 调回 Loadout，须标记该卡 Recall Cost 数量的 Stress；如 Loadout 已满，先免费把一张当前卡移入 Vault。
- 升级新获得的 Domain Card 可免费立即放入 Loadout；若已满，仍需把另一张卡移入 Vault。
- 用途次数限制按卡牌文本记录；某些特性根据 Trait 修正赋予次数，修正为 +0 或更低时得到 0 次。

## 18. DH-REST｜休息与 Downtime

每名 PC 每次休息最多执行 2 个 Downtime Move。队伍在 Short Rest 与 Long Rest 之间选择；连续 3 次 Short Rest 后，下次必须 Long Rest。

### Short Rest
- 约 1 小时游戏内时间；若被敌人打断，本次不获得休息收益。
- 每名 PC 可先免费调整 Loadout / Vault，再选择 2 个 Downtime Moves（可重复）：
  - Tend to Wounds：自己或盟友清除 1d4 + Tier HP。
  - Clear Stress：清除 1d4 + Tier Stress。
  - Repair Armor：清除自己或盟友 1d4 + Tier Armor Slots。
  - Prepare：独自准备获得 1 Hope；与至少一名队友共同准备时，参与者各获得 2 Hope。
- 结束时刷新 per-rest 次数，并结束持续至 next rest 的效果。
- GM 获得 1d4 Fear。

### Long Rest
- 在营地休息/睡眠数小时；若被打断，只获得 Short Rest 收益。
- 每名 PC 可先免费调整 Loadout / Vault，再选择 2 个：
  - Tend to All Wounds：自己或盟友清除全部 HP。
  - Clear All Stress：清除全部 Stress。
  - Repair All Armor：清除自己或盟友全部已标记 Armor Slots。
  - Prepare：独自准备获得 1 Hope；与至少一名队友共同准备时，参与者各获得 2 Hope。
  - Work on a Project：需 GM 批准，创建 Countdown；简单项目每次使用自动推进，复杂项目由 GM 决定是否掷 Action Roll 推进。
- 结束时刷新 per-rest / per-long-rest 次数，并结束相应持续效果。
- GM 获得 1d4 + PC 数量 Fear；通常推进一个与当前局势相关的 Long-term Countdown 一次。若具体卡牌、环境、Campaign 规则规定了不同推进条件，按其文本处理。

## 19. DH-COUNTDOWN｜倒计时

- Countdown 从起始值开始，每次推进减少 1；降至 0 时触发。
- Standard Countdown：每次玩家进行 Action Roll 时减少 1。
- Dynamic Countdown：依掷骰结果推进，单次最多推进 3。
- Long-term Countdown：通常在休息后推进。
- Progress / Consequence 推进表：

| 掷骰结果 | Progress 减少 | Consequence 减少 |
|---|---:|---:|
| Failure with Fear | 0 | 3 |
| Failure with Hope | 0 | 2 |
| Success with Fear | 1 | 1 |
| Success with Hope | 2 | 0 |
| Critical Success | 3 | 0 |

- 其他变体包括随机起始值、Loop、Increasing / Decreasing、Linked。
- 倒计时记录类型、起始值、当前值、触发条件、推进事件与触发后结果。同一 Action Roll 不得对同一 Countdown 重复推进。

## 20. DH-NPC｜GM NPC

- 普通 NPC 的基本信息只需 Name、Description、Motive。
- 只有当 PC 可能对其频繁掷骰时，才加 Difficulty。
- NPC 的行动由欲望、关系、利益、恐惧和处境驱动；不用为每个 NPC 创建完整敌人 Stat Block。
- NPC 成为战斗盟友时通常无需完整 Stat Block；可把 Spotlight 给 NPC 并描述其行动如何改变局势。若 PC 借助其帮助，给 PC Advantage。
- 即使没有 HP / Stress 轨，NPC 也可能按虚构情境受伤或死亡。
- 重要 NPC 可有少量 Feature；每项明确 Choice（如适用）、Trigger、Effect。避免过度模拟普通 NPC。

## 21. DH-ENEMY-DATA / DH-ENV-DATA｜敌人与环境

敌人和环境的完整本地数据分别位于：
- `Reference_Data/Core_Set/adversaries.json`
- `Reference_Data/Core_Set/environments.json`

Hope & Fear 对应数据单独放在 `Reference_Data/Hope_and_Fear/`，默认关闭。

**Adversary Stat Block：** Name、Tier、Type、Description、Motives & Tactics、Difficulty、Major / Severe Threshold、HP、Stress、Attack Modifier、Standard Attack、可选 Experience、Action / Reaction / Passive Features、Fear Features；必要时还有 Token Pool 与 Evolution。

敌人类型：Bruiser、Horde、Leader、Minion、Ranged、Skulk、Social、Solo、Standard、Support。

**Environment Stat Block：** Name、Tier、Type、Description、Impulses、Difficulty、Potential Adversaries、Features 与 Feature Questions。环境类型：Exploration、Social、Traversal、Event。

- 敌人表现其自身动机与战术，不只作为伤害数字。
- Reaction 在触发时结算，不需等待 Spotlight；Passive 持续生效；Action 在 Spotlight 时使用。
- Fear Feature 按其文本消耗 Fear；若已花费 Fear 抢夺 Spotlight，Fear Feature 的成本是额外支出。
- Horde、Minion、Relentless、Slow、Pool 和 Evolution 等特性按敌人卡面执行，不要只凭类型猜规则。

## 22. DH-ENCOUNTER｜遭遇预算（Battle Points）

**初始预算：** `3 × 实际参与战斗的 PC 数量 + 2`。

调整：
- −1：希望战斗更轻或更短。
- −2：使用 2 个或更多 Solo。
- −2：全部敌人伤害骰额外增加 1d4（或固定 +2）。
- +1：选用低于队伍 Tier 的敌人。
- +1：遭遇中没有 Bruiser、Horde、Leader 或 Solo。
- +2：希望战斗更困难或更长。

加入敌人的 BP 成本：

| 类型 | BP |
|---|---:|
| 一组 Minions（数量等于 PC 人数） | 1 |
| Social / Support | 1 |
| Horde / Ranged / Skulk / Standard | 2 |
| Leader | 3 |
| Bruiser | 4 |
| Solo | 5 |

预算是准备工具，不是强制脚本或胜负保证。仍须检查目标、地形、敌人组合、Fear 储备与队伍 Tier。

## 23. DH-GEAR｜装备、背包与经济

- 角色只能使用已装备的武器、护甲和物品能力；装备 Tier 不得高于角色 Tier。
- Active Weapon 最多一件 Primary 与一件 Secondary；库存可携带最多两件额外武器。休息或平静时可免费替换 Active / Inventory Weapon；其他时候更换需标记 Stress。
- 护甲只能装备一套；处于危险/压力中不能换装；护甲不能放入普通 Inventory。换装后重算 Armor Score 和阈值。
- 武器字段：Tier、Trait、Range、Damage、Damage Type、Burden、可选 Feature。Burden 是占用手数；角色装备武器总 Burden 上限 2。
- 投掷已装备武器：可对 Very Close 目标使用 Finesse 攻击；投出后不再视为已装备，必须取回并重新装备才能再次攻击或受益于其 Feature。
- 魔法伤害武器通常要求角色拥有 Spellcast Trait。
- 每一种 Consumable 最多持有 5 件；使用通常不要求检定，除非物品文本或虚构情境要求。
- Gold 抽象为 Handfuls、Bags、Chests：10 Handfuls = 1 Bag；10 Bags = 1 Chest；最多持有 1 Chest。满格后再获同档财富，转换为上一级单位并清空低级单位。

## 24. DH-LEVEL-UP｜成长与升级

- GM 判断达到叙事里程碑时全队同步升级，通常约每 3 次 Session 一个里程碑；这是节奏指导，不是硬性计时。
- 共 10 级、4 个 Tier：Tier 1 = Lv1；Tier 2 = Lv2–4；Tier 3 = Lv5–7；Tier 4 = Lv8–10。
- Lv2、Lv5、Lv8 Tier Achievement：获得一个 +2 Experience、Proficiency 永久 +1；Lv5 和 Lv8 还清除此前标记的 Trait 提升限制。
- 每次升级选择 2 个 Tier 当前或更低的未满 Advancement；有多格的选项可重复选择。某些选项（如提升 Proficiency 或 Multiclass）要求占用两个 Advancement 格。
- 常见 Advancement：提升两个 Traits；增加 HP Slots；增加 Stress Slots；提升两个 Experiences；取得额外 Domain Card；提升 Evasion；取得下一张 Subclass Card（Foundation→Specialization→Mastery）；提升 Proficiency；Multiclass。
- 每级提升所有 Damage Threshold 1；取得一张本级或更低等级的 Domain Card。
- Multiclass 从 Lv5 开始：选择额外职业，获得其一个 Domain 与 Class Feature，并取得其一个 Subclass Foundation。来自新 Domain 的卡等级不得超过当前等级的一半（向上取整）；Multiclass 与 Subclass 升级存在规则规定的互斥/消耗格限制，按升级步骤逐项核验。

## 25. DH-DEATH｜死亡行动

PC 标记最后一个 HP 时立即进行 Death Move，选择一项：

1. **Blaze of Glory：** 角色进行最后行动；经 GM 同意，该行动自动 Critical Success，随后角色死亡。
2. **Avoid Death：** 角色昏迷，不能移动、行动或成为攻击目标。盟友清除其至少 1 HP，或队伍完成 Long Rest 后醒来。昏迷后掷 Hope Die；若点数 ≤ 角色等级，获得 Scar：永久划掉一个 Hope Slot，并与 GM 确定长期叙事影响及可能的恢复方式。若最后一个 Hope Slot 也被划掉，角色旅程结束。
3. **Risk It All：** 掷 Duality Dice。Hope Die 更高：角色存活，清除总量等于 Hope Die 点数的 HP 和/或 Stress；Fear Die 更高：角色死亡；双骰相同：存活并清除全部 HP 与 Stress。

死亡 PC 的替代角色通常在下次 Session 前创建，等级与队伍其他 PC 当前等级相同。

## 26. 运行状态最小账本

内部状态至少按需维护：

- PC：Level / Tier / Traits / Evasion / HP / Stress / Hope / Proficiency
- Domain：Loadout / Vault / Recall Cost / 每卡使用次数与刷新条件
- Gear：Active Weapons / Inventory Weapons / Active Armor / Armor Score / Armor Slots / 阈值 / Gold / 消耗品
- Scene：地点 / Range 关系 / Spotlight / 当前威胁 / 可见线索
- GM：Fear（0–12）/ 当前 GM Turn / 已聚焦敌人
- Enemy：HP / Stress / Armor 或 Resistance / Token / Pool / Evolution / Fear Features
- Countdown：类型 / 起始值 / 当前值 / 触发条件 / 下一次推进来源
- Condition：来源 / 目标 / 生效和解除条件
- Rest：上次 Short/Long、连续 Short 次数、各角色已用 Downtime Moves、刷新状态
- Transaction：Rule ID、骰值、前状态、结果、状态差分、来源分类、提交状态

恢复 Session 时，先恢复状态和未完成效果；不得重掷已提交骰、重复应用已提交差分或自动清空跨 Session 的 Hope / Fear。

## 27. 本地检索与回查策略

- 常规规则：查本手册与 [LOOKUP_TABLES.md](./LOOKUP_TABLES.md)，不重复搜索网页。
- 角色/职业/卡牌/装备：查 `Reference_Data/Core_Set/`，按英文名称、类别、Tier 检索。
- 敌人/环境：查本地 JSON 和 [ADVERSARY_INDEX.md](./ADVERSARY_INDEX.md) / [ENVIRONMENT_INDEX.md](./ENVIRONMENT_INDEX.md)。
- 只有本地未覆盖、规则文本冲突、出现官方勘误、新版本、特殊能力覆盖、数据缺失或用户提出具体规则质疑时，才定向回查官方来源。
- SRD 无法替代完整 Core Rulebook；书本特有的示例、完整 GM 指导、地图与专有资料，按许可边界处理。
- 不确定时标记 `UNKNOWN` / `VERSION_UNRESOLVED`，只暂停依赖该缺口的行动，不冻结无关互动。

## 28. 核验状态

- `SOURCE_IMPORTED`：条目已由 SRD 2.0 结构化数据导入或按其整理。
- `SOURCE_CHECKED`：已回查官方 SRD 对应内容与版本归属。
- `VERIFIED_CORE`：步骤、例外、结算顺序已核对，并具备对应测试用例。
- `RUNTIME_TESTED`：已在 GM 运行或独立回归中验证。
- `UNKNOWN` / `DISPUTED` / `VERSION_UNRESOLVED`：仍待解决。

本版完成第一轮结构化和运行化，不代表全部条目已达到 VERIFIED_CORE 或 RUNTIME_TESTED。

## 36. DH-HOPE-FEATURE-TIMING｜希望特性与同次掷骰资源

- 如果 PC 的 Action Roll 结果带 Hope，则该次掷骰获得的 Hope 可以立即用于该行动触发的 Hope Feature，包括支付其全部或部分 Hope 成本。
- 这个时序是对通常“掷骰前声明资源和修正”规则的明确例外：只有该次 Hope 结果所生成的 Hope，才能依本条用于同次行动的 Hope Feature。
- 不得据此在结果出来后补报其他 Experiences、普通额外骰或未声明的资源效果；其他事后生效能力仍按其自身文本和 DH-GENERAL 处理。
- Critical Success 视为 Hope 结果，因此其获得的 Hope 也符合本条。


## 33. Adversary 伤害与生命状态（补充）

- Adversary 的 Major / Severe Threshold 与 HP 直接读取 Stat Block；受到伤害后按与 PC 相同的阈值分档标记 1–3 HP：低于 Major 标记 1，达到 Major 标记 2，达到 Severe 标记 3。
- Adversary 标记最后一个 HP 时即为 Defeated；其表现为失能、逃跑、被制服、死亡或其他状态，由桌面结合虚构决定。
- Adversary 的 Stress 记录在 Stat Block 中，按其 Feature 或效果要求标记；不要把 PC 的 Vulnerable / Stress 耗尽规则擅自套到敌人身上，除非规则明确适用。
- Adversary 没有默认 Armor Score / Armor Slots；若某个敌人有相关能力或效果，按其 Stat Block 明文处理。
- PC 的 Armor Score 上限为 12；PC 的 HP 与 Stress Slots 上限也各为 12。

## 34. Death Move 的叙事边界（补充）

- 标记最后一个 HP 通常立即触发 Death Move。
- 但若角色行为按世界逻辑会直接导致即时死亡（例如无保护跳入活火山），GM 可以裁定不触发 Death Move；这种重大后果必须在行动完成前明确告知玩家，并符合世界逻辑。
- 这是基于虚构的裁定，不是 GM 在普通战斗中任意取消 Death Move 的权限。
