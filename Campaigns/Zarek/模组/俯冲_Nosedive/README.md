# 《俯冲》（Nosedive）｜模组档案

> 状态：**Prep QA CLOSED；首次 Preflight 已执行。2026-11-23 的第一次 Session 01 尝试作废（NON-CANON）；随后已从机构简报室重新开团。有效 Session 01 现已保存并暂停，当前续接点为咖啡馆会面结束、等待次日下午与 Marcus 的约见。权威进度见 08_RUNTIME_STATE.md 与 Sessions/SESSION_01.md。**
> 系统：Triangle Agency 中文 v22。规则唯一权威为用户指定的中文 v22。
> 信息等级：本目录除明确标注玩家侧的文件外，均为 GM-only。

## 文件索引

- [01_GM_PREP.md](./01_GM_PREP.md)：原文基石、任务结构、异常机制、场景与结局。
- [02_NAME_INDEX.md](./02_NAME_INDEX.md)：规范 ID 与中英文名称。
- [03_NPC_BEHAVIOR_LEDGER.md](./03_NPC_BEHAVIOR_LEDGER.md)：五位 Nosedive 成员及重要外围 NPC 的独立动机、知识和行为。
- [04_CLUE_AND_SOURCE_LEDGER.md](./04_CLUE_AND_SOURCE_LEDGER.md)：调查线索、来源、获取方式、替代路径与收束条件。
- [05_SOLO_ADAPTATION_AND_SESSION_PLAN.md](./05_SOLO_ADAPTATION_AND_SESSION_PLAN.md)：单人桌适配边界、多 Session 节奏与叙事执行。
- [06_RUNTIME_QUICK_REFERENCE.md](./06_RUNTIME_QUICK_REFERENCE.md)：现场运行入口与关键索引。
- [07_SOURCE_AND_RULE_CROSSCHECK.md](./07_SOURCE_AND_RULE_CROSSCHECK.md)：来源、版本、规则核验与资料缺口。
- [08_RUNTIME_STATE.md](./08_RUNTIME_STATE.md)：本模组唯一有效的当前运行状态；开团前从正式人物卡同步。
- [PREFLIGHT_2026-11-23.md](./PREFLIGHT_2026-11-23.md)：首次 Preflight 记录；玩家确认项已完成，等待明确开团指令。
- [09_PLAYER_NOTES.md](./09_PLAYER_NOTES.md)：玩家角色已知信息；目前为空。
- [10_COMMUNITY_AND_PLAYFLOW_RESEARCH.md](./10_COMMUNITY_AND_PLAYFLOW_RESEARCH.md)：官方任务流程、社区主持经验、实际游玩反馈及其对本桌的可执行建议。
- [11_NARRATIVE_PRESENTATION_MATERIALS.md](./11_NARRATIVE_PRESENTATION_MATERIALS.md)：场景感官锚点、异常呈现、动作节拍与对话演出建议。
- [12_NPC_FIRST_CONTACT_CARDS.md](./12_NPC_FIRST_CONTACT_CARDS.md)：受害者首次接触事实卡；开场与首次拜访前必须读取。
- [运行事故复盘](./QA/2026-11-23_RUNTIME_INCIDENT_POSTMORTEM.md)：本次事实偏离的根因、影响范围、修复与回归验证。
- [Sessions/SESSION_01.md](./Sessions/SESSION_01.md)：有效 Session 01 完整事实日志与当前保存点。
- [Sessions/SESSION_01_HANDOFF_PROMPT.md](./Sessions/SESSION_01_HANDOFF_PROMPT.md)：新对话恢复提示词。
- `Sessions/SESSION_01_ABORTED_2026-11-23.md`：第一次作废尝试，仅供事故审计，NON-CANON。

## 模组信息

- 来源：Haunted Table Games，《The Vault: Missions for Triangle Agency》。
- 作者：Caleb Zane Huett；插画：Marie Enger。
- 原文位置：中文 v22《密库》母稿，源 PDF 页 102–110，印刷页 198–215。
- 官方产品版本：The Vault 数字版 1.2；官方样章包含 Dead Quiet 与 Nosedive。官方页面另列 Quick Patch 1.01；已核对补丁说明，未列出 Nosedive 专项修正。
- 主题：移动派对 Nosedive、五位成员、共振者的稳定性与自主选择、社群保护与机构任务之间的冲突。

## 流程状态

| 环节 | 状态 |
|---|---|
| 模组选择 | 已确认 |
| 中文 v22 母稿读取 | 已完成 |
| 事实与场景提取 | 初版已完成 |
| 单人桌适配设计 | 初版完成 |
| 规则原文交叉核验 | 初版完成；官方样章轨道图像已核验 |
| 官方/社区流程研究 | 已完成初轮；见 10 号文件 |
| 运行索引与状态文件 | 已建立 |
| Prep QA | CLOSED（2026-11-23）；报告指定阻断项全部关闭，无开放阻断项 |
| 第一次 Preflight | 已执行（2026-11-23）；开团前玩家确认项已完成 |
| Session 01 | 已有效开团；当前暂停保存，等待跨对话恢复 |

## 已解决的备团核验项

四条九格轨道的初始填色已由用户上传的官方样章 PDF 核验：PDF 第 17 页（印刷页 202–203）清晰显示 Feast 0/9、Venice 1/9、Wodge 3/9、Mimi 6/9 已标记。结合同页“每花费 1 Chaos 标记一格”的规则，按开场已标记进度处理；剩余空间分别为 9、8、6、3 格。原文未说明预标记对应的具体过往事件，不补写。

独立 Prep QA 原始结论为 FAIL（2 项 Critical、11 项 Major、5 项 Minor）；报告指定阻断项已全部修订并完成定向复核，**Prep QA 正式关闭（CLOSED），无开放阻断项**。原始 FAIL 作为审计历史保留。逐项处理见 [QA 修订与关闭记录](./QA/2026-11-23_PREP_QA_REVISION_LOG.md)。原始 25 页 PDF 为本次对话上传的 GM-only 审查附件；GitHub 连接不支持通过此流程上传二进制 PDF，因此此处保存可追溯的逐项记录，不声称 PDF 已入库。Minor Effect 防护用途已按官方样章明确落实。

## 保密约定

隐藏真相、NPC 秘密、调查答案、成员轨道和结局分支均属于 GM-only。不得在普通玩家可见简报或便笺中透露。玩家侧材料只记录扎雷克通过合理渠道实际获知的内容。

## 叙事原则

本模组明确采用 **Show, don't tell**：
- 通过动作、选择、空间、声音、物件与人物之间的反应呈现情绪、关系和动机。
- 不让 NPC 轮流讲解自己的心理、背景或阵营立场。
- 不替玩家总结隐藏真相；提供可观察证据，让玩家自己推断。
- 细节服务于行动、氛围、关系或判断；重复流程与低价值信息快速压缩。
- 不把“展示”误解成每段都写成长篇描写。克制、具体、留白优先。

## 2026-11-24｜用户确认的正式结案（覆盖此前等待续团状态）

> **状态：CLOSED / NARRATIVE RESOLVED / NO REWARDS / NO PENALTIES。** 本节是用户明确确认的最终剧情结局与结算边界，覆盖本 README、Runtime、Session 交接中所有等待 Marcus 会面、待继续调查或尚未结案的旧状态描述。旧记录保留为当时真实发生的历史，不删除、不改写。

### 结案 CANON
- 五名成员已与扎雷克一方达成一致。
- 另有一名转变为异常的成员处于控制状态；未收容、未消灭。该状态按用户明确确认记录，不推断具体控制机制、地点、负责人员或后续处置细节。
- 机构直接接手并处理后续事项。扎雷克与凯瑟琳不清楚交接后的具体过程；不得把机构后续行动写成二人的亲历、对话、记忆或玩家已知信息。
- 叙事上本模组已处理完毕，不再有待继续的调查、Marcus 约见或其他活动剧情。此前计划与未确认线索仅作为历史记录保留，不视为已执行，也不自动补齐。

### 奖励与惩罚
- 本模组不结算任何奖励：无任务嘉奖、无 Mission MVP、无职能轨迹成长、无 Time 奖励或其他奖励。
- 本模组不结算任何惩罚：无新增 Demerits、无处分、无负面任务评级或其他惩罚。
- 本模组结案不改变扎雷克既有 Harm、QA、Commendations、Demerits、Time、装备、补给或能力状态。没有明确发生的变化保持原值；未知项目仍为 UNKNOWN。

### 扎雷克与凯瑟琳的记忆和关系
- 扎雷克与凯瑟琳在最后一次实际跑团中共同经历的内容，保留为二人的记忆。
- 两人的历史关系在本模组中有进展，并作为质性关系事实记录；不据此擅自增加机械 Connection 数值或其他资源。
- 二人的共同记忆止于最后一次实际跑团的内容。之后发生了什么，二人均不清楚。
- 机构接手后的处理属于 GM-only 世界状态的未知后续；除非未来通过合理渠道披露，不得进入扎雷克或凯瑟琳的个人记忆、玩家便笺或可知事实。

### 归档规则
- 将模组标记为已结案、Session 01 已关闭；不得从旧 Handoff 继续剧情。
- 原始 Session Log、Runtime 历史保存点、玩家便笺和事故记录保留。以追加结案记录形成新的最终检查点。
- 当前运行入口应将本模组列为 CLOSED，不再将其列为下一场正式任务。
