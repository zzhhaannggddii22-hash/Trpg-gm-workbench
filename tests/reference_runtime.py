"""Test-only implementation of the documented contracts. Never loads a real save."""
from hashlib import sha256
import json
import os
from pathlib import Path
import sys


def read_json(path):
    return json.loads(path.read_bytes())


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n").encode()


def digest(value):
    return sha256(encoded(value)).hexdigest()


def write_json(path, value):
    temp = path.with_suffix(".tmp")
    temp.write_bytes(encoded(value))
    temp.replace(path)


class Batch:
    """A single prepared batch in a synthetic sandbox, with repeatable process faults."""

    def __init__(self, root):
        self.root = root
        self.base = root / "previous.json"
        self.manifest = root / "prepare.json"

    def prepare(self, event):
        if self.manifest.exists():
            old = read_json(self.manifest)
            if event != old["event"]:
                raise ValueError("same batch identity with different event")
            return old
        base = read_json(self.base)
        envelope = {key: event[key] for key in
                    ("event_id", "batch_id", "base_revision", "target_revision", "event_revision_id",
                     "visibility", "recipient_scope")}
        if base["revision"] != envelope["base_revision"]:
            raise ValueError("base revision changed")
        targets = {
            "runtime": {**envelope, "revision": event["target_revision"],
                        "balance": base["balance"] + event["delta"]},
            "log": {**envelope, "delta": event["delta"]},
            "notes": {**envelope, "text": event["public_text"]},
        }
        manifest = {"event": event, "targets": targets,
                    "expected_fingerprints": {name: digest(data) for name, data in targets.items()}}
        write_json(self.manifest, manifest)
        if read_json(self.manifest) != manifest:
            raise ValueError("PREPARE readback failed")
        return manifest

    def inspect(self):
        if not self.manifest.exists():
            return {"batch_status": "UNKNOWN"}
        manifest = read_json(self.manifest)
        targets = {}
        for name, wanted in manifest["expected_fingerprints"].items():
            path = self.root / (name + ".json")
            if not path.exists():
                targets[name] = "MISSING"
            elif sha256(path.read_bytes()).hexdigest() == wanted:
                targets[name] = "VERIFIED"
            else:
                targets[name] = "DISPUTED"
        publication = self.root / "published.json"
        current_base = read_json(self.base)
        verified = all(status == "VERIFIED" for status in targets.values())
        current = manifest["event"]["base_revision"] == current_base["revision"]
        published_proof = {"batch_id": manifest["event"]["batch_id"],
                           "manifest_fingerprint": digest(manifest)}
        published = (verified and current and publication.exists() and
                     read_json(publication) == published_proof)
        return {"batch_status": ("PUBLISHED" if published else
                                 "DISPUTED" if not current or "DISPUTED" in targets.values() else
                                 "INCOMPLETE"),
                "targets": targets}

    def finish(self, event, fault=None):
        manifest = self.prepare(event)
        before = self.inspect()
        if before["batch_status"] == "DISPUTED":
            return before
        if before["batch_status"] == "PUBLISHED":
            return {**before, "writes": 0}
        writes = 0
        order = ("runtime", "log", "notes") if fault == "runtime-only" else ("log", "runtime", "notes")
        for name in order:
            if before["targets"][name] == "MISSING":
                write_json(self.root / (name + ".json"), manifest["targets"][name])
                writes += 1
            if writes == 1 and fault in ("log-only", "runtime-only"):
                print(json.dumps({"pid": os.getpid(), "partial_target": name}), flush=True)
                os._exit(73)
        reread = self.inspect()
        if set(reread["targets"].values()) != {"VERIFIED"} or reread["batch_status"] == "DISPUTED":
            return reread
        write_json(self.root / "published.json", {"batch_id": event["batch_id"],
                                                "manifest_fingerprint": digest(manifest)})
        if fault == "ack-lost":
            os._exit(74)
        return {**self.inspect(), "writes": writes}



class CloseoutBatch:
    """Test-only reference model using Runtime's existing GM-only diagnostics records."""

    def __init__(self, root):
        self.root = root
        self.diagnostics = root / "operational_diagnostics.json"
        self.runtime = root / "runtime_state.json"
        self.base = root / "base.json"
        self.candidate = root / "candidate.json"
        self.published = root / "published.json"

    def discover(self, identity):
        if not self.diagnostics.exists():
            return {"status": "PENDING_DISCOVERY"}
        diagnostics = read_json(self.diagnostics)
        if diagnostics.get("complete") is not True:
            return {"status": "PENDING_DISCOVERY"}
        matches = [item for item in diagnostics.get("records", [])
                   if item.get("manifest", {}).get("identity") == identity
                   and item.get("status") not in ("SUPERSEDED", "CANCELLED")]
        if len(matches) > 1:
            return {"status": "IDENTITY_CONFLICT"}
        if len(matches) == 1:
            return {"status": "FOUND", "operation": matches[0]}
        if self.runtime.exists():
            runtime = read_json(self.runtime)
            persistence = runtime.get("persistence", {})
            has_pending_reference = (
                persistence.get("status") in ("PREPARED", "INCOMPLETE", "PENDING_EXTERNAL_WRITE", "DISPUTED")
                or persistence.get("batch_id")
                or persistence.get("prepare_manifest_ref")
                or any(str(ref).startswith("GMOD-CLOSEOUT-")
                       for ref in persistence.get("reconciliation_manifest_refs", []))
            )
            if has_pending_reference:
                # A mismatched/missing Run identity cannot prove this state is unrelated.
                # Runtime references locate the immutable diagnostics record; they cannot replace it.
                return {"status": "PENDING_DISCOVERY"}
        return {"status": "NOT_FOUND_VERIFIED"}

    def _repair_runtime_locator(self, record):
        manifest = record["manifest"]
        runtime = read_json(self.runtime)
        if runtime.get("identity") != manifest["identity"]:
            return "DISPUTED"
        persistence = runtime.setdefault("persistence", {})
        pointer = read_json(self.published) if self.published.exists() else None
        published = pointer == {
            "operation_id": manifest["operation_id"],
            "batch_id": manifest["batch_id"],
            "manifest_fingerprint": digest(manifest),
            "checkpoint_id": manifest["target_checkpoint_id"],
        }
        persistence.update({
            "batch_id": manifest["batch_id"],
            "status": "PUBLISHED" if published else "PREPARED",
            "prepare_manifest_ref": record["manifest_ref"],
            "previous_published_checkpoint_ref": manifest["base_checkpoint_id"],
        })
        persistence.setdefault("reconciliation_manifest_refs", [])
        persistence.setdefault("applied_event_ids", [])
        if published:
            persistence["published_checkpoint_ref"] = manifest["target_checkpoint_id"]
            if record["manifest_ref"] not in persistence["reconciliation_manifest_refs"]:
                persistence["reconciliation_manifest_refs"].append(record["manifest_ref"])
        write_json(self.runtime, runtime)
        if read_json(self.runtime) != runtime:
            return "UNVERIFIABLE"
        return "OK"

    def begin(self, identity, requested_operation_id, plan):
        found = self.discover(identity)
        if found["status"] == "FOUND":
            record = found["operation"]
            if record["manifest"]["plan_fingerprint"] != digest(plan):
                raise ValueError("frozen closeout plan changed; create an authorized plan revision")
            locator_status = self._repair_runtime_locator(record)
            if locator_status != "OK":
                return {"status": locator_status}
            return found
        if found["status"] != "NOT_FOUND_VERIFIED":
            return found
        # O_EXCL is a deterministic test stand-in for conditional first-start creation;
        # it does not prove the real Git branch-head CAS and is not a production lock service.
        lock = self.root / "operational-diagnostics.lock"
        try:
            descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            os.close(descriptor)
        except FileExistsError:
            return {"status": "IDENTITY_UNVERIFIABLE"}
        try:
            found = self.discover(identity)
            if found["status"] != "NOT_FOUND_VERIFIED":
                return found
            diagnostics = read_json(self.diagnostics)
            if any(item.get("manifest", {}).get("operation_id") == requested_operation_id
                   and item.get("manifest", {}).get("identity") != identity
                   for item in diagnostics.get("records", [])):
                return {"status": "IDENTITY_CONFLICT"}
            base = read_json(self.base)
            candidate = read_json(self.candidate)
            if base["revision"] != candidate["base_revision"]:
                return {"status": "DISPUTED"}
            targets = plan["targets"]
            field_operation_ids = plan["field_operation_ids"]
            if set(targets) != set(field_operation_ids):
                raise ValueError("each target field requires one stable field_operation_id")
            manifest = {
                "operation_id": requested_operation_id,
                "manifest_id": plan["manifest_id"],
                "manifest_ref": plan.get("manifest_ref", f"GMOD-CLOSEOUT-{plan['batch_id']}"),
                "batch_id": plan["batch_id"],
                "identity": identity,
                "base_revision": base["revision"],
                "base_checkpoint_id": base["checkpoint_id"],
                "target_checkpoint_id": plan["target_checkpoint_id"],
                "rules_revision": plan["rules_revision"],
                "adapter_revision": plan["adapter_revision"],
                "campaign_rules_revision": plan["campaign_rules_revision"],
                "module_rules_revision": plan["module_rules_revision"],
                "source_event_revision": plan["source_event_revision"],
                "plan_revision": plan["plan_revision"],
                "plan_fingerprint": digest(plan),
                "targets": targets,
                "field_operation_ids": field_operation_ids,
                "required_fields": list(targets),
            }
            record = {"status": "PREPARED", "manifest_ref": manifest["manifest_ref"],
                      "manifest": manifest}
            diagnostics["records"].append(record)
            write_json(self.diagnostics, diagnostics)
            reread = read_json(self.diagnostics)
            matches = [item for item in reread["records"]
                       if item.get("manifest", {}).get("identity") == identity
                       and item.get("status") not in ("SUPERSEDED", "CANCELLED")]
            if len(matches) != 1 or matches[0] != record:
                return {"status": "IDENTITY_UNVERIFIABLE"}
            locator_status = self._repair_runtime_locator(record)
            if locator_status != "OK":
                return {"status": locator_status}
            return {"status": "FOUND", "operation": record}
        finally:
            lock.unlink(missing_ok=True)

    def prepare(self, identity, requested_operation_id, plan):
        operation = self.begin(identity, requested_operation_id, plan)
        if operation["status"] != "FOUND":
            return operation
        return {"status": "PREPARED", "manifest": operation["operation"]["manifest"],
                "record": operation["operation"]}

    def inspect(self, identity):
        discovered = self.discover(identity)
        if discovered["status"] != "FOUND":
            return {"status": discovered["status"]}
        record = discovered["operation"]
        manifest = record.get("manifest")
        if not manifest or record.get("manifest_ref") != manifest.get("manifest_ref"):
            return {"status": "INCOMPLETE", "discovery": "FOUND"}
        base = read_json(self.base)
        state = read_json(self.candidate)
        if base["revision"] != manifest["base_revision"] or state["base_revision"] != manifest["base_revision"]:
            return {"status": "DISPUTED"}
        fields = {}
        for field, target in manifest["targets"].items():
            operation_id = manifest["field_operation_ids"][field]
            matches = [item for item in state["applied_operations"] if item["id"] == operation_id]
            if len(matches) > 1:
                fields[field] = "DISPUTED"
            elif len(matches) == 1:
                fields[field] = ("APPLIED" if matches[0]["field"] == field
                                 and matches[0]["value"] == target
                                 and state["fields"].get(field) == target else "DISPUTED")
            elif state["fields"].get(field) == base["fields"].get(field):
                fields[field] = "NOT_APPLIED"
            else:
                fields[field] = "UNVERIFIABLE"
        publication = "UNPUBLISHED"
        if self.published.exists():
            pointer = read_json(self.published)
            expected = {"operation_id": manifest["operation_id"],
                        "batch_id": manifest["batch_id"],
                        "manifest_fingerprint": digest(manifest),
                        "checkpoint_id": manifest["target_checkpoint_id"]}
            if pointer == expected and all(value == "APPLIED" for value in fields.values()):
                publication = "PUBLISHED"
            elif pointer.get("checkpoint_id") == manifest["base_checkpoint_id"] and not pointer.get("operation_id"):
                publication = "UNPUBLISHED"
            else:
                publication = "DISPUTED"
        if publication == "PUBLISHED":
            status = "PUBLISHED"
        elif publication == "DISPUTED" or any(v in ("DISPUTED", "UNVERIFIABLE") for v in fields.values()):
            status = "DISPUTED"
        else:
            status = "INCOMPLETE"
        return {"status": status, "operation_id": manifest["operation_id"],
                "batch_id": manifest["batch_id"], "fields": fields,
                "publication": publication}

    def apply_field(self, identity, field):
        current = self.inspect(identity)
        if current["status"] in ("PENDING_DISCOVERY", "IDENTITY_CONFLICT", "DISPUTED"):
            return {"status": current["status"], "writes": 0}
        if current["fields"].get(field) == "APPLIED":
            return {"status": "APPLIED", "writes": 0}
        if current["fields"].get(field) != "NOT_APPLIED":
            return {"status": "UNVERIFIABLE", "writes": 0}
        operation = self.discover(identity)["operation"]
        manifest = operation["manifest"]
        state = read_json(self.candidate)
        base = read_json(self.base)
        if state["base_revision"] != manifest["base_revision"] or state["fields"].get(field) != base["fields"].get(field):
            return {"status": "DISPUTED", "writes": 0}
        operation_id = manifest["field_operation_ids"][field]
        state["fields"][field] = manifest["targets"][field]
        state["applied_operations"].append({"id": operation_id, "field": field,
                                            "value": manifest["targets"][field]})
        write_json(self.candidate, state)
        return {"status": "APPLIED", "writes": 1}

    def finish(self, identity, operation_id, plan, fault_after_fields=None, fault=None):
        prepared = self.prepare(identity, operation_id, plan)
        if prepared["status"] != "PREPARED":
            return {"status": prepared["status"], "writes": 0}
        manifest = prepared["manifest"]
        before = self.inspect(identity)
        if before["status"] == "PUBLISHED":
            return {**before, "writes": 0}
        if before["status"] in ("PENDING_DISCOVERY", "IDENTITY_CONFLICT", "DISPUTED"):
            return {**before, "writes": 0}
        writes = 0
        for field in manifest["required_fields"]:
            status = self.inspect(identity)["fields"][field]
            if status == "APPLIED":
                continue
            if status != "NOT_APPLIED":
                return {"status": "DISPUTED", "writes": writes}
            applied = self.apply_field(identity, field)
            if applied["status"] != "APPLIED":
                return {"status": applied["status"], "writes": writes}
            writes += applied["writes"]
            if fault_after_fields is not None and writes == fault_after_fields:
                print(json.dumps({"pid": os.getpid(), "partial_field": field}), flush=True)
                os._exit(73)
        reconciled = self.inspect(identity)
        if reconciled["status"] == "DISPUTED" or any(
                value != "APPLIED" for value in reconciled.get("fields", {}).values()):
            return {**reconciled, "writes": writes}
        base = read_json(self.base)
        prior_pointer = read_json(self.published) if self.published.exists() else None
        if base["revision"] != manifest["base_revision"]:
            return {"status": "DISPUTED", "writes": writes}
        if prior_pointer and prior_pointer.get("checkpoint_id") != manifest["base_checkpoint_id"]:
            return {"status": "DISPUTED", "writes": writes}
        runtime = read_json(self.runtime)
        persistence = runtime.setdefault("persistence", {})
        persistence.update({
            "batch_id": manifest["batch_id"],
            "status": "PUBLISHED",
            "prepare_manifest_ref": manifest["manifest_ref"],
            "previous_published_checkpoint_ref": manifest["base_checkpoint_id"],
            "published_checkpoint_ref": manifest["target_checkpoint_id"],
        })
        refs = persistence.setdefault("reconciliation_manifest_refs", [])
        if manifest["manifest_ref"] not in refs:
            refs.append(manifest["manifest_ref"])
        write_json(self.runtime, runtime)
        pointer = {"operation_id": manifest["operation_id"],
                   "batch_id": manifest["batch_id"],
                   "manifest_fingerprint": digest(manifest),
                   "checkpoint_id": manifest["target_checkpoint_id"]}
        write_json(self.published, pointer)
        if fault == "ack-lost":
            os._exit(74)
        return {**self.inspect(identity), "writes": writes}


def validate_dependency_graph(steps):
    """Return a deterministic topological order; reject missing nodes and cycles."""
    by_id = {item["id"]: item for item in steps}
    if len(by_id) != len(steps):
        raise ValueError("duplicate step id")
    pending = {key: set(item.get("depends_on", [])) for key, item in by_id.items()}
    if any(dep not in by_id for deps in pending.values() for dep in deps):
        raise ValueError("dependency references unknown step")
    order = []
    while pending:
        ready = sorted(key for key, deps in pending.items() if not deps)
        if not ready:
            raise ValueError("dependency cycle")
        for key in ready:
            order.append(key)
            pending.pop(key)
        for deps in pending.values():
            deps.difference_update(ready)
    return order


def fields_known(required_fields, known_fields):
    """Unknown state blocks only actions that explicitly depend on it."""
    return set(required_fields).issubset(set(known_fields))

def _canonical_ref(value):
    """Canonicalize stable identifiers, never free-form natural-language descriptions."""
    if not isinstance(value, str) or not value.strip():
        return None
    return " ".join(value.split()).casefold()


def _remedy_identity(remedy):
    """Return the complete semantic identity; incomplete proposals fail closed."""
    if not isinstance(remedy, dict):
        return None
    fields = ("action_kind", "operation_ref", "target_ref", "scope_ref")
    values = tuple(_canonical_ref(remedy.get(field)) for field in fields)
    atoms = remedy.get("action_atoms")
    if any(value is None for value in values) or not isinstance(atoms, list) or not atoms:
        return None
    canonical_atoms = [_canonical_ref(atom) for atom in atoms]
    if any(atom is None for atom in canonical_atoms):
        return None
    return {"signature": values, "action_atoms": frozenset(canonical_atoms)}


def _declined_action_assessment(candidate, refused):
    """Read a GM-authored comparison of natural-language intent against one refusal."""
    assessments = candidate.get("declined_action_assessments")
    if not isinstance(assessments, list):
        return None
    matches = [item for item in assessments
               if isinstance(item, dict)
               and item.get("declined_remedy_id") == refused.get("remedy_id")]
    if len(matches) != 1:
        return None
    assessment = matches[0]
    relation = assessment.get("relation")
    basis = assessment.get("basis")
    if relation not in ("SAME_ACTION", "CONTAINS_DECLINED_ACTION", "DISTINCT_ACTION", "UNCLEAR"):
        return None
    if not isinstance(basis, str) or not basis.strip():
        return None
    return relation


def _declined_action_relation(candidate, declined_records):
    """Classify a candidate against refusals without conflating HOLD and refusal."""
    identity = _remedy_identity(candidate)
    if identity is None:
        return "UNCLEAR"
    for refused in declined_records:
        prior = _remedy_identity(refused)
        if prior is None:
            return "UNCLEAR"
        if identity["signature"] == prior["signature"]:
            return "BLOCKED"
        if identity["action_atoms"] & prior["action_atoms"]:
            return "BLOCKED"  # Atoms represent prohibited operations/effects, not shared goals.
        derived_signature = candidate.get("derived_from_signature")
        if derived_signature is not None and derived_signature == refused.get("semantic_signature"):
            return "BLOCKED"
        derived_id = candidate.get("derived_from_remedy_id")
        if derived_id is not None and derived_id == refused.get("remedy_id"):
            return "BLOCKED"
        relation = _declined_action_assessment(candidate, refused)
        if relation in ("SAME_ACTION", "CONTAINS_DECLINED_ACTION"):
            return "BLOCKED"
        if relation != "DISTINCT_ACTION":
            return "UNCLEAR"  # Missing, ambiguous, or malformed comparison => clarify.
    return "DISTINCT"


def _same_declined_action(candidate, declined_records):
    """Compatibility predicate for refusal deduplication."""
    return _declined_action_relation(candidate, declined_records) != "DISTINCT"


def route_incident(record, choice):
    """Synthetic policy: semantic refusals persist; alternatives require player inquiry/authorization."""
    private = record["delivery"] in ("INTERNAL_DRAFT", "STAGED_PRIVATE")
    if private and record.get("isolated") and not any(record[k] for k in ("accessed", "executed", "depended")):
        return {"phase": "DRAFT_DISCARDED", "history": record["history"]}
    declined = list(record.get("declined_remedies", []))
    refused = record.get("remedy")
    refusal_status = "NOT_APPLICABLE"
    if choice == "REJECT_REMEDY":
        identity = _remedy_identity(refused)
        if identity is None:
            refusal_status = "INCOMPLETE"
        else:
            refusal_record = {**refused, "semantic_signature": list(identity["signature"]),
                              "action_atoms": sorted(identity["action_atoms"])}
            if not any(_remedy_identity(item) is not None
                       and _same_declined_action(refusal_record, [item]) for item in declined):
                declined.append(refusal_record)
            refusal_status = "RECORDED"
    permission = record.get("player_permission", "NONE")
    may_discuss = permission in ("ASKED", "AUTHORIZED") and refusal_status != "INCOMPLETE"
    proposed = list(record.get("proposed_remedies", []))
    available = []
    clarification_required = []
    if may_discuss:
        for item in proposed:
            relation = _declined_action_relation(item, declined)
            if relation == "DISTINCT":
                available.append(item)
            elif relation == "UNCLEAR":
                clarification_required.append(item)
    status = {"CONTINUE_SAFE_SCOPE": "CONTAINED", "PAUSE_AUDIT": "OPEN",
              "TERMINATE": "TERMINATED"}.get(choice, "OPEN")
    return {"phase": status, "history": record["history"], "affected_advances": 0,
            "player_choice": choice, "declined_remedies": declined,
            "remedy_recording_status": refusal_status,
            "available_remedies": available,
            "clarification_required": clarification_required,
            "allowed_threads": ["safe"] if status == "CONTAINED" else [],
            "notice": "此前的调查依据待核，沿该线继续可能影响后续判断。",
            "choices_offered": ["CONTINUE_SAFE_SCOPE", "PAUSE_AUDIT", "TERMINATE"]}


def projection(root, segments, recipient, forbidden, readable=True, extra=b""):
    """Synthetic plain-text proof, without a platform/real recipient ACL claim."""
    if not readable:
        return "NOT_PUBLISHED"
    private = root / "private"
    private.mkdir(mode=0o700, exist_ok=True)
    public = root / recipient
    body = "\n".join(item["text"] for item in segments
                     if recipient in item["recipients"] and item["delivery"] == "PRESENTED"
                     and item["field"] in ("public_utterance", "public_observation", "player_known_claim"))
    draft = private / "player.txt"
    audit = private / "audit.json"
    draft.write_bytes(body.encode() + extra)
    write_json(audit, {"segments": segments, "recipient": recipient})
    # Read actual output bytes before publishing. Audit is never copied into public.
    import unicodedata
    def normalized(value):
        return unicodedata.normalize("NFKC", value).casefold()
    checked = normalized(draft.read_bytes().decode("utf-8"))
    if any(normalized(item) in checked for item in forbidden):
        return "NOT_PUBLISHED"
    public.mkdir()
    draft.replace(public / "notes.txt")
    return "PUBLISHED"


if __name__ == "__main__":
    root = Path(sys.argv[1])
    command = json.load(sys.stdin)
    if command["op"].startswith("closeout_"):
        closeout = CloseoutBatch(root)
        if command["op"] == "closeout_inspect":
            result = closeout.inspect(command["identity"])
        else:
            result = closeout.finish(command["identity"], command["operation_id"], command["plan"],
                                     command.get("fault_after_fields"), command.get("fault"))
    else:
        batch = Batch(root)
        result = batch.inspect() if command["op"] == "inspect" else batch.finish(command["event"], command.get("fault"))
    print(json.dumps({"pid": os.getpid(), **result}))
