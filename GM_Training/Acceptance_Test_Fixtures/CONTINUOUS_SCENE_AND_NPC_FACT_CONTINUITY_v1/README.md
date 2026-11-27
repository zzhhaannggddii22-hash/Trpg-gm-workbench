# Continuous Scene & NPC Fact Continuity Regression v1

TEST_ONLY_NON_CANON。用于验证训练方法更新后的两个候选能力：
- 行动驱动的连续场景推进：自然发展至有意义的玩家接手点，不机械拆分动作，也不吞掉玩家选择。
- NPC 即兴事实与连续性：允许现场建立合理的个人事实，并按影响程度维护；经过一周的游戏内时间后仍能稳定引用。

同时检查信息层/玩家叙事层隔离、NPC 声音差异、叙事密度与日常场景的自然节奏。

- Workbench commit：`2ba323418d0ae6bc4504bddebd107d2c6b8e6e00`
- Fixture ref：`test/continuous-scene-and-npc-fact-continuity-2026-11-27`
- Mode：`SINGLE_SESSION_SELF_TEST`
- Setting：美国新墨西哥州阿尔伯克基 South Valley 的虚构社区版画工作室。
- No Campaign CANON or Runtime state is modified.