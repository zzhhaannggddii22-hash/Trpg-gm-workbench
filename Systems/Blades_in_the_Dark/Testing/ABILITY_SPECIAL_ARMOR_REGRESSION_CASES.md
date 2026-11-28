# Blades in the Dark｜Special Armor Ability Regression Cases

> Primary source: user-provided Chinese core rulebook V1.3, PC ability descriptions, PDF pp.88–93.
> Type: manually reviewed expected-result cases. Not an automated test suite.

## Expected results

| ID | Situation | Expected handling | Source |
|---|---|---|---|
| ARM-01 | Cutter with Battleborn takes an attack consequence in combat and marks Special Armor to reduce harm | Reduce this instance of harm by exactly one level; do not treat it as a Resistance Roll or reduce unrelated consequences | p.88 |
| ARM-02 | Cutter with Battleborn uses Special Armor to Push in combat | Choose one normal Push benefit; do not charge the usual 2 Stress; mark Special Armor | p.88 |
| ARM-03 | Hound with Focused faces an unexpected consequence or a mental consequence such as fear, confusion, or losing someone's trail | May spend Special Armor to completely avoid that eligible consequence; do not extend this to arbitrary physical harm | p.89 |
| ARM-04 | Hound with Focused spends Special Armor to Push for ranged combat or tracking | Choose one normal Push benefit without paying 2 Stress; the named action scope still applies | p.89 |
| ARM-05 | Leech with Fortitude faces fatigue, weakness, or an alchemical-effect consequence | May spend Special Armor to completely avoid that eligible consequence; other chemical or physical consequences need their own fictional fit | p.90 |
| ARM-06 | Lurk with Shadow faces a consequence from detection or a security measure | May spend Special Armor to completely avoid that eligible consequence; it is not universal immunity to every obstacle | p.91 |
| ARM-07 | Slide with Subterfuge faces a consequence from suspicion or persuasion | May spend Special Armor to completely avoid that eligible consequence; do not expand it to unrelated social consequences | p.92 |
| ARM-08 | Spider with Mastermind protects a teammate from harm/consequence while Spider is elsewhere | May spend Special Armor; the ability explicitly allows remote use. Player narrates prior preparation that explains the protection. Resolve as canceling or reducing severity, not automatically erasing every other consequence | p.92 |
| ARM-09 | Whisper with Warded protects against a supernatural consequence while not present | May spend Special Armor remotely if the player narrates how prior protection applies; the ability can cancel or reduce severity | p.93 |
| ARM-10 | Whisper with Warded uses Special Armor to Push while confronting or using arcane forces | Choose one normal Push benefit without paying 2 Stress; mark Special Armor | p.93 |
| ARM-11 | Any of the above abilities has expended its Special Armor; Downtime begins | Restore the Special Armor at the beginning of Downtime, as the ability texts state | pp.88–93 |
| ARM-12 | A PC has ordinary Armor / Heavy Armor marked and enters Downtime | Do not restore ordinary Armor here; it returns when Load is selected for the next Score. Keep this separate from Special Armor timing | Core rules p.39; R-005 |

## Review boundary

- 12/12 cases manually compared with the corresponding ability wording and the existing R-005 resolution.
- Automated execution: not performed.
- This checks resource timing and trigger scope only; it does not validate every interaction among all Playbook and Crew abilities.
