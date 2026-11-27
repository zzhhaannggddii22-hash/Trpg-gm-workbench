# Source & Rule Crosscheck｜Blame It on the Trains

> GM-only。此文件是验证登记与证据索引，不替代模组原文、中文 v22 或 Campaign Binding。状态只反映已取得的证据，不把“曾阅读”升级为独立核验。

## 1. Source register

| Source ID | Authority | Exact locator / version | Evidence state |
|---|---|---|---|
| SRC-MODULE-VAULT | *The Vault: Missions for Triangle Agency* | Blame It on the Trains；source PDF pp.93–101；printed pp.180–197 | 官方来源及页码已登记；英文原版逐页复核 NOT DONE |
| SRC-VAULT-ZH | `the_vault_zh.docx` | Library source; chapter begins at source PDF p.93 / printed p.180; file pagination pp.191–208 | 中文精翻章节第 191–208 页已分页回读；不等于英文原版独立校勘 |
| SRC-TA-V22-PDF | 用户指定《三角机构》中文 v22 PDF | Library file `triangle_agency_zh.pdf`；当前可读取版本；规则定位以印刷页码为准 | 已从 PDF 检索到相关页面摘录；完整规则矩阵仍需逐项核对 |
| SRC-TA-V22-GH | 用户指定公开规则仓库 | `p33333333333333l/triangle-agency-ai-zh`；Commit `7f6d52f40bbd3ff1a6c383ba2431c9aecda283b1`；Markdown blob SHA `5aa02d55b17cb88e2f477066d10db629f2e90ab6` | 固定版本完整 Markdown 已成功读取；相关规则条文已定位；剩余项目按矩阵逐项核验 |
| SRC-ZAREK-BINDING | Zarek Campaign System Binding | `Campaigns/Zarek/SYSTEM_BINDING.md` at campaign commit | 已读取 |
| SRC-ZAREK-RULINGS | Zarek Campaign approved rulings | `Campaigns/Zarek/RULE_ADJUDICATIONS.md` at campaign commit; Q01–Q05 | 已读取；仅限 Zarek Campaign |

## 2. Source limitations and conflict policy

- 中文精翻中 Jahnavi 姓名拼写出现 Reddy / Reddi 差异；Name Index 保留别名，正式英文拼写仍待英文原版终核。
- 中文精翻中的表格、特殊效果和术语需按其页面图像/版面复核；文本抽取不完整时，以可见页面图像为准，不从文本层被遮挡内容补全。
- Sub-Reality 暂译“子现实”；Loose End 暂译“松散端”；保留英文锚点。
- 英文原版逐页比对尚未完成。任何中文翻译准确性结论只能标为“中文精翻内部一致性”，不能写成“官方原文准确”。
- 来源缺失、文本抽取失败或访问受限时，记录具体缺少的证据；不切换版本，不用模型记忆补齐。

## 3. Prep Rule Validation matrix (mandatory before first Preflight)

This phase validates what the GM must know to run the module. It is not Preflight and is not the optional independent Prep QA.

| Rule area | Required validation | Current evidence / authority | Status |
|---|---|---|---|
| System binding | system_id, exact ruleset version and Campaign scope | SYSTEM_BINDING.md | VERIFIED |
| Campaign rulings | Confirm Q01–Q05 scope and approval; do not generalize them | RULE_ADJUDICATIONS.md | VERIFIED AS CAMPAIGN BINDING |
| QA | Nine Qualities, QA spend/adjustment, quality-specific pool and stated exceptions | v22 Markdown printed pp.34–35; Campaign's quality-to-check constraint; Q03 insurance exception | PARTIAL：通用 QA 调整条文已核；本桌对应 Quality 的使用约束需与既有 Campaign 规则记录一致；Q03 伤害保障明确允许任意 Quality QA |
| Burnout | Trigger, remove one 3 per Burnout, +1 Chaos per Burnout, stable-three exception and Q04 sequence | v22 Markdown printed pp.35–37; Campaign ruling Q04 | VERIFIED：通用 Burnout 与稳定性文本已核；执行顺序按 Zarek Q04（先 Burnout 后 QA） |
| Chaos | Initial pool, +1 per die without a 3, public reporting, module effects and close/reset | v22 Markdown printed pp.33, 156; module source; Q01/Q02 | PARTIAL：生成规则与域界规则已核；本模组初始池/结团处理仍须按模组与 Campaign 依据确认 |
| Harm / Stability / Domain | Harm application, death threshold, anomaly Stability/Threat, Domain costs and benefits | v22 core rules + module source + Q01/Q02/Q03 | OPEN |
| Ask the Agency | 6d4, Causality Chain, Quality selection, effect scope and failure | v22 printed pp.40–43 | PARTIAL |
| Module-specific abilities | Every referenced ability's trigger, Quality, success/failure and extra-3 effects | Exact v22 ability entries | OPEN |
| Sub-Reality change table | Full d44 table, repeat-entry procedure and application order | Chinese Vault translation file pp.200–202; source PDF p.97 | VERIFIED IN CHINESE SOURCE：完整 d44 表及重复进入叠加规则已分页回读 |
| Chaos Effects table | Full station effects table, trigger thresholds and application | Chinese Vault translation file pp.196, 203; source PDF pp.95, 98 | VERIFIED IN CHINESE SOURCE：车站表与 Jahnavi 特殊效果均已分页回读 |
| Jahnavi rescue special effect | Exact trigger and Chaos 4 effect | Chinese Vault translation file p.203; source PDF p.98 | VERIFIED IN CHINESE SOURCE：触发与效果文本已回读 |
| Ripple Gun | Charge, target, line of sight, effect and recharge timing | v22 printed p.21 | PARTIAL |
| Normal Briefcase | Eligible target state, focus/condition and capture resolution | v22 printed pp.21–22 | PARTIAL |
| Commendations / Demerits | Mission report, optional goals, authorized behaviors and award/penalty timing | v22 performance/report rules + module source | OPEN |
| Mission MVP / Probation / Participant | Eligibility, award order and mark/benefit effects | v22 printed pp.148–149 and Work/Life Balance sheet | PARTIAL |
| Loose Ends | Regional baseline, additions, weather effects and reporting | v22 regional rules + Campaign records | OPEN |
| Time | Distinguish system rules from Campaign Q05 award timing and reverse-linked field | RULE_ADJUDICATIONS.md Q05 | VERIFIED AS CAMPAIGN RULING ONLY |
| Equipment handoff | Holder, charge, use, return/restoration basis for each key item | Character card + prior Module Ledger + item rules | OPEN |

A row becomes VERIFIED only after the cited authority has been opened and the relevant rule text checked against the actual module use. A page number or a summary alone is not a pass.

## 4. Lifecycle and gate states

| Dimension | Current state | Meaning |
|---|---|---|
| Artifact delivery | DELIVERED | Files exist in the fixed repository version and are read back |
| Prep design review | REVIEWED | Structure and content reviewed; not a rule-validation pass |
| Source validation | BLOCKED | English source crosscheck incomplete; Chinese Vault source pages 191–208 read |
| Prep Rule Validation | BLOCKED | Core mechanical rows remain OPEN/PARTIAL |
| Single-player feasibility | NOT TESTED | No complete key-path cost/availability proof |
| Optional independent Prep QA | NOT RUN | Not a mandatory substitute for the above |
| Preflight | NOT STARTED / BLOCKED | Per-Session state recovery only, after Prep Rule Validation |
| Runtime | NOT STARTED | No actual play events |
| Player start authorization | WAITING | Only explicit user “开始” authorizes start |

## 5. Review and test evidence

### Review 1 — Static preparation review
- Result: REVIEWED WITH OPEN ITEMS.
- Scope: module structure, source mapping, spatial facts, named NPC/subject records, single-player adaptation principles and information boundaries.
- Not covered: full official English source collation, all v22 rule rows, complete end-to-end single-player path tests.

### Review 2 — targeted internal review
- Result: REVIEWED WITH OPEN ITEMS.
- Scope: selected spatial relations, NPC knowledge boundaries, authority references, resource ownership and player-facing separation.
- Not covered: full player-path simulation, independent blind review, complete rule-by-rule verification.

### Independent audit findings (input, not authority)
The 2026-11-27 independent report is treated as a defect lead list. Each item must be independently rechecked against the current branch before closure. Its own severity-count inconsistency is recorded in the remediation log; do not copy its aggregate counts.

## 6. Test execution ledger

| Test ID | Test | Execution type | Status | Result |
|---|---|---|---|---|
| SRC-01 | Confirm Chinese Vault source and chapter pagination | Source inspection | DONE | Library source and chapter location confirmed |
| SRC-02 | Compare English official module source page by page | Source inspection | NOT RUN | English original not yet independently read |
| RULE-01 | Verify v22 QA / Burnout and Q04 boundary | Rule inspection | PARTIAL | Campaign ruling read; full rule source matrix incomplete |
| RULE-02 | Verify Chaos initial/generation/close rules | Rule inspection | NOT RUN | OPEN |
| RULE-03 | Verify Harm / Domain / Stability resolution | Rule inspection | NOT RUN | OPEN |
| RULE-04 | Verify ability-specific triggers and outcomes | Rule inspection | NOT RUN | OPEN |
| SOLO-01 | Prove core path action/resource feasibility for one PC | Desk simulation | NOT RUN | OPEN |
| SOLO-02 | Remove one information source / NPC and test alternatives | Desk simulation | NOT RUN | OPEN |
| RT-01 | Cold-start from repository only | Recovery simulation | PARTIAL | Required file set now identified; full startup blocked by validation |
| RT-02 | Resume from checkpoint without replay or duplicate application | Synthetic state test | NOT RUN | Schema remediation landed; execution pending |
| RES-01 | Duplicate Event ID / Idempotency Key | Synthetic ledger test | NOT RUN | Schema remediation landed; execution pending |
| PFG-01 | Check mandatory Player-Facing Gate loading and output filtering | Static / synthetic | PARTIAL | Gate content passes static inspection; dynamic test pending |

## 7. Final status

- Artifact：DELIVERED.
- Prep design：REVIEWED.
- Source validation：BLOCKED.
- Prep Rule Validation：BLOCKED.
- Single-player feasibility：NOT TESTED.
- Optional independent Prep QA：NOT RUN.
- Preflight：NOT STARTED / BLOCKED.
- Runtime：NOT STARTED.
- User start authorization：WAITING.
- Any test not executed remains NOT RUN; no result is inferred from file existence or an earlier self-review.
