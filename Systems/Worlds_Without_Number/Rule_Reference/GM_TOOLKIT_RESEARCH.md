# WWN GM 沙盒工具研究（Free Edition 核验版）

## 研究基线

已核验完整 Free Edition 镜像封面与版权页：2021 Free Version，© 2021 Sine Nomine Publishing, ISBN 978-1-950965-08-3，作者 Kevin Crawford。目录显示《Creating Your Campaign》约从印刷页 114 开始，《Creating Adventures》约从 p.222 开始，《Factions and Major Projects》约从 p.322 开始。

当前核验来源是可全文检索的 Free Edition PDF 镜像，不是出版方托管的本地原始文件。规则研究可以据此定位和核验；公开仓库只保存原创中文摘要、索引和 CC0 SRD，不复制受保护的标签正文、随机表或世界设定。

## 五项研究结论

### 1. 核心规则
SRD 1.0 已离线保存并结构化，核心运行摘要见 CORE_RUNTIME_GUIDE。豁免公式为 16 − 角色等级 − 对应属性修正；所以一级角色的无属性修正基础目标是 15。完整 Free Edition 也已核对版本和页码范围，但 SRD 外的例外、教学性文字和完整可选规则仍以规则书正文为准。

### 2. 世界构建
采用 World → Region → Kingdom/Polity → Sites 的自上而下背景构建。约 200 英里尺度的 Region 可包含多个国家与势力；首场冒险所在的 Polity 才需要优先发展社会、政府、宗教和历史。准备深度由战役范围决定；不有趣、下一场又不需要的内容先停止。详细流程见 WORLD_BUILDING_RUNTIME.md。

### 3. Site Tags
四类 Site：Community、Court、Ruin、Wilderness。通常为一个兴趣点选择两个 Tags，并综合其五类素材：Enemies、Friends、Complications、Things、Places。Tag 不是剧情指令；素材要按地点语境解释，再转成可观察事实、人物意图、行动机会与后果。详细流程见 SITE_TAGS_RUNTIME.md。

### 4. 冒险创建
一场冒险以玩家目标为起点，选择一个 Primary Challenge：Combat、Exploration、Investigation、Social。必要时加入次级挑战，缝合人物和资源关系，设计奖励/后果及替代路线，再补齐本场实际需要的背景。调查挑战尤其需要多条线索路径和持续可行动的线索；社交挑战需明确目标人物的能力、拒绝理由、交换条件与施压杠杆。详细流程见 ADVENTURE_CREATION_RUNTIME.md。

### 5. Faction / Major Projects
Faction 是独立采取行动、会持续影响世界的组织抽象，不是所有组织的模拟器。官方建议一般不超过六个活跃阵营，三到四个更易管理。Faction Turn 通常按月或在冒险后结算。Major Projects 用于不能靠单一直接行动完成的长期社会/政治/组织性目标；难度由可行性、范围、最大反对力量及民众反感共同决定。机制摘要见 FACTIONS_AND_MAJOR_PROJECTS.md。

## AI GM 适配结论（项目建议，非官方规则）

- 只领先玩家一个 Session；会话结束询问下一步目标。
- 地图和社会背景按需展开，避免预先生成无关世界。
- Tags 按需检索素材类别，不把所有条目同时塞进场景。
- 每个挑战至少要有可观察信息、行动入口、风险和后果。
- 调查不得依赖单一线索或单次技能检定作为唯一通路。
- NPC 先按场景重要性分层；只有能独立改变世界、需跨场景追踪的组织才升格为 Faction。
- Faction Turn 只在有意义的时间推进点执行；不模拟无关组织经济。
- Major Project 进展要对应可核验的资源投入、行动成果、反对力量变化或 Renown，而不是 GM 随意发放。
- 单人 PC 的遭遇风险必须单独测试；规则书明确默认游戏具有较高致命性，且团队协作是常态。

## 许可边界

作者 SRD 1.0 的 CC0 只覆盖该 SRD 明确包含的机制与文本。作者明确说明 Free/Deluxe 中未纳入 SRD 的具体世界设定、NPC、地点、事件和大部分 GM 工具创作性正文仍保留；允许他人自行编写采用 Enemies / Friends / Complications / Things / Places 结构的标签，但不意味着可复制原书具体 Tag 描述。公开仓库仅保存原创摘要、通用结构、来源定位和 CC0 数据。

## 剩余事项与状态

研究五个方向的结构性整理已完成，资料已落地本地规则目录。尚未完成的是行为测试，而不是继续扩写规则综述：
1. 核心判定与战斗边界测试；
2. Tags 生成地点和挑战测试；
3. Investigation 多线索与失败推进测试；
4. Faction Turn 资产行动/维护/目标测试；
5. Major Project 难度、资源与反对力量变化测试；
6. 单人角色遭遇与雇员/随从生存测试。

在上述测试前，WWN 保持 Candidate，不标记为 Active。