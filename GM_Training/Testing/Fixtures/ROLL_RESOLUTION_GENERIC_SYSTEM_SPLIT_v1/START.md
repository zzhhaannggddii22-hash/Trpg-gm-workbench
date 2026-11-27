# START｜Generic/System Roll Split Regression v1

> Type: SINGLE_SESSION_SELF_TEST
> Fixture ref: qa/roll-resolution-generic-system-split-fixtures-v1_3
> Workbench candidate commit: 9ae553e864408cbe5678cdf9f93a0e61e5219eaf
> Baseline main commit: ec54bc100dceaf1da370edd811da22dc48f07a42
> Status: TEST_ONLY_NON_CANON

## Goal
Verify that generic GM routing remains system-neutral; the current Triangle Agency binding alone supplies Triangle Agency mechanics; player roll initiation and assistant default execution remain separate; core roll branches do not mix; current Resource Ledger / Runtime projection boundaries are respected; unsupported Playwall mechanics stop safely.

## Read order
1. Read this START and GM_PACKET.
2. Read ACTION_01, execute and update only the test ledger.
3. Then read ACTION_02; repeat sequentially through ACTION_11.
4. Do not read ORACLE until all eleven actions have been processed.
5. After the final action, read ORACLE and produce a structured self-review.

## Required source refs
- System/runtime baseline: ec54bc100dceaf1da370edd811da22dc48f07a42
- Candidate generic/system roll design: 9ae553e864408cbe5678cdf9f93a0e61e5219eaf
- Every GitHub read must pass the exact ref explicitly.
- Missing source or fixture dependency => BLOCKED; do not switch to main or guess.

## Scope and limits
This fixture tests a deterministic reference model and observable rule-routing behavior. It does not prove actual platform RNG, live Resource Ledger writes, multi-user ChatGPT turns, or deployed UI behavior.


## v1.2 correction
The original v1 ACTION_06 and ACTION_07 omitted the exact Quality. This immutable v1.1 fixture supplies those values; v1 remains unchanged as historical evidence.


v1.2 separates Playwall authorization failure from an unlocked document whose dice mechanics are not integrated. It adds one action and pins the current main commit.


v1.3 clarification: the fixture explicitly distinguishes real Playwall authorization from the single synthetic A7 document used only in ACTION_10.
