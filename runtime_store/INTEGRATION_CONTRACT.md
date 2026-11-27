# GitHub Runtime Store｜GM Runtime Integration Contract

**Status:** ARCHITECTURE REVIEW / IMPLEMENTATION CONTRACT — NOT A DEPLOYED COORDINATOR

This document maps the generic storage component to the existing GM Runtime. It is subordinate to:

- `GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md` §§14.4-A, 14.6, 14.8, 14.10, 14.12, 14.14, 14.17, 14.19.
- `Systems/SYSTEM_RULE_RUNTIME_INTEGRATION_PROTOCOL.md` §§1–9.
- `GM_Training/GITHUB_RUNTIME_SAVE_QUICK_PATH.md`.

If this document conflicts with those authorities, the existing GM Runtime and System Integration protocols win.

## 1. Decision

The GraphQL adapter is a **storage backend only**. It is not a GM Runtime, event adjudicator, system rules engine, player projection filter, incident manager, or campaign state authority.

The integration must have one caller above the adapter: a future **Runtime Persistence Coordinator**. That coordinator is responsible for translating an already-adjudicated and authorized Runtime batch into storage operations, then reconciling the returned storage evidence against the domain manifest and current Runtime state.

No Triangle Agency or Cairn rules adapter may call the GitHub storage adapter directly. System adapters provide verified rule outcomes and state deltas to the generic Runtime layer; they do not own persistence policy.

## 2. Authority and ownership map

| Concern | Authoritative owner | Adapter responsibility |
|---|---|---|
| Rule resolution, legal transitions, resource semantics | Active `Systems/<System>/` adapter | None |
| Campaign facts, Runtime State, Session Log, event identity | Campaign / GM Runtime | Store exact approved bytes |
| Event revision, field ownership, before/after values, ordered applications | GM Runtime §14.14 reconciliation manifest | Preserve the immutable manifest bytes and fingerprint |
| Visibility, recipient scope, presentation segments, Player Notes allowlist | GM Runtime §14.4-A / §§14.8, 14.16, 14.19 | No authorization or filtering; store only the already-approved projection |
| T0, field disputes, persistence disputes, dependencies and player authorization | GM Runtime §§14.6, 14.11, 14.15 | Return storage evidence/errors; never resolve domain disputes |
| Commit ancestry, immutable PREPARE/receipt records, expected HEAD, exact file-byte verification | GitHub Runtime Store | Enforce and report storage facts |
| Player-facing publication and GM-only access boundary | Authorized delivery host / GM Runtime | No delivery or access-control claims |

A successful Git commit proves that bytes were committed. It does **not** prove that a rule was applied correctly, that every intended event field was included, that a Player Notes projection was authorized, or that a player received it.

## 3. One manifest authority — no second ledger

For an important cross-file batch, the one immutable GM-only PREPARE object must be the existing §14.14 `reconciliation_manifest` (with the §14.4-A event envelope and required-target mapping). It is not a second, storage-specific business manifest.

The future coordinator must build and validate this domain manifest before calling `prepare()`. The manifest must preserve, as applicable:

- `manifest_id`, version, `batch_id`, exact base/target domain revisions and creation time;
- each ordered event's `event_id`, `event_revision_id`, `payload_version`, `payload_fingerprint`, sequence and exact `applied_fields[]` with object, canonical field path, before/after value references and application status;
- §14.4-A visibility, recipient scope and exact projection target/record identities;
- each required file target and its expected content fingerprint;
- the previous independently verified published checkpoint reference.

The adapter's current generic envelope (batch ID, revisions, base Git OID and file fingerprints) is only a **storage transport envelope**. It is not, by itself, a §14.14 reconciliation manifest. The coordinator must pass the complete domain manifest as an opaque, fingerprinted member of the PREPARE payload. The adapter may preserve and fingerprint it, but must not interpret its game semantics.

The Runtime State fields `persistence.prepare_manifest_ref` and `checkpoint.reconciliation_manifest_refs[]` must point to this same immutable PREPARE object. They are references/indexes, not duplicate manifest copies. Do not create another Operation Index, registry, event ledger or parallel reconciliation manifest.

The Operations branch is the GM-only storage lane for that one PREPARE object. Its direct `.runtime/operations/<batch_id>.json` locator is acceptable only when the coordinator binds it to the exact Campaign/Module/Run identity and stores that reference in the existing Runtime State fields. It must not become a separate source of domain truth.

## 4. Commit lifecycle

The future coordinator owns the full domain lifecycle:

1. **ADJUDICATE / AUTHORIZE** — resolve the action under the active system rules; determine actual state deltas, field ownership, visibility, recipient scope and permitted projection targets. No persistence call can repair a bad adjudication.
2. **BUILD DOMAIN MANIFEST** — create the single immutable §14.14 manifest, ordered applications and required target records. Verify the exact target file set against the authorized projection target set.
3. **PREPARE** — call adapter `prepare()`; independently confirm the exact manifest was stored and read back. Until then, no target write is permitted.
4. **PUBLISH STORAGE COMMIT** — call adapter `publish()`. The Runtime State, Session Log, approved Player Notes (if any), required GM audit target(s), storage checkpoint and receipt are committed together in one Runtime-branch commit guarded by GitHub `expectedHeadOid`.
5. **RECONCILE DOMAIN** — read the exact commit identified by the adapter; verify the manifest, each ordered application, field-level before/after evidence, target identities, recipient/visibility mapping and complete file contents. Verify that the new Runtime checkpoint references the same manifest and that the application chain reaches the new domain revision.
6. **FINALIZE DOMAIN STATE** — only the coordinator may set domain persistence status to `PUBLISHED`, mark Session Log applications APPLIED/PARTIAL, update `reconciliation_manifest_refs[]`, and clear only those pending fields proven applied.
7. **HANDLE DISPUTES** — on mismatch, keep the domain batch INCOMPLETE/DISPUTED. Use §14.6 to append the durable `persistence.disputes[]` object and matching Session Log INCIDENT/DISPUTE event, then independently read both back. Do not silently repair, overwrite, or clear evidence.

Because the storage publication is a single atomic Git commit, a crash before it leaves a PREPARED operation and the prior Runtime checkpoint intact. A lost response after the commit is resolved by the immutable receipt and exact historical commit readback. The coordinator must still perform domain-level reconciliation after storage reconciliation.

## 5. Storage status is not domain status

The adapter API uses storage-scoped statuses:

- `STORE_NOT_FOUND`
- `STORE_PREPARED`
- `STORE_COMMITTED`
- `STORE_DISPUTED`

`STORE_COMMITTED` means only that the receipt, expected parent, store checkpoint and declared target-file bytes have been verified at one immutable commit.

It must never be rendered to a player or copied directly into Runtime State as domain `PUBLISHED`. Only the coordinator can promote a batch to domain `PUBLISHED` after §14.4-A / §14.14 checks pass. Likewise, `STORE_DISPUTED` is evidence for the coordinator; it is not a substitute for the durable §14.6 dispute object.

## 6. Two different checkpoints

The adapter's `.runtime/store_checkpoint.json` is **storage metadata only**. It records the commit's batch, domain revision labels, previous Runtime commit OID and PREPARE/receipt references so the adapter can verify its own commit.

It is not the authoritative Runtime State `checkpoint:` object and must not replace or shadow:

- `checkpoint.revision`, `branch`, `last_event_id`;
- `unapplied_event_ids[]`, `applied_event_ids[]`;
- `reconciliation_manifest_refs[]`;
- `persistence.published_checkpoint_ref`, `prepare_manifest_ref` and domain reconciliation state.

The rename from `.runtime/checkpoint.json` to `.runtime/store_checkpoint.json` is deliberate: it prevents storage metadata from being mistaken for the campaign's authoritative checkpoint.

## 7. Player projection and delivery boundary

The adapter does not decide whether a Player Notes file should exist or what it may contain. Before a Player Notes target is included, the coordinator must:

- derive it from the one authorized `player_reply_payload` / recipient-specific view under §14.19;
- enforce field-level allowlists, recipient scope and presentation evidence;
- keep GM Audit Artifact separate from Player Artifact under §14.12;
- use a host with private staging, independent readback, complete scan and an explicit publication boundary under §14.17.

A Git commit is not proof of private staging, player delivery, recipient isolation, or access control. If the host cannot establish those controls, the coordinator must not publish a player-facing artifact and must preserve NOT_PUBLISHED / NOT_VERIFIABLE.

## 8. Lightweight save path remains the default

`GM_Training/GITHUB_RUNTIME_SAVE_QUICK_PATH.md` remains the default for ordinary, low-risk, single-host state/log updates that can be committed together in one Git commit with expected-HEAD protection and readback.

The GraphQL adapter is an optional backend for workflows that actually require an independently discoverable PREPARE record, immutable receipt, historical recovery and stronger reconciliation evidence. Do not route every ordinary turn through PREPARE or add per-message persistence overhead.

If the one-commit quick path is sufficient for a particular operation, do not instantiate a second branch pair or manifest lifecycle merely because the adapter exists. The coordinator chooses the path by the existing Runtime risk/trigger rules, not by system name.

## 9. Campaign and branch identity

Each configured branch pair must map to exactly one repository + Campaign ID + Module/Run identity and a documented Runtime State root. The immutable PREPARE manifest must carry that identity. Branch provisioning, least-privilege token provisioning and repository rules are administrative prerequisites, not adapter side effects.

Before any production use, independently verify that both branches block force-push and deletion and that the token can write only to the intended repository/branches to the extent GitHub permissions allow. The current live smoke proves component behavior with temporary branches; it does not prove branch-protection policy or production access isolation.

## 10. Adoption gates

Do not connect this component to a live Campaign or remove Draft status until all are true:

1. A concrete Runtime Persistence Coordinator exists and has an explicit typed request/response contract.
2. The one domain reconciliation manifest is passed intact through PREPARE; no second ledger/manifest is introduced.
3. Runtime State, Session Log, and any Player Notes / GM Audit targets are generated from the same authorized event envelope and exact field ownership.
4. Storage commit evidence and domain application evidence remain separate; storage status cannot set domain PUBLISHED.
5. Cold-start reconciliation verifies the exact manifest, field-level ordered application chain, target records and current revision.
6. §14.6 disputes are durably written to Runtime State and Session Log, independently read back, and block dependent actions.
7. Player projection staging, scanning, recipient controls and publication satisfy §§14.12, 14.17 and 14.19 in the actual host.
8. Branch protections, least-privilege credentials and Campaign/Run isolation are independently verified.
9. Target-environment P1-0C gaps are addressed by their own controlled tests. Component smoke results do not replace those tests.

**Current disposition:** storage component and live component smoke are validated; Runtime coordinator, domain manifest integration, durable dispute handling, player publication controls, branch protections and target-environment P1-0C remain NOT IMPLEMENTED / NOT VERIFIED. Keep PR #78 Draft.
