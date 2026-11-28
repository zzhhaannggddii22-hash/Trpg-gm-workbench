# Twin Lakes｜EBB Preflight 与恢复核验

> Campaign：CA01_Zaf
> 系统：Cairn 2e
> 恢复核验日期：2026-11-28
> 模组状态：PREPARED_NOT_STARTED
> Campaign 状态：NOT_STARTED
> 系统状态：candidate；activation pending

## 1. 恢复范围
本次将 Twin Lakes 的 Campaign 入口、人物卡、跨战役只读快照及 EBB 模组资料恢复到 main。

- Zaf、茱比洛、凯瑟琳三份 Cairn 人物卡及两份跨战役只读快照，从历史提交 482578b121721075f7aa452ab593bc3eb659b002 的原始 Git Blob 恢复。
- EBB 原备团目录未能在当前 main 或可读取的历史树中找回；本版依据用户提供的官方 Pages PDF 与已锁定桌面裁定重建，明确标记为恢复重建，不冒称找回旧文件原文。

## 2. 权威来源与资料顺序
1. 用户提供的 Xeno & Kraft 官方 EBB Pages PDF。
2. 本 Campaign 已锁定的桌面裁定：Path 7 = 1 小时；恰好 8 小时抵达仍成功。
3. 本 Campaign 人物卡与 SYSTEM_BINDING。
4. EBB 的 MANIFEST、GM_ONLY_PREP、REFERENCE_INDEX 与 QA_REPORT。
5. Cairn 2e 本地规则运行手册；模组专属机制以模组原文为准。

如发现冲突，保留来源原文、标注冲突，并执行已由玩家确认的桌面裁定；不得静默改写来源。

## 3. 人物与队伍状态
- Zaf：玩家控制 PC；人物卡及锁定随机结果恢复，未重掷。
- 茱比洛：GM 控制的正式 L3 NPC 队员；人物卡恢复，PC 等价资源机制仅为本战役配置。
- 凯瑟琳：人物卡与历史状态保留；本次冒险休止。
- Lorenz：模组护送对象，不是第三名 PC 或自动 hireling。

## 4. EBB 核验
- 原始来源：Escape to Blackboot Bog: A Moonlit Pathcrawl for Cairn，Xeno & Kraft。
- PDF 第 4 页地图可用作玩家地图；第 5 页包含图例和路线摘要。
- Path 7 的路线摘要列为 1 小时，而第 8 页河流场景文字列为 2 小时；本桌采用 1 小时。
- 八小时截止边界包含 8:00；超过 8 小时仍未抵达才算失败。
- 路线遭遇、区域遭遇、Bog 线索修正、特殊 NPC 能力、特殊物品、信件分支及 Dawn 失败程序已整理到 GM-only 备团和快速索引。
- Gertrud 信件分支保留原文条件“If she does not read the letter”；不简化为“没有收到信”。

## 5. 未启动状态
- 没有开始游戏，没有推进游戏内时间或选择路线。
- 没有投掷随机遭遇、反应或其他骰子。
- 没有扣除、恢复或改变任何人物资源。
- 没有建立 Runtime State / Session Log。
- Cairn 仍为 candidate，activation pending。

**结论：** Campaign 资料与 EBB 备团文档已恢复/重建到 main；模组为 PREPARED_NOT_STARTED。必须等待用户明确说“开始”才进入正式游戏。
