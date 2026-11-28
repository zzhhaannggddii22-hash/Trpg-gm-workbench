# EBB｜恢复与备团 QA 报告

> Date: 2026-11-28
> Status: STATIC_PREP_QA_COMPLETE
> Result: 25/25 static checks PASS
> Not a live-play certification.

## 恢复来源
- Zaf、茱比洛、凯瑟琳人物卡及两份跨战役只读快照：从历史提交 482578b121721075f7aa452ab593bc3eb659b002 的原始 Git Blob 恢复。
- EBB 文件：旧目录未出现在当前 main 或可读取的历史树中；此版依据用户提供的官方 Pages PDF 与已锁定裁定重新整理。
- 本报告评价资料完整性、来源和跨文件一致性，不声称旧 EBB 文件被逐字找回。

## 静态检查
| # | 检查项 | 结果 |
|---:|---|---|
| 1 | Xeno & Kraft 作者归属 | PASS |
| 2 | 官方 itch.io 与作者来源页 | PASS |
| 3 | CC BY-SA 4.0 文本与 ©2025 美术分别说明 | PASS |
| 4 | 未将整本出版物复制进仓库 | PASS |
| 5 | PDF 第 4 页地图作为玩家地图 | PASS |
| 6 | PDF 第 5 页与第 8 页 Path 7 冲突 | PASS |
| 7 | Path 7 采用玩家裁定 1 小时 | PASS |
| 8 | 8 小时边界包含恰好 8:00 | PASS |
| 9 | 每小时旅行开始时按区域掷 d6 | PASS |
| 10 | 唯一性遭遇重掷 | PASS |
| 11 | Bog 线索每条 +1 | PASS |
| 12 | Bog 测绘图携带时 +2 | PASS |
| 13 | Shambling Mound 结果 3 的追逐例外 | PASS |
| 14 | Bernhildi STR 归零击败条件与再生 | PASS |
| 15 | Sieger 鞭 charges 与 recharge 代价 | PASS |
| 16 | Dryad / Befuddle / Acorn | PASS |
| 17 | Moon Druid / Silja / Cauldron | PASS |
| 18 | Lute / Werepig Charm | PASS |
| 19 | Fields 火灾、卫士与毒蛇 | PASS |
| 20 | Lake 鲸灵、Volline、月鱼 | PASS |
| 21 | Bog 毒气、藤蔓、Will-o-Wisp 与小屋线索 | PASS |
| 22 | Gertrud 分支精确保留“If she does not read the letter” | PASS |
| 23 | Dawn 失败结果与 Gertrud Spider | PASS |
| 24 | Zaf/Jubilo/Catherine 人物卡与队伍状态 | PASS |
| 25 | 未创建 Runtime/Session Log；未宣称已开始或激活 | PASS |

## 限制
- 未进行真实游戏或实战时序验证。
- 未验证平台宿主跨对话持久化。
- 未在模组摘录中完整呈现的法术书效果保持待查。
- 25/25 是本次文档静态一致性检查，不是 Cairn 系统激活、模组实战或 GM 独立盲测结论。
