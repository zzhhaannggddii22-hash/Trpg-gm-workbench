# Campaign Naming Convention｜战役目录命名规范

本规范适用于整个 GM Workbench 的所有规则系统、所有 Campaign。它是跨系统通用项目规则，不属于任何单一系统。

## 目录名格式

`<系统简称><该系统战役序号两位数>_<角色名>`

示例：
- `TA01_Zarek`：Triangle Agency（`triangle_agency`）下的第 1 个战役，以角色 Zarek 命名。
- Cairn（`cairn`）的第 1 个战役应使用登记给 Cairn 的系统简称加 `01`，再接角色名。

## 系统简称登记

系统简称必须唯一、稳定，并在 `Systems/README.md` 的系统登记表中登记；不得在创建战役时临时发明或与其他系统重复。

| 系统 | system_id | 目录简称 |
|---|---|---|
| Triangle Agency / 三角机构 | `triangle_agency` | `TA` |
| Cairn / 石冢 | `cairn` | `CA` |

新增系统时，先确定并登记简称，再创建该系统下的 Campaign。

## 序号规则

1. 每个规则系统独立编号，从 `01` 开始递增；不同系统可分别拥有 `01`。
2. 序号按该系统已建立的 Campaign 编号分配，不因战役结团、归档、暂停或角色死亡而回收。
3. 新建前检查 `Campaigns/README.md` 与目录树，选用该系统尚未使用的最小可用递增序号；不得仅根据当前活跃战役数量编号。
4. 序号固定为两位数；达到 100 个战役后按自然位数扩展，不截断或重复。

## 角色名规则

- 下划线后的名称使用该 Campaign 的主要玩家角色名，保持简洁、稳定，建议使用人物卡中的规范英文名或固定罗马字。
- 角色改名不自动重命名既有 Campaign；只有玩家明确要求迁移目录时才修改。
- 同一角色在不同规则系统中的独立战役仍使用各自系统编号，绝不共用目录。

## 引用与迁移

- Campaign 根目录、`Campaigns/README.md`、`SYSTEM_BINDING.md`、跨目录链接、提示词和交接文件必须引用规范目录名。
- 目录改名时，必须同步更新所有索引、显式路径、文件链接和绑定字段；相对路径若在目录内部且目录结构不变，可保持原样，但必须确认其解析目标未变。
- 迁移应保留目录内所有文件、子目录、历史记录和 Git 历史语义；不得借目录整理重写战役 CANON。
- 新建 Campaign 时先按本规范确定目录名，再建立 `SYSTEM_BINDING.md`，然后建立人物档案与模组资料。

## 当前目录登记

- `TA01_Zarek` — Triangle Agency / `triangle_agency` 第 1 战役。
- `CA01_Zaf` — Cairn / `cairn` 第 1 战役（Twin Lakes；角色创建中；Cairn 系统接入仍为 candidate，不代表正式激活）。
