# Resource Ledger｜Blame It on the Trains

> GM-only。模组资源交易唯一流水。当前账本 EMPTY；所有开场余额须在 Preflight 从权威人物卡/战役账本核对。不得从历史快照推算未知余额。

## 1. Opening reconciliation (NOT EXECUTED)

- Session：NOT STARTED
- Character snapshot：PENDING PRE-FLIGHT READBACK
- Previous module close：Bower Street closeout; exact source checkpoint must be cited at Preflight
- Commendations：18（暂定交接值；须回读人物卡）
- QA：任务间恢复规则已绑定；逐项上限/当前值须回读人物卡
- Demerits：UNKNOWN
- Harm：UNKNOWN / RULE RECONCILIATION REQUIRED
- Available Time：UNKNOWN（仅 Bower Street 完整结团 +1 奖励已确认）
- Ordinary Chaos Pool：本模组独立池；开场值须按模组/战役权威依据核验，不继承旧模组余额
- Ripple Gun：暂定 1/1；须按装备规则与人物卡点交
- Loose Ends：Campaign 基线暂记 1，Bower Street 模组增量 +0；Preflight 核对 Campaign 权威记录
- Other equipment / holders / charges：PENDING ITEM-BY-ITEM HANDOFF

UNKNOWN is a real state, not zero. An unknown balance blocks only transactions that depend on that balance; it does not block unrelated narration.

## 2. Resource scope (generic categories)

| Scope | Definition | Close/reset behavior |
|---|---|---|
| Session-scoped | Resource consumed/restored within one Session | Per active system rules |
| Module-scoped | Temporary pool or counter owned by this Module | Per active system/module rules; close only when explicitly required |
| Campaign-persistent | Resource persists across Modules | Never reset merely because a Module closes |
| Character snapshot | Boundary snapshot, not an event ledger | Updated only at authorized reconciliation checkpoints |
| Equipment charge / use | State attached to a specific item and holder | Per that item's rule and explicit handoff |
| Cumulative regional metric | Campaign/region baseline plus Module delta | Preserve baseline and record this Module's delta, including +0 |

Concrete resources and their reset/award rules are defined by the active System Binding, Campaign rulings, module source and item rules—not by this generic category table.

## 3. Ledger schema

| Entry ID | Event ID | Session | Timestamp | Owner | Resource | Scope | Balance Before | Delta | Balance After | Rule Basis | Source / Evidence | Application Status | Idempotency Key | Reverses Entry |
|---|---|---|---|---|---|---|---:|---:|---:|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | — | EMPTY | — | — | — |

### Required status enum

- PREPARED：交易已计算并登记待应用，尚未改变权威余额。
- APPLIED：已按权威来源执行一次；必须记录应用后的余额/状态。
- VERIFIED：独立回读确认权威记录与交易结果一致。
- INCOMPLETE：部分字段或目标写入；不得视为已完成。
- DISPUTED：来源、前值、应用状态或余额存在冲突。
- REVERSED：通过新的冲正 Entry 抵消；原交易保留。

Empty ledger rows are not events. Never create placeholder transaction IDs for unoccurred events.

## 4. Transaction contract (idempotent)

For every resource transaction:

1. Identify one actual Event ID and a stable Idempotency Key (normally Campaign/Module + Event ID + Resource + Owner).
2. Resolve the resource owner and scope from the System Binding / Campaign rule / item rule.
3. Read the authoritative Balance Before. If unknown, stop this transaction; do not guess.
4. Record the rule basis and source evidence. Calculate Delta and expected Balance After.
5. Append PREPARED before applying any cross-file state change.
6. Apply the transaction once to its owning record.
7. Read back the owning record independently and compare the observed result with the expected Balance After.
8. Mark VERIFIED only after readback. Update the Runtime checkpoint to reference the verified Entry ID.
9. If any step fails, mark INCOMPLETE or DISPUTED and preserve the prior verified checkpoint.

### Retry / duplicate protection

- Before retrying, search the Idempotency Key and Event ID.
- If a matching transaction is VERIFIED, do not apply it again.
- If PREPARED / INCOMPLETE / DISPUTED, reconcile the target before retrying; never assume it was not applied.
- A correction is a new Entry with `Reverses Entry` pointing to the original. Never edit or delete the original row.
- Multiple resource effects from one event use distinct Entry IDs but share the same Event ID and batch ID.

## 5. Checkpoints and reconciliation

- Session checkpoint: record last VERIFIED Entry ID for each resource owner/scope.
- Runtime State stores only checkpoint references; it does not duplicate mutable balances.
- Character sheet is updated only at the authorized Session/Module boundary, after ledger reconciliation.
- Campaign-level resources and module-level resources must not be mixed.
- Historical UNKNOWN remains UNKNOWN unless new source evidence resolves it.
- A resource reset is itself an explicit transaction with rule basis, before/after values and close event ID.

## 6. System-specific rules binding (Triangle Agency / Zarek only)

The following are pointers to Campaign-specific rules, not generic ledger rules:

- QA, Burnout, Chaos, Harm, Domain, Commendations, Demerits and Loose Ends: see `Campaigns/Zarek/SYSTEM_BINDING.md`, `RULE_ADJUDICATIONS.md`, the Chinese v22 rulebook and module-specific source.
- Time award timing and reverse-linked fields: Campaign ruling Q05. A complete Module close awards +1 available Time; a Session close alone does not. The award and the separately tracked remaining-Time field must be recorded as separate linked changes. If either absolute before-value is UNKNOWN, record only the confirmed delta and leave the resulting absolute balance UNKNOWN.
- Ripple Gun and Normal Briefcase: item-specific v22 rules plus explicit holder/charge handoff. Do not infer blanket equipment restoration from a generic category.

## 7. Module close (NOT EXECUTED)

At Module close, after the actual close condition is met:

1. Freeze the event range and identify all actual Session Logs / Runtime checkpoints.
2. Reconcile every resource transaction by owner and scope.
3. Apply only source-supported awards, penalties and resets.
4. Record the close event and any persistent resource changes as new entries.
5. Reconcile equipment and item holders individually.
6. Update the character sheet only after the ledger is verified.
7. Read back all changed records and publish a close checkpoint.
8. Keep unresolved values UNKNOWN / DISPUTED; do not block unrelated completed outcomes.

## 8. Current ledger status

- Transactions：0
- Applied transactions：0
- Verified transactions：0
- Pending transactions：0
- Session：NOT STARTED
- This section records current repository state only; it does not authorize play.
