# Cairn 2e 初步研究与接入计划

研究日期：2026-11-27
目标：将 Cairn 作为 GM Workbench 第二套独立规则系统接入，并通过 1–2 个短团同时验证 Cairn 运行与 L3 NPC 的 PC 级资源/主动性。
当前阶段：candidate / research and integration preparation。

## 1. 来源核验

- 官方 2e 规则入口：https://cairnrpg.com/second-edition/
- 官方冒险目录：https://cairnrpg.com/adventures/
- 官方 Warden's Guide：https://cairnpress.itch.io/cairn-wardens-guide
- 简体中文社区 SRD：https://fi.cairnrpg.com/localization/second-edition/chinese/
- 官方 2e 文本许可：CC BY-SA 4.0。
- 中文 SRD 页面声明覆盖 Player's Guide、Warden's Guide 全部 31 个核心章节及 CAS-1 至 CAS-4。中文版本作为阅读辅助，官方英文原文作为冲突核验来源。

## 2. 设计概览

Cairn 的轻量来自压缩角色能力与检定结构，而不是取消主持程序：

- 角色只使用 STR、DEX、WIL 三项属性；风险行动通过 d20 属性 Save 解决。
- 背景而非职业决定角色初始装备、能力和身份线索。
- 攻击自动命中，伤害骰减护甲后扣 HP；HP 归零后的溢出伤害会进入 STR 与 Critical Damage 流程。
- 物品格、Fatigue、光源、口粮和旅行时间是探索资源压力的核心。
- 地城探索使用 Turn / Action / Consequence 循环，并通过 Dungeon Events 表使时间与噪音产生后果。
- 荒野探索通过 Watch、Travel、Make Camp、天气、迷路与事件程序抽象处理旅程。
- Warden 原则强调中立、信息透明、虚构优先、NPC 自利且求生、随机表生成局势而非剧情。

## 3. 对 GM Workbench 的研究价值

### 高价值

1. **信息呈现与玩家能动性**：可见信息直接提供，不用检定挡住合理观察；行动风险在玩家决定前明确。
2. **NPC 自主性**：Reaction、目标、利益、求生意愿和记忆共同驱动互动，不把 NPC 当线索自动售货机。
3. **环境与时间压力**：地城循环让停留、噪音、快速移动和探索区域产生明确成本。
4. **低成本状态管理**：HP、属性、护甲、Fatigue、物品格、光源和口粮形成较小但有意义的状态集合。
5. **程序化世界而非剧情生成**：随机表提供遭遇、迹象、环境变化、损耗、疲劳或安静，不强迫剧情走向。

### Warden's Guide 的额外发现

- Cairn 没有通用知识/专长检定或感知检定；知识由虚构背景与经历支撑，基本感官可感知的信息应充分提供。
- NPC Tables 提供姓名、外观特征、背景、目标、美德与恶癖等生成素材，但 L3 NPC 还需要独立的目标、事务、资源、关系和知识模型。
- Growth 是经历产生显著影响后的适应结果，不是每次经历后的自动奖励。
- 地城主持要明确空间位置、危险、感官信息和探索时间成本；荒野程序通过 Watches、行动、路线与事件维持玩家选择。
- 详见 [Warden's Guide 导航](../Rule_Reference/WARDEN_GUIDE_INDEX.md)。

### 与现有工作台的关系

- 可迁移至 GM_Training 的候选方法：信息透明、风险预告、NPC 自利、环境状态持续性、随机表与因果一致性。
- 不应直接迁移至通用 GM 规范的系统规则：属性豁免、自动命中、伤害、HP/属性分层、Fatigue、库存格、地城事件表、Watch 等。
- Cairn 专属机制留在 Systems/Cairn；只有经跨系统实战验证的主持方法才考虑进入 GM_Training。

## 4. 单人短团风险

Cairn 的默认冒险通常以 party 为单位，战斗危险且角色可能死亡。单玩家与 GM 的短团需要先明确角色规模和同伴控制权。

建议初测：
- 玩家只创建并控制一个 PC。
- 若模组/风险需要队伍支援，使用规则内 hirelings；由 GM 扮演其行动、动机与反应，不把他们当无条件战斗工具。
- 不擅自降低伤害、改变 Critical Damage 或死亡规则。
- 若模组明确依赖多人协作，先换模组，不在首次测试中悄悄改写结构。

## 5. 短团模组候选

优先只考虑明确标注 Cairn 2e、可获得合法文本且能支持短时体验的作品：

1. **CAS-2: Rise of the Blood Olms** — 官方入门冒险，探索新发现的洞穴并寻找失踪远征队；官方说明其危险但可通过批判思考与谨慎探索生存。适合验证地城循环、危险提示、资源消耗和战斗规则。单人适配风险较高，必须先读完整模组并评估队伍规模。
   - 官方入口：https://cairnpress.itch.io/rise-of-the-blood-olms
2. **CAS-1: Trouble in Twin Lakes** — 官方独立冒险，包含两个核心谜团、多个 NPC 和地点；适合验证调查、线索分布、NPC 自主性和非线性探索。
   - 官方规则/模组文本：https://cairn.puzzledungeon.com/adventures/first-party/cas-1/
3. **CAS-3: The Feast of Tegny Wood** — 官方独立 2e 冒险，采用 forestcrawl 结构，主题涉及疾病、职责与腐朽；适合验证荒野探索、环境变化和事件程序。
   - 官方入口：https://cairnrpg.com/adventures/first-party/cas-3/
4. **A Feast for Flies** — 社区原创、官方索引标记为 Cairn one-shot 且免费；作为短团备选，需进一步核对 2e 兼容性和单人队伍适配。
   - 官方冒险索引：https://cairnrpg.com/adventures/

## 6. 建议测试顺序

- **短团 1：L3 NPC 与调查验证**。优先评估 CAS-1《Trouble in Twin Lakes》。官方介绍确认它包含两个核心谜团、多个 NPC 与多个探索地点；适合测试 L3 NPC 的 PC 级资源账本、独立目标、日程、关系、信息边界、主动行动与玩家干预。模组文本采用 CC BY-SA 4.0。单人队伍适配仍需完整备团后评估，不能因其适合新老玩家就推定适合单 PC。
- **短团 2：地城探索与生存资源验证**。优先评估 CAS-2《Rise of the Blood Olms》。官方明确称其为入门冒险且致命，角色可通过批判思考和谨慎探索生存；适合验证 Dungeon Cycle、事件触发、资源消耗、危险提示、战斗与死亡规则。单人队伍适配风险较高，必须先评估 PC、hirelings 与遭遇规模。若 CAS-2 对单人桌面不合适，则考虑 CAS-3 的荒野/森林探索验证。

若只运行一个短团，优先 CAS-1，因为本次特别增加了 L3 NPC 资源与主动性测试目标；但正式选择仍以完整 GM-only 备团和单人风险审查为准。
- 每次测试都标记 TEST ONLY / NON-CANON，独立 Campaign 状态，结束后做规则准确性、信息公平、NPC 区分度、探索自由、节奏与连续性复盘。

## 7. L3 NPC 联合测试

本次短团还将用于验证 Workbench L3 NPC 能否在 Cairn 环境中保持 PC 级资源意识与独立主动性。L3 是 Workbench 人物模拟投入等级，不是 Cairn 官方角色等级。

- 测试对象为明确登记的 L3 NPC；PC 由用户创建，大概率使用“凯瑟琳”作为另一世界的平行角色。
- 新 PC 与 Triangle Agency 凯瑟琳只共享用户明确确认的人格核心/设定相似点；不继承原角色履历、能力、关系、记忆和物品。
- PC 的个人印记从 Cairn 世界中的背景、经历、可获得工具和生活环境自然形成。速写、拓印、符号记录等可以探索，但不预先写入 CANON。
- L3 NPC 使用 Workbench 的 PC 级资源账本：必要时追踪属性、HP、Armor、Fatigue、库存/装备、食物、光源、工具、金钱、人手、时间、承诺与知识。该要求不代表 Cairn 官方要求所有 NPC 按 PC 生成。
- L3 NPC 需有独立目标、事务、计划、日程、资源限制和触发条件；能拒绝、调整、主动行动或不行动。
- 离场时按需模拟：只保留锚点与触发条件；游戏内时间或事件推进后再核算，现实消息间隔不触发；重逢时不得重置，也不得泄露玩家未获知的私有经历。
- 至少覆盖共同场景互动、PC 离场/重逢、PC 打乱 NPC 计划、资源竞争与风险后果。
- 详细执行标准见 [L3 NPC PC 级资源与主动性测试计划](../Testing/L3_NPC_PC_RESOURCE_AND_AUTONOMY_TEST_PLAN.md)。

## 8. 接入完成标准

1. 规则原文核验完成，中文 SRD 关键差异已记录。
2. Rule Index、GM Skill、Preflight 与 Campaign Binding 模板可独立使用。
3. 规则正例/反例/边界测试通过。
4. Triangle Agency ↔ Cairn 隔离测试通过。
5. 1–2 次短团完成并复盘。
6. 根据实测修订系统 Skill 与运行流程，再由用户决定是否将状态升级为 active。

## 9. 当前限制

本文件是初步研究，不是完整规则摘要，也不是模组备团文件。模组的隐藏信息、完整内容、遭遇细节和 GM-only 资料应在选定后单独备团，不在通用研究文档中暴露给玩家。
