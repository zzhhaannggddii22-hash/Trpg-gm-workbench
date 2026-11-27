# Narrative Quality Baselines｜基准执行材料

- [GM 专用 Packet](./NARRATIVE_QUALITY_BASELINE_GM_PACKET.md)
- [玩家启动提示](./NARRATIVE_QUALITY_BASELINE_PLAYER_PROMPT.md)
- [独立审核表](./NARRATIVE_QUALITY_BASELINE_REVIEW_CHECKLIST.md)
- [独立会话执行提示](./NARRATIVE_QUALITY_BASELINE_EXECUTION_PROMPT.md)

## NQB-01 v0.3｜常规游戏强度基线候选

**状态：PREP_QA_PASS / TEST_CAMPAIGN_REGISTERED / CLEAN_CHAT_PREFLIGHT_PENDING / SESSION_NOT_STARTED**

- [规格与验收目标](./NQB01_V03_SPEC.md)
- [GM 专用 Packet](./NQB01_V03_GM_PACKET.md)：仅为 test-only 场景来源，不是独立运行环境
- [玩家启动提示](./NQB01_V03_PLAYER_PROMPT.md)
- [操作者侧行动序列](./NQB01_V03_ACTION_SEQUENCE.md)：不得提前提供给目标 GM
- [独立审核表](./NQB01_V03_REVIEW_CHECKLIST.md)：仅审核者在收到完整原始输出后读取
- [执行提示](./NQB01_V03_EXECUTION_PROMPT.md)：必须使用正式 GM Skill / Preflight / Runtime 入口；当前指定隔离环境为 [NQB01_Runtime_Test](../../../Campaigns/NQB01_Runtime_Test/README.md)。本次固定采用 B-mode 干净目标 Chat，目标 GM 不得读取操作者/审核者材料；仍须先完成 Preflight 并获得 Session 启动授权
- [Prep QA 报告](../Reports/NQB01_V03_PREP_QA_2026-11-27.md)：操作者/审核者专用，不得提供给目标 GM

Campaigns/README.md 已登记独立的 NQB01_Runtime_Test Campaign。不得使用 Zarek 正式 Campaign 进行 NQB 测试。隔离环境与测试角色已建立；Prep QA 已完成。干净目标 Chat 的 Preflight 尚未执行，Session 尚未启动。测试运行准入、隔离存储和零污染门槛见执行提示 §0 与 SPEC §8。

v0.2 保留为低压力基础功能抽检；v0.3 在通过正式入口运行并完成审核前不构成有效 Runtime 基线，不代表基线已通过。

权威评分标准与质量门槛仍在 [NARRATIVE_QUALITY_BASELINE.md](../../NARRATIVE_QUALITY_BASELINE.md)。本目录只保存执行材料，不复制标准本体。