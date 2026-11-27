# Cairn 2e Preflight（候选版）

> 仅适用于 `system_id: cairn`。当前系统状态 candidate；本文件用于研究与未来测试准备，不代表已达到 active。

## A. 系统绑定

- [ ] Campaign 的 `SYSTEM_BINDING.md` 明确 `system_id: cairn`。
- [ ] 规则版本明确为 Cairn Second Edition，中文 SRD 仅作非官方阅读辅助。
- [ ] 系统登记表、入口路径、系统 ID 与版本完全一致。
- [ ] 不加载 Triangle Agency 的规则、资源、角色状态或模组状态。

## B. 规则准备

- [ ] 读取 `Rule_Reference/CORE_RULES_RUNTIME.md` 与 `RUNTIME_PROTOCOL.md`，确认本次运行调用版本。
- [ ] 核心规则已按 Rule ID 规范化；常规行动不依赖实时网页搜索。
- [ ] 标记本次冒险会用到的 PARTIAL / MODULE_DEPENDENT 条目，并提前核对对应官方 2e 原文/表格。
- [ ] 核对玩家手册：角色创建、Background、属性、HP、库存、装备、法术书。
- [ ] 核对核心规则：Saves、恢复、Deprivation、Armor、Reaction、Morale、Combat、Critical Damage、属性损伤、死亡、Retreat。
- [ ] 核对监守手册：Dungeon Exploration、Wilderness Exploration、Pointcrawls、NPC Tables、Bestiary、Growth、Knowledge & Perception。
- [ ] 所有关键规则均能回查官方英文 2e 原文；中文翻译差异已记录。
- [ ] 模组使用的规则程序与其适用版本相符。
- [ ] 确认 Runtime Snapshot 能记录时间阶段、Rule ID、待结算触发与资源差分。
- [ ] 根据本次模组选择并执行核心规则回归矩阵中的适用用例；失败项修复或明确阻断后才能进入实测。

## C. 桌面与角色

- [ ] 确认单人玩家测试所用的 PC 数量、hirelings / 同伴与控制权安排。
- [ ] 完成角色创建，逐项记录属性、HP、装备、物品格、Fatigue、背景、Traits、Bonds 与 Omens。
- [ ] 确认玩家理解战斗危险、HP 与属性损伤差异、死亡后替代角色规则。
- [ ] 确认光源、口粮、工具、负重和其他关键消耗品的记录方式。

## D. L3 NPC 与 PC 测试准备

- [ ] 明确区分用户控制的 PC 与 GM 模拟的 L3 NPC；不得把玩家角色和 NPC 的控制权混淆。
- [ ] PC 由用户按 Cairn 2e 创建；若为另一世界的凯瑟琳，只继承用户确认的人格核心，不导入 Triangle Agency 角色履历、能力、关系或物品。
- [ ] L3 NPC 明确登记；L3 是 Workbench 模拟投入等级，不是 Cairn 官方等级。
- [ ] L3 NPC 有独立目标、事务、计划、日程、触发条件、知识边界与关系承诺。
- [ ] L3 NPC 的 PC 级资源账本按情境维护：属性/HP/Armor/Fatigue、装备/库存、食物/光源/工具、金钱/人手、时间和社会资源；不把此 Workbench 要求误写为 Cairn 官方 NPC 创建规则。
- [ ] 明确游戏内时间锚点、离场按需模拟与重逢状态核算；现实时间不触发模拟。
- [ ] 确认 PC 可见信息与 NPC 私有知识分离；资源交付/消耗/丢失均有状态依据。
- [ ] 计划覆盖互动、离场重逢、打乱计划、资源约束与风险后果。

## E. 模组与世界状态

- [ ] 模组来源、版本、版权许可和玩家可见资料已确认。
- [ ] GM-only 信息与玩家资料隔离。
- [ ] 地图、地点、NPC 目标/动机、Reaction、遭遇、线索、事件表和因果关系已核对。
- [ ] 明确时间推进、地城事件触发、旅行 Watch、天气、迷路、营地与资源消耗程序。
- [ ] 不把随机表结果写成预设剧情；随机生成结果与既有事实相容。

## F. 运行锁与验收

- [ ] Runtime 快照记录 `system_id: cairn`、规则版本、Campaign 与 Module。
- [ ] 规则缺口标为 UNKNOWN，不借用其他系统机制填补。
- [ ] 正例、反例、边界案例和跨系统污染测试已完成。
- [ ] 若是短团测试，明确 NON-CANON / TEST ONLY，禁止把测试角色状态继承到其他战役。
- [ ] Preflight 完成后才可进入正式游戏；candidate 状态下仍不得宣称系统已正式激活。
