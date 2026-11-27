# GM-only Prep｜CAS-1: Trouble in Twin Lakes

> **权限：GM-only。** 本文件含模组秘密、NPC 隐藏动机、陷阱与结局信息。不得复制到 Player Notes，不得自动成为凯瑟琳的角色知识。
> **Campaign:** Twin Lakes VR / TEST_ONLY_NON_CANON
> **Module:** CAS-1: Trouble in Twin Lakes
> **System:** Cairn Second Edition (Candidate Validation only)
> **Validation ID:** CAIRN-VR-TWIN-LAKES-01
> **Prep revision:** 1
> **Prepared against:** `SOURCE/CAS1_OFFICIAL_SOURCE.md`
> **Official source:** https://github.com/yochaigal/cairn/blob/main/adventures/first-party/cas-1.md
> **Published official page:** https://cairnrpg.com/adventures/first-party/cas-1/
> **Official release page:** https://cairnpress.itch.io/trouble-in-twin-lakes
> **Verified release note:** 2026-03-31 — “Added HP for Fasha, fixed timing of events.”
> **License of source text:** CC-BY-SA 4.0; attribution is retained in the source archive.

---

## 0. Source hierarchy and unresolved source discrepancy

1. The archived upstream Markdown is the primary locally available module text. Use it before any external search during ordinary runtime.
2. Cairn's published CAS-1 page is the public official mirror.
3. Cairn Press's itch.io release page and devlogs establish published release notes.
4. The 2026-03-31 official devlog states that HP was added for Fasha and event timing was fixed.
5. **Important source discrepancy:** the currently retrievable official upstream Markdown's Fasha stat line contains STR 14, DEX 13, WIL 5 and attacks, but no HP value. The official 2026-03-31 devlog ([release note](https://yochaigal.itch.io/trouble-in-twin-lakes/devlog/1474652/added-cairn-press-logo-minor-fixes)) says HP was added. A separately hosted PDF text copy ([secondary copy](https://www.scribd.com/document/1046629213/CAS1-Trouble-in-Twin-Lakes)) shows **10 HP** for Fasha, but this copy is not the official release endpoint and the official PDF binary was not directly inspected in this pass.
6. **Current table ruling: GM_INFERENCE — Fasha 10 HP.** Evidence: secondary PDF text copy reports “10 HP, 14 STR, 13 DEX, 5 WIL”; the official devlog independently confirms that an HP value was added. This is a narrowly scoped provisional value for Fasha only. It is not to be described as official until the official 2026-03-31 PDF is directly verified. If the official PDF later differs, replace the inference through a documented correction before resolving any affected combat.
7. The online source text and the official release note are not perfectly synchronized. The 10 HP inference is corroborated but remains GM_INFERENCE, not SOURCE.

## 1. Adventure identity and premise

CAS-1 is a Cairn Second Edition adventure in the Vald setting. It contains two central mysteries that share some people and places but are **unrelated events**:

- The disappearance and murder of Aldra, the Isthmus Town butcher, tied to Fasha, Reeve Trellis, the Eye of Vuk and Vuk's attempted return.
- Jandy's repeated death at Deadmill, tied to the Echo Spark, a time loop, Annafranax and a planned Gate to the Roots.

Do not merge these into one conspiracy. Shared geography and NPC connections are deliberate cross-links, not proof of one causal chain.

The module itself says to rely especially on Cairn 2e Backgrounds and Dungeon Exploration. Due to the short distances between locations, Wilderness Procedures are unlikely to be useful; use the module's own road encounter table instead.

## 2. Opening hooks and reward contracts

### Aldra / Tideborn hook
- Tideborn offer 750gp for determining Aldra's whereabouts.
- Additional 250gp if Aldra's body is recovered and returned to a Tideborn acolyte for proper burial.
- Contact: Flavia at the Butcher in Isthmus Town.

### Jandy / Cities hook
- Cities offer 200gp per character for locating Jandy.
- Reward only if the tithe is returned intact and accounted for.
- Contact: Reeve Trellis at the Stuffed Inn.

Do not presume both hooks have been accepted. Do not pay rewards merely for finding a clue or body if the stated reward condition is unmet. Record the accepting party, exact deliverable, and eventual proof separately.

## 3. Region and spatial relationships

- Twin Lakes lies north of the Cities, reached by a few days on horseback through the Humpbacks.
- Isthmus Town is the only major settlement, on a narrow strip between two freshwater lakes; fewer than thirty families live there.
- South of town: farmland, the Farming Path, and Dunston, a defunct fishing village.
- North of town: Stone Forest, old mills and lumber paths.
- West Lake remains the healthy fish and water source.
- East Lake is depleted; East Lake Pass winds along it and through the Downs, then west toward Old Mill Road.
- White Tower Fens is a small wood east of the Downs, entered from East Lake Pass at the fork toward Old Mill Road.
- Deadmill is at the forest outskirts, approached from Old Mill Road at its south entrance.
- Bone Sump is a bog a few minutes' walk south of White Tower Fens; its mound conceals the Temple of the Fungal Lizards.
- The Temple is an underground, building-sized beetle-shaped ship.

The region map in the source is authoritative. Do not invent travel distances or a grid. Use described paths and actual travel choices.

## 4. Time and event control

Maintain a single explicit campaign clock, with day number, time of day, and elapsed time. The module's clocks are related but not interchangeable.

### 4.1 Victim schedule
The printed schedule states:
- Day 1: no victim selected.
- Day 2: roll 1d8 on Victims Table.
- Day 3: no victim selected.
- Day 4: roll 1d8 on Victims Table.
- Day 5: Vuk awakens at sunset.

Victims Table: Corsetta, Giva, Franz, Drum, Beju, Reeve Trellis, Nicolas, Flavia (results 1–8 respectively).

The narrative also says Fasha kidnaps a victim every other evening and the heart is consumed the following morning. Treat the day schedule as a set of scheduled victim-selection beats, not as permission to kidnap someone who has already been rescued, protected, moved, or otherwise made unavailable. Once a victim is secured or an event is prevented, remove that person from the eligible state and do not repeat the event.

### 4.2 Annafranax / Gate clock
- Annafranax returns to Deadmill two days after the adventure begins, in the evening.
- Unless stopped, she opens a Gate to the Roots two days after the adventure begins.
- The 2026-03-31 release note says event timing was fixed. The currently available Markdown still contains both statements. Treat the exact action time as a single scheduled beat at Day 2 evening, subject to the actual published release text; do not invent a second separate Gate-opening beat.
- If the party has already removed the Wisp Lamp, broken the loop, confronted Annafranax, or otherwise changed the prerequisites, recalculate from current facts. Do not run a stale event as if nothing happened.

### 4.3 Vuk clock
- At adventure start, Vuk has consumed Aldra's heart; two more human hearts are required.
- She cannot return to full form until three hearts have been consumed and the T10a door has been opened.
- The Day 5 sunset entry is a scheduled awakening point, not an unconditional scene teleport. Check current heart count, door state, and other module conditions.
- If the party arrives within 24 hours of Vuk's transformation, the source says she has broken free and can be found at T9. Track the actual transformation time if it occurs; do not guess the window.

### 4.4 General anti-duplication rule
For every scheduled beat, record: trigger, preconditions, current status, whether already resolved, and consequences. A prevented event becomes PREVENTED/INVALIDATED, not PENDING. Never repeat a victim selection, sacrifice, transformation, encounter, or resource loss already resolved.

## 5. Travel and road procedures

### Rumors
Roll 1d6 whenever the party leaves Isthmus Town; reroll repeated results. Rumors concern:
1. West Lake fishing and Giva's memories of East Lake.
2. The Downs and White Tower Fens.
3. Workers repairing the Crawko home in Dunston, paid by an unnamed benefactor.
4. Anti-Tideborn accusation regarding Aldra.
5. A traveler seeking the Frog Woman before the next full moon.
6. A hunter describing a foul wind from the Downs.

A rumor is a conversational encounter, not a guaranteed quest marker or proof. Deliver the speaker's words and let the players decide whether to follow up.

### Road encounters
Roll 1d6 whenever the party travels between two points; roll twice at night. This is the module-specific procedure. Do not also roll a generic Wilderness encounter for the same leg.

1. Bloodsuckers: attracted to body heat; open flame repels them. If not avoided, everyone gains Fatigue.
2. Kettlewright: sells kitchenware; may sell Fletcher's Ire for 100gp if pressed.
3. Sudden wind and floating vegetation: each character loses one resource (torch extinguished, ration dropped, shoe lost, etc.); choose a plausible resource and record exactly what changed.
4. Fish-cart ambush: if party stops to help, three bandits ambush; unprepared PCs automatically fail the DEX save. The cart is +4 slots and fine once freed; crates empty.
5. Mud: anyone traveling by foot gains Fatigue.
6. Frog trappers: spiced legs 2gp; vial of toad excretions 25gp, two uses, psychedelic and truth-serum-like.

Bandits:
- Leader: 6 HP, 2 Armor, STR 13, DEX 14, WIL 13, long sword d10 (Bulky).
- Two bandits: each 4 HP, 1 Armor, STR 12, DEX 12, WIL 9, sword d6; one has short bow d6.
- Morale saves use leader's WIL; if leader dies, bandits retreat.

Do not trigger an encounter simply because a character changes position within a location. “Between two points” means an actual travel leg. If a journey is interrupted, resolve only the leg actually undertaken.

## 6. Important NPCs: behavior and knowledge boundaries

### Reeve Trellis
- Charismatic, well-liked, ruggedly handsome; affected drawl; frequently forgets names.
- Owner of Stuffed Inn and elected town official.
- Avoids PCs where possible; works against them if they show interest in Aldra.
- Knows Jandy failed to return for the tithe; directs questions about Jandy's belongings to Drum.
- His office ledger is fake; true tithe ledger is hidden in the Inn cellar; Jandy's satchel has a matching true record.
- If his life is threatened, admits stealing from the tithe, but does not confess to Aldra's murder.
- Do not make him volunteer his complicity or reveal facts beyond what he knows.

### Fasha
- Farmer from Dunston; formerly meek and selfish, now empowered and emboldened by the Eye of Vuk.
- Official source stats: STR 14, DEX 13, WIL 5; fists d8+d8; hook knife d6.
- **HP: 10 — GM_INFERENCE (provisional).** A secondary PDF text copy gives 10 HP, and the official 2026-03-31 devlog confirms an HP value was added; the official PDF itself remains uninspected. Do not label 10 HP as official SOURCE.
- Flees toward White Tower Fens if necessary, hoping pursuers trigger traps.
- If he defeats an opponent and has the opportunity, drags them to the Temple for sacrifice.
- Do not make him fight to the death by default; his listed flight behavior is relevant.

### Aldra
- Well-liked, burly butcher, devout Tideborn, Flavia's husband.
- Saw Trellis carrying large bags from the cellar trapdoor; followed him; Fasha ambushed and killed him; body was moved to Bone Sump; heart consumed by Vuk.
- His body is preserved in the bog; chest open and heart removed.

### Flavia
- Aldra's wife and co-owner of Butcher Shop; visibly distraught but brave.
- Knows he removed a pendant with three angled squiggles before sleep; it is missing.
- Last saw him counting coins at his desk; half-finished ledger remains in locked desk drawer.
- Drawer key hangs from a small silver chain around her neck.
- Heard Fasha takes late-night walks on East Lake Pass; dislikes him.
- Can say Aldra found Giva charming despite Giva's temperament.

### Jandy
- Middle-aged, frumpy Scrivener and Cities tithingman.
- Horse and wagon remain in Isthmus Town stables, bearing Cities livery.
- Friendly with Giva; interviewed locals for a regional history.
- If rescued from loop, remembers entering Deadmill from west, seeing paddles through east window, exiting south, missing quicksand, dying and returning inside.
- Carries a tithe record in his satchel.

### Giva
- Oldest person in Isthmus Town; grumpy, dislikes most people, especially Fasha; Drum's great-aunt.
- Likes Jandy; expected him at a recent rendezvous. He said he planned to visit old lumber mills.
- Can decode the archaic Deadmill paddle instruction according to the source.
- Knows Bone Sump's location; the source says it is known only to Fasha and Giva.

### Drum
- Sarcastic, lanky teenager; works afternoons/evenings at Stuffed Inn.
- Wants to save gold to leave town; thinks Trellis is a phony.
- Knows Jandy's horse and wagon are still in the stables.
- For 15gp, shares his Deadmill witness account: teen game at Old Mill Road, popping sound, man exits south and is swallowed by ground. He does not know Jandy's full identity or the time-loop explanation.

### Annafranax
- Elder Half Witch in Stone Forest; illusion and intelligence oriented; seeks access to the Roots for curatives and lost magic; eats fungi and occasionally rude travelers.
- Stats: 9 HP, STR 11, DEX 14, WIL 17.
- Can change appearance: young auburn-haired woman or squat, amphibious figure.
- Returns to Deadmill on Day 2 evening. Very powerful and old; avoids combat if possible.
- Near-perfect knowledge of forest and its history; offers cures; always keeps her word.
- Carries four spellbooks chosen from: Animate Object, Arcane Eye, Auditory Illusion, Beast Form, Befuddle, Haste, Pacify, Push/Pull, Read Mind, Thicket, True Sight, Visual Illusion.
- The source does not specify which four. Record a deliberate GM_PREP_CHOICE before any spellbook use; do not imply an official fixed loadout.
- If killed, every bird in Stone Forest attacks her murderer until they die or flee the Wood.

## 7. Isthmus Town locations and evidence

### General
- Fewer than 30 families; market 8am–2pm daily; ordinary items under 10gp available.
- Popular goods: fishing equipment 15gp, bog shoes 10gp/pair, rainproof clothing 15gp.
- Local foods: fried cod, roasted frog legs, hot stewberry pie.

### Stuffed Inn
- Only tavern and safe traveler lodging; shared room 10gp/night including onion soup and weak beer; stabling 5gp/night.
- H-shaped building; northeast main entrance; east-side trapdoor; west stable.
- Trapdoor visible from Butcher Shop second-floor window; chained and only opens from inside unless chain is broken. Reeve has key.
- Jandy's horse and wagon are in one stable stall.
- Tavern functionally closed until 3pm; Drum and cook arrive then.
- Reeve's office: locked, Reeve has key, but lock is easily picked. Fake black tithing ledger in desk.
- Cellar door: locked; Reeve and Drum have keys.
- Cellar: tithe crates; workbench with hidden false drawer containing true ledger. Trapdoor leads to alley between Inn and Butcher, chained with brass lock; Reeve has key.

### Butcher Shop
- Adjacent two-story building; Flavia is on first floor all day.
- Butcher block hidden latch compartment holds current day's earnings (1d20 × hour of day); money is moved each evening to desk upstairs.
- Second floor: eight windows, bed, desk, Rivulus painting.
- Under bed: dagger d6, gold hilt worth 20gp.
- Desk drawer locked; Flavia holds key; contains sales ledger and 870gp.
- Painting of Rivulus worth 400gp; three squiggly lines on robe.
- Views: north Giva/Stone Forest; west Inn and basement exit; east East Lake/White Tower Fens; south town square/Farming Path.

### Giva's Home
- Single-room shack north of town; purple door and dried herbs/wolfsbane as folk protection.
- Two glasses and wine set out; Giva is waiting for Jandy, not the PCs.
- Wine worth 50gp.
- Admits Jandy missed their rendezvous nearly a week earlier.

### Farming Path and Dunston
- Farming Path runs south from town through Humpbacks toward Cities; farms/homesteads alongside.
- Dunston is a defunct fishing village.
- Fasha's farm and the abandoned home are separate investigative locations.
- The abandoned home's southwest floorboards are imperfect; a single person can climb halfway underneath. Two sacks below contain Fasha's tithe share, 200gp each. Removing them takes time and draws attention during daytime.
- Use the archived source for full room-specific facts; do not infer extra residents or services.

## 8. Deadmill and time loop

- Old gristmill at forest edge, half-sunk; approach from Old Mill Road reaches south entrance.
- South ground is unsafe quicksand. DEX Save to escape; failed save sinks further, maximum three attempts.
- Every 30 seconds the south door opens and Jandy exits, looks back, turns and falls into quicksand; the popping sound is Echo Spark recharge.
- The loop breaks by saving Jandy or freeing Echo Spark from under millstone and taking it a short distance away.
- If more than three people including Jandy are inside simultaneously, mill fully sinks; DEX Save to escape or accomplish anything notable.
- Satchel: dagger d6, notebook, tithe record, 2 Rations, Torch 3 uses, 23gp.
- Notebook contains local history/interviews with Giva, including “The Lumber Trade, a History.”
- Paddles: counter-clockwise instruction. At least two able-bodied people can manually turn paddles to move millstone enough to free Echo Spark.
- A learned ancient-text reader, Giva or Jandy can decode: “To prime, turn counter-clockwise.”
- Wisp Lamp is hidden in leaves/debris by the waterwheel. It contains a Wisp, has absorbed Jandy's repeated deaths, and the iron cage causes it pain. If freed before Annafranax returns, it flies to her home leaving a trail of fire.

## 9. White Tower Fens and Bone Sump

### Whistlewood
An almost invisible wire between trees emits a high-pitched sound only animals can hear if broken.

### Pit Trap
Hidden by leaves/debris; sharp stakes; d6 STR damage.

### Log Trap
A log crossing a small creek rotates under weight, dumping the victim into water with spinemoss. Spinemoss contact deprives the victim and impairs attacks for 1d4-1 hours.

### White Tower
- 40ft broken white tower; thick ladder; upper part missing.
- Bottom contains four-foot-deep amber liquid, acid that damages flesh for 4 STR on contact; other materials unaffected and preserved if fully immersed.
- Liquid is highly flammable and burns away in moments, leaving contents unharmed.
- Armored skeleton in chainmail: 82gp and torn silk rope 42ft.
- Oily residue stings like nettles.

### Bone Sump
- Bog and mound of grass/debris; known only to Fasha and Giva.
- Aldra's preserved body is among corpses; chest torn open, heart missing.
- Mound conceals stairs into Temple of Fungal Lizards.
- Entrance sconces contain removable diamond lights worth 150gp each, Bulky; currently off; controlled from T7.

## 10. Temple of the Fungal Lizards: topology and key state

General:
- No light; diamond sconces in room corners are off.
- Blue-black foreign alloy walls/floors cannot be chipped/broken by mundane weapons; fire and explosive powder have some effect.
- Two Surarus roam; they appear on Encounter and Environmental results from Cairn 2e Dungeon Events.

Room map links:
- T1 entrance → T2 columbarium.
- T2 connects to T4 through concealed hatch.
- T4 connects T2, T6 and T7.
- T6 secret/hatch route to T4.
- T7 controls light and T7–T8 forcefield; secret door to T4.
- T8 views T7 and T9.
- T9 connects toward T8 and T10a; West exit to T8 is blocked by fungal growth.
- T10a door leads to T10b; Curved Dagger normally opens it.

### T1 Antechamber
- Three removable statues (NW eggs, SW spores, NE veiny spore/reptilian outline); each 50gp; twisting off makes loud noise.
- SE pedestal holds only a copper-like ring remnant.

### T2 Columbarium
- Scaled-leather tube contains Watersnatch: absorbs up to wagon-load/roughly 1,000 gallons, one charge; recharge after a month and a day away from moisture.
- Pottery search takes at least two turns; can split work.
- Bird-like mummified remains in first-row pot, specialty value 150gp.
- Twisting attached urn opens hatch to T4 and makes a very loud noise; roll on Dungeon Events.
- Seams are T4 hatch; no obvious handles; too narrow for crowbar/blade.

### T3 Breeding Chamber
- Burst sacs show Suraru breeding; intact nodule is twice size, warm and pulsating.
- Fully grown Suraru inside; bursts on nearby loud noise or an Encounter result on Dungeon Events; attacks anything in sight.

### T4 Maintenance Tunnel
- U-shaped bars at corridors can be twisted to open hatches.
- Skeleton of tall bird-like humanoid, throat torn, red crest; wrapped in Moon Cloth (warm/weather resistant, Petty; can be woven into any shape in moonlight, grows one foot/hour).
- Carries Curved Dagger d6; red jewel; key to T10a; damage enhanced against Suraru Imperator.

### T5 Hall of Glyphs
Carvings show a beetle-like vessel falling from sky, winged figures emerging, lizard creatures killing humanoids and later standing over kneeling people. Present as observed images; do not give players an interpretation their characters have not earned.

### T6 Waste Disposal
- Deep well with ancient refuse at bottom.
- Nozzles activate when weight placed on drains; scalding water; one chirp warning.
- Pulling up southwest grate triggers west-wall secret hatch to T4.
- Seams also lead T4.

### T7 Light Room
- Forcefield between T7 and T8; minor shock on contact; cannot be penetrated normally.
- Pad controls forcefield; only pad or disconnecting control board disables it.
- Dial controls all room sconces.
- Extreme brightness: after one dungeon cycle all diamond bulbs explode, d4 STR damage to anyone nearby; three immediate chirps from each sconce warn. Nearby Surarus then come directly to T7.
- Removing board permanently disables sconces and forcefield; board value 500gp to Aurifex/similar.
- Small switch under board opens secret door in west wall to T4.

### T8 Preparation Room
- Grate in floor and ceiling nozzle.
- Any weight on grate triggers superheated water, 3 STR damage; single chirp warning.
- Forcefield from T7 can only be disabled in T7.

### T9 Chamber of Worship
- Two Surarus present, sleeping/eating/placing flesh by fungal growth.
- Corpses of Fasha's prior victims (except Aldra); hearts removed.
- Depending on actual day/state, one potential victim may be alive, tied and unconscious.
- If one Suraru is killed, the others attempt to wake Imperator by slashing the sac.
- Imperator's growth blocks west exit to T8.
- Suraru: 6 HP, 1 Armor, STR 14, DEX 12, WIL 5; claws d6+d6 or teeth d8. Perfect dark vision; fiercely loyal. If Imperator dies, survivors always flee to prepare a new breeding sac.
- Suraru Imperator: 10 HP, 1 Armor, STR 16, DEX 12, WIL 11; claws d8+d8 or venomous bite d6 (Blast). Brood protects sac and fights to death. Critical Damage: body part dissolves in venomous acid; target loses 1 Armor.

### T10a / T10b / Vuk
- T10a door normally opens with Curved Dagger inserted in hooked gash. Window reveals interior; thick but breakable glass. Handle opens blood-slick drawer/mail slot.
- T10b contains two hanging chains, stone block and slot/viscera. If Vuk has not returned to full form, ash cloud circles room.
- Hearts are from Fasha's victims; drawer arrangement is reciprocal: opening outside drawer closes inside drawer.
- Stone block can be broken at visible crack after several minutes; memory prism inside, Bulky, 1,000gp.
- Vuk as Ash Phantom is confined to T10b until three human hearts consumed.
- Vuk already consumed Aldra's heart at campaign start; two further hearts required.
- Full form also requires T10a door opened.
- If party arrives within 24 hours of her transformation, she may already be at T9.
- Immune to mundane attacks. Can be destroyed by submerging remains in water or destroying the memory prism; if reborn, only destroying the prism works.
- Choking Hold: envelops target, controls body for one action, then drops paralyzed body for d4 STR damage; victim suffocates unless ash expelled (STR Save).
- Memory Prism stores final moments minute by minute; longer exposure means more memories. A new death nearby replaces stored memories. Direct contact replays memories as first-hand experience.
- Current memory depicts a prisoner in T10, masked humanoids and lizard-like creature cutting their abdomen; preserve exact sensory fragment, do not add an explanation.

## 11. Relics and special items

- Eye of Vuk: Suraru never attack wearer. Every time worn, WIL Save; on failure wearer becomes more ruthless/cruel/reptilian. While worn, STR and DEX each increase by 1d4 and senses improve. Once per month wearer may fully recover STR by shedding skin. Effects end if removed for longer than a few days.
- Fletcher's Ire: heavy tungsten bar; missile attacks against targets within 30ft are Impaired; Bulky, 3 charges; recharge by bathing in molten lead furnace then cooling.
- Echo Spark: on a death in its presence, returns the dead person to about 30 seconds before death; no memory of death; one charge; recharge by crushing with elephant weight. It is caught in the Deadmill loop.
- Moon Cloth: very warm, weather-resistant, Petty; when held in moonlight can be woven into any shape, grows one foot/hour.
- Curved Dagger: d6; enhanced damage vs Imperator; key for T10a.
- Watersnatch: 1,000 gallons/wagon-load water, one charge; dry for a month and a day to recharge.
- Wisp Lamp: iron cage containing Wisp; not listed as a conventional inventory relic stat block in source; preserve its observed function and condition.
- Diamond sconces: each 150gp, Bulky.
- Memory Prism: Bulky, 1,000gp.

Do not invent item slot sizes, charges, or recharges where the source is silent; apply Cairn 2e inventory rules and clearly record any needed adjudication.

## 12. Encounter and hazard fairness

- Do not scale down traps, enemy stats, or consequences for a two-PC party.
- Do not force combat where observation, negotiation, retreat, diversion, manipulation of environment or timing are plausible.
- Do not hide an observable warning merely to create a surprise.
- Honor source-stated warnings: chirps, high-pitched wire, visible ground changes, smell, noise, light, tracks, and spatial sightlines.
- For automatic/hidden hazards, adjudicate the character's approach, visibility, attention and declared method before applying the consequence.
- For traps, distinguish the source's stated save and damage from any added interpretation. If an exact trigger or escape method is not specified, mark the ruling GM_INFERENCE.
- Keep player-facing description sensory and actionable; do not narrate secret explanations before earned.

## 13. Runtime rule-routing

- Road travel between two points: use CAS-1 road encounter table, once per leg; twice at night. Do not add generic Wilderness encounter rolls.
- Leaving Isthmus Town: separately roll rumor table; reroll duplicates.
- Temple exploration: use Cairn 2e Dungeon Exploration/Dungeon Events procedures. The two roaming Surarus are integrated into the source's Encounter and Environmental results, not added as extra free encounters every turn.
- Loud noises explicitly marked in source call for the relevant Dungeon Event roll.
- A loud noise near T3 can hatch the nodule. Do not trigger this if no noise/event condition occurred.
- The temple's cycle is Cairn Dungeon Exploration's cycle; one-cycle effects (T7 brightness) use that procedure, not arbitrary minutes.
- Wilderness procedures should not be layered on top of the module's point-to-point road procedure.

## 14. Cold-start and first-contact handoff

The module does not mandate one exact opening camera/scene. It supplies two contact points:
- Flavia / Butcher Shop for Aldra hook.
- Reeve Trellis / Stuffed Inn for Jandy hook.

Do not force a specific hook or presume both accepted. At start, establish only the location and time selected by the actual opening setup, then make the relevant NPC available with the facts they would naturally disclose. Do not stage both NPCs simultaneously unless the players choose to visit both.

First-contact cards:
- Flavia: distraught but composed; first-hand information about Aldra's disappearance, missing pendant, desk and Fasha rumors only if asked.
- Reeve: public official/innkeeper demeanor; may offer Jandy contract; do not reveal tithe theft or Aldra involvement without earned discovery.
- Drum: available afternoons/evenings; can mention wagon if asked; Deadmill witness account costs 15gp.
- Giva: at home; waits for Jandy; does not treat PCs as expected visitors.

Opening choice is still NOT SET until the player selects/accepts a scene. Do not establish initial scene time/location as CANON before “开始”.

## 15. Rules dependency checklist before play

Before any action that invokes a rule, retrieve the exact Cairn 2e rule section from the repository's system reference:
- Character creation and Backgrounds.
- Inventory slots, Bulky/Petty, Armor, weapons and item handling.
- Saves and damage to HP/STR.
- Armor reduction, HP overflow, Scars, Critical Damage and death.
- Combat turn order, DEX Saves, multiple attackers and damage dice.
- Reaction and Morale.
- Dungeon Exploration cycle and Dungeon Events.
- Light, torches, watches, food, Fatigue and Deprived.
- Spellbooks and spell use for Annafranax.
- Any Relic or condition not fully specified in CAS-1.

This Prep is a module-specific index and ruling boundary, not a replacement for Cairn rules.

## 16. Prep QA evidence boundary

The campaign's earlier records report:
- full online module text review,
- Cairn 2e rule cross-check,
- timeline/travel/event logic checks,
- 11 synthetic scene assertions and 6 time/travel assertions.

These are same-assistant self-review and synthetic checks. They are not independent blind tests and not a real player session. Keep this distinction in all reports.

## 17. Open issues

| Issue | Status | Impact | Handling |
|---|---|---|---|
| Fasha HP absent in official Markdown; secondary PDF text copy says 10 HP | GM_INFERENCE: 10 HP | Exact stat usable with explicit inference label | Verify official 2026-03-31 PDF later; if different, correct before affected combat |
| Exact four spellbooks carried by Annafranax | GM_PREP_CHOICE | Matters only if spellbook use becomes relevant | Select and record before first use; do not imply source fixed the list |
| Exact starting scene/time | NOT SET | Opening presentation | Decide at start with player input; no pre-start time advance |
| User PC and Katherine PC final cards | NOT PROVIDED | Initial resource accounting and party loadout | Wait for confirmed cards; no guessed stats or equipment |
| PDF binary archive | NOT VERIFIED | Layout/artwork/print-only details | Markdown source is archived; do not claim PDF itself stored |

## 18. Runtime discipline

- This document is GM-only.
- It does not create a game event, initialize an opening scene, or authorize play.
- Runtime State remains NOT STARTED, revision 0.
- Session Log remains empty.
- Character cards and resource ledgers remain pending.
- No game time advances until the user explicitly says “开始”.

## 19. Local Cairn rules reference and offline-first lookup

The following repository references are the first lookup path for this campaign:

- `Systems/Cairn/Rule_Reference/CORE_RULES_RUNTIME.md` — runtime rules index and normalized procedures (v0.2). Most relevant sections are marked VERIFIED_CORE, but the document itself explicitly marks attribute recovery and hirelings PARTIAL. A PARTIAL topic must be checked against the official source before a consequential ruling.
- `Systems/Cairn/Rule_Reference/CORE_RULE_INDEX.md` — navigation summary, not a substitute for full rule text.
- `Systems/Cairn/PREFLIGHT.md` — Candidate system-specific checklist, not an activation or formal-binding grant.

Official source routes retained for targeted verification only:
- Core Rules: https://cairnrpg.com/second-edition/players-guide/core-rules/
- Procedures: https://cairnrpg.com/second-edition/players-guide/procedures/
- Warden Combat: https://cairnrpg.com/second-edition/wardens-guide/combat/
- Dungeon Exploration: https://cairnrpg.com/second-edition/wardens-guide/dungeon-exploration/
- Wilderness Exploration: https://cairnrpg.com/second-edition/wardens-guide/wilderness-exploration/
- Spellbooks: https://cairnrpg.com/second-edition/wardens-guide/spellbooks/

**Offline-first policy:** During ordinary play, consult the archived module source and these local rule references first. Revisit the web only when a relevant local topic is PARTIAL/UNKNOWN, the official source is known to have changed, or an actual discrepancy appears. Do not claim the local runtime manual is a complete transcription of every official rule chapter.