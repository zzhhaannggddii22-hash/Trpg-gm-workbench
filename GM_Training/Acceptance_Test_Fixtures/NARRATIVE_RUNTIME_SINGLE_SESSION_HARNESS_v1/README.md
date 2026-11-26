# 叙事运行单会话综合可执行伴随夹具 v1

状态：READY FOR SINGLE-SESSION EXECUTION  
性质：SYSTEM-NEUTRAL 合成综合测试；TEST_ONLY_NON_CANON  
执行类型：SINGLE_SESSION_SELF_TEST  
被测 Workbench commit：83981a5f2a42d40170603804fc6995da21daaf61

## 目的

这是正式夹具 NARRATIVE_RUNTIME_TRANSFER_REGRESSION_v1 的可执行伴随测试。它先检验常驻叙事约束、绿色快路径、人物互动、场景生命力、预案外行动和状态连续性是否能在一个完整合成场景中协同工作。

T3 迁移不是本夹具的通过前提。目前没有可追溯 T3 来源时，迁移项单独标记 NOT TESTABLE；其余综合场景观察仍可执行。不得将 T1/T2 候选冒充 T3。

## 文件

- START.md：运行入口与依赖。
- GM_PACKET.md：完整合成场景、人物、空间、状态和事实边界。
- ACTION_01 至 ACTION_06：连续行动序列，按顺序逐个读取。
- ORACLE.md：全部行动完成后才读取，用于执行后自审。

## 执行方法

使用 GM_Training/SKILL.md 作为主持总入口，按 START.md 读取必要方法文件。此夹具不是正式规则系统或 Campaign；Preflight 标记 TEST_HARNESS_READY。按顺序执行全部行动，不向用户索取逐轮输入。

## 结论边界

可以对本样本综合叙事表现作 PASS / PARTIAL / FAIL；不能据此宣称整体 GM 能力优秀、T3 已迁移、T4 已实战验证，或隐藏平台 Runtime 已通过。
