"""Daggerheart Core Set deterministic reference executor.

Test oracle only; this is not the production GM runtime.
Run: python Systems/Daggerheart/Testing/daggerheart_reference_engine.py
"""
from dataclasses import dataclass, field
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Reference_Data"


@dataclass
class PC:
    hope: int = 2
    stress: int = 0
    stress_max: int = 6
    hp: int = 0
    hp_max: int = 6
    armor_slots: int = 0
    vulnerable: bool = False
    major: int = 5
    severe: int = 10
    loadout: list = field(default_factory=list)
    vault: list = field(default_factory=list)


@dataclass
class GM:
    fear: int = 0


def bounded(value, delta, maximum):
    return min(maximum, max(0, value + delta))


def action_roll(hope_die, fear_die, modifier, difficulty):
    if not (1 <= hope_die <= 12 and 1 <= fear_die <= 12):
        raise ValueError("Duality Dice must be d12")
    total = hope_die + fear_die + modifier
    if hope_die == fear_die:
        return {"total": total, "success": True, "kind": "critical"}
    return {"total": total, "success": total >= difficulty,
            "kind": "hope" if hope_die > fear_die else "fear"}


def clear_stress(pc, amount=1):
    was_full = pc.stress == pc.stress_max
    pc.stress = max(0, pc.stress - amount)
    if was_full and pc.stress < pc.stress_max:
        pc.vulnerable = False


def resolve_action(pc, gm, result):
    if result["kind"] == "critical":
        pc.hope = bounded(pc.hope, 1, 6)
        clear_stress(pc)
    elif result["kind"] == "hope":
        pc.hope = bounded(pc.hope, 1, 6)
    elif result["kind"] == "fear":
        gm.fear = bounded(gm.fear, 1, 12)
    return result


def reaction_roll(die_a, die_b, modifier, difficulty):
    total = die_a + die_b + modifier
    return {"total": total, "success": total >= difficulty,
            "critical": die_a == die_b}


def mark_hp(pc, amount):
    pc.hp = bounded(pc.hp, amount, pc.hp_max)


def mark_stress(pc, amount=1):
    overflow = max(0, pc.stress + amount - pc.stress_max)
    pc.stress = min(pc.stress_max, pc.stress + amount)
    if pc.stress == pc.stress_max:
        pc.vulnerable = True
    if overflow:
        mark_hp(pc, overflow)
    return overflow


def pay_stress_cost(pc, amount):
    if amount < 0 or pc.stress + amount > pc.stress_max:
        return False
    pc.stress += amount
    if pc.stress == pc.stress_max:
        pc.vulnerable = True
    return True


def damage_marks(damage, major, severe):
    if damage <= 0:
        return 0
    if damage >= severe:
        return 3
    if damage >= major:
        return 2
    return 1


def take_damage(pc, damage, direct=False, resistant=False, use_armor=False):
    # Resistance halves incoming damage (round up) before thresholds and Armor.
    # Direct damage bypasses Armor Slots only; it does not bypass Resistance.
    final = max(0, damage)
    if resistant:
        final = (final + 1) // 2
    marks = damage_marks(final, pc.major, pc.severe)
    if use_armor and not direct and marks and pc.armor_slots:
        marks -= 1
        pc.armor_slots -= 1
    mark_hp(pc, marks)
    return {"final_damage": final, "hp_marks": marks}



def resolve_incoming_damage(pc, sources, resistances=(), immunities=(), direct=False, use_armor=False):
    """Resolve one simultaneous incoming-damage event.

    Each source is {"amount": int, "type": "phy"|"mag"}. Sources are
    aggregated by type before Resistance. For mixed-type damage, defenses
    apply only when every damage type is covered by Resistance or Immunity.
    Direct damage bypasses Armor Slots, not Resistance or Immunity.
    """
    totals = {"phy": 0, "mag": 0}
    for source in sources:
        damage_type = source["type"]
        if damage_type not in totals:
            raise ValueError("Damage type must be phy or mag")
        amount = source["amount"]
        if amount < 0:
            raise ValueError("Damage amount cannot be negative")
        totals[damage_type] += amount

    active_types = {kind for kind, amount in totals.items() if amount > 0}
    resistances = set(resistances)
    immunities = set(immunities)
    if not active_types:
        final = 0
    elif len(active_types) > 1 and not all(
        kind in resistances or kind in immunities for kind in active_types
    ):
        # Mixed damage receives no partial defense unless both types are covered.
        final = sum(totals.values())
    else:
        final = 0
        for kind in active_types:
            amount = totals[kind]
            if kind in immunities:
                continue
            if kind in resistances:
                amount = (amount + 1) // 2
            final += amount

    marks = damage_marks(final, pc.major, pc.severe)
    armor_spent = False
    if use_armor and not direct and marks and pc.armor_slots:
        marks -= 1
        pc.armor_slots -= 1
        armor_spent = True
    mark_hp(pc, marks)
    return {
        "final_damage": final,
        "hp_marks": marks,
        "armor_spent": armor_spent,
        "damage_by_type": totals,
    }


def advantage_state(advantage_sources, disadvantage_sources):
    net = advantage_sources - disadvantage_sources
    return "advantage" if net > 0 else "disadvantage" if net < 0 else "none"


def advance_countdown(state, event_id, amount=1):
    applied = state.setdefault("applied_events", set())
    if event_id in applied:
        return False
    state["value"] += amount
    applied.add(event_id)
    return True


def short_rest(state, interrupted=False):
    if interrupted:
        return {"completed": False, "refresh": False}
    if state.get("short_rests_since_long", 0) >= 2:
        return {"completed": False, "refresh": False, "requires_long_rest": True}
    state["short_rests_since_long"] = state.get("short_rests_since_long", 0) + 1
    return {"completed": True, "refresh": True}


def long_rest(state, interrupted=False, fear_roll=0, pc_count=1, gm=None):
    if interrupted:
        return short_rest(state)
    state["short_rests_since_long"] = 0
    if gm is not None:
        gm.fear = bounded(gm.fear, fear_roll + pc_count, 12)
    return {"completed": True, "refresh": True, "long_rest": True}


def recall_card(pc, card, stress_cost):
    if card not in pc.vault or not pay_stress_cost(pc, stress_cost):
        return False
    if len(pc.loadout) >= 5:
        pc.vault.append(pc.loadout.pop(0))
    pc.vault.remove(card)
    pc.loadout.append(card)
    return True


def help_ally(pc, advantage_rolls):
    cost = len(advantage_rolls)
    if cost == 0 or pc.hope < cost:
        return None
    pc.hope -= cost
    return max(advantage_rolls)


def group_action_modifier(helper_reactions):
    # Each helper contributes +1 on success and -1 on failure.
    return sum(1 if success else -1 for success in helper_reactions)


def adversary_attack(d20, attack_modifier, pc_evasion):
    if not 1 <= d20 <= 20:
        raise ValueError("Adversary attack die must be d20")
    total = d20 + attack_modifier
    return {"total": total, "hit": total >= pc_evasion}


def spend_fear(gm, amount=1):
    if amount < 0 or gm.fear < amount:
        return False
    gm.fear -= amount
    return True


def add_shared_pool_token(pool, token=1):
    pool["tokens"] = pool.get("tokens", 0) + token


def consume_shared_pool_token(pool):
    if pool.get("tokens", 0) <= 0:
        return False
    pool["tokens"] -= 1
    return True


def trigger_evolution_once(state, evolution_id):
    triggered = state.setdefault("triggered_evolutions", set())
    if evolution_id in triggered:
        return False
    triggered.add(evolution_id)
    return True


def can_equip_tier(character_tier, item_tier):
    return item_tier <= character_tier


def loadout_is_valid(loadout):
    return len(loadout) <= 5


def load_core_data():
    manifest = json.loads((DATA / "DATASET_MANIFEST.json").read_text(encoding="utf-8"))
    datasets = {p.stem: json.loads(p.read_text(encoding="utf-8"))
                for p in (DATA / "Core_Set").glob("*.json")}
    return manifest, datasets


class TestDaggerheartReferenceExecutor(unittest.TestCase):
    def test_01_success_with_hope(self):
        r = action_roll(9, 4, 2, 15)
        self.assertEqual((r["success"], r["kind"]), (True, "hope"))

    def test_02_success_with_fear(self):
        r = action_roll(3, 9, 4, 15)
        self.assertEqual((r["success"], r["kind"]), (True, "fear"))

    def test_03_failure_with_hope(self):
        r = action_roll(8, 2, 0, 15)
        self.assertEqual((r["success"], r["kind"]), (False, "hope"))

    def test_04_failure_with_fear(self):
        r = action_roll(2, 8, 0, 15)
        self.assertEqual((r["success"], r["kind"]), (False, "fear"))

    def test_05_tie_is_automatic_critical(self):
        r = action_roll(5, 5, -4, 99)
        self.assertEqual((r["success"], r["kind"]), (True, "critical"))

    def test_06_critical_awards_hope_and_clears_stress(self):
        pc, gm = PC(stress=3), GM()
        resolve_action(pc, gm, action_roll(7, 7, 0, 20))
        self.assertEqual((pc.hope, pc.stress, gm.fear), (3, 2, 0))

    def test_07_hope_caps_at_six(self):
        pc = PC(hope=6)
        resolve_action(pc, GM(), action_roll(8, 3, 0, 1))
        self.assertEqual(pc.hope, 6)

    def test_08_fear_caps_at_twelve(self):
        gm = GM(fear=12)
        resolve_action(PC(), gm, action_roll(2, 9, 0, 1))
        self.assertEqual(gm.fear, 12)

    def test_09_reaction_does_not_change_hope_or_fear(self):
        pc, gm = PC(), GM()
        reaction_roll(12, 12, 0, 10)
        self.assertEqual((pc.hope, gm.fear), (2, 0))

    def test_10_advantage_disadvantage_cancel_pairwise(self):
        self.assertEqual(advantage_state(2, 1), "advantage")
        self.assertEqual(advantage_state(1, 2), "disadvantage")
        self.assertEqual(advantage_state(2, 2), "none")

    def test_11_last_stress_causes_vulnerable(self):
        pc = PC(stress=5)
        mark_stress(pc)
        self.assertTrue(pc.vulnerable)

    def test_12_clearing_stress_removes_full_stress_vulnerable(self):
        pc = PC(stress=6, vulnerable=True)
        clear_stress(pc)
        self.assertFalse(pc.vulnerable)

    def test_13_stress_overflow_marks_hp(self):
        pc = PC(stress=6)
        self.assertEqual(mark_stress(pc), 1)
        self.assertEqual((pc.stress, pc.hp), (6, 1))

    def test_14_unpayable_stress_cost_does_not_overflow(self):
        pc = PC(stress=6)
        self.assertFalse(pay_stress_cost(pc, 1))
        self.assertEqual(pc.hp, 0)

    def test_15_minor_damage_marks_one_hp(self):
        self.assertEqual(damage_marks(4, 5, 10), 1)

    def test_16_major_damage_marks_two_hp(self):
        self.assertEqual(damage_marks(5, 5, 10), 2)

    def test_17_severe_damage_marks_three_hp(self):
        self.assertEqual(damage_marks(10, 5, 10), 3)

    def test_18_zero_damage_marks_no_hp(self):
        self.assertEqual(damage_marks(0, 5, 10), 0)

    def test_19_armor_reduces_severity_once(self):
        pc = PC(armor_slots=1)
        result = take_damage(pc, 10, use_armor=True)
        self.assertEqual((result["hp_marks"], pc.armor_slots, pc.hp), (2, 0, 2))

    def test_20_direct_damage_ignores_armor(self):
        pc = PC(armor_slots=1)
        result = take_damage(pc, 10, direct=True, use_armor=True)
        self.assertEqual((result["hp_marks"], pc.armor_slots), (3, 1))

    def test_21_resistance_halves_and_rounds_up_before_threshold(self):
        result = take_damage(PC(), 11, resistant=True)
        self.assertEqual((result["final_damage"], result["hp_marks"]), (6, 2))

    def test_22_countdown_event_is_idempotent(self):
        state = {"value": 0}
        self.assertTrue(advance_countdown(state, "roll-1"))
        self.assertFalse(advance_countdown(state, "roll-1"))
        self.assertEqual(state["value"], 1)

    def test_23_distinct_rolls_advance_countdown_separately(self):
        state = {"value": 0}
        advance_countdown(state, "roll-1")
        advance_countdown(state, "roll-2")
        self.assertEqual(state["value"], 2)

    def test_24_interrupted_short_rest_has_no_refresh(self):
        self.assertFalse(short_rest({}, interrupted=True)["refresh"])

    def test_25_third_consecutive_short_rest_requires_long_rest(self):
        self.assertTrue(short_rest({"short_rests_since_long": 2})["requires_long_rest"])

    def test_26_long_rest_resets_short_rest_counter_and_adds_fear(self):
        state, gm = {"short_rests_since_long": 2}, GM()
        long_rest(state, fear_roll=2, pc_count=1, gm=gm)
        self.assertEqual((state["short_rests_since_long"], gm.fear), (0, 3))

    def test_27_interrupted_long_rest_downgrades_to_short_rest(self):
        state = {"short_rests_since_long": 0}
        r = long_rest(state, interrupted=True)
        self.assertTrue(r["completed"])
        self.assertNotIn("long_rest", r)

    def test_28_recall_uses_stress_and_preserves_five_card_loadout(self):
        pc = PC(loadout=list("abcde"), vault=["f"])
        self.assertTrue(recall_card(pc, "f", 1))
        self.assertEqual(len(pc.loadout), 5)
        self.assertIn("a", pc.vault)
        self.assertIn("f", pc.loadout)
        self.assertEqual(pc.stress, 1)

    def test_29_recall_fails_when_stress_is_unpayable(self):
        pc = PC(stress=6, loadout=["a"], vault=["b"])
        self.assertFalse(recall_card(pc, "b", 1))
        self.assertEqual(pc.loadout, ["a"])

    def test_30_help_an_ally_uses_highest_advantage_die(self):
        pc = PC(hope=3)
        self.assertEqual(help_ally(pc, [2, 6, 4]), 6)
        self.assertEqual(pc.hope, 0)

    def test_31_help_an_ally_requires_hope_per_helper(self):
        pc = PC(hope=1)
        self.assertIsNone(help_ally(pc, [3, 5]))
        self.assertEqual(pc.hope, 1)

    def test_32_group_action_success_and_failure_net_to_zero(self):
        self.assertEqual(group_action_modifier([True, False]), 0)

    def test_33_group_action_all_successes_add_up(self):
        self.assertEqual(group_action_modifier([True, True, True]), 3)

    def test_34_adversary_attack_uses_d20_plus_modifier_vs_evasion(self):
        self.assertTrue(adversary_attack(12, 3, 15)["hit"])
        self.assertFalse(adversary_attack(8, 3, 15)["hit"])

    def test_35_adversary_attack_rejects_non_d20(self):
        with self.assertRaises(ValueError):
            adversary_attack(21, 0, 10)

    def test_36_gm_must_have_fear_to_spend(self):
        gm = GM(fear=1)
        self.assertTrue(spend_fear(gm))
        self.assertFalse(spend_fear(gm))
        self.assertEqual(gm.fear, 0)

    def test_37_shared_pool_tokens_are_shared_and_consumed_once(self):
        pool = {}
        add_shared_pool_token(pool)
        self.assertTrue(consume_shared_pool_token(pool))
        self.assertFalse(consume_shared_pool_token(pool))

    def test_38_enemy_evolution_triggers_only_once_per_scene(self):
        state = {}
        self.assertTrue(trigger_evolution_once(state, "evolve"))
        self.assertFalse(trigger_evolution_once(state, "evolve"))

    def test_39_item_tier_cannot_exceed_character_tier(self):
        self.assertTrue(can_equip_tier(2, 2))
        self.assertFalse(can_equip_tier(1, 2))

    def test_40_loadout_limit_is_five(self):
        self.assertTrue(loadout_is_valid(list("abcde")))
        self.assertFalse(loadout_is_valid(list("abcdef")))

    def test_41_core_dataset_counts_and_expansion_isolation(self):
        manifest, data = load_core_data()
        self.assertEqual(manifest["default_ruleset"], "Daggerheart Core Set")
        self.assertEqual(manifest["categories"]["core_set"]["adversaries"], len(data["adversaries"]))
        self.assertTrue((DATA / "Hope_and_Fear").is_dir())
        self.assertNotIn("Hope_and_Fear", data)

    def test_42_all_core_json_files_parse(self):
        _, data = load_core_data()
        self.assertGreaterEqual(len(data), 10)
        self.assertTrue({"domain_cards", "weapons", "environments"} <= set(data))


    def test_43_direct_damage_still_applies_resistance_but_bypasses_armor(self):
        pc = PC(armor_slots=1)
        result = take_damage(pc, 11, direct=True, resistant=True, use_armor=True)
        self.assertEqual((result["final_damage"], result["hp_marks"], pc.armor_slots), (6, 2, 1))

    def test_44_resistance_applies_before_armor_slot(self):
        pc = PC(armor_slots=1)
        result = resolve_incoming_damage(
            pc, [{"amount": 11, "type": "phy"}],
            resistances={"phy"}, use_armor=True
        )
        self.assertEqual((result["final_damage"], result["hp_marks"], pc.armor_slots), (6, 1, 0))

    def test_45_duplicate_resistance_does_not_stack(self):
        result = resolve_incoming_damage(
            PC(), [{"amount": 11, "type": "phy"}],
            resistances=["phy", "phy"]
        )
        self.assertEqual(result["final_damage"], 6)

    def test_46_immunity_negates_matching_damage_type(self):
        pc = PC()
        result = resolve_incoming_damage(
            pc, [{"amount": 12, "type": "mag"}], immunities={"mag"}
        )
        self.assertEqual((result["final_damage"], result["hp_marks"]), (0, 0))

    def test_47_mixed_damage_gets_no_partial_defense(self):
        result = resolve_incoming_damage(
            PC(), [{"amount": 6, "type": "phy"}, {"amount": 5, "type": "mag"}],
            resistances={"phy"}
        )
        self.assertEqual((result["final_damage"], result["hp_marks"]), (11, 3))

    def test_48_mixed_damage_applies_matching_resistance_to_both_types(self):
        result = resolve_incoming_damage(
            PC(), [{"amount": 11, "type": "phy"}, {"amount": 5, "type": "mag"}],
            resistances={"phy", "mag"}
        )
        self.assertEqual((result["final_damage"], result["hp_marks"]), (9, 2))

    def test_49_simultaneous_sources_are_combined_before_thresholds(self):
        result = resolve_incoming_damage(
            PC(), [{"amount": 3, "type": "phy"}, {"amount": 3, "type": "phy"}]
        )
        self.assertEqual((result["final_damage"], result["hp_marks"]), (6, 2))

    def test_50_mixed_damage_can_be_fully_ignored_when_immune_to_both(self):
        result = resolve_incoming_damage(
            PC(), [{"amount": 6, "type": "phy"}, {"amount": 5, "type": "mag"}],
            immunities={"phy", "mag"}
        )
        self.assertEqual((result["final_damage"], result["hp_marks"]), (0, 0))

if __name__ == "__main__":
    unittest.main(verbosity=2)
