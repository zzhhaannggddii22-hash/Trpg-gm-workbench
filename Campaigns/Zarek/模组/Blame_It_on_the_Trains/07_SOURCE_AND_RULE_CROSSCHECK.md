# Source & Rule Crosscheck｜Blame It on the Trains

> GM-only。记录来源核对与测试证据；本文件不是规则书替代品，也不是“已全部核验”的声明。

## 1. 来源定位

| Source ID | 来源 | 定位 | 核验状态 |
|---|---|---|---|
| SRC-MODULE-VAULT | *The Vault: Missions for Triangle Agency* | Blame It on the Trains；源 PDF 93–101；印刷页 180–197 | 中文精翻已读取 |
| SRC-VAULT-ZH | `the_vault_zh.docx` | Library file；文件第 191–208 页；源 PDF 93–101 | 完整章节分页回读；表格与遭遇页已核 |
| SRC-TA-V22 | 《三角机构》中文 v22 | 固定公开版本：`p33333333333333l/triangle-agency-ai-zh` Commit `7f6d52f40bbd3ff1a6c383ba2431c9aecda283b1`；`最终交付_v22/triangle_agency_zh.md`；Campaign Binding 与 Q01–Q05 桌裁清单 | 已读取相关基础条文与桌裁；逐项行级核验仍须 Preflight 完成 |

## 2. 来源差异与待核

- 中文精翻在 Jahnavi 姓名拼写处出现 Reddy / Reddi 差异；当前统一实体索引，保留别名，待英文原版终核。\n- 车站 Chaos Effects 表、d44 子现实变化表和 Jahnavi 营救特殊效果已从中文精翻分页阅读核实，并整理入 01 §15。
- Sub-Reality 暂译“子现实”；Loose End 暂译“松散端”；术语统一依 v22 与全书终审。
- 个别专名如 Urgency / Urgents 在中文母稿中有 [待核] 标记；本备团保留英文锚点，不推断其制度含义。
- 本轮未访问英文原始 PDF 文件进行逐页比对；引用中文精翻时明确此限制。

## 3. 规则交叉核验矩阵

| 领域 | 核验目标 | 状态 |
|---|---|---|
| 系统绑定 | Triangle Agency / 中文 v22 | BOUND |
| QA 与素质检定 | 九项 Quality、同 Quality QA 修改、任务间完全恢复 | PARTIAL VERIFIED：v22 印刷页 34–35；Preflight 再核能力专属例外 |
| Burnout | QA 归零含初始 0 QA、移除 3 并 +1 Chaos；本桌时序 Q04 | PARTIAL VERIFIED：v22 印刷页 35、40–43；Q04 绑定 |
| Harm / Domain | 人寿保单防护、异常 Stability/Threat、域界收益 | PARTIAL：人寿保单 Q03；异常 Stability/Threat 按次级异常条款；域界 Q01/Q02 |
| Chaos | 初始值、效果表、结算 | OPEN |
| 异常能力 | 模组相关能力检定和效果 | OPEN |
| Ripple Gun | 单发充能、回机构补充；直接瞄准且无遮挡；只中和目标异常 | SOURCE VERIFIED：v22 印刷页 21；开场装备仍须点交 |
| Normal Briefcase | 异常须精疲力竭、情绪平静或愿意收容；焦点识别通常为前提 | SOURCE VERIFIED：v22 印刷页 21–22；收容判定细节 Preflight 核对 |
| Commendation / Demerit | 模组可选目标、职能授权行为、MVP 奖励 | PARTIAL：模块奖励已整理；任务结束总额/资格按 v22 与人物卡核对 |
| Mission MVP | 最高嘉奖者；免费标记一格职能轨迹 | SOURCE VERIFIED：v22 印刷页 148–149；当前人物卡已记录 MVP 成长 |
| Loose Ends | 识别、报告与后果 | OPEN |
| Time | 完整模组结团 +1、可使用 Time 与剩余可用 Time 反向联动 | CAMPAIGN Q05 CONFIRMED（2026-11-27）；非通用 v22 规则 |

## 4. 内部审查记录

### Review 1 — 结构与来源复核
- 结果：PASS WITH OPEN ITEMS。
- 覆盖：模组来源、空间结构、首遇入口、主要 NPC、两名初始受害者、异常域界、单人桌适配、玩家信息权限。
- 缺口：规则行级交叉引用、英文原版逐页比对、独立盲审尚未完成。

### 修订
- 把所有未核规则项目显式标记 OPEN。
- 移除对角色当前资源状态的猜测，改由正式人物卡和 Resource Ledger 核验。
- 将玩家侧笔记设为空白，不从 GM Prep 自动派生。
- 将生命周期设为 READY WITH OPEN ITEMS，阻止未完成规则核验被误报为 READY。

### Review 2 — 定向复审
- 结果：PASS WITH OPEN ITEMS。
- 复核：空间层级关系、进入/离开逻辑、NPC 知识边界、单人行动经济、GM-only/玩家侧分离、资源来源。
- 未执行：完整玩家路径自动化模拟、独立模型盲审、规则行级全覆盖。
- 结论：可作为备团底稿；开团前必须完成 Preflight 的 OPEN 规则项，建议先执行独立 Prep QA。

## 5. 压力测试覆盖状态

| 测试路径 | 状态 | 备注 |
|---|---|---|
| 不同初始入口 | STATIC REVIEW | 已审查入口映射 |
| 跳过某个 NPC | NOT RUN | 需模拟检查信息可替代性 |
| 错误空间假设 | NOT RUN | 需模拟验证世界反馈 |
| 非预设能力 | NOT RUN | 需按具体能力测试 |
| 先营救后撤离 | STATIC REVIEW | 原文空间条件已整理 |
| 撤离后返回 | NOT RUN | 需验证触发与状态连续性 |
| 拒绝营救/优先撤离 | NOT RUN | 需检查收束分支 |
| 暴力/非暴力路径 | STATIC REVIEW | 仅整理模组结构，规则结算待核 |
| 关键 NPC 缺席 | NOT RUN | 需检查软锁 |
| 反复进入同一子现实 | STATIC REVIEW | 已记录重复进入骰流程 |

## 6. 最终状态

- Prep：READY WITH OPEN ITEMS。
- Independent Prep QA：NOT RUN。
- Preflight：NOT STARTED。
- Runtime：NOT STARTED。
- 任何未执行测试均不得在后续报告中称为通过。


## 7. 规则来源与桌裁边界

- 固定规则版本公开入口：`https://github.com/p33333333333333l/triangle-agency-ai-zh/tree/7f6d52f40bbd3ff1a6c383ba2431c9aecda283b1/最终交付_v22`。
- QA 与 Burnout：主规则 Markdown 对应 01_field_agent_manual/020–021；印刷页 34–35。QA 仅改动本次 Quality 的骰子；QA 任务间完全恢复。Burnout 包括该 Quality 初始没有 QA 的情形；每层移除一个 3 并增加 1 Chaos。
- Ask the Agency：主规则 Markdown 对应 01_field_agent_manual/024；印刷页 40–43。必须明确效果、可信 Causality Chain、相关 Quality 和 6d4；只改写尚未确立事实；GM 对 Quality 有最终决定权。
- Chaos：主规则印刷页 33、156；每枚未显示 3 的骰子通常产生 1 Chaos；普通池数量对玩家公开。域界免费门槛/三倍费用按 Zarek Campaign 已绑定 Q01/Q02。
- Normal Briefcase / Ripple Gun：主规则印刷页 21–22；异常需满足公文包收容状态要求；Ripple Gun 单发充能、回机构补充，直接瞄准无遮挡目标异常可永久中和。
- Time：当前 +1 触发和反向联动是 Zarek Campaign 的 Q05 桌裁，不得描述为通用 v22 规则。
- 本次未把系统记忆卡或测试卡当成高于完整规则原文的证据；它们只用于定位和提醒。
