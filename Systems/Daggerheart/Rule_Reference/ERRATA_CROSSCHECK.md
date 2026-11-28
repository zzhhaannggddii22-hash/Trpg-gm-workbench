# 官方 Core Errata 与公开 SRD 2.0 交叉核验

> 核验基准：2025-09-09 Official Core Errata；2026-08-25 Official SRD 2.0。  
> 当前用途：核对旧版印刷核心书/卡牌勘误是否已进入公开 SRD 2.0 结构化数据。  
> 状态：抽样核验已完成；并非对所有实体卡牌、完整 Core Rulebook 页面和所有勘误条目的穷尽验收。

## 1. 来源

- [官方 Core Errata（2025-09-09）PDF](https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-Errata-September9th2025.pdf)
- [官方 SRD 2.0 页面](https://www.daggerheart.com/srd/)
- [官方 SRD 2.0 PDF（2026-08-25）](https://www.daggerheart.com/wp-content/uploads/2026/08/DH_SRD_2_2026_08_25.pdf)
- [官方 Downloads / Errata](https://www.daggerheart.com/downloads/)
- [第三方中文维基：Daktadae, The Cleaver](https://daggerheart.huijiwiki.com/wiki/%E2%80%9C%E9%93%A1%E5%88%80%E2%80%9D%EF%BC%8C%E8%BE%BE%E5%85%8B%E5%A1%94%E6%88%B4)（仅用于定位，非权威规则源）

官方 SRD 2.0 Changelog 声明已修复拼写/抽取错误并落实此前勘误；官方 Downloads 仍保留 Core 与 Hope & Fear 的 Errata 分区。因此本文件不把“SRD 2.0 已实现勘误”解释成“所有 Core Rulebook 印刷版、卡牌与辅助表差异都已逐项消失”。

## 2. 抽样核验表

| Errata 条目 | 2025 Errata 修正方向 | SRD 2.0 / 本地数据结果 | 处理 |
|---|---|---|---|
| Powerful Beast Beastform | Strength +3、Evasion +1 | 当前 Beastform 结构化记录一致 | Core 数据保留 |
| Striking Serpent | Venomous Strike 使用 Direct Physical Damage | 当前 Feature 文本一致 | Core 数据保留 |
| Legendary Hybrid | 攻击伤害类型补为 Physical | 当前记录为 phy | Core 数据保留 |
| Beastform Step 4 | 变形时选择合适的 Physical / Magic Damage | 属于规则步骤；仍须以对应书籍规则确认完整上下文 | Runtime 结合 Beastform 规则调用 |
| Beastbound Companion | Companion 伤害类型选项调整 | SRD2 的相关子职业文本需进一步逐卡确认 | 未标为完全核验 |
| Rogue: Cloaked | 脱离 Hidden 的条件补充：攻击或结束移动后进入敌人视线 | Rogue Class Feature 当前文本包含两种结束条件 | Core 数据匹配 |
| Rogue Hope Feature | 没有攻击成功时，Evasion 加值持续到下次休息 | 当前 Class Hope Feature 文本一致 | Core 数据匹配 |
| HP / Stress 上限 | 两类资源槽最大 12 | 当前 Runtime 按 12 上限记录 | Runtime 已纳入 |
| Hidden | 敌人移动到可见位置、PC 进入视线或攻击时结束 | 当前 Conditions 规则一致 | Runtime 已纳入 |
| Experiences | 对两个 Experiences 各提升 +1 | 当前升级规则按两项 Experiences 处理 | Runtime 已补充步骤 |
| Glowing Rings | Tier 1 伤害调整为 d10+2 Magic | 当前武器数据一致 | Core 武器数据匹配 |
| Spear | 移除 Cumbersome；各 Tier 伤害调整 | 当前 Tier 1 Spear 为 d8+3 Physical，且无 Cumbersome | Core 武器数据匹配 |
| Longsword | 各 Tier 伤害调整 | 当前 Tier 1 Longsword 为 d10+3 Physical | Core 武器数据匹配 |
| Buckler: Deflecting | 2025 Errata 用语为 “available Armor Slots” | SRD 2.0 PDF / 结构化记录用语为 “available Armor Score” | 术语差异保留；当前运行按较新的 SRD 2.0 用语 |
| Knuckle Claws | Tier 4 Burden 改为 One-Handed | 当前 Tier 4 Knuckle Claws 为 One-Handed | Core 武器数据匹配 |
| Sweet Moss | 休息时可清除 1d10 HP 或 Stress | 当前 Consumable 数据一致 | Core 消耗品匹配 |
| Long-term Countdown | 长休通常推进一个相关长期倒计时一次 | SRD 2.0 Rest 摘要允许 GM 推进一个 Long-term Countdown；2025 Errata 进一步建议长休时通常推进一次与当前局势相关的长期倒计时 | Runtime 采用“通常推进一个相关倒计时一次”；具体规则文本优先 |
| Adversary Actions | 补充 Adversary Rolls 的交叉引用 | SRD 2.0 有独立 Adversary Action / Roll 指引 | Runtime 已补入非攻击行动与 Reaction 区分 |
| Team-Up Reaction | 触发距离改为 Very Close | 当前需按具体 Adversary Feature 文本检查；未作为通用机制写入 | 单项 Feature 核验 |
| Glass Snake | Armor-Shredding Shards：无法标记 Armor Slot 时标记 HP | 当前 Glass Snake Feature 一致 | Core Adversary 数据匹配 |
| The Box | Relentless 改为 (2) | 当前公开 SRD 对应 Stat Block 名称为 Battle Box，相关 Feature 文本仍以 The Box 指称，Relentless (2) | 按 SRD 2.0 名称保存；旧称作为定位别名 |
| Adult Flickerfly | Hallucinatory Breath 类型改为 Reaction | 当前 Feature 类型为 Reaction | 对应数据匹配 |
| Seraph（Adversary） | Relentless 改为 (3) | 公开 SRD 2.0 对应 Stat Block 名称为 High Seraph，其文本以 The Seraph 指称，Relentless (3) | 按 High Seraph 的当前数据保存；不要与 Core Class Seraph 混淆 |
| Zombie Legion | 攻击名称改为 Undead Hands | 当前公开数据使用 Undead Hands | Adversary 数据匹配 |
| Sledgehammer | Massive：−1 Evasion，而不是 −1 Agility | 出现在 Supplemental Campaign Mechanics 的 Everyday Hero 起始装备可选表，不在默认 Core 武器表 | 保留在 Optional Procedures，不纳入默认装备 |
| Revolver | Western 可选武器伤害骰调整为 d8 | 出现在 Supplemental Campaign Mechanics 的 Western 选项表 | 保留在 Optional Procedures，不纳入默认装备 |
| Daktadae, The Cleaver | Colossal Power 改为 Reaction；失败攻击时 GM 获得 Fear | 官方 Core Errata（p.322）确认修正文本；第三方中文维基可定位到完整 Stat Block，但公开 SRD 2.0 Adversary JSON 未收录 | 仅记录公开 Errata 修正；不将第三方完整 Stat Block 复制进公开数据，待合法 Core Rulebook 来源核验 |
| Whirlwind | 文字与额外目标伤害说明调整 | 当前领域卡文本与 SRD 2.0 数据一致 | Core Domain Card 匹配 |
| I See It Coming | 触发条件与 Stress 成本澄清 | 当前领域卡文本一致 | Core Domain Card 匹配 |
| Splintering Strike | 使用范围和伤害分配步骤澄清 | 当前领域卡文本一致 | Core Domain Card 匹配 |
| Book of Grynn | Arcane Deflection / Time Lock / Wall of Flame 文字与格式修正 | 当前 Grimoire 文本与 SRD 2.0 结构化数据一致 | Core Domain Card 匹配 |

## 3. 必须保留的版本边界

### “The Box” 与 “Battle Box”
旧 Errata 称为 The Box；SRD 2.0 当前结构化 Stat Block 使用 Battle Box。工作台以 SRD 2.0 当前名称为主，检索时保留旧称作为别名，不复制两份 Stat Block。

### “Seraph” 的同名歧义
Seraph 是 Core Set 的 PC Class；Errata 中被修正 Relentless (3) 的 Seraph 是 Adversary Stat Block。不可将其误认为 Seraph 职业特性。公开 SRD 2.0 Adversary 数据中未发现该敌人，因此当前没有把它加入 Core Adversaries。

### Buckler 术语差异
2025 Errata 的 Buckler Deflecting 使用 “available Armor Slots”；SRD 2.0 PDF 与对应 JSON 使用 “available Armor Score”。当前本地 Runtime / 数据按 SRD 2.0 当前文本执行，并将印刷版/旧 Errata 差异保留在 RULE_ISSUES。取得最新官方 Core Rulebook 或新 Errata 后再复核。

### 书籍/可选章节独有项目
Sledgehammer 和 Revolver 的勘误目标来自可选 Supplemental Campaign Mechanics，不属于基础装备表。High Seraph 已与公开 SRD 2.0 的当前 Stat Block 对应。Daktadae 的存在与 Colossal Power 修正已由官方 Core Errata 确认，但完整 Stat Block 不在公开 SRD 2.0 Adversaries 数据中；第三方中文维基可用于定位，不作为正式规则源。公开仓库只记录 Errata 修正，不复制完整 Stat Block；取得合法 Core Rulebook / 相关卡片后再补私人运行资料。

## 4. 当前结论

- 已抽样确认的主要 Beastform、武器、消耗品、Rogue 特性、Glass Snake、Battle Box、Adult Flickerfly、Zombie Legion 和领域卡修正，均能在 SRD 2.0 当前数据中找到对应结果。
- 少数项目存在术语差异，或属于 Optional Campaign Procedures / 完整规则书而非公开 SRD 数据。
- 因此本工作台使用 SRD 2.0 作为现行公开参考，另存旧 Errata 对照；不把旧版勘误文本无差别覆盖到新版数据。
- 本表属于抽样证据；后续仍需对完整 Core Rulebook、实体卡牌、官方 Errata 和公开 SRD 的边界做更完整核验。
