# Cairn 2e 核心规则运行手册

> 规则绑定：`system_id: cairn`；`ruleset_version: Cairn Second Edition`
> 状态：runtime normalization v0.1；供候选系统测试调用，不代表已完成全部章节核验。
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
| CR-ATTR-REC | 属性恢复 | 属性损伤后治疗/休养 | PARTIAL |
| CR-FAT | Deprived / Fatigue | 食物、睡眠或其他关键需求缺失 | VERIFIED_CORE |
| CR-INV | 库存与负重 | 携带、获得、丢弃物品/Fatigue | VERIFIED_CORE |
| CR-ARM | Armor | 伤害结算前 | VERIFIED_CORE |
| CR-REACTION | NPC Reaction | NPC 态度不明确 | VERIFIED_CORE |
| CR-MORALE | 敌方士气 | 首次出现伤亡、敌方损失半数；孤立敌人 HP 到 0 | VERIFIED_CORE |
| CR-COMBAT | 战斗轮与行动 | 战斗开始及每轮 | VERIFIED_CORE |
| CR-ATTACK | 攻击与伤害 | 攻击行动结算 | VERIFIED_CORE |
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
| CR-HIRELING | Hirelings | 招募/创建雇工 | PARTIAL |
| CR-DOF | Die of Fate | 事件结果不确定且需随机判断 | VERIFIED_CORE |
| EX-DUNGEON | 地城探索循环 | 危险地点中的探索行动 | VERIFIED_CORE |
| EX-DUNGEON-EVENT | 地城事件 | 达到事件触发条件 | VERIFIED_CORE |
| EX-WILDERNESS | 荒野探索与 Watches | 野外旅行/探索 | PARTIAL |
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

- 短暂休息并饮水可恢复失去的 HP；此举可能使队伍暴露于危险。
- 地城中可以花费一个 Turn 休息恢复全部 HP，但需要光源和安全地点；存在或迫近的危险时无法安全休息。
- 地城休息不恢复 Fatigue；地城内不能安全进行 Make Camp。
- HP 是 Hit Protection，不等同身体健康，也不能替代 STR/DEX/WIL。

### CR-ATTR-REC｜属性恢复 — PARTIAL

属性损失通常需要一周休息，并由治疗者或其他适当专业支持；具体恢复服务、费用、魔法或特殊来源依场景/规则条目而定。正式裁定前需核对对应治疗来源。不得把 HP 恢复套用为属性恢复。

### CR-FAT｜Deprived 与 Fatigue — VERIFIED_CORE

**触发**：角色缺少食物、休息等关键需求；或法术/事件/特定规则要求增加 Fatigue。

**执行**：
1. 记录 Deprived 状态及起始时间/持续时长。
2. Deprived 超过一天后，按每一天增加 1 个 Fatigue。
3. 每个 Fatigue 占用 1 个库存格。
4. Deprived 期间不能恢复 HP、属性，也不能清除库存中的 Fatigue。
5. 若被迫增加 Fatigue 而无空格，必须丢弃一件库存物品。
6. Fatigue 持续到角色能够恢复（例如在安全地点获得完整夜间休息）；按实际恢复条件移除。

**状态分离**：Deprived 是需求未满足状态；Fatigue 是占用库存格的具体资源负担。两者不可合并为单一疲劳值。

### CR-INV｜库存 — VERIFIED_CORE

- 每名角色最多 10 个库存格；满 10 格时 HP 降至 0，不能超过 10 格。
- 一般物品占 1 格；Bulky 占 2 格；Petty 不占格。
- 背包最多容纳 6 格物品或 Fatigue；物品能否装入及其占格按物品描述与 Warden 对虚构情境的裁定。
- 角色通常只能舒适携带约 4–5 件物品；背包、马匹、车辆、雇工等可改变实际携带能力。
- 价值低于 100gp 的一袋钱币属于 Petty，不占库存格；其他财物按具体物品条目与 Warden 的虚构裁定处理。不可自行将所有钱币统一视为 0 格。
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

**执行**：掷 2d6：
- 2：Hostile
- 3–5：Wary
- 6–8：Curious
- 9–11：Kind
- 12：Helpful

结果决定初始反应倾向，不抹除 NPC 的目标、知识、关系、恐惧、资源和处境。态度明确或既有事实已决定反应时，不为随机而随机。

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
2. 掷武器伤害骰。
3. 应用 Impaired/Enhanced 等攻击修正。
4. 减去目标当前 Armor（最低造成伤害按具体规则处理；不得自行制造负伤害）。
5. 伤害扣除目标 HP。
6. 检查 HP 是否恰好降至 0 或低于 0，并调用 CR-SCARS 或 CR-CRITICAL。
7. 更新 HP、属性、伤疤、状态及相关士气触发。

多名攻击者攻击同一目标：所有伤害骰掷出，只取单个最高结果；不是将伤害相加。所有行动须先声明再结算。

### CR-MOD｜攻击修正 — VERIFIED_CORE

- Impaired：处于明显劣势位置/条件（例如隔着掩体攻击、双手受缚）时，伤害骰改为 d4；徒手攻击恒为 d4。
- Enhanced：处于明显优势位置（例如攻击无助目标或完成大胆战术动作）时，伤害骰改为 d12。
- Blast：影响标注范围内所有目标，对每个受影响角色分别掷伤害；目标数量不明时按规则指引处理。
- 双持同时攻击：掷两把武器伤害骰，取最高单骰结果。
- 同一次攻击不要叠加互相冲突的 Impaired 与 Enhanced；如情境无法明确，先裁定位置优势/劣势及适用规则，不凭空相互抵消。

### CR-CRITICAL｜Critical Damage — VERIFIED_CORE

**触发**：伤害结算后，目标 HP 低于 0。HP 恰好等于 0 不触发本流程，PC 改走 CR-SCARS。

**执行**：
1. 计算溢出伤害：本次伤害超过目标剩余 HP 的部分。
2. 将溢出伤害从目标 STR 扣除。
3. 以新的 STR 立即进行 STR Save。
4. 成功：目标仍在战斗中，但 STR 已降低；以后每次再次承受 Critical Damage，仍须再次进行 Critical Damage Save。
5. 失败：PC 只能虚弱爬行；若获得援助（例如绷带）则稳定，未获治疗则一小时内死亡。NPC/怪物失败通常由 Warden 按规则裁定为死亡；特定敌人能力可能触发额外效果。

**关键边界**：先扣除溢出伤害，再以新 STR 检定。不能用旧 STR 掷骰；不能把 HP 恰好 0 误判为低于 0。

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
- 这里的 HP=0 是恐慌规则直接造成的状态变化，不是伤害造成的 HP 归零，因此不触发 Scars。官方条目没有明确说明恐慌解除时是否恢复先前 HP；运行时不得擅自恢复，需标记为 `GM_INFERENCE / unresolved`，并按正常 HP 恢复规则处理后续恢复。

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

### CR-HIRELING｜Hirelings — PARTIAL

雇工可凭其独特技能、知识和训练协助冒险。创建方式包括从 Marketplace 的 Hirelings 表选角色，或从背景生成程序构建；属性各掷 3d6，HP 掷 1d6，并按身份赋予装备及人物特征。具体工资、忠诚、角色表和装备必须查 Marketplace 对应条目，不在此臆造。

### CR-DOF｜Die of Fate — VERIFIED_CORE

可选工具：当事件结果不确定，或需要模拟偶然性时掷 1d6。4+ 通常有利于 PC，3- 通常不利。它是 Warden 的可选不确定性工具，不替代明确规则、Save 或模组指定的骰表。

## 6. 探索程序

### EX-DUNGEON｜地城探索循环 — VERIFIED_CORE

“Dungeon”可指任何危险地点，不限地下城。

每个 Cycle：
1. **Describe**：描述环境、位置关系、可见物、即时危险和进行中的威胁；明显信息免费提供。
2. **Declare**：玩家声明角色移动与行动；每个角色通常可移动至多一个光源照明周界（约 40 ft）并做一个行动。快速移动可覆盖至三倍距离，但会提高触发 Dungeon Event 的风险。
3. **Resolve**：主持人同时处理各角色行动与已经在进行的行动；需要时调用对应专属规则。
4. **Record**：记录时间、位置、光源、物品、Fatigue、条件及其他资源变化。
5. **Event Check**：若满足 EX-DUNGEON-EVENT 条件，掷/查 Dungeon Events。
6. 进入下一个 Cycle。

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
4 Loss（光源熄灭、持续法术失效等损失/后果）
5 Exhaustion（休息并额外触发事件、增加 Fatigue 或消耗口粮，按规则/情境选择）
6 Quiet（暂时无人打扰，当前安全）

事件结果必须结合地点与既有事实解释。不要把事件表当作剧情强制推进器。触发条件需逐项记录，不能漏掷，也不能因玩家只问问题就机械地重复掷骰。

### EX-WILDERNESS｜荒野探索 — PARTIAL

**Watch 基础**：一天分为 Morning、Afternoon、Night 三个各 8 小时的 Watches。每名角色每 Watch 选择一个 Wilderness Action；队伍分开行动时，各组视为独立实体。

**旅行时间**：从当前 Point 到目标 Point 的耗时由路径距离、路径类型、地形、天气和队伍状态共同决定。将对应惩罚相加，换算为 Watches；水路参考周边地形难度，特别广阔的地形可额外增加最多 +2 Watches。当前速查未收录完整路径/天气修正表，具体行程必须查官方 Procedures 表格或 Campaign Quick Reference。

- 路径：Road 无额外 Watch/迷路风险；Trail +1 Watch、2-in-6 迷路；Wilderness +2 Watches、3-in-6 迷路。
- 距离：Short +1 Watch；Medium +2 Watches；Long +3 Watches。
- 地形：Easy +0；Tough +1 Watch；Perilous +2 Watches。
- 天气：每天按季节掷天气表；连续两次出现 Extreme 则变为 Catastrophic。Unpleasant：增加 Fatigue 或旅程 +1 Watch；Inclement：增加 Fatigue 或 +1 Watch，且地形难度提高一级；Extreme：增加 Fatigue 并 +1 Watch，且地形难度提高一级；Catastrophic 通常无法旅行。

**行动与事件**：每个 Watch 中，队伍成员分别选择一项 Wilderness Action；Travel 通常由全队共同执行，视为一次队伍行动。Warden 叙述结果后掷 Wilderness Events，再处理玩家响应和状态变化。常用行动包括 Travel、Explore、Supply、Make Camp。

- Travel：揭示沿途可见地点/地貌；队伍掷 1d6 判断迷路，风险由路径难度、地图、技能和向导调整。迷路后可能要额外花费一个 Wilderness Action 找回路线，否则抵达路线上的下一 Point。
- Explore：一名或多名角色搜索大片区域、侦察或谨慎行动，发现地点或地貌；即使区域已探索，离开仍需 Travel。
- Supply：一名或多名角色狩猎、捕鱼、采集，基础获得 1d4 Rations（每份 3 次使用）；额外参与者可提高骰阶，最高 d12；经验/装备也可能提高收获。
- Make Camp：每名角色及其坐骑各消耗一份 Ration；安排守夜轮值。小队人数少时，可能需要冒无人守夜风险或跨多日轮换睡眠。成功休息者移除全部 Fatigue。

**夜晚与睡眠**：夜间旅行应在 Wilderness Events 表上掷两次。每天最后一个 Watch 通常用于 Make Camp。若跳过 Make Camp，每名角色增加一份 Fatigue 并陷入 Deprived；睡眠不足时旅行，地形难度提高一级。超出轻微干扰的睡眠中断可能取消睡眠收益。

**单人队伍警告**：不能假设一名 PC 可以安排完整守夜轮值。明确处理无人守夜、分段睡眠或聘用/雇用同伴的选择与后果；不替玩家自动选择。

### EX-WILDERNESS-EVENT｜荒野事件 — VERIFIED_CORE

荒野行动循环后按程序掷 1d6：
1 Encounter
2 Sign
3 Environment
4 Loss
5 Exhaustion
6 Discovery

结果含义与地点/地形/模组事实结合。Travel、Explore、Supply、Make Camp 的具体效果、Watch 花费、口粮、守夜和路线修正依赖完整 Wilderness 章节；参照官方 Procedures 页面，不从本摘要推导未列出的数值。

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
- 特定法术、遗物、武器、护甲、怪物、雇工或 Detachment 的专属效果；
- 完整的 Wilderness 路线/地形/天气数值与单人守夜安排；
- 属性恢复的具体服务、时间、费用与特殊治疗；
- 模组自定义程序、随机表和遭遇数量；
- 本文件标记 PARTIAL 或 MODULE_DEPENDENT 的项目。

不得把“每次都查原文”作为常态，也不得把“已经有速查”当成可以忽略原文更新的理由。规范化条目是运行入口；官方 2e 是权威底层。
