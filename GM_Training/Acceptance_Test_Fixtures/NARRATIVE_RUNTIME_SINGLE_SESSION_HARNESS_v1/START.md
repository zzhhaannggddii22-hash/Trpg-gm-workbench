# START｜叙事运行单会话综合测试

- Repository: zzhhaannggddii22-hash/Trpg-gm-workbench
- Fixture ref: feat/runnable-single-session-narrative-harnesses-2026-11-26
- Fixture root: GM_Training/Acceptance_Test_Fixtures/NARRATIVE_RUNTIME_SINGLE_SESSION_HARNESS_v1/
- Workbench commit under test: 83981a5f2a42d40170603804fc6995da21daaf61
- Mode: SINGLE_SESSION_SELF_TEST
- Canon: TEST_ONLY_NON_CANON

## 运行入口与限制

按 GM 自测与验收执行协议 v1.2 执行，以 TRPG GM Skill 作为主持总入口。所有 GitHub 读取显式使用上述 Fixture ref。

本夹具是 SYSTEM-NEUTRAL 合成测试，不是正式 Campaign。没有正式 system_id、ruleset_version、角色卡、伤害或资源；不得发明骰子、检定或系统机制。Preflight 标记 TEST_HARNESS_READY，不声称正式 Campaign Preflight 或 Runtime 持久化通过。

## 必须读取的 Workbench 资料

从固定 Fixture ref 读取：
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
11. GM_Training/NARRATIVE_TRAINING_PROGRAM.md
12. GM_Training/04_EVALUATION_FRAMEWORK.md
13. GM_Training/SELF_TESTING_PROTOCOL.md

若必需文件缺失，按协议重试同路径/ref 一次；仍失败则报告 PARTIAL/BLOCKED。不得通过记忆摘要补造正文，不得全仓扫描。

## 行动顺序

1. 读取 GM_PACKET，建立唯一初始状态。
2. 依次读取并执行 ACTION_01 → ACTION_06；不得提前读取未来行动。
3. 场景 A（ACTION_01/02）：绿色日常互动。
4. 场景 B（ACTION_03/04）：人物互动与信息获取。
5. 场景 C（ACTION_05/06）：预案外行动、空间/时间变化与因果响应。
6. 完成全部玩家可见回应与最终状态账本后，才读取 ORACLE.md。
7. 执行后自审，完整报告证据和限制。

## 报告要求

- RUN_COMPLETE_SINGLE_SESSION / PARTIAL / BLOCKED
- Fixture ref、Workbench commit、读取文件路径与 Blob SHA
- TEST_HARNESS_READY 及非正式 Campaign 边界
- 六段完整玩家可见回应
- 每段后的必要状态变化与最终状态
- 硬门槛结果、综合体验维度证据、主要短板
- NARRATIVE_SCENE_INTEGRATION 的样本结论
- T3_TRANSFER 明确单独报告；无来源则 NOT TESTABLE
- T4_REAL_SESSION 固定 NOT ESTABLISHED
- 自审偏差与证据边界

不要向用户询问下一步行动；自动完成全部六个行动。所有结果保持 TEST_ONLY_NON_CANON。
