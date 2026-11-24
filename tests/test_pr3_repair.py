"""Repository checks and explicit test-only reference exercises."""
from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile
import unittest

import yaml

from navigation import scan_links
from reference_runtime import projection, route_incident, write_json


ROOT = Path(__file__).resolve().parents[1]
BASE = "6c6109202d92d7bbacd638d5aa37d00418262d2b"
GM = "GM_Training/"
ND = "Campaigns/Zarek/模组/俯冲_Nosedive/"
WORKER = Path(__file__).with_name("reference_runtime.py")


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def metadata(text):
    match = re.search(r"^```yaml\s*\n(.*?)^```", text, re.M | re.S)
    return yaml.safe_load(match[1]) if match else {}


def registry_route(registry, binding, load_entry):
    """Reference use of the actual registry data, including exact case."""
    if not binding or binding.get("status") != "active":
        return "HOLD"
    entries = [entry for entry in registry if entry["system_id"] == binding["system_id"]]
    if len(entries) != 1:
        return "HOLD"
    item = entries[0]
    if item["status"] != "active" or binding["system_entry"] != item["system_entry"]:
        return "HOLD"
    path = PurePosixPath(item["system_entry"])
    if not path.parts or path.parts[0] != "Systems" or ".." in path.parts:
        return "HOLD"
    target = load_entry(str(path))
    edition = binding["ruleset"]["edition"]
    if (not target or target["system_id"] != item["system_id"] or target["status"] != "active"
            or edition not in item["ruleset_versions"] or edition not in target["ruleset_versions"]):
        return "HOLD"
    return "READY"


def resume(checkpoint, expected):
    if not checkpoint or checkpoint.get("active_system") != expected:
        return "HOLD"
    if checkpoint["checkpoint"]["branch"] == "CLOSED":
        return "CLOSED"
    return "CONTINUE" if (checkpoint["checkpoint"]["branch"] == "ACTIVE" and
                          checkpoint["resume"]["can_advance"] is True) else "HOLD"


def approved(scope, binding, rule_id, module_id):
    if not scope or not binding.get("adjudications_entry"):
        return False
    if any(scope[key] != value for key, value in (
        ("system_id", binding["system_id"]), ("ruleset_version", binding["ruleset"]["edition"]),
        ("campaign_id", binding["campaign_id"])
    )):
        return False
    return any(r["rule_id"] == rule_id and r.get("approval_ref")
               and (r["scope"] == "CAMPAIGN" or module_id in r.get("module_ids", []))
               for r in scope["approved_rules"])


class RepositoryChecks(unittest.TestCase):
    def test_RT07_RT12_RT14_single_T0_entry(self):
        runtime = read(GM + "07_RUNTIME_CONTROL_PROTOCOL.md")
        self.assertEqual(runtime.count("唯一 T0 操作入口"), 1)
        self.assertNotIn("回到最后一个有效场景节点", runtime)
        entry = runtime.split("### 14.1 唯一事故处置路径")[1].split("### 14.2")[0]
        for term in ("立即暂停", "原事件", "已发生的成本", "拒绝", "明确适用授权", "§14.1.1"):
            self.assertIn(term, entry)
        semantic_gate = runtime.split("### 14.1.1 补救身份、语义封锁与替代方案准入")[1].split("### 14.2")[0]
        for term in ("action_kind", "operation_ref", "target_ref", "scope_ref", "action_atoms[]",
                     "不同 remedy_id", "拆成多个子步骤", "available_remedies", "HOLD"):
            self.assertIn(term, semantic_gate)
        for path in ("SKILL", "GM_RELIABILITY_AND_EXPERIENCE_CONTROL_PROTOCOL",
                     "13_PREP_TO_RUNTIME_HANDOFF_STANDARD", "02_WORKFLOW_AND_PREFLIGHT"):
            self.assertIn("#141-唯一事故处置路径", read(GM + path + ".md"))
        self.assertNotIn("删除/标记", read(GM + "08_CLUE_AND_SOURCE_LEDGER.md"))

    def test_RT09_closed_metadata(self):
        raw = read(ND + "08_RUNTIME_STATE.md")
        historic = raw.split("## 9.")[1].split("## 10.")[0]
        close = metadata(raw.split("## 10.")[1])
        handoff = metadata(read(ND + "Sessions/SESSION_01_HANDOFF_PROMPT.md"))
        self.assertEqual(handoff["handoff_status"], "RETIRED")
        self.assertEqual(handoff["checkpoint_id"], close["checkpoint"]["checkpoint_id"])
        self.assertNotIn("一律使用 CONTINUE", raw.split("## 0.")[1].split("## 1.")[0])
        self.assertIn("已被本文件 §10 的 CLOSED 检查点取代", raw)
        readme = read(ND + "README.md")
        preflight_line = next(line for line in readme.splitlines() if "PREFLIGHT_2026-11-23.md" in line)
        self.assertIn("仅供追溯", preflight_line)
        self.assertNotIn("等待明确开团指令", preflight_line)
        preflight = read(ND + "PREFLIGHT_2026-11-23.md")
        self.assertIn("历史 Preflight 记录", preflight)
        self.assertIn("不构成开团、续团或推进许可", preflight)
        self.assertEqual(resume(metadata(historic), close["active_system"]), "HOLD")
        self.assertEqual(resume(handoff, close["active_system"]), "HOLD")
        self.assertEqual(resume({"mode": "CONTINUE"}, close["active_system"]), "HOLD")
        self.assertFalse(close["resume"]["can_advance"])
        self.assertEqual(resume(close, close["active_system"]), "CLOSED")
        active = {**close, "checkpoint": {"branch": "ACTIVE"}, "resume": {"can_advance": True}}
        self.assertEqual(resume(active, close["active_system"]), "CONTINUE")

    def test_RT11_current_schema_requires_manifest(self):
        state = read(GM + "RUNTIME_STATE_TEMPLATE.md")
        runtime = read(GM + "07_RUNTIME_CONTROL_PROTOCOL.md")
        self.assertNotIn("applied_event_ids 或 reconciliation manifest", state)
        for field in ("prepare_manifest_ref", "previous_published_checkpoint_ref",
                      "expected_version_ref", "independent_readback_ref"):
            self.assertIn(field, state)
        self.assertIn("在任何目标写入前保存并读回独立的 GM 批次清单", runtime)
        self.assertIn("回执丢失时按原 batch_id", runtime)

    def test_RT13_exact_registration_and_scope(self):
        registry = metadata(read("Systems/README.md"))["systems"]
        binding = metadata(read("Campaigns/Zarek/SYSTEM_BINDING.md"))
        entry = binding["system_entry"]
        actual_entries = {entry: metadata(read(entry))}
        self.assertTrue((ROOT / entry).exists())
        self.assertFalse((ROOT / "Systems/triangle_agency/README.md").exists())
        self.assertEqual(registry_route(registry, binding, actual_entries.get), "READY")
        bad_case = {**registry[0], "system_entry": entry.lower()}
        cases = [
            (registry, {}),
            (registry, {**binding, "ruleset": {"edition": "v99"}}),
            (registry * 2, binding),
            ([bad_case], {**binding, "system_entry": entry.lower()}),
            ([{**registry[0], "status": "candidate"}], binding),
        ]
        for entries, candidate in cases:
            with self.subTest(candidate=candidate):
                self.assertEqual(registry_route(entries, candidate, actual_entries.get), "HOLD")
        self.assertEqual(registry_route(registry, binding,
                         lambda _: {**actual_entries[entry], "system_id": "other"}), "HOLD")
        scope = metadata(read(binding["adjudications_entry"]))
        self.assertEqual({r["rule_id"] for r in scope["approved_rules"]}, {"Q01", "Q02", "Q03", "Q04"})
        self.assertTrue(approved(scope, binding, "Q04", "nosedive"))
        self.assertFalse(approved(scope, {**binding, "campaign_id": "other"}, "Q04", "nosedive"))
        self.assertFalse(approved(scope, {**binding, "ruleset": {"edition": "v99"}}, "Q04", "nosedive"))
        module_scope = {**scope, "approved_rules": [{"rule_id": "Q99", "scope": "MODULE",
                         "module_ids": ["nosedive"], "approval_ref": "synthetic evidence"}]}
        self.assertFalse(approved(module_scope, binding, "Q99", "other"))

    def test_RT16_markdown_links(self):
        paths = git("ls-files", "-z", "*.md").decode().rstrip("\0").split("\0")
        result = scan_links({p: read(p) for p in paths})
        print(f"\nRT-16: {len(paths)} Markdown files, {result['local_links']} local links, "
              f"{len(result['missing_paths'])} broken paths, "
              f"{len(result['anchor_candidates'])} candidate anchors", flush=True)
        self.assertEqual(result["missing_paths"], [])
        self.assertEqual(result["anchor_candidates"], [])

    def test_RT17_independent_arithmetic(self):
        path = "Campaigns/Zarek/模组/冰淇淋车_Ice_Cream_Truck/03_RUNTIME_STATE.md"
        text = read(path)
        reward, rest = text.split("### 任务奖励")[1].split("### 嘉奖流水")
        items = list(map(int, re.findall(r"\|\s*([+-]\d+)\s*\|", reward)))
        total = int(re.search(r"合计\*\*\s*\|\s*\*\*\+(\d+)", reward)[1])
        flow = rest.split("### Time")[0]
        balance = int(re.search(r"开场余额：(\d+)", flow)[1]) + sum(map(int, re.findall(r"[+-]\d+", flow)))
        spent, capacity, left = map(int, re.search(r"已花费 \*\*(\d+)/(\d+)\*\*，剩余 \*\*(\d+)", rest).groups())
        self.assertEqual((sum(items), total, balance, capacity - spent, left), (11, 11, 7, 28, 28))
        self.assertEqual(rest, git("show", BASE + ":" + path).decode().split("### 嘉奖流水")[1])
        print("\nRT-17: subtotal=11, balance=7, time=28; ledger unchanged", flush=True)

    def test_RT18_training_and_historical_phone(self):
        guidance = read(GM + "NARRATIVE_TRAINING_PROGRAM.md")
        self.assertIn("不要求用户预先审题", guidance)
        self.assertNotIn("每次开练前交用户审题", guidance)
        self.assertIn("选题和审核依本文件", guidance)
        sample = read(ND + "11_NARRATIVE_PRESENTATION_MATERIALS.md").split("### 2.3")[1].split("### 2.4")[0]
        self.assertIn("在场且可用", sample)
        self.assertNotIn("屏幕亮着", sample)
        for path in ("12_NPC_FIRST_CONTACT_CARDS.md", "Sessions/SESSION_01.md"):
            self.assertEqual(read(ND + path).encode(), git("show", BASE + ":" + ND + path))


class ReferenceExercises(unittest.TestCase):
    def test_RT07_RT12_RT14_incident_choices(self):
        history = ["original reply", "player choice", "cost"]
        base = {"delivery": "PLAYER_VISIBLE", "isolated": False, "accessed": True,
                "executed": False, "depended": True, "history": history}
        branches = [
            ({**base, "delivery": "INTERNAL_DRAFT", "isolated": True, "accessed": False,
              "depended": False}, None, "DRAFT_DISCARDED"),
            ({**base, "depended": False}, None, "OPEN"),
            (base, None, "OPEN"),
            (base, "REJECT_REMEDY", "OPEN"),
            (base, "CONTINUE_SAFE_SCOPE", "CONTAINED"),
            (base, "PAUSE_AUDIT", "OPEN"),
            (base, "TERMINATE", "TERMINATED"),
            ({**base, "delivery": "UNKNOWN"}, None, "OPEN"),
        ]
        for entry in ("Skill", "Runtime", "Handoff"):
            for record, choice, expected in branches:
                with self.subTest(entry=entry, delivery=record["delivery"], choice=choice):
                    observed = route_incident(record, choice)
                    self.assertEqual(observed["phase"], expected)
                    self.assertEqual(observed["history"], history)
                    if expected != "DRAFT_DISCARDED":
                        self.assertEqual(observed["affected_advances"], 0)
                        self.assertEqual(len(observed["choices_offered"]), 3)
                        self.assertEqual(observed["allowed_threads"],
                                         ["safe"] if expected == "CONTAINED" else [])
        refused = {
            "remedy_id": "restore-source-claim-v1",
            "action_kind": "RESTORE_SOURCE_ASSERTION",
            "operation_ref": "REINSERT_ORIGINAL_SOURCE_CLAIM",
            "target_ref": "claim:source-origin-17",
            "scope_ref": "incident:INC-01:claim-17",
            "action_atoms": ["restore:claim-17:source-assertion"],
            "description": "恢复原始来源声明",
        }
        independent = {
            "remedy_id": "independent-audit",
            "action_kind": "AUDIT_UNAFFECTED_BRANCH",
            "operation_ref": "VERIFY_SEPARATE_EVIDENCE_CHAIN",
            "target_ref": "branch:unaffected-02",
            "scope_ref": "incident:INC-01:unaffected-branch-02",
            "action_atoms": ["audit:branch-02:independent-evidence"],
            "description": "独立核验不受影响的旁支",
        }
        remedy = {**base, "remedy": refused, "declined_remedies": [],
                  "proposed_remedies": [refused, independent]}
        rejected = route_incident(remedy, "REJECT_REMEDY")
        self.assertEqual(rejected["remedy_recording_status"], "RECORDED")
        self.assertEqual(rejected["declined_remedies"][0]["remedy_id"], refused["remedy_id"])
        self.assertEqual(rejected["declined_remedies"][0]["semantic_signature"],
                         ["restore_source_assertion", "reinsert_original_source_claim",
                          "claim:source-origin-17", "incident:inc-01:claim-17"])
        self.assertEqual(rejected["available_remedies"], [],
                         "a GM must not volunteer an alternative after refusal")

        # Same operation, target, scope and atomic effect; new ID and new wording do not help.
        reworded_new_id = {**refused, "remedy_id": "fresh-remedy-id",
                           "target_label": "另一种写法的来源目标描述",
                           "description": "重新梳理材料，再把来源声明补进去"}
        retried = route_incident({**base, "declined_remedies": rejected["declined_remedies"],
                                  "proposed_remedies": [reworded_new_id],
                                  "player_permission": "ASKED"}, "PAUSE_AUDIT")
        self.assertEqual(retried["available_remedies"], [])

        # A decomposed sub-step remains blocked through its shared atomic action reference.
        split_step = {"remedy_id": "small-step-2", "action_kind": "APPEND_NOTE",
                      "operation_ref": "ADD_SOURCE_LINE_TO_APPENDIX",
                      "target_ref": "claim:source-origin-17", "scope_ref": "incident:INC-01:claim-17",
                      "action_atoms": ["restore:claim-17:source-assertion"],
                      "description": "只在附录中补一行来源声明"}
        split_result = route_incident({**base, "declined_remedies": rejected["declined_remedies"],
                                       "proposed_remedies": [split_step],
                                       "player_permission": "AUTHORIZED"}, "PAUSE_AUDIT")
        self.assertEqual(split_result["available_remedies"], [])

        # A genuinely distinct proposal is still withheld until the player asks/authorizes.
        no_permission = route_incident({**base, "declined_remedies": rejected["declined_remedies"],
                                        "proposed_remedies": [independent]}, "PAUSE_AUDIT")
        self.assertEqual(no_permission["available_remedies"], [])
        asked = route_incident({**base, "declined_remedies": rejected["declined_remedies"],
                                "proposed_remedies": [independent], "player_permission": "ASKED"},
                               "PAUSE_AUDIT")
        self.assertEqual([item["remedy_id"] for item in asked["available_remedies"]], ["independent-audit"])

        # Missing semantic identity is fail-closed, even after the player asks for alternatives.
        incomplete = {"remedy_id": "unknown-semantics", "description": "another way to fix it"}
        incomplete_result = route_incident({**base, "declined_remedies": rejected["declined_remedies"],
                                            "proposed_remedies": [incomplete],
                                            "player_permission": "ASKED"}, "PAUSE_AUDIT")
        self.assertEqual(incomplete_result["available_remedies"], [])
        # If the refusal itself cannot be assigned a complete semantic identity, fail closed.
        malformed_refusal = route_incident({**base, "remedy": incomplete,
                                            "proposed_remedies": [independent],
                                            "player_permission": "AUTHORIZED"}, "REJECT_REMEDY")
        self.assertEqual(malformed_refusal["remedy_recording_status"], "INCOMPLETE")
        self.assertEqual(malformed_refusal["available_remedies"], [])
        self.assertEqual(rejected["history"], history)
        print("\nT0 reference: refusal survives new ID/rewording/split action; alternatives require player inquiry; history preserved", flush=True)

    def test_RT11_process_faults(self):
        event = {"event_id": "RWD-1", "event_revision_id": "RWD-1-v1", "batch_id": "B1",
                 "base_revision": 1, "target_revision": 2, "delta": 3, "public_text": "Reward +3",
                 "visibility": "RECIPIENT_SCOPED", "recipient_scope": "player"}

        def invoke(root, **cmd):
            result = subprocess.run([sys.executable, str(WORKER), str(root)], input=json.dumps(cmd),
                                    text=True, capture_output=True)
            return result.returncode, json.loads(result.stdout) if result.stdout else {}, result.stderr

        for fault, expected_code in (("log-only", 73), ("runtime-only", 73), ("ack-lost", 74)):
            with self.subTest(fault=fault), tempfile.TemporaryDirectory() as name:
                root = Path(name)
                write_json(root / "previous.json", {"revision": 1, "balance": 7})
                code, interrupted, err = invoke(root, op="commit", event=event, fault=fault)
                self.assertEqual(code, expected_code, err)
                code, readback, err = invoke(root, op="inspect")
                self.assertEqual(code, 0, err)
                self.assertEqual(readback["batch_status"], "PUBLISHED" if fault == "ack-lost" else "INCOMPLETE")
                if interrupted:
                    self.assertNotEqual(interrupted["pid"], readback["pid"])
                    self.assertEqual(readback["targets"][interrupted["partial_target"]], "VERIFIED")
                    self.assertEqual(sum(s == "MISSING" for s in readback["targets"].values()), 2)
                code, saved, err = invoke(root, op="commit", event=event)
                self.assertEqual(code, 0, err)
                self.assertEqual(saved["batch_status"], "PUBLISHED")
                self.assertEqual(saved["writes"], 0 if fault == "ack-lost" else 2)
                self.assertEqual(json.loads((root / "runtime.json").read_bytes())["balance"], 10)
                code, again, err = invoke(root, op="commit", event=event)
                self.assertEqual(code, 0, err)
                self.assertEqual(again["writes"], 0)
                code, _, err = invoke(root, op="commit", event={**event, "delta": 99})
                self.assertNotEqual(code, 0)
                self.assertIn("different event", err)
                self.assertEqual(json.loads((root / "runtime.json").read_bytes())["balance"], 10)
                print(f"\nRT-11 {fault}: exit={expected_code}; observed={readback}; "
                      f"recovery_writes={saved['writes']}; retry_writes=0; balance=10", flush=True)
                write_json(root / "notes.json", {"recipient_scope": "wrong"})
                code, disputed, err = invoke(root, op="inspect")
                self.assertEqual(code, 0, err)
                self.assertEqual(disputed["batch_status"], "DISPUTED")

    def test_RT13_reference_A_B_A(self):
        a = metadata(read("Campaigns/Zarek/SYSTEM_BINDING.md"))
        registry = metadata(read("Systems/README.md"))["systems"]
        b = {"system_id": "paper_lantern", "system_entry": "Systems/Paper/README.md",
             "status": "active", "campaign_id": "paper", "ruleset": {"edition": "0.1"}}
        b_entry = {"system_id": b["system_id"], "status": "active", "ruleset_versions": ["0.1"]}
        registry.append({**b_entry, "system_entry": b["system_entry"]})
        rules = {"triangle_agency": {"QA": "Quality Assurance", "dice": 6},
                 "paper_lantern": {"QA": "Quiet Access", "dice": 2, "threshold": 8}}
        states = {}
        history = {"QA": "Quality Assurance", "dice": 6, "target": 3}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for bound, head in ((a, metadata(read(a["system_entry"]))), (b, b_entry)):
                package = root / Path(bound["system_entry"]).parent
                package.mkdir(parents=True)
                (package / "README.md").write_text("```yaml\n" + yaml.safe_dump(head) + "```\n")
                write_json(package / "rules.json", rules[bound["system_id"]])
            for bound, result in ((a, "Quality Assurance"), (b, "Quiet Access"), (a, "Quality Assurance")):
                self.assertEqual(registry_route(registry, bound, lambda p: metadata((root / p).read_text())), "READY")
                active = json.loads((root / Path(bound["system_entry"]).parent / "rules.json").read_bytes())
                path = root / (bound["campaign_id"] + ".json")
                state = json.loads(path.read_bytes()) if path.exists() else {"turn": 0}
                self.assertEqual(active["QA"], result)
                if bound == b:
                    self.assertNotEqual(active["dice"], history["dice"])
                    self.assertGreaterEqual(sum([3, 4]) + 1, active["threshold"])
                if state["turn"]:
                    self.assertEqual(state, states[bound["campaign_id"]])
                state["turn"] += 1
                write_json(path, state)
                states[bound["campaign_id"]] = state
        self.assertEqual(states, {"zarek": {"turn": 2}, "paper": {"turn": 1}})
        print("\nRT-13 reference: A Quality Assurance -> B Quiet Access / 2d6+1=8 -> A restored", flush=True)

    def test_RT08_final_artifact(self):
        segments = [
            {"field": "public_utterance", "recipients": ["a", "b"], "delivery": "PRESENTED", "text": "Observed"},
            {"field": "player_known_claim", "recipients": ["a"], "delivery": "PRESENTED", "text": "Only A"},
            {"field": "gm_plan", "recipients": ["a", "b"], "delivery": "PRESENTED", "text": "GM-PLAN"},
            {"field": "gm_track", "recipients": [], "delivery": "NOT_PRESENTED", "text": "GM-TRACK"},
            {"field": "gm_truth", "recipients": ["a"], "delivery": "PRESENTED", "text": "GM-TRUTH"},
            {"field": "public_observation", "recipients": ["a"], "delivery": "UNKNOWN", "text": "UNSEEN-ID"},
        ]
        forbidden = ("GM-PLAN", "GM-TRACK", "GM-TRUTH", "UNSEEN-ID")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for recipient, expected in (("a", "Observed\nOnly A"), ("b", "Observed")):
                self.assertEqual(projection(root, segments, recipient, forbidden), "PUBLISHED")
                data = (root / recipient / "notes.txt").read_bytes()
                self.assertEqual(data.decode(), expected)
                self.assertEqual([p.name for p in (root / recipient).iterdir()], ["notes.txt"])
                print(f"\nRT-08 {recipient}: readback SHA-256 {sha256(data).hexdigest()}", flush=True)
            self.assertEqual(projection(root, segments, "unsafe", forbidden, extra="\n附录：ＧＭ-ＰＬＡＮ".encode()), "NOT_PUBLISHED")
            self.assertEqual(projection(root, segments, "no-readback", forbidden, readable=False), "NOT_PUBLISHED")
            self.assertFalse((root / "unsafe").exists())
            self.assertFalse((root / "no-readback").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
