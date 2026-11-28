# NQB-01 v0.3 Runtime Test Campaign

> **TEST_ONLY / NON_CANON** — 用户授权建立的独立 GM Runtime 测试环境。

本 Campaign 不属于 Zarek / 扎雷克正式战役，不继承任何正式 Campaign 的人物、NPC、关系、装备、资源、记忆、模组事件、Session Log 或 Runtime State。测试内容及结果不得回写任何正式 Campaign。

## 系统绑定
- [SYSTEM_BINDING.md](./SYSTEM_BINDING.md)：`triangle_agency` / 《三角机构》中文 v22。
- 系统唯一权威入口：[Systems/Triangle_Agency/README.md](../../Systems/Triangle_Agency/README.md)。
- 本 Campaign 不复制或改写系统规则。

## 当前测试模组
- [NQB-01 v0.3｜雨脚客栈，雨未停](./Modules/NQB01_V03/README.md)
- GM-only 场景来源：[NQB01_V03_GM_PACKET.md](../../GM_Training/Testing/Baselines/NQB01_V03_GM_PACKET.md)。
- 操作者专用规格、行动序列和审核表仍留在 `GM_Training/Testing/Baselines/`，不得装配给目标 GM。

## 运行状态
- Campaign：`PREPARED_PENDING_PREFLIGHT`。
- Prep QA gate：已在第一次 Preflight 前完成；审核报告保存在操作者专用目录，不属于目标 GM Runtime 上下文。
- Runtime：`NOT_STARTED`；干净目标 Chat 的正式 Preflight 尚未执行，测试 Session 尚未授权启动。
- 初始运行检查点：[Modules/NQB01_V03/03_RUNTIME_STATE.md](./Modules/NQB01_V03/03_RUNTIME_STATE.md)。
- 玩家身份：[TEST_PLAYER_PROFILE.md](./TEST_PLAYER_PROFILE.md)；完整预生成角色卡：[TEST_CHARACTER_SHEET.md](./TEST_CHARACTER_SHEET.md)。唐予安是休假期间私人出行的外勤特工，不是当前任务成员；角色 ARC 与 9 点 QA 已按中文 v22 建立，未复制任何正式角色。

## 目录与状态权威
- `SYSTEM_BINDING.md`：唯一系统绑定。
- `TEST_PLAYER_PROFILE.md`：玩家侧身份与知识边界。
- `TEST_CHARACTER_SHEET.md`：本测试预生成角色的 ARC 与机械数据。
- `Modules/NQB01_V03/03_RUNTIME_STATE.md`：唯一当前 Runtime 快照。
- `Modules/NQB01_V03/04_SESSION_LOG.md`：只记录本测试实际发生的事件。
- `Modules/NQB01_V03/05_PLAYER_NOTES.md`：只记录测试角色实际获知的信息。
- 所有新增记录必须留在本 Campaign 目录；任何测试数据均不得进入正式战役目录。

## 执行准入
环境建立不代表 Preflight 已完成或测试已开始。目标 GM 必须从 `GM_Training/SKILL.md` 正常进入，执行完整 Preflight、系统绑定核验、规则资料装配、Context Assembly 和 Prep-to-Runtime 交接。用户明确授权开始测试前，保持 `NOT_STARTED`。
