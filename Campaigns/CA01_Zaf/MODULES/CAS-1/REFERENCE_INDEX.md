# CAS-1｜本地模组资料检索索引

> **权限：GM-only。** 本索引会暴露模组人物、地点和秘密结构；不得放入 Player Notes、玩家 handout 或公开 Preflight 输出。
> Campaign：CA01_Zaf / Twin Lakes
> Module：CAS-1 — Trouble in Twin Lakes
> System：Cairn Second Edition（Candidate）
> 状态：备团资料已归档；战役未开始；本索引不初始化 Runtime State 或 Session Log。

## 1. 本地权威资料

| 文件 | 用途 | 权威层级 |
|---|---|---|
| [SOURCE/CAS1_OFFICIAL_SOURCE.md](./SOURCE/CAS1_OFFICIAL_SOURCE.md) | CAS-1 官方 Markdown 全文归档：剧情、NPC 原始描述、地点、遭遇、怪物、陷阱、独特物品、时序与结局 | 模组原文 SOURCE |
| [GM_ONLY_PREP.md](./GM_ONLY_PREP.md) | 中文主持准备、时间线、空间拓扑、NPC 知识边界、状态时钟、遭遇处理、规则路由和裁定记录 | GM-only 工作文件；须区分 SOURCE / GM_INFERENCE / GM_PREP_CHOICE |
| [MANIFEST.md](./MANIFEST.md) | 版本、来源、许可、迁移历史及未解决差异 | 来源元数据 |
| [OFFICIAL_CATALOG_INDEX.md](../../../../Systems/Cairn/Rule_Reference/OFFICIAL_CATALOG_INDEX.md) | Cairn 2e 通用怪物、Spellbooks、Relics、NPC Tables、20 个 Backgrounds 离线目录 | 系统级官方快照 |

## 2. GM-only Prep 快速定位

### 核心剧情与事件时钟

- §0：来源优先级、Fasha HP 的来源差异与当前临时裁定。
- §1：模组前提与两条彼此独立的谜团线。
- §2：Aldra/Tideborn 与 Jandy/Cities 两条委托、报酬及交付条件。
- §4：事件时间控制，包括 Victim Schedule、Annafranax/Gate clock、Vuk clock，以及防止重复结算的规则。
- §8：Deadmill 与时间循环。
- §10：Temple of the Fungal Lizards 的空间结构和关键状态。
- §11：模组独特 Relics 与物品。
- §17：尚待解决的来源差异和准备事项。

### NPC 目录

GM-only Prep §6 保存 NPC 的行为模型、已知信息、动机和知识边界：

- Reeve Trellis
- Fasha
- Aldra
- Flavia
- Jandy
- Giva
- Drum
- Annafranax

NPC 的原始描述与数值应同时对照官方归档的 Important NPCs 对应章节。不能把 GM-only 真相自动写入 NPC 的知识，也不能把一个 NPC 的信息传播给其他 NPC，除非存在可追踪的信息来源。

### 地点、线索与遭遇

GM-only Prep §7–10 及官方归档对应地点章节：

- Isthmus Town：Stuffed Inn、Butcher Shop、Giva's Home、Farming Path、Dunston。
- Old Mill Road、Stone Forest、Deadmill、East Lake Pass、The Downs。
- White Tower Fens：Whistlewood、Pit Trap、Log Trap、White Tower、Bone Sump。
- Temple of the Fungal Lizards：T1–T10b、Vuk、Memory Prism。

遭遇、陷阱和房间数据以具体地点条目为准；不要仅凭地图邻接推断房间内容，也不要提前触发尚未满足的事件时钟。

### 旅行、传闻与随机遭遇

- GM-only Prep §5：旅行路线、Rumors、Road Encounters。
- 模组说明指出 Twin Lakes 区域地点距离较短，常规 Wilderness Procedures 通常不是主要流程；按模块自己的 Road Encounter 表处理。
- Cairn 通用旅行/Watch 规则仍用于模块未覆盖的部分；不得用通用 Wilderness Event 表替代模块专属道路遭遇表。

### 结局与独特物品

- 官方归档 Concluding the Adventure：分别检查 Vuk 是否重生、Gate 是否开启，以及组合分支。
- 官方归档 Relics & Items：Eye of Vuk、Fletcher's Ire、Echo Spark、Moon Cloth、Curved Dagger。
- 这些物品的能力、限制与后果属于 CAS-1 专属数据，不得与系统级 Reliquary 的同名/相似条目混淆。

## 3. 规则检索顺序

1. 先查本索引定位到 GM-only Prep 的具体章节。
2. 再查 SOURCE 归档中的对应原文，确认模组事实与专属程序。
3. 模组未覆盖的基础机制，查 Systems/Cairn/Rule_Reference/CORE_RULES_RUNTIME.md。
4. 查具体怪物、Spellbook、普通 Relic 或 Background 时，查 Systems/Cairn/Rule_Reference/OFFICIAL_CATALOG_INDEX.md 对应本地快照。
5. 若官方来源和本地 Prep 冲突，先暂停相关裁定，记录差异；不得静默用推断替换 SOURCE。

## 4. 已知待核项目

- Fasha 的 HP：官方 Markdown 与 2026-03-31 发布说明存在不同步。现有 Prep 将 10 HP 标记为 GM_INFERENCE，尚不能写成官方 SOURCE；正式使用前优先核对官方 PDF。
- Annafranax 携带的四本 Spellbooks：官方模块未固定具体清单；属于 GM_PREP_CHOICE，首次使用前需完成选择并记录。
- 起始场景与时间：尚未确定，不得在 Preflight 阶段擅自推进。
- 玩家角色人物卡与资源：以已确认的人物卡为准；不得从旧测试角色推测本战役状态。

## 5. 运行与保密边界

- 本目录中的 SOURCE 与 GM_ONLY_PREP 均为 GM 使用资料。
- 只有角色通过调查、对话、观察、推理或其他有效行动获得的信息，才进入玩家角色知识。
- 模组时钟、NPC 计划和遭遇状态在实际运行前不启动。
- 任何本地目录索引都不能替代 Runtime State 与 Session Log；两者只在战役正式开始后按运行协议创建和更新。
