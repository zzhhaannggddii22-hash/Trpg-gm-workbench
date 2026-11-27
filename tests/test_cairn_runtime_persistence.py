"""Test-only filesystem adapter contract for Cairn Runtime persistence.

This is deliberately NOT the production GM Runtime or a platform storage adapter.
It exercises the minimum durable transaction contract with real temporary files,
atomic replace, cold-process restart, and deterministic crash injection.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


def _canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def _fingerprint(value):
    return hashlib.sha256(_canonical(value)).hexdigest()


def _read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def _atomic_write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    data = _canonical(value)
    with temp.open("wb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temp, path)
    # Directory fsync makes the rename durable on the POSIX CI host.
    descriptor = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


class CairnPersistenceContract:
    """Minimal write-ahead manifest + per-target idempotency ledger."""

    def __init__(self, root):
        self.root = Path(root)
        self.journal = self.root / "journal"
        self.targets = self.root / "targets"

    def manifest_path(self, event_id):
        return self.journal / (event_id + ".json")

    def target_path(self, target_id):
        return self.targets / (target_id + ".json")

    def seed_target(self, target_id, state):
        path = self.target_path(target_id)
        if path.exists():
            raise ValueError("target already exists")
        _atomic_write(path, {"state": state, "applied_events": {}})

    def prepare(self, event):
        event_id = event["event_id"]
        path = self.manifest_path(event_id)
        frozen = {
            "event_id": event_id,
            "event_kind": event["event_kind"],
            "targets": event["targets"],
            "metadata": event.get("metadata", {}),
        }
        fingerprint = _fingerprint(frozen)
        if path.exists():
            old = _read(path)
            if old["fingerprint"] != fingerprint or old["event"] != frozen:
                raise ValueError("event identity reused with different payload")
            return old
        manifest = {
            "event": frozen,
            "fingerprint": fingerprint,
            "status": "PREPARED",
            "prepared": True,
        }
        _atomic_write(path, manifest)
        if _read(path) != manifest:
            raise IOError("prepare manifest readback mismatch")
        return manifest

    def inspect(self, event_id):
        path = self.manifest_path(event_id)
        if not path.exists():
            return {"status": "NOT_PREPARED", "targets": {}}
        manifest = _read(path)
        fingerprint = manifest["fingerprint"]
        statuses = {}
        for target_id, transition in manifest["event"]["targets"].items():
            target_path = self.target_path(target_id)
            if not target_path.exists():
                statuses[target_id] = "MISSING"
                continue
            record = _read(target_path)
            applied = record["applied_events"].get(event_id)
            if applied is not None:
                statuses[target_id] = (
                    "APPLIED" if applied == fingerprint and
                    all(record["state"].get(k) == v for k, v in transition["after"].items())
                    else "DISPUTED"
                )
            elif all(record["state"].get(k) == v for k, v in transition["before"].items()):
                statuses[target_id] = "NOT_APPLIED"
            else:
                statuses[target_id] = "DISPUTED"
        if manifest["status"] == "COMMITTED":
            status = "COMMITTED" if statuses and set(statuses.values()) == {"APPLIED"} else "DISPUTED"
        elif "DISPUTED" in statuses.values():
            status = "DISPUTED"
        else:
            status = "INCOMPLETE"
        return {"status": status, "targets": statuses, "fingerprint": fingerprint}

    def apply_target(self, event_id, target_id):
        manifest = _read(self.manifest_path(event_id))
        transition = manifest["event"]["targets"][target_id]
        record = _read(self.target_path(target_id))
        prior = record["applied_events"].get(event_id)
        if prior is not None:
            if prior == manifest["fingerprint"] and all(
                    record["state"].get(k) == v for k, v in transition["after"].items()):
                return {"status": "APPLIED", "writes": 0}
            return {"status": "DISPUTED", "writes": 0}
        if not all(record["state"].get(k) == v for k, v in transition["before"].items()):
            return {"status": "DISPUTED", "writes": 0}
        record["state"].update(transition["after"])
        record["applied_events"][event_id] = manifest["fingerprint"]
        _atomic_write(self.target_path(target_id), record)
        reread = _read(self.target_path(target_id))
        if reread != record:
            return {"status": "UNVERIFIABLE", "writes": 1}
        return {"status": "APPLIED", "writes": 1}

    def commit(self, event, fault=None):
        manifest = self.prepare(event)
        event_id = event["event_id"]
        if fault == "after_prepare":
            os._exit(70)

        current = self.inspect(event_id)
        if current["status"] == "COMMITTED":
            return {"status": "COMMITTED", "writes": 0}
        if current["status"] == "DISPUTED":
            return {"status": "DISPUTED", "writes": 0}

        writes = 0
        for index, target_id in enumerate(manifest["event"]["targets"]):
            status = self.inspect(event_id)["targets"][target_id]
            if status == "APPLIED":
                continue
            if status != "NOT_APPLIED":
                return {"status": "DISPUTED", "writes": writes}
            result = self.apply_target(event_id, target_id)
            if result["status"] != "APPLIED":
                return {"status": result["status"], "writes": writes + result["writes"]}
            writes += result["writes"]
            if fault == "after_first_target" and writes == 1:
                os._exit(71)

        reconciled = self.inspect(event_id)
        if set(reconciled["targets"].values()) != {"APPLIED"}:
            return {"status": reconciled["status"], "writes": writes}

        manifest = _read(self.manifest_path(event_id))
        manifest["status"] = "COMMITTED"
        manifest["committed_target_fingerprints"] = {
            target_id: _fingerprint(_read(self.target_path(target_id)))
            for target_id in manifest["event"]["targets"]
        }
        _atomic_write(self.manifest_path(event_id), manifest)
        if self.inspect(event_id)["status"] != "COMMITTED":
            return {"status": "UNVERIFIABLE", "writes": writes}
        if fault == "after_commit_before_ack":
            os._exit(72)
        return {"status": "COMMITTED", "writes": writes}


def _worker(root, event, fault):
    result = CairnPersistenceContract(root).commit(event, fault=fault)
    print(json.dumps(result, sort_keys=True))


class CairnPersistenceContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.store = CairnPersistenceContract(self.root)

    def tearDown(self):
        self.temp.cleanup()

    def _spawn(self, event, fault):
        command = (
            "import json,sys; "
            f"sys.path.insert(0, {str(Path(__file__).resolve().parent)!r}); "
            "from test_cairn_runtime_persistence import _worker; "
            f"_worker({str(self.root)!r}, json.loads({json.dumps(json.dumps(event))}), {fault!r})"
        )
        return subprocess.run([sys.executable, "-c", command], capture_output=True, text=True)

    def _single_event(self):
        self.store.seed_target("pc-1", {"hp": 8, "max_hp": 8})
        return {
            "event_id": "cairn-event-001",
            "event_kind": "scar_resolution",
            "targets": {
                "pc-1": {
                    "before": {"hp": 8, "max_hp": 8},
                    "after": {"hp": 8, "max_hp": 12},
                }
            },
            "metadata": {"effect_id": "walloped-001", "resolution_event_id": "cairn-event-001"},
        }

    def test_prepared_manifest_survives_cold_restart_and_commits_once(self):
        event = self._single_event()
        interrupted = self._spawn(event, "after_prepare")
        self.assertEqual(interrupted.returncode, 70)
        self.assertEqual(self.store.inspect(event["event_id"])["status"], "INCOMPLETE")

        recovered = self._spawn(event, None)
        self.assertEqual(recovered.returncode, 0, recovered.stderr)
        self.assertIn('"status": "COMMITTED"', recovered.stdout)
        self.assertEqual(self.store.inspect(event["event_id"])["status"], "COMMITTED")
        state = _read(self.store.target_path("pc-1"))["state"]
        self.assertEqual(state["max_hp"], 12)

        replay = self.store.commit(event)
        self.assertEqual(replay, {"status": "COMMITTED", "writes": 0})
        self.assertEqual(_read(self.store.target_path("pc-1"))["state"]["max_hp"], 12)

    def test_blast_partial_target_commit_recovers_only_missing_target(self):
        self.store.seed_target("target-a", {"hp": 5, "str": 10})
        self.store.seed_target("target-b", {"hp": 1, "str": 5})
        event = {
            "event_id": "blast-event-001",
            "event_kind": "blast_damage",
            "targets": {
                "target-a": {
                    "before": {"hp": 5, "str": 10},
                    "after": {"hp": 2, "str": 10},
                },
                "target-b": {
                    "before": {"hp": 1, "str": 5},
                    "after": {"hp": 0, "str": 4},
                },
            },
            "metadata": {"blast_id": "blast-001"},
        }
        interrupted = self._spawn(event, "after_first_target")
        self.assertEqual(interrupted.returncode, 71)
        partial = self.store.inspect(event["event_id"])
        self.assertEqual(partial["status"], "INCOMPLETE")
        self.assertEqual(partial["targets"], {"target-a": "APPLIED", "target-b": "NOT_APPLIED"})

        recovered = self.store.commit(event)
        self.assertEqual(recovered, {"status": "COMMITTED", "writes": 1})
        self.assertEqual(self.store.inspect(event["event_id"])["status"], "COMMITTED")
        self.assertEqual(_read(self.store.target_path("target-a"))["state"]["hp"], 2)
        self.assertEqual(_read(self.store.target_path("target-b"))["state"], {"hp": 0, "str": 4})

        replay = self.store.commit(event)
        self.assertEqual(replay, {"status": "COMMITTED", "writes": 0})
        self.assertEqual(len(_read(self.store.target_path("target-a"))["applied_events"]), 1)
        self.assertEqual(len(_read(self.store.target_path("target-b"))["applied_events"]), 1)

    def test_pending_effect_consumption_is_idempotent_after_lost_ack(self):
        self.store.seed_target("pc-1", {
            "max_hp": 8,
            "pending_effects": {"walloped-001": {"status": "ready"}},
        })
        event = {
            "event_id": "walloped-resolution-001",
            "event_kind": "pending_effect_resolution",
            "targets": {
                "pc-1": {
                    "before": {
                        "max_hp": 8,
                        "pending_effects": {"walloped-001": {"status": "ready"}},
                    },
                    "after": {
                        "max_hp": 12,
                        "pending_effects": {"walloped-001": {
                            "status": "consumed",
                            "resolution_event_id": "walloped-resolution-001",
                        }},
                    },
                }
            },
            "metadata": {
                "effect_id": "walloped-001",
                "source_event_id": "scar-event-001",
                "resolution_event_id": "walloped-resolution-001",
                "roll": 4,
            },
        }
        interrupted = self._spawn(event, "after_commit_before_ack")
        self.assertEqual(interrupted.returncode, 72)
        self.assertEqual(self.store.inspect(event["event_id"])["status"], "COMMITTED")

        replay = self.store.commit(event)
        self.assertEqual(replay, {"status": "COMMITTED", "writes": 0})
        state = _read(self.store.target_path("pc-1"))["state"]
        self.assertEqual(state["max_hp"], 12)
        self.assertEqual(state["pending_effects"]["walloped-001"]["status"], "consumed")
        self.assertEqual(
            state["pending_effects"]["walloped-001"]["resolution_event_id"],
            "walloped-resolution-001",
        )

    def test_event_id_cannot_be_reused_for_a_different_payload(self):
        event = self._single_event()
        self.store.prepare(event)
        changed = {**event, "metadata": {"effect_id": "different-effect"}}
        with self.assertRaisesRegex(ValueError, "reused with different payload"):
            self.store.prepare(changed)

    def test_unexplained_target_change_fails_closed(self):
        event = self._single_event()
        self.store.prepare(event)
        target = _read(self.store.target_path("pc-1"))
        target["state"]["max_hp"] = 9
        _atomic_write(self.store.target_path("pc-1"), target)
        result = self.store.commit(event)
        self.assertEqual(result["status"], "DISPUTED")
        self.assertEqual(_read(self.store.target_path("pc-1"))["state"]["max_hp"], 9)


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "--worker":
        _worker(sys.argv[2], json.loads(sys.argv[3]), None)
    else:
        unittest.main()
