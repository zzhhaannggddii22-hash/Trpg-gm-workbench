#!/usr/bin/env python3
"""Synthetic reference adapter for roll-result persistence conformance tests.

This is not a production ChatGPT/Workbench storage connector. It models the
repository's existing Resource Ledger, Session Log, Runtime checkpoint and
immutable-manifest contracts on a local filesystem.
"""
from __future__ import annotations
import hashlib, json, os, pathlib, tempfile
from typing import Any

PLAYER_FIELDS = {"kind", "headline", "result", "dice", "choices", "resource_changes", "current_resources", "narrative", "pending_notice"}
FORBIDDEN_PLAYER_KEYS = {"event_id", "event_revision_id", "batch_id", "manifest_id", "ledger_entry_id", "gm_only", "audit", "internal_notes", "source_document", "hidden_truth"}

def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()

def fingerprint(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()

def atomic_json(path: pathlib.Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "wb") as f:
        f.write(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2).encode())
        f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)
    if hasattr(os, "O_DIRECTORY"):
        fd = os.open(path.parent, os.O_DIRECTORY)
        try: os.fsync(fd)
        finally: os.close(fd)

def read_json(path: pathlib.Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def read_jsonl(path: pathlib.Path) -> list[dict]:
    if not path.exists(): return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]

def append_once(path: pathlib.Path, key: str, value: dict) -> None:
    rows = read_jsonl(path)
    matches = [x for x in rows if x.get("idempotency_key") == key]
    if matches:
        if len(matches) != 1 or matches[0] != value: raise RuntimeError("IDEMPOTENCY_CONFLICT")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "ab") as f:
        f.write(canonical(value) + b"\n"); f.flush(); os.fsync(f.fileno())

class SimulatedCrash(RuntimeError): pass

class RollRuntimeAdapter:
    def __init__(self, root: pathlib.Path):
        self.root=root; self.ledger=root/"resource_ledger.jsonl"; self.log=root/"session_log.jsonl"
        self.runtime=root/"runtime_state.json"; self.prepares=root/"prepare"; self.manifests=root/"manifests"
        self.projection=root/"player_reply_payload.json"

    @classmethod
    def initialize(cls, root: pathlib.Path, balances: dict[str,int]):
        root.mkdir(parents=True,exist_ok=True); obj=cls(root)
        atomic_json(obj.runtime,{"checkpoint":{"revision":10,"branch":"ACTIVE","can_advance":True,
            "applied_event_ids":[],"reconciliation_manifest_refs":[]},"persistence":{"status":"VERIFIED","disputes":[]},
            "resource_balance_location":"RESOURCE_LEDGER_ONLY"})
        atomic_json(root/"resource_snapshot.json",{"revision":10,"balances":balances})
        return obj

    def prepare(self,event:dict)->dict:
        required={"event_id","event_revision_id","batch_id","base_revision","target_revision","payload_version","resource_deltas","player_reply_payload"}
        if not required.issubset(event): raise ValueError("EVENT_ENVELOPE_INCOMPLETE")
        if event["target_revision"]!=event["base_revision"]+1: raise ValueError("REVISION_NOT_SEQUENTIAL")
        payload={k:event[k] for k in ("resource_deltas","player_reply_payload")}
        prep={"batch_id":event["batch_id"],"event_id":event["event_id"],"event_revision_id":event["event_revision_id"],
              "base_revision":event["base_revision"],"target_revision":event["target_revision"],
              "payload_version":event["payload_version"],"payload":payload,"payload_fingerprint":fingerprint(payload)}
        path=self.prepares/f"{event['batch_id']}.json"
        if path.exists() and read_json(path)!=prep: raise RuntimeError("PREPARE_IDENTITY_CONFLICT")
        if not path.exists(): atomic_json(path,prep)
        return prep

    @staticmethod
    def crash(requested,point):
        if requested==point: raise SimulatedCrash(point)

    @staticmethod
    def sanitize(payload:dict)->dict:
        if not isinstance(payload,dict): raise ValueError("PLAYER_PAYLOAD_NOT_OBJECT")
        leaked=set(payload)&FORBIDDEN_PLAYER_KEYS; unknown=set(payload)-PLAYER_FIELDS
        if leaked or unknown: raise ValueError(f"PLAYER_PROJECTION_REJECTED: forbidden={sorted(leaked)} unknown={sorted(unknown)}")
        encoded=canonical(payload).decode()
        if any(k in encoded for k in FORBIDDEN_PLAYER_KEYS): raise ValueError("PLAYER_PROJECTION_CONTENT_LEAK")
        return payload

    def apply(self,event:dict,crash_at=None)->dict:
        rt=read_json(self.runtime)
        if event["event_id"] in rt["checkpoint"]["applied_event_ids"]:
            self.verify(event); return {"status":"IDEMPOTENT_REPLAY"}
        if rt["checkpoint"]["branch"]!="ACTIVE" or not rt["checkpoint"]["can_advance"]: raise RuntimeError("CHECKPOINT_NOT_ADVANCEABLE")
        if rt["checkpoint"]["revision"]!=event["base_revision"]: raise RuntimeError("BASE_REVISION_MISMATCH")
        # Validate the player-facing projection before any domain/resource write.
        safe_projection=self.sanitize(event["player_reply_payload"])
        prep=self.prepare(event); self.crash(crash_at,"AFTER_PREPARE")
        baseline=read_json(self.root/"resource_snapshot.json")["balances"]; history=read_jsonl(self.ledger); entry_ids=[]
        for field,delta in sorted(event["resource_deltas"].items()):
            if field not in baseline: raise RuntimeError("UNKNOWN_RESOURCE_FIELD")
            before=baseline[field]
            for old in [x for x in history if x["resource_field"]==field]:
                if old["before"]!=before: raise RuntimeError("LEDGER_CHAIN_DISPUTED")
                before=old["after"]
            entry_id=f"{event['event_revision_id']}::{field}"
            entry={"idempotency_key":entry_id,"entry_id":entry_id,"event_id":event["event_id"],
                   "event_revision_id":event["event_revision_id"],"resource_field":field,"before":before,
                   "delta":delta,"after":before+delta,"application_status":"APPLIED"}
            append_once(self.ledger,entry_id,entry); entry_ids.append(entry_id)
        self.crash(crash_at,"AFTER_LEDGER")
        log={"idempotency_key":event["event_revision_id"],"event_id":event["event_id"],
             "event_revision_id":event["event_revision_id"],"runtime_application":{"status":"APPLIED",
             "applied_to_revision":event["target_revision"],"ledger_entry_ids":entry_ids}}
        append_once(self.log,event["event_revision_id"],log); self.crash(crash_at,"AFTER_SESSION_LOG")
        rt=read_json(self.runtime); rt["checkpoint"]["revision"]=event["target_revision"]
        rt["checkpoint"]["applied_event_ids"].append(event["event_id"]); rt["persistence"]["status"]="INCOMPLETE"
        atomic_json(self.runtime,rt); self.crash(crash_at,"AFTER_RUNTIME_CHECKPOINT")
        rows=[x for x in read_jsonl(self.ledger) if x["event_revision_id"]==event["event_revision_id"]]
        manifest={"manifest_id":f"MANIFEST::{event['batch_id']}","manifest_version":1,"batch_id":event["batch_id"],
            "base_revision":event["base_revision"],"target_revision":event["target_revision"],
            "ordered_applications":[{"event_id":event["event_id"],"event_revision_id":event["event_revision_id"],
             "payload_version":event["payload_version"],"payload_fingerprint":prep["payload_fingerprint"],"sequence":1,
             "applied_fields":[{"object_id":"RESOURCE_LEDGER","field_path":f"resources.{x['resource_field']}",
                "before_value_ref":fingerprint(x["before"]),"after_value_ref":fingerprint(x["after"])} for x in rows],
             "application_status":"APPLIED","source_event_ref":event["event_revision_id"]}],"manifest_fingerprint":None}
        manifest["manifest_fingerprint"]=fingerprint({k:v for k,v in manifest.items() if k!="manifest_fingerprint"})
        mp=self.manifests/f"MANIFEST__{event['batch_id']}.json"
        if mp.exists() and read_json(mp)!=manifest: raise RuntimeError("IMMUTABLE_MANIFEST_CONFLICT")
        if not mp.exists(): atomic_json(mp,manifest)
        self.crash(crash_at,"AFTER_MANIFEST")
        rt=read_json(self.runtime); rt["checkpoint"]["reconciliation_manifest_refs"].append(manifest["manifest_id"])
        rt["persistence"]["status"]="VERIFIED"; atomic_json(self.runtime,rt)
        self.crash(crash_at,"AFTER_RUNTIME_MANIFEST_LINK")
        atomic_json(self.projection,safe_projection)
        self.crash(crash_at,"AFTER_PROJECTION")
        self.verify(event)
        return {"status":"APPLIED","manifest_id":manifest["manifest_id"],"ledger_entries":len(rows)}

    def verify(self,event):
        rt=read_json(self.runtime)
        prep_path=self.prepares/f"{event['batch_id']}.json"
        if not prep_path.exists(): raise RuntimeError("PREPARE_MANIFEST_MISSING")
        prep=read_json(prep_path)
        payload={k:event[k] for k in ("resource_deltas","player_reply_payload")}
        if (prep["event_id"]!=event["event_id"] or prep["event_revision_id"]!=event["event_revision_id"]
            or prep["payload_fingerprint"]!=fingerprint(payload)):
            raise RuntimeError("EVENT_PAYLOAD_IDENTITY_CONFLICT")
        rows=[x for x in read_jsonl(self.ledger) if x["event_revision_id"]==event["event_revision_id"]]
        logs=[x for x in read_jsonl(self.log) if x["event_revision_id"]==event["event_revision_id"]]
        mp=self.manifests/f"MANIFEST__{event['batch_id']}.json"
        if event["event_id"] not in rt["checkpoint"]["applied_event_ids"] or len(logs)!=1 or not mp.exists(): raise RuntimeError("APPLICATION_PROOF_INCOMPLETE")
        m=read_json(mp)
        if m["manifest_id"] not in rt["checkpoint"]["reconciliation_manifest_refs"]: raise RuntimeError("MANIFEST_NOT_LINKED_FROM_CHECKPOINT")
        if m["base_revision"]!=event["base_revision"] or m["target_revision"]!=event["target_revision"]: raise RuntimeError("MANIFEST_REVISION_MISMATCH")
        if m["manifest_fingerprint"]!=fingerprint({k:v for k,v in m.items() if k!="manifest_fingerprint"}): raise RuntimeError("MANIFEST_FINGERPRINT_MISMATCH")
        app=m["ordered_applications"][0]
        if app["payload_fingerprint"]!=prep["payload_fingerprint"] or app["payload_version"]!=event["payload_version"]: raise RuntimeError("MANIFEST_PAYLOAD_MISMATCH")
        if len(rows)!=len(event["resource_deltas"]) or any(x["application_status"]!="APPLIED" or x["after"]!=x["before"]+x["delta"] for x in rows): raise RuntimeError("LEDGER_FIELD_OR_ARITHMETIC_MISMATCH")
        fields={x["field_path"]:x for x in app["applied_fields"]}
        if set(fields)!={f"resources.{k}" for k in event["resource_deltas"]}: raise RuntimeError("MANIFEST_FIELD_SET_MISMATCH")
        if sorted(logs[0]["runtime_application"]["ledger_entry_ids"])!=sorted(x["entry_id"] for x in rows): raise RuntimeError("SESSION_LOG_LEDGER_REFERENCE_MISMATCH")
        for entry in rows:
            proof=fields[f"resources.{entry['resource_field']}"]
            if proof["before_value_ref"]!=fingerprint(entry["before"]) or proof["after_value_ref"]!=fingerprint(entry["after"]):
                raise RuntimeError("MANIFEST_VALUE_REFERENCE_MISMATCH")
        baseline=read_json(self.root/"resource_snapshot.json")["balances"]
        for field,value in baseline.items():
            for prior in [x for x in read_jsonl(self.ledger) if x["resource_field"]==field]:
                if prior["before"]!=value or prior["after"]!=prior["before"]+prior["delta"]:
                    raise RuntimeError("LEDGER_CHAIN_DISPUTED")
                value=prior["after"]
        if rt["checkpoint"]["revision"]!=event["target_revision"] or rt["persistence"]["status"]!="VERIFIED": raise RuntimeError("CHECKPOINT_NOT_VERIFIED")
        if self.projection.exists(): self.sanitize(read_json(self.projection))
        return {"ledger_entries":len(rows),"session_log_events":len(logs),"revision":rt["checkpoint"]["revision"],
                "projection":"VERIFIED" if self.projection.exists() else "REBUILDABLE_FROM_PREPARE"}

    def cold_recover(self,event):
        try:
            proof=self.verify(event)
            if not self.projection.exists():
                prep=read_json(self.prepares/f"{event['batch_id']}.json")
                atomic_json(self.projection,self.sanitize(prep["payload"]["player_reply_payload"]))
            proof["projection"]="VERIFIED"
            return {"status":"RECOVERED_VERIFIED",**proof}
        except Exception as exc:
            rt=read_json(self.runtime); rt["checkpoint"]["branch"]="DISPUTED"; rt["checkpoint"]["can_advance"]=False
            rt["persistence"]["status"]="INCOMPLETE"
            dispute={"batch_id":event["batch_id"],"event_id":event["event_id"],"event_revision_id":event["event_revision_id"],
                     "reason":str(exc),"domain_event_replayed":False}
            if dispute not in rt["persistence"]["disputes"]: rt["persistence"]["disputes"].append(dispute)
            atomic_json(self.runtime,rt)
            return {"status":"DISPUTED","reason":str(exc),"domain_event_replayed":False,
                    "ledger_entries":len([x for x in read_jsonl(self.ledger) if x["event_revision_id"]==event["event_revision_id"]])}

def event():
    return {"event_id":"EVT-ROLL-001","event_revision_id":"EVT-ROLL-001-R1","batch_id":"BATCH-ROLL-001",
        "base_revision":10,"target_revision":11,"payload_version":1,"resource_deltas":{"empathy_qa":2,"chaos":0},
        "player_reply_payload":{"kind":"ROLL_RESULT","headline":"请求成功","result":"成功","dice":[3,3,3,2,4,1],
        "choices":["All Hands","Circle Back","Employee of the Moment"],"resource_changes":[{"field":"empathy_qa","delta":2}],
        "current_resources":{"empathy_qa":4},"narrative":"门禁应声打开。"},"gm_only":{"hidden_truth":"DO_NOT_LEAK"}}

def run_tests():
    out=[]
    with tempfile.TemporaryDirectory() as td:
        a=RollRuntimeAdapter.initialize(pathlib.Path(td),{"empathy_qa":2,"chaos":0}); e=event()
        assert a.apply(e)["status"]=="APPLIED" and a.apply(e)["status"]=="IDEMPOTENT_REPLAY"
        assert len(read_jsonl(a.ledger))==2 and "balances" not in read_json(a.runtime)
        out.append("commit + duplicate delivery")
    points=["AFTER_PREPARE","AFTER_LEDGER","AFTER_SESSION_LOG","AFTER_RUNTIME_CHECKPOINT","AFTER_MANIFEST","AFTER_RUNTIME_MANIFEST_LINK","AFTER_PROJECTION"]
    for point in points:
        with tempfile.TemporaryDirectory() as td:
            a=RollRuntimeAdapter.initialize(pathlib.Path(td),{"empathy_qa":2,"chaos":0}); e=event()
            try: a.apply(e,point)
            except SimulatedCrash: pass
            else: raise AssertionError("crash injection did not fire")
            one=a.cold_recover(e); two=a.cold_recover(e)
            expected="RECOVERED_VERIFIED" if point in ("AFTER_RUNTIME_MANIFEST_LINK","AFTER_PROJECTION") else "DISPUTED"
            assert one["status"]==expected and two["status"]==expected,(point,one,two)
            rt=read_json(a.runtime)
            if expected=="DISPUTED": assert rt["checkpoint"]["branch"]=="DISPUTED" and not rt["checkpoint"]["can_advance"]
            else: assert a.projection.exists()
            assert len([x for x in read_jsonl(a.ledger) if x["event_revision_id"]==e["event_revision_id"]])<=2
            out.append("crash recovery "+point)
    with tempfile.TemporaryDirectory() as td:
        a=RollRuntimeAdapter.initialize(pathlib.Path(td),{"empathy_qa":2,"chaos":0}); e=event()
        e["player_reply_payload"]["event_id"]="GM-SECRET"
        try: a.apply(e)
        except ValueError as exc: assert "PLAYER_PROJECTION_REJECTED" in str(exc)
        else: raise AssertionError("projection leak accepted")
        assert not a.projection.exists()
        rt=read_json(a.runtime); assert rt["checkpoint"]["revision"]==10 and rt["checkpoint"]["applied_event_ids"]==[]
        assert len(read_jsonl(a.ledger))==0 and len(read_jsonl(a.log))==0
        out.append("player projection leak rejected before domain writes")
    with tempfile.TemporaryDirectory() as td:
        a=RollRuntimeAdapter.initialize(pathlib.Path(td),{"empathy_qa":2,"chaos":0}); e=event(); a.apply(e)
        e2=event(); e2.update({"event_id":"EVT-ROLL-002","event_revision_id":"EVT-ROLL-002-R1","batch_id":"BATCH-ROLL-002",
            "base_revision":11,"target_revision":12,"resource_deltas":{"empathy_qa":-1}})
        a.apply(e2); rows=[x for x in read_jsonl(a.ledger) if x["resource_field"]=="empathy_qa"]
        assert [(x["before"],x["delta"],x["after"]) for x in rows]==[(2,2,4),(4,-1,3)]
        out.append("sequential Resource Ledger chain")
    with tempfile.TemporaryDirectory() as td:
        a=RollRuntimeAdapter.initialize(pathlib.Path(td),{"empathy_qa":2,"chaos":0}); e=event(); a.apply(e)
        altered=event(); altered["resource_deltas"]["empathy_qa"]=99
        try: a.apply(altered)
        except RuntimeError as exc: assert "EVENT_PAYLOAD_IDENTITY_CONFLICT" in str(exc)
        else: raise AssertionError("same event identity with changed payload accepted")
        assert len(read_jsonl(a.ledger))==2
        out.append("changed-payload duplicate rejected without reapplication")
    with tempfile.TemporaryDirectory() as td:
        a=RollRuntimeAdapter.initialize(pathlib.Path(td),{"empathy_qa":2,"chaos":0}); e=event()
        e["base_revision"]=9; e["target_revision"]=10
        try: a.apply(e)
        except RuntimeError as exc: assert "BASE_REVISION_MISMATCH" in str(exc)
        else: raise AssertionError("stale revision accepted")
        out.append("stale base revision rejected")
    return {"harness":"synthetic_roll_runtime_application_adapter_v1","test_count":len(out),"passed":len(out),"failed":0,"overall":"PASS","cases":out}

if __name__=="__main__": print(json.dumps(run_tests(),ensure_ascii=False,indent=2))
