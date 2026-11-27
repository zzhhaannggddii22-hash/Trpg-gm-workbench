"""Executable reference-model tests for Cairn runtime state invariants.

This is a small deterministic protocol model, not the GM runtime itself and not
an independent blind test of a language model. It protects arithmetic,
idempotency, pending-effect, travel, resource, event-routing and NPC-state
invariants used by the Cairn 2e candidate runtime.
"""
import math
import unittest


def resolve_attack_damage(hp, strength, armor, damage, save_roll=None, actor="PC"):
    final_damage = max(0, damage - armor)
    result = {
        "hp_before": hp,
        "str_before": strength,
        "damage_after_armor": final_damage,
        "hp": hp,
        "strength": strength,
        "overflow": 0,
        "scars": False,
        "dead": False,
        "save_rolled": False,
        "save_success": None,
        "status": "no_damage",
    }
    if final_damage == 0:
        return result

    hp_raw = hp - final_damage
    if hp_raw > 0:
        result.update(hp=hp_raw, status="ordinary_damage")
        return result

    if hp_raw == 0:
        result.update(hp=0, scars=(actor == "PC"), status="scars" if actor == "PC" else "zero_hp")
        return result

    overflow = -hp_raw
    strength_after = strength - overflow
    result.update(hp=0, overflow=overflow, strength=max(0, strength_after))
    if actor != "PC":
        result["status"] = "warden_adjudication"
        return result
    if strength_after <= 0:
        result.update(dead=True, status="dead_str_zero")
        return result
    if save_roll is None:
        result["status"] = "critical_save_required"
        return result

    success = save_roll == 1 or (save_roll != 20 and save_roll <= strength_after)
    result.update(
        save_rolled=True,
        save_success=success,
        status="critical_saved" if success else "critical_failed",
    )
    return result


def set_hp_zero_by_condition(cause):
    return {
        "hp": 0,
        "hp_zero_cause": cause,
        "scars": False,
        "critical_damage": False,
    }


class PendingEffectLedger:
    def __init__(self):
        self.effects = {}

    def create(self, effect_id, trigger):
        if effect_id not in self.effects:
            self.effects[effect_id] = {
                "trigger": trigger,
                "status": "pending",
                "resolution_event_id": None,
            }
        return self.effects[effect_id]

    def mark_ready(self, effect_id, condition_met):
        effect = self.effects[effect_id]
        if effect["status"] == "pending" and condition_met:
            effect["status"] = "ready"
        return effect["status"]

    def consume(self, effect_id, resolution_event_id):
        effect = self.effects[effect_id]
        if effect["status"] == "consumed":
            return effect["resolution_event_id"] == resolution_event_id
        if effect["status"] != "ready":
            return False
        effect["status"] = "consumed"
        effect["resolution_event_id"] = resolution_event_id
        return True


class TravelPlan:
    def __init__(self, total_watches):
        self.total_watches = total_watches
        self.watches_elapsed = 0
        self.watch_events = set()
        self.travel_actions = {}
        self.status = "travelling"

    def record_travel_action(self, action_id, check_id, roll, result):
        if action_id in self.travel_actions:
            return self.travel_actions[action_id]
        record = {
            "check_id": check_id,
            "roll": roll,
            "result": result,
            "committed": True,
        }
        self.travel_actions[action_id] = record
        return record

    def commit_watch(self, watch_event_id):
        if watch_event_id in self.watch_events:
            return self.watches_elapsed
        self.watch_events.add(watch_event_id)
        self.watches_elapsed += 1
        if self.watches_elapsed >= self.total_watches:
            self.status = "arrived"
        return self.watches_elapsed


class Ration:
    def __init__(self, uses=3):
        self.uses_remaining = uses

    def consume(self):
        if self.uses_remaining <= 0:
            return False
        self.uses_remaining -= 1
        return True

    @property
    def removed(self):
        return self.uses_remaining == 0


def deprivation_fatigue_ticks(elapsed_hours):
    if elapsed_hours <= 24:
        return 0
    return max(0, math.ceil(elapsed_hours / 24) - 1)


def dungeon_exhaustion_followup(parent_event_id, choice):
    if choice == "rest":
        return {
            "parent_event_id": parent_event_id,
            "child_event_id": parent_event_id + ":rest-event",
            "reroll": True,
        }
    if choice in ("fatigue", "ration"):
        return {
            "parent_event_id": parent_event_id,
            "child_event_id": None,
            "reroll": False,
        }
    raise ValueError("invalid Dungeon Exhaustion choice")


def wilderness_event_followup(event_type, chosen_cost):
    if event_type == "loss":
        return {"kind": "fictional_loss_cost", "cost": chosen_cost, "dungeon_pause": False}
    if event_type == "exhaustion":
        return {"kind": "travel_obstacle", "cost": chosen_cost, "dungeon_recursive_roll": False}
    return {"kind": "ordinary_event", "cost": None}


def resolve_blast(targets, damages):
    if len(targets) != len(damages):
        raise ValueError("one damage input is required per affected target")
    return [
        resolve_attack_damage(
            hp=t["hp"],
            strength=t["strength"],
            armor=t["armor"],
            damage=damage,
        )
        for t, damage in zip(targets, damages)
    ]


class NPCState:
    def __init__(self, location, ration_uses, task_state, private_knowledge):
        self.location = location
        self.ration_uses = ration_uses
        self.task_state = task_state
        self.private_knowledge = set(private_knowledge)
        self.committed_actions = set()

    def commit_offscreen_action(self, event_id, location, ration_cost, task_state):
        if event_id in self.committed_actions:
            return False
        self.committed_actions.add(event_id)
        self.location = location
        self.ration_uses -= ration_cost
        self.task_state = task_state
        return True

    def reencounter(self):
        return {
            "location": self.location,
            "ration_uses": self.ration_uses,
            "task_state": self.task_state,
            "private_knowledge": set(self.private_knowledge),
            "committed_actions": set(self.committed_actions),
        }


def resolve_mixed_modifiers(impaired, enhanced):
    if impaired and enhanced:
        return "needs_fictional_adjudication"
    if impaired:
        return "impaired"
    if enhanced:
        return "enhanced"
    return "normal"


class CairnRuntimeProtocolTests(unittest.TestCase):
    def test_armor_reduces_damage_to_zero(self):
        result = resolve_attack_damage(3, 10, 2, 2)
        self.assertEqual(result["status"], "no_damage")
        self.assertEqual((result["hp"], result["strength"]), (3, 10))
        self.assertFalse(result["scars"])

    def test_exact_zero_from_pc_attack_triggers_scars(self):
        result = resolve_attack_damage(3, 10, 0, 3)
        self.assertEqual(result["status"], "scars")
        self.assertEqual(result["hp"], 0)
        self.assertTrue(result["scars"])

    def test_overflow_uses_new_strength_for_save(self):
        result = resolve_attack_damage(1, 4, 0, 3, save_roll=2)
        self.assertEqual(result["overflow"], 2)
        self.assertEqual(result["strength"], 2)
        self.assertTrue(result["save_success"])
        self.assertEqual(result["hp"], 0)

    def test_strength_zero_death_precedes_natural_one(self):
        result = resolve_attack_damage(1, 2, 0, 3, save_roll=1)
        self.assertEqual(result["strength"], 0)
        self.assertTrue(result["dead"])
        self.assertFalse(result["save_rolled"])

    def test_hp_zero_then_hit_is_critical_not_scars(self):
        result = resolve_attack_damage(0, 5, 0, 2, save_roll=3)
        self.assertEqual(result["overflow"], 2)
        self.assertEqual(result["strength"], 3)
        self.assertFalse(result["scars"])
        self.assertTrue(result["save_success"])

    def test_non_damage_hp_zero_has_no_scars(self):
        for cause in ("panic", "inventory_overload"):
            result = set_hp_zero_by_condition(cause)
            self.assertEqual(result["hp"], 0)
            self.assertEqual(result["hp_zero_cause"], cause)
            self.assertFalse(result["scars"])
            self.assertFalse(result["critical_damage"])

    def test_pending_scar_effect_waits_for_recovery(self):
        ledger = PendingEffectLedger()
        ledger.create("scar-72", "broken_limb_healed")
        self.assertEqual(ledger.mark_ready("scar-72", False), "pending")
        self.assertEqual(ledger.mark_ready("scar-72", True), "ready")

    def test_pending_effect_consumes_once(self):
        ledger = PendingEffectLedger()
        ledger.create("scar-73", "walloped_recovered")
        ledger.mark_ready("scar-73", True)
        self.assertTrue(ledger.consume("scar-73", "resolve-1"))
        self.assertEqual(ledger.effects["scar-73"]["status"], "consumed")
        self.assertTrue(ledger.consume("scar-73", "resolve-1"))
        self.assertFalse(ledger.consume("scar-73", "resolve-2"))

    def test_doomed_trigger_is_scoped_to_critical_save(self):
        ledger = PendingEffectLedger()
        ledger.create("doomed-1", "next_critical_damage_save")
        self.assertEqual(ledger.effects["doomed-1"]["status"], "pending")
        self.assertEqual(ledger.mark_ready("doomed-1", False), "pending")
        self.assertEqual(ledger.mark_ready("doomed-1", True), "ready")

    def test_multi_watch_travel_does_not_arrive_early(self):
        plan = TravelPlan(total_watches=4)
        plan.commit_watch("watch-1")
        plan.commit_watch("watch-2")
        self.assertEqual(plan.watches_elapsed, 2)
        self.assertEqual(plan.status, "travelling")

    def test_travel_handoff_reuses_same_action_check(self):
        plan = TravelPlan(total_watches=4)
        first = plan.record_travel_action("travel-action-1", "lost-check-1", 2, "lost")
        replay = plan.record_travel_action("travel-action-1", "lost-check-1", 5, "not_lost")
        self.assertEqual(first, replay)
        self.assertEqual(len(plan.travel_actions), 1)

    def test_new_travel_action_gets_new_check(self):
        plan = TravelPlan(total_watches=4)
        plan.record_travel_action("travel-action-1", "lost-check-1", 2, "lost")
        plan.record_travel_action("travel-action-2", "lost-check-2", 5, "not_lost")
        self.assertEqual(len(plan.travel_actions), 2)

    def test_watch_commit_is_idempotent(self):
        plan = TravelPlan(total_watches=4)
        plan.commit_watch("watch-1")
        plan.commit_watch("watch-1")
        self.assertEqual(plan.watches_elapsed, 1)

    def test_ration_is_consumed_by_use(self):
        ration = Ration(3)
        self.assertTrue(ration.consume())
        self.assertEqual(ration.uses_remaining, 2)
        self.assertFalse(ration.removed)

    def test_deprivation_ticks_follow_labeled_time_boundary(self):
        self.assertEqual(deprivation_fatigue_ticks(24), 0)
        self.assertEqual(deprivation_fatigue_ticks(25), 1)
        self.assertEqual(deprivation_fatigue_ticks(49), 2)

    def test_dungeon_rest_creates_distinct_child_event(self):
        result = dungeon_exhaustion_followup("event-1", "rest")
        self.assertTrue(result["reroll"])
        self.assertNotEqual(result["parent_event_id"], result["child_event_id"])

    def test_wilderness_events_do_not_use_dungeon_recursion(self):
        loss = wilderness_event_followup("loss", "oil_flask_lost")
        exhaustion = wilderness_event_followup("exhaustion", "one_watch_delay")
        self.assertFalse(loss["dungeon_pause"])
        self.assertFalse(exhaustion["dungeon_recursive_roll"])

    def test_blast_targets_are_resolved_separately(self):
        targets = [
            {"hp": 5, "strength": 10, "armor": 1},
            {"hp": 5, "strength": 10, "armor": 0},
            {"hp": 5, "strength": 10, "armor": 2},
        ]
        results = resolve_blast(targets, [4, 2, 5])
        self.assertEqual([x["hp"] for x in results], [2, 3, 2])
        self.assertEqual(len(results), 3)

    def test_npc_reencounter_preserves_offscreen_state_and_knowledge(self):
        npc = NPCState("landing", 3, "skiff_missing", {"debt", "sealed_cargo_contents"})
        self.assertTrue(npc.commit_offscreen_action("search-1", "downstream", 1, "skiff_found"))
        first = npc.reencounter()
        self.assertEqual(first["location"], "downstream")
        self.assertEqual(first["ration_uses"], 2)
        self.assertTrue(npc.commit_offscreen_action("search-1", "old_mill", 1, "cargo_found"))
        second = npc.reencounter()
        self.assertEqual(second["location"], "downstream")
        self.assertEqual(second["ration_uses"], 2)
        self.assertIn("sealed_cargo_contents", second["private_knowledge"])

    def test_conflicting_attack_modifiers_require_adjudication(self):
        self.assertEqual(resolve_mixed_modifiers(True, True), "needs_fictional_adjudication")
        self.assertEqual(resolve_mixed_modifiers(True, False), "impaired")
        self.assertEqual(resolve_mixed_modifiers(False, True), "enhanced")


if __name__ == "__main__":
    unittest.main()
