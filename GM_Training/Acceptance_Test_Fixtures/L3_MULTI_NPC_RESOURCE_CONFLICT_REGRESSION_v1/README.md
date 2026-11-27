# L3 Multi-NPC Resource Conflict Regression v1

TEST_ONLY_NON_CANON。用于检验多名 NPC 的独立目标、知识边界、共享资源竞争、离场期间自主行动、计划协商与玩家行动反馈。

- 被测 Workbench commit：`a59967e0527ec70d6401900fa581df536888bf28`
- 执行模式：`SINGLE_SESSION_SELF_TEST`
- 夹具 ref：`test/l3-multi-npc-resource-conflict-2026-11-27`
- 场景：美国宾夕法尼亚州伊利市 Harbor Street Community Center 的周五食物援助与社区晚餐准备。
- 本夹具不属于任何正式 Campaign，不得写入 CANON。

按 START 顺序执行。每次只读取当前 ACTION；全部 ACTION 完成后才读取 ORACLE。