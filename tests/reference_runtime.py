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


def route_incident(record, choice):
    """Reference policy driven by delivery evidence, including unresolved receipts."""
    private = record["delivery"] in ("INTERNAL_DRAFT", "STAGED_PRIVATE")
    if private and record.get("isolated") and not any(record[k] for k in ("accessed", "executed", "depended")):
        return {"phase": "DRAFT_DISCARDED", "history": record["history"]}
    status = {"CONTINUE_SAFE_SCOPE": "CONTAINED", "PAUSE_AUDIT": "OPEN",
              "TERMINATE": "TERMINATED"}.get(choice, "OPEN")
    return {"phase": status, "history": record["history"], "affected_advances": 0,
            "player_choice": choice, "allowed_threads": ["safe"] if status == "CONTAINED" else [],
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
    batch = Batch(root)
    command = json.load(sys.stdin)
    result = batch.inspect() if command["op"] == "inspect" else batch.finish(command["event"], command.get("fault"))
    print(json.dumps({"pid": os.getpid(), **result}))
