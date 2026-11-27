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
| Chaos | Initial pool, +1 per die without a 3, public reporting, module effects and close/reset | v22 Markdown printed pp.33, 156; Campaign Binding; module source; Q01/Q02 | PARTIAL：生成规则、公开记录和域界规则已核；Campaign 默认初始值 0 已绑定，仍需确认本模组是否有覆盖特例及结团关闭处理 |
| Harm / Stability / Domain | Harm application, death threshold, anomaly Stability/Threat, Domain costs and benefits | v22 core rules + module source + Q01/Q02/Q03 | OPEN |
| Ask the Agency | 6d4, Causality Chain, Quality selection, effect scope and failure | v22 printed pp.40–43 | PARTIAL |
| Module-specific ability text | Smell the Roses trigger, Presence check, success/failure and extra-3 effects | Chinese Vault translation file p.208 | VERIFIED IN CHINESE SOURCE：文本已回读；其规则通用结算仍按 v22 能力规则核验 |
| Module-specific mechanical resolution | Apply the ability's Quality, dice, QA/Burnout and extra-3 rules in play | v22 ability-resolution sections + Campaign constraints | OPEN |
| Sub-Reality change table | Full d44 table, repeat-entry procedure and application order | Chinese Vault translation file pp.200–202; source PDF p.97 | VERIFIED IN CHINESE SOURCE：完整 d44 表及重复进入叠加规则已分页回读 |
| Chaos Effects table | Full station effects table, trigger thresholds and application | Chinese Vault translation file pp.196, 203; source PDF pp.95, 98 | VERIFIED IN CHINESE SOURCE：车站表与 Jahnavi 特殊效果均已分页回读 |
| Jahnavi rescue special effect | Exact trigger and Chaos 4 effect | Chinese Vault translation file p.203; source PDF p.98 | VERIFIED IN CHINESE SOURCE：触发与效果文本已回读 |
| Ripple Gun | One charge, unobstructed direct aim, permanent neutralization, return to Agency for recharge | v22 Markdown printed p.21 | VERIFIED |
| Normal Briefcase | Target must be exhausted, calm or willing; focus identification is usually needed | v22 Markdown printed pp.21–22 | VERIFIED |
| Commendations / Demerits | Mission report, optional goals, authorized behaviors and award/penalty timing | v22 performance/report rules + module source | PARTIAL：规则框架已定位；模组结算和历史余额仍须逐项核 |
| Mission MVP / Probation / Participant | Eligibility, tie-breaks, award order and track benefit | v22 Markdown printed pp.134–135 and Work/Life Balance sheet | VERIFIED; single-player application is straightforward but still checked at closeout |
| Loose Ends | Regional baseline, +7 per escaped anomaly, weather-event roll/escalation and reporting | v22 Markdown printed pp.164–169; Campaign records | PARTIAL：通用规则与当前基线 1 已核；本模组开始前的天气掷骰/历史结果回读待执行 |
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
The 2026-11-27 independent report is treated as a defect lead list, not as authority. Each item is independently rechecked against the current branch and source evidence before closure. Its severity-count inconsistency is recorded in the remediation log; do not copy its aggregate counts.

## 6. Test execution ledger

| Test ID | Test | Execution type | Status | Result |
|---|---|---|---|---|
| SRC-01 | Confirm Chinese Vault source and chapter pagination | Source inspection | DONE | Library source and chapter location confirmed |
| SRC-02 | Compare English official module source page by page | Source inspection | NOT RUN | English original not yet independently read |
| RULE-01 | Verify v22 QA / Burnout and Q04 boundary | Rule inspection | PARTIAL | Campaign ruling read; full rule source matrix incomplete |
| RULE-02 | Verify Chaos initial/generation/close rules | Rule inspection | PARTIAL | Generation and Domain rules verified; initial default 0 bound; module override/close treatment still open |
| RULE-03 | Verify Harm / Domain / Stability resolution | Rule inspection | PARTIAL | Core Harm, insurance and Threat/Stability rules read; module-specific action mapping and current Harm state remain open |
| RULE-04 | Verify ability-specific triggers and outcomes | Rule inspection | PARTIAL | Module ability text read; general ability-resolution rules and each in-play interaction still need full mapping |
| SOLO-01 | Prove core path action/resource feasibility for one PC | Desk simulation | PARTIAL | Key path principles checked; action/resource costs and rescue sequencing remain OPEN |
| SOLO-02 | Remove one information source / NPC and test alternatives | Desk simulation | PARTIAL | Alternative source categories exist; source-dependency graph is not yet proven end-to-end |
| RT-01 | Cold-start from repository only | Recovery simulation | PARTIAL | Mandatory load order and authority map restored; full startup remains blocked by Prep Rule Validation |
| RT-02 | Resume from checkpoint without replay or duplicate application | Synthetic state test | PASS | Applied/unapplied event IDs and narrative anchors prevent replay in synthetic case SYN-05 |
| RES-01 | Duplicate Event ID / Idempotency Key | Synthetic state test | PASS | Duplicate retry no-op; incomplete write reconciled; conflicting before-value marked DISPUTED (SYN-01–04) |
| PFG-01 | Check mandatory Player-Facing Gate loading and output filtering | Static inspection | PASS (STATIC ONLY) | Quick Reference requires the gate; Player Notes remains empty; no dynamic dialogue test executed |

## 7. Desk simulation results (2026-11-27)

| Test ID | Player action class | Result | Reason / boundary |
|---|---|---|---|
| DSK-01 | Choose among the documented entry routes | PASS | Each route has a distinct first-contact/source path; one PC does not require a second PC to enter |
| DSK-02 | Bypass one anchor NPC | PARTIAL | Other clue-source categories remain; the skipped source's unique information is not automatically replaced |
| DSK-03 | Bypass a different anchor NPC | PARTIAL | Alternative observation/NPC sources exist; exact clue parity and dependency costs remain unproven |
| DSK-04 | Act on an incorrect hypothesis | PASS | World facts remain independent; GM procedure distinguishes player inference from confirmed fact |
| DSK-05 | Use a non-prepared ability/action | BLOCKED | Ability-specific resolution and related v22 mechanics remain OPEN; no guessed ruling allowed |
| DSK-06 | Choose rescue order or decline one objective | PARTIAL | Player choice is preserved; full action/resource/time cost and downstream feasibility remain unproven |
| DSK-07 | Re-enter an already visited Sub-Reality | PASS | Source requires one d44 roll per prior entry and cumulative application; Runtime now stores entry count/history |
| DSK-08 | Complete a rescue, then re-enter the station | PASS | Source trigger is explicit; event ID and checkpoint contract prevent duplicate trigger application |
| DSK-09 | Proceed without NPC assistance | PARTIAL | One PC remains the only PC; information alternatives exist, but every core route's solo cost is not proven |
| DSK-10 | Attempt a resource-intensive action with unknown current balances | BLOCKED | Unknown Harm/QA/Chaos/Time values stop dependent mechanics; unrelated narration remains available |

Desk simulation: 10 scenarios executed; 4 PASS, 4 PARTIAL, 2 BLOCKED. This is not a full round-by-round GM/player simulation.

## 8. Synthetic state tests

| Test ID | Test | Result |
|---|---|---|
| SYN-01 | Apply a resource transaction once | PASS |
| SYN-02 | Retry an already VERIFIED idempotency key | PASS — no second application |
| SYN-03 | Recover an INCOMPLETE entry where target balance already equals expected after-value | PASS — mark VERIFIED without reapplying |
| SYN-04 | Detect a conflicting before-value | PASS — mark DISPUTED, preserve actual value |
| SYN-05 | Resume from checkpoint with applied and unapplied events | PASS — do not replay applied event |
| SYN-06 | Re-enter Sub-Reality with cumulative d44 results | PASS — preserve prior rolls and append the required additional rolls |
| SYN-07 | Prevent NPC knowledge without source event | PASS — reject unsourced knowledge |

Synthetic tests: 7/7 PASS. These are executed state-model tests in the current work session, not an automated test suite committed to CI.

## 9. Final status

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
