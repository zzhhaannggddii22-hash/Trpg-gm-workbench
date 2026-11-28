# Blades in the Dark｜AI GM Behavior Self-Test

> date: 2026-11-28  
> ruleset baseline: 中文核心规则书 V1.3（英文原版 v8.2）  
> tested documents: GM_SKILL.md, RUNTIME_PROTOCOL.md, GM_BEHAVIOR_REGRESSION_CASES.md  
> test type: same-model scenario response self-test  
> status: preliminary / not independent evaluation / not real playtest

## 1. Method and limits

本轮逐项运行 GM_BEHAVIOR_REGRESSION_CASES.md 的 18 个场景。对每个输入生成一个候选 GM 回应，再按案例预期行为与 GM Skill 检查。判定分为 PASS、PARTIAL、FAIL。

这不是独立模型评审，也不是隔离的自动化测试程序：生成和评价由同一模型完成，存在自我偏差风险。结果只能说明本次模型在已加载规范下能否产出符合要求的回应样例，不能证明跨会话稳定性、长期状态连续性或真实桌面表现。

## 2. Results

- PASS: 16
- PARTIAL: 2
- FAIL: 0
- Automated engine execution: 0
- Independent evaluator: 0
- Real playtest: 0

## 3. Case-by-case execution

| ID | Candidate GM response / behavior | Result | Notes |
|---|---|---|---|
| GM-01 | “你准备怎么拿到钥匙？描述一下角色实际做的事；你可以据此选择对应的 Action。” | PASS | 不代替玩家指定 Action。 |
| GM-02 | “门没有上锁，走廊也没人看守。你推门进去，里面是……” | PASS | 无挑战、无风险，直接成功。 |
| GM-03 | “你当然可以尝试。行动值为 0 不代表角色无能；我会按核心规则的 0d 骰池程序处理，而不是取消行动。” | PARTIAL | 行为原则正确，但当前 GM Skill 未明确指向 0d 规则锚点；应补充规则调用提示。 |
| GM-04 | “你能看到两名警卫：一人在门边抽烟，另一人在楼梯口来回巡逻。正门和侧窗都在视野内。” | PASS | 直接提供角色可观察事实。 |
| GM-05 | “正面拜访会被门卫拦下。你可以先找到他信任的工头，也可以制造一场公开事故让他不得不出面；你也可以提出第三种办法。你打算怎样创造这个机会？” | PASS | 提供机遇，不封死行动。 |
| GM-06 | “你想徒手翻过带玻璃碎片的高墙。风险位置：墙顶的碎玻璃和外侧巡逻会让你暴露并受伤；效果有限：你能越墙，但很难同时保持隐蔽。你要这样做，还是改变方法？” | PASS | 风险与成果规模分开说明。 |
| GM-07 | “你成功拿到了文件，但守卫在你离开时击中了你。你可以抵抗这次伤害；即使完全避免伤害，你仍然已经拿到了文件，也仍处在被发现的现场。” | PARTIAL | 成果与既定事实保留；需要更明确区分 Resistance 可以减轻乃至完全避免某项后果，但不能抹除行动已经确立的事实。 |
| GM-08 | “你推开门时，房间里最先映入眼帘的是一排覆着灰的档案柜。靠窗那只柜门半开着，里面有新鲜的泥点。” | PASS | 在玩家进入时确立潜在细节，之后应保持连续。 |
| GM-09 | NPC 拒绝交出账本：“你可以打断我的手，但账本不会因此归你。账本是我保命的筹码。你若想拿走它，就得让我相信你能提供更好的保障，或者让我失去继续持有它的能力。” | PASS | NPC 依目标与底线回应，不为配合玩家而软化。 |
| GM-10 | “这把普通挂锁没有额外防护。你用工具处理它；若没有新的风险或复杂机制，不需要为它单独建立 Clock。” | PASS | 不把简单障碍过度钟表化。 |
| GM-11 | “你们穿过煤烟弥漫的街道。半小时后，已经站在联系人那间二楼办公室门外。门内传来收音机和争吵声。” | PASS | 无意义移动快切，同时给出场景信息。 |
| GM-12 | “计划和细节已经确定，大家也选好了 Load。我们掷 Engagement，随后直接切入行动开始时的处境。若你发现缺少准备，可以在之后提出 Flashback。” | PASS | 不让计划无限蔓延。 |
| GM-13 | “你已经拿到目标账本。账本上的交易记录完整可读；这部分成果归你们。外面传来警笛，是之前行动留下的后果，不会取消账本已经到手的事实。” | PASS | 兑现成功，不克扣成果。 |
| GM-14 | “你动作快得几乎让他来不及反应，但他早已把椅子横在门口。你撞上椅背，手里的枪滑进桌底；他趁机冲向警铃。” | PASS | 失败源自环境和对手，不把角色演成笨蛋。 |
| GM-15 | “她说话时一直把右手压在外套口袋上，回答到名字时停顿了一瞬。她似乎在防备什么；你能感觉到她并不相信这场会面安全。” | PASS | 提供可察觉迹象，不直接揭露秘密。 |
| GM-16 | “目前没有证据表明城外的黑灯党知道这次交易，也没有人能及时赶到。这个场景里他们不会突然出现。” | PASS | 屏幕外事件需要因果、信息与行动能力。 |
| GM-17 | “你们已经检查了三间相似的仓库，手法和线索都重复。我们快进到最后一间：这次门锁被人从里面反锁，地上有一条新鲜的血痕。” | PASS | 根据重复度压缩镜头，转向新决策点。 |
| GM-18 | “这里按 Blades 的 Action / Fortune / Resistance / Downtime 处理；不会借用其他系统的属性检定、资源或阶段。” | PASS | 保持系统边界。 |

## 4. Findings and corrective actions

### Finding A — Zero Action Rating dispatch needs an explicit anchor

GM Skill 已写明 0 Action Rating 不等于角色无能，但没有明确要求在需要时调用核心规则中的 0d 骰池程序。建议补充：0 点行动值仍可尝试；骰池和结果按 CORE_RULES_RUNTIME 的零骰规则处理，不得自行改写。

### Finding B — Resistance wording needs precision

GM Skill 已说明 Resistance 可减轻或避免后果，但在主持陷阱章节容易被简写成“改变严重程度或表现”。应明确：Resistance 可以完全避免某项后果；它不能撤销行动骰已经确立的虚构事实或成果。

### Finding C — Same-model evaluation is weak evidence

本轮自测没有独立评分者，也没有真实玩家输入中的歧义、情绪、跑题、长期记忆压力。应将其视为一次自我校验和文档修订，不应将 16/18 PASS 解释为 GM 能力通过率。

## 5. Next validation layer

1. 修正 GM Skill 的两处措辞。
2. 在新会话仅加载系统入口与 GM Skill，重复相同案例，检查规范能否在最小上下文中被正确调用。
3. 进行一次短场景真人跑团，重点观察玩家能动性、NPC 可信度、信息公平和镜头节奏。
4. 依据真实表现更新案例，不为追求全 PASS 而降低验收标准。


## 6. Targeted retest after corrections

对两项 PARTIAL 进行针对性复测：

- **GM-03 — PASS（targeted retest）**：修订后的 GM Skill 明确要求 0 Action Rating 仍可尝试，并调用 CORE_RULES_RUNTIME 的零骰程序，不得自行取消行动或发明骰池处理。
- **GM-07 — PASS（targeted retest）**：修订后的 GM Skill 明确 Resistance 可减轻或完全避免某项后果，但不能撤销行动骰已确立的虚构事实。

因此，本轮 18 个案例均已有符合预期的候选回应：初次 16 PASS / 2 PARTIAL；修订后对两项 PARTIAL 定向复测 2/2 PASS。此结果仍是同模型自评，不应改写成独立评估或真人跑团通过。

## 7. Static integration checks

对 main 上的 GM Skill、Runtime Protocol、Preflight、README、案例集、自测报告和 Manifest 执行 11 项文本/结构检查：

- GM Skill 章节结构与关键条款；
- 0 Action Rating 的规则锚点；
- Resistance 可完全避免后果且不撤销既定事实；
- Runtime Protocol 委托 GM Skill；
- Preflight 包含 GM 行为就绪检查；
- 18 个案例 ID 唯一且齐全；
- 自测报告覆盖 GM-18 且结果汇总一致；
- Manifest 和 README 的交叉链接。

结果：11/11 PASS。该检查验证文档结构和互相引用，不验证实际主持质量。
