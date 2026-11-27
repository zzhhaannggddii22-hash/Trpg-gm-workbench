# NQB-01 v0.3｜雨脚客栈，雨未停

> TEST_ONLY / NON_CANON｜GM-only 资料与玩家侧资料严格分离。
> Fixture: NQB-01 v0.3
> Campaign: `nqb01_v03_test`
> System: `triangle_agency` / 中文 v22
> Runtime: NOT_STARTED

## 文件索引
- [01_GM_PREP.md](./01_GM_PREP.md)：模组 GM Prep 入口。
- [02_NAME_INDEX.md](./02_NAME_INDEX.md)：NPC 与场景对象规范名称。
- [03_RUNTIME_STATE.md](./03_RUNTIME_STATE.md)：本模组唯一 Runtime 检查点。
- [04_SESSION_LOG.md](./04_SESSION_LOG.md)：本测试实际事件记录。
- [05_PLAYER_NOTES.md](./05_PLAYER_NOTES.md)：玩家侧已知信息。
- [06_POSTMORTEM.md](./06_POSTMORTEM.md)：测试后复盘；执行前保持空白。

## 来源
- GM-only 场景来源：[NQB01_V03_GM_PACKET.md](../../../../GM_Training/Testing/Baselines/NQB01_V03_GM_PACKET.md)。
- 玩家启动材料：[NQB01_V03_PLAYER_PROMPT.md](../../../../GM_Training/Testing/Baselines/NQB01_V03_PLAYER_PROMPT.md)。
- 操作者专用规格、行动序列、审核表和执行提示不得装配给目标 GM。

## 运行纪律
1. 必须经过主 GM Skill、Preflight、系统绑定、系统规则资料装配、Context Assembly 与 Prep-to-Runtime。
2. 所有状态写入仅允许发生在本 Campaign 本模组目录；不得写入 Zarek 或其他正式 Campaign。
3. GM-only Packet 不得向玩家展示；玩家启动材料是玩家侧唯一预置场景资料。
4. 当前场景不含强制危机或必需谜题；不得为了测试覆盖而制造冲突。
5. 任何测试行动、NPC、物件、承诺、时间变化与输出均为 NON-CANON。
