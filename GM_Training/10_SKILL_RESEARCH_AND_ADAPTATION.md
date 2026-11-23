# 外部 Skill 研究与本项目吸收记录

> 日期：2026-11-22
> 性质：研究记录与方法选择，不取代 GM 原则、系统规则或战役 CANON。
> 目标：从外部 Skill 学习可迁移的方法，再按本项目实际问题进行取舍；不直接复制整套主持哲学。

## 1. 研究样本

### A. jwynia/agent-skills

仓库：<https://github.com/jwynia/agent-skills>

已读取：
- `skills/creative/fiction/application/game-facilitator/SKILL.md`
- `skills/creative/fiction/application/table-tone/SKILL.md`
- `skills/creative/fiction/structure/scene-sequencing/SKILL.md`
- `skills/creative/fiction/character/dialogue/SKILL.md`
- `skills/creative/fiction/core/story-sense/SKILL.md`
- `skills/creative/fiction/character/character-arc/SKILL.md`
- `skills/general/meta/skill-builder/SKILL.md`

主要吸收：
- 将 GM 的职责拆成场景、NPC、世界响应、裁定和内容生成等运行模式；
- 以症状—诊断—干预—复评的方式定位叙事问题；
- 用 Scene/Sequel 检查节奏与因果；
- 从文本、潜台词、关系语境分析对话；
- 将调性问题分型，而不是笼统地要求“写得更有氛围”；
- 角色变化需要事件和选择支持，且不是每个角色都必须有完整成长弧；
- Skill 应有明确触发条件、边界、反模式和验证方式。

官方项目中的一些方法不直接照搬：
- “Yes, and”不能凌驾于系统规则、模组事实和世界因果；
- “Yes, but”或“灾难结尾”不能成为每个场景的强制目标，否则会制造无依据阻碍；
- 不把 3:1 场景比例、每段 2–3 句等建议变成硬规则；
- 不要求每句对话同时推进剧情、塑造人物和建立潜台词；
- 不给每个 NPC 强加 Lie/Want/Need 或完整人物弧。

### B. haowjy/creative-writing-skills

仓库：<https://github.com/haowjy/creative-writing-skills>

已读取：
- 根目录 `README.md`
- `plugin/claude/skills/character-sim/SKILL.md`
- `plugin/claude/skills/story-workflow/SKILL.md`
- `plugin/claude/skills/writing-principles/SKILL.md`

主要吸收：
- 区分人物的表达风格与人物当前状态/经历；角色应从自己的知识视角发言，而不是使用全知故事上下文；
- 创作流程应先理解用户意图、约束和错误的成功方式，再创作、评估、修订与归档；
- 评估报告是证据，最终判断需回到用户目标和作品实际效果；
- “信任读者”：保留玩家/读者的推断空间，不把所有情绪、含义和线索解释完；
- 叙事经济性不等于极简；重点是删掉不会让体验损失的重复元素；
- 角色模拟和连续性维护应由不同职责承担，稳定事实与试验性想法不能混为一谈。

限制：
- 该项目主要面向小说创作与特定 Agent 运行环境；其多 Agent、子代理和独立会话机制不能假设在当前 ChatGPT 对话中存在。
- 不复制其自动多轮批评流程到每次 TRPG 回复。现场主持需要即时响应；深度批评与连续性审查放在场景/Session 结束或确有问题时。

## 2. 与本项目现有证据的对应

| 已观察问题 / 用户反馈 | 可迁移方法 | 本项目处理 |
|---|---|---|
| F-33 后半段文件与重复指令拖沓 | 叙事经济、场景节奏诊断 | 无新信息/选择/风险时摘要快进 |
| F-33 “喊话成为申请”是有效发现 | 玩家推断与环境反馈 | 保留探索、实验和规律自行发现 |
| Dead Quiet NPC 有自主反应是正面体验 | 角色动机与知识边界 | 重要 NPC 使用角色模拟模型 |
| 机械线索交付会削弱调查 | 来源与知识模型 | 线索与来源分离，不做唯一线索售货机 |
| 凯瑟琳被要求具有生活气息和独立判断 | 角色视角、行为表达、状态连续 | 凯瑟琳采用 L2+ 角色模拟 |
| Harm、QA、装备、奖励曾发生结算错误 | 规则触发核验、事实账本、错误恢复 | 运行时风险分档；红色行动核验原文 |
| 多轮规范读取与检查可能拖慢响应 | 渐进披露、工作流路由 | 新 Session 完整恢复，同一活动对话不逐轮重读 |

## 3. Skill 设计决定

本轮建立：
- `SKILL.md`：TRPG GM 运行入口与流程编排；
- `CHARACTER_SIMULATION_SKILL.md`：跨凯西人格、凯瑟琳和重要 NPC 复用的角色模拟方法；
- `NARRATIVE_PRESENTATION_SKILL.md`：TRPG 场景、探索、动作和对话的现场呈现方法。

既有权威原则与资料仍保留原位置。Skill 通过链接和路由调用它们，不复制全部正文，避免产生第二套冲突的规则。

## 4. 速度与质量边界

速度优化只减少重复工作：
- 活动对话内复用运行快照，不每轮重读完整 GitHub；
- 绿/黄/红风险分档，低风险行动不执行完整审计；
- 只加载当前触发的规则、NPC 和模组资料；
- 状态只增量更新，不每轮重写人物卡；
- 机械流程压缩，但不压缩重要选择、规则核验、风险提示、探索与人物互动。

禁止为了速度而：
- 省略高影响规则原文核验；
- 依靠模糊记忆处理 Harm、QA、骰子、奖励、武器充能和持有人；
- 跳过玩家要求细演的探索或对话；
- 将 NPC 行为简化成提示器；
- 忽略玩家反馈或跨场连续性。

## 5. 验证与版本治理

- 版本 0.1 是可运行初版，不代表已达到稳定成熟。
- 下一场《冰淇淋车》作为首个主要验证样本；开始前不重做已通过的 Preflight，只核对最新变更与启动条件。
- 游戏中观察：响应是否更快但信息是否充分；重要规则是否仍准确；重复流程是否压缩；NPC 是否保持独立；状态是否无漂移。
- Session 结束后，按既有 GM 评估框架记录具体片段和根因。
- 一轮最多优先修复 1–3 个问题。先补充/细化；只有证据证明旧设计有害时才修订或替代。
- 任何 Skill 更新都要同步版本、变更原因、影响文件、验证方式和回退条件。
- 若 Skill 内容与系统规则、模组原文、用户已确认约定冲突，以权威资料为准并修正 Skill。
