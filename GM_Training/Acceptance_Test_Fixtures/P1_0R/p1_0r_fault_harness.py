#!/usr/bin/env python3
"""Isolated P1-0R crash-injection harness. Synthetic data only; not a product-storage test."""
import hashlib, json, os, pathlib, subprocess, sys, tempfile

ROOT = pathlib.Path(tempfile.mkdtemp(prefix="p1_0r_isolated_"))
MANIFEST = {
    "batch_id": "BATCH-P1-0R-001", "event_id": "EVT-SYNTH-001",
    "event_revision_id": "EVT-SYNTH-001-R1", "base_revision": 5,
    "target_revision": 6, "payload_version": 1,
    "payload": {"synthetic_counter": 1, "item_holder": "Sol"}
}
MANIFEST["payload_fingerprint"] = hashlib.sha256(
    json.dumps(MANIFEST["payload"], sort_keys=True).encode()
).hexdigest()

def atomic_write(path, obj):
    path = pathlib.Path(path)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "wb") as f:
        f.write(json.dumps(obj, sort_keys=True, indent=2).encode())
        f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)
    if hasattr(os, "O_DIRECTORY"):
        dfd = os.open(path.parent, os.O_DIRECTORY)
        try: os.fsync(dfd)
        finally: os.close(dfd)

def read(path):
    with open(path, encoding="utf-8") as f: return json.load(f)

def init_case(d):
    d.mkdir(parents=True)
    atomic_write(d/"prepare_manifest.json", MANIFEST)
    atomic_write(d/"runtime.json", {
        "checkpoint":{"revision":5,"branch":"ACTIVE","can_advance":True,
                      "unapplied_event_ids":[MANIFEST["event_id"]],"applied_event_ids":[]},
        "persistence":{"batch_id":MANIFEST["batch_id"],"status":"PREPARED"},
        "domain_state":{"synthetic_counter":0},"incident_markers":[]})
    atomic_write(d/"session_log.json", {"incidents":[]})

def writer_child(case_dir, mode):
    d=pathlib.Path(case_dir)
    marker={"batch_id":MANIFEST["batch_id"],"event_id":MANIFEST["event_id"],
            "event_revision_id":MANIFEST["event_revision_id"],
            "payload_fingerprint":MANIFEST["payload_fingerprint"]}
    if mode=="runtime_then_crash":
        rt=read(d/"runtime.json")
        rt["checkpoint"]["branch"]="DISPUTED"; rt["checkpoint"]["can_advance"]=False
        rt["persistence"]["status"]="INCOMPLETE"; rt["incident_markers"].append(marker)
        atomic_write(d/"runtime.json",rt)
        os._exit(71)
    if mode=="log_then_crash":
        lg=read(d/"session_log.json"); lg["incidents"].append({**marker,"status":"OPEN"})
        atomic_write(d/"session_log.json",lg)
        os._exit(72)
    if mode=="both_fail":
        os._exit(73)
    raise ValueError(mode)

def recover_child(case_dir):
    d=pathlib.Path(case_dir); m=read(d/"prepare_manifest.json")
    actual=hashlib.sha256(json.dumps(m["payload"],sort_keys=True).encode()).hexdigest()
    if actual!=m["payload_fingerprint"]: raise RuntimeError("PREPARE payload fingerprint mismatch")
    rt=read(d/"runtime.json"); lg=read(d/"session_log.json")
    bid,eid=m["batch_id"],m["event_id"]
    expected={"batch_id":bid,"event_id":eid,"event_revision_id":m["event_revision_id"],
              "payload_fingerprint":m["payload_fingerprint"]}
    r_matches=[x for x in rt.get("incident_markers",[]) if x.get("batch_id")==bid]
    l_matches=[x for x in lg.get("incidents",[]) if x.get("batch_id")==bid]
    if any(x!=expected for x in r_matches): raise RuntimeError("Runtime marker identity/version conflict")
    if any(any(x.get(k)!=v for k,v in expected.items()) for x in l_matches):
        raise RuntimeError("Log marker identity/version conflict")
    if not r_matches: rt.setdefault("incident_markers",[]).append(expected)
    rt["checkpoint"]["branch"]="DISPUTED"; rt["checkpoint"]["can_advance"]=False
    rt["persistence"]["status"]="INCOMPLETE"
    rt["reconciliation"]={"batch_id":bid,"source":"PREPARE_MANIFEST",
                          "action":"APPEND_MISSING_DISPUTE_MARKERS_ONLY",
                          "domain_event_replayed":False}
    atomic_write(d/"runtime.json",rt)
    if not l_matches:
        lg.setdefault("incidents",[]).append({**expected,"status":"OPEN","recovered_from":"PREPARE_MANIFEST"})
        atomic_write(d/"session_log.json",lg)
    # Independent disk readback from this fresh recovery process.
    rt2,lg2=read(d/"runtime.json"),read(d/"session_log.json")
    return {"runtime_marker_count":sum(x.get("batch_id")==bid for x in rt2["incident_markers"]),
            "log_marker_count":sum(x.get("batch_id")==bid and x.get("event_id")==eid for x in lg2["incidents"]),
            "branch":rt2["checkpoint"]["branch"],"can_advance":rt2["checkpoint"]["can_advance"],
            "persistence_status":rt2["persistence"]["status"],"revision":rt2["checkpoint"]["revision"],
            "domain_state":rt2["domain_state"],"applied_event_ids":rt2["checkpoint"]["applied_event_ids"],
            "unapplied_event_ids":rt2["checkpoint"]["unapplied_event_ids"]}

def run_case(name,mode):
    d=ROOT/name; init_case(d)
    writer=subprocess.run([sys.executable,__file__,"writer",str(d),mode],check=False)
    first=subprocess.run([sys.executable,__file__,"recover",str(d)],capture_output=True,text=True,check=True)
    second=subprocess.run([sys.executable,__file__,"recover",str(d)],capture_output=True,text=True,check=True)
    a,b=json.loads(first.stdout),json.loads(second.stdout)
    assert writer.returncode in (71,72,73)
    for state in (a,b):
        assert state["runtime_marker_count"]==1 and state["log_marker_count"]==1,state
        assert state["branch"]=="DISPUTED" and state["can_advance"] is False,state
        assert state["persistence_status"]=="INCOMPLETE" and state["revision"]==5,state
        assert state["domain_state"]=={"synthetic_counter":0},state
        assert state["applied_event_ids"]==[] and state["unapplied_event_ids"]==[MANIFEST["event_id"]],state
    return {"case":name,"injected_mode":mode,"writer_exit_code":writer.returncode,
            "after_first_cold_recovery":a,"after_second_cold_recovery":b,"assertions":"PASS"}

if __name__=="__main__":
    if len(sys.argv)>1 and sys.argv[1]=="writer": writer_child(sys.argv[2],sys.argv[3])
    elif len(sys.argv)>1 and sys.argv[1]=="recover": print(json.dumps(recover_child(sys.argv[2])))
    else:
        results=[run_case("A_runtime_success_log_failure","runtime_then_crash"),
                 run_case("B_log_success_runtime_failure","log_then_crash"),
                 run_case("C_both_targets_fail","both_fail")]
        print(json.dumps({"harness":"P1-0R isolated filesystem crash-injection",
                          "results":results,"overall":"PASS"},indent=2))
