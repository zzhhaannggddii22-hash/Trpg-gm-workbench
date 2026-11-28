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
    # Compatibility wrapper: untyped legacy test damage defaults to physical.
    resistances = {"phy"} if resistant else set()
    result = resolve_incoming_damage(
        pc, [{"amount": max(0, damage), "type": "phy"}],
        resistances=resistances, direct=direct, use_armor=use_armor
    )
    return {"final_damage": result["final_damage"], "hp_marks": result["hp_marks"]}


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



def apply_condition(state, target, name, source, tag="standard"):
    """Apply a condition once per target, retaining source and lifecycle data."""
    conditions = state.setdefault("conditions", [])
    if any(c["target"] == target and c["name"] == name and c["active"] for c in conditions):
        return False
    conditions.append({
        "target": target, "name": name, "source": source,
        "tag": tag, "active": True, "cleared_by": None,
    })
    return True


def active_condition(state, target, name):
    return any(
        c["target"] == target and c["name"] == name and c["active"]
        for c in state.get("conditions", [])
    )


def condition_effects(state, target):
    hidden = active_condition(state, target, "hidden")
    vulnerable = active_condition(state, target, "vulnerable")
    restrained = active_condition(state, target, "restrained")
    net = int(vulnerable) - int(hidden)
    return {
        "roll_state": "advantage" if net > 0 else "disadvantage" if net < 0 else "none",
        "can_move": not restrained,
        "can_act": True,
    }


def clear_condition(state, target, name, cleared_by):
    for condition in state.get("conditions", []):
        if condition["target"] == target and condition["name"] == name and condition["active"]:
            condition["active"] = False
            condition["cleared_by"] = cleared_by
            return True
    return False


def clear_temporary_condition(state, target, name, actor_kind, action_success=False, has_spotlight=False):
    condition = next((
        c for c in state.get("conditions", [])
        if c["target"] == target and c["name"] == name and c["active"] and c["tag"] == "temporary"
    ), None)
    if condition is None:
        return {"cleared": False, "spotlight_consumed": False}
    if actor_kind == "pc" and action_success:
        condition["active"] = False
        condition["cleared_by"] = "successful_action_roll"
        return {"cleared": True, "spotlight_consumed": False}
    if actor_kind == "adversary" and has_spotlight:
        condition["active"] = False
        condition["cleared_by"] = "adversary_spotlight"
        return {"cleared": True, "spotlight_consumed": True}
    return {"cleared": False, "spotlight_consumed": False}


def clear_special_condition(state, target, name, requirement_met=False):
    condition = next((
        c for c in state.get("conditions", [])
        if c["target"] == target and c["name"] == name and c["active"] and c["tag"] == "special"
    ), None)
    if condition is None or not requirement_met:
        return False
    condition["active"] = False
    condition["cleared_by"] = "specific_requirement"
    return True



RANGE_RANK = {
    "melee": 0, "very_close": 1, "close": 2,
    "far": 3, "very_far": 4, "out_of_range": 5,
}


def pc_can_reposition(distance_band, action_roll_made, agility_success=False):
    if distance_band not in RANGE_RANK:
        raise ValueError("Unknown Daggerheart range band")
    if action_roll_made and RANGE_RANK[distance_band] <= RANGE_RANK["close"]:
        return True
    return bool(agility_success)


def adversary_movement(distance_band, part_of_action=True):
    if distance_band not in RANGE_RANK:
        raise ValueError("Unknown Daggerheart range band")
    rank = RANGE_RANK[distance_band]
    if rank <= RANGE_RANK["close"]:
        return {"allowed": True, "separate_action_required": False}
    if rank <= RANGE_RANK["very_far"]:
        return {"allowed": not part_of_action, "separate_action_required": True}
    return {"allowed": False, "separate_action_required": True}


def ranged_attack_status(line_of_sight, obstruction="none"):
    if obstruction not in {"none", "partial", "total"}:
        raise ValueError("Obstruction must be none, partial, or total")
    if not line_of_sight or obstruction == "total":
        return {"allowed": False, "roll_state": "blocked"}
    if obstruction == "partial":
        return {"allowed": True, "roll_state": "disadvantage"}
    return {"allowed": True, "roll_state": "normal"}


def area_effect_targets_valid(distance_bands, origin_in_range=True):
    return bool(origin_in_range) and all(
        band in RANGE_RANK and RANGE_RANK[band] <= RANGE_RANK["very_close"]
        for band in distance_bands
    )



def begin_gm_turn(state):
    state["spotlight_side"] = "gm"
    state["gm_turn_active"] = True
    state["enemy_spotlights"] = {}
    state["total_enemy_spotlights"] = 0


def seize_spotlight(gm, state):
    if state.get("spotlight_side") != "pc" or state.get("gm_turn_active"):
        return False
    if not spend_fear(gm, 1):
        return False
    begin_gm_turn(state)
    return True


def spotlight_adversary(gm, state, enemy_id, relentless_limit=1, fear_feature_cost=0,
                        spotlight_cost_override=None):
    if not state.get("gm_turn_active") or state.get("spotlight_side") != "gm":
        return {"allowed": False, "spotlight_cost": 0, "feature_cost": 0}
    if fear_feature_cost < 0 or (spotlight_cost_override is not None and spotlight_cost_override < 0):
        raise ValueError("Fear costs cannot be negative")
    counts = state.setdefault("enemy_spotlights", {})
    count = counts.get(enemy_id, 0)
    if count >= relentless_limit:
        return {"allowed": False, "spotlight_cost": 0, "feature_cost": 0}
    extra_spotlight = state.get("total_enemy_spotlights", 0) > 0
    spotlight_cost = spotlight_cost_override if spotlight_cost_override is not None else (1 if extra_spotlight else 0)
    total_cost = spotlight_cost + fear_feature_cost
    if not spend_fear(gm, total_cost):
        return {"allowed": False, "spotlight_cost": spotlight_cost, "feature_cost": fear_feature_cost}
    counts[enemy_id] = count + 1
    state["total_enemy_spotlights"] = state.get("total_enemy_spotlights", 0) + 1
    return {"allowed": True, "spotlight_cost": spotlight_cost, "feature_cost": fear_feature_cost}




def begin_spotlighting_feature(state, feature_id, adversary_ids):
    if state.get("spotlighting_feature_active") or not adversary_ids:
        return False
    state["spotlighting_feature_active"] = True
    state["spotlighting_feature_id"] = feature_id
    state["pending_feature_spotlights"] = list(adversary_ids)
    return True


def complete_feature_spotlight(state, adversary_id):
    if not state.get("spotlighting_feature_active"):
        return False
    pending = state.get("pending_feature_spotlights", [])
    if adversary_id not in pending:
        return False
    pending.remove(adversary_id)
    if not pending:
        state["spotlighting_feature_active"] = False
        state["spotlighting_feature_id"] = None
    return True


def can_use_spotlighting_feature(state):
    return not state.get("spotlighting_feature_active", False)


def perform_extra_gm_move(gm, state):
    if not state.get("gm_turn_active") or state.get("spotlight_side") != "gm":
        return False
    if not spend_fear(gm, 1):
        return False
    state["extra_gm_moves"] = state.get("extra_gm_moves", 0) + 1
    return True


def end_gm_turn(state):
    state["spotlight_side"] = "pc"
    state["gm_turn_active"] = False
    return True




ADVERSARY_BP_COST = {
    "social": 1, "support": 1,
    "horde": 2, "ranged": 2, "skulk": 2, "standard": 2,
    "leader": 3, "bruiser": 4, "solo": 5,
}


def adversary_bp_cost(adversary_type, pc_count=None, minion_count=None):
    kind = adversary_type.lower()
    if kind == "minions":
        if pc_count is None or minion_count != pc_count:
            raise ValueError("The 1 BP Minion group must contain one Minion per PC")
        return 1
    if kind not in ADVERSARY_BP_COST:
        raise ValueError("Unknown Adversary Type")
    return ADVERSARY_BP_COST[kind]


def calculate_encounter_budget(pc_count, adversary_types, light=False,
                               all_damage_boosted=False, has_lower_tier_enemy=False,
                               harder=False):
    if pc_count < 1:
        raise ValueError("Encounter must include at least one PC")
    types = [kind.lower() for kind in adversary_types]
    base = 3 * pc_count + 2
    adjustments = {}
    if light:
        adjustments["light_or_short"] = -1
    if types.count("solo") >= 2:
        adjustments["two_or_more_solos"] = -2
    if all_damage_boosted:
        adjustments["all_enemy_damage_boosted"] = -2
    if has_lower_tier_enemy:
        adjustments["lower_tier_enemy"] = 1
    if types and not any(kind in {"bruiser", "horde", "leader", "solo"} for kind in types):
        adjustments["no_major_type"] = 1
    if harder:
        adjustments["harder_or_longer"] = 2
    return {"base": base, "adjustments": adjustments,
            "budget": base + sum(adjustments.values())}


def encounter_bp_total(entries, pc_count):
    total = 0
    for entry in entries:
        total += adversary_bp_cost(
            entry["type"], pc_count=pc_count, minion_count=entry.get("count")
        )
    return total



def advantage_state(advantage_sources, disadvantage_sources):
    net = advantage_sources - disadvantage_sources
    return "advantage" if net > 0 else "disadvantage" if net < 0 else "none"


def tick_down_countdown(state, event_id=None, amount=1):
    """Advance a Daggerheart countdown by reducing its remaining value."""
    if amount < 0:
        raise ValueError("Countdown advancement cannot be negative")
    applied = state.setdefault("applied_events", set())
    if event_id is not None and event_id in applied:
        return False
    state["value"] = max(0, state["value"] - amount)
    if event_id is not None:
        applied.add(event_id)
    return True


def advance_countdown(state, event_id, amount=1):
    """Advance a standard/long-term countdown; advancement means ticking down."""
    return tick_down_countdown(state, event_id, amount)


def advance_dynamic_countdown(state, event_id, roll_result):
    """Apply the SRD 2.0 dynamic countdown table to a progress/consequence clock."""
    progress = {
        "failure_with_fear": 0,
        "failure_with_hope": 0,
        "success_with_fear": 1,
        "success_with_hope": 2,
        "critical_success": 3,
    }
    consequence = {
        "failure_with_fear": 3,
        "failure_with_hope": 2,
        "success_with_fear": 1,
        "success_with_hope": 0,
        "critical_success": 0,
    }
    kind = state.get("type")
    if kind not in {"progress", "consequence"}:
        raise ValueError("Dynamic countdown type must be progress or consequence")
    table = progress if kind == "progress" else consequence
    if roll_result not in table:
        raise ValueError("Unknown action roll result")
    amount = table[roll_result]
    applied = tick_down_countdown(state, event_id, amount)
    return {"applied": applied, "ticks": amount if applied else 0,
            "value": state["value"], "triggered": state["value"] == 0}


def work_on_project(project, rest_state, actor_id, approved, rest_type=None,
                    starting_value=None, action_roll_result=None, event_id=None):
    """Resolve a Campaign-bound Work on a Project move during a Long Rest.

    GM approval and project complexity/value are Campaign decisions. A complex
    project uses an already-resolved Action Roll result as progress input.
    """
    if not approved:
        return {"allowed": False, "reason": "gm_approval_required"}
    if rest_type != "long":
        return {"allowed": False, "reason": "long_rest_required"}
    if not event_id:
        raise ValueError("Work on a Project requires a unique rest event ID")
    used = rest_state.setdefault("moves_used", {})
    if used.get(actor_id, 0) >= 2:
        return {"allowed": False, "reason": "downtime_move_limit"}
    if project.get("status", "active") != "active":
        return {"allowed": False, "reason": "project_not_active"}
    if "countdown" not in project:
        if starting_value is None or starting_value < 1:
            return {"allowed": False, "reason": "starting_value_required"}
        project["countdown"] = {"type": "progress", "value": starting_value}
    complexity = project.get("complexity", "simple")
    if complexity not in {"simple", "complex"}:
        raise ValueError("Project complexity must be simple or complex")
    if complexity == "complex" and action_roll_result is None:
        return {"allowed": False, "reason": "action_roll_required"}
    if complexity == "simple":
        applied = tick_down_countdown(project["countdown"], event_id, 1)
        ticks = 1 if applied else 0
        value = project["countdown"]["value"]
        triggered = value == 0
        result = {"applied": applied, "ticks": ticks, "value": value,
                  "triggered": triggered}
    else:
        result = advance_dynamic_countdown(
            project["countdown"], event_id, action_roll_result
        )
        applied = result["applied"]
    if not applied:
        return {"allowed": False, "reason": "duplicate_project_event",
                "countdown": project["countdown"]["value"]}
    used[actor_id] = used.get(actor_id, 0) + 1
    if result["triggered"]:
        project["status"] = "completed"
    return {"allowed": True, "moves_used": used[actor_id],
            "countdown": result["value"], "ticks": result["ticks"],
            "triggered": result["triggered"], "complexity": complexity}


def short_rest(state, interrupted=False, fear_roll=0, gm=None):
    if interrupted:
        return {"completed": False, "refresh": False, "gm_fear_gained": None,
                "gm_consequence_required": True}
    if state.get("short_rests_since_long", 0) >= 3:
        return {"completed": False, "refresh": False, "requires_long_rest": True}
    state["short_rests_since_long"] = state.get("short_rests_since_long", 0) + 1
    fear_before = gm.fear if gm is not None else 0
    if gm is not None:
        gm.fear = bounded(gm.fear, fear_roll, 12)
    return {"completed": True, "refresh": True,
            "gm_fear_gained": gm.fear - fear_before if gm is not None else 0}


def long_rest(state, interrupted=False, fear_roll=0, pc_count=1, gm=None,
               countdown=None, countdown_event_id=None):
    if interrupted:
        # PCs receive short-rest benefits. The SRD does not explicitly clarify
        # whether the GM still gets long-rest Fear / countdown consequences;
        # keep those un-applied pending a table ruling.
        return {
            "completed": True, "refresh": True, "long_rest": False,
            "benefit_type": "short_rest", "gm_fear_gained": None,
            "countdown_advanced": None, "gm_consequence_required": True,
        }
    state["short_rests_since_long"] = 0
    fear_before = gm.fear if gm is not None else 0
    if gm is not None:
        gm.fear = bounded(gm.fear, fear_roll + pc_count, 12)
    advanced = False
    if countdown is not None:
        advanced = tick_down_countdown(countdown, countdown_event_id)
    return {
        "completed": True, "refresh": True, "long_rest": True,
        "gm_fear_gained": gm.fear - fear_before if gm is not None else 0,
        "countdown_advanced": advanced,
    }



def apply_downtime_move(rest_state, actor_id, actor, move, rest_type,
                        tier=1, roll=1, target=None, participants=None):
    """Resolve one PC's Core Set downtime move and spend one of its two slots.

    rest_state is scoped to one rest event. Group Prepare consumes one move
    from every participant. Project-specific procedures remain outside this
    compact reference helper.
    """
    if rest_type not in {"short", "long"}:
        raise ValueError("Rest type must be short or long")
    used = rest_state.setdefault("moves_used", {})
    group = participants or [(actor_id, actor)]
    if move == "prepare":
        if any(used.get(pid, 0) >= 2 for pid, _ in group):
            return {"allowed": False, "reason": "downtime_move_limit"}
        hope_gain = 2 if len(group) > 1 else 1
        for pid, pc in group:
            used[pid] = used.get(pid, 0) + 1
            pc.hope = bounded(pc.hope, hope_gain, 6)
        return {"allowed": True, "hope_gained": hope_gain, "participants": len(group)}

    if used.get(actor_id, 0) >= 2:
        return {"allowed": False, "reason": "downtime_move_limit"}

    target = target or actor
    short_moves = {"tend_to_wounds", "clear_stress", "repair_armor"}
    long_moves = {"tend_all_wounds", "clear_all_stress", "repair_all_armor", "work_on_project"}
    allowed = short_moves | {"prepare"} if rest_type == "short" else long_moves | {"prepare"}
    if move not in allowed:
        return {"allowed": False, "reason": "move_not_available_for_rest"}

    if move in {"tend_to_wounds", "clear_stress", "repair_armor"}:
        if not 1 <= roll <= 4:
            raise ValueError("Short Rest recovery roll must be d4")
        amount = roll + tier
        if move == "tend_to_wounds":
            recovered = min(target.hp, amount)
            target.hp -= recovered
        elif move == "clear_stress":
            before = target.stress
            clear_stress(target, amount)
            recovered = before - target.stress
        else:
            recovered = min(target.armor_slots, amount)
            target.armor_slots -= recovered
    elif move == "tend_all_wounds":
        recovered = target.hp
        target.hp = 0
    elif move == "clear_all_stress":
        recovered = target.stress
        clear_stress(target, target.stress)
    elif move == "repair_all_armor":
        recovered = target.armor_slots
        target.armor_slots = 0
    else:
        return {"allowed": False, "reason": "project_move_requires_campaign_procedure"}

    used[actor_id] = used.get(actor_id, 0) + 1
    return {"allowed": True, "recovered": recovered, "moves_used": used[actor_id]}


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

    def test_22_countdown_event_is_idempotent_and_ticks_down(self):
        state = {"value": 2}
        self.assertTrue(advance_countdown(state, "roll-1"))
        self.assertFalse(advance_countdown(state, "roll-1"))
        self.assertEqual(state["value"], 1)

    def test_23_distinct_rolls_advance_countdown_separately(self):
        state = {"value": 2}
        advance_countdown(state, "roll-1")
        advance_countdown(state, "roll-2")
        self.assertEqual(state["value"], 0)

    def test_24_interrupted_short_rest_has_no_refresh(self):
        result = short_rest({}, interrupted=True)
        self.assertFalse(result["refresh"])
        self.assertIsNone(result["gm_fear_gained"])
        self.assertTrue(result["gm_consequence_required"])

    def test_25_fourth_consecutive_short_rest_requires_long_rest(self):
        self.assertTrue(short_rest({"short_rests_since_long": 3})["requires_long_rest"])

    def test_26_long_rest_resets_short_rest_counter_and_adds_fear(self):
        state, gm = {"short_rests_since_long": 2}, GM()
        long_rest(state, fear_roll=2, pc_count=1, gm=gm)
        self.assertEqual((state["short_rests_since_long"], gm.fear), (0, 3))

    def test_27_interrupted_long_rest_downgrades_to_short_rest(self):
        state = {"short_rests_since_long": 0}
        r = long_rest(state, interrupted=True)
        self.assertTrue(r["completed"])
        self.assertFalse(r["long_rest"])
        self.assertEqual(r["benefit_type"], "short_rest")

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

    def test_51_mixed_damage_can_use_different_defenses_per_type(self):
        result = resolve_incoming_damage(
            PC(), [{"amount": 11, "type": "phy"}, {"amount": 5, "type": "mag"}],
            resistances={"phy"}, immunities={"mag"}
        )
        self.assertEqual((result["final_damage"], result["hp_marks"]), (6, 2))


    def test_52_standard_condition_does_not_stack_on_same_target(self):
        state = {}
        self.assertTrue(apply_condition(state, "pc-1", "hidden", "behind-wall"))
        self.assertFalse(apply_condition(state, "pc-1", "hidden", "smoke"))
        self.assertTrue(apply_condition(state, "pc-2", "hidden", "behind-wall"))
        self.assertEqual(len(state["conditions"]), 2)

    def test_53_hidden_gives_disadvantage_and_ends_when_target_attacks(self):
        state = {}
        apply_condition(state, "pc-1", "hidden", "out-of-sight")
        self.assertEqual(condition_effects(state, "pc-1")["roll_state"], "disadvantage")
        self.assertTrue(clear_condition(state, "pc-1", "hidden", "target-attacked"))
        self.assertEqual(condition_effects(state, "pc-1")["roll_state"], "none")

    def test_54_restrained_prevents_movement_but_not_actions(self):
        state = {}
        apply_condition(state, "pc-1", "restrained", "web")
        effects = condition_effects(state, "pc-1")
        self.assertEqual((effects["can_move"], effects["can_act"]), (False, True))

    def test_55_vulnerable_gives_advantage_to_rolls_targeting_creature(self):
        state = {}
        apply_condition(state, "adversary-1", "vulnerable", "exposed")
        self.assertEqual(condition_effects(state, "adversary-1")["roll_state"], "advantage")

    def test_56_hidden_and_vulnerable_cancel_pairwise(self):
        state = {}
        apply_condition(state, "pc-1", "hidden", "darkness")
        apply_condition(state, "pc-1", "vulnerable", "opening")
        self.assertEqual(condition_effects(state, "pc-1")["roll_state"], "none")

    def test_57_pc_clears_temporary_condition_only_on_success(self):
        state = {}
        apply_condition(state, "pc-1", "pinned", "net", tag="temporary")
        failed = clear_temporary_condition(state, "pc-1", "pinned", "pc", action_success=False)
        self.assertFalse(failed["cleared"])
        passed = clear_temporary_condition(state, "pc-1", "pinned", "pc", action_success=True)
        self.assertTrue(passed["cleared"])
        self.assertFalse(passed["spotlight_consumed"])

    def test_58_adversary_clears_temporary_condition_with_its_spotlight(self):
        state = {}
        apply_condition(state, "adversary-1", "pinned", "snare", tag="temporary")
        no_spotlight = clear_temporary_condition(state, "adversary-1", "pinned", "adversary")
        self.assertFalse(no_spotlight["cleared"])
        with_spotlight = clear_temporary_condition(
            state, "adversary-1", "pinned", "adversary", has_spotlight=True
        )
        self.assertEqual((with_spotlight["cleared"], with_spotlight["spotlight_consumed"]), (True, True))

    def test_59_special_condition_requires_its_specific_requirement(self):
        state = {}
        apply_condition(state, "adversary-1", "sealed", "ritual", tag="special")
        self.assertFalse(clear_special_condition(state, "adversary-1", "sealed", requirement_met=False))
        self.assertTrue(active_condition(state, "adversary-1", "sealed"))
        self.assertTrue(clear_special_condition(state, "adversary-1", "sealed", requirement_met=True))
        self.assertFalse(active_condition(state, "adversary-1", "sealed"))


    def test_60_pc_can_move_within_close_during_action_roll(self):
        self.assertTrue(pc_can_reposition("close", action_roll_made=True))
        self.assertFalse(pc_can_reposition("far", action_roll_made=True))

    def test_61_pc_needs_successful_agility_roll_to_reposition_without_action(self):
        self.assertFalse(pc_can_reposition("close", action_roll_made=False, agility_success=False))
        self.assertTrue(pc_can_reposition("close", action_roll_made=False, agility_success=True))

    def test_62_adversary_moves_close_with_action_but_very_far_separately(self):
        close = adversary_movement("close", part_of_action=True)
        very_far = adversary_movement("very_far", part_of_action=True)
        separate = adversary_movement("very_far", part_of_action=False)
        self.assertTrue(close["allowed"])
        self.assertFalse(very_far["allowed"])
        self.assertTrue(very_far["separate_action_required"])
        self.assertTrue(separate["allowed"])

    def test_63_cover_gives_disadvantage_and_total_obstruction_blocks_ranged_attack(self):
        partial = ranged_attack_status(True, "partial")
        total = ranged_attack_status(True, "total")
        self.assertEqual((partial["allowed"], partial["roll_state"]), (True, "disadvantage"))
        self.assertEqual((total["allowed"], total["roll_state"]), (False, "blocked"))

    def test_64_area_effect_requires_all_targets_within_very_close_of_origin(self):
        self.assertTrue(area_effect_targets_valid(["melee", "very_close"]))
        self.assertFalse(area_effect_targets_valid(["melee", "close"]))

    def test_65_ranged_attack_requires_line_of_sight(self):
        self.assertEqual(ranged_attack_status(False)["roll_state"], "blocked")
        self.assertTrue(ranged_attack_status(True)["allowed"])

    def test_66_area_effect_origin_must_be_within_effect_range(self):
        self.assertFalse(area_effect_targets_valid(["melee"], origin_in_range=False))


    def test_67_successful_short_rest_gives_gm_one_d4_fear(self):
        gm = GM()
        result = short_rest({}, fear_roll=3, gm=gm)
        self.assertEqual((result["gm_fear_gained"], gm.fear), (3, 3))

    def test_68_successful_long_rest_adds_pc_count_fear_and_advances_countdown(self):
        gm, countdown = GM(), {"value": 3}
        result = long_rest({}, fear_roll=2, pc_count=2, gm=gm, countdown=countdown)
        self.assertEqual((result["gm_fear_gained"], gm.fear), (4, 4))
        self.assertTrue(result["countdown_advanced"])
        self.assertEqual(countdown["value"], 2)

    def test_69_interrupted_long_rest_gives_short_benefit_without_faking_short_rest(self):
        state, gm, countdown = {"short_rests_since_long": 2}, GM(), {"value": 3}
        result = long_rest(
            state, interrupted=True, fear_roll=2, pc_count=2,
            gm=gm, countdown=countdown
        )
        self.assertTrue(result["completed"])
        self.assertEqual(result["benefit_type"], "short_rest")
        self.assertFalse(result["long_rest"])
        self.assertIsNone(result["gm_fear_gained"])
        self.assertIsNone(result["countdown_advanced"])
        self.assertTrue(result["gm_consequence_required"])
        self.assertEqual(state["short_rests_since_long"], 2)
        self.assertEqual((gm.fear, countdown["value"]), (0, 3))


    def test_70_long_term_countdown_ticks_down_once_per_rest_event(self):
        countdown = {"value": 3}
        self.assertTrue(tick_down_countdown(countdown, "rest-1"))
        self.assertFalse(tick_down_countdown(countdown, "rest-1"))
        self.assertEqual(countdown["value"], 2)

    def test_71_rest_fear_gain_respects_gm_fear_cap(self):
        gm = GM(fear=11)
        result = short_rest({}, fear_roll=4, gm=gm)
        self.assertEqual((result["gm_fear_gained"], gm.fear), (1, 12))


    def test_72_seizing_pc_spotlight_costs_one_fear(self):
        gm, state = GM(fear=2), {"spotlight_side": "pc"}
        self.assertTrue(seize_spotlight(gm, state))
        self.assertEqual((gm.fear, state["spotlight_side"], state["gm_turn_active"]), (1, "gm", True))

    def test_73_cannot_seize_spotlight_without_fear(self):
        gm, state = GM(fear=0), {"spotlight_side": "pc"}
        self.assertFalse(seize_spotlight(gm, state))
        self.assertEqual(state["spotlight_side"], "pc")

    def test_74_first_enemy_spotlight_is_free_and_second_enemy_costs_fear(self):
        gm, state = GM(fear=2), {}
        begin_gm_turn(state)
        first = spotlight_adversary(gm, state, "bandit-a")
        second = spotlight_adversary(gm, state, "bandit-b")
        self.assertEqual((first["allowed"], first["spotlight_cost"]), (True, 0))
        self.assertEqual((second["allowed"], second["spotlight_cost"], gm.fear), (True, 1, 1))

    def test_75_relentless_two_allows_one_repeat_at_one_fear(self):
        gm, state = GM(fear=1), {}
        begin_gm_turn(state)
        first = spotlight_adversary(gm, state, "solo", relentless_limit=2)
        second = spotlight_adversary(gm, state, "solo", relentless_limit=2)
        third = spotlight_adversary(gm, state, "solo", relentless_limit=2)
        self.assertTrue(first["allowed"])
        self.assertEqual((second["allowed"], second["spotlight_cost"], gm.fear), (True, 1, 0))
        self.assertFalse(third["allowed"])

    def test_76_fear_feature_cost_is_separate_from_extra_spotlight_cost(self):
        gm, state = GM(fear=3), {}
        begin_gm_turn(state)
        spotlight_adversary(gm, state, "enemy-a")
        result = spotlight_adversary(gm, state, "enemy-b", fear_feature_cost=2)
        self.assertEqual((result["spotlight_cost"], result["feature_cost"], gm.fear), (1, 2, 0))

    def test_77_insufficient_fear_prevents_extra_enemy_spotlight_and_feature(self):
        gm, state = GM(fear=2), {}
        begin_gm_turn(state)
        spotlight_adversary(gm, state, "enemy-a")
        result = spotlight_adversary(gm, state, "enemy-b", fear_feature_cost=2)
        self.assertFalse(result["allowed"])
        self.assertEqual(gm.fear, 2)

    def test_78_gm_turn_returns_spotlight_to_pcs(self):
        state = {}
        begin_gm_turn(state)
        self.assertTrue(end_gm_turn(state))
        self.assertEqual((state["spotlight_side"], state["gm_turn_active"]), ("pc", False))

    def test_79_new_gm_turn_resets_enemy_spotlight_counts(self):
        gm, state = GM(fear=1), {}
        begin_gm_turn(state)
        spotlight_adversary(gm, state, "solo", relentless_limit=2)
        spotlight_adversary(gm, state, "solo", relentless_limit=2)
        end_gm_turn(state)
        begin_gm_turn(state)
        result = spotlight_adversary(gm, state, "solo", relentless_limit=2)
        self.assertTrue(result["allowed"])
        self.assertEqual(state["enemy_spotlights"]["solo"], 1)


    def test_80_third_short_rest_is_allowed_but_fourth_requires_long_rest(self):
        state = {"short_rests_since_long": 2}
        third = short_rest(state, fear_roll=1, gm=GM())
        self.assertTrue(third["completed"])
        self.assertEqual(state["short_rests_since_long"], 3)
        fourth = short_rest(state, fear_roll=1, gm=GM())
        self.assertTrue(fourth["requires_long_rest"])
        self.assertEqual(state["short_rests_since_long"], 3)

    def test_81_interrupted_short_rest_does_not_increment_streak(self):
        state = {"short_rests_since_long": 2}
        result = short_rest(state, interrupted=True, fear_roll=4, gm=GM())
        self.assertFalse(result["completed"])
        self.assertEqual(state["short_rests_since_long"], 2)



    def test_82_extra_gm_move_costs_one_fear_during_gm_turn(self):
        gm, state = GM(fear=1), {}
        begin_gm_turn(state)
        self.assertTrue(perform_extra_gm_move(gm, state))
        self.assertEqual((gm.fear, state["extra_gm_moves"]), (0, 1))


    def test_83_pc_can_use_at_most_two_downtime_moves_per_rest(self):
        state, pc = {}, PC(hp=3)
        self.assertTrue(apply_downtime_move(state, "pc-1", pc, "tend_to_wounds", "short", roll=1)["allowed"])
        self.assertTrue(apply_downtime_move(state, "pc-1", pc, "clear_stress", "short", roll=1)["allowed"])
        third = apply_downtime_move(state, "pc-1", pc, "repair_armor", "short", roll=1)
        self.assertEqual((third["allowed"], third["reason"]), (False, "downtime_move_limit"))

    def test_84_short_rest_tend_to_wounds_uses_d4_plus_tier(self):
        actor, ally = PC(), PC(hp=6)
        result = apply_downtime_move({}, "pc-1", actor, "tend_to_wounds", "short", tier=2, roll=3, target=ally)
        self.assertEqual((result["recovered"], ally.hp), (5, 1))

    def test_85_short_rest_clear_stress_removes_vulnerable_when_not_full(self):
        actor, target = PC(), PC(stress=6, vulnerable=True)
        result = apply_downtime_move({}, "pc-1", actor, "clear_stress", "short", tier=1, roll=2, target=target)
        self.assertEqual((result["recovered"], target.stress, target.vulnerable), (3, 3, False))

    def test_86_short_rest_repair_armor_uses_d4_plus_tier(self):
        actor, target = PC(), PC(armor_slots=5)
        result = apply_downtime_move({}, "pc-1", actor, "repair_armor", "short", tier=1, roll=2, target=target)
        self.assertEqual((result["recovered"], target.armor_slots), (3, 2))

    def test_87_prepare_solo_grants_one_hope_and_respects_cap(self):
        pc = PC(hope=5)
        result = apply_downtime_move({}, "pc-1", pc, "prepare", "short")
        self.assertEqual((result["hope_gained"], pc.hope), (1, 6))

    def test_88_group_prepare_grants_two_hope_to_each_and_spends_one_move(self):
        state, a, b = {}, PC(hope=2), PC(hope=4)
        result = apply_downtime_move(
            state, "pc-1", a, "prepare", "short",
            participants=[("pc-1", a), ("pc-2", b)]
        )
        self.assertEqual((result["participants"], a.hope, b.hope), (2, 4, 6))
        self.assertEqual(state["moves_used"], {"pc-1": 1, "pc-2": 1})

    def test_89_long_rest_tend_all_wounds_clears_all_hp(self):
        actor, target = PC(), PC(hp=6)
        result = apply_downtime_move({}, "pc-1", actor, "tend_all_wounds", "long", target=target)
        self.assertEqual((result["recovered"], target.hp), (6, 0))

    def test_90_long_rest_clear_all_stress_also_clears_full_stress_vulnerable(self):
        actor, target = PC(), PC(stress=6, vulnerable=True)
        result = apply_downtime_move({}, "pc-1", actor, "clear_all_stress", "long", target=target)
        self.assertEqual((result["recovered"], target.stress, target.vulnerable), (6, 0, False))

    def test_91_long_rest_repair_all_armor_clears_all_marked_slots(self):
        actor, target = PC(), PC(armor_slots=4)
        result = apply_downtime_move({}, "pc-1", actor, "repair_all_armor", "long", target=target)
        self.assertEqual((result["recovered"], target.armor_slots), (4, 0))

    def test_92_short_rest_move_cannot_be_used_during_long_rest(self):
        result = apply_downtime_move({}, "pc-1", PC(), "tend_to_wounds", "long", roll=4)
        self.assertEqual((result["allowed"], result["reason"]), (False, "move_not_available_for_rest"))



    def test_93_encounter_budget_base_is_three_per_pc_plus_two(self):
        self.assertEqual(calculate_encounter_budget(1, [])["budget"], 5)
        self.assertEqual(calculate_encounter_budget(4, ["solo"])["budget"], 14)

    def test_94_encounter_budget_adjustments_stack(self):
        result = calculate_encounter_budget(
            3, ["solo", "solo"], light=True, all_damage_boosted=True,
            has_lower_tier_enemy=True, harder=True
        )
        self.assertEqual(result["base"], 11)
        self.assertEqual(result["budget"], 9)

    def test_95_adversary_type_battle_point_costs(self):
        costs = [adversary_bp_cost(x) for x in
                 ["social", "support", "horde", "ranged", "skulk", "standard", "leader", "bruiser", "solo"]]
        self.assertEqual(costs, [1, 1, 2, 2, 2, 2, 3, 4, 5])

    def test_96_minion_group_costs_one_bp_only_at_pc_count(self):
        self.assertEqual(adversary_bp_cost("minions", pc_count=3, minion_count=3), 1)
        with self.assertRaises(ValueError):
            adversary_bp_cost("minions", pc_count=3, minion_count=2)

    def test_97_encounter_cost_sums_and_can_exceed_budget(self):
        entries = [{"type": "horde"}, {"type": "standard"}, {"type": "solo"}]
        self.assertEqual(encounter_bp_total(entries, pc_count=2), 9)
        self.assertGreater(encounter_bp_total(entries, 2), calculate_encounter_budget(2, ["horde", "standard", "solo"])["budget"])

    def test_98_encounter_without_bruiser_horde_leader_or_solo_gets_one_bp_adjustment(self):
        self.assertEqual(calculate_encounter_budget(2, ["standard", "ranged"])["budget"], 9)
        self.assertEqual(calculate_encounter_budget(2, ["leader", "standard"])["budget"], 8)


    def test_99_feature_granted_spotlight_does_not_double_charge_generic_cost(self):
        gm, state = GM(fear=1), {}
        begin_gm_turn(state)
        spotlight_adversary(gm, state, "enemy-a")
        result = spotlight_adversary(
            gm, state, "glass-snake", fear_feature_cost=1,
            spotlight_cost_override=0
        )
        self.assertEqual((result["allowed"], result["spotlight_cost"], result["feature_cost"], gm.fear),
                         (True, 0, 1, 0))

    def test_100_feature_granted_spotlight_still_requires_its_feature_cost(self):
        gm, state = GM(fear=0), {}
        begin_gm_turn(state)
        spotlight_adversary(gm, state, "enemy-a")
        result = spotlight_adversary(
            gm, state, "glass-snake", fear_feature_cost=1,
            spotlight_cost_override=0
        )
        self.assertFalse(result["allowed"])
        self.assertEqual(gm.fear, 0)


    def test_101_spotlighting_features_cannot_chain_while_prior_spotlights_are_active(self):
        state = {}
        self.assertTrue(begin_spotlighting_feature(state, "tactician", ["ally-a", "ally-b"]))
        self.assertFalse(can_use_spotlighting_feature(state))
        self.assertFalse(begin_spotlighting_feature(state, "ally-feature", ["ally-c"]))
        self.assertTrue(complete_feature_spotlight(state, "ally-a"))
        self.assertFalse(can_use_spotlighting_feature(state))
        self.assertTrue(complete_feature_spotlight(state, "ally-b"))
        self.assertTrue(can_use_spotlighting_feature(state))

    def test_102_spotlighting_feature_lock_only_clears_for_its_own_targets(self):
        state = {}
        begin_spotlighting_feature(state, "tactician", ["ally-a"])
        self.assertFalse(complete_feature_spotlight(state, "ally-b"))
        self.assertTrue(can_use_spotlighting_feature(state) is False)
        self.assertTrue(complete_feature_spotlight(state, "ally-a"))
        self.assertTrue(can_use_spotlighting_feature(state))


    def test_103_standard_countdown_ticks_down_and_clamps_at_zero(self):
        clock = {"value": 1}
        self.assertTrue(advance_countdown(clock, "action-1"))
        self.assertEqual(clock["value"], 0)
        self.assertTrue(advance_countdown(clock, "action-2"))
        self.assertEqual(clock["value"], 0)

    def test_104_dynamic_progress_countdown_uses_srd_advancement_table(self):
        expected = {
            "failure_with_fear": 0, "failure_with_hope": 0,
            "success_with_fear": 1, "success_with_hope": 2,
            "critical_success": 3,
        }
        for result, ticks in expected.items():
            clock = {"type": "progress", "value": 5}
            applied = advance_dynamic_countdown(clock, result, result)
            self.assertEqual((applied["ticks"], clock["value"]), (ticks, 5 - ticks))

    def test_105_dynamic_consequence_countdown_uses_srd_advancement_table(self):
        expected = {
            "failure_with_fear": 3, "failure_with_hope": 2,
            "success_with_fear": 1, "success_with_hope": 0,
            "critical_success": 0,
        }
        for result, ticks in expected.items():
            clock = {"type": "consequence", "value": 5}
            applied = advance_dynamic_countdown(clock, result, result)
            self.assertEqual((applied["ticks"], clock["value"]), (ticks, 5 - ticks))

    def test_106_dynamic_countdown_rejects_non_dynamic_types(self):
        with self.assertRaises(ValueError):
            advance_dynamic_countdown({"type": "standard", "value": 3}, "r1", "success_with_hope")

    def test_107_simple_project_uses_progress_countdown_and_completes(self):
        project, rest = {"complexity": "simple"}, {}
        first = work_on_project(project, rest, "pc-1", True, rest_type="long", starting_value=2, event_id="rest-1")
        second = work_on_project(project, rest, "pc-1", True, event_id="rest-2")
        self.assertEqual((first["countdown"], second["countdown"], project["status"]), (1, 0, "completed"))
        self.assertEqual(rest["moves_used"]["pc-1"], 2)

    def test_108_complex_project_requires_roll_and_uses_progress_table(self):
        project, rest = {"complexity": "complex"}, {}
        missing = work_on_project(project, rest, "pc-1", True, starting_value=4, event_id="rest-1")
        self.assertEqual(missing["reason"], "action_roll_required")
        result = work_on_project(
            project, rest, "pc-1", True, rest_type="long", action_roll_result="success_with_hope", event_id="rest-1"
        )
        self.assertEqual((result["ticks"], result["countdown"]), (2, 2))
        self.assertEqual(rest["moves_used"]["pc-1"], 1)


    def test_109_work_on_project_is_rejected_during_short_rest(self):
        project, rest = {"complexity": "simple"}, {}
        result = work_on_project(
            project, rest, "pc-1", True, rest_type="short",
            starting_value=2, event_id="rest-short"
        )
        self.assertFalse(result["allowed"])
        self.assertEqual(result["reason"], "long_rest_required")
        self.assertNotIn("countdown", project)
        self.assertEqual(rest.get("moves_used", {}), {})

if __name__ == "__main__":
    unittest.main(verbosity=2)
