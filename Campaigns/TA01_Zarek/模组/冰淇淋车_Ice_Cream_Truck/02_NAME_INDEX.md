# 名称索引｜Ice Cream Truck

> 本文件是本模组唯一名称映射表。规范 ID 是身份主键；中文名、英文原名、简称和别名都必须指向同一个 ID。修改名称时只更新本表，不新建重复人物/地点。
> 玩家可见称呼首次出现使用“中文名（English Original）”；之后可按语境使用中文简称。GM 内部检索中英文名均返回同一 ID。

## 1. 地点

| 规范 ID | 中文显示名 | 英文原名 | 可检索别名 | 来源/备注 |
|---|---|---|---|---|
| LOC-TERNION-CITY | 特尼昂市（Ternion City） | Ternion City | Ternion City；特尼昂市；城市 | 扎雷克当前人物卡已使用的城市名 |
| LOC-33-ICICLE-DR | 冰柱路33号（33 Icicle Drive） | 33 Icicle Drive | 33 Icicle Drive；Icicle Drive；冰柱路33号；冰柱路 | 模组示例任务明确地址 |
| LOC-POOL-PARTY | 泳池派对现场（Pool Party） | Pool Party | pool party；泳池派对；派对现场 | 位于冰柱路33号；非独立正式地名 |
| LOC-TRUCK-INTERIOR | 冰淇淋车内部（Inside the Ice Cream Truck） | Inside the Ice Cream Truck | truck interior；车内；冰淇淋车内部；领域 | 模组明确的 Domain；不可与车辆外部混为一处 |

## 2. NPC

> 核心规则书示例任务没有为现场普通人物提供固定专名。保持角色称谓，不将社区实况中的即兴姓名移植进本桌。

| 规范 ID | 中文显示名 | 英文原名/角色称谓 | 可检索别名 | 来源/备注 |
|---|---|---|---|---|
| NPC-PARTY-HOST | 派对主人（Party Host） | Party Host | host；主人；派对主人 | 原文未给专名；其具体身份按现场事实呈现 |
| NPC-PARTY-GUEST | 派对来宾（Party Guest） | Party Guest | guests；来宾；参加者 | 群体角色，不预设个人姓名 |
| NPC-ICECREAM-CUSTOMER | 冰淇淋顾客（Ice-Cream Customer） | Ice-Cream Customer | customer；顾客；排队者 | 群体角色 |
| NPC-TRUCK-OPERATOR | 冰淇淋车经营者／Mr. Scoop | Mr. Scoop（本桌使用称呼；原文角色称谓为 Ice-Cream-Truck Operator） | operator；经营者；车主；冰淇淋车那边的人；Mr. Scoop；Mr Scoop；Scoop | 核心示例未提供固定专名。Session Log 与玩家便笺使用 Mr. Scoop 称呼该人物；这是本桌 CANON，姓名最初由谁提出的记录不足，不属于模组原文。其身份与异常本体的关系仍按已确认桌面事实处理，不额外推定。 |
| NPC-POTENTIAL-WITNESS | 潜在目击者（Potential Witness） | Potential Witness | witness；目击者；旁观者 | 只有实际目击异常活动的人才归入；按具体身份另建记录 |

## 3. 组织与物品

| 规范 ID | 中文显示名 | 英文原名 | 可检索别名 | 备注 |
|---|---|---|---|---|
| ORG-TRIANGLE-AGENCY | 三角机构（Triangle Agency） | Triangle Agency | Agency；机构；三角机构 | 世界观组织 |
| ITEM-RIPPLE-GUN | 涟漪枪（Ripple Gun） | Ripple Gun | Ripple Gun；涟漪枪 | 扎雷克标准任务装备；按中文 v22 核验弹药与作用条件 |
| MOD-ICE-CREAM-TRUCK | 冰淇淋车（Ice Cream Truck） | Ice Cream Truck | Ice Cream Truck；冰淇淋车；本次示例任务 | 模组标题，不是 NPC 名称 |

## 4. 明确排除的外部实况姓名

以下姓名出现在其他桌的公开 Actual Play 或讨论中，不属于核心规则书示例任务的既定 NPC，除非玩家未来明确要求将某个改编版本引入本桌，否则不得使用：
- Tony Dakota（托尼·达科塔）
- Donnie / Donifer（唐尼／唐尼弗）
- Jillian Pink（吉莉安·平克）
- Tommy、Jared Honeydew 等其他实况临时角色

## 5. 索引操作规则

1. 搜索任意中文名、英文原名、简称或别名，先解析到规范 ID，再读取该 ID 的唯一记录。
2. 同一 NPC/地点不得因语言变化、拼写变化、简称或称谓变化而重复建档。
3. 如果原文没有专名，保留“角色称谓（English Role Label）”；不要凭空造一个英文姓名。
4. 如游戏中确实需要为无名 NPC 命名，先在 GM-only 名称索引中建立唯一 ID，再记录中文名、英文原名、首次出现时间和命名依据；首次向玩家呈现时使用“中文名（English Original）”。
5. 新地点同理。街道、地址、建筑、房间、异常领域分别建 ID；不要把同一地点的口语称呼当成新地点。
6. 玩家便笺只记录玩家已知且有意义的名称；本索引的 GM-only 身份备注不得泄露。
