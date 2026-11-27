# Runtime State｜Twin Lakes VR

> 状态：NOT STARTED
> canon_status: TEST_ONLY_NON_CANON
> 模组备团已完成；当前尚未开始游戏。

## 桌面锁

- system_id: cairn
- ruleset_version: Cairn Second Edition
- validation_id: CAIRN-VR-TWIN-LAKES-01
- module_id: CAS-1_TROUBLE_IN_TWIN_LAKES
- party_size_baseline: 2
- party_roles: user-controlled PC + assistant-controlled Katherine PC
- frame: shared VR game
- Katherine_rules_identity: full_player_character
- GM_Katherine_information_boundary: strict

## 角色与资源

- 用户 PC：未在本备团流程中读取或推算人物属性、装备、背景及资源。
- 凯瑟琳 PC：角色卡待创建/确认；不预填任何属性或资源数值。
- 双方均采用完整 Cairn 2e 玩家角色规则和同粒度资源账本。
- 模组备团与队伍风险基准按两名冒险者完成，不因未知人物卡调整模组内容、敌人数据或危险程度。

## 游戏状态

- 游戏内时间：NOT STARTED
- 地点：NOT STARTED
- 当前场景：NOT STARTED
- PC 当前已知信息：无（尚未开始）
- 凯瑟琳私有知识：仅角色卡背景中明确确立的知识；游戏内知识从实际经历开始。
- NPC / 环境状态：未初始化
- pending effects / delayed events：无（尚未开始）
- revision: 0
- last_event_id: null

## Prep QA｜非剧透状态

- 已核对官方 CAS-1 在线文本全部主要章节及地点键。
- 已对照 Cairn 2e Core Rules、Procedures、Warden Combat 和 Dungeon Exploration。
- 已完成桌面逻辑回归，重点覆盖独立事件时钟、模组专用旅行触发、夜间旅行、地下事件、伤害结算和角色知识隔离。
- 一项模组 NPC 数值在官方在线文本中缺失；主持侧补值会标为 GM_INFERENCE，不作为官方规则。
- 当前证据属于 GM 自审与合成逻辑检查；未完成独立盲测或真实玩家回合验证。
- 未读取、推算或假设任何角色卡数据。

## 运行约束

- 不因现实时间间隔推进游戏时间。
- 每次重要状态变化时更新 Runtime State 与 Session Log；纯叙事且无状态变化的互动不必写入。
- 用户与凯瑟琳的资源变化均按 Cairn 2e 玩家角色规则分别结算；凯瑟琳不得漏记。
- GM-only 信息不得泄露给玩家，也不得流入凯瑟琳的角色知识。
- 用户尚未说“开始”，不得进入游戏场景。
