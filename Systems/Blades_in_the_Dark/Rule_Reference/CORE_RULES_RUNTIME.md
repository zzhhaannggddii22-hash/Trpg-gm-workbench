# Blades in the Dark｜核心规则运行手册

> system_id: blades_in_the_dark  
> 适用阶段：candidate / 行为验证前  
> 核心来源：Blades in the Dark SRD（中文《暗夜冷锋》译本）；关键流程以官方规则网页及官方 Full Player's Kit v8.2 交叉核验。  
> 本文为原创运行摘要，不是规则书全文，也不替代 Campaign 锁定版本的原文。

本文把常用规则整理成可触发执行的步骤。普通叙事不必逐项扫描；只有触发相应规则时才调用对应章节。

---

## 1. 基本运行约束

1. 只有当前 Campaign 明确绑定 system_id: blades_in_the_dark 和规则版本，才使用本手册正式裁定。
2. 本系统独立于 Triangle Agency、Cairn 等其他规则环境。不得引入其他系统的属性检定、资源、伤害、行动经济或阶段流程。
3. 先确定虚构情境、目标、风险和可能后果，再决定是否掷骰；不能先掷骰再反向编造风险。
4. Blades 的核心 Action Roll 同时处理行动表现与后果风险，但 Position 和 Effect 是两条独立轴：Position 决定风险/后果严重度，Effect 决定行动的影响量。
5. GM 应先说明 Position、Effect 和可能的风险方向，再掷骰。掷骰后与玩家共同描述发生了什么。
6. 规则摘要负责快速执行；版本差异、重要例外、角色/组织特殊能力和不可逆结果应回查完整规则。
7. 不模拟所有 NPC 的每一刻。通过已建立的目标、派系状态、项目钟及 Downtime 的相关行动，让世界产生可追踪变化。

## 2. 骰型与基础结算

系统常用四种骰型：Action Roll、Downtime Roll、Fortune Roll、Resistance Roll。Downtime Roll 不是一套独立的骰子判定规则，而是休整阶段执行具体活动时，使用对应 Action rating 或 Trait 的骰池，按相同的六面骰结果档位结算。

### BLD-DICE-01｜Action Dice

**触发**：角色以某项行动克服危险或麻烦障碍。

- 每个对应 Action rating 点数提供 1d6。
- 骰池为 1d 或更多时，读取最高单颗骰子。
- 0d 或负骰池：掷 2d6 并取较低者；按 SRD 说明不能以此获得 Critical。
- 结果：1–3、4/5、6、Critical（至少两颗 6）。

**关键限制**：行动点数必须对应角色当前在虚构中实际做的事。不能仅因为某行动评级更高就随意选它。

### BLD-DICE-02｜Fortune Roll

**触发**：某个结果不确定，但并非由 PC 进行一次危险/麻烦的主动行动来解决；或要判断 NPC、派系、资产、超自然力量等在当前情境中的表现程度。

- 用最相关的 Trait 作为骰池，例如 Crew Tier、Cohort Quality、超自然 Magnitude 或合适的 Action rating。
- 视重大优势/劣势增减骰。
- 无 Position / Effect。读取最高骰：1–3 表现较差，4/5 混合，6 表现良好，Critical 表现卓越。
- 对抗性 Fortune Roll 可分别掷骰并比较结果。

**不要过度掷骰**：常识、稳定事实、没有实际不确定性的结果直接叙述。只有结果差异会影响当前局势时才需要 Fortune Roll。

### BLD-DICE-03｜Resistance Roll

**触发**：某个具体后果已经发生或即将落到 PC 身上，玩家决定承受还是抵抗。常规时点是 GM 宣布行动后果之后；若敌人/危险在 PC 行动前就拥有压倒性优势（例如剑术高手先一步缴械），GM 可以先宣布该后果并要求 Resistance，再让 PC 继续行动。Resistance 不能在尚无具体威胁/后果时预先掷。

- 由 Consequence 类型确定属性组：Insight、Prowess 或 Resolve。
- 骰池等于该属性组内所有 Action dots 的总数。
- Stress 成本 = 6 - 最高骰结果；Critical 抵抗清除 1 Stress。
- 抵抗总会有效：GM 根据情境决定完全避免后果，或降低其严重程度。
- 同一个 Consequence 只能抵抗一次；多个独立后果可分别抵抗。
- 不得在后果揭示前预掷 Resistance。

### BLD-DICE-04｜骰型分流

| 当前问题 | 使用 |
|---|---|
| PC 进行危险/麻烦行动 | Action Roll |
| 只判断结果大小、NPC/派系表现或随机事实 | Fortune Roll |
| 玩家决定减少/避免已明确的后果 | Resistance Roll |
| 行动明显轻松、没有危险或麻烦障碍 | 不掷骰，直接处理 |

### BLD-DICE-05｜属性组与行动对照

| Attribute | Actions |
|---|---|
| Insight | Hunt、Study、Survey、Tinker |
| Prowess | Finesse、Prowl、Skirmish、Wreck |
| Resolve | Attune、Command、Consort、Sway |

Resistance Roll 使用属性组骰池，即该组内所有 Action dots 的总和；普通 Action Roll 仍只使用玩家选择的单一 Action rating。选择哪一组由后果性质决定：
- **Insight**：因欺骗、误判或理解问题造成的后果；
- **Prowess**：因身体劳累、受伤或身体危险造成的后果；
- **Resolve**：因心理压力、恐惧或意志力考验造成的后果。

## 2-A. Action 与 Attribute 对照

| Attribute | Actions |
|---|---|
| Insight | Hunt、Study、Survey、Tinker |
| Prowess | Finesse、Prowl、Skirmish、Wreck |
| Resolve | Attune、Command、Consort、Sway |

Resistance Roll 使用属性组骰池，即该组内所有 Action dots 的总和；普通 Action Roll 仍只使用玩家选择的单一 Action rating。

## 3. Action Roll（行动骰）

### BLD-ACT-01｜六步执行

1. **目标**：玩家说明角色想得到的具体结果。必要时追问“你想让这次行动具体改变什么？”
2. **Action**：玩家选择符合当前虚构行动的评级。不能脱离正在做的事。
3. **Position**：GM 评估行动处于 Controlled、Risky 还是 Desperate。
4. **Effect**：GM 评估行动的预计影响为 Limited、Standard 或 Great。
5. **奖励骰**：加入合法 Assist、Push Yourself 或 Devil's Bargain。
6. **掷骰与结算**：读取结果档，根据 Position 选择有依据的后果，再按 Effect 处理目标进度；共同叙述行动。

默认 Position 为 Risky（若已经值得掷骰且没有特别情况）。默认 Effect 通常为 Standard，但必须根据行动方法、目标和条件判断。

### BLD-ACT-02｜Position

| Position | 情境 | 4/5 | 1–3 |
|---|---|---|---|
| Controlled | 角色按自己的条件行动，有明显优势 | 可撤回/改换方法；或成功但承受轻微后果 | 可抓住一个 Risky 机会继续；或撤回 |
| Risky | 正面应对危险，通常是默认位置 | 达成目标，但承受一个或多个适当后果 | 事情严重出错；通常失败并承受后果，某些情况下可部分生效 |
| Desperate | 角色越过能力边界，处于严重危险中 | 达成目标，但承受严重后果 | 最坏结果；严重后果和/或失去当前机会 |

Position 不等同于成功率修正，也不改变骰池；它规定不同结果档允许/建议出现的后果严重度。Desperate Action 另会触发对应 Attribute XP。

### BLD-ACT-03｜Effect

| Effect | 常见进度 | 意义 |
|---|---:|---|
| Limited | 1 格 | 只获得有限成果，仍有重要障碍 |
| Standard | 2 格 | 达成符合预期的标准成果 |
| Great | 3 格 | 取得明显超额成果或额外收益 |

这些格数适用于有进度钟的情形；Effect 也可用非数值方式描述成果范围、目标改变或额外好处。因素可能将 Effect 降到 **Zero Effect**（没有实质成果），或提高到 **Extreme Effect**（超过 Great 的成果）。角色能力提供的 +1 Effect 在 GM 完成因素评估后应用；Push Yourself 也可用 2 Stress 换取 +1 Effect。Critical 令 Effect 提高一级。

Effect 因素通常包括：
- **Potency**：某种能力/方法对目标是否特别有效；
- **Quality / Tier**：装备品质、组织/对手层级；
- **Scale**：人数、面积、影响范围、资源量级；
- 具体情境及玩家采取的行动方式。

不得把所有因素简单相加成固定公式。GM 应说明何种因素造成优势/限制以及最终 Effect。

### BLD-ACT-04｜奖励骰

- **Assist**：队友说明如何帮助，得到 +1d；协助者承担 1 Stress。每次 Action Roll 最多一名 Assist。
- **Push Yourself**：每选择一项强推收益，支付 2 Stress：+1d、+1 Effect，或在失能状态下仍采取行动。每项收益在同一次行动中最多选择一次；可同时选择不同收益并分别支付 Stress（例如 +1d 与 +1 Effect 共支付 4 Stress）。
- **Devil's Bargain**：由 GM/其他玩家提出一项真实代价；接受后得到 +1d。代价无论最终骰子结果如何都会发生。玩家可拒绝或商议替代方案。
- **Dice bonus 限制**：Assist 最多提供一个 +1d；另一个 +1d 来源只能在 Push Yourself 与 Devil's Bargain 中选一个。不能用 Push 的 +1d 再叠加 Devil's Bargain 的 +1d。
- **Effect bonus 是另一项收益**：玩家可以接受 Devil's Bargain 获得 +1d，同时支付 2 Stress Push Yourself 获得 +1 Effect；也可以 Push Yourself 同时获得 +1d 与 +1 Effect（支付 4 Stress）。Push 的各项收益每次行动各最多选择一次。角色特殊能力可以改变限制，按能力原文处理。

### BLD-ACT-05｜Consequences（后果类型）

根据当下虚构选择一个或多个适当后果：

1. **Harm**：角色受伤或状态受损。
2. **Complication**：出现麻烦、危机、障碍或推进危险钟。
3. **Reduced Effect**：成果低于预期，Effect 降一级。
4. **Lost Opportunity**：原本的机会消失，需要新方法/新机会。
5. **Worse Position**：接下来处于更危险的位置。

Complication 可表现为立即发生的麻烦，或一个有意义的进度钟；轻微/标准/严重复杂状况通常分别推进危险钟 1/2/3 格。GM 可按当前情势提出一个或多个后果；玩家可以选择抵抗其中一个或多个，每个后果分别处理。不能把每次失败都机械地转成新钟。不可使用“你成功了但目标无事发生”来抹消玩家已赢得的行动成果，除非明确是 1–3 且情境允许行动未能生效。

### BLD-ACT-06｜Position 与 Effect 独立

在任何 Action Roll 之前分别回答：

- “如果你这么做，最危险的地方是什么？” → Position。
- “即使成功，你的做法实际能改变多少？” → Effect。

Position 低不等于 Effect 低；风险高也不代表没有成果。必要时，在 GM 先分别宣告基础 Position 与 Effect 后，玩家可以提出以 Position 换 Effect，或以 Effect 换 Position。例：接受更危险的 Position 换取更大 Effect，或接受更小的 Effect 换取更稳妥的 Position。只有在当前虚构情境说得通时才接受；它不是固定的数值兑换表，也不是 GM 在评估 Effect 因素时提前扣算的修正。

### BLD-ACT-07｜Action Roll 后的叙述

掷骰后，GM 先按结果确认角色已获得的成果范围，再落实后果。玩家和 GM 共同描述现场；GM 对最终结果与后果有裁定权。后果要有情境依据，不得为了制造戏剧性任意追加无关惩罚。

### BLD-ACT-08｜双用行动骰（PC 与 NPC 的对抗）

NPC 通常不为自己的行动单独掷 Action Roll。PC 的 Action Roll 同时解决 PC 行动与当前相关 NPC 行动如何交锋：

- **6**：PC 达成目标并取得其 Effect；PC 胜出当前对抗。
- **4/5**：PC 达成目标并取得其 Effect，但 NPC 也取得其行动效果，因此产生一个或多个后果。
- **1–3**：NPC 在当前交锋中胜出；NPC 的行动效果体现为 PC 承受的后果，PC 目标通常未达成，除非当前情境明确支持部分效果。

这不是说世界中所有 NPC 都永远不掷骰：当 NPC 的独立结果不与 PC 的 Action Roll 直接对抗，且结果真正不确定时，GM 可用 Fortune Roll 判断其表现。

掷骰后，GM 先按结果确认角色已获得的成果范围，再落实后果。玩家和 GM 共同描述现场；GM 对最终结果与后果有裁定权。后果要有情境依据，不得为了制造戏剧性任意追加无关惩罚。

## 4. Consequence、Resistance 与 Armor

### BLD-CNS-01｜Harm 等级

| 等级 | 通常影响 |
|---|---|
| Level 1 | 轻伤；相关行动受到 Reduced Effect |
| Level 2 | 中度伤害；相关行动 -1d |
| Level 3 | 严重伤害；角色失能，未经帮助通常无法行动，除非 Push Yourself 继续行动 |
| Level 4 | 致命伤害；若未被 Resistance 避免，角色死亡 |

受伤按角色卡 Harm 栏登记。若某等级栏已满，必须把伤害记入上一等级栏；若 Level 3 栏也已满，适用灾难性永久后果。伤害影响必须依角色当前做的事情判断相关性，不是所有伤势都对所有行动施加惩罚。

### BLD-CNS-02｜Resistance

按后果性质选择属性组：Insight 对应欺骗/理解，Prowess 对应身体劳累/伤害，Resolve 对应心理劳累/意志力。GM 说明当前后果以及抵抗能完全避免还是降低严重程度，再让玩家决定是否抵抗。

- 常规时点：Action Roll 已结算，GM 提出具体 Consequence 后，玩家选择抵抗。
- 先手威胁例外：若强势敌人已在 PC 行动前造成明确后果（例如先行缴械），可以先处理 Resistance，再进行 PC 行动。
- 不允许无具体后果时预先掷骰，也不能先掷 Resistance 再决定是否承担代价。

1. 确定后果具体内容。
2. 玩家决定是否抵抗。
3. GM 确定对应 Attribute。
4. 玩家掷 Attribute Dice。
5. 计算 Stress，确定后果被避免还是减轻。
6. 写入 Stress 与后果的最终状态。

GM 应在抵抗之前说明可抵抗的后果。不得把 Resistance 变成事前保护罩或可随意重掷行动。

### BLD-CNS-03｜Armor

Armor 是 Resistance 的替代处理手段，不是额外叠加的一次抵抗。必须先确认本次 Score 的 Loadout：

- **Standard Armor**：角色需要在本次 Score 将 Armor 作为携带物品声明，标准护甲占 2 Load。合适后果出现时，可标记角色卡上的 Standard Armor 格来减轻或避免后果。
- **Heavy Armor**：以标准 Armor 为基础，额外占 3 Load（合计 5 Load）。在适用后果上可标记 Heavy Armor 格，提供第二次减轻；例如先用 Standard Armor 将 Level 2 Harm 降至 Level 1，再以 Heavy Armor 降至 0。
- **Special Armor**：每张角色卡有独立 Special Armor 格；只有角色拥有明确使用 Special Armor 的 Playbook Ability 时才能勾选。它通常用来触发该能力，而不是通用伤害减免。
- 每个已标记的 Armor 格在本次 Score 中不能重复使用；所有 Armor 在下次 Score 选择 Load 时恢复。
- 若角色本次 Loadout 没有带上适用的 Standard/Heavy Armor，则不能临时声明携带并使用；除非某项特殊能力明确豁免 Load 或提供特殊保护。

因此，对同一个后果，先让玩家在可用的 Armor 与 Resistance 之间选择；不能把 Armor 的效果先计入，再对同一后果额外做一次 Resistance。

- 普通 Armor、Heavy Armor、Special Armor 是角色卡独立的使用格。
- 角色可在适用伤害后果时使用 Armor，说明装备如何挡住/降低该后果并勾选使用格。
- Heavy Armor 可在符合规则时额外勾选一格。
- Armor 使用格在下一次 Score 选择 Load 时恢复；进入 Downtime 本身不会恢复已标记的 Armor。
- 特殊能力中的 Special Armor 有独立用途；必须按该角色能力的明文触发条件执行。

**互斥与时序**：对同一后果，不能既将 Armor 视为已完全解决，又重复把同一后果交给 Resistance 再结算一次。先说明具体后果，再选择可用的处理手段。

### BLD-CNS-04｜Stress / Trauma

- Stress 主要来自 Resistance、Push、Flashback、团队协作和其他规则明示来源。
- 当 PC 标记最后一个 Stress 格时，获得一个 Trauma 状态并退出当前冲突/场景，不能继续行动；稍后回到游戏时 Stress 清为 0，且下一次 Downtime 会自动满足其 Vice。
- Trauma 是永久的角色性格状态（如冷漠、恶梦、痴迷、偏执、鲁莽、软弱、不稳、恶毒），会持续影响角色行为与选择，不只是数值惩罚。
- 达到 4 个 Trauma 后，角色不能再作为常规亡命徒继续行动；玩家选择退休或入狱等规则允许的退场方式。

### BLD-CNS-05｜Healing Clock

- 在 Downtime 使用 Recover 活动。
- 治疗者以适用 Action（通常为 Tinker；有特定能力者可使用能力指定的方式）或 NPC Quality 掷骰。
- 1–3 推 1 格、4/5 推 2 格、6 推 3 格、Critical 推 5 格。
- 治疗钟填满后，角色现有每一项 Harm 降低一级，清空该钟；多余进度结转。
- 新 Harm 会清除已经累积的 Healing Clock 进度。

### BLD-CNS-06｜致命风险

- Level 4（致命）Harm 若未被 Resistance 避免，角色死亡。
- 若角色必须标记 Level 3 Harm，但 Level 3 栏已满，发生灾难性、永久性后果；是否立即死亡取决于当前情境。
- 不能把一般 Level 3 Harm 自动判为死亡；不能把满栏升级与 Level 4 的死亡规则混为一谈。
- 任何死亡/永久伤害都要先确认规则条件、可用的 Resistance/Armor 和玩家选择。

## 5. Clocks、Fortune 与 Gather Information

### BLD-CLK-01｜Progress Clock

适合真实复杂、分阶段或持续发展的障碍和项目。常见大小为 4、6、8 格：复杂障碍 4 格、更复杂障碍 6 格、可怕/艰难障碍 8 格；更复杂目标可使用多只关联钟。简单阻碍通常直接以一次行动处理，不需要时钟。

建立时，时钟应描述**阻碍本身**，而不是玩家必须采用的解法。例如“内部巡逻”或“塔楼防线”是阻碍；“悄悄通过守卫”或“爬上塔”是方法。玩家可以用不同方法推进同一阻碍的时钟。钟代表虚构进程，而不是固定的成功次数或对手 HP。

常见类别：
- Danger：危险逐步发生；
- Racing：双方争夺时间或目标；
- Linked：多个阶段或防线；
- Mission：任务窗口/期限；
- Tug-of-War：事件可填充或回退的对抗；
- Long-Term Project：角色/组织长期目标；
- Faction Clock：派系的持续计划。

### BLD-CLK-02｜钟的推进与后果

- Action 的 Effect 决定进度通常推进多少格：Limited 1 格、Standard 2 格、Great 3 格。
- Consequence 引发的危险钟推进通常为轻微 1 格、标准 2 格、严重 3 格。
- GM 因后果推进危险钟时，说明正在累积的危险。
- 玩家行动可能推进、阻止或回退某些钟，必须有虚构因果。
- 钟填满后，发生其描述的结果；不得随意改变已公开钟的目标含义。

### BLD-CLK-03｜Fortune Roll

只判断程度、质量、成功范围或不确定事实。不要对已经清晰的常识重复掷骰。对手/派系的 Fortune Roll 可用其 Tier 或 Quality 表示能力；优势/劣势应来自具体条件。

- 每个适用 Trait 点数提供 1d；每个重大优势 +1d，每个重大劣势 -1d。
- 读取最高骰：1–3 为坏结果/微弱效果，4/5 为混合结果/有限效果，6 为好结果/标准效果，Critical 为额外成果/重大或极端效果。
- Fortune Roll 没有 Position，也没有 Action Roll 意义上的 Consequence；它用于决定表现程度。

### BLD-CLK-04｜Gather Information

- **常识**：直接回答。
- **发现信息存在危险障碍**：用 Action Roll。
- **信息存在但结果不确定，无直接危险障碍**：用 Fortune Roll。
- **复杂调查或需要多步积累**：使用 Long-Term Project。
GM 应如实提供角色有资格获取的信息；Effect 决定信息的详细程度/范围。若角色问的是可知事实，不要为了制造戏剧性故意含糊。

### BLD-CLK-05｜时间与重复调查

调查活动会消耗合理的时间并可能改变局势。只有当情境提供了新的方法/资源/机会时，才允许重复尝试相同的调查；不要用重复无意义掷骰拖延。

## 6. Score、计划与 Engagement Roll

### BLD-SCR-01｜Score 目标

Score 是有具体目标的任务行动，常见目标：
- Crew 类型所擅长的犯罪业务；
- 获取一个 Claim；
- 玩家提出的特殊目标。

Score 可以短至几个行动，也可以发展成复杂事件。任务目标可以来自派系、客户、组织 Claim Map 或玩家主动提出。

### BLD-SCR-02｜六种 Plan

| Plan | 意图 | 必须提供的 Detail |
|---|---|---|
| Assault | 对目标施加暴力 | 攻击点 |
| Deception | 引诱、欺骗、操纵 | 欺骗方法 |
| Stealth | 秘密潜入/穿越 | 渗透点 |
| Occult | 与超自然力量接触 | 奥术方法 |
| Social | 谈判、交易、说服 | 社交关系/关联 |
| Transport | 让货物或人员通过危险 | 路线与方式 |

Plan + Detail 足以开始任务。未知 Detail 可以用 Gather Information 查明。GM 不要求玩家事先模拟所有细节。

### BLD-SCR-03｜Load

Plan 和 Detail 确立后，每名 PC 选择 Load：
- 1–3：Light，轻装、低调、行动快；
- 4–5：Normal，通常装备状态；
- 6：Heavy，行动慢且明显携带任务装备；
- 7–9：Encumbered，负担过重、只能缓慢移动。

玩家不必事先选完具体道具；行动期间可以在 Load 限额内声明可用道具。双格道具消耗两个 Load；斜体道具不计入 Load，按角色表解释。特殊能力可能提高上限。

### BLD-SCR-04｜Engagement Roll

在 Plan + Detail + Load 后，GM 直接切入任务已经开始、PC 遇到第一个重要障碍的场面。Engagement Roll 是特殊 Fortune Roll：
- 基础 1d；
- 特别大胆 +1d；过度复杂/依赖很多条件 -1d；
- Detail 利用目标弱点 +1d；目标对此做足准备或该方法正中其强势 -1d；
- 友人/联系人能提供实质帮助 +1d；敌人/对手干扰 -1d；
- 其他明确 Tier/地点因素可调整。

结果只决定开局：
- Critical：第一个障碍已解决，下一步以 Controlled 开始；
- 6：Controlled；
- 4/5：Risky；
- 1–3：Desperate。

Engagement 结果不会锁定整个 Score 的所有后续 Position。

### BLD-SCR-05｜Score 行动循环

- GM 明确当前障碍、目标、危险和可见环境。
- 玩家说明目标与行动，按 Action Roll 处理。
- 结果影响世界/目标/资源/钟；必要时用 Flashback 或 Teamwork。
- 达成目标、放弃行动或遭遇必须结束的局势时，收束本 Score。
- 不强迫每次 Score 都持续一整场；不把每个小障碍都扩成完整任务。

### BLD-SCR-06｜放弃 Score

放弃 Score 会进入 Downtime；通常没有任务 Payoff，但仍结算因行动产生的 Heat 和 Entanglements。不能因玩家放弃就抹去已经发生的世界后果。

## 7. Flashback 与 Teamwork

### BLD-FLB-01｜Flashback

Flashback 是玩家提出角色过去曾经采取的行动，解释它如何影响当前局势。它不能撤销既定事实，也不代表角色可以修改已经发生的结果。

GM 按复杂程度设 Stress：
- 0：正常、容易安排的行动；
- 1：复杂行动或不太容易得到的机会；
- 2+：精密准备、多个特殊机会或附带条件。

Flashback 按真实行动类型处理：有危险用 Action Roll；结果不确定用 Fortune Roll；合理且无风险时可以直接完成。若涉及一项 Downtime Activity，成本改为 1 Coin 或 1 Rep。

### BLD-FLB-02｜Assist

协助者说明如何帮助，主行动得到 +1d；协助者承担 1 Stress。每次行动最多一名 Assist。若协助者可能承受后果，也要按场景明确。

### BLD-FLB-03｜Group Action

所有参与 PC 用同一 Action 各自掷骰，最高结果代表全组结果；未参与掷骰的 PC 不获得该行动效果。Leader 对每名掷出 1–3 的成员承受 1 Stress。角色 Action rating 不需特别高也能领导 Group Action；NPC Cohort 可按规则参与。

### BLD-FLB-04｜Protect / Setup

- Protect：角色替队友承受后果，然后可以正常抵抗。
- Setup：先做一个间接行动；若成功，后续指定行动获得 +1 Effect 或更好的 Position。影响多个后续行动必须有明确因果。

## 8. Downtime 活动

### BLD-DOW-01｜活动预算

通常每名 PC 有 2 个正式 Downtime Activities；处于 War 时只有 1 个，除非 Crew Ability 明确例外。额外活动每次支付 1 Coin 或 1 Rep。自由行动、谈话、普通调查和场景演绎仍可以发生，不受这份活动额度限制。

如朋友/联系人提供帮助，活动骰池 +1d。掷后可用每枚 Coin 提升一个结果等级。

### BLD-DOW-02｜Acquire Asset

临时取得一项资产：特殊物品/普通装备组、Cohort、载具或服务。临时使用通常持续一个有意义的使用期，常见为本次 Score。掷 Crew Tier：
- 1–3：Tier -1；
- 4/5：Tier；
- 6：Tier +1；
- Critical：Tier +2。
若想把结果提高到 Critical 以上，每增加一个 Tier 花费 2 Coin。GM 可设最低品质门槛；达不到则无法取得。重复取得同一资产可 +1d，持续重新租用可近似长期使用。危险化学品、毒药、炸弹等高限制资产如通过 Acquire Asset 取得（而非自行打造），增加 +2 Heat。永久取得资产应通过 Crew Upgrade 或 Long-Term Project 实现。

### BLD-DOW-03｜Long-Term Project

说明如何推进项目，掷适用 Action：1–3 推 1 格、4/5 推 2 格、6 推 3 格、Critical 推 5 格。基础项目通常 8 格，复杂项目可以多个钟。GM 应设定合理的钟和实现方法；若角色尚不具备项目所需条件，先解决获取条件的问题。

### BLD-DOW-04｜Recover

Recover 由需要治疗的角色花费自己的 Downtime Activity；治疗者进行掷骰：
- PC Physicker/治疗能力通常使用 Tinker 或 Attune（依能力）；NPC 治疗者按 Quality 掷骰。
- 1–3 推 1 格、4/5 推 2 格、6 推 3 格、Critical 推 5 格。
- 角色可自行治疗，但需额外承受 2 Stress。
- 没有治疗者仍可硬撑：承受 1 Stress，以 0d 掷骰（掷 2d 取低值）。
- 帮别人治疗不会消耗治疗者自己的 Downtime Activity；被治疗者仍要花自己的 Recover 活动。
- Healing Clock 填满后，所有现有 Harm 各降一级并清钟，多余进度结转。角色新受伤会清除 Healing Clock 已累积的进度。

### BLD-DOW-05｜Reduce Heat

角色说明如何减少组织 Heat，并掷适用 Action：
- 1–3：减 1；
- 4/5：减 2；
- 6：减 3；
- Critical：减 5。

### BLD-DOW-06｜Train

选择一个 Attribute 或 Playbook XP track 标 1 XP；相应 Crew Training Upgrade 可加 1 XP。每次 Downtime 不能训练同一 XP track 多次。

### BLD-DOW-07｜Indulge Vice

以角色最低 Attribute 的骰池掷骰，按最高骰清除 Stress。清除量大于当前 Stress 就 Overindulge。若未能/不能沉溺 Vice，承担等同 Trauma 数量的 Stress。

Overindulge 结果包括：额外 Entanglement、吹嘘导致 +2 Heat、角色失踪一段时间并由其他角色临时代演、供应者切断供应并需寻找新来源。

### BLD-DOW-08｜NPC/Faction Downtime

对本阶段与玩家相关的派系推进项目钟，并选择 1–2 个符合其利益、目标和机会的行动：夺取 Claim、增强 Hold、收集情报、完成短期目标、获取资产、请求盟友援助、施加政治压力等。暂时忽略的派系可在重新进入焦点时合理追赶。通过地下社会的朋友、联系人或 Vice purveyor 向玩家传递他们应该知道的消息。

## 9. Score 结算：Payoff、Heat、Entanglements

### BLD-SET-01｜Payoff

- 默认任务报酬 2 Rep。
- 目标 Tier 每高于 Crew Tier 一级，+1 Rep；每低一级，-1 Rep（最低 0）。
- 完全低调的任务默认不获得 Rep，除非 Crew Ability 修改。
- Coin 按任务规模/收益判断：2（小型）、4（小型但可观）、6（常规）、8（大型）、10+（重大）。
- 向地头势力缴纳 Tithe 时，按 Crew Tier+1 扣 Coin（若适用）。

### BLD-SET-02｜Heat

每次 Score 或与对手发生冲突后结算曝光：
- 基础曝光：0（平稳安静）、2（控制良好）、4（吵闹混乱）、6（极其显眼/破坏性）。
- 高调或关系显赫的目标 +1；
- 敌方地盘 +1；
- Crew 与对手处于战争 +1；
- 涉及杀人 +2；
- 另计 Devil's Bargain、后果或场景已明确增加的 Heat。

Heat 轨达到 9 时 Wanted Level +1，并将超额 Heat 结转。Wanted Level 不由 Reduce Heat 直接消除；须按 Incarceration 等规则降低。

### BLD-SET-03｜Entanglements

Payoff、Heat 之后掷 Entanglement：
- 骰池 = 当前 Wanted Level；
- Wanted Level 0：掷 2d 取低值；
- 以当前 Heat 所在档位查表。
- 按触发的 Entanglement 落实局势。GM 可等到合适时机把已发生的麻烦带进场景，但不能让玩家在它显现前提前取消这次纠葛。

官方 v8.2 查表：
| 结果 | Heat 0–3 | Heat 4/5 | Heat 6+ |
|---|---|---|---|
| 1–3 | Gang Trouble / Usual Suspects | Gang Trouble / Questioning | Flipped / Interrogation |
| 4/5 | Rivals / Unquiet Dead | Reprisals / Unquiet Dead | Demonic Notice / Show of Force |
| 6 | Cooperation | Show of Force | Arrest |

### BLD-SET-04｜Incarceration / Wanted

- 组织有关联的人因组织相关罪行入狱时，Crew Wanted Level 通常降低 1 并清除 Heat。
- 服刑时间由 Wanted Level 决定；Crew Tier 掷 Incarceration Roll。
- v8.2 参考表：Critical 获得 +3 Rep、一个 Prison Claim、支持派系 +1 Status；6 获得一个 Prison Claim 和 +1 Status；4/5 平稳完成；1–3 获得 Trauma。
- Prison Claims 只在相应规则范围内生效；需要时回查相关条文。

### BLD-SET-05｜顺序不可混淆

完整顺序：Payoff → Heat → Entanglements → Downtime。成功/失败影响 Payoff 和当前世界事实，但不会自动跳过因果成立的 Heat/Entanglements。玩家放弃 Score 时仍按规则处理 Heat 与 Entanglements。

## 10. Crew、Factions 与 Cohorts

### BLD-CRW-01｜Crew 初始与核心状态

典型新 Crew 起点：Tier 0、Strong Hold、0 Rep、2 Coin；还要按 Crew Type 建立声望、Lair、Hunting Grounds、Favored Operation、特殊能力、起始升级与联络人。不同版本/组织卡的明确起始内容优先于泛化摘要。

Crew Creation 的状态输入不可遗漏：
1. 选择 Crew Type；它决定常见业务、Crew XP 触发点、Crew Ability 与专属升级。
2. 选择 Reputation 与 Lair。
3. 选择 Hunting Grounds，并处理声称拥有该区域的 Faction：支付 1 Coin 换取活动空间；或支付 2 Coin 获得 +1 Status；或不付钱并承受 -1 Status。
4. 选择 Preferred Operation、Crew Special Ability。
5. Crew Sheet 已预选两项升级，再选择两项，总计四项；按升级影响记录一个帮助派系（+1 Status，可付 1 Coin 改为 +2）和一个受损派系（-2 Status，可付 1 Coin 改为 -1）。
6. 选择 Favorite Contact；记录一个友好派系 +1 Status、一个敌对派系 -1 Status；可按规则改为 +2/-2。
7. 确认初始 Cohort、特殊升级、Coin/Vault 与 Claim Map 节点。

### BLD-CRW-01A｜Hunting Grounds 与 Preferred Operation

当 Crew 准备在自己的 Hunting Grounds 执行所选 Preferred Operation 时：
- 该次准备所需的 Gather Information Rolls 获得 +1d；
- 获得一个免费的额外 Downtime Activity，且必须用于贡献这次 Score 的准备（例如发现机会、获取资产或寻找客户）。

这项免费活动不是通常的额外活动购买，不消耗 1 Coin / 1 Rep。若已获得 Turf，Crew 可扩大 Hunting Grounds 的区域和/或业务类型。

### BLD-CRW-02A｜Coin / Vault / Stash

- Coin 是抽象现金/流动资产单位；PC 日常零碎支出不逐笔追踪。小额贿赂等日常目标，使用 PC 的 Lifestyle Quality 作 Fortune Roll。
- **个人散放现金**：超过 4 Coin 是不方便随身/散放的金额；多余部分应花掉或转入个人 Stash。若将实体银币或其他大宗现金带在身上，每 1 Coin 占 1 个 Load 物品格。
- **Crew 库存**：组织的 Lair 默认可存放 4 Coin。Vault 第一次升级把容量提高至 8，第二次提高至 16。超过组织容量的 Coin 应尽快花掉（通常在下一次 Score 前）或分配给组织成员。
- **个人 Stash**：长期个人财富，单独记录在 PC 卡上。每个完整的 10 Stash 表示一档 Lifestyle Quality（0–4）；达到最终 Trauma 退场时，Stash 决定角色退休后的生活。每移除 2 Stash，换回 1 Coin 现金。
- 常见 Coin 用途：每花 1 Coin 获得一个额外 Downtime Activity；每花 1 Coin 可在 Downtime 掷骰后提升一个结果等级；也可用于避免部分 Crew Entanglements、升级 Crew Tier，或转入个人 Stash。
- 每次 Crew Advance 时，每名 PC 获得等于 Crew Tier + 2 的 Stash；这一增加是个人 Stash，不是 Crew 的可花费 Coin。
- 组织升级 Tier 时支付新 Tier × 8 Coin；Patron 等能力可修改成本。

### BLD-CRW-02｜Tier / Hold / Rep / Turf

- Tier 衡量组织的资源、影响力与相对地位；也决定物品品质及 Cohort 的 Quality/Scale 基线。不要把 Tier 简化成单纯人数。
- Hold 为 Strong 或 Weak，反映组织巩固其当前地位的能力。
- Rep 基础轨为 12；每片 Turf 使本次晋级所需 Rep 减少 1，Turf 最多 6 片。因此当前晋级阈值为 12 - Turf 数量（最低 6）。晋级重置 Rep 时保留 Turf。
- 当 Rep 达到阈值：若 Hold 为 Weak，则提升为 Strong 并将 Rep 重置为 0；若 Hold 为 Strong，则可支付新 Tier × 8 Coin 提升 Tier，之后 Rep 重置为 0、Hold 降为 Weak。
- Turf 和 Claim 有各自具体效果；夺取 Claim 通常会影响目标派系 Status 与组织关系。
- SRD 的 Scale / gang-size 参照为 Tier 0：1–2 人；Tier I：3–6；Tier II：12；Tier III：20；Tier IV：40；Tier V：80；Tier VI：160。此表用于估算规模，不等于每个派系必须按该人数配齐 Cohort。

### BLD-CRW-02B｜Claims 与 Claim Map

- 每种 Crew Type 有专属 Claim Map，从 Lair 节点向外连接，显示典型的组织成长路线。
- 通常沿连接路径逐步夺取 Claim；地图路径是推荐路线，不是绝对限制。直接挑战不相邻 Claim 或地图外特殊 Claim 通常特别困难，可能需要额外调查/搜集情报来发现机会。
- Claim 已被某个 Faction 控制。玩家声明想夺取的 Claim 后，GM 给出地点、描述与当前控制者。
- 夺取 Claim 是一次正常 Score。成功后 Crew 获得 Claim，原派系失去它；通常对原控制派系 -2 Status，可能对其敌对派系 +1 Status。
- Claim 的收益只在 Crew 持有期间生效；失去 Claim 后立即失去该收益。若 Lair 被夺走，所有 Claim 收益暂时停用，直到 Crew 通过 Score 恢复或建立新 Lair。
- 各 Crew 的 Claim 名称与简要收益见 [CREW_CLAIMS_AND_STARTUP_REFERENCE.md](./CREW_CLAIMS_AND_STARTUP_REFERENCE.md)。实际路径、重复 Turf 节点与位置以 Campaign 锁定版本的 Crew Sheet 为准。

### BLD-CRW-03｜Faction Status / War

派系关系从 -3 到 +3。Status -3 为 War：派系即使代价高也会伤害对方，双方均有所防备。War 会带来以下规则影响：
- 每个 Score 的 Heat +1；
- Crew 暂时失去 1 Hold；若战前为 Weak，可能暂时降 Tier，War 结束后按规则恢复战前 Tier；
- 每名 PC 每次 Downtime 只有 1 个正式活动，而非 2 个。
具备明确 Crew Ability 的组织可按该能力覆盖相应惩罚。War 不是纯叙事标签，应按规则改变状态与活动额度。

### BLD-CRW-04｜Cohort

Cohort 可以是 Gang 或 Expert：
- Gang 以 Crew Tier 决定 Quality/Scale；人数规模由 Tier 决定。
- Expert 通常 Quality = Crew Tier+1，Scale 为单人。
- Cohort 可有 Types、Edges 和 Flaws；按相关领域使用 Quality。
- 任务中派遣 Cohort 可由 GM 按 Quality 作 Fortune Roll；PC 直接领导/参与时按 Teamwork 或相应 Action 处理。

### BLD-CRW-05｜Cohort 状态

- Weakened：Effect 降低；
- Impaired：相关行动 -1d；
- Broken：恢复前不能行动；
- Armor：按 Cohort 自身规则消耗。
休整期间通常恢复一个伤害等级；PC 花费相应活动照料可加快恢复。Dead/Destroyed 需要按成本/活动重新招募或替换。

### BLD-CRW-06｜Faction Clock

每个重要派系应有目标和必要时的项目钟。只有当它与 PC/Crew 的处境、已知利益或当前冲突相关时才推进。NPC 不能因 GM 想制造戏剧性就获得无来源的行动能力；行动必须符合目标、资源、机会与世界事实。

### BLD-CRW-07｜状态持续性

Score、Claim、Tier、Rep、Hold、Status、Heat、Wanted、Coin、Cohort 状态与项目钟均可能跨场景持续。状态变化要有事件依据，不能在下一场景无说明重置。Crew advancement、Downtime 和规则规定的恢复时点是状态重置的主要入口。

## 11. PC 与 Crew 成长

### BLD-ADV-01｜PC XP

每次 Desperate Action 在对应 Attribute XP Track 标 1 XP。这里的“对应属性”是该 Action 所属的 Insight / Prowess / Resolve 属性组，不是单独给该 Action 点数本身加 XP。Session 结束按 Playbook XP triggers、表达角色信念/驱力/出身/背景、与 Vice/Trauma 的冲突结算 XP，按出现次数给 1 或 2 XP。填满对应轨后获得 Action dot 或 Playbook Special Ability。

### BLD-ADV-02｜Action Rating 上限

角色创建时 Action rating 通常不超过 2；正常成长可到 3；Crew 解锁 Mastery 后才能到 4。任何特殊能力如有例外，按原文处理。

### BLD-ADV-03｜Crew XP

每次 Session 结束按 Crew Type 的成功行动类型、面对高于自身地位的挑战、加强/发展声望、表达组织目标/驱力/冲突/本质结算 XP。Crew XP 轨填满后获得组织特殊能力或 2 个升级格。

### BLD-ADV-04｜Crew Advance 的个人奖励

官方 Player's Kit v8.2 Crew Sheet 说明：Crew 每次 advance 时，每名 PC 获得等同当前 Tier+2 的 Stash。按 Campaign 采用版本再锁定这一字段。

### BLD-ADV-05｜Vice / Trauma 的长期影响

Vice 是 Stress 缓解方法，也会带来 Overindulgence 后果；Trauma 是持久特质并改变人物表现。主持时需把二者转化为角色行为/关系/机会，不把它们只当作数值按钮。

## 12. Ritual、Magnitude 与 Crafting

### BLD-ARC-01｜Magnitude

Magnitude 是 GM 判断超自然实体、力量、品质、范围、规模和持续时间的量级参照（通常 0–6）。它是裁定辅助，不是所有维度都自动相加的公式。判断力量对目标有多大影响时，可在不确定时使用 Magnitude 作为 Fortune Roll Trait。

### BLD-ARC-02｜Ritual 来源与学习

有 Ritual 能力的角色通常开始时知道一个仪式。新仪式需要找到来源，再通过 Long-Term Project 学习；常见学习钟为 8 格。玩家与 GM 共同定义仪式的效果、怪异之处、执行方法、材料/时间/代价，以及施术者获得的新信念或恐惧。

### BLD-ARC-03｜执行 Ritual

仪式通常消耗一个或更多 Downtime Activities，并按 Magnitude 产生 Stress 成本；延长施法时间可以降低成本。危险/麻烦的执行需要 Action Roll；效果不确定需要 Fortune Roll；既危险又不确定时两者都可能需要。可以使用 Clock 表示仪式引发的后续奥术力量/威胁。不得将 Ritual 当作免费、稳定、无后果的法术列表。

### BLD-ARC-04｜Invention / Crafting

- 发明新的配方/设计通常通过 8 格 Long-Term Project。
- 玩家定义创造物类型与用途；GM 根据 Magnitude 判断最低品质，玩家补充其稀有/奇异/不常见之处，GM 定义缺点。
- 打造通常消耗一项 Downtime Activity，以 Tinker 掷骰决定品质；基础品质为 Crew Tier，结果将其调整为 Tier-1/Tier/Tier+1/Tier+2。
- Coin 可逐级提高品质；Workshop 等升级可能提高可用品质。
- 改造已有物品按预期效果设置最低品质；越超常的改造需求越高。

### BLD-ARC-05｜Craft 缺点

可能包括复杂（多阶段）、显眼（反复使用带来 Heat）、消耗品、稀有材料、不可靠（使用时掷 Fortune）、不稳定（危险副作用）。缺点必须在发明/打造阶段建立，并记录在物品状态中。
