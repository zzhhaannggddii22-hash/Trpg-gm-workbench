# Module Closeout Cold-Recovery Regression v1

> Test type: SINGLE_SESSION_SELF_TEST with deterministic synthetic state.
> Purpose: exercise v0.3 recovery decisions without relying on previous chat history.
> Evidence boundary: this fixture can validate protocol logic in a simulated cold-start scenario. It cannot prove Git/host persistence, conditional writes, or actual cross-session discoverability.
> Canonical protocol: `GM_Training/MODULE_CLOSEOUT_AND_RESOURCE_RECONCILIATION_PROTOCOL.md`
> System adapter: `Systems/Triangle_Agency/Rule_Reference/03_MODULE_CLOSEOUT_ADAPTER.md`

## START｜Locked synthetic input

All names and values below are synthetic. They are not Campaign canon.

### Runtime identity
- Campaign ID: `CAMP-SYN-01`
- Source Module ID: `MOD-SYN-ALPHA`
- Run/Branch Identity: `RUN-SYN-01 / branch-A`
- Destination Module ID: `MOD-SYN-BETA`
- Last verified published checkpoint: `CP-010`
- Published pointer at test start: `CP-010`

### Closeout operation
- `closeout_operation_id`: `CLO-ALPHA-001`
- `prepare_manifest_id`: `MAN-ALPHA-001`
- `save_batch_id`: `BATCH-ALPHA-001`
- `plan_revision`: `PLAN-1`
- `system_rules_revision`: `TA-v22-synthetic-lock`
- `adapter_revision`: `TA-CLOSEOUT-ADAPTER-v1`
- `campaign_rules_revision`: `CAMP-RULES-4`
- `module_rules_revision`: `MOD-RULES-7`
- `source_event_revision`: `EVENTSET-22`
- Operation identity is unique and the PREPARE Manifest is independently discoverable from the Module's existing GM-only Operational Diagnostics and Runtime persistence.prepare_manifest_ref by Campaign + Module + Run + Branch.

### Frozen settlement plan
1. Confirm Module result and report rating independently.
2. Confirm MVP eligibility and the player's selected free Competency mark.
3. Apply the selected Quality QA cap increase from 1 to 2.
4. Restore QA to the final cap, yielding 2/2.
5. Apply paired Time fields as two separate operations: usable Time +1; remaining Time -1.
6. Reconcile persistent resources and module-scoped resets.
7. Publish required field targets and Module CLOSED in one final publication batch.

The order in items 2–4 is adapter-specific and is not a Generic hard-coded rule.

### Partial-application snapshot
| Field | Planned target | Existing evidence at cold start |
|---|---|---|
| Usable Time | +1 delta | Field Operation `FOP-TIME-PLUS-01` independently read back as APPLIED |
| Remaining Time | -1 delta | No application evidence; state NOT_APPLIED only because the target and operation history prove no write occurred |
| QA cap | 2 | APPLIED under `FOP-QA-CAP-01` |
| QA current value | 2/2 | NOT_APPLIED; prior value 0/1 |
| Character boundary snapshot | New version referencing last Entry ID | Candidate absent; NOT_APPLIED |
| Module lifecycle | CLOSED | Published pointer still references CP-010; effective status is CLOSEOUT_PENDING because MAN-ALPHA-001 exists |
| Publication pointer | BATCH-ALPHA-001 | UNPUBLISHED |

### Independent evidence
- PREPARE Manifest exists and reads back intact.
- Existing Operational Diagnostics contains exactly one active operation for this Module/Run, and Runtime persistence references point to its PREPARE Manifest.
- The published pointer still references CP-010.
- No other writer changed the base revision.
- One historical Demerits value is UNKNOWN; the adapter marks it AUDIT_ONLY for this scenario because no closeout step or destination prerequisite depends on its exact amount.
- Postmortem has not been performed.

## ACTION｜Cold recovery execution

Execute in this order. Do not assume prior chat history.

1. Recover the current published checkpoint and branch/run identity.
2. Query the existing Module GM-only Operational Diagnostics and Runtime persistence references for the active closeout operation.
3. Discover and independently read the PREPARE Manifest.
4. Verify unique Operation ID, rules/adapter/plan revisions, source event revision and base checkpoint.
5. Re-read each field target and classify its Application state.
6. Continue only operations proven not yet applied; do not reapply APPLIED fields.
7. Reconcile the final field values and all required targets.
8. Publish the result, required handoff fields and Module CLOSED together through the final publication pointer.
9. Independently read the publication pointer and target versions.
10. Evaluate Destination Module READY separately from source Module CLOSED.
11. Confirm that unfinished Postmortem and the AUDIT_ONLY Demerits value do not block unrelated closeout/intermission work.

## ORACLE｜Expected decisions

- The old published pointer CP-010 does not imply there is no pending closeout.
- MAN-ALPHA-001 must be found from existing GM-only Operational Diagnostics and Runtime persistence Manifest references.
- CLO-ALPHA-001 is reused; no new closeout operation is created.
- Usable Time +1 and QA cap +1 are not repeated.
- Remaining Time -1, QA restore to 2/2 and the character boundary snapshot are applied only once.
- If a field's application cannot be proven, classify it UNVERIFIABLE, not NOT_APPLIED.
- Module remains logically CLOSEOUT_PENDING until final publication succeeds.
- The final publication batch includes Module CLOSED and required handoff fields; no separate post-publication CLOSED write occurs.
- After final publication, CLOSED is verified from the pointer and target readback.
- Destination Module READY remains NOT_CHECKED until MOD-SYN-BETA's own Required Fields and Preflight are checked.
- UNKNOWN Demerits remains unknown; it does not block this scenario's independent closeout, but it would block any action requiring its exact balance.
- Postmortem remains optional and does not block CLOSED.

## Negative controls

### NC-1｜Manifest discovery unavailable
If the existing Operational Diagnostics or Runtime persistence references cannot be queried, or their completeness cannot be verified, do not infer “no pending operation” from CP-010. Mark PENDING_DISCOVERY / UNVERIFIABLE and block dependent progression.

### NC-2｜Multiple active operations
If Operational Diagnostics contains two active Operation IDs, or two manifests both claiming the current valid plan for the same Module/Run/Scope (excluding explicitly SUPERSEDED plan revisions), stop automatic settlement. Do not choose the newest.

### NC-3｜Lost final publication receipt
If the pointer references BATCH-ALPHA-001 and all required targets independently match, classify PUBLISHED and do not replay. If the pointer remains CP-010 and the original manifest/targets/base remain unchanged, retry only the original conditional publication. If the base or targets drift, stop and reconcile.

### NC-4｜Host lacks conditional publication
Leave the batch UNPUBLISHED. Produce a pending-save handoff; do not claim Module CLOSED.

## Pass criteria

All positive expected decisions are satisfied; no negative control permits duplicate application, guessed state, silent closure or false READY.
