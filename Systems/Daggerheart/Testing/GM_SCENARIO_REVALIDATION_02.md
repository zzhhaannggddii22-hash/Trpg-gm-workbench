# Daggerheart GM 场景复核 — Round 2

> 规则绑定：Core Set / CORE_ONLY  
> 角色规模：1 PC（假设角色，不改写基础规则）  
> 数据来源：本地 Core_Set/environments.json、Core_Set/adversaries.json  
> 方法：基于真实 Core Stat Block 的内部场景模拟；非外部盲测、非实际玩家 Session  
> 目的：复核 GM 设计专题中的后果选择、环境驱动、敌人动机、Fear 与 Spotlight 处理。

## 场景 A — Local Tavern：社交信息与 NPC 动机

**环境数据**
- Environment：Local Tavern，Tier 1 / Social / Difficulty 10。
- Impulse：提供冒险机会、维系社区。
- 相关 Feature：What's the Talk of the Town?（Passive）、Mysterious Stranger（Action）、Someone Comes to Town（Action）、Bar Fight!（Action，花费 Fear）。

**场景**
PC 向酒保打听附近的异常事件。酒保并非万能情报机：他关心店铺生意、熟客安全和自己在镇上的信誉。邻桌一名陌生人听见了部分谈话，但尚未决定是否接近。

**模拟行动**
1. PC 先问酒保营业时间、最近是否有人来过。这些普通事实直接回答，不强制掷骰。
2. PC 进一步询问当地传闻，触发环境提供的 Presence Roll。
3. 测试输入：总值达到 Difficulty，Hope Die 高于 Fear Die。
4. 结果：Success with Hope，PC 从选项中取得两条信息；Spotlight 留在玩家侧。
5. NPC 回应：酒保只提供自己确实知道的内容；陌生人暂时观察，不因 GM 需要制造冲突而立刻袭击。

**检查**
- [x] 普通事实不被无意义检定门槛阻挡。
- [x] 环境 Feature 的专用检定与结算正确。
- [x] NPC 只根据自己的信息、利益和风险行动。
- [x] Success with Hope 不强行追加代价或抢夺 Spotlight。

**结果：PASS（桌面模拟）**

## 场景 B — Abandoned Grove：探索信息与失败推进

**环境数据**
- Environment：Abandoned Grove，Tier 1 / Exploration / Difficulty 11。
- Impulse：吸引好奇者、回响过去。
- 相关 Feature：Overgrown Battlefield（Passive）、Barbed Vines（Action）、You Are Not Welcome Here（Action）、Defiler（Action，花费 Fear）。

**场景**
PC 进入一片被植被吞没的旧战场。地面散落断裂武器和折断枝条；一截覆满苔藓的树干形状异常。角色可以观察这些直接可见的事实；“为什么发生战斗”“树干是否为树妖尸体”“魔法如何扭曲树林”则属于调查所得。

**模拟行动**
1. GM 直接描述可感知事实，不把所有视觉信息锁在检定后。
2. PC 进行 Instinct Roll，试图识别战场证据。
3. 测试输入：总值低于 Difficulty，Hope Die 高于 Fear Die。
4. 结果：Failure with Hope。PC 未获得完整调查结果；可按环境 Feature 的失败分支选择标记 Stress，取得一条信息并获得下一次调查优势。
5. GM 使用 Soft Move：风吹过断枝，远处传来一声不属于鸟类的短促鸣叫。玩家知道危险可能接近，仍可决定调查、躲藏或离开。

**检查**
- [x] 观察事实与调查解释分开。
- [x] 环境 Feature 的成功/失败分支不被通用流程覆盖。
- [x] Failure with Hope 保持较轻后果与回应窗口。
- [x] 后果推进信息和危险，而非直接伤害或封死路线。

**结果：PASS（桌面模拟）**

## 场景 C — Ambushed：敌人目标、环境动作与额外 Spotlight

**本地敌人数据**
- Adversary：Jagged Knife Bandit，Tier 1 / Standard / Difficulty 12。
- HP 5，Stress 3，Thresholds 8/14，Attack +1，Daggers 1d8+1 physical。
- Motives & Tactics：Escape, profit, steal, throw smoke。
- Features：Climber（Passive）、From Above（Passive；从高处成功使用标准攻击时造成 1d10+1 physical damage）。

**环境数据**
- Environment：Ambushed，Tier 1 / Event。
- Impulse：Overwhelm, scatter, surround。
- Surprise!（Action）：伏击者现身；GM 获得 2 Fear；Spotlight 立即转给其中一名伏击敌人。
- Relative Strength（Passive）：环境 Difficulty 等于场景中最高 Difficulty 的敌人。

**场景目标**
PC 试图追回被盗的信物并撤离，不需要击败所有敌人。两名 Bandit 已占据高低不同的位置；退路可见，但经过狭窄木桥。

**模拟行动**
1. Surprise! 触发，GM 获得 2 Fear，第一名 Bandit 获得 Spotlight。
2. 第一名 Bandit 按 Motives & Tactics 行动：优先抢走信物并向掩体撤退，而不是默认站在原地与 PC 互砍。
3. GM 花费 1 Fear，让第二名 Bandit 获得额外 Spotlight；该敌人从高处攻击，只有在实际位置与标准攻击成功时才应用 From Above。
4. 若 PC 选择追击，GM 呈现木桥、落差和逃跑路线，让玩家决定追击、射击、绕路或放弃信物。
5. 若 PC 夺回信物并成功脱离，场景结束；不为了清空敌人 HP 强迫继续战斗。

**检查**
- [x] Environment Action 的 Fear 收入与敌人 Spotlight 按顺序处理。
- [x] 第一个敌人 Spotlight 与额外敌人 Spotlight 的成本分开。
- [x] 第二名敌人行动前支付额外 Fear。
- [x] Motives & Tactics 决定敌人优先级，敌人不机械攻击最近目标。
- [x] From Above 只在条件满足时触发。
- [x] 战斗目标是夺回信物并撤离，不强迫歼灭。
- [ ] 单人遭遇的实际难度与玩家体验：未验证。BP 仅可作初步预算，不代表单人平衡已经成立。

**结果：PASS（规则流程与叙事逻辑）；单人遭遇平衡 NOT VERIFIED**

## 总体复核

1. 新增 GM Design Guide 能够把环境 Feature、NPC 动机、敌人目标与 Hope/Fear 结果串成连续场景。
2. GM 不需要给 NPC 建立完整状态机：目标、当前利益、风险与可用信息足以支持即时决策。
3. 环境 Feature 应改变场景的选择空间；不要把所有环境动作改写成伤害。
4. 战斗以目标为中心，敌人可以偷取、拖延、保护或撤退；玩家达成目标后可以结束场景。
5. 本轮仍是内部桌面模拟。它验证的是本地规则数据可被正确调用、流程逻辑一致；不证明实际主持的节奏、难度或乐趣。

## 状态

- 社交场景：PASS（桌面模拟）
- 探索场景：PASS（桌面模拟）
- 战斗流程：PASS（桌面模拟）
- 单人遭遇平衡：NOT VERIFIED
- 外部盲测：NOT RUN
- 实际玩家短场景：NOT RUN
