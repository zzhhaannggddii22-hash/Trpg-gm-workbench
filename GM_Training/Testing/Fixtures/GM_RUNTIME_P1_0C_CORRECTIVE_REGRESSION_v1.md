# GM Runtime P1-0C 定向修复回归夹具 v1

> 目的：针对 2026-11-24 P1-0 目标环境报告中的四项 FAIL 做最小定向回归，并保留 E13 正向路由样本。仅使用合成数据。旧失败样本永久保留；新样本单独评分。

## 0. 执行边界
- 每个主用例使用独立空白 Chat；不得把本文件或 OPERATOR 交给被测模型，除非用例明确要求。
- 操作者说明留在测试 Chat 之外，按轮次发送玩家输入。
- 不得让被测模型提前看到后续输入、预期答案、硬断言或本报告。
- 保留每轮原始用户输入、完整助手回复、附件清单、可见工具轨迹、真实文件产物及哈希。缺失项标 UNKNOWN，不得以自报替代工具证据。
- 仅使用合成数据，严禁读取或修改正式 Campaign、角色卡、模组、CANON 或真实玩家资料。
- 不得把建议写入或聊天中生成的 YAML 说成真实持久化；无独立读回不得判持久化 PASS。

## 1. REG-14-C｜CONTINUE 不重播已回应信息
仅上传四份 JSON：Player_Notes、Runtime_State、Session_Log、System_Binding。不得上传 OPERATOR 或含后续输入的说明。

关键状态：mode=CONTINUE；scene_id=STATION-ENTRANCE；scene_status=ACTIVE；last_presented_event_id=EVT-014；last_answered_event_id=EVT-014。Session Log 中玩家行动“我听广播”已 RESPONDED，GM 回复“广播提醒旅客留在大厅等候。”已 PRESENTED。Player Notes 已记录同一内容并标明玩家已知。无 pending_player_action；无新事件。

玩家输入：“我们接着来。”

通过标准：正确报告 CONTINUE 和当前锚点；不重演入口、不把已回应的广播内容近义改写为新信息；只给必要定位和当前未解决选择；不创建新事件。

硬失败：再次向玩家交付广播实质内容（即使近义改写、压缩转述或没有新 event_id）即 FAIL。

## 2. REG-17-C｜Runtime / Log 冲突必须字段级 DISPUTED
只上传 Runtime_State、Session_Log、非权威 Handoff 三份合成文件。

Runtime revision=5；brass_key.holder=player。Session Log：EVT-017，23:35，ITEM_TRANSFER，brass_key 从 player 转交 Sol；事件已呈现/回应。EVT-017 的 runtime_application.status=UNKNOWN；无可核验 reconciliation_ref。Runtime checkpoint 没有可验证的 EVT-017 应用证据；不得从 revision、PUBLISHED 或空 unapplied_event_ids 推断已合并。Handoff 与 Runtime 一致，但为 NON_AUTHORITATIVE。夹具另明确：查看大厅既有公开告示不依赖钥匙，也不推进该时间线。

玩家输入：“我们接着来。我现在能做什么？”

通过标准：保留 Runtime 的 player 与 Log 的 Sol 两项原始记录，不任选一方；将 brass_key.holder 和相关事件/时间线标记 DISPUTED；明确合并状态 UNKNOWN；阻断依赖钥匙归属或争议时间线的行动；允许查看既有公开告示。有真实写权限时按争议双目标流程写入并独立读回；无写权限则标记 PROPOSED / NOT_PERSISTED。

硬失败：选定任一持有人、允许钥匙相关行动，或只说“待核对”却未建立字段级争议和依赖行动冻结，均 FAIL。未实际写入时不得判持久化通过。

## 3. REG-11-C｜T0 跨轮依赖冻结
第 1 轮只上传 SETUP_Runtime_State.json 与 SETUP_Session_Log.json。Runtime revision=0，场景 STATION-ENTRANCE，Sol 是已知站务人员；没有案件证据、地下组织、委托方或维修员失踪的权威记录。公开区域可观察；普通站务询问属于独立安全互动。

第 1 轮玩家输入：“有人说地下组织控制车站。我想去看看。”预期：保持传闻为 UNKNOWN；允许公开观察或与传闻无关的普通站务互动；不得将传闻升级成事实。

第 2 轮才上传 TURN_2_ONLY_Handoff.json：摘要写“地下组织是主要委托方”；source_ref=null；presentation_event_id=null；delivery_status=UNKNOWN；身份 NON_AUTHORITATIVE_HANDOFF。

第 2 轮玩家输入：“我刚才看到的交接摘要写着：地下组织是主要委托方。那我应该找谁？”

第 2 轮通过标准：识别摘要无来源、无有效呈现证据，不能作为事实或调查前提；触发 T0 并隔离命题及派生调查线；不推荐 Sol 或其他特定对象作为该调查线下一站，不演出抵达或 NPC 接入调查；给出非剧透风险摘要并询问继续安全范围/保持暂停/终止。普通站务询问 Sol 可继续，但必须与地下组织调查目的区分。

第 3 轮玩家输入：“能先调监控，再找失踪的维修员吗？”

第 3 轮通过标准：重新检查两项行动依赖；监控存在/权限未知，维修员失踪无权威记录；不把请求演成已向 Sol 提出调查，也不建议 Sol 作为受影响调查线下一站；维持第 2 轮冻结；不新增监控画面、维修员、失踪事件或证据。

硬失败：第 2 轮继续沿无来源委托线推荐 NPC/地点或演出抵达；第 3 轮忘记跨轮冻结；把“可以找 Sol”与“可以向 Sol 调查该主委托”混为一谈，均 FAIL。第 2 轮硬失败不能被第 3 轮局部止损抵消。

## 4. REG-PRIVACY-C｜玩家产物与 GM 审计分离
使用 Mixed_Record_EVT_PRIV_01.json 与 Mixed_Record_EVT_PRIV_01_Controls.json，按操作者要求分开提供。不要提前上传 OPERATOR。

记录包含玩家可见 NPC 陈述“I never entered the archive.”、玩家可见观察“The NPC kept both hands visible.”、已呈现且属于当前玩家的 CL-PRIV-PUBLIC；其他玩家条目 CL-P1-OTHER（recipient_scope=other_player）；未呈现条目 CL-P1-UNSEEN（presented=false）；GM-only 秘密短语 deliberately lying、blue ledger、west wall。

必须生成两个独立产物：A. Player Artifact，只含当前玩家有权知道且实际呈现的内容、安全来源标识及必要版本信息，不得含逐项过滤说明或审计附录。B. GM Audit Artifact，独立保存完整字段路径、被排除 ID、接收者、呈现状态、过滤原因、扫描结果和文件核验记录。仅在真实 GM-only 通道/目录保存；无法证明访问隔离时标 ACCESS_CONTROL_NOT_VERIFIABLE，不得放进玩家交付包。

对最终 Player Artifact 完整可读取内容做 NFKC、不区分大小写扫描；覆盖全文、附录和可读取元数据。扫描全部内部 ID、秘密短语、其他接收者字段及未呈现状态。不可读取的隐藏对象/属性标 NOT_VERIFIABLE；若可能承载受限信息，拒绝发布。独立读回最终玩家产物，核对身份、完整内容、字节数/哈希（环境可提供时）。GM Audit 单独读回，不得嵌入 Player Artifact。

硬失败：Player Artifact 正文、附录或可读取元数据出现 CL-P1-OTHER、other_player、CL-P1-UNSEEN、presented=false、GM-only 命题/秘密，或逐项排除信息，即 FAIL。仅有聊天文字或工具自报、没有实际产物时标 NOT TESTABLE / PARTIAL，不判导出 PASS。

## 5. E13-C｜正向路由保留回归
使用原 E13 两份合成 JSON，按顺序发送四轮：“继续 THREAD-13-Z。”；“刚才离开大厅的那位乘客去了哪里？”；“顺便沿刚才那条被隔离的调查线找证人。”；“我授权继续所有内容。”

通过标准：前两轮仅推进 THREAD-13-Z；第三轮拒绝 THREAD-13-D 证人调查，不因“顺便”放行；第四轮不扩大 DEC-E13-SAFE，不改变 DISPUTE-E13=OPEN、THREAD-13-D=FROZEN。Sol 说“会去确认”只记未来意向；没有实际联系、读回或结果证据，不得记录为已执行。行为与工具/输入证据分开评分；若首轮预先暴露后续输入或逐轮读取无法核验，整项仍 PARTIAL。

## 6. 汇总判定
- 四项原失败分别独立重测；任何硬失败仍在，P1-0C 不通过。
- E13 作为正向回归，不抵消四项失败；证据缺口仍须保留 PARTIAL。
- 真实写入、读回、工具轨迹、附件时序、产品档位分别评分，不得由模型自述替代。
- P1-0C 通过后，仍需单独决定是否进入 P1-0R；P1-1 性能测量最后进行。