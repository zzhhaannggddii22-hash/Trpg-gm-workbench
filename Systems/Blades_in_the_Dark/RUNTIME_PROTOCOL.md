# Blades in the Dark｜Runtime Protocol

> system_id: blades_in_the_dark  
> 状态：DRAFT / CANDIDATE VALIDATION PENDING  
> 本文件负责把系统规则连接到一次具体桌面的运行状态；具体规则数值与效果以 Rule_Reference/CORE_RULES_RUNTIME.md 和 Campaign 锁定版本原文为准。

## 1. 目标与边界

- 系统规则只有在 Campaign Binding 锁定本系统后才可正式执行。
- 运行阶段由 Free Play、Score、Downtime 循环组成。
- 规则按触发调用；常规叙事不逐轮检查全部机制。
- PC、Crew、Faction、Cohort 与 Clock 是不同实体，不得混成单一资源总表。
- 规则和世界状态的所有变化都要有可追溯事件依据。
- 不把本协议变成复杂模拟器；只维护对游戏选择和后果有意义的状态。

## 2. 一次性 Preflight 与运行时锁

新 Campaign / 新 Session 开始前确认：

1. Campaign Binding 的 system_id = blades_in_the_dark。
2. 规则版本明确，中文 SRD 修订号或官方规则版次有记录。
3. 已确认本桌采用的术语表、可选扩展与设定资料来源。
4. 读取 PC Sheets、Crew Sheet、当前状态快照、活跃派系与项目钟。
5. 明确当前处于 Free Play、Score 或 Downtime 的哪一阶段。

锁定快照：

```yaml
active_system:
  system_id: blades_in_the_dark
  ruleset_version: "<exact selected version>"
  campaign_id: "<campaign_id>"
  module_id: "<module_id or null>"
runtime:
  phase: FREE_PLAY | SCORE | DOWNTIME
  current_score_id: "<score_id or null>"
```

同一 Session 中不得静默切换规则版本。若版本/来源缺失或冲突，只暂停依赖该规则的裁定，不冻结无关互动。

## 3. 最小持久化状态

### 3.1 PC State

每名 PC 保存：
- Playbook、Heritage、Background、Vice、Vice Purveyor、Friend/Rival；
- 12 项 Action Rating、三组 Attribute；
- Stress、Trauma、Harm、Armor / Heavy / Special Armor 使用格；
- Healing Clock；
- Playbook/Attribute XP；
- Stash；
- 当前 Score 的 Load 与本次声明携带物品。

### 3.2 Crew State

Crew 保存：
- Type、Tier、Hold、Rep、Turf、Claims；
- Reputation、Lair、Hunting Grounds、Favored Operation；
- Crew Special Abilities、Upgrades；
- Coin / Vault、Heat、Wanted Level；
- 各 Faction Status；
- Cohorts（类型、Quality/Scale、Edges/Flaws、伤害状态）。

### 3.3 World / Faction State

只需保存对当前 Campaign 有意义的：
- 相关 Faction 的 Tier、Status、Hold、Claims、目标和项目钟；
- 重要 NPC 的目标、偏好手段、资源、关系和当前可用状态；
- 公开地点、障碍、威胁、任务窗口和已确立事实。

每个 Faction 不必都有项目钟；只有当一个目标有阶段变化或时间压力时才建立钟。

### 3.4 Score State

当前 Score 保存：
- 目标、委托人/来源、目标对象和地点；
- Plan、Detail、每名 PC Load；
- Engagement Roll 的骰池与结果；
- 当前障碍、活跃时钟、PC/NPC 状态变化；
- 已确定但尚未结算的 Payoff、Heat、Entanglements；
- Score 结束原因（完成、失败、放弃或其他）。

## 4. Free Play Runtime

**触发**：尚未进入 Score，PC 在城市/社区/组织内部自由活动。

流程：
1. 让玩家说清想做什么；使用角色目标和 NPC 目标推进场景。
2. 如果是常识或对角色可直接获知的信息，直接回答。
3. 若玩家主动获取信息，按 Gather Information 分流：常识直答；危险障碍用 Action Roll；无直接危险但结果不确定用 Fortune Roll；复杂长期调查才建 Project Clock。
4. 若 NPC/Faction 采取行动，必须由既有目标、利益、资源、机会及世界状态支持。
5. 当出现值得追求的任务目标或玩家明确选择行动，进入 Score Setup。

Free Play 不强制每个对话都掷骰，也不要求玩家在接到任务前先完成一套“任务准备清单”。

## 5. Score Setup → Engagement

**触发**：Crew 决定执行一个具体任务目标。

按顺序：
1. 明确 Score 目标与成功标准。
2. 玩家选择 Plan 类型；若 Detail 未知，先用 Gather Information。
3. 玩家给出 Detail。GM 只追问会影响 Engagement 或实际行动的缺失事实。
4. 每名 PC 选择 Load 档位。
5. GM 评估主要优势/劣势，进行 Engagement Roll。
6. 根据结果确定初始 Position，并立即切入第一个重要障碍。

重要约束：
- 不要求玩家把每个步骤、路线和应急方案都事前讲完。
- Engagement Roll 已经解决“如何接近目标”和起始情势；掷完不能再把镜头退回漫长的接近过程。
- Engagement 只决定起始 Position。之后每个 Action Roll 仍按当前场景重新确定 Position/Effect。
- 玩家可在障碍出现后提出 Flashback，补充此前合理的准备。

## 6. Score Action Loop

每次重要行动：
1. 确认目标；
2. 玩家选择符合虚构的 Action；
3. GM 评估 Position；
4. GM 评估 Effect；
5. 玩家选择 Assist / Push / Devil's Bargain（以及合法特殊能力）；
6. 掷骰，读取结果；
7. GM 按 Position 与场景给出后果；
8. 玩家选择 Resistance 或 Armor；
9. 更新 Stress、Harm、Clock、Heat、物品、关系、时间、地点等受影响状态；
10. 共同描述现场的具体变化。

### 6.1 Action event record

重要行动的最小记录：
- action_id / scene_id；
- PC / NPC / Cohort；
- goal 与 Action；
- Position、Effect；
- Dice pool 来源（Action dots、Assist、Push/Devil's Bargain、Ability）；
- Roll result；
- 成果；
- Consequences；
- Resistance / Armor 处理；
- Stress/Harm/Clock/Heat 等实际变化；
- 世界状态影响与可见信息。

普通、无后果的小互动不需要创建事件记录。

### 6.2 Score 中的 Flashback / Teamwork

只在玩家提出或当前局势确实需要时处理。不要每一行动主动提示 Flashback；不要强迫团队行动。Setup 必须具体改善后续行动，而非抽象地给“灵感加成”。

### 6.3 Score close conditions

任务目标完成、行动明确失败、PC 放弃任务，或当前局势已到必须结束的点时，关闭 Score。关闭后按固定结算顺序继续。

## 7. Score Closeout

固定顺序：

1. **Payoff**：按实际任务结果、目标 Tier、是否低调、组织能力与任务收益结算 Rep/Coin。
2. **Heat**：确定基础曝光与修正项；写入 Crew Heat。
3. **Wanted Level**：Heat 达 9 时提升 Wanted，并清除/结转 Heat。
4. **Entanglements**：按 Heat/Wanted 查表掷骰，并确定事件如何落到世界。
5. **Downtime**：恢复 Armor 使用格，PC 进入活动选择。
6. **NPC/Faction Downtime**：推动当前相关派系的计划和项目钟，选择合理的 1–2 个行动。
7. 保存新的 Crew、PC、Faction、Clock 与 Score history 状态。

每个步骤完成后标记已完成。恢复上下文时，不重新执行已提交的 Payoff/Heat/Entanglements；只补完尚未完成的步骤。

## 8. Downtime Runtime

**触发**：Score 结算后进入 Downtime。

执行：
1. 为每名 PC 分配正式活动次数：通常 2；War 时 1。
2. 玩家逐项选择活动；每项先确认可行的方法和必要前提。
3. 朋友/联系人帮助时 +1d。
4. 完成对应骰型和结果。
5. 需要时花 Coin 提升结果档位。
6. 记录 Coin/Rep 支出、Stress、Harm、Heat、项目钟、资源或能力状态变化。
7. 正式活动次数用完后，仍可继续普通 Free Play 行动。
8. Downtime 结束时，处理当前相关派系变化及新机会，回到 Free Play。

Downtime Activity 选择项：
- Acquire Asset；
- Long-Term Project；
- Recover；
- Reduce Heat；
- Train；
- Indulge Vice。

不要把普通社交、访友、散步、调查等活动误算成有限 Downtime Activity；只有上述清单中的活动计入次数，具体以规则文本为准。

## 9. NPC / Faction 的世界推进

使用低成本、目标驱动的推进方式：
- 每个重要 NPC 有自己的目标、偏好行动方法和当前资源/关系。
- 每个关注中的 Faction 有目标、可用手段、对其他派系的关系及必要的项目钟。
- Downtime 时，只推进本阶段与玩家处境相关的派系；每个派系选择 1–2 个合理行动。
- 被暂时忽略的派系可在重新进入焦点时补做合理的时间追赶，不必每轮后台模拟。
- 任何行动都必须满足派系目标、资源、机会及当前世界状态。
- 通过联系人、朋友、Vice purveyor 或可观察事件，把玩家有资格知道的变化传达给他们。

## 10. 未知规则与错误恢复

出现规则不确定时：
1. 锁定本 Campaign 的规则版本与对应 Rule ID。
2. 查本地 Rule_Reference 与私人 SRD 镜像。
3. 若本地条文存在翻译冲突/缺口，再回查已登记的官方来源。
4. 标记 SOURCE / TABLE ADAPTATION / GM INTERPRETATION / UNKNOWN。
5. 只暂停依赖该规则的裁定；其他不相关行动继续。
6. 将新问题登记到 Rule_Reference/RULE_ISSUES.md。

不得用别的系统的相似规则替代未知条款。

## 11. 性能边界

- 新 Campaign / 新 Session：执行一次 Preflight，读取当前快照与需要的规则锚点。
- 同一活动对话：复用已核验版本、PC/Crew Snapshot 和已知规则；不重复扫描全目录。
- 普通行动：不重读全部规则文件。
- 触发某项规则：只调用该 Rule ID。
- 高风险、版本冲突、不可逆后果：回查该条完整规则及特殊能力。
- 只记录对选择、结果、关系或持续世界状态有影响的变化；不为每句台词或轻微动作建立账本。
