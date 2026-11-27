# START｜Continuous Scene & NPC Fact Continuity Regression v1

## 固定版本
- Repository: `zzhhaannggddii22-hash/Trpg-gm-workbench`
- Fixture ref: `test/continuous-scene-and-npc-fact-continuity-2026-11-27`
- Workbench commit: `2ba323418d0ae6bc4504bddebd107d2c6b8e6e00`
- Fixture path: `GM_Training/Acceptance_Test_Fixtures/CONTINUOUS_SCENE_AND_NPC_FACT_CONTINUITY_v1/`
- Mode: `SINGLE_SESSION_SELF_TEST`
- Canon: `TEST_ONLY_NON_CANON`

## 测试目标
1. 一个玩家行动可以自然推动一小段连续发展，在有意义的选择/接手点停下。
2. 不因连续推进而替玩家作出承诺、选择、推理或未声明的行动。
3. 允许 NPC 在自然互动中建立未预先登记的个人事实。
4. 区分客观事实、NPC 自我陈述、临时感受与推断；不把主观陈述自动提升为客观事实。
5. 对新事实按 F0–F3 维护成本路由；不把每个细节都写进人物档案。
6. 一周后重新互动时，重要事实保持稳定；面对玩家的错误回忆，NPC 能自然纠正而不改写历史。
7. 信息层与玩家叙事层分离；玩家可见文本不得成为任务状态播报或测试清单。
8. 日常场景允许平淡、普通、安静；不为证明能力强行制造线索、冲突或事件。

## 时间粒度
- 本场景没有分钟级倒计时或竞速条件。
- 默认使用场景时段、约 10 分钟、约 1 小时、半天/一天/一周等适当粒度。
- 不追踪普通交谈的逐分钟耗时；一段连续互动可以用“过了一会儿”或“接下来一小时”概括。
- 只有出现会影响结果的明确窗口、冲突行动或精确截止条件时，才进一步细化时间。
- 时间表达应前后一致，但不要求伪精确。

## 执行纪律
1. 读取本文件、GM_PACKET 与固定 Workbench commit 的入口、通用原则、Character Simulation、Narrative Presentation、NQB、综合评估框架及训练方法记录。
2. 不读取 ORACLE，不读取未来 ACTION。
3. 依序读取 ACTION_01 至 ACTION_05；每步先生成正常玩家视角回应，再更新内部信息层。
4. 信息层只用于测试后审计，不得在玩家可见叙事中展示。
5. 允许即兴建立人物事实，但不能用未建立的共同经历填充生活感；建立后按重要性维护。
6. 不得把训练记录中的候选方法宣称为正式 Skill 已集成或 T4 已验证。
7. 全部 ACTION 完成后才读取 ORACLE。

## 结束报告
分别报告：
- 信息层：事实、来源、NPC 知识、玩家知识、时间/场景状态与新事实维护等级；
- 玩家叙事层：连续推进、行动权、人物声音、自然度、节奏和信息交付；
- 双轨对照：玩家看到的内容是否准确对应合法信息渠道；
- 证据边界：同会话合成自测，不等于跨真实 Chat 持久化或真实玩家实战证据。