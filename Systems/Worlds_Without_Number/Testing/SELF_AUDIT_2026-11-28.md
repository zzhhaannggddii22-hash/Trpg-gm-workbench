# WWN 自审查与桌面模拟测试

日期：2026-11-28  
测试范围：当前 main 上的 WWN 规则摘要与主持流程  
测试类型：文档审计 + 手算规则用例 + TEST_ONLY_NON_CANON 主持模拟  
结论：研究文档可进入针对性行为测试；系统仍为 Candidate，不代表完整规则验证通过。

## 1. 审查方法与边界

检查了以下本地文件：
- Rule_Reference/CORE_RUNTIME_GUIDE.md
- Rule_Reference/FACTIONS_AND_MAJOR_PROJECTS.md
- Rule_Reference/WORLD_BUILDING_RUNTIME.md
- Rule_Reference/SITE_TAGS_RUNTIME.md
- Rule_Reference/ADVENTURE_CREATION_RUNTIME.md
- Rule_Reference/README.md
- Research/SOURCES.md
- Testing/README.md

规则抽查使用作者 SRD 1.0 原文；Free Edition 的世界构建和冒险章节使用此前取得的 2021 Free Version 研究定位。当前可访问的 SRD PDF 已可全文检索；Free Edition 第三方镜像本轮访问返回 403，因此本轮没有重新逐页读取整本 Free Edition。第三方镜像不是出版方托管源。

## 2. 文档审查发现

### 已修正

1. **Major Project 范围判断缺少“立即受影响人口”原则。**  
   原摘要只列出 Village / City / Region / Kingdom / Known World 倍率，容易按间接影响范围过度放大难度。现已补充：城镇变成贸易枢纽，若直接改变主要影响城镇居民及最近贸易伙伴，按 City；组织型项目按该机构实际能持续影响的最大范围计算。

2. **Major Project 的魔法项目分支缺失。**  
   普通 Renown 难度公式不足以处理大规模魔法变化。现已补充 Working 的规模、数量和材料/冒险准备边界，并明确王国级 Working 超出现代魔法能力的限制。

3. **既有 Faction 对 Major Project 的一般影响没有写全。**  
   现已补充项目像冒险一样处理：会损伤/创造资产、制造阵营反对，或由盟友贡献 Renown；与玩家阵营通过 Faction Turn 直接协助的数值机制分开。

4. **Faction Tags 与 Asset Qualities 的边界不清。**  
   现已补充 Faction Tags 的作用范围，并要求特殊资产能力回查本地结构化数据，不凭摘要推断。

5. **Frail 的解除条件过于模糊。**  
   现已补充：一周卧床并接受医疗照护，或医生使用治疗工具工作一小时并进行难度 10 的 Dex/Heal 或 Int/Heal 检定。

### 仍需注意

- 核心手册是 SRD 1.0 机制摘要，不是完整玩家规则书。Trauma 的详细武器数据、职业/Focus/法术/资产的完整特性必须查本地数据或原文。
- Site Tags 手册只记录结构和生成方法，不包含具体原书 Tag 名称/条目；这是许可边界下的有意取舍。
- Adventure Creation 中房间规模等建议不应转化为硬性规则；实际地点规模应由游戏时长和场景目的决定。
- 文档摘要不能代替完整 Free Edition 的示例、例外和页码核验。

## 3. 规则手算测试

### T-01｜PC Saving Throw

输入：1 级 PC，Strength 修正 +1，Constitution 修正 0。  
预期：Physical = 16 − 1 − max(+1, 0) = 14。  
结果：14。  
判定：通过。一级无属性修正基础值为 15；不是把公式常数 16 当作最终目标值。

### T-02｜NPC Saving Throw

输入：NPC，3 HD。  
预期：15 − floor(3/2) = 14。  
结果：14。  
判定：通过。

### T-03｜Reaction Roll

输入：2d6 = 7，PC 有机会主动问候，Charisma 修正 +1。  
预期：总值 8，落在 6–8；反应符合该情境通常会有的友善/敌意程度，不自动转为友好或敌对。  
结果：中性基线反应。GM 应在玩家选择初始行动前描述态度信号。  
判定：通过。

### T-04｜Mortally Injured 急救

输入：目标已倒下两个完整 Round；施救者有治疗工具。  
预期：稳定难度 = 8 + 2 = 10；若无工具则为 12。每轮只有一名盟友可尝试稳定，但其他人可以协助；后续轮次可重试。稳定后 10 分钟恢复 1 HP 并获得 Frail。  
结果：难度与时序一致；Frail 解除条件已补入核心手册。  
判定：通过。

### T-05｜Faction Turn 收入与修复

输入：Faction Force 5、Wealth 2、Cunning 4。  
收入：ceil(2/2 + (5+4)/4) = ceil(3.25) = 4 Treasure。  
Force Asset 修复：每次修复恢复 ceil(5/2) = 3 HP；同一 Asset 同轮第二次修复成本 2 Treasure，第三次 3 Treasure。  
Faction 自身 HP 修复：ceil((最高 5 + 最低 2)/2) = 4 HP；每轮只能使用一次，成本 1 Treasure。  
结果：与 SRD 6.2、6.6 公式相符。  
判定：通过。

### T-06｜Major Project 难度

输入：废除一个王国范围内的奴隶制度；变化本身 Improbable；国王为最大反对力量；当地人口普遍强烈反对。  
计算：2 × 16 × 16 × 2 = 1,024 Renown。  
结果：1,024。  
判定：通过。若国王被说服退出反对，最大反对者降为下一层时，难度倍率随之下降；不能继续保留已被解除的国王倍率。

### T-07｜Faction 协助 Major Project

输入：Faction Wealth 4、Force 3、Cunning 2，适合该项目；愿意支援。  
预期：每个 Faction Turn 可协助同一项目一次；消耗本轮 Faction Action 和 1 Treasure；理想适配时属性总和翻倍，难度减少 (4+3+2)×2 = 18，最低降至 1。该减值持续到项目完成或阵营撤回支持。  
结果：18 点减值；符合 SRD 7.9。  
判定：通过。

## 4. TEST_ONLY_NON_CANON 主持流程测试

### T-08｜世界构建按需展开

玩家目标：想让一座边境小镇摆脱盐税垄断。  
运行：
1. 不预先生成整个世界史。
2. 只建立当前区域的交通、河道、盐源和邻近权力关系。
3. 展开目标小镇的治理结构、盐税制度和相关组织。
4. 将具体地点落在盐仓、渡口、旧水闸和镇议事厅。
5. 不为无关的王国宫廷或远方宗教创建完整档案。

结果：足以支持本场冒险；没有生成与玩家目标无关的百科全书。  
判定：通过。

### T-09｜双主题 Tag 生成地点

使用完全原创的测试主题，不引用原书具体 Tag：
- 主题 A：盐税垄断；
- 主题 B：被洪水淹没的旧水利设施。

生成的 Community：
- 可见事实：盐仓入口有官方封条；渡口的秤砣比镇上其他秤重；退潮时旧闸门露出石阶。
- Friends：渡船工知道夜间运盐路线，但担心失去执照。
- Enemies：盐税承包商雇佣的账房与巡守。
- Complication：旧闸门正在缓慢堵塞河道，下一次涨水会淹没下游仓房。
- Thing：一份记录旧水道产权的账簿；闸门钥匙可能在失踪的水利工头手里。
- Places：盐仓、渡口、旧闸门、镇议事厅。

结果：两个主题相互加强；素材产生人物、资源、危机和可调查地点，而非只生成氛围词。  
判定：有条件通过。仍需玩家真实行动验证这些素材是否足够自然、是否有过度预设。

### T-10｜Investigation 多路径

秘密：盐税承包商夜间改道运输，利用旧闸门私运盐货，并伪造部分税账。

线索路径：
1. 账簿路径：对照官方税账与仓库出入记录，发现数量差额。
2. 现场路径：旧闸门石阶上的新鲜盐渍、车辙和绳索纤维指向夜间运输。
3. 人际路径：渡船工或被解雇的水利工人能说明夜间活动，但需要保护或报酬。

失败处理：
- 调查检定失败不抹除线索；失败代价可以是时间流逝、对方察觉、证人提高条件或关键货物转移。
- 三条路径最终指向同一事实，但每条路径提供不同证据和风险。

结果：不存在唯一检定门槛；失败仍改变局势。  
判定：通过（设计层）；尚未进行真实玩家盲测。

### T-11｜四种 Primary Challenge 转换

同一玩家目标“让盐税垄断失去控制”：
- Investigation：证明账目造假并确认私运路线。
- Social：争取镇议会、渡船工与税务官支持。
- Exploration：进入旧闸门，找到私运通道和产权证据。
- Combat：若对手主动暴力阻止，处理守卫或承包商雇佣的打手。

结果：四类挑战都能围绕同一目标成立；Combat 不必成为默认主线。  
判定：通过（结构层）。

## 5. 综合结果

| 测试 | 结果 |
|---|---|
| Saving Throws | 通过 |
| NPC Saves | 通过 |
| Reaction Roll | 通过 |
| Mortal Injury / First Aid | 通过 |
| Faction Turn 收入与修复 | 通过 |
| Major Project 难度 | 通过 |
| Faction 协助项目 | 通过 |
| Worldbuilding 按需展开 | 通过 |
| 双主题 Site Tag | 有条件通过 |
| Investigation 多路径 | 设计层通过，待玩家盲测 |
| 四类 Primary Challenge | 结构层通过 |

## 6. 当前结论

**文档层：有条件通过。** 已修正本轮发现的遗漏；其余核心数值抽查与主要流程手算一致。

**规则层：部分机制通过抽查，不等于全规则验收。** 本轮未逐项测试所有职业、Focus、法术、武器、怪物、资产特殊能力和完整旅行/远征表。

**主持层：设计流程通过初步模拟，未经过玩家盲测。** 双 Tag 和 Investigation 的可玩性仍需要在真实互动中观察。

**系统状态：Candidate。** 下一步优先做一场短小、TEST_ONLY_NON_CANON 的实际玩家测试，验证信息呈现、自由行动、危险压力、NPC反应和规则调用负担；不应继续无限扩张研究文档。
