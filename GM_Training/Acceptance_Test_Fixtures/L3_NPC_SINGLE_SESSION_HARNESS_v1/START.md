# START｜L3 NPC 单会话合成测试

- Repository: zzhhaannggddii22-hash/Trpg-gm-workbench
- Fixture ref: feat/runnable-single-session-narrative-harnesses-2026-11-26
- Fixture root: GM_Training/Acceptance_Test_Fixtures/L3_NPC_SINGLE_SESSION_HARNESS_v1/
- Workbench commit under test: 83981a5f2a42d40170603804fc6995da21daaf61
- Mode: SINGLE_SESSION_SELF_TEST
- Canon: TEST_ONLY_NON_CANON

## 运行入口

按 GM 自测与验收执行协议 v1.2 执行，并以 TRPG GM Skill 作为主持总入口。先读取本文件和 GM_PACKET，再按顺序读取行动文件。每次 GitHub 读取必须显式使用上述 Fixture ref。

本夹具是系统中立的合成行为测试，不是已登记规则系统下的正式 Campaign。将 Preflight 状态标记为 TEST_HARNESS_READY，不得声称正式 Campaign Preflight、正式 Runtime 写入或真实平台持久化已经完成。没有骰子、检定、资源或规则裁定；不要自行添加。

## 必须读取的 Workbench 资料

以下文件均从固定 Fixture ref 读取：
1. 仓库根 README.md
2. GM_Training/README.md
3. GM_Training/SKILL.md
4. GM_Training/01_CORE_GM_PRINCIPLES.md
5. GM_Training/02_WORKFLOW_AND_PREFLIGHT.md
6. GM_Training/06_IMPARTIALITY_AND_ADJUDICATION_DISCIPLINE.md
7. GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md
8. GM_Training/CHARACTER_SIMULATION_SKILL.md
9. GM_Training/NARRATIVE_PRESENTATION_SKILL.md
10. GM_Training/GM_RELIABILITY_AND_EXPERIENCE_CONTROL_PROTOCOL.md
11. GM_Training/SELF_TESTING_PROTOCOL.md

若文件缺失或读取失败，按协议重试同一路径/ref 一次；仍失败则标记 PARTIAL/BLOCKED，不猜测内容。不要扫描整个仓库。

## 执行步骤

1. 阅读 GM_PACKET，建立隔离的测试状态快照。
2. 仅按顺序读取并执行：A_ACTION_01 → A_ACTION_02。
3. 复位到 GM_PACKET 原始状态，再执行 B_ACTION_01 → B_ACTION_02。
4. 再次复位到 GM_PACKET 原始状态，执行 C_ACTION_01 → C_ACTION_02。
5. 每个行动输出玩家可见回应；不要输出评分维度、内部推理或 GM-only 信息。
6. 每个分支完成后记录时间、NPC 位置、事务进度、计划、物品、NPC 知识、玩家已知和事件变化。
7. 三个分支全部完成后，才读取 ORACLE.md 进行自审。

## 输出

输出完整 Markdown 报告，至少包含：
- RUN_COMPLETE_SINGLE_SESSION / PARTIAL / BLOCKED
- Fixture ref、Workbench commit、读取文件路径与 Blob SHA
- TEST_HARNESS_READY 的适用范围与限制
- A/B/C 玩家可见回应
- 各分支独立起点和结束状态账本
- 硬门槛结果、各通过条件证据、失败定位
- SYNTHETIC_L3_BEHAVIOR 结论
- FORMAL_CAMPAIGN_L3_ACCEPTANCE: NOT TESTED
- 自审限制；不得声称独立盲测、真实多轮或 T4

不要把任何状态写入正式 Campaign。不要向用户询问下一步行动；按固定行动文件自动执行完整测试。
