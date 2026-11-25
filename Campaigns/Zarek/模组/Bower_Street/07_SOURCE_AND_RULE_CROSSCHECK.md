# Bower Street｜Source & Rule Crosscheck

> 当前版本：v1.1-audit-fix｜状态：BLOCKED（完成针对性修订，等待独立复审与最终 Preflight）
> 本文件记录来源核验、独立审查、实际修订和复审边界；不把案头推演冒充真实玩家测试。

## 一、权威来源与版本边界

- 模组：Haunted Table Games，《The Vault: Missions for Triangle Agency》，Kay W.
- Campaign 原先使用的 Library 文件：`the_vault_zh.docx`，file ID `file_00000000dc5082079c9c18b481a13486`。
- 模组定位：源 PDF 41–49；印刷页 76–93。
- 本次独立审查：用户提供的 `Bower_Street_GM_Audit.md`，审查基线为 main `4e85fc5f2c1ec4343099326b54d5d930894695db`。
- 审查者报告说明：其核验使用公开中文 v22 交付中的同名 DOCX 与同版可检索译稿；公开 DOCX 已核对通话时间，章节逐项比较使用同版译稿。
- **版本限制**：尚未确认公开交付与用户 Library 副本逐字一致；英文出版物亦未逐字复核。涉及翻译差异的判断应保留来源说明，不声称已经完成英文原版核对。
- 规则：Triangle Agency 中文 v22；本 Campaign 绑定 `Campaigns/Zarek/SYSTEM_BINDING.md`，桌裁以 `Campaigns/Zarek/RULE_ADJUDICATIONS.md` 和其批准历史为准。

## 二、原文与规则核验状态

| 项目 | 当前状态 | 依据与限制 |
|---|---|---|
| Focus / Domain / Appearance / Impulse、历史与扩张 | VERIFIED | 模组印刷页 78–79。初始 Domain 为地下室；逃离阶段才明确扩展至整栋房屋。 |
| Domain 费用换算 | VERIFIED | Zarek Q01/Q02：域内费用 ≤3 免费；>3 乘三并向上取整。模组值 2/4/5/6/8 换算为域内 0/12/15/18/24。域外不套用域内免费。 |
| Corrupt 在 Evie 卧室的应用 | VERIFIED / 修订 | 模组措辞是异常“尝试”腐化；首次楼上调查在 Domain 外，标示值 2。不能写成入门即自动成功，更不能在 Pool=0 时免费毁掉布娃娃。 |
| Manifest：Shape / Vision 与手机猫 | INCOMPLETE | 审查报告指出 Shape 可用被捕者熟悉形象呼救引去地下室；Vision 使直接触碰者陷入自身舒适记忆。两只猫的费用是一次还是分别计算，原文未明确，保持 UNKNOWN。 |
| Attract / Expand / Displace | VERIFIED（效果摘要） | 模组印刷页 80–81；具体现场触发仍需依当时场景和 Pool 处理，不按固定脚本逐项自动播放。 |
| 开场 Chaos Pool | UNKNOWN / PRE-FLIGHT REQUIRED | 模组没有专属初始值。v22 有分部累计 Loose Ends 规则（审查报告定位为印刷页 22、译稿 R5755–5776）；Q01–Q04 没有批准废除该规则。不得仅凭其他模组曾从 0 开始就固定本场为 0。须在 Preflight 结合扎雷克当前分部状态计算并公开。 |
| 911 通话时间 | VERIFIED / 修订 | 通话发生于一周前；机构昨晚截获。二者不可混写。 |
| 晨会入口 | VERIFIED / 已补回 | 模组印刷页 81：重逢的旧猫、蓝色溢水浴缸、旧友来电、Evie 电动车采访、CR 壁画。均为可选切入点，不是强制剧情。 |
| 调查地点、物件与钥匙 | INCOMPLETE / 已修订 | 项圈归棚屋；厨房钥匙盒含车库侧门、棚屋与车钥匙；门后声音及客厅追踪胶带/氯味补回。账单属于 Lewis，不能证明 Hamamoto 夫妇婚姻。 |
| 泳池取钥匙 | VERIFIED / 已修订 | 可见池底反光；特定角度看似盛满蓝水。明确危险分支是特工爬入池内取钥匙。池外遥取的统一后果 UNKNOWN。 |
| NPC 知识边界 | VERIFIED / 已修订 | Justin、Fumiko、Rebecca、Jodie、Caitlin、Evie 分别按原文知识和现场信息呈现；Jodie 本人受记忆改写只标 GM INFERENCE，不作为原文事实。 |
| 地下室七个人形身份 | UNKNOWN | 原文未逐一确认；不得映射到 Jacob Mills、Caleb Coleman 或其他失踪者。 |
| Caitlin / Fumiko 恢复与束缚状态 | INCOMPLETE / 已修订 | 认知恢复、解除束缚、位置和带离地下室分别记录；只救一人不自动恢复另一人。未写明的专属即时反应保持 UNKNOWN。 |
| 厨房逃离引路者 | VERIFIED / 修订 | 原文由狗引路；不可写成 Caitlin 引路。 |
| 真实 Evie 联系耗尽路径 | VERIFIED / 修订 | 关键时刻由 Caitlin 与真实 Evie 建立联系；仅找到号码、发送未读消息或此前联系不满足条件。 |
| Ripple Gun / Normal Briefcase | INCOMPLETE / 已修订 | Ripple Gun 需有可指定、可见且无遮挡的 VHS 带体目标，并核对持有人与充能；摧毁显现版本不等于收容整个异常。公文包仍需满足耗尽条件。 |
| 任务结果、奖励与 Loose Ends | INCOMPLETE / 已补充 | 收容：全体特工 +3 Commendations；中和：无额外奖惩；逃脱：全体特工 +3 Demerits，另 +7 分部 Loose Ends。Loose Ends 按 v22 实际遗留风险核算，不按知情 NPC 人头计。 |
| Aftermath | VERIFIED / 修订 | Justin、Rebecca 的怀旧宿醉按原文呈现；异常逃脱后追逐 Evie 周围的人是可能后续，不写成已经发生或必然发生。 |
| QA / Burnout / Harm 与装备 | INCOMPLETE | 依 v22 与 Q03/Q04 处理；本模组未给异常固定 Harm/HP 阈值、伤害数值或追逐轮数，不补造。正式卡与交接旧快照冲突的活力/主动 QA 以正式人物卡 §6 的当前 1/1 为准，除非有更新的实际消耗事件。 |

## 三、Campaign 桌裁核对

- Q01：Domain 内费用 ≤3 免费。
- Q02：适用域界花费调整时，标示费用乘三后向上取整。
- 对应域内换算：Corrupt 2 → 0；Manifest 4 → 12；Attract 5 → 15；Expand 6 → 18；Displace 8 → 24。
- 以上只对 Domain 内效果适用。Evie 卧室首次调查仍在域外，Corrupt 标示值为 2；不得套用域内免费。
- Q03：人寿保单保障项目 1 的特定 QA 防护例外；不可泛化为普通检定跨素质挪用 QA。
- Q04：先检查 Burnout，再检查 QA；同次 QA 消耗不在同次检定即时产生 Burnout。
- 当前开局普通 Chaos Pool 仍待 Preflight 按 v22 分部累计 Loose Ends 规则和当前角色分部状态计算；本文件不预设数值。

## 四、独立审查记录

### 外部审查（用户提供，2026-11-25）

- 审查结论：BLOCKED。
- 审查基线：main `4e85fc5`。
- 审查范围：模组八份文件、目录标准、战役 README、SYSTEM_BINDING、桌裁与批准记录、正式人物卡、战役交接；15 条单人玩家路径为案头推演，无真实玩家测试。
- 主要阻塞：Evie 卧室 Corrupt 被写成进入即触发；泳池危险条件和可见征兆失真。
- 其他发现：911 通话与截获时间混淆；厨房引路者写错；Caitlin/真实 Evie 联系条件过宽；地点物件位置冲突；Manifest 次级猫效果信息不足；结局与 Loose Ends 结算不完整；开局 Pool 与分部累计规则、正式人物卡资源与旧交接快照有冲突。
- 审查者确认 Domain 五项换算 0/12/15/18/24 正确。
- 未核实：用户 Library 副本与公开译本逐字一致性、英文原版对应；这些不确定性继续保留。

## 五、本轮修订记录（2026-11-25）

本轮在分支 `fix/bower-street-audit-iteration-2` 基于审查基线进行，尚未合并 main。

### 已修订
1. **01_GM_PREP.md**
   - 将状态改为 BLOCKED，修正 911 时间线。
   - 细化 Domain 边界和 Evie 卧室 Corrupt：尝试而非自动成功、域外费用 2、Pool=0 不可免费发动。
   - 恢复泳池反光/蓝水征兆，区分入池取钥匙与池外取钥匙。
   - 补回晨会入口、客厅追踪线索、厨房钥匙盒内容与门后声音。
   - 修正项圈位置、Lewis 账单的证据用途、厨房狗引路。
   - 补充 Manifest Shape/Vision 与手机猫的效果边界，计费粒度保持 UNKNOWN。
   - 将 Caitlin/Fumiko 的认知、束缚、位置、撤离状态分开记录。
   - 收紧 Caitlin 与真实 Evie 联系的耗尽条件。
   - 明确 Ripple Gun 的可见目标、射界、持有人和充能检查。
   - 修正 Aftermath 的确定性，并补入任务结果、奖励/处分和分部 Loose Ends 规则。
2. **02_NAME_INDEX.md**
   - Evie 长幼关系标 UNKNOWN。
   - 明确项圈在棚屋，扩充 Cooper、Felix、Ollie、异常猫、引路狗、厨房钥匙盒、布娃娃与婚戒索引。
3. **03_RUNTIME_STATE.md**
   - 开局 Chaos Pool 不再硬编码 0；改为 Preflight 依据分部累计 Loose Ends 规则计算。
   - 标记 BLOCKED FOR PREFLIGHT，并记录角色 QA 旧交接快照与正式卡差异。
4. **Campaign README**
   - 同步用户已选择 Bower Street、当前备团 BLOCKED 的状态。
   - 修正活力/主动当前 QA 为正式人物卡 §6 所载 1/1。
5. **GM Prep 状态**
   - 增加针对性现场判定卡，便于桌上按触发条件、资源、状态和目标可见性执行。

### 尚需完成
- 第二轮独立模型复审尚未执行；本轮模型自检不能冒充独立审查。
- 对照用户 Library 源文件与公开同版译稿的逐字一致性仍 UNKNOWN。
- 角色当前分部累计 Loose Ends 与开局普通 Chaos Pool 必须在 Preflight 前核算。
- 真实玩家测试尚未执行。

## 六、第二轮定向复审（本轮自检；非独立审查）

| 场景 | 修订后预期裁定 | 状态 |
|---|---|---|
| 零 Pool 首次进入 Evie 卧室 | 首次楼上调查在 Domain 外；Corrupt 标示值 2；Pool=0 不可发动，不自动毁布娃娃；先呈现原文“尝试腐化”而非必然成功。 | PASS（文本逻辑复核） |
| 池外取钥匙 | 先呈现反光/蓝水征兆；不把池外取物自动判为入池溺水；工具/能力的可达性按行动判定，具体异常后果 UNKNOWN。 | PASS（边界已标明；具体行动待现场） |
| 入池取钥匙 | 只有角色实际爬入池中取钥匙才触发原文明确的灌入黏液、受困与溺水危险；单人救援不能免费增加帮手或固定轮数。 | PASS（触发条件已区分） |
| 单人先救 Fumiko | Fumiko 的认知/束缚/位置/带离状态单独记录；Caitlin 不自动恢复；切断束缚仍触发反击；未写明的专属反应保留 UNKNOWN。 | PASS（状态模型复核） |
| 胶带遮挡前后开枪 | 带体可见、可指定且射界无遮挡时才有 Ripple Gun 射击窗口；被遮蔽不可指定时不能射击；检查持有人和充能；击毁显现不等于收容。 | PASS（条件逻辑复核） |

本轮 PASS 仅表示文档指令之间逻辑一致，未证明实际玩家一定能识别或利用这些窗口。正式放行前仍须高级模型/独立审查复核本轮修订差异。

## 七、剩余 UNKNOWN 与 Preflight 闸门

- 两只异常猫的 Manifest 费用是一次还是分别计费：UNKNOWN。
- 池外遥取铜钥匙的具体异常后果：UNKNOWN；按实际行动与规则裁定。
- 只唤醒一名受害者后另一人的专属即时反应：UNKNOWN。
- 地下室七个人形的个体身份：UNKNOWN。
- Evie 与 Caitlin 双胞胎的长幼关系：UNKNOWN。
- 用户 Library 中文模组副本与公开译本的逐字一致性：UNKNOWN。
- 开局普通 Chaos Pool：须按当前 R&D 分部累计 Loose Ends 规则和角色当前分部状态计算；未完成前不得开始 Preflight。
- 正式人物卡 §6 记载 Dynamism 1/1、Initiative 1/1；旧交接历史快照记载 0/1 或 0/0。以正式卡当前值为基线，除非找到更新的实际消耗事件。

**当前结论：BLOCKED。** 本轮完成了针对性修订和文档自检，但尚未取得独立第二轮审查。不得改写为 READY，也不得开始正式 Preflight 或跑团。
