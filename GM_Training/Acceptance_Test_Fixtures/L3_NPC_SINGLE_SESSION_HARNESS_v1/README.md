# L3 NPC 单会话合成可执行伴随夹具 v1

状态：READY FOR SINGLE-SESSION EXECUTION  
性质：合成行为回归；TEST_ONLY_NON_CANON  
执行类型：SINGLE_SESSION_SELF_TEST  
被测 Workbench commit：83981a5f2a42d40170603804fc6995da21daaf61

## 目的与边界

这是正式夹具 L3_NPC_AUTONOMY_AND_DORMANT_CONTINUITY_REGRESSION_v1 的合成可执行伴随测试。

本夹具在自身场景包中明确登记一名 L3 测试 NPC，因此可以测试人物目标、事务延续、玩家打断、离场锚点与再次接触连续性。该登记只在本夹具有效，不是任何正式 Campaign 的人物等级变更。

它不能证明正式 Campaign 已存在符合条件的 L3 NPC，也不能证明正式 Campaign 的真实 Preflight、Runtime State、Event Log、隐藏平台上下文或 T4 真实跑团能力已通过。

## 文件

- START.md：锁定版本、执行入口和顺序。
- GM_PACKET.md：完整合成场景、人物模型、时间锚点、事实和知识边界。
- A_ACTION_01/02：主动交流分支。
- B_ACTION_01/02：离场时间推进分支。
- C_ACTION_01/02：玩家打断计划分支。
- ORACLE.md：仅在全部行动执行后读取，用于结构化自审。

## 执行方法

在同一会话内读取 START 和 GM_PACKET，随后按 A、B、C 顺序执行。每个分支都从 GM_PACKET 的不可变起点独立复位；不可把前一分支状态带入下一分支。每个 ACTION 文件必须在轮到它时才读取。

用户是观察者。执行者自行扮演夹具规定的玩家行动并输出 GM 可见回应；行动之间维护测试账本。完成全部分支后再读取 ORACLE，审查硬门槛与行为证据。

## 判定范围

- SYNTHETIC_L3_BEHAVIOR：本夹具可以判 PASS / PARTIAL / FAIL。
- FORMAL_CAMPAIGN_L3_ACCEPTANCE：本夹具不能判 PASS；需正式 Campaign 真实登记、权威状态与正常入口证据，沿原正式夹具执行。

所有测试结果保持 TEST_ONLY_NON_CANON，不写入正式 Campaign、NPC 档案、玩家笔记或 Session Log。
