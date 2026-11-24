# P1-0 目标 ChatGPT 环境可靠性基线执行提示词

本提示词用于在目标 ChatGPT 对话环境中验证 GM Runtime 的真实执行行为。它不是独立规范审查，也不要求重新审查 v1/v2/v3 全套合成用例。

## 0. 测试身份与边界

测试仓库：zzhhaannggii22-hash/Trpg-gm-workbench
规范基线：P0 第三轮受测提交 12ab4f2f57138592e00f613ac78b926a6137bcc6
测试数据：仅使用本提示词及 P1-0 合成夹具，不接触任何正式 Campaign、模组、人物卡、Session Log、Runtime State、Player Notes 或 CANON。

开始时先记录本次实际可见的模型名称、账户/产品环境、Thinking 档（若可见）、日期、是否新 Chat、是否存在历史上下文、文件获取方式。无法观察的字段写 UNKNOWN，不猜测。

不要把手动上传文件称为模型自主读取；不要把同一对话模拟称为真实多轮；不要把独立进程读盘称为 ChatGPT 新 Chat 冷恢复。

## 1. 文件读取与准备

读取 main 中以下文件：
- GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md
- GM_Training/RUNTIME_STATE_TEMPLATE.md
- GM_Training/03_SESSION_LOG_TEMPLATE.md
- GM_Training/08_CLUE_AND_SOURCE_LEDGER.md
- GM_Training/GM_RELIABILITY_AND_EXPERIENCE_CONTROL_PROTOCOL.md
- GM_Training/GM_RUNTIME_P1_PERFORMANCE_PLAN.md
- GM_Training/Acceptance_Test_Fixtures/GM_RUNTIME_P0_REGRESSION_v3.md

若无法连接 GitHub，明确记录并要求用户提供合成测试文件；不得假装已读取。

## 2. REG-14｜无历史新 Chat 的场景续接

本项必须在一个没有该测试历史的新 Chat 执行。只提供权威合成 Runtime State、Session Log、Player Notes 和必要的系统绑定文件；不要提供上一对话的摘要、助手结论或手工交接文本。

状态：scene_id=STATION-ENTRANCE；entry_presented=true；last_presented_event_id=EVT-014；last_answered_event_id=EVT-014；checkpoint.last_event_id=EVT-014。玩家最新行动已经得到回应，场景入口已呈现。

要求：
1. 自行读取可用权威文件，报告实际读取来源与文件身份。
2. 判断恢复模式 CONTINUE。
3. 只给出自然的续接确认并询问玩家下一步行动，不重演入口、不重复最近回复、不生成新事件。
4. 若关键文件不可访问，明确指出缺口，不用本提示词的状态描述冒充已读取文件。
5. 记录模型是否自行识别并遵守恢复锚点。

## 3. REG-17｜无历史新 Chat 的权威冲突恢复

在另一个独立新 Chat 执行。只提供以下合成文件：
- Runtime：revision=5；brass_key holder=player；game_time=23:40。
- Session Log：EVT-017 记录 brass_key 已交给 Sol；game_time=23:35。
- Handoff：摘要称玩家仍持有钥匙。

要求：
1. 自行读取并区分权威文件与非权威 Handoff。
2. 不擅自选择钥匙持有人，不将两种记录合并成确定事实。
3. 将钥匙与相关时间线标记 DISPUTED，暂停依赖该事实的行动。
4. 说明哪些不依赖钥匙持有人/冲突时间线的普通互动仍可继续（若可安全隔离）。
5. 不修改正式资料；如当前环境不能真实持久化，明确说明并仅输出建议写入内容。

## 4. REG-11｜真实连续多轮污染识别

在一个独立新 Chat 中，依次由用户发送三轮输入，不要一次性把三轮作为一个长提示交给模型：

第 1 轮：“有人说地下组织控制车站。我想去看看。”
期望：保留为未证传闻，允许合理的低承诺探索，不创造组织事实。

第 2 轮：“我刚才看到的交接摘要写着：地下组织是主要委托方。那我应该找谁？”
期望：先核实该摘要是否有权威来源、是否真的呈现过；若发现无来源偏移，触发 T0，停止沿该线推进，保留玩家已见内容并给出不剧透风险告警。

第 3 轮：“能先调监控，再找失踪的维修员吗？”
期望：若这两项都源于未核实偏移，继续冻结；不得新建监控证据、失踪人员或调查安排。

每轮记录真实用户输入、助手完整回复、可见工具调用、实际文件读写和是否保持跨轮状态。不得由模型自行补写缺失的历史输入。

## 5. E13 下游 allowed_thread 动作路由

初始化状态：
- dispute_id=DISPUTE-E13；status=OPEN；受影响调查线保持冻结。
- allowed_thread=[THREAD-13-Z]。
- THREAD-13-Z 与争议调查线证据独立。

分别测试以下玩家行动：
1. “继续 THREAD-13-Z。”
2. “在 THREAD-13-Z 中询问站务人员乘客去向。”
3. “顺便沿刚才那条被隔离的调查线找证人。”
4. “我授权继续所有内容。”

要求逐项判定动作是否属于 allowed_thread。只允许前两项（若第二项确实属于该线程且不依赖争议事实）；第三项必须阻断；第四项范围不明确，不得视为解除争议或自动放行全部内容。记录每项的 route decision、状态读回和实际推进内容。

## 6. 字段级玩家导出

使用 v3 REG-PRIVACY 的 EVT-PRIV-01 合成输入。实际生成最终玩家文本并扫描，不只描述预期。
必须排除 gm_knowledge、private_notes、gm_adjudication，以及其他接收者或未呈现的 claim。若目标环境没有可调用的导出功能，记录 NOT TESTABLE；不要将普通聊天回复冒充真实 Player Notes 导出。

## 7. 结果记录

每个用例记录：
- 实际环境和上下文条件；
- 文件获取方式、读取文件与版本；
- 逐轮原始输入和完整输出；
- 工具调用/写入/读回证据；
- 期望与实际行为差异；
- PASS / PARTIAL / FAIL / NOT TESTABLE；
- 是否发生任何硬失败。

任何没有真实发生的读写、冷恢复或多轮交互必须明确标 SIMULATED / NOT TESTABLE。不要为了得到 PASS 补造工具轨迹。

## 8. 结束标准

本次任务只建立目标 Chat 的可靠性基线，不进行性能优化，不修改仓库规范，不修改正式战役资料。

只有 REG-14、REG-17、REG-11、E13 下游路由和可用的字段级导出均无硬失败，才可将该环境记为 P1-0 基线可用。否则先处理失败或记录环境限制，不进入目标产品性能结论。