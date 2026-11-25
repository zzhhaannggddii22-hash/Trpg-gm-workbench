# GM Failure Database｜记录索引

> 本索引只汇总已建立的 Failure 条目。Issue 是问题跟踪编号，PR 是修改记录编号；两者不可混用。条目状态以各 Failure 文件及其验证证据为准。

最后整理：2026-11-26（UTC+8）

## 当前记录

| Failure ID | 问题 | 关联 Issue | Failure 状态 | 当前判断 |
|---|---|---|---|---|
| [GMF-20261126-01](Records/GMF-20261126-01.md) | 规则检定结算遗漏 Chaos Pool | [#22](https://github.com/zzhhaannggddii22-hash/Trpg-gm-workbench/issues/22) | ANALYZED | 尚无修复与行为回归证据 |
| [GMF-20261126-02](Records/GMF-20261126-02.md) | 历史 NPC 与线索未能正确接续 | [#23](https://github.com/zzhhaannggddii22-hash/Trpg-gm-workbench/issues/23) | ANALYZED | 尚无对应行为回归证据 |
| [GMF-20261126-03](Records/GMF-20261126-03.md) | NPC 同行承诺在场景移动中丢失 | [#24](https://github.com/zzhhaannggddii22-hash/Trpg-gm-workbench/issues/24)、[#25](https://github.com/zzhhaannggddii22-hash/Trpg-gm-workbench/issues/25) | ANALYZED | 两个 Issue 指向同一 SESSION 01 失败事件，合并关联，不重复计数；尚无对应行为回归证据 |
| [GMF-20261126-04](Records/GMF-20261126-04.md) | 全局场景状态中的驾驶者与座位信息丢失 | [#26](https://github.com/zzhhaannggddii22-hash/Trpg-gm-workbench/issues/26) | ANALYZED | 尚无对应行为回归证据 |
| [GMF-20261126-05](Records/GMF-20261126-05.md) | NPC 引用了未获知的 GM-only 地点信息 | [#27](https://github.com/zzhhaannggddii22-hash/Trpg-gm-workbench/issues/27) | ANALYZED | P0 信息权限问题；尚无对应行为回归证据 |

## 盘点范围与编号说明

- 本次 GitHub Issue 搜索在当前仓库返回 #22–#27 六个 Issue，均为 OPEN；未返回 CLOSED Issue。
- #24 与 #25 的描述对应同一场景转换中的同一失败事件，因此在 Failure Database 中共用一条记录，并保留两个 Issue 链接。
- 此前被误当成历史 Issue 的 #1–#21 实际是 PR（修改记录），不纳入 Failure 计数。
- 当前索引覆盖已检索到的六个真实 Issue；不把 PR 标题或 PR 自审中的缺陷清单自动转换为正式 Failure。若之后发现独立历史事件，应按来源和证据补登记。
- 所有五条记录当前均为 ANALYZED。尚未因文档修订、PR 合并或合成测试而标记 FIXED_PENDING_VERIFICATION / CLOSED。需要对应失败行为的可复核回归证据后，才能推进状态。
