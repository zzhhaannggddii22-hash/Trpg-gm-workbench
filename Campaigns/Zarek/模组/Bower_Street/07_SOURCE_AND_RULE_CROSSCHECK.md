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
| Manifest：Shape / Vision；手机囚禁型次级异常猫 | VERIFIED / 部分 UNKNOWN | Shape 使用被捕者熟悉形象呼救引去地下室；Vision 使直接触碰物件/不太聪明生物者陷入自身舒适记忆。手机充电开机后显现两只囚禁型次级异常猫，触碰猫会触发囚禁效果；两只猫的费用按一次还是分别计算，原文未明确，保持 UNKNOWN。 |
| Attract / Expand / Displace | VERIFIED（效果摘要） | 模组印刷页 80–81；具体现场触发仍需依当时场景和 Pool 处理，不按固定脚本逐项自动播放。 |
| 开场 Chaos Pool | UNKNOWN / PRE-FLIGHT REQUIRED | 模组没有专属初始值。v22 有地方分部累计 Loose Ends 规则；正式人物卡的 R&D 是职能，不是分部。须在 Preflight 内核实实际所属地方分部及累计值，计算并公开开局 Pool；须在正式场景开始前完成。 |
| 911 通话时间 | VERIFIED / 修订 | 通话发生于一周前；机构昨晚截获。二者不可混写。 |
| 晨会入口 | VERIFIED / 已补回 | 模组印刷页 81：重逢的旧猫、蓝色溢水浴缸、旧友来电、Evie 电动车采访、CR 壁画。均为可选切入点，不是强制剧情。 |
| 调查地点、物件与钥匙 | INCOMPLETE / 已修订 | 项圈归棚屋；厨房钥匙盒含车库侧门、棚屋与车钥匙；门后声音及客厅追踪胶带/氯味补回。账单属于 Lewis，不能证明 Hamamoto 夫妇婚姻。 |
| 泳池取钥匙 | VERIFIED / 已修订 | 可见池底反光；特定角度看似盛满蓝水。明确危险分支是特工爬入池内取钥匙。池外遥取的统一后果 UNKNOWN。 |
| NPC 知识边界 | INCOMPLETE / 已修订 | 六名 NPC 的基本知识边界保留；Jodie 的 Felix 往事、邻里流言、夫妇争吵按不同对话条件披露；“Evie 搬入”上游来源 UNKNOWN。 |
| 地下室七个人形身份 | UNKNOWN | 原文未逐一确认；不得映射到 Jacob Mills、Caleb Coleman 或其他失踪者。 |
| Caitlin / Fumiko 恢复与束缚状态 | INCOMPLETE / 已修订 | 认知恢复、解除束缚、位置和带离地下室分别记录；两人均恢复时才有原文明确的异常缓和与电视扭曲。只恢复一人时不提前套用该结果。 |
| 厨房逃离引路者 | VERIFIED / 修订 | 仅 Caitlin 足够稳定且识破假 Ollie 时狗才引路；否则动物围住她并试图拖离特工。若 Caitlin 不在场，同一分支的套用方式 UNKNOWN。 |
| 真实 Evie 联系耗尽路径 | VERIFIED / 修订 | 关键时刻由 Caitlin 与真实 Evie 建立联系；仅找到号码、发送未读消息或此前联系不满足条件。 |
| Ripple Gun / Normal Briefcase | INCOMPLETE / 已修订 | 射击窗口需有可指定、可见且无遮挡的 VHS 带体目标，并核对持有人与充能。射击后按实际命中对象判定：任务目标确实被摧毁则按 v22 中和结算；仅确认显现版本被毁则只记录已知结果，不推断残存本体或逃脱。公文包仍需满足耗尽条件。 |
| 任务结果、奖励与 Loose Ends | INCOMPLETE / 已补充 | 收容：全体特工 +3 Commendations；中和：无额外奖惩；逃脱：全体特工 +3 Demerits，另 +7 分部 Loose Ends。Loose Ends 按 v22 实际遗留风险核算，不按知情 NPC 人头计。 |
| Aftermath | INCOMPLETE / 已修订 | Justin/Rebecca 的怀旧宿醉与逃脱追逐风险分开；Evie 研究异常的触发条件及 Cooper/Fumiko/Justin 的分支后续按原文主体和条件记录。 |
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
- 其他发现：911 通话与截获时间混淆；厨房引路者写错；Caitlin/真实 Evie 联系条件过宽；地点物件位置冲突；手机囚禁型次级异常猫的触碰效果与计费粒度记录不足；结局与 Loose Ends 结算不完整；开局 Pool 与分部累计规则、正式人物卡资源与旧交接快照有冲突。
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
   - 补充 Shape/Vision 的一般效果与手机囚禁型次级异常猫的独立触碰效果；计费粒度保持 UNKNOWN。
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
- 本段记录的是独立报告到达前的 PR 自检状态；随后收到第二轮独立报告，结论与阻塞项见第八节。
- 对照用户 Library 源文件与公开同版译稿的逐字一致性仍 UNKNOWN。
- 角色当前分部累计 Loose Ends 与开局普通 Chaos Pool 必须在 Preflight 前核算。
- 真实玩家测试尚未执行。

## 六、第二轮玩家路径复核（本轮自检；非独立审查）

以下 15 条逐项对照修订后的 01、02、03 与角色能力卡复核。PASS 表示当前备团已有可执行边界，不代表真实玩家测试通过。

| # | 玩家路径 | 第二轮复核结果 |
|---|---|---|
| 1 | 从社区调查开始 | PASS WITH INFORMATION GATES。到场先给可见浇花者与寻宠启事；继续观察/异常手段提供进一步迹象，实际测量后才确认锥形地貌。不可把测量结论预先告知。 |
| 2 | 直接前往 1063 | PASS。外部静电/电视、备用钥匙、后院与泳池线索可独立呈现；角色是否已知该地址与 Domain 真相分开处理。 |
| 3 | 跳过某个关键房间 | PASS WITH INFORMATION LOSS。车库、厨房、楼上分别提供不同线索；跳过会失去对应信息，但不强行补给，也不把单个房间设成唯一推进门槛。 |
| 4 | 拒绝与某 NPC 交谈 | PASS WITH INFORMATION LOSS。拒绝访谈不封锁其他路线；与 Jodie 交谈时，Felix 往事、邻里流言、夫妻争吵须分别满足单独交谈、聊得投机、询问夫妇的披露条件。 |
| 5 | 没有取得某个记忆锚点 | PASS WITH INFORMATION LOSS。Caitlin 与 Fumiko 有多种独立锚点；未取得时不自动恢复、不让 NPC 代答，可回查其他已知路径或承担行动后果。 |
| 6 | 先恢复 Caitlin 或先恢复 Fumiko | PASS / UNKNOWN EDGE。两人的认知、束缚、位置、撤离状态独立记录；仅两人都恢复才有原文明确的异常缓和与电视扭曲。仅一人恢复时只更新其状态，另一人的专属反应 UNKNOWN。 |
| 7 | 直接破坏地下室 VHS | PASS WITH RISK。取 VHS、直告 Fumiko 身份或解除束缚会触发反击；普通攻击不自动等于中和。Ripple Gun 仅在带体可见、可指定时有射击窗口。 |
| 8 | 常规撬锁或破门 | PASS。地下室门的常规开锁/破坏不能替代泳池铜钥匙；铜钥匙插入后融化。异常穿越实体门按能力本身裁定，不等于把锁打开。 |
| 9 | 先救人撤离，再返回 | PASS / HARD CONSEQUENCE。带任一受害者离开后再折返，异常会在离开期间逃脱；不重置最终遭遇。 |
| 10 | 使用异常能力绕过预设路线 | PASS WITH RULE CHECK。依正式角色能力逐项判定；Unbound 可穿越实体障碍，但不自动打开锁或穿越非实体 Domain 边界，也不自动带走所有受害者。 |
| 11 | 异常未耗尽就使用 Normal Briefcase | PASS。Normal Briefcase 在异常耗尽前无效；唤醒受害者不等于耗尽。 |
| 12 | 胶带遮挡前后使用 Ripple Gun | 射击窗口条件通过；结果按实际命中对象裁定。带体可见、可指定且射界无遮挡才有窗口；命中后记录对象。任务目标确实被摧毁则按 v22 中和结算；仅确认显现版本被毁则不推断残存本体或逃脱。 |
| 13 | 拒绝进入地下室或中途撤离 | PASS。未干扰地下室内容时可以返回楼上继续调查；单纯暂退不触发自动逃脱。只有带受害者离开后再返回有明确逃脱后果。 |
| 14 | 把假 Evie 引到泳池 | PASS WITH RISK。阳光使其失去 Domain 加成；玩家仍需实际诱导它进入泳池黏液，站在池边或单纯见光不自动耗尽/收容。 |
| 15 | 通过其他方式联系真正的 Evie | PASS / ACTION-DEPENDENT。只有关键时刻 Caitlin 与真实 Evie 建立联系才满足该耗尽路径；仅取得号码、发送未读信息或此前接触不自动满足。 |

### 四个高风险情境复核

| 情境 | 修订后预期裁定 | 状态 |
|---|---|---|
| 零 Pool 首次进入 Evie 卧室 | 首次楼上调查在 Domain 外；Corrupt 标示值 2；Pool=0 不可发动，不自动毁布娃娃；先呈现原文“尝试腐化”而非必然成功。 | PASS（文本逻辑复核） |
| 池外取钥匙与入池取钥匙 | 先呈现反光/蓝水征兆；只有实际爬入池中取钥匙才触发明确的黏液灌入与溺水危险。池外取物按实际行动判定，具体异常后果 UNKNOWN。 | PASS（边界已标明；具体行动待现场） |
| 单人先救 Fumiko | Fumiko 的认知/束缚/位置/带离状态单独记录；Caitlin 不自动恢复；切断束缚仍触发反击；未写明的专属反应保留 UNKNOWN。 | PASS（状态模型复核） |
| 胶带遮挡前后开枪 | 带体可见、可指定且射界无遮挡时才有 Ripple Gun 射击窗口；被遮蔽不可指定时不能射击；检查持有人和充能；击毁显现不等于收容。 | PASS（条件逻辑复核） |

本轮 PASS 仅表示文档指令之间逻辑一致，未证明实际玩家一定能识别或利用这些窗口。真实玩家测试尚未执行；本轮模型自检不能冒充独立第二轮审查。

## 七、剩余 UNKNOWN 与 Preflight 闸门

- 两只异常猫的 Manifest 费用是一次还是分别计费：UNKNOWN。
- 池外遥取铜钥匙的具体异常后果：UNKNOWN；按实际行动与规则裁定。
- 只唤醒一名受害者后另一人的专属即时反应：UNKNOWN。
- 地下室七个人形的个体身份：UNKNOWN。
- Evie 与 Caitlin 双胞胎的长幼关系：UNKNOWN。
- 用户 Library 中文模组副本与公开译本的逐字一致性：UNKNOWN。
- 开局普通 Chaos Pool：须在 Preflight 内核实角色实际所属地方分部及其累计 Loose Ends 后计算；R&D 是职能，不代表分部。必须在正式场景开始前完成核算。
- 正式人物卡 §6 记载 Dynamism 1/1、Initiative 1/1；旧交接历史快照记载 0/1 或 0/0。以正式卡当前值为基线，除非找到更新的实际消耗事件。

**当前结论：BLOCKED。** 第二轮独立审查发现 C1–C7；第三轮修订后仍须独立复核。真实玩家测试尚未执行。不得改写为 READY，也不得进入正式 Preflight 或跑团。


## 八、第二轮独立审查与第三轮修订（2026-11-25）

### 第二轮独立审查结论

- 用户提供的独立报告结论：BLOCKED；审查对象为 PR #20 head `d442c4c`，基线 `4e85fc5`。
- 上轮卧室 Corrupt 与泳池取钥匙两项首要问题确认已修复；Domain 五项换算 0/12/15/18/24 正确。
- 新阻塞：C1 厨房狗引路条件被写成无条件且漏掉拖离后果；C2 Ripple Gun 摧毁目标后的结算过度确定；C3 手机双猫与 Manifest/Double 资源规则冲突未解决，单人脱困路径不清；C4 将“两名受害者均恢复”后的异常缓和提前至任一人恢复；C5 社区观察和 Jodie 信息披露条件过宽；C6 Aftermath 的 Evie 研究及相关后续分支确定性/条件失真；C7 把 R&D 职能误作分部，并将 Pool 核算错误设为 Preflight 前置闸门。
- 审查还要求记录局部 Expand 对 Domain 的实际影响，以及布娃娃只保留一个物件状态。
- 15 条路径均为案头推演；无真实玩家测试。报告未修改或合并 PR。

### 第三轮修订（本分支待复核）

1. 厨房追逐拆为互斥条件：Caitlin 稳定且识破假 Ollie 才由狗引路；否则动物尝试将她拖离特工；不预判拖离成功。Caitlin 不在场时保留 UNKNOWN。
2. Ripple Gun 改为记录命中对象和可观察状态；任务目标确实被摧毁时按 v22 中和结算；只确认显现版本被毁时不推断残存本体、再战或逃脱。
3. 手机双猫明确并列 SOURCE、Manifest 4、Double 7 与直接行动资源规则；未批准免费特例或强制 Double。Pool=0/4/7 不凭直觉补费或免费施加囚禁；争议效果暂停但手机调查继续。加入按能力/环境尝试脱困的单人入口，不附赠成功。
4. 仅一人恢复时不套用两人均恢复后的异常缓和与电视扭曲；两人均恢复才按 SOURCE 处理。
5. 社区信息按到场可见、继续观察/异常手段、实际测量分层；Jodie 按单独交谈、建立融洽、询问夫妇等条件披露。Evie 搬入说法的上游来源保持 UNKNOWN。
6. Aftermath 恢复 Caitlin 告知 Evie 后 Evie 会着手研究的确定性；Cooper、Fumiko、Justin 的分支后续只按实际条件记账。
7. 分部核算移入 Preflight 内部：先确认实际地方分部，R&D 仅为职能；在正式场景开始前算出并公开 Pool，不把未核实分部设成 Preflight 之前置条件。
8. 补充 Expand 将 Domain 扩至另一地点的规则影响；CLUE-OLD-DOLL 与 ITEM-DOLL 合并为同一实物的别名/索引，运行时只保留一个状态。

### 第三轮验收状态

- 本次修改是对独立报告的定向修复与文档自检，不是第三方独立审查。
- 以下仍须独立复核：C1–C7 是否逐项修复；Domain 扩张和物件单一状态是否正确；15 条路径是否需调整。
- 正式 Preflight 仍未开始；真实玩家测试仍未进行。
- 可保留 UNKNOWN：七个人形身份、双胞胎长幼、邮件截断后文、池外取匙统一后果、仅一人恢复时的另一人专属反应、双猫特例收费、Library 私有副本与公开译本逐字一致性、当前实际分部累计 Loose Ends（须在 Preflight 核实）。
- 当前状态：BLOCKED / AWAITING TARGETED RE-REVIEW。
