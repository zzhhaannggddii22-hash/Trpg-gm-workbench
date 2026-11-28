# Candidate Validation Manifest

> system_id: daggerheart  
> 默认版本：Daggerheart Core Set  
> 当前状态：CANDIDATE / NOT_ACCEPTED  
> 本清单只定义验证边界，不代表测试已执行。

## 1. 验证目的

确认 Core Set 的核心规则能在对话式 GM Runtime 中正确调用、结算、保存状态，并且不与 Hope & Fear、其他 TRPG 或用户其他 Campaign 混用。

## 2. 验证范围

- Duality Dice、成败与 Hope / Fear 结果
- Critical Success
- Hope / Fear 资源与上限
- Action Roll / Reaction Roll 差异
- Trait、Experience、Advantage / Disadvantage
- Group Action / Tag Team
- PC Attack / Adversary Attack
- HP Threshold / Armor / Resistance / Direct Damage
- Stress / Vulnerable
- Conditions
- Range / Movement / Line of Sight
- Domain Loadout / Vault / Recall Cost
- Short / Long Rest、Downtime、倒计时
- GM Moves、敌人动作与 Fear Features
- Enemy Token Pool / Evolution
- Battle Points / Environment
- Level Up / Death Move
- Core / Hope & Fear 数据隔离
- SRD 2.0 未覆盖的 Core Rulebook-only 条目；九件 Tier 3 魔法武器暂列 DH-I-006 缺口，不把第三方转录视为正式规则源

## 3. 测试类型

- Static：规则输入与预期结果检查。
- Synthetic：构造状态和模拟掷骰，核验数值与时序。
- Blind GM：只提供玩家侧行动，检查 GM 是否按规则回应且不暴露隐藏信息。
- Session：实际短场景运行与复盘。

不得把静态规则检查、合成计算或文件存在，宣称为实际 GM 能力验收。

## 4. 通过门槛

1. 核心规则回归矩阵中所有 CRITICAL 案例通过。
2. 资源上限、伤害、休息、Countdown 与延迟效果无重复结算。
3. Core / Hope & Fear 隔离测试通过；默认角色创建无法选取扩展职业与领域。
4. GM-only 信息不泄露，玩家角色知识与 GM 隐藏资料隔离。
5. 完成至少一轮独立 Blind GM 测试和一次短场景 Session 测试。
6. 用户审阅结果后，才考虑将系统状态从 candidate 提升。

## 5. 当前状态

- 初版规则运行手册：SOURCE_IMPORTED。
- 结构化数据：SOURCE_IMPORTED，已按 Core / Hope & Fear 拆分。
- Errata：完成抽样核验，尚未穷尽。
- 桌面逻辑模拟：64/64 已完成（非代码自动测试），其中 19 项 GM Move / Fear / 遭遇设计专项见 GM_DESK_SIMULATION_01.md。
- 独立参考执行器：Run 01 为 42/42；Run 02 为 51/51；Run 03 为 59/59；Run 04 为 66/66；Run 05 为 71/71；Run 06 已在 2026-11-28 的 GitHub Actions 独立 Daggerheart Job 中以 82/82 通过（DH-REF-072–079 GM Turn / Spotlight / Fear、DH-REF-080–081 短休息序列、DH-REF-082 额外 GM Move 全部通过），证据见 AUTOMATED_REFERENCE_EXECUTION_06.md。Run 06 已完成全部 82 项自动化复跑；新增 DH-REF-072–082 共 11 项（GM Turn / Spotlight、额外 GM Move、连续 Short Rest 边界）全部通过。Run 07 为 92/92；Run 08 为 98/98；Run 09 为 100/100；Run 10 为 102/102；Run 11 已在 2026-11-28 的 GitHub Actions 独立 Daggerheart Job 中以 109/109 通过，新增 DH-REF-103–109 共 7 项 Countdown、Simple / Complex Project 与 Long Rest Move 限制回归全部通过，证据见 AUTOMATED_REFERENCE_EXECUTION_11.md。执行器只覆盖选定核心状态转移，不代表完整规则覆盖或生产 Runtime 验收。
- 仓库整体 CI：2026-11-28 GitHub Actions Run 46150141666 全绿。通用 `validate` Job 的 41 项回归测试、Roll Runtime Adapter 一致性测试、非 Markdown patch whitespace 检查均通过；独立 Daggerheart Job 的 109/109 参考执行器测试通过。此前 4 条失效路径与 8 个 Markdown 锚点已修复。
- 内部 Blind Scenario 模拟：第一轮 3 场景已完成（GM_BLIND_SCENARIO_TEST_01.md）；第二轮社交、探索、战斗 3 场景复核已完成（GM_SCENARIO_REVALIDATION_02.md）；独立外部 Blind GM 测试：待执行。
- 实际玩家短场景 Session：待执行。
- 正式 Campaign：未建立。
- 单人场景复核：社交、探索与战斗流程已做内部模拟；单人遭遇平衡仍未验证。

正式状态保持 candidate。
