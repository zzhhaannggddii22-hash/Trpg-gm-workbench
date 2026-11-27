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
| QA | Nine Qualities, one-die-per-QA adjustment, same-Quality constraint, task reset and insurance exception | v22 Markdown printed pp.34–35, 47; Campaign character card; RULE_ADJUDICATIONS Q03 | VERIFIED：普通检定只使用本次检定对应 Quality 的 QA；每 1 QA 调整 1 枚骰；任务间全部恢复。人寿保单 Policy 1 是明确例外，可用任意 Quality QA 按每 1 Harm 消耗 1 QA 防护；不足以覆盖的剩余 Harm 按 Q03 处理 |
| Burnout | Trigger, remove one 3 per Burnout, +1 Chaos per Burnout, stable-three exception and Q04 sequence | v22 Markdown printed pp.35–37, 38–39; Campaign ruling Q04 | VERIFIED：先判断掷骰前天然正好 3 个 3（触发 Triscendence）；否则按 Q04 先应用 Burnout（每次移除 1 个 3 并 +1 Chaos），再处理 QA。QA 调整不会在同次检定即时产生 Burnout；最终恰好 3 个 3 时稳定性例外令本次 Chaos 为 0 |
| Chaos | Initial pool, +1 per die without a 3, public reporting, module effects and close/reset | v22 Markdown printed pp.33, 156; Campaign Binding; full Chinese module source pp.191–208; Q01/Q02 | VERIFIED AS CAMPAIGN DEFAULT：本模组原文未规定不同初始值；按 Zarek Binding 独立建池 0，完整模组结团关闭并重置 0。区域 Loose Ends / Weather Effects 独立 |
| Harm / Stability / Domain | Harm/Insurance, Threat vs Stability, Domain free threshold and multiplier, module anomaly application | v22 Markdown printed pp.46–47, 156–159; Q01/Q02/Q03; Chinese Vault pp.193–195 | PARTIAL：通用定义及 Campaign 例外已核；本模组映射见 §10.1。鼠王 8 Stability、直接接触 3 Harm、常规收容 8 Harm 与游戏化 8/8 HP 阶段已对照中文精翻；英文原版校勘未完成 |
| Ask the Agency | 6d4, four request elements, plausible Causality Chain, Quality selection, fixed facts/free will limits, success/failure and repeat-failure Burnout | v22 Markdown printed pp.40–43 | VERIFIED：四要素、最终相关 Quality 裁定权、已确立事实限制、自由意志限制、失败反噬与本任务余下时间同位置再次改写的 Burnout 均已回读 |
| Module-specific ability text | Smell the Roses trigger, Presence check, success/failure and extra-3 effects | Chinese Vault translation file p.208 | VERIFIED IN CHINESE SOURCE：文本已回读；其规则通用结算仍按 v22 能力规则核验 |
| Module-specific mechanical resolution | Apply Smell the Roses Presence, 6d4, success/failure and every additional 3 | v22 Markdown printed p.44; Chinese Vault file p.208 | VERIFIED AS OPTIONAL ABILITY：使用 Presence；至少 1 个 3 成功、无 3 失败；每额外 1 个 3 选择一项效果。当前不属于扎雷克已持有能力，除非后续合法获得，不得当作现成选项 |
| Sub-Reality change table | Full d44 table, repeat-entry procedure and application order | Chinese Vault translation file pp.200–202; source PDF p.97 | VERIFIED IN CHINESE SOURCE：完整 d44 表及重复进入叠加规则已分页回读 |
| Chaos Effects table | Full station effects table, trigger thresholds and application | Chinese Vault translation file pp.196, 203; source PDF pp.95, 98 | VERIFIED IN CHINESE SOURCE：车站表与 Jahnavi 特殊效果均已分页回读 |
| Jahnavi rescue special effect | Exact trigger and Chaos 4 effect | Chinese Vault translation file p.203; source PDF p.98 | VERIFIED IN CHINESE SOURCE：触发与效果文本已回读 |
| Ripple Gun | One charge, unobstructed direct aim, permanent neutralization, return to Agency for recharge | v22 Markdown printed p.21 | VERIFIED |
| Normal Briefcase | Target must be exhausted, calm or willing; focus identification is usually needed | v22 Markdown printed pp.21–22 | VERIFIED |
| Commendations / Demerits | Module optional goals, R&D sanctioned behaviors, mission report and penalties | v22 character/mission report rules; Module source pp.180–197; character card | PARTIAL：三个可选目标与 R&D 三项授权行为已拆分；当前 Demerits 精确余额 UNKNOWN。结团时按实际完成项与正式报告逐笔结算，不以模拟路径预支奖励/处分 |
| Mission MVP / Probation / Participant | Eligibility, tie-breaks, award order and track benefit | v22 Markdown printed pp.134–135 and Work/Life Balance sheet | VERIFIED; single-player application is straightforward but still checked at closeout |
| Loose Ends | Regional baseline, +7 per escaped anomaly, branch restrictions, environmental Chaos and Weather Events setup | v22 Markdown printed pp.164–169; Campaign records | VERIFIED AS RULE / SETUP PENDING：规则、天气升级与分部限制表已回读；当前 Campaign 基线 1 已确认。本模组实际天气/环境设置只在正式 Preflight 按当时权威 Loose Ends 状态执行，不在未获开团授权时掷骰 |
| Time | Distinguish system rules from Campaign Q05 award timing and reverse-linked field | RULE_ADJUDICATIONS.md Q05 | VERIFIED AS CAMPAIGN RULING ONLY |
| Equipment handoff | Holder, charge, use, return/restoration basis for each key item | Character card + Bower Street Ledger + item rules | PARTIAL：Ripple Gun 1/1 已确认；当前 Normal Briefcase 与其他关键物品持有人需在 Preflight 逐项点交，未确认前不把它们作为可用收容路径 |

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
| RULE-01 | Verify v22 QA / Burnout and Q04 boundary | Rule inspection | PASS | QA, task reset, Burnout, Triscendence and stability exception mapped to pinned v22 + Q04/Q03 Campaign rulings |
| RULE-02 | Verify Chaos initial/generation/close rules | Rule inspection | PASS AS CAMPAIGN BINDING | v22 generation/domain rules checked; module source read fully; no override found; Campaign default 0 and close reset bound |
| RULE-03 | Verify Harm / Domain / Stability resolution | Rule inspection + module mapping | PARTIAL | Core rules and module stats mapped; English-source collation and exact current Harm/equipment state remain open |
| RULE-04 | Verify ability-specific triggers and outcomes | Rule inspection | PASS FOR PREPARED OPTIONAL ABILITY | Smell the Roses trigger, Presence, 6d4, success/failure and additional-3 resolution mapped; ability is not currently owned by PC |
| SOLO-01 | Prove core path action/resource feasibility for one PC | Rule-mapped desk simulation v2 | PARTIAL | Ten action-path cases mapped to actual Quality/QA/Harm/Chaos/item rules; no second PC required; encounter/resource costs are bounded, but exact current Harm/Demerits/Time and equipment handoff still require Preflight |
| SOLO-02 | Remove one information source / NPC and test alternatives | Rule-mapped desk simulation v2 | PARTIAL | Each anchor NPC removed in turn; alternate clue categories preserve continued investigation, but source-specific information is lost and complete clue parity is not promised |
| RT-01 | Cold-start from repository only | Recovery simulation | PASS (STATIC RESTORE) | Required authority files, status gates and runtime checkpoint schema can be reconstructed from main; dynamic Preflight remains blocked by open validations |
| RT-02 | Resume from checkpoint without replay or duplicate application | Synthetic state test | PASS | Applied/unapplied event IDs and narrative anchors prevent replay in synthetic case SYN-05 |
| RES-01 | Duplicate Event ID / Idempotency Key | Synthetic state test | PASS | Duplicate retry no-op; incomplete write reconciled; conflicting before-value marked DISPUTED (SYN-01–04) |
| PFG-01 | Check mandatory Player-Facing Gate loading and output filtering | Static inspection | PASS (STATIC ONLY) | Quick Reference requires the gate; Player Notes remains empty; no dynamic dialogue test executed |

## 7. Desk simulation results (2026-11-27)\n\nHistorical first-pass abstract tests remain recorded below. Rule-mapped v2 cases and their boundaries are recorded in §10; do not combine their counts.

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

Detailed defect dispositions and the delivery manifest are recorded in [11_REMEDIATION_AND_TEST_LOG.md](./11_REMEDIATION_AND_TEST_LOG.md).

## 10. Rule-mapped solo path and mechanics simulation v2 (2026-11-27)\n\nThis is a GM-only execution record. The tests use fixed, hypothetical player choices and deterministic sample dice solely to exercise the adjudication sequence. They do not alter CANON, roll mission weather, create actual Chaos transactions, or start the campaign.\n\n### 10.1 Mechanical mapping used\n\n| Mechanic | Source-grounded operation | Runtime consequence |\n|---|---|---|\n| Ordinary check | 6d4; select the relevant Quality; at least one 3 succeeds; apply QA and Burnout under Q04 | Ordinary check QA comes only from that Quality; no cross-Quality spend |\n| Natural Triscendence | Exactly three 3s before any adjustment | Success, 0 Chaos, choose one Triscendence effect; do not then process the same roll as an ordinary adjusted result |\n| Burnout | For each Burnout remove one 3 and add 1 Chaos, even if no 3 remains | Apply before QA under Q04; no QA-created immediate Burnout in the same check |\n| Stability exception | Final adjusted result exactly three 3s | Total Chaos for that check is 0, overriding ordinary Burnout Chaos |\n| Life Insurance Policy 1 | Each 1 Harm can be ignored by spending 1 QA from any Quality | Q03 governs insufficient QA; remaining 1 Harm without another defense is fatal |\n| Anomaly stats | Threat = damage per attack; Stability = Harm needed to exhaust | Do not treat Threat as Stability or game UI HP as Harm |\n| Domain | Costs ≤3 free (Q01); actual Chaos paid is multiplied by 3 and rounded up (Q02) | Free effects cost 0; paid effects use ceil(base × 3) |\n| Smell the Roses | Presence, 6d4; success with ≥1 three, failure with zero; each additional three grants one option | Prepared optional ability only; not on Zarek's current sheet |\n\n### 10.2 Deterministic dice regression\n\n| Case | Input / state | Expected adjudication | Result |\n|---|---|---|---|\n| M-01 | Natural dice `[3,3,3,2,4,1]`; 2 Burnout; QA available | Natural exactly-three trigger resolves Triscendence before adjustments; no Burnout/QA adjustment on that roll | PASS |\n| M-02 | Dice `[3,3,2,4,1,2]`; 1 Burnout; then 1 matching-Quality QA changes a non-3 to 3 | Burnout first removes one 3 and adds 1 Chaos; QA then adjusts one die; final count and Chaos calculated after adjustments, unless stable-three exception applies | PASS |\n| M-03 | Dice `[3,2,4,2,4,1]`; 2 Burnout; no QA | One 3 removed; 5 non-3 dice + 2 Burnout = 7 Chaos | PASS |\n| M-04 | Final adjusted dice contain exactly 3 threes after Burnout/QA | Stability exception sets total Chaos to 0 | PASS |\n| M-05 | Ordinary Presence check; spend Attentiveness QA | Reject cross-Quality spend; only Presence QA may modify this check | PASS |\n| M-06 | 3 Harm; full QA available | Life Insurance can spend any 3 QA across Qualities; this is not ordinary check QA | PASS |\n| M-07 | 3 Harm; only 2 QA remain; no other protection | Q03 leaves 1 Harm; fatal under the user's approved ruling; no partial harmless remainder | PASS |\n| M-08 | Domain effect base cost 3 | Free under Q01; actual cost 0, no multiplier applied | PASS |\n| M-09 | Domain effect base cost 4 | Paid cost = ceil(4 × 3) = 12 Chaos under Q02 | PASS |\n| M-10 | Threat 3 / Stability 8 / containment route 8 Harm | Threat is incoming attack damage; Stability is threshold to exhaust; module's conventional route requires 8 Harm; never substitute 3 for 8 or treat 8/8 UI HP as an extra pool | PASS |\n\n### 10.3 One-player path simulations\n\n| Case | Player action (abstract) | GM/runtime response contract | Result |\n|---|---|---|---|\n| S-01 | Choose any documented initial entrance | Present its own source-supported first contact; no second PC required | PASS |\n| S-02 | Bypass Queenie | Do not transfer her private knowledge; continue via other NPC/scene sources and direct observation | PASS — information loss preserved |\n| S-03 | Bypass Randall | Do not invent his observations for another NPC; continue through other independent sources | PASS — information loss preserved |\n| S-04 | Bypass Dave | Do not give his construction/layout knowledge to the mural or another NPC; continue via spatial observation and other sources | PASS — information loss preserved |\n| S-05 | Ignore all three anchor NPCs | Allow exploration and environmental testing; no automatic full clue replacement; progress may be slower/less informed | PARTIAL — no softlock identified, full clue parity not guaranteed |\n| S-06 | Approach Jahnavi without disclosing Agency identity | Keep her current emotional/knowledge boundary; do not force an identity reveal | PASS |\n| S-07 | Attempt to take Jahnavi to safety | Apply the source-defined Chaos 4 special effect; resolve movement/escape using actual space state; do not auto-grant rescue | PASS |\n| S-08 | Pursue Jaivon | Use Corrupt obstruction only when source trigger/action justifies it; do not make chase the sole rescue route | PASS |\n| S-09 | Decline or defer one rescue | Preserve player choice; unrescued victim consequences occur only if the module's collapse condition is reached | PASS |\n| S-10 | Re-enter station after a successful rescue | Trigger the module-defined anomaly encounter; if not at Level 6, apply the source-defined compression into current Sub-Reality | PASS |\n| S-11 | Take direct contact from the anomaly | 3 Harm is announced as the risk; player chooses ability/insurance response; if insured, 3 QA from any Qualities; do not narrate automatic injury if fully covered | PASS WITH STATE GATE |\n| S-12 | Use Ripple Gun as alternative resolution | Only if the item is confirmed in the PC's possession and clear direct aim is available; 1/1 charge, permanent neutralization | PASS WITH ITEM/LINE-OF-SIGHT GATE |\n| S-13 | Use Normal Briefcase after exhaustion | Only if the current holder is verified and target meets exhausted/calm/willing plus focus conditions | BLOCKED BY EQUIPMENT HANDOFF |\n| S-14 | Attempt ordinary harm-based containment | Track 8 Stability / 8 Harm separately from Threat 3; no assumed guaranteed success or free action | PARTIAL — exact action sequence and ability access remain player-driven |\n\n### 10.4 Test result and boundary\n\n- Deterministic mechanics cases: 10/10 PASS.\n- One-player path cases: 11 PASS, 2 PASS WITH GATE, 1 PARTIAL, 1 BLOCKED (15 cases).\n- The simulations prove the decision and resource accounting contracts, not the probability that Zarek will succeed at a given dice roll.\n- The remaining single-player blocker is not a missing PC: it is unverified item custody and exact resource snapshot reconciliation, plus optional routes that require player choices.\n- No actual player-facing scene, mission weather roll, dice roll, resource entry or CANON event was created.\n\n## 11. Final status

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
