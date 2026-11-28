# 核心规则索引

> 默认范围：Core Set only。Rule Area 用于定位；实际运行优先调用 `CORE_RULES_RUNTIME.md` 的 Rule ID。  
> 当前运行化状态：首轮本地规则手册已建立；逐项测试仍待进行。

## 主要规则区域

| Rule ID | 规则区域 | 本地运行资料 | 当前状态 |
|---|---|---|---|
| DH-LOOP | 游戏流程与场景循环 | CORE_RULES_RUNTIME §2 | SOURCE_IMPORTED |
| DH-SPOTLIGHT | Spotlight 与行动经济 | CORE_RULES_RUNTIME §3 | SOURCE_IMPORTED |
| DH-CREATE | 角色创建 | CORE_RULES_RUNTIME §4、CHARACTER_OPTIONS_INDEX | SOURCE_IMPORTED |
| DH-ACTION | Duality Dice 动作掷骰 | CORE_RULES_RUNTIME §5 | SOURCE_IMPORTED |
| DH-HOPE-FEAR | Hope / Fear 资源 | CORE_RULES_RUNTIME §6 | SOURCE_IMPORTED |
| DH-GM-MOVE | GM Moves 与后果 | CORE_RULES_RUNTIME §7 | SOURCE_IMPORTED |
| DH-REACTION | Reaction Roll | CORE_RULES_RUNTIME §8 | SOURCE_IMPORTED |
| DH-GROUP / DH-TAG-TEAM | 协作行动与 Tag Team | CORE_RULES_RUNTIME §9 | SOURCE_IMPORTED |
| DH-ADV | Advantage / Disadvantage | CORE_RULES_RUNTIME §10 | SOURCE_IMPORTED |
| DH-SPELLCAST | Spellcast Roll | CORE_RULES_RUNTIME §11 | SOURCE_IMPORTED |
| DH-ATTACK | PC 攻击 | CORE_RULES_RUNTIME §12 | SOURCE_IMPORTED |
| DH-ENEMY-ATTACK | 敌人攻击 | CORE_RULES_RUNTIME §13 | SOURCE_IMPORTED |
| DH-DAMAGE | HP、阈值、Armor、抗性 | CORE_RULES_RUNTIME §14 | SOURCE_IMPORTED |
| DH-RANGE | 距离、移动、视线 | CORE_RULES_RUNTIME §15 | SOURCE_IMPORTED |
| DH-CONDITION | Hidden / Restrained / Vulnerable 等 | CORE_RULES_RUNTIME §16 | SOURCE_IMPORTED |
| DH-DOMAIN | Domain Cards / Loadout / Vault | CORE_RULES_RUNTIME §17 | SOURCE_IMPORTED |
| DH-REST | Short / Long Rest | CORE_RULES_RUNTIME §18 | SOURCE_IMPORTED |
| DH-COUNTDOWN | 倒计时与进度 | CORE_RULES_RUNTIME §19 | SOURCE_IMPORTED |
| DH-NPC | 普通 NPC 运行 | CORE_RULES_RUNTIME §20 | SOURCE_IMPORTED |
| DH-ENEMY-DATA | Adversary 数据结构 | CORE_RULES_RUNTIME §21、ADVERSARY_INDEX | SOURCE_IMPORTED |
| DH-ENV-DATA | Environment 数据结构 | CORE_RULES_RUNTIME §21、ENVIRONMENT_INDEX | SOURCE_IMPORTED |
| DH-ENCOUNTER | Battle Points 遭遇预算 | CORE_RULES_RUNTIME §22、LOOKUP_TABLES | SOURCE_IMPORTED |
| DH-GEAR | 装备、库存与 Gold | CORE_RULES_RUNTIME §23、Reference_Data | SOURCE_IMPORTED |
| DH-LEVEL-UP | 成长与升级 | CORE_RULES_RUNTIME §24 | SOURCE_IMPORTED |
| DH-DEATH | Death Move | CORE_RULES_RUNTIME §25 | SOURCE_IMPORTED |
| DH-GM-GUIDANCE | GM Principles / GM Practices / GM Moves / NPC / Environment | GM_GUIDANCE_RUNTIME.md | SOURCE_CHECKED |

## 核心选项

- 9 个 Core 职业、18 个子职业、9 个核心领域、189 张领域卡。
- 18 个 Core Ancestries、9 个 Core Communities、24 个 Beastforms。
- 129 个 Core Adversaries、19 个 Core Environments。
- 183 件 Core Weapons、34 件 Core Armor、60 件 Core Items、60 种 Core Consumables。

详细数据见 [Reference_Data/README.md](../Reference_Data/README.md) 和 [CHARACTER_OPTIONS_INDEX.md](./CHARACTER_OPTIONS_INDEX.md)。

## 不属于默认 Core Set 的内容

- Assassin、Brawler、Warlock、Witch 与对应子职业。
- Dread Domain 与 21 张 Dread Domain Cards。
- Hope & Fear 的 6 种 Transformations。
- Hope & Fear 新增的种族、社群、装备、敌人与环境。
- SRD 2.0 混合版本的 Character Creation / Classes / Domains 原始章节，统一存放在 `Reference_Data/Mixed_Version/`。
- Supplemental Campaign Mechanics，单独存放在 `Reference_Data/Optional_Procedures/`。

扩展详细列表见 [Hope & Fear 隔离清单](../Expansions/Hope_and_Fear/README.md)。

## 下一轮核验顺序

1. 对 CORE_RULES_RUNTIME 中的关键机制建立正例、反例、边界用例，重点是动作掷骰、Reaction Roll、资源时序、伤害/Armor 和休息。
2. 按 Core Errata 更新卡牌、装备和运行条目。
3. 核验结构化敌人与环境字段是否能覆盖所有触发和结算需求。
4. 取得合法 Core Rulebook 后补齐 SRD 未覆盖的 GM 细节、示例与细微规则解释。
5. 完成独立 Preflight 与短场景主持测试，再评估是否从 candidate 升级。

`SOURCE_IMPORTED` 不等于 `VERIFIED_CORE` 或 `RUNTIME_TESTED`。未经测试的条目不得宣称已验收。