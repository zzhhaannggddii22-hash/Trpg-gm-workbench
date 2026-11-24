# 《俯冲》｜Runtime State（GM-only）

 > 当前状态：**模组已结案（CLOSED）。** 第9节及此前内容均为历史运行快照；最新状态以第10节最终结案检查点为准。2026-11-23 首次尝试继续为 NON-CANON。

## 0. 场景续接锚点（2026-11-24 补充）

- Resume Mode：**CLOSED / NO RESUME**。本模组已结案；此前 CONTINUE 仅为历史保存状态。
- Current Scene ID：**CAFE-MEETING-END**（咖啡馆会面结束）。
- Current Scene Status：**CLOSED**。
- Entry Narration Delivered：**Yes**（机构简报室开场已在本轮有效 Session 發生）。
- Last Confirmed Event ID：Daniel 已联系 Marcus，約次日下午 3 点在市中心“老地方”见面；Venice 已接受朋友式合作。
- Pending Player Action：**NONE**。此前取得地址、准备会面均为未执行计划，结案后不再待办。
- Previous Attempt：**NON-CANON**。此前 Cass 首访及其音频设备/客户/R&D 回收分支全部作废，不继承为角色经历、世界事件、物品、伤害、线索或 NPC 知识。
- Player/Character Knowledge Boundary：玩家可能记得作废尝试中的内容；扎雷克与凯瑟琳在正式 CANON 中没有经历该分支，也不得据此行动或获得角色知识。

启动后的更新要求：
1. 机构简报室入口第一次实际呈现后，将场景状态改为 ENTERED / ACTIVE，并记录最后已呈现叙事节点。
2. 后续同一 Session 内或跨对话恢复一律使用 CONTINUE，从最后确认节点接续，不重演机构简报室入口。
3. 只有玩家明确要求重播/回顾时才重新呈现旧内容；回顾不能被记为新的 CANON 事件。
4. 若正式开场前发现状态文件、Session Log 或 Preflight 互相冲突，先修复状态，不开始叙事。


## 1. 模组进度

- 历史状态：有效 Session 01 曾运行至咖啡馆会面结束并暂停；当前已由第10节结案检查点关闭。
- Session：01；当前状态 CLOSED（旧保存点当时曾为 CONTINUE）。
- 游戏内绝对日期：UNKNOWN；相对时间为受害者调查、三晚 Nosedive、次日下午咖啡馆会面。
- 当前地点/场景：咖啡馆会面自然结束；Daniel 是否已离开未确认。
- 当前在场/相关人物：Zarek、Catherine、Venice、Daniel Morris。
- 玩家可知信息：详见 09_PLAYER_NOTES.md。
- 本模组 TABLE CANON：详见 Sessions/SESSION_01.md；2026-11-23 作废尝试仍 NON-CANON，不继承。

## 2. 扎雷克 Session 01 开场状态（已从正式人物卡同步）

- 职级：Associate；职能 R&D；Good Standing。
- Harm 0；Demerits 0；Commendations 7。
- QA 上限/任务间恢复后可用：Professionalism 3/3、Empathy 3/3、Subtlety 3/3、Attentiveness 1/1、Duplicity 1/1、Dynamism 1/1、Initiative 1/1、Persistence 0/0、Presence 0/0；总上限 13。任务间所有 QA 自动、完全恢复。
- Time：已花费 2/30，剩余 28。
- A3 补给「Scoop 的小小心意」1 份；本模组每场正式任务可用一次。
- 橡皮鸭：完好；本场是否使用待玩家决定。
- 涟漪枪：满充 1 发。
- 常规公文包：由扎雷克携带。
- 棒球棍：扎雷克持有。
- 螺丝刀、锤子及《死寂》遗留杂项：已归还。
- Relationship：Sam Mercer 6；Dale Rourke 3；第三槽暂空。
- 凯瑟琳：长期独立 NPC/同行搭档；不再作为机械 Relationship。

## 3. 凯瑟琳 Session 01 开场状态

- 身份：23 岁，R&D 新人，长期独立搭档。
- 9 QA 防护储备：预计任务间恢复后 9/9；仅用于她本人实际受到 Harm 时的防护。
- 不具备异常能力；不是第二名 PC；不进行玩家特工式主动检定。
- 装备/物品：由凯瑟琳按自身风格自主准备；选择轻便、便于携带且在公共场合不引人过度注意的物品。开场装备记录见 Session 01 日志。
- 知识：只知道她实际经历过、被告知或合理推断的内容；不得自动知晓 Nosedive 隐藏真相。

## 4. 五位成员的模组初始状态（SOURCE）

| 成员 | 位置/状态 | 轨道初始视觉状态 | 本桌动态状态 |
|---|---|---|---|
| Venice | La Cave / Nosedive | 1/9 已标记，剩余 8 格 | 尚未接触 |
| Wodge | La Cave / Nosedive | 3/9 已标记，剩余 6 格 | 尚未接触 |
| Mimi | La Cave / Nosedive | 6/9 已标记，剩余 3 格 | 尚未接触 |
| Feast | La Cave / Nosedive | 0/9 已标记，剩余 9 格 | 尚未接触 |
| Leyden | Nosedive 技术设备/电流形态 | 不适用 | 已是异常；尚未接触 |

来源核验：用户上传的官方样章 PDF 第 17 页（印刷页 202–203）清晰展示轨道填色。结合该页“每花费 1 Chaos 标记一格”的规则，按开场已标记进度记录；未标记格即剩余空间。原文未说明预标记对应的具体过往事件，不补写。

## 5. Chaos 与共振者轨道审计（GM-only，强制维护）

**不得因玩家能力提升、场景顺利或叙事节奏而省略资源结算。** Chaos 是异常威胁与任务难度的一部分；漏记生成、消耗或倍率会直接改变遭遇难度。

### 5.1 资源边界
- Leyden 是本模组唯一使用普通 Chaos Pool 的成员；她已是异常。**开场 Chaos Pool = 0**：模组原文未指定其他初始值，按本桌已确认的默认值记录。普通 Chaos Pool 的当前数值及变化始终向玩家公开；个人轨道与 NPC 后台信息仍保密。
- Venice、Wodge、Mimi、Feast 的九格个人轨道是模组独特机制，不得与 Leyden 的 Chaos Pool 混为一谈。她们为创造 Nosedive、让人开心而使用能力时免费；其他用途按 Minor/Major/Extreme 的 1/2/3 费用标记各自轨道。每一格变化都记录到对应成员，不从 Leyden 的 Pool 中扣除，除非规则原文明确要求。
- Leyden 在自己的 Domain 内适用 Domain Benefits。必须分别记录效果是否因 Domain 规则免费显现，以及实际发生的 Chaos 支出；凡实际支出的 Chaos，按中文 v22 规则计算三倍；非整除结果按用户确认的本桌裁定向上取整（TABLE CANON，见系统规则疑点记录 Q02）。不要把 Domain 免费显现与实际支出混成同一个步骤，也不要把该规则套给四位无焦点共振者。
- 若某项规则、初始池数值或倍率交互不确定，暂停该项高影响裁定并回查中文 v22 原文；不得凭印象估算。

### 5.2 逐次流水（每次触发立即记录）
| 序号/场景 | 行动与目标 | 规则依据/效果等级 | 生成 Chaos | 基础消耗 | Domain 调整 | 实际消耗 | Pool 变化前→后 | 个人轨道变化 | 可见征兆/信息层级 |
|---|---|---|---:|---:|---|---:|---|---|---|
| 开场 | 模组未指定初始值，采用默认值 0 | 本桌 Chaos 初始值默认规则 | — | — | — | — | 0 → 0 | Feast 0/9；Venice 1/9；Wodge 3/9；Mimi 6/9 | Pool 数值公开；个人轨道 GM-only |

每次 Chaos 生成、效果发动、费用减免/倍率、轨道标记、轨道填满与转化，都必须有独立流水行；同一轮发生多项变化时逐项列明顺序。每次记录后核算 Pool 余额与轨道格数，不允许只在 Session 结束时凭回忆补账。

### 5.3 Session / Mission 结束核对
- 核对初始值 + 所有生成 − 所有实际支出 = 结束前 Pool；逐项与流水复算。
- 核对四位共振者轨道的每次增减、是否填满、是否转化，以及 Feast 牺牲机制是否触发。
- 按中文 v22 规则确认任务结束时 Chaos Pool 的处置；不得擅自把未用 Chaos 带入下一任务，也不得未经规则依据自行清零。
- 若发生漏记，明确标为记录缺口；回查对话/事件与规则，能确认的修复，无法确认的保留 UNKNOWN，不以有利于玩家或 GM 的方向猜数。
- GM-only 账本保留个人轨道、NPC 后台状态及隐藏触发；普通 Chaos Pool 数值和变化必须向玩家公开。不要因此公开个人九格轨道或 NPC 后台计划。

## 6. 本场事件日志索引

- Session 01：有效日志 `./Sessions/SESSION_01.md`；当前保存点为咖啡馆会面结束。新对话提示词：`./Sessions/SESSION_01_HANDOFF_PROMPT.md`；作废尝试另见 `./Sessions/SESSION_01_ABORTED_2026-11-23.md`。

## 7. 历史重启约束（仅用于隔离作废尝试；当前已完成重启）
- 本次重启前，禁止引用作废尝试中的公寓前台、工作室、音频设备、设备客户、R&D 回收、客户电话及其衍生信息。
- 扎雷克没有因此次作废剧情获得新线索、物品、伤害、QA 变化、奖励或机构委托。
- 凯瑟琳没有因此次作废剧情获得新线索、承诺或资源变化。
- 本次从机构简报重新开始；玩家重新选择调查路径。
- 作废过程仅见 Sessions/SESSION_01_ABORTED_2026-11-23.md 与 QA 事故复盘，不属于世界时间线。

## 8. 待办/UNKNOWN

- 轨道初始进度已由官方样章 PDF 第 17 页（印刷页 202–203）核验；无需再作为待办。
- Minor Effect 的防护用途已由官方样章原文确认：支付 1 格，可保护自己或他人最多 3 Harm；不是增加 HP，也不扣普通 Chaos Pool。
- 核对 Urgency / Urgents 术语及 Playwalled Document W8 的可用性；未解锁前不提供机械能力。
- 结案时回查目标异常、其他成员捕获/逃脱、报告惩罚、奖励与 Loose Ends 规则。
- 确认扎雷克与凯瑟琳的开团装备、补给与防护状态。
- Session 01 场次副本已建立；后续状态变动即时写入本文件及场次日志。


## 9. 有效 Session 01 运行状态（2026-11-24 保存点）

> 本节覆盖文件顶部旧的“重置待开场”状态。旧重置说明保留作历史审计；当前正式 CANON 是重置后重新开始并运行至本节保存点的这一轮。

- 当前状态：**ACTIVE / PAUSED FOR CROSS-SESSION SAVE**。Session 01 已有效开始，现暂停在咖啡馆会面结束后。
- Resume Mode：**CONTINUE**，不是 NEW START。不得重演机构简报室、三名受害者首次调查、前三晚派对或咖啡馆会面。
- Current Scene ID：**CAFE-MEETING-END**。
- Last Confirmed Event：Daniel 已通过短信联系 Marcus；Marcus 回复并约定次日下午 3 点在市中心“老地方”酒吧见面，要求 Daniel 一个人来；Venice 已与 Zarek 握手，接受朋友式合作。
- Next Planned Scene：Daniel 确认酒吧具体名称/地址；次日下午三点，Daniel 单独与 Marcus 会面，Zarek 与 Catherine 在附近观察。此为计划，不是已发生事件。
- 游戏内绝对日期：UNKNOWN；只记录相对时间“次日下午三点”。不得补造日历日期。
- 游戏内时间跨度：受害者调查、三晚 Nosedive 及次日下午咖啡馆会面；没有精确日期/小时的事件不得自行细化。
- 当前场景在场/相关人物：Zarek、Catherine、Venice、Daniel Morris；咖啡馆会面已自然收束。Daniel 是否已离开场所未确认。
- 关键 NPC 知识边界：Daniel、Erin、Venice、Cass、Mimi 各自只知道其实际经历与陈述；Catherine 的跟踪、观察与承诺按其独立行动记录，不自动获得 GM-only 真相。
- 玩家角色状态：Harm 0；Demerits 0；Commendations 7；QA 13/13（Professionalism 3、Empathy 3、Subtlety 3、Attentiveness 1、Duplicity 1、Dynamism 1、Initiative 1）；Time 已花费 2/30，剩余 28；装备与补给无已确认变化；Rubber Duck 未用；Ripple Gun 1 发；A3 补给 1 份未用；Newborn 轨道 UNKNOWN。
- Catherine 防护 QA：9/9；无已确认消耗。
- 本次暂停不是正式任务结案，也未确认结束正式 Session；因此固定 +1 Time 的 Session 结束奖励尚未结算。
- 本 Session 无已记录骰检、异常能力使用、Harm、QA 消耗、Chaos 变化或个人轨道变化。
- NPC/线索的详细增量分别见 03_NPC_BEHAVIOR_LEDGER.md、04_CLUE_AND_SOURCE_LEDGER.md、09_PLAYER_NOTES.md 与 Sessions/SESSION_01.md。

### 9.1 车辆身份隔离（强制）
1. Daniel Morris 的深蓝色四门轿车：已确认车主为 Daniel；Cass 曾接触其门把手并被电击。
2. Marcus 所驾驶的另一辆深色轿车：由 Daniel 描述；尚未实地见到或核实车牌。
3. Erin 照片中的另一名男子：身份未确认；可能是 Daniel 所说的 Marcus，但不得先行认定。
4. 第二晚黑色 SUV、第三晚白色两厢车、第一晚灰色面包车：均是独立目击记录，目前无证据与上述两辆深色轿车关联。
5. 任何新出现车辆必须独立记录颜色、车身类型、车牌（仅当实际可读）、驾驶员和目击来源；禁止仅凭“深色车”合并。

### 9.2 关键事实的证据等级
- 直接观察/物证：深蓝色车牌重复匹配；Daniel 自愿打开后备箱；万用表当时未测出明显电压（仪表电池状态有疑点）；Erin 提供照片（原始拍摄时间地点未核）。
- NPC 自述：Daniel 对 Cass、Matthew、盒子、源头、Marcus、旧仓库的陈述；Erin 对哥哥行为、照片时间地点的陈述；Venice 对合作范围的承诺。
- 转述：Daniel 对 Matthew 的理论，属于 Daniel 转述 Matthew，未经独立核验。
- 推断：照片中的男子可能是 Marcus；多辆深色车是否相关；异常是否沿物品接触传播。以上都不能写成事实。

## 10. 最终结案检查点（2026-11-24｜用户明确确认）

> 本节为最新且唯一有效的最终状态。第9节及此前保存点保留为历史快照，不再作为当前活动状态或续团入口。

- Module Status：**CLOSED / NARRATIVE RESOLVED**。
- Session 01 Status：**CLOSED**；不再 CONTINUE，不再请求 Marcus 地址，不再推进此前计划中的会面。
- Active Branch：CLOSED；历史有效 Session 01 的已呈现事件仍是 TABLE CANON。第一次作废尝试继续保持 NON-CANON。
- Final Narrative Outcome：五名成员与扎雷克一方达成一致；另一名转变为异常的成员处于控制状态，未收容、未消灭。
- Institutional Handoff：机构直接接手后续处理。具体接手过程、人员、方式、地点、处置结果和后续细节均 UNKNOWN；扎雷克与凯瑟琳均不知情。
- Rewards：NONE。无嘉奖、无 Mission MVP、无职能轨迹成长、无 Time 奖励或其他奖励。
- Penalties：NONE。无新增 Demerits、处分或负面评级。
- Character state：本模组结案不改变扎雷克/凯瑟琳的 Harm、QA、装备、持有人、补给、能力或其他资源；保留最后一次实际跑团可核验的值，未知项继续 UNKNOWN。
- Catherine/Zarek relationship：本模组期间关系有进展，记录为质性历史变化；不自动改变机械 Connection。
- Memory boundary：二人共同记忆仅延续至最后一次实际跑团中实际发生/呈现的内容。其后机构接手及处理过程不属于二人记忆，也不属于玩家角色已知信息。
- Pending player action：NONE。No further investigation / no open scene / no next scene.
- Persistence：此节为追加的结案检查点；Session Log、Player Notes、Campaign Handoff 与人物档案需同步引用本检查点。不得删除或覆盖第9节历史记录。
