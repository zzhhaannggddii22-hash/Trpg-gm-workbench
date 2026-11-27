# Remediation & Test Log｜Blame It on the Trains

> GM-only. This log records the current remediation batch, evidence boundaries, tests actually executed and unresolved blockers. It contains no player-facing scenario information.

## 1. Delivery manifest

| Field | Value |
|---|---|
| Delivery ID | `BLAME-TRAIN-REMEDIATION-2026-11-27-R1` |
| Target repository | `zzhhaannggddii22-hash/Trpg-gm-workbench` |
| Target branch | `fix/blame-trains-independent-remediation-2026-11-27` |
| Audit target Commit | `99f41bd4dafd202c9d81430e4ca098356d8e3cc7` |
| Base Commit | `76be1f28babb95e27fcd3afd6d3ac63c2e4219cf` |
| Artifact Commit (code/readback snapshot before this manifest file) | `613460a72c560e26306b6a724b12d061ee5729ef` |
| Manifest status | DRAFT → readback pending |
| Writer / validator / delivery owner | Casey — SELF-REVIEW; not independent QA |
| External AI review | NOT USED in this remediation batch |
| Main branch mutation | NONE; all writes are on the remediation branch |

### Change set

- Module: `01_GM_PREP.md`, `03_RUNTIME_STATE.md`, `07_SOURCE_AND_RULE_CROSSCHECK.md`, `08_RUNTIME_QUICK_REFERENCE.md`, `09_RESOURCE_LEDGER.md`, `README.md`.
- Campaign: `SYSTEM_BINDING.md`, `人物档案/扎雷克_正式人物卡.md`, `模组/README.md`, `README.md`.
- Prior module reconciliation: `Bower_Street/04_SESSION_LOG.md`.
- Generic workflow: `GM_Training/09_MODULE_FOLDER_STANDARD.md`, `GM_Training/13_PREP_TO_RUNTIME_HANDOFF_STANDARD.md`.
- New artifact: this remediation and test log.

## 2. Source evidence

| Source | Evidence obtained | Boundary |
|---|---|---|
| Fixed Chinese v22 rule source | Pinned Commit `7f6d52f40bbd3ff1a6c383ba2431c9aecda283b1`; full Markdown blob SHA `5aa02d55b17cb88e2f477066d10db629f2e90ab6`; relevant sections opened and read | Core QA, Burnout, Harm, Life Insurance, Chaos, Domain, Stability/Threat, equipment, mission superlatives and Loose Ends rules were inspected; remaining module-specific mapping stays open |
| Chinese Vault translation | Library `the_vault_zh.docx`; Blame It on the Trains file pages 191–208 were paginated and read | This closes Chinese translation pagination only; it is not an independent English-original collation |
| Official English Vault PDF | Official publisher listing confirms the digital PDF/plain-text files are distributed as paid downloads | The English original was not available in the current Library/source set; no wording or table was reconstructed from memory |
| Campaign Binding / rulings | `SYSTEM_BINDING.md`, `RULE_ADJUDICATIONS.md`, Q01–Q05 | Campaign-specific rulings are not general v22 rules |

### Verified source details

- QA core adjustment, task-between restoration, Burnout effect, Triscendence/stability exception and Q04 sequence were checked against the pinned v22 text and Campaign Binding.
- Life Insurance Policy 1 explicitly allows any Quality's QA to ignore Harm; this is an exception to the Campaign's ordinary same-Quality QA constraint.
- Harm 1 is lethal to an ordinary person; Threat describes an anomaly's attack damage, while Stability is the damage required to exhaust it.
- Domain effects costing 3 Chaos or less may manifest for free inside the Domain; Chaos actually spent is tripled, with Q02 clarifying the table's rounding/application.
- Ripple Gun and Normal Briefcase core item rules were checked against v22.
- Mission MVP, Probation and Participant eligibility/tie-breaks were checked against v22.
- Regional Loose Ends rules, including +7 for an escaped anomaly and the weather-event roll/escalation process, were checked. The current Campaign baseline is 1; the next mission's weather roll has not been made.
- Chinese Vault pages 191–208 were read, including the complete d44 Sub-Reality table, station Chaos Effects table, rescue special effect, encounter and aftermath. English original collation remains open.

## 3. Defect-by-defect disposition

Statuses:
- **FIXED** — correction landed and read back in this branch.
- **PARTIAL** — structure improved, but a required execution or source proof remains.
- **OPEN** — unresolved and continues to block dependent readiness.

| ID | Severity | Status | Remediation / remaining boundary |
|---|---|---|---|
| PREP-001 | P1 | FIXED | Replaced ambiguous READY WITH OPEN ITEMS with separate delivery, validation, runtime and authorization dimensions; active module entry is DELIVERED / PREP RULE VALIDATION BLOCKED / NOT STARTED |
| PREP-002 | P1 | FIXED | Old source gaps are explicitly SUPERSEDED; Chinese source pagination is consistently recorded as pages 191–208 |
| RULE-001 | P1 | OPEN | Core rule matrix still contains OPEN/PARTIAL module mappings; no Preflight |
| RULE-002 | P1 | OPEN | Campaign default Chaos Pool 0 is bound, but module-specific override/close behavior still needs final source mapping |
| RULE-003 | P1 | FIXED | Rule hierarchy now distinguishes core rules, explicit module exceptions, errata and Campaign rulings; unresolved conflicts stop dependent rulings |
| RULE-004 | P2 | FIXED | SYSTEM_BINDING now pins v22 to immutable Commit `7f6d...`, not `main` |
| RULE-005 | P2 | FIXED | Chinese source reading range and official English collation are explicitly distinguished |
| SOLO-001 | P1 | PARTIAL | One-PC adaptation matrix added; action/resource costs and full rescue feasibility remain unproven |
| SOLO-002 | P2 | PARTIAL | Information-source dependency matrix added; bypassing one NPC leaves alternatives, but complete information parity is not established |
| RT-001 | P1 | FIXED | Runtime now instantiates revision, resume, applied/unapplied events, persistence manifest, reconciliation, dispute and T0 fields |
| RT-002 | P1 | FIXED | Scene, spatial, NPC knowledge, event/thread, delta and cumulative d44 entry history are represented |
| RT-003 | P1 | FIXED | Mandatory runtime assembly includes System Binding, Campaign rulings and Player-Facing Gate |
| RT-004 | P2 | PARTIAL | Section-level quick references added for common runtime needs; not every Prep item has a unique callout ID |
| PROC-001 | P1 | FIXED | Prep Rule Validation is now mandatory before Preflight; Preflight only restores verified state |
| PROC-002 | P1 | FIXED | This file is the Delivery Manifest/test record; final readback is recorded below |
| PROC-003 | P1 | PARTIAL | Expected-HEAD/CAS, PREPARE/APPLY/READBACK/PUBLISH and failure recovery are specified; real concurrent-write race test was not run |
| PROC-004 | P2 | FIXED | Substantive post-Preflight changes can trigger targeted version-specific regression without reopening the entire old Prep QA |
| PROC-005 | P2 | PARTIAL | Logical roles are defined; Casey holds multiple roles and is explicitly marked SELF-REVIEW |
| PROC-006 | P2 | FIXED | Generic resource standard now defines scopes only; Triangle-specific resource rules are bound in the Campaign/System layer |
| PROC-007 | P3 | FIXED | Duplicate subsection numbering corrected |
| RES-001 | P1 | FIXED | Historical pre-close Chaos UNKNOWN and post-close current Chaos 0 are separated |
| RES-002 | P2 | FIXED | Bower Street Session index now points to the closeout reset while preserving the pre-close unknown |
| RES-003 | P1 | FIXED | New ledger restores owner, event, before/after, status, idempotency, reversal and readback fields |
| RES-004 | P2 | FIXED | Runtime no longer owns mutable resource balances; it stores verified ledger checkpoint references only |
| RES-005 | P1 | OPEN | Harm, exact Demerits, absolute available Time and some equipment handoff values remain UNKNOWN; dependent mechanics remain blocked |
| RES-006 | P2 | PARTIAL | New ledger requires item-by-item equipment handoff; historical equipment restoration evidence still needs final reconciliation |
| DOC-001 | P3 | FIXED | Literal backslash-n separators removed from Campaign README and module index |

The original audit report's summary counts conflict with its own defect table. This log tracks the 27 distinct IDs above; no aggregate count from the audit's inconsistent summary is reused.

## 4. Executed structural tests

### Module / state checks

| Test | Result |
|---|---|
| All 11 original module artifacts exist | PASS |
| Module README and campaign index lifecycle state match | PASS |
| Campaign README and module index contain no literal `\\n` separators | PASS |
| Prep Rule Validation is a mandatory pre-Preflight gate | PASS |
| Player Notes remains empty and contains no scenario facts | PASS |
| Quick Reference mandates System Binding, rulings and disclosure gate | PASS |
| Resource Ledger contains before/after, owner, event, idempotency, status and reversal fields | PASS |
| Runtime contains checkpoint, resume, persistence and dispute fields | PASS |
| Runtime does not duplicate mutable resource balances | PASS |
| Generic resource standard is system-neutral | PASS |
| Delivery standard subsection numbering is unique | PASS |
| System Binding points to immutable v22 Commit | PASS |
| Character card no longer asserts zero current Demerits | PASS |
| Historical and post-close Chaos values are distinguished | PASS |
| Bower Street Session index distinguishes pre-close unknown from post-close reset | PASS |
| Active module entry no longer says READY WITH OPEN ITEMS | PASS |
| Old incomplete-pagination statements are marked SUPERSEDED | PASS |
| Single-agent and clue-dependency matrices exist | PASS |
| Player-Facing Gate is mandatory in Quick Reference | PASS |

**Structural checks: 18/18 PASS** across the two execution batches (some assertions overlap by design).

### Standards / reference checks

- Generic resource standard contains no Triangle-specific resource names in its generic scope section: PASS.
- Delivery standard numbering: PASS.
- Prep Rule Validation / Preflight boundary: PASS.
- Transaction and expected-HEAD contract present: PASS.
- Fixed v22 source link: PASS.
- Module README relative links: 11/11 PASS before this new log file was added; this log's link receives a separate post-create readback below.

## 5. Synthetic state tests

These tests executed against a small in-session state model matching the new ledger/checkpoint contract. They are not a committed CI test suite.

| Test ID | Test | Result |
|---|---|---|
| SYN-01 | Apply a resource transaction once | PASS |
| SYN-02 | Retry a VERIFIED idempotency key | PASS — no second application |
| SYN-03 | Recover an INCOMPLETE entry when target already equals expected after-value | PASS — verify without reapplying |
| SYN-04 | Detect a conflicting before-value | PASS — DISPUTED; preserve actual value |
| SYN-05 | Resume with applied and unapplied event IDs | PASS — do not replay applied event |
| SYN-06 | Re-enter Sub-Reality and preserve cumulative d44 results | PASS |
| SYN-07 | Reject NPC knowledge without a source event | PASS |

**Synthetic state tests: 7/7 PASS.**

## 6. Single-player desk simulations

Ten abstract player-action paths were executed against the source/Prep and current state contracts. They did not generate dice or mutate CANON.

| Test ID | Player action class | Result | Reason / boundary |
|---|---|---|---|
| DSK-01 | Choose among documented entry routes | PASS | Each route has a distinct first-contact/source path; no second PC is required to enter |
| DSK-02 | Bypass one anchor NPC | PARTIAL | Other clue-source categories remain; the skipped source's unique information is not automatically replaced |
| DSK-03 | Bypass a different anchor NPC | PARTIAL | Alternative observation/NPC sources exist; exact clue parity and dependency costs remain unproven |
| DSK-04 | Act on an incorrect hypothesis | PASS | World facts remain independent; procedure distinguishes player inference from confirmed fact |
| DSK-05 | Use a non-prepared ability/action | BLOCKED | Ability-specific resolution and related v22 mechanics remain OPEN; no guessed ruling allowed |
| DSK-06 | Choose rescue order or decline one objective | PARTIAL | Player choice is preserved; full action/resource/time cost and downstream feasibility remain unproven |
| DSK-07 | Re-enter an already visited Sub-Reality | PASS | Source requires one d44 roll per prior entry and cumulative application; Runtime stores entry count/history |
| DSK-08 | Complete a rescue, then re-enter the station | PASS | Source trigger is explicit; event/checkpoint contract prevents duplicate trigger application |
| DSK-09 | Proceed without NPC assistance | PARTIAL | One PC remains the only PC; information alternatives exist, but every core route's solo cost is not proven |
| DSK-10 | Attempt resource-intensive action with unknown current balances | BLOCKED | Unknown Harm/QA/Chaos/Time values stop dependent mechanics; unrelated narration remains available |

**Desk simulation: 10 scenarios; 4 PASS, 4 PARTIAL, 2 BLOCKED.** This is not a full round-by-round GM/player simulation.

## 7. Test evidence boundary

| Evidence type | Count | Status |
|---|---:|---|
| Static structural checks | 18 | PASS |
| Standards/reference checks | 7 | PASS |
| Module README relative links (before this file) | 11 | PASS |
| Synthetic state tests | 7 | PASS |
| Desk simulations | 10 | 4 PASS / 4 PARTIAL / 2 BLOCKED |
| Full round-by-round executed GM/player simulation | 0 | NOT RUN |
| Real player test | 0 | NOT RUN |
| Independent blind review | 0 | NOT RUN |

The static and synthetic tests verify document contracts and state handling only. They do not establish that every scene or mechanical path can be run end-to-end.

## 8. Remaining blockers

1. Official English *The Vault* original has not been independently collated against the Chinese translation.
2. Prep Rule Validation still has OPEN/PARTIAL core mechanics, including module-specific Chaos behavior, Harm/Domain application, ability resolution and full reward/penalty mapping.
3. One-PC action/resource costs and key clue dependency paths remain only partially proven.
4. Harm, exact Demerits, absolute available Time and equipment handoff are not all reconciled. Do not guess.
5. A real concurrent branch update / partial-write failure injection test has not been run.
6. Player-Facing Gate is an output-discipline constraint, not technical access control. The public repository's GM-only labels do not prevent a repository reader from opening those files.

## 9. Current decision

- Artifact delivery：DELIVERED on the remediation branch.
- Prep design：REVIEWED.
- Source validation：BLOCKED.
- Prep Rule Validation：BLOCKED.
- Single-player feasibility：PARTIAL / OPEN.
- Runtime schema and resource transaction structure：REMEDIATED; synthetic tests PASS.
- Optional independent Prep QA：NOT RUN.
- Preflight：NOT STARTED / BLOCKED.
- Runtime：NOT STARTED.
- Player authorization：WAITING FOR USER “开始”.

No test-only event was written to Session Log, Player Notes, Runtime CANON or the character sheet. No GM-only information was included in player-facing files. No main-branch write, PR or external AI review occurred in this batch.
