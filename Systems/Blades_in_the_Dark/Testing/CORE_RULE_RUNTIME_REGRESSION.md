# Blades in the Dark｜Core Runtime Regression Matrix

> Fixture: BITD_CANDIDATE_V01  
> Status: 61/61 SYNTHETIC CASES EXECUTED; LIVE PLAY NOT PERFORMED  
> 结果记录区分：STATIC REVIEW、SYNTHETIC EXECUTION、LIVE PLAY。已执行的固定输入用例见 [Synthetic Execution Report](./SYNTHETIC_EXECUTION_REPORT_2026-11-28.md)。

| ID | 输入/场景 | 预期规则行为 | 结果类型 |
|---|---|---|---|
| BLD-T01 | 角色试图跨过没有危险/麻烦的矮栅栏 | 不掷 Action Roll；直接叙述通过 | Static / Synthetic |
| BLD-T02 | 角色在敌人火力下冲过庭院 | 先确定目标、Action、Position、Effect，再掷 Action Roll；默认 Risky | Synthetic |
| BLD-T03 | 玩家用 Study 去砸开厚重木门 | Action 与虚构不匹配，GM 解释其风险/效果显著较差，玩家可改方法；不自动允许用高评级代替合理行动 | Synthetic |
| BLD-T04 | Risky 行动骰结果为 4/5 | PC 达成目标；GM 按情境给适当后果；玩家可在明确后果后选择 Resistance/Armor | Synthetic |
| BLD-T05 | Desperate Action Roll 结果为 1–3，PC 正与 NPC 争斗 | NPC 在对抗中胜出，NPC 行动体现为 PC 后果；不另为同一交锋重复掷 NPC Action Roll | Synthetic |
| BLD-T06 | Controlled 结果为 4/5 | 允许玩家撤回/改换方法，或达成目标并承受轻微后果 | Synthetic |
| BLD-T07 | GM 先定 Risky/Standard，玩家提出接受 Desperate 以换 Great Effect | 只有虚构情境合理时允许 Position ↔ Effect 交易；不使用固定兑换表 | Synthetic |
| BLD-T08 | Resistance Dice 最高骰为 4 | Consequence 减轻/避免；PC 承受 2 Stress；记录属性组骰池和后果变化 | Synthetic |
| BLD-T09 | Resistance Roll 得到 Critical | 正常抵抗后果，并额外清除 1 Stress | Synthetic |
| BLD-T10 | PC 对 Level 2 Harm 使用 Heavy Armor | 先以 Armor 替代 Resistance；可按规则勾选两格 Armor 进一步降低；同一后果不再重复 Resistance | Synthetic |
| BLD-T11 | Level 3 Harm 槽已满，再承受 Level 3 Harm | 触发灾难性永久后果；是否死亡取决于场景；不能自动当作一般 Level 3 | Synthetic |
| BLD-T12 | 0d Action Roll | 掷 2d 取最低，不得产生 Critical | Static / Synthetic |
| BLD-T13 | 复杂障碍“内部巡逻”持续升级 | 建立以障碍本身命名的 Clock；不以某一种解法命名 | Synthetic |
| BLD-T14 | 调查角色查看可自由取得的公开档案 | 常识/可知信息直接提供；若无危险或不确定，无需掷骰 | Synthetic |
| BLD-T15 | 玩家要知道不确定 NPC 是否背叛 | 用适用 Trait 作 Fortune Roll，不设置 Position/Effect | Synthetic |
| BLD-T16 | Crew 选择 Stealth Plan，Detail 未知 | 可先 Gather Information；Plan + Detail + Load 完成后进行 Engagement Roll | Synthetic |
| BLD-T17 | Engagement Roll 为 Critical | PC 已越过第一个障碍，并以 Controlled Position 进入更深处的下一行动；该初始 Position 只作为开场，之后的 Action Roll 按新场景重新评估 | Synthetic |
| BLD-T18 | Score 中遇到卫兵，玩家 Flashback 曾买通过守卫 | GM 按复杂程度设 0/1/2+ Stress；危险行动掷 Action Roll，不撤销已确立事实 | Synthetic |
| BLD-T19 | Group Action 三名 PC 结果 6、4/5、1–3 | 全组按最高结果处理；Leader 对 1–3 成员承受 1 Stress | Synthetic |
| BLD-T20 | Score 结束后连续结算 | 顺序为 Payoff → Heat → Entanglements → Downtime；禁止跳步或重复结算 | Synthetic |
| BLD-T21 | Downtime 中 PC 进行 Long-Term Project，掷出 Critical | 推进 5 格；Coin 可以在掷后提升结果等级 | Static / Synthetic |
| BLD-T22 | PC 有两个 Downtime Activities 后继续访友/普通调查 | 普通 Free Play 不消耗活动次数；只有正式六种活动受预算限制 | Synthetic |
| BLD-T23 | Crew Heat 为 8，获得 3 Heat | Wanted Level +1；Heat 清除并结转超额 2 Heat | Synthetic |
| BLD-T24 | Wanted Level 为 0，掷 Entanglement | 掷 2d 取最低；根据 Heat 档读表 | Static / Synthetic |
| BLD-T25 | Crew 有 3 Turf，Rep track 达 9 | 晋级阈值为 12-3=9；晋级后保留 Turf | Synthetic |
| BLD-T26 | Crew 与某派系 Status -3 | 进入 War；每 Score +1 Heat、暂时失去 Hold、PC Downtime 变为每人 1 次、产生 Coin 的 Claims 收入减半（向下取整），按规则处理恢复 | Synthetic |
| BLD-T27 | 只与一个无关派系有关的城内新闻 | 不为了模拟世界而推进所有派系；只更新会影响 PC/Crew 的对象 | Static / Synthetic |
| BLD-T28 | 当前桌绑定 Triangle Agency，玩家提到 Flashback | 识别其属于 Blades；不加载或执行 Blades 机制 | Cross-system |
| BLD-T29 | 当前桌绑定 Cairn，玩家提到 Crew Tier | 不把 Tier/Heat/Downtime 资源移入 Cairn；只有明确切换系统才加载 | Cross-system |
| BLD-T30 | 上下文压缩后恢复 Score closeout | 检查已提交步骤，只执行未完成字段；不得重复 Payoff、Heat 或 Entanglement | Synthetic |
| BLD-T31 | PC 拥有 Battleborn，进入战斗并选择用 Special Armor 强推 | 只在对应战斗/行动触发；勾选 Special Armor，免除通常 Push 的 2 Stress；在规则规定的恢复时点复原 | Synthetic |
| BLD-T32 | PC 拥有 Tough as Nails，受到 Level 3 Harm | 依能力将伤害造成的惩罚降低一级，但保留原始伤害等级供后续恢复；Level 4 仍致命 | Synthetic |
| BLD-T33 | PC 未拥有 Ghost Mind，场景出现灵体 | 不自动获得 Ghost Mind 的感知/调查加成；按普通规则与角色可知信息处理 | Synthetic |
| BLD-T34 | Crew 拥有 Pack Rats，执行 Acquire Asset | 在对应 Downtime 活动触发时按能力给 +1d；不影响无关骰型 | Synthetic |
| BLD-T35 | 当前 Crew 未选择 War Dogs，进入 War | 应用基础 War 的 Hold / Downtime 惩罚；不把未拥有的 Crew Ability 当作默认豁免 | Synthetic |
| BLD-T36 | PC 获得新 Ability 或 Crew 更换/增加 Ability | 更新已拥有能力清单；后续只对该清单中的能力做触发检查 | Static / Synthetic |
| BLD-T37 | PC 使用一次普通 Resistance，另有特殊 Armor 能力 | 先确认能力是否允许对该后果使用 Special Armor；避免将能力成本、普通 Armor 与 Resistance 重复套用 | Synthetic |
| BLD-T38 | PC 接受 Devil's Bargain 获得 +1d，同时 Push Yourself 获得 +1 Effect | 合法组合：Devil's Bargain 提供唯一的额外 +1d 来源，Push 为 +1 Effect 支付 2 Stress；不能再额外 Push 获得第二个 +1d | Synthetic |
| BLD-T39 | Crew 在自家 Hunting Grounds 执行 Preferred Operation | 相关 Gather Information +1d，额外获得一次只用于该 Score 准备的免费 Downtime Activity | Synthetic |
| BLD-T40 | Crew 沿 Claim Map 连接路径夺取 Claim | 作为普通 Score 处理；成功后转移 Claim、更新双方 Faction Status，并开始获得该 Claim 收益 | Synthetic |
| BLD-T41 | Crew 尝试越过连接路线直接夺取远端 Claim | 可以尝试，但需额外努力/调查，不能自动按常规路径难度处理 | Synthetic |
| BLD-T42 | Crew 失去 Lair | 暂停所有 Claim 收益，直到通过 Score 恢复/建立新 Lair | Synthetic |
| BLD-T43 | 新 Crew 创建时选择 Favored Contact 与两项额外 Upgrade | 分别更新升级帮助/受损的派系状态与联系人相关派系状态，不得漏记或重复 | Synthetic |
| BLD-T44 | Cutter 拥有 Vigorous，开始一次 Recover | Healing Clock 有一格永久起始进度，治疗处置骰 +1d；不因普通恢复重复填入永久格 | Synthetic |
| BLD-T45 | Leech 拥有 Venomous，使用其选定毒药/药物 | 角色对选定物质免疫；Push Yourself 后才可由皮肤/唾液/呼气分泌，不自动免费触发 | Synthetic |
| BLD-T46 | PC 选择 Heavy Load 携带 Armor | Standard Armor 占 2 Load，Heavy 加 3（总计 5）；没有携带不能以普通 Armor 处理后果；已标记 Armor 在下一次 Score 选择 Load 时恢复，而非进入 Downtime 时恢复 | Static / Synthetic |
| BLD-T47 | PC 声称使用 Special Armor，但没有相应 Playbook Ability | 不具备使用资格；不能仅凭角色卡上的空格触发 Special Armor | Synthetic |
| BLD-T48 | PC 自行 Recover | PC 消耗自己的 Downtime Activity，额外承受 2 Stress，完成正常治疗掷骰 | Synthetic |
| BLD-T49 | PC 没有治疗者但选择 Tough It Out | 承受 1 Stress，以 0d（2d 取低）推进 Healing Clock | Synthetic |
| BLD-T50 | A 治疗 B 的 Harm | B 花费自己的 Recover Activity；治疗者不消耗自己的 Downtime Activity | Synthetic |
| BLD-T51 | PC 的 Loadout 已满，行动中想临时声明重甲 | Load limit 不允许，除非有明确能力/虚构来源提高 Load；不得免费增加 Armor | Synthetic |
| BLD-T52 | PC Push Yourself 同时选择 +1d 与 +1 Effect | 每项收益各支付 2 Stress，共 4 Stress；每项每次行动最多选择一次 | Synthetic |
| BLD-T53 | PC Push Yourself 选择 +1d，再接受 Devil's Bargain | 不合法：同一额外骰来源只能二选一；改选 Push +1 Effect + Devil's Bargain +1d 才可组合 | Synthetic |
| BLD-T54 | Lurk 拥有 Shadow，面对侦测/安保后果 | 可用 Special Armor 抵抗该类后果，或 Push Yourself 用于运动/潜行；其他后果不能泛化套用 | Synthetic |

| BLD-T55 | Crew 招募 Gang / Expert Cohort，并派遣其执行 Type 匹配与不匹配的任务 | Gang Quality/Scale = Crew Tier；Expert Quality = Tier+1、Scale 0；Type 不匹配时 Quality 0；最多两个 Type | Synthetic |
| BLD-T56 | 创建 Cohort 时选择 Edges / Flaws | 选择 1–2 个 Edge，并选择相同数量 Flaw；其影响按描述在虚构中体现，不自动变成通用数值加成 | Synthetic |
| BLD-T57 | Cohort 先后承受 Weakened、Impaired、Broken、Dead，并进入 Downtime | Harm 逐级产生 Effect 降低、Quality -1d、无法行动、摧毁；Downtime 条件允许时恢复 1 级，PC 花 1 Activity 帮助则恢复 2 级 | Synthetic |
| BLD-T58 | Cohort 被摧毁后 Crew 招募替代者 | 支付 Crew Tier+2 Coin，并花费 2 个 Downtime Activities；不得免费重置 Cohort | Synthetic |
| BLD-T59 | Score 帮助/伤害多个 Faction，且任务完全低调 | 有明确受益/受损派系时按规则调整 Status；完全低调且无人知晓时通常不改变 Status | Synthetic |
| BLD-T60 | Crew 与任意派系处于 War，拥有产生 Coin 的 Claim | War 期间此类 Claim 的 Coin 收入减半并向下取整；与 +1 Heat、-1 Hold、Downtime 活动减少分别记录 | Synthetic |
| BLD-T61 | Downtime 推进当前关注派系的项目钟，另有暂时忽略的派系 | 只推进当前相关派系；需要追赶时以派系 Tier Fortune Roll，按 1–3/4–5/6/Critical 推进 1/2/3/5 格 | Synthetic |

## 结果登记

| 验证阶段 | 日期 | 结果 | 证据 |
|---|---|---|---|
| Source review | 2026-11-28 | 已完成主要 SRD 章节校读与部分官方 v8.2 交叉核验 | 中文 SRD 私人镜像、官方 Player's Kit v8.2 |
| Static document review | 2026-11-28 | 文档已建立，细节仍需第二轮审阅 | 本测试矩阵、Runtime、Index、Protocol |
| Synthetic execution | 2026-11-28 | 61/61 固定输入用例完成三轮人工桌面推演；非自动化测试 | [首轮报告](./SYNTHETIC_EXECUTION_REPORT_2026-11-28.md)；[第二轮报告](./SYNTHETIC_EXECUTION_REPORT_2026-11-28_R2.md)；[第三轮报告](./SYNTHETIC_EXECUTION_REPORT_2026-11-28_R3.md) |
| Live play | Pending | 尚无实战证据 | — |

## 当前开放风险

- 七种核心 PC Playbook 与六类 Crew 的 Special Ability 已有摘要索引；摘要不是完整卡面，实际建卡与关键触发仍须回查当前版本原文。
- 六类 Crew 的完整升级与 Claim 表尚未逐条录入，需要按实际 Campaign 类型查表。
- Doskvol 专有设定、官方 NPC、地区、地图和非 SRD 材料需要合法来源。
- 中文 SRD 的修订号未明确，正式 Campaign 前必须锁定实际使用版本。
