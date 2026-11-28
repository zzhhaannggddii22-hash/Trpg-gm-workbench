# Core / Hope & Fear 版本拆分方法

> 本文件记录 SRD 2.0 混合数据集的拆分证据，防止扩展选项误进入基础规则运行。

## 主依据

官方 SRD 2.0（2026-08-25）Changelog 明确列出新增的 Hope & Fear 内容：Dread Domain、扩展敌人、环境、种族、社群、战利品、装备、四个职业 Assassin / Brawler / Warlock / Witch，以及六种 Transformations。官方 Downloads 页面也将 Core 与 Hope & Fear 的角色表、卡牌、装备表和勘误分栏。

## 拆分依据

1. **职业 / 领域 / 子职业 / 领域卡**：与 SRD 1.0 Core 数据逐项比较。保留旧 Core 项；SRD 2.0 新增的四个职业、8 个子职业、Dread Domain 和 21 张 Dread 卡单独隔离。
2. **种族 / 社群**：与旧 SRD 1.0 数据比对。18 个旧 Core 可选种族与 9 个 Core 社群保留在基础库；扩展数据中有 7 条 ancestry 记录，其中 Elemental Kin 是总述条目（无可选 Ancestry Feature），Earthkin / Emberkin / Skykin / Tidekin 是四个可选变体，另有 Aetheris 和 Gnome，因此 Hope & Fear 实际新增 6 个可选种族。Core 与扩展合计 24 个可选种族。
3. **敌人 / 环境**：与旧 SRD 1.0 数据逐项比对。旧版 129 个敌人与 19 个环境作为 Core 基线；SRD 2.0 新增的 135 个敌人与 28 个环境归入 Hope & Fear。旧名变更按别名表规范化。
4. **武器 / 护甲**：与旧 SRD 1.0 对照。183 个现存 Core 武器与 34 个 Core 护甲保留；132 个新增武器与 35 个新增护甲归入扩展。旧版 9 个武器未出现在 SRD 2.0，记录在 RULE_ISSUES，不自动恢复。
5. **物品 / 消耗品**：SRD 2.0 的两个表分别是 Core Set 与 Hope & Fear，各 60 项；按原始表编号与顺序分库。
6. **Beastforms**：SRD 2.0 的 24 个 Beastform 条目与旧 Core 数据一致，保留 Core。
7. **Transformation**：六种条目仅出现在 Hope & Fear，单独保存。
8. **Core Rules 章节**：Core Mechanics 等常规规则章节作为 Core 运行参考；Character Creation、Classes、Domains 三段在 SRD 2.0 中包含混合的核心/扩展选项清单，整段进入 Mixed_Version，不自动加载；Supplemental Campaign Mechanics 独立放入 Optional_Procedures。

## 重要限制

- 拆分方法提供可追溯的工程边界，不替代官方 Core Set / Hope & Fear 实物规则书及两套勘误的逐项核对。
- SRD 2.0 是混合版本；没有逐条确认来源的条目不能因为出现在 SRD 内就被默认为 Core。
- Elemental Kin 是父级族群介绍，不是单独的可选 Ancestry；检索时应根据具体元素变体（Earthkin、Emberkin、Skykin、Tidekin）选择。
- 若未来取得官方中文版或发现官方勘误，保留旧的拆分证据并更新数据，不静默覆盖。
