# Worlds Without Number｜研究与验证计划

## 目标

完整理解 WWN 规则与 GM 工具体系，评估其是否适合 AI 主持长期单人沙盒。先研究并离线保存规则，再做短测；不提前开发复杂 Runtime。

## 原则

1. 官方规则、作者开放 SRD、第三方解释和 House Rule 分开记录。
2. 先研究完整系统，再决定简化。
3. 机制只在触发时进入 Runtime。
4. 世界模拟使用有意义的抽象层级。
5. AI 适配不能改变官方规则含义。
6. 资料不足时记录缺口，不从其他系统推测。
7. 合法可保存的规则和索引尽量放入本地仓库，减少运行时查网。

## 研究范围与状态

| 方向 | 状态 | 本地入口 |
|---|---|---|
| A. 版本、来源与许可 | 已核验 | SOURCES.md、GM_TOOLKIT_RESEARCH.md |
| B. 核心机制与角色规则 | SRD 摘要完成；需行为测试 | CORE_RUNTIME_GUIDE.md、Data/ |
| C. World / Region / Polity / Site 构建 | 研究摘要完成 | WORLD_BUILDING_RUNTIME.md |
| D. Site Tags | 结构和组合流程完成；原书 Tag 正文不复制 | SITE_TAGS_RUNTIME.md |
| E. 冒险创建 | 四类挑战与准备流程摘要完成 | ADVENTURE_CREATION_RUNTIME.md |
| F. Faction / Major Projects | SRD 机制摘要完成 | FACTIONS_AND_MAJOR_PROJECTS.md |
| G. AI GM / 单人适配 | 初步建议完成；尚未验证 | GM_TOOLKIT_RESEARCH.md、Testing/ |

## 已完成的研究工作

- [x] 建立 WWN 独立系统目录和 Candidate 边界。
- [x] 核对 SRD 1.0 作者、日期、CC0 边界。
- [x] 将 SRD 原文、结构化数据和本地搜索索引纳入仓库。
- [x] 核对 Free Edition 版本、版权页、ISBN 和章节目录。
- [x] 完成核心规则运行摘要，并明确一级豁免目标值计算。
- [x] 完成 World / Region / Polity / Sites 背景层级与准备原则。
- [x] 完成四类 Site、五类 Tag 素材和双 Tag 组合流程摘要。
- [x] 完成 Combat / Exploration / Investigation / Social 冒险挑战流程摘要。
- [x] 完成 Faction Turn、Faction Actions 与 Major Projects 摘要。
- [x] 建立 AI Runtime 适配建议和许可边界。
- [x] 将五项研究入口加入本地索引。

## 剩余工作：验证而非继续堆文档

1. 核心检定、豁免、战斗、Shock、濒死和恢复的规则行为测试。
2. Tags 生成地点与冒险入口的可用性测试。
3. Investigation 多线索、失败推进和信息闭环测试。
4. Faction Turn 资产行动、维护、Goal 和状态变化测试。
5. Major Project 难度、投入、反对力量变化与完成测试。
6. 单人 PC 的生存压力、雇员/随从价值和遭遇规模测试。
7. 通过测试后再评估 Candidate → Active；不以文档数量代替验证。

所有测试使用 TEST_ONLY_NON_CANON，不连接正式 Campaign。