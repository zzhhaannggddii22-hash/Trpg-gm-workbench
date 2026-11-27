# Cairn 2e 核心规则运行手册

> 规则绑定：`system_id: cairn`；`ruleset_version: Cairn Second Edition`
> 状态：runtime normalization v0.4；官方 Player's Guide / Warden's Guide 章节核验完成，Bestiary、Spellbooks、Reliquary、NPC Tables、怪物/背景创建指南及 20 个官方 Backgrounds 已建立本地完整来源快照。模组专属资料保存在各 Campaign 目录。该状态不代表已完成全部数据结构化，也不代表系统已通过真实跑团验收或可正式激活。
> 权威来源：[官方 Core Rules](https://cairnrpg.com/second-edition/players-guide/core-rules/)、[Character Creation](https://cairnrpg.com/second-edition/players-guide/character-creation/)、[Procedures](https://cairnrpg.com/second-edition/players-guide/procedures/)。本手册为自写结构化摘要，不替代原文。

## 0. 使用规则

本文件把规则转换为运行时可调用条目。每条包含：**触发条件 → 输入 → 执行 → 输出/状态变化 → 例外/边界 → 来源**。

- 标记 `VERIFIED_CORE`：已按官方 2e 对应章节核对，可作为常规运行依据。
- 标记 `PARTIAL`：已建立调用骨架，但依赖的表格、具体选项或边界章节尚未完整录入；涉及细节时必须查官方原文。
- 标记 `MODULE_DEPENDENT`：核心规则要求查具体角色、物品、怪物或模组数据。
- 规则摘要与原文冲突时，以当前桌绑定的官方 Cairn 2e 原文为准，并修订本手册。
- 不得以 Cairn 1e、Into the Odd 或其他系统的相似规则补缺。
- 未收录的规则不等于不存在；不得将“本手册没写”解释为“规则没有规定”。

## 1. 规则调用总表

| ID | 规则 | 触发时机 | 状态 |
|---|---|---|---|
| CR-ATTR | 三属性语义 | 选择豁免属性 | VERIFIED_CORE |
| CR-SAVE | 属性豁免 | 风险行动可能产生负面结果 | VERIFIED_CORE |
| CR-INFO | 信息与知识 | 描述环境、回答问题、判断角色所知 | VERIFIED_CORE |
| CR-HP | HP 恢复 | 短暂休息、饮水、地城休息 | VERIFIED_CORE |
| CR-ATTR-REC | 属性恢复 | 属性损伤后治疗/休养 | VERIFIED_CORE |
| CR-FAT | Deprived / Fatigue | 食物、睡眠或其他关键需求缺失 | VERIFIED_CORE |
| CR-INV | 库存与负重 | 携带、获得、丢弃物品/Fatigue | VERIFIED_CORE |
| CR-ARM | Armor | 伤害结算前 | VERIFIED_CORE |
| CR-REACTION | NPC Reaction | NPC 态度不明确 | VERIFIED_CORE |
| CR-MORALE | 敌方士气 | 首次出现伤亡、敌方损失半数；孤立敌人 HP 到 0 | VERIFIED_CORE |
| CR-COMBAT | 战斗轮与行动 | 战斗开始及每轮 | VERIFIED_CORE |
| CR-ATTACK | 攻击与伤害 | 攻击行动结算 | VERIFIED_CORE |
| CR-DAMAGE-TX | 伤害事务与状态提交 | 伤害、HP归零、Critical Damage | VERIFIED_CORE |
| CR-MOD | 攻击优势/劣势 | 攻击位置或条件影响攻击 | VERIFIED_CORE |
| CR-CRITICAL | Critical Damage | 伤害使目标 HP 低于 0 | VERIFIED_CORE |
| CR-SCARS | Scars | PC 的 HP 被伤害恰好降至 0 | VERIFIED_CORE |
| CR-ATTR-LOSS | 属性损伤与归零 | 战斗外伤害/属性损失 | VERIFIED_CORE |
| CR-DEATH | 角色死亡与接替 | 角色死亡 | VERIFIED_CORE |
| CR-DETACH | Detachments | 大群同类战斗单位整体作战 | VERIFIED_CORE |
| CR-RETREAT | Retreat | 从危急战斗/危险中撤退 | VERIFIED_CORE |
| CR-RANGED | 远程攻击 | 使用远程武器 | VERIFIED_CORE |
| CR-PANIC | 恐慌 | 黑暗、包围或直面最深恐惧 | VERIFIED_CORE |
| CR-TRAPS | 陷阱 | 角色接近/触发陷阱 | VERIFIED_CORE |
| CR-LIGHT | 光源 | 地城/荒野光照与照明资源变化 | VERIFIED_CORE |
| CR-MAGIC | 法术书施法 | 角色使用 Spellbook | VERIFIED_CORE |
| CR-SCROLL | 卷轴 | 使用一次性 Scroll | VERIFIED_CORE |
| CR-RELIC | 遗物 | 使用 Relic | VERIFIED_CORE |
| CR-HIRELING | Hirelings | 招募/创建雇工 | VERIFIED_CORE |
| CR-DOF | Die of Fate | 事件结果不确定且需随机判断 | VERIFIED_CORE |
| EX-DUNGEON | 地城探索循环 | 危险地点中的探索行动 | VERIFIED_CORE |
| EX-DUNGEON-EVENT | 地城事件 | 达到事件触发条件 | VERIFIED_CORE |
| EX-WILDERNESS | 荒野探索与 Watches | 野外旅行/探索 | VERIFIED_CORE |
| EX-WILDERNESS-EVENT | 荒野事件 | 每次荒野行动循环后 | VERIFIED_CORE |

## 2. 核心角色与检定

### CR-ATTR｜属性语义 — VERIFIED_CORE

- STR：力量、体能、强行操作、抵抗毒素等。
- DEX：敏捷、反应、闪避、攀爬、潜行、平衡等。
- WIL：意志与社交影响，包括说服、欺骗、审问、威吓、魅惑、操纵法术等。

属性用于对应风险的 Save；不要把属性值解释成技能熟练度，也不要从其他系统引入技能列表。

### CR-SAVE｜属性豁免 — VERIFIED_CORE

**触发**：角色做出的选择存在真实风险，且可能产生负面结果；或双方对抗/协同行动需要确定风险承担者。

**输入**：行动情境、风险、适当属性、执行豁免的角色。

**执行**：
1. 先判断行动在虚构情境中是否可行，以及准备、工具、时间或能力是否足以直接解决。
2. 无真实风险或结果确定时，不掷 Save。
3. 若确有风险，选择与风险性质对应的 STR/DEX/WIL。
4. 掷 d20；结果 ≤ 属性成功，> 属性失败；1 恒成功，20 恒失败。
5. 对抗时由更处于风险中的一方 Save；共同完成行动时通常由相关属性较低、风险较高者 Save。
6. 依据成功/失败及既定情境落实后果；不自动将失败解释为“什么也没发生”。

**输出**：成功/失败、虚构后果、时间/资源/位置/状态变化。

**禁止**：把每次观察、知识回忆、社交对话或所有不确定性都转成 Save；套用其他系统的技能检定、难度 DC、优势骰或失败等级。

来源：Core Rules / Saves；Warden's Guide / Saves、Variable Difficulty。

### CR-INFO｜信息与知识 — VERIFIED_CORE

- 主动提供角色基本感官可感知的相关信息；明显可见、可听、可闻的内容不以检定设门槛。
- 角色知识由背景、经历、关系、教育和已获得信息支撑。没有依据时不凭空知道。
- GM 掌握的秘密不自动成为 PC 或 NPC 的知识。
- 对不确定的知识机会，可按 Warden's Guide 的适用指引使用 Die of Fate；不得把它改造成通用知识技能检定。
- 描述应区分：角色直接观察到的事实、可合理推断的内容、尚未获知的事实。

来源：Warden's Guide / Knowledge and Perception。

## 3. 资源与恢复

### CR-HP｜HP 恢复 — VERIFIED_CORE

- PC 在安全、舒适的环境中会恢复 HP；短暂休息并饮水也可恢复失去的 HP，但此举可能使队伍暴露于危险。
- 地城中可以花费一个 Turn 休息恢复全部 HP，但需要光源和安全地点；存在或迫近的危险时无法安全休息。
- 地城休息不恢复 Fatigue；地城内不能安全进行 Make Camp。
- HP 是 Hit Protection，不等同身体健康，也不能替代 STR/DEX/WIL。

### CR-ATTR-REC｜属性恢复 — VERIFIED_CORE

- 属性损失通常可通过一周休息恢复，并由治疗者或其他适当专业支持协助。
- 官方允许部分治疗服务免费；魔法或更快捷的恢复方式可能收费。
- Marketplace 列有 Medical Healing：50 gp。该价格是官方集市服务价，不应被解释为所有属性损伤、所有伤势或所有地区都必然能以 50 gp 完整治愈。
- 具体服务能否处理某种伤势、是否需要特殊材料/专家、费用是否变化，仍由对应条目与虚构情境决定。
- HP 恢复与属性恢复是两套不同程序；短暂休息饮水或地城 Turn Rest 不自动恢复属性。

来源：Player's Guide / Core Rules / Healing & Recovery；Marketplace / Upkeep & Recovery。

### CR-FAT｜Deprived 与 Fatigue — VERIFIED_CORE

**触发**：角色缺少食物、休息等关键需求；或法术/事件/特定规则要求增加 Fatigue。

**执行**：
1. 记录 Deprived 状态及起始时间/持续时长。
2. Deprived 超过一天后，按每一天增加 1 个 Fatigue。官方没有规定必须在何种具体钟点/Watch 边界执行周期 tick；Workbench 可以用 deprived_since 与唯一 fatigue_tick_id 防止漏算/重复算，但具体 tick 边界属于 GM_INFERENCE / 运行时记账约定，不得宣称为官方明文。
3. 每个 Fatigue 占用 1 个库存格。
4. Deprived 期间不能恢复 HP、属性，也不能清除库存中的 Fatigue。
5. 若被迫增加 Fatigue 而无空格，必须丢弃一件库存物品。
6. Fatigue 持续到角色能够恢复（例如在安全地点获得完整夜间休息）；按实际恢复条件移除。

**状态分离**：Deprived 是需求未满足状态；Fatigue 是占用库存格的具体资源负担。两者不可合并为单一疲劳值。

### CR-INV｜库存 — VERIFIED_CORE

- 每名角色最多 10 个库存格；填满全部 10 格时 HP 降至 0，不能超过 10 格。
- 满格造成的 HP=0 记录 hp_zero_cause: inventory_overload，不是伤害，不触发 Scars / Critical Damage。腾出格子只解除超载原因，不自动回填 HP；后续按正常 HP 恢复规则处理。后半句属于 Workbench 状态解释，官方原文只明确“满 10 格时降至 0 HP”。
- 一般物品占 1 格；Bulky 占 2 格；Petty 不占格。
- 背包最多容纳 6 格物品或 Fatigue；物品能否装入及其占格按物品描述与 Warden 对虚构情境的裁定。
- 角色通常只能舒适携带约 4–5 件物品；背包、马匹、车辆、雇工等可改变实际携带能力。
- 价值低于 100gp 的一袋钱币属于 Petty，不占库存格；其他财物按具体物品条目与 Warden 的虚构裁定处理。不可自行将所有钱币统一视为 0 格。
- 口粮按每份 3 次使用记录 uses_remaining；消耗一次减少一次，降至 0 后才移除该份 Ration。不得把一次消耗误记为整份口粮丢失。
- 角色通常从创建时获得一个可容纳最多 6 格物品或 Fatigue 的 Backpack；它是容器容量，不额外创造超过角色 10 格的总负重上限。
- 每次获得、使用、转移、丢弃、损坏或增加 Fatigue，都必须更新账本并重新计算占格与 HP 限制。

来源：Character Creation / Inventory；Core Rules / Deprivation & Fatigue。

### CR-ARM｜Armor — VERIFIED_CORE

- 伤害进入 HP 前，先从伤害骰结果减去目标 Armor。
- 盾牌等提供的防御加值，仅在符合持有/穿戴条件时生效。
- PC、NPC、怪物 Armor 上限为 3。
- 记录 Armor 来源及其是否当前生效；不要把 Armor 直接加到 HP，也不要重复减伤。

## 4. NPC 反应与士气

### CR-REACTION｜Reaction — VERIFIED_CORE

**触发**：遭遇 NPC，且其对 PC/队伍的态度并不明显。

**执行**：Warden 可以选择掷 2d6（官方可选程序）：
- 2：Hostile
- 3–5：Wary
- 6–8：Curious
- 9–11：Kind
- 12：Helpful

结果决定初始反应倾向，不抹除 NPC 的目标、知识、关系、恐惧、资源和处境。Warden 可依据已确立的虚构事实直接裁定；不得把 Reaction 当作强制骰或覆盖 NPC 已有动机。

### CR-MORALE｜Morale — VERIFIED_CORE

- 敌方首次出现伤亡时，相关敌人/群体进行 WIL Save，成功才避免逃跑。
- 敌方失去半数成员时，再次触发。
- 某些群体可使用领袖 WIL 代替成员；孤立敌人在 HP 降至 0 时进行 Save。
- Morale 不影响 PC。
- 记录触发点，避免同一触发事件重复结算；群体结构与特殊怪物规则可能改变适用方式。

## 5. 战斗程序

### CR-COMBAT｜战斗轮 — VERIFIED_CORE

**时间**：每轮约 10 秒。

**首轮**：
1. 战斗开始，确认双方位置、参与者、明显危险和行动意图。
2. 每名 PC 进行 DEX Save 才能在首轮行动；特殊情境、能力、物品或技能可能豁免此要求。
3. 未通过者失去本轮行动。
4. 可行动 PC 一方先声明行动并结算；随后对手方行动。
5. 双方行动结果按规则视为同时发生；不要因叙述先后而让一方自动取消另一方已声明的行动。

**后续轮**：PC 方先行动，再由对手方行动；双方行动结果同时结算。持续到一方被击败或逃离。

每名角色每轮可移动最多 40 ft 并采取最多一个行动；行动可为攻击、施法、第二次移动或其他合理行动。所有行动先声明，再掷骰/结算。

### CR-ATTACK｜攻击与伤害 — VERIFIED_CORE

1. 战斗攻击自动命中；通常不进行命中检定。
2. 先声明双方行动，再按 Cairn 的 side-turn 程序结算；同一方行动结果同时发生。
3. 对每次攻击建立独立伤害事务，调用 CR-DAMAGE-TX。
4. 多名攻击者攻击同一目标：所有伤害骰掷出，只取单个最高结果；不是将伤害相加。双持同理按 CR-MOD。
5. 对 Blast 的每个受影响目标分别建立伤害事务；不得把多个目标的伤害合并为一个事务。
6. 每个事务完成后检查 Scars、Critical Damage、Morale、死亡及其他触发；事件 ID 必须唯一，不能重复结算。

### CR-DAMAGE-TX｜伤害事务与状态提交 — VERIFIED_CORE / WORKBENCH TRANSACTION

本条把官方伤害规则转换为可审计、可恢复、不可重复扣账的单次事务。事务字段和幂等约束属于 Workbench 实现；骰子与伤害后果以 Cairn 2e 为准。

**事务输入**：event_id、target_id、hp_before、str_before、armor_before、damage_roll、攻击修正、适用 Armor、cause、rule_id 与来源定位。

**执行顺序**
1. 确认伤害来源、目标、目标当下 HP/STR/Armor；同一 event_id 若已提交，读取既有结果，不再次扣账。
2. 得到最终伤害骰结果（含 Impaired/Enhanced 等修正）。
3. 仅在适用时扣除 Armor，得到 damage_after_armor；最终伤害不得低于 0。
4. 计算临时值 hp_raw = hp_before - damage_after_armor。hp_raw 只用于分支与溢出计算，不直接作为长期负数 HP 记录。
5. damage_after_armor = 0：HP/STR 不变；记录 no-damage 事务，不触发 Scars 或 Critical Damage。
6. hp_raw > 0：持久化 HP = hp_raw。
7. PC 因本次攻击伤害 hp_raw = 0：持久化 HP = 0，以本次实际 HP 损失量查 CR-SCARS；不进入 Critical Damage。
8. hp_raw < 0：计算 overflow = abs(hp_raw)；先将溢出伤害从 STR 扣除，再持久化 HP = 0。负 HP 仅是计算中间值。
9. STR 扣减后达到或低于 0：持久化 STR = 0 并立即判定 PC 死亡；不再进行 Critical Damage Save。自然 1 不能覆盖 STR 归零死亡。
10. STR 扣减后仍大于 0：立即以新 STR 进行 Critical Damage Save。成功者仍在战斗中但保持降低后的 STR；失败者按 CR-CRITICAL 进入濒死/爬行与救助时限。
11. 提交 HP、STR、条件、Scars、死亡/稳定状态和后续触发；一次事务只能提交一次。

**边界**
- HP 原本为 0 后再次受到正伤害：hp_raw < 0，本次 Armor 后伤害均为溢出；不得再次触发“恰好降至 0”的 Scars。
- 满库存或 Panic 直接把 HP 设为 0：不是伤害事务，不触发 Scars；必须记录 hp_zero_cause。
- 其他非攻击伤害若按具体规则直接扣属性，走相应属性损伤规则，不擅自改走 HP/Scars。
- NPC/怪物的 STR 归零、Critical Damage 失败后果按其官方条目和 Warden 裁定；不得将 PC 结果机械套用到所有生物。
- Armor、伤害来源或目标状态无法核实时，暂停该事务，不得先扣账再补证据。

**输出**：完整中间值、最终 HP/STR、触发规则、状态差分、提交状态与来源分类。

### CR-MOD｜攻击修正 — VERIFIED_CORE

- Impaired：处于明显劣势位置/条件（例如隔着掩体攻击、双手受缚）时，伤害骰改为 d4；徒手攻击恒为 d4。
- Enhanced：处于明显优势位置（例如攻击无助目标或完成大胆战术动作）时，伤害骰改为 d12。
- Blast：影响标注范围内所有目标，对每个受影响角色分别掷伤害；若不确定能影响多少目标，按官方指引掷相关伤害骰确定数量。
- 双持同时攻击：掷两把武器伤害骰，取最高单骰结果。
- 同一次攻击不要叠加互相冲突的 Impaired 与 Enhanced；如情境无法明确，先裁定位置优势/劣势及适用规则，不凭空相互抵消。

### CR-CRITICAL｜Critical Damage — VERIFIED_CORE

**触发**：伤害结算后，目标 HP 低于 0。PC HP 恰好等于 0 时走 CR-SCARS；NPC/怪物的后果依其条目和 Warden 裁定。

**PC 执行**
1. 计算本次伤害溢出值：overflow = damage_after_armor - hp_before，仅当结果大于 0。
2. 将 overflow 从 STR 扣除。
3. 若新 STR 达到或低于 0，将 STR 记为 0 并立即判定死亡；不进行 Save。
4. 若新 STR 大于 0，立即以新 STR 进行 STR Save。
5. 成功：PC 仍可行动，但 STR 已降低；以后每次再次承受 Critical Damage，仍须再次进行 Critical Damage Save。
6. 失败：PC 只能虚弱爬行；若获得援助（例如绷带）则稳定，未获治疗则一小时内死亡。

**状态表达**
- Workbench 持久化 HP = 0；负 HP 只作为计算溢出的临时值，不保留为长期 HP。
- 每次 Critical Damage 保存 event_id、HP_before、Armor 后伤害、overflow、STR_before/after、Save 骰值和结果。
- 失败后的爬行/稳定/死亡时限作为持续条件记录；救助稳定不自动恢复 HP 或 STR。
- NPC/怪物失败通常由 Warden 按官方规则与其特殊能力裁定死亡或其他效果；不要套用 PC 的全部后果。

**关键边界**：先扣除溢出伤害，再以新 STR 检定；STR 归零死亡优先于 Save；不能用旧 STR 掷骰；不能把 HP 恰好 0 误判为低于 0。

### CR-SCARS｜Scars — VERIFIED_CORE

**触发**：PC 受到伤害后，HP 恰好降至 0。仅仅因库存满格、Panic 等非伤害规则效果被降至 0 HP，不自动触发 Scars。

- 依据本次攻击造成的 HP 损失量（Armor 减伤后的实际 HP 损失）查 Scars 表，而不是按攻击伤害骰原始结果或角色最大 HP 查表。
- 结果可能造成伤疤、失衡、击倒、骨折、疾病、头部创伤等；每项后续恢复/属性变化按官方表格逐项执行。
- Scars 的 1–12 项结果已在下方做结构化自写摘要；如遇原文更新或对具体措辞有争议，回查官方 2e Scars 表。
- Scars 结算后仍须检查角色状态与后续行动限制。

#### Scars 结果速查（自写摘要）

| HP Lost | 结果与后续处理 |
|---:|---|
| 1 | **Lasting Scar**：掷 1d6 决定伤疤部位（颈、手、眼、胸、腿、耳）；再掷 1d6，若高于最大 HP，则将最大 HP 提高到新结果。 |
| 2 | **Rattling Blow**：角色眩晕、惊魂未定，描述如何重新集中；掷 1d6，若高于最大 HP，则将最大 HP 提高到新结果。 |
| 3 | **Walloped**：角色被击飞、倒地、喘不过气；Deprived 数小时，休息数小时后掷 1d6 并增加最大 HP。 |
| 4 | **Broken Limb**：掷 1d6 决定骨折部位（1–2 腿、3–4 臂、5 肋骨、6 头骨）；治愈后掷 2d6，若高于最大 HP，则将最大 HP 提高到新结果。 |
| 5 | **Diseased**：感染疾病；痊愈后掷 2d6，若高于最大 HP，则将最大 HP 提高到新结果。 |
| 6 | **Reorienting Head Wound**：掷 1d6 决定受影响属性（1–2 STR、3–4 DEX、5–6 WIL）；掷 3d6，若高于该属性当前值，则将该属性提高到新结果。 |
| 7 | **Hamstrung**：角色几乎无法移动，直到获得严肃治疗与休息；恢复后掷 3d6，若高于最大 DEX，则将最大 DEX 提高到新结果。 |
| 8 | **Deafened**：角色失聪，直到获得非凡援助；无论如何都进行 WIL Save，成功则最大 WIL 增加 1d4。 |
| 9 | **Re-brained**：角色精神/心理状态发生剧烈变化；掷 3d6，若高于最大 WIL，则将最大 WIL 提高到新结果。 |
| 10 | **Sundered**：由 Warden 指定一个肢体被撕裂、残废或失去功能；随后进行 WIL Save，成功则最大 WIL 增加 1d6。 |
| 11 | **Mortal Wound**：角色 Deprived 且失去行动能力；若一小时内未获治疗则死亡。恢复后掷 2d6，将结果设为新的最大 HP。 |
| 12 | **Doomed**：角色侥幸存活，但下一次 Critical Damage Save 若失败便会惨死；若成功，掷 3d6，若高于最大 HP，则将最大 HP 提高到新结果。 |

**最大值提升规则**：表格中“若骰值高于最大值，则采用新结果”表示提高相应最大值；若未超过，则不提高。伤疤/伤势的持续限制仍须按具体结果处理。

### CR-ATTR-LOSS｜属性损伤 — VERIFIED_CORE

- PC 在战斗外受到伤害时，通常直接损失某项属性（通常 STR），而不是 HP。
- STR 降至 0：死亡。
- DEX 降至 0：瘫痪。
- WIL 降至 0：神志错乱（delirious）。
- DEX/WIL 完全损失会使角色无法行动，直到通过长期休息或非常规手段恢复。

### CR-DEATH｜死亡与接替 — VERIFIED_CORE

角色死亡后，玩家创建新角色或接管一名 Hireling；新角色立即加入队伍，以减少等待时间。具体加入方式需与当前冒险地点和虚构情境协调。

### CR-DETACH｜Detachments — VERIFIED_CORE

- 大量相似战斗者可作为一个 Detachment 处理。
- Detachment 承受 Critical Damage 时被击溃或显著削弱；STR 降至 0 时被摧毁。
- 个体攻击 Detachment 时为 Impaired（Blast 除外）；Detachment 攻击个体时为 Enhanced 并造成 Blast 伤害。
- 需核对 Detachment 的具体数据与场景适用条件；不可把普通多人攻击随意改成 Detachment。

### CR-RETREAT｜Retreat — VERIFIED_CORE

从危急情境中逃跑需要成功 DEX Save，并且必须存在可抵达的安全目的地。没有安全目的地时，不能仅靠成功 Save 宣称逃脱。

### CR-RANGED｜远程攻击 — VERIFIED_CORE

- 远程武器可攻击距离足够近、能看清其眼白的敌人。
- 对特别远的目标，攻击为 Impaired。
- 除非物品/场景另有规定，不追踪普通弹药消耗。

### CR-PANIC｜恐慌 — VERIFIED_CORE

**触发**：角色被敌人包围、陷入黑暗，或直面其最深恐惧等情境。

- 通常进行 WIL Save，以避免失控并陷入 Panicked。
- Panicked 角色 HP 降至 0；战斗首轮不能行动，所有攻击均为 Impaired。
- Panicked 角色必须在自己回合花费一个行动并通过 WIL Save，才能克服恐慌。
- Panic 造成的 HP=0 是状态效果，不是伤害；不触发 Scars，也不进行 Critical Damage。
- 克服 Panic 只移除 Panicked 条件；官方条文没有规定同时恢复 HP。Workbench 不自动回填先前 HP，HP 保持 0，之后依正常 HP 恢复规则处理。该状态处理标记为 GM_INFERENCE，不得伪装成官方额外条文。
- 记录 hp_zero_cause: panic、Panic 起止事件与克服检定；防止跨 Session 恢复时重复施加 HP=0 或重复执行克服检定。

### CR-TRAPS｜陷阱 — VERIFIED_CORE

- 谨慎行动的角色应获得足以避免触发陷阱的所有可观察信息；不得把明显线索藏在感知检定之后。
- 未察觉且按虚构情境会触发陷阱时，按实际情况结算；若情境没有明确决定结果，通常有 2-in-6 机会触发。
- 陷阱伤害通常扣除属性（一般 STR 或 DEX），而非 HP。Armor 仅在虚构情境中确实适用时减伤；例如盾牌不能防护有毒气体。
- 具体陷阱仍以模组/场景条目为准。

### CR-LIGHT｜光源 — VERIFIED_CORE

- 火把及其他辐射光源照亮约 40 ft；更远处只能看见物体的模糊轮廓。
- 火把可点燃 3 次，之后永久损坏；火把持续燃烧，直到角色或环境将其熄灭。
- 提灯每罐灯油可重新点燃 6 次；提灯及油罐占格按具体物品条目记录。
- 无光源角色可能陷入 Panic，直到处境改善。
- 风、水、尘土等环境条件可能熄灭火把；记录剩余点燃次数和当前是否点燃。

### CR-MAGIC｜Spellbook 施法 — VERIFIED_CORE

- Spellbook 包含一个法术，占 1 个库存格；法术书通常通过探索地点/遗迹取得，不可轻易抄录或自行制作。
- 施法者必须双手持有 Spellbook 并大声朗读其中内容，施法后向库存增加 1 Fatigue。
- 有时间且处于安全环境时，PC 可以增强法术效果（例如影响多个目标或提高威力），无需额外成本。
- 若 PC Deprived 或处于危险中（例如战斗），Warden 可以要求 WIL Save 以避免施法不良后果。失败后果应与法术预期效果相称，可能包括增加 Fatigue、毁坏 Spellbook、受伤甚至死亡。
- 法术具体效果、限制和额外属性以 Spellbook 条目为准；不得只凭法术名称推断。

### CR-SCROLL｜卷轴 — VERIFIED_CORE

- Scroll 属于 Petty，不占库存格。
- 使用卷轴不增加 Fatigue。
- 使用一次后卷轴消失。

### CR-RELIC｜遗物 — VERIFIED_CORE

- Relic 是带有法术或特殊力量的物品；不会因使用而增加 Fatigue。
- 通常有有限使用次数与 Recharge 条件；每次使用按该 Relic 自身条目结算，必须记录剩余次数及充能条件。

### CR-HIRELING｜Hirelings — VERIFIED_CORE

- 雇工可凭独特技能、知识与训练协助远征；应按其角色与具体人物设定处理，不将其视为无差别的额外 PC。
- 标准创建：从 Marketplace 的 Hirelings 表选择适当角色；各属性分别掷 3d6，HP 掷 1d6；赋予符合其身份/岗位的装备；再掷 Character Traits 表补充人物特征。
- 替代创建：选择 Character Creation 中合适的 Background 和姓名，按该背景流程生成；随后掷/选择 Rations、GP、Attributes、HP 与年龄。
- Marketplace 官方每日工资（GP/day）：Alchemist 30；Animal Handler 5；Blacksmith 15；Bodyguard 10；Local Guide 5；Lockpick 10；Navigator 10；Sailor 5；Scholar 20；Tracker 5；Trapper 5；Veteran Bodyguard 20。
- 这些岗位名称与工资已由官方 Marketplace 明确；岗位具体能力、装备和实际可提供的服务须结合人物与情境确定。
- 核心规则没有给出适用于所有 Hirelings 的统一忠诚度、士气或叛逃检定流程。不得自行补入通用 Loyalty/Morale 数值；具体雇佣关系、报酬、风险与行为按人物动机和虚构情境裁定。

来源：Player's Guide / Core Rules / Hirelings；Marketplace / Hirelings (per day)。

### CR-DOF｜Die of Fate — VERIFIED_CORE

可选工具：当事件结果不确定，或需要模拟偶然性时掷 1d6。4+ 通常有利于 PC，3- 通常不利。它是 Warden 的可选不确定性工具，不替代明确规则、Save 或模组指定的骰表。

## 6. 探索程序

### EX-DUNGEON｜地城探索循环 — VERIFIED_CORE

“Dungeon”可指任何危险地点，不限地下城。

每个 Cycle：
1. **Describe**：描述环境、位置关系、可见物、即时危险和进行中的威胁；明显信息免费提供。谨慎观察附近门窗/墙体时，可根据听觉、嗅觉等线索判断附近生命迹象与危险。
2. **Declare**：玩家声明角色移动与行动；每个角色通常可移动至多一个光源照明周界（约 40 ft）并做一个行动。快速移动可覆盖至三倍距离，但会提高触发 Dungeon Event 的风险。
3. **Resolve**：主持人同时处理各角色行动与已经在进行的行动；需要时调用对应专属规则。部分行动可持续多个 Cycle。
4. **Record**：记录时间、位置、光源、物品、Fatigue、条件及其他资源变化。
5. **Event Check**：若满足 EX-DUNGEON-EVENT 条件，掷/查 Dungeon Events。
6. 进入下一个 Cycle。

**Search 行动**：角色可花费一个 Turn，彻底搜索区域中的一个物件或地点，揭示相关隐藏宝藏、陷阱、密门等。大型房间或复杂地形可能需要数个 Turn 才能搜完。搜索需要时间，但通常比盲目推进更安全。响亮或显眼的行动也可能直接引起地城居民遭遇；按虚构情况处理，不必机械地把每次声音都变成一次事件表掷骰。

### EX-DUNGEON-EVENT｜地城事件 — VERIFIED_CORE

当队伍：
- 在同一房间/地点花费超过一个 Dungeon Cycle；
- 快速或草率穿越地点；
- 进入新区域、层级或分区；
- 制造响亮骚动；

则掷 1d6 查 Dungeon Events：
1 Encounter（查遭遇表，可能敌对，必要时查 Reaction）
2 Sign（线索、踪迹、痕迹、遗弃巢穴、气味、受害者等）
3 Environment（环境变化或危险升级）
4 Loss（火把熄灭、持续法术失效等；必须先解决 Loss 的具体效果，才能继续）
5 Exhaustion（必须选择：休息并立即再次掷 Dungeon Events、增加 Fatigue、或消耗一份 Ration）
6 Quiet（暂时无人打扰，当前安全）

**后续程序**
- Loss 必须指出具体失效资源/效果、受影响对象和已完成的状态差分。未解决前不进入下一 Cycle。
- Exhaustion 的三个选项是本条规则给出的处理路径。选择休息会触发一个新的独立 Dungeon Event Roll；若再次得到 Exhaustion，建立新的事件并继续处理。
- 父事件与递归产生的子事件使用不同 event_id；选择、资源扣减、额外掷骰和结果均逐项记录，避免重复扣账。
- 事件结果结合地点与既有事实解释；不把事件表当作剧情强制推进器，也不因玩家只问问题而机械重复掷骰。

### EX-WILDERNESS｜荒野探索 — VERIFIED_CORE

**Watch 基础**：一天分为 Morning、Afternoon、Night 三个各 8 小时的 Watches。每名角色每 Watch 选择一个 Wilderness Action；队伍分开行动时，各组视为独立实体。

**旅行时间**：从当前 Point 到目标 Point 的耗时由路径距离、路径类型、地形、天气和队伍状态共同决定。将对应惩罚相加，换算为 Watches；水路参考周边地形难度，特别广阔的地形可额外增加最多 +2 Watches。当前速查未收录完整路径/天气修正表，具体行程必须查官方 Procedures 表格或 Campaign Quick Reference。

- 路径：Road 无额外 Watch/迷路风险；Trail +1 Watch、2-in-6 迷路；Wilderness +2 Watches、3-in-6 迷路。
- 距离：Short +1 Watch；Medium +2 Watches；Long +3 Watches。
- 地形：Easy +0；Tough +1 Watch；Perilous +2 Watches。
- 天气：每天按季节掷天气表；连续两次出现 Extreme 则变为 Catastrophic。Nice/Fair 有利于旅行；Unpleasant：增加 Fatigue 或旅程 +1 Watch；Inclement：增加 Fatigue 或 +1 Watch，且地形难度提高一级；Extreme：增加 Fatigue 并 +1 Watch，且地形难度提高一级；Catastrophic 通常无法旅行。

**每日天气表（按季节掷 1d6）**：

| d6 | Spring | Summer | Fall | Winter |
|---:|---|---|---|---|
| 1 | Nice | Nice | Fair | Fair |
| 2 | Fair | Nice | Fair | Unpleasant |
| 3 | Fair | Fair | Unpleasant | Inclement |
| 4 | Unpleasant | Unpleasant | Inclement | Inclement |
| 5 | Inclement | Inclement | Inclement | Extreme |
| 6 | Extreme | Extreme | Extreme | Extreme |

连续两天掷出 Extreme，天气转为 Catastrophic。

**行动与事件**：每个 Watch 中，队伍成员分别选择一项 Wilderness Action；Travel 通常由全队共同执行，视为一次队伍行动。Warden 叙述结果后掷 Wilderness Events，再处理玩家响应和状态变化。常用行动包括 Travel、Explore、Supply、Make Camp。

- Travel：揭示沿途可见地点/地貌；队伍掷 1d6 判断迷路，风险由路径难度、地图、技能和向导调整。迷路后可能要额外花费一个 Wilderness Action 找回路线，否则抵达路线上的下一 Point。
- Explore：一名或多名角色搜索大片区域、侦察或谨慎行动，发现地点或地貌；即使区域已探索，离开仍需 Travel。
- Supply：一名或多名角色狩猎、捕鱼、采集，基础获得 1d4 Rations（每份 3 次使用）；每增加参与者，收获骰可逐级提高（如 d4→d6），最高 d12；相关经验或装备也可能提高收获。也可能通过民居/村庄花费金币与一个完整 Watch 补给。
- Make Camp：每名角色及其坐骑各消耗一份 Ration；安排守夜轮值。小队人数少时，可能需要冒无人守夜风险或跨多日轮换睡眠。成功休息者移除全部 Fatigue。

**夜晚与睡眠**：夜间旅行应在 Wilderness Events 表上掷两次。每天最后一个 Watch 通常用于 Make Camp。若跳过 Make Camp，每名角色增加一份 Fatigue 并陷入 Deprived；睡眠不足时旅行，地形难度提高一级。超出轻微干扰的睡眠中断可能取消睡眠收益。

**单人队伍警告**：不能假设一名 PC 可以安排完整守夜轮值。明确处理无人守夜、分段睡眠或聘用/雇用同伴的选择与后果；不替玩家自动选择。

### EX-WILDERNESS-EVENT｜荒野事件 — VERIFIED_CORE

每次 Wilderness Cycle 后按程序掷 1d6；夜间旅行在 Wilderness Events 表上掷两次：
1 Encounter（查对应地形/地点遭遇表；适用时可掷 Reaction）
2 Sign（发现线索、踪迹、附近遭遇/地点/隐藏特征的信息）
3 Environment（天气或地形变化）
4 Loss（遭遇资源、时间或努力成本；按具体情境呈现选择与差分）
5 Exhaustion（遭遇障碍，可能需要额外时间/额外 Wilderness Action，或增加 Fatigue）
6 Discovery（发现食物、宝藏或其他有用资源；Warden 也可揭示区域主要特征）

**与 Dungeon Events 的区别**
- Wilderness Loss 按资源、时间或努力成本处理；不套用 Dungeon Loss 的固定表达，除非具体情境本身要求暂停。
- Wilderness Exhaustion 是旅途障碍；根据虚构情境落实额外时间、额外 Action 或 Fatigue，不套用 Dungeon Exhaustion 的三选一与递归掷骰程序。
- 每次事件骰记录独立 Event Roll ID；夜间两次掷骰是两个独立事件，不因 Handoff 重掷。
- Discovery 必须与地图、季节、地貌和已确立世界事实相容。

## 7. 状态账本最小字段

每名 PC 与明确登记的 L3 NPC 至少按需维护：

- 身份：名称、PC/NPC、所属队伍、当前地点。
- 属性：STR/DEX/WIL 当前值与最大值（若适用）。
- HP：当前/最大 HP。
- Armor：数值、来源、当前是否生效。
- Inventory：物品、占格、Bulky/Petty、背包/容器归属、空格。
- Fatigue：数量、占格、来源、清除条件。
- Deprivation：当前是否 Deprived、起始时间、需求缺口。
- 伤疤/条件：效果、来源、持续时间、解除条件。
- 时间：当前游戏内日期/Watch/Turn/Combat Round。
- 资源：口粮、光源及使用次数、金钱、工具、雇工/坐骑等。
- 事件：待结算触发、已结算触发，防止漏结算或重复结算。

每次行动结束必须执行一次状态差分：**行动前 → 触发规则 → 骰值/结果 → 资源变化 → 行动后**。没有变化也可记录为 no-change，但不得省略关键状态检查。

## 8. 运行时不可推断清单

以下情况必须查对应官方 2e 条目或模组数据：
- Scars 表具体结果及其后续恢复；
- 特定法术、遗物、武器、护甲、怪物、雇工或 Detachment 的专属效果：先查 OFFICIAL_CATALOG_INDEX.md 的本地快照；模组专属对象则查对应 Campaign 的 SOURCE / GM-only Prep；仅在本地缺项、上游更新或来源冲突时再联网回查；
- 特定地图路线的实际距离、沿途地形/天气变化、向导/地图/坐骑等具体修正，以及单人队伍的守夜选择；核心路径、距离、地形和天气规则已本地化，具体地点数据仍依地图/模组而定；
- 属性恢复的具体服务、时间、费用与特殊治疗；
- 模组自定义程序、随机表和遭遇数量；
- 本文件标记 PARTIAL 或 MODULE_DEPENDENT 的项目。
- 具体怪物、法术书、遗物、NPC 生成表与背景专属数据，优先查阅 [OFFICIAL_CATALOG_INDEX.md](./OFFICIAL_CATALOG_INDEX.md) 指向的本地官方快照；不要把具体条目只留作在线回查。
- Campaign 专属 NPC、遭遇、陷阱、地点、事件时钟与特殊程序，优先查该 Campaign 的模块 SOURCE 归档和 GM-only Reference Index；不得混入系统级通用目录。

不得把“每次都查原文”作为常态，也不得把“已经有速查”当成可以忽略原文更新的理由。规范化条目是运行入口；官方 2e 是权威底层。
