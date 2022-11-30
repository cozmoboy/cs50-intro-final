WEAPONTYPESfantasy = ["Swords", "Axes", "Bows", "Staffs",
               "Bludgeons", "Daggers"]

WEAPONTYPESmodern = ["Pistols", "Rifles", "Explosives"]

WEAPONTYPESscifi = ["Lasers", "Electro-Blades"]

WEAPONGRADES = ["Light", "Medium", "Heavy"]


SPECIALS = [
    {"name": "Academic",
     "description": "Succeed at an INT Check to know something about esoterica (GMs discretion)."},
    {"name": "Acid Spit",
     "description": "PC's saliva will corrode metal and causes 1d6-2 damage as an attack."},
    {"name": "Adrenal Boost",
     "description": "Twice between long rests, PC may heal themselves 1d6 HPs. "},
    {"name": "Amphibious", "description": "PC is able to breathe in air or water."},
    {"name": "Animal Communication",
     "description": "The PC is able to communicate with one type of animal (e.g. - Dogs, Cats, Birds, Fish, etc.). "},
    {"name": "Animal Familiar",
     "description": "PC has an animal familiar (specify what kind) with which they can communicate telepathically."},
    {"name": "Arcane Magic",
     "description": "PC may learn and use ANY magic spell according to the Magic rules (see Magic section)."},
    {"name": "Armored", "description": "Describe natural armor: hide, scaled, carapace, etc. Character naturally decreases damage taken by 2."},
    {"name": "Backstabber", "description": "If PC makes a successful attack from behind while undetected, they inflict triple damage on the target."},
    {"name": "Banish Evil", "description": "PC causes any nearby evil NPCs of equal or fewer HPs to flee. PC must make a successful Opposed PRE Check for each. Undead creatures of up to twice PC's HP may flee but require an Opposed Check at Disadvantage."},
    {"name": "Battle Focus", "description": "When invoked, PC may make 3 attacks per turn, for two turns in a row. Usable one time between long rests."},
    {"name": "Berserk", "description": "PC goes into a reckless fighting frenzy. For duration of battle, PC may make two attacks per turn, and have Advantage on all attacks. BUT all opponents also have Advantage to hit the PC. Usable once between long rests."},
    {"name": "Biohazard Filter",
     "description": "A cybernetic implant that makes the PC immune to toxins and disease-causing pathogens."},
    {"name": "Bioluminescence", "description": "PC has glowing skin. Will illuminate small room. PC rolls 1d6 at creation, 1-3: PC can control glow on/off 4-6: PC always glows"},
    {"name": "Blast",
     "description": "PC can generate a natural blast attack. Specify type on character creation: Freeze, Fire, Electrical, Sonic, or Concussive. Specify how it shoots (e.g. - eyes, mouth, hands, etc.). DEX Check to hit. 1d6+2 damage."},
    {"name": "Bone Struts", "description": "Strong metal framing has been fused to the PC's bones. Decrease falling, crushing, and bludgeoning damage by 3 points."},
    {"name": "Brawler",
     "description": "PC does 1d6 Damage (as a Medium Weapon) when fighting unarmed or using improvised weapons and attacks with Proficiency"},
    {"name": "Burrower",
     "description": "PC can dig quickly. Not cartoon fast, but pretty fast."},
    {"name": "Calc/Info Chip", "description": "This chip implant lets the PC do lightning mathematical calculations and provides instant access to a huge encyclopedia of information."},
    {"name": "Calm",
     "description": "PC can calm a frightened, angry, or irrational NPC of equal or fewer HPs with a successful PRE Check. More powerful creatures require a roll at Disadvantage. (n.b. - Not all enemies are angry, irrational, or frightnened.)"},
    {"name": "Chameleon Skin", "description": "PC can change their skin tone to blend into patterned surroundings or disguise themselves: highlights, hair color, and eye color, etc. Advantage on stealth and disguise Checks."},
    {"name": "Charge Attack", "description": "With a proper run, the PC can make a charge melee attack with Advantage, doing 1d6+3 damage."},
    {"name": "Charm Beast", "description": "PC can calm a frightened or angry animal or beast of equal or fewer HPs with a successful PRE Check. More powerful creatures require a PRE Check at Disadvantage."},
    {"name": "Charming",
     "description": "PC has Advantage on PRE Checks when being silver tongued."},
    {"name": "Clairvoyance",
     "description": "PC can perceive distant people, objects, locations, and events with ESP."},
    {"name": "Climber", "description": "PC has advantage on DEX Checks involving climbing."},
    {"name": "Cold Blooded", "description": "The PC's body temperature always matches the surrounding air. The PC is invisible in infrared."},
    {"name": "Command", "description": "PC may command any NPC of equal or fewer HPs to perform a simple task with successful PRE Check. Usable once between long rests."},
    {"name": "Contortionist",
     "description": "PC can squeeze into and through small spaces."},
    {"name": "Cryokinetic", "description": "PC can lower the temperature of or freeze objects with their mind. GM determines strength."},
    {"name": "Cyber-Enhanced Hearing", "description": "An implant allows the PC to hear tiny and distant sounds with ease and filter out any selected sounds. Grants immunity to ear damage by sonic attack."},
    {"name": "Cyber-Enhanced Vision",
     "description": "The PC can see infrared, ultraviolet, electrical fields, in low light, and has a binocular mode for distance."},
    {"name": "Danger Sense",
     "description": "PC can sense imminent danger, is never surprised, and always goes first in combat."},
    {"name": "Deadeye", "description": "PC starts with Advantage on ranged attacks and may add or subtract 1 from either or both dice on the Hit Location Chart."},
    {"name": "Decapitate", "description": "When the PC makes a successful attack with a blade or axe, and the Danger Die shows a 6, the target is decapitated."},
    {"name": "Demolitions", "description": "Allows the safe improvisation of explosives, handling of explosives, and knowledge of where to place them. Any PC without this knowledge has a must make an INT check at Disadvantage to avoid blowing themselves up at any particular stage of explosive handling."},
    {"name": "Detect Evil", "description": "PC can detect the presence of Evil."},
    {"name": "Detect Traps",
     "description": "With a successful INT Check, PC can detect whether an object is boobytrapped."},
    {"name": "Disarm Traps",
     "description": "With a successful DEX Check, PC can disarm a known trap."},
    {"name": "Disguise", "description": "With proper materials, the PC can attempt to disguise themselves. Requires successful PRE Check for each person who sees the disguise."},
    {"name": "Distance Vision",
     "description": "PC's can see as if they were using binoculars."},
    {"name": "Dodger", "description": "PC is good at avoiding attack. Attackers suffer a Disadvantage on combat Checks."},
    {"name": "Driver", "description": "PC can drive any land vehicle and has Advantage on all related Checks."},
    {"name": "Durability", "description": "Hero's body is tough, either like rubber or steel. All damage taken is reduced by 2."},
    {"name": "Echolocation", "description": "PC can make inaudible peeps and use external noises to “see” in the dark. Even works in magical darkness."},
    {"name": "Elasticity", "description": "PC is like silly-putty and can stretch their head, neck, limbs, and torso up to 3 times normal length, flatten them, make them skinny, twist them, or change their shape."},
    {"name": "Electrical Discharge",
     "description": "Once per day (between long rests), PC can discharge an electrical burst on touch, or in a bolt up to 3m. Both do 2d6 damage. A Ranged electrical attack must roll DEX Check to hit. A touch attack hits automatically. In either case, anyone touching the target is also damaged."},
    {"name": "EMF Regen", "description": "An implanted cyber-organ regenerates the PC 6HP per hour of exposure to electrical fields as would be found near any home wiring or electrical circuits."},
    {"name": "Empath", "description": "PC has a heightened sense for what another is feeling. Grants the ability to detect lies."},
    {"name": "Endurance", "description": "PC can run much further, or exert themselves longer, than normal characters."},
    {"name": "Extra Attack",
     "description": "PC may make an extra attack instead of moving during their turn."},
    {"name": "Extra Body Parts",
     "description": "PC has 1 - 3 fully functional extra body parts, player's choice, subject to GM approval."},
    {"name": "Extra Claws", "description": "PC has a set of appropriately sized claws besides whatever limbs they already have. In combat, they act as medium weapons."},
    {"name": "Extra HP", "description": "PC starts the game with a boost to Health Points."},
    {"name": "Extra Large", "description": "PC is twice the average size of their species and has 6 extra HP. This may make the PC easier to hit."},
    {"name": "Extra Limbs", "description": "PC has 1 - 3 extra arms or legs."},
    {"name": "Extra Small", "description": "PC is one quarter the average size of their species. This may make the PC harder to hit."},
    {"name": "Fan the Hammer", "description": "When using a revolver, the PC may take 3 shots in a turn, each at Disadvantage. Each shot may have a different target."},
    {"name": "Fast Talker", "description": "PC may Check PRE with Advantage to persuade someone of something not-quite-right. When successful, effects are short-lived."},
    {"name": "Fear", "description": "PC may cause fear in target. Requires opposed PRE Check. Success causes target to flee in panic. Useable once between long rests."},
    {"name": "Finger Laser", "description": "The PC's finger shoots fine laser beam. 1d6 damage. May be used as a cutter, with patience."},
    {"name": "Flight", "description": "PC can fly without wings at twice their normal ground speed."},
    {"name": "Force Shield", "description": "The PC can create an invisible, spherical force field of up to 1m radius around themselves. Only objects the PC allows through can pass. Lasts for 3 turns in combat, or 3 minutes otherwise. Useable twice between Long Rests."},
    {"name": "Gambler",
     "description": "Roll 6 dice instead of five when dealt a poker hand (see Poker Rules pg [pg#])."},
    {"name": "Genius", "description": "INT is 7 and PC also gets Advantage on all related rolls."},
    {"name": "Gills", "description": "The character has gills and can breathe underwater."},
    {"name": "Good Looking", "description": "PC is exceptionally good looking giving Advantage or Disadvantage where appropriate."},
    {"name": "Grip", "description": "Only an extraordinary force can break the PC's grip. Character will not fall from a rope or tree, or drop an item accidentally, if they are gripping it solidly. "},
    {"name": "Guitar & Singin'", "description": "PC is a meadow lark. Specify what instrument the PC plays. Advantage on related rolls when singing and/or playing."},
    {"name": "Gyro Stabilizer", "description": "Tiny stabilizing mechanism inserted in the brain. The PC's DEX is effectively 6 when making balance related Checks."},
    {"name": "Heal Wounds", "description": "PC can restore 6 HPs to any PC or NPC by touch. Usable once between long rests. Cannot be used to raise the dead."},
    {"name": "Heat Vision",
     "description": "PC has wider vision spectrum and can see in infrared and ultra-violet. "},
    {"name": "Heightened Balance",
     "description": "PC has Advantage on DEX rolls involving climbing, balancing, tumbling."},
    {"name": "Heightened Senses", "description": "PC has better than average sensed, and gains Advantage on PRE Checks related to detecting and noticing things."},
    {"name": "Heightened Smell", "description": "PC has a dog's sense of smell. May be used for tracking, finding, and detecting. If a dog could do it, so can the PC."},
    {"name": "Heightened Smell", "description": "PC has a dog's sense of smell. Can be used for tracking, finding, and detecting. If a dog can do it, so can the PC."},
    {"name": "Hold Breath", "description": "PC can hold their breath for 15 minutes."},
    {"name": "Horns", "description": "PC has large horns that count as medium weapons in combat, doing 1d6 damage."},
    {"name": "Horsemanship",
     "description": "PC gets Advantage on Checks dealing with horses and horseback riding."},
    {"name": "Hypnotic Suggestion", "description": "With a successful Opposed PRE Check, the PC can psychically make a victim do as he is told for 3 turns. After every 3 turns, they must make another Check. Once the spell is broken with a failed Check, it cannot be reestablished for 24 hours. Can be used on one person between long rests."},
    {"name": "Immunity", "description": "PC suffers no damage from certain effects. Choose at character creation: Fire, Cold, Electricity, Poison, Disease, or Radiation."},
    {"name": "Improvise Weapon",
     "description": "PC may use any reasonable item as a Medium Weapon for 1d6 damage."},
    {"name": "Internal Compass",
     "description": "PC will never get lost, and always knows what direction they're facing."},
    {"name": "Intimidate",
     "description": "PC makes PRE Checks with Advantage when trying to intimidate."},
    {"name": "Invisibility", "description": "PC can become invisible at will and cannot be seen for 5 minutes under normal conditions, or 3 turns in combat, unless they attack an enemy. Useable 3 times between Long Rests. The effect includes clothes and possessions."},
    {"name": "Leader", "description": "PC gains Advantage on PRE Checks when trying to convince a group to take action."},
    {"name": "Leap", "description": "PC can leap 3m vertically or 5m horizontally."},
    {"name": "Leg Servos", "description": "Implanted motors and strengthened bones allow the PC to run 3 times as fast, leap 5m vertically or horizontally, and jump down from up to 10m without injury."},
    {"name": "Levitate", "description": "PC can levitate themselves and whatever they're carrying straight up and straight down and hold in place."},
    {"name": "Liquid/Gas Form",
     "description": "PC can change to liquid or gas form at will. Choose which at character creation."},
    {"name": "Locking Jaw", "description": "Once their jaw clamps onto something, PC cannot be forced to let go unless dead or unconscious."},
    {"name": "Locksmith",
     "description": "With proper tools, the PC can pick a lock on a successful DEX Check."},
    {"name": "Magnetic Control",
     "description": "PC can attract and repel small pieces of metal up to 5m away."},
    {"name": "Martial Arts", "description": "PC may make unarmed melee attacks using a DEX Check instead of STR. Martial Arts attacks do 1d6 damage."},
    {"name": "Medic", "description": "Given time and proper materials, PC can heal 1d6 HPs to an injured PC or NPC. Typical medic's bag contains supplies for three uses."},
    {"name": "Memory Card", "description": "This insertable card acts as photographic memory. The PC will never forget information gathered. They may also download memories and information from other Memory Cards or share their own with any PC's who have the same enhancement."},
    {"name": "Mind Blast", "description": "PC blasts a mental attack that automatically hits for 1D6+2 damage. The victim is stunned 1d6 turns. Useable 2 times between long rests."},
    {"name": "Naked Fighter", "description": "When the PC has a lot of skin showing, they effectively have Medium Armor, and all damage is reduced by 2 HP."},
    {"name": "Natural Armor", "description": "PC's skin is tough. Depending on the PC, it may look and feel normal skin, it may be a tough hide, a carapace, a shell, or it may be something else. Describe what it looks and feels like. It acts as medium armor for 2 HP of damage reduction."},
    {"name": "Nature Magic",
     "description": "PC may learn and use Nature Magic spells according to the Magic rules (see Magic section)."},
    {"name": "Night Vision",
     "description": "PC's vision works as well in the dark as it does during the day."},
    {"name": "Olfactory Array", "description": "The PC's olfactory implant gives them super-sniffing strength equal to that of a dog. It also parses the incoming data and will help them identify what they smell."},
    {"name": "Oversized Body Parts",
     "description": "Some aspect of the PC's body is beneficially oversized. Specify (player's choice, subject to GM approval)."},
    {"name": "Photosynthetic", "description": "PC's skin generates nutrition from exposure to sunlight and heals 1d6 HP of damage per hour of exposure."},
    {"name": "Pick Pocket",
     "description": "PC can pick a pocket with a successful DEX Check. Failure means discovery."},
    {"name": "Pilot",
     "description": "PC can fly a plane, helicopter, or spaceship (specify)."},
    {"name": "Poisonous",
     "description": "PC has a Poisonous Bite, Sting, or Skin (specify). Their venom deals 1d6 damage per turn for 1d6 turns. Useable twice between long rests."},
    {"name": "Pounce", "description": "If attacking while hiding undetected, the PC's attack, armed or unarmed, does 2d6 damage."},
    {"name": "Prehensile Nose", "description": "PC has a nose like an elephant. "},
    {"name": "Prehensile Tail",
     "description": "PC can hold objects with or hang by their tail. Not good for fine manipulation."},
    {"name": "Project Illusion",
     "description": "PC can create an illusion that will last 3 turns. Must make a successful PRE Check for each victim."},
    {"name": "Psychic Healer",
     "description": "PC may heal any character for 1d6 HPs with a touch. Useable twice between long rests."},
    {"name": "Psychic Vampire", "description": "On successful opposed PRE Check, target takes 1d6 damage, and mutant is healed by the same amount. Useable twice between long rests."},
    {"name": "Psychometry",
     "description": "The PC can learn things about the past of an object by touching it."},
    {"name": "Pyrokinesis", "description": "PC can create and manipulate fire with their mind: heat objects, cause objects to ignite. With continued focus, targets can be burned for 1d6 burning damage per turn."},
    {"name": "Quickdraw",
     "description": "Gives the PC Advantage to the Draw Phase of a showdown (see Showdown rules pg [pg#])."},
    {"name": "Quills", "description": "PC is covered with quills. Anyone coming into forceful contact with PC takes 1d6 piercing damage."},
    {"name": "Rage Transformation", "description": "When PC is wounded for the first time, the initial damage is removed and they enter Rage Stage: STR = 7, Advantage on melee and brawling attacks, Disadvantage on Ranged attacks, except for big, thrown objects. While in Rage State, the PC cannot invoke other powers and Specials, and must attack, or move to attack, every turn. A PC may try to resist entering Rage State by succeeding at a PRE Check, but must continue to make a Check every time they are injured. Rage State subsides after all threats are gone."},
    {"name": "Rampage/Battle Fury",
     "description": "Upon killing an enemy, the PC may immediately make an extra attack."},
    {"name": "Read Languages",
     "description": "PC can get the gist of something written in a foreign language on a successful INT roll."},
    {"name": "Reader of People",
     "description": "The PC can get a sense of an NPC's motivation or detect lying with a successful PRE Check. "},
    {"name": "Regenerate Limbs",
     "description": "PC will regrow lost limbs over a 5-day period."},
    {"name": "Regeneration",
     "description": "As an Action, the PC can heal themself 1d6 HP per turn at will."},
    {"name": "Repulsive Spray", "description": "PC can spray a very bad-smelling chemical cloud. Anyone caught in it must make a PRE Check. Those who fail will be disoriented and flee."},
    {"name": "Restore Health", "description": "Once between long rests, PC may heal themselves completely. All HPs are restored, and any disease or sickness is cured."},
    {"name": "Retractable Claws",
     "description": "PC has retractable claws or blades that function as a medium weapon in combat."},
    {"name": "Shapeshift - Animal", "description": "PC can take the form of an animal. Choose an animal type at character creation. Change does not include clothing or belongings."},
    {"name": "Shapeshift - People",
     "description": "PC can take the form of any another person. Does not include clothing."},
    {"name": "Shapeshift - Size", "description": "Hero may shrink to 1/100th of normal size, or expand to 5 times normal size. Scaling is proportional. GM will judge how to adjust combat capabilities accordingly. Does not apply to belongings or clothing. Useable twice between long rests."},
    {"name": "Sleep Wave", "description": "PC can make a visible target fall sound asleep with a successful PRE Check. Usable once between long rests."},
    {"name": "Speak With Animals",
     "description": "PC can communicate with animals in simple concepts."},
    {"name": "Speed", "description": "PC's running Speed is tripled, and they may attack twice per turn in combat."},
    {"name": "Stealth Magic",
     "description": "PC may learn and use Stealth Magic spells according to the Magic rules (see Magic section)."},
    {"name": "Stealthy", "description": "PC makes sneaking and hiding DEX rolls at Advantage."},
    {"name": "Sticky", "description": "PC's skin can stick to things like walls and ceilings."},
    {"name": "Sticky Tongue", "description": "PC has a sticky, 2m long tongue and can snatch things with it on a successful DEX Check."},
    {"name": "Strength Booster", "description": "An implanted chemical micro-factory can boost the PC's STR to 7 for 1 minute. STR Checks succeed on 3 - 6, and they can turn over a car. Useable Once between long rests."},
    {"name": "Strong", "description": "The PC is stronger than their STR would suggest. STR remains the same, but PC gets Advantage on all non-combat STR rolls."},
    {"name": "Super Digestion", "description": "PC is immune to most toxins, poisons, and digestive illnesses, and can eat things that might make a normal character sick."},
    {"name": "Super Strength", "description": "PC's STR is 8. STR Checks succeed on 3 - 6. They get Advantage on all rolls involving feats of strength and can flip over a car."},
    {"name": "Survival", "description": "Given time in normal terrain, the PC can find a meal for 5 PCs with a successful INT roll."},
    {"name": "Swift", "description": "PC gains advantage on running, chasing, etc."},
    {"name": "Swimmer", "description": "PC knows how to swim very well and gets Advantage on related Checks."},
    {"name": "Telekinesis",
     "description": "The PC can manipulate objects with the mind: lift, bend, even break."},
    {"name": "Telepathy", "description": "PC can transmit or receive thoughts psychically."},
    {"name": "Teleport", "description": "PC can teleport to any spot he can see. Use twice between long rests."},
    {"name": "Tentacles", "description": "PC has up to 8 prehensile tentacles as well as, or instead of, their normal limbs."},
    {"name": "Tinker", "description": "PC can understand and repair machines and electronics with a successful INT check. Given time and resources, they may even invent and build interesting gadgets, with GM approval."},
    {"name": "Tough", "description": "PC is very rugged. Add 4 extra HPs at character creation, and every time they reach a new level."},
    {"name": "Tracker", "description": "PC can track others, under normal conditions, on a successful INT roll."},
    {"name": "True Strike", "description": "Causes a ranged or melee attack to automatically hit for double damage. Usable once per Combat."},
    {"name": "Truth", "description": "PC may force anyone to tell the truth. Requires a successful PRE Check. Useable once between Long Rests"},
    {"name": "Tusks", "description": "PC has long tusks like a warthog. They function as a medium weapon in combat."},
    {"name": "Two Gun", "description": "PC can use either hand to shoot without Disadvantage, or can shoot two pistols per turn"},
    {"name": "Ugly", "description": "PC is exceptionally ugly. Advantage/Disadvantage where appropriate."},
    {"name": "Unsavory Contacts",
     "description": "PC has access to underworld information. Given time, opportunity, and a successful INT Check, certain answers may surface (GM's discretion)."},
    {"name": "Virtue Magic",
     "description": "PC may learn and use Virtue Magic spells according to the Magic rules (see Magic section)."},
    {"name": "Weapon Mastery (specify)",
     "description": "Specify a weapon type. Chosen weapon type is wielded with Advantage on attack rolls."},
    {"name": "Web Maker", "description": "PC can spin webs from a special gland. Specify where this gland is at character creation. The webs are good for trapping and holding things."},
    {"name": "Wings", "description": "PC has wings and can fly."}
]

SPELLS = [

    {"name": "Air Diver",
     "level":  5,
     "description": "Target can swim through the air."},

    {"name": "Amputate",
     "level":  3,
     "description": "Any of the caster's body parts may be de-tached and reattached at will, without causing pain or damage. Caster can still control them."},

    {"name": "Animate Dead",
     "level":  7,
     "description": "L skeletons rise from the ground to serve the caster. Very stupid and can only obey simple orders."},

    {"name": "Animate Object",
     "level": 3,
     "description": "And object becomes flexible and obeys the caster's commands as best it can."},

    {"name": "Army",
     "level": 3,
     "description": "Caster gains up to L extra arms."},

    {"name": "Arrow",
     "level":  1,
     "description": "Caster shoots L magic arrows, each doing 1d6 damage. Specify targets."},

    {"name": "Babble",
     "level":  5,
     "description": "Caster can understand all languages."},

    {"name": "Beast Form",
     "level":  3,
     "description": "Target and possessions transform into any common animal."},

    {"name": "Bigger",
     "level":  1,
     "description": "Targeted creature doubles in size, and does double damage."},

    {"name": "Bind",
     "level":  6,
     "description": "Paralyses 1d6 targets within 10m of the caster."},

    {"name": "Bloodhound",
     "level":  1,
     "description": "Caster's sense of smell becomes heightened, comparable to that of a dog."},

    {"name": "Body Swap",
     "level":  5,
     "description": "Caster switches bodies with touched creature or character. If one dies, the other dies as well."},

    {"name": "Bramble",
     "level":  4,
     "description": "Targeted area up to 100m in diameter is suddenly overgrown with impassable vegetation."},

    {"name": "Calm",
     "level":  2,
     "description": "Target is relieved of fear."},

    {"name": "Charm",
     "level":  5,
     "description": "L creatures treat caster like a friend."},

    {"name": "Cloak",
     "level":  6,
     "description": "L creatures become invisible until they move or the spell ends."},

    {"name": "Cold Blast",
     "level":  4,
     "description": "Caster shoots a freezing cloud from hands. Any creature in front of caster within 10m takes Lx1d6 damage. All liquid is frozen."},

    {"name": "Command",
     "level":  5,
     "description": "Target creature obeys one single, three-word command that will not cause self-harm."},

    {"name": "Conflagration",
     "level":  10,
     "description": "Enormous explosion of flame consumes a targeted area 15m in diameter. Anything in the area takes 6d6 fire damage."},

    {"name": "Confuse",
     "level":  3,
     "description": "L creatures of caster's choice become highly confused and cannot figure out what is going on."},

    {"name": "Control Weather",
     "level":  5,
     "description": "The caster may change the type of weather, but does not otherwise control it."},

    {"name": "Counterspell",
     "level":  6,
     "description": "Make and opposed INT check against the caster of a nearby spell. On success, caster may cancel the spell. Counterspell may be used on out of turn as a reaction, or against an ongoing magical effect."},

    {"name": "Cure Disease",
     "level":  4,
     "description": "Removes all diseases from target."},

    {"name": "Cure Light Wounds",
     "level":  1,
     "description": "Targeted creature is healed 1d6 HP."},

    {"name": "Cure Poison",
     "level":  3,
     "description": "Cures target of all poisonings."},

    {"name": "Cure Serious Wounds",
     "level":  4,
     "description": "Targeted creature is healed 3d6 HP."},

    {"name": "Darkness",
     "level":  2,
     "description": "Targeted point is surrounded by a magical darkness with a radius of 20m. Nothing will light it, and no vision can see through it."},

    {"name": "Darkvision",
     "level":  3,
     "description": "Caster can see in total non-magical darkness."},

    {"name": "Deafen",
     "level":  3,
     "description": "All creatures in a 10m radius of the caster become temorarily deaf."},

    {"name": "Describble",
     "level":  1,
     "description": "Caster can read any writing."},

    {"name": "Detect Evil",
     "level":  1,
     "description": "Caster can sense evil in a creature, or the presence of unseen evil within 20m."},

    {"name": "Detect Foes",
     "level":  2,
     "description": "All enemies, even invisible ones, glow a green that can be seen through walls."},

    {"name": "Detect Magic",
     "level":  2,
     "description": "Magical items and effects emit a glow that the caster can see."},

    {"name": "Disenchant",
     "level":  10,
     "description": "Targeted item is permanently stripped of all magic and magical effects."},

    {"name": "Disguise",
     "level":  3,
     "description": "Caster may change the looks of L characters, so long as they remain humanoid in appearance. Any attempt to look like a specific individual is easily detected by anyone knowing them."},

    {"name": "Disintegrate",
     "level":  12,
     "description": "Instantly reduces target to dust."},

    {"name": "Dispel",
     "level":  5,
     "description": "Dispels L targeted summoned creatures."},

    {"name": "Dispel Magic",
     "level":  3,
     "description": "Ends the effect of one caster's spell. Does not affect magically enchanted items."},

    {"name": "Displace",
     "level":  2,
     "description": "An object appears to be up to Lx10' from its actual position."},

    {"name": "Door",
     "level":  3,
     "description": "Causes a door-sized opening to appear in targeted wall up to 3m thick."},

    {"name": "Dopplegang",
     "level":  3,
     "description": "Target person transforms into a perfect duplicate of a touched individual."},

    {"name": "Earify",
     "level":  1,
     "description": "Greatly amplifies caster's hearing."},

    {"name": "Earthquake",
     "level":  10,
     "description": "The ground for 100m around the caster shakes violently. Structures may be damaged or collapse."},

    {"name": "Elemental Servant",
     "level":  5,
     "description": "Summons an elemental of specified type to do caster's bidding."},

    {"name": "Enchant Weapon",
     "level":  3,
     "description": "Targeted weapon grants advantage to attacks."},

    {"name": "Ethereal Tunnel",
     "level":  7,
     "description": "Must be cast on an object ahead of time. When cast again, the spell opens twin doors connected through the ethereal plane: one at caster's location, the other at the location where the object was left."},

    {"name": "Eye of the Sorcerer",
     "level":  1,
     "description": "Caster can see through a magical eyeball that flies around at their command."},

    {"name": "Fear",
     "level":  3,
     "description": "L nearby targeted enemies must make a PRE check. If they fail, they flee in terror."},

    {"name": "Feather Fall",
     "level":  1,
     "description": "Target will float gently to the ground rather than plummet."},

    {"name": "Feeblemind",
     "level":  4,
     "description": "Target is reduced to animal intelligence."},

    {"name": "Find Traps",
     "level":  3,
     "description": "Causes all nearby traps to glow a blue light."},

    {"name": "Fireball",
     "level":  5,
     "description": "Shoots ranged ball of fire, 3m in diameter. 3d6 damage to anyone in the area."},

    {"name": "Flame",
     "level":  2,
     "description": "Flames shoot from caster's hands. All targets in nearby arc take 1d6 damage."},

    {"name": "Fly",
     "level":  3,
     "description": "Caster can fly at normal walking speed."},

    {"name": "Fog",
     "level":  2,
     "description": "A dense fog spreads out from the caster."},

    {"name": "Freeze",
     "level":  1,
     "description": "Ice spreads out from caster's touch, up to L.10ftin radius."},

    {"name": "Freeze Time",
     "level":  10,
     "description": "Time stops for everything except the caster within a 100m radius."},

    {"name": "Frenzy",
     "level":  5,
     "description": "L targeted creatures become violently frenzied, and will attack the person or creature nearest to them."},

    {"name": "Great Warding",
     "level":  10,
     "description": "Target is impervious to all enemy magic."},

    {"name": "Greed",
     "level":  5,
     "description": "L targeted creatures are siezed by an overwhelming urge to possess a visible item of the caster's choice."},

    {"name": "Haste",
     "level":  1,
     "description": "Caster's walk and run speed is tripled."},

    {"name": "Hole",
     "level":  1,
     "description": "A hole appears at target with a diameter of up to Lx1m and up to Lx2m deep."},

    {"name": "House of Mirrors",
     "level":  3,
     "description": "Up to L illusory duplicates of the caster appear and are under their control."},

    {"name": "Hover",
     "level":  3,
     "description": "Target object hovers frictionless 1m above the ground. It will support up to Lxhumanoids weight."},

    {"name": "Humanimal",
     "level":  4,
     "description": "Target animal gians either human intelligence or human appearance for up to L hours."},

    {"name": "Illusion",
     "level":  2,
     "description": "A silent, immobile, illusion of your choice appears, up to the size of a bedroom."},

    {"name": "Illusory Clone",
     "level":  4,
     "description": "L illusions of the caster appear. Each vanishes if attacked."},

    {"name": "Invisibility",
     "level":  4,
     "description": "Targeted creature becomes invisible until spell ends or it attacks."},

    {"name": "Knock",
     "level":  3,
     "description": "Unlocks one common or magical lock on touch."},

    {"name": "Lay Waste",
     "level":  12,
     "description": "2d6 targeted creatures within a 10m radius of the caster immediately die."},

    {"name": "Leap",
     "level":  1,
     "description": "Caster can leap Lx10' horizontally or vertically."},

    {"name": "Levitate",
     "level":  2,
     "description": "Caster can float strait up or straight down."},

    {"name": "Light",
     "level":  1,
     "description": "Targeted object casts a soft light."},

    {"name": "Lightning",
     "level":  3,
     "description": "Caster shoots a lightning bolt. 2d6 damage."},

    {"name": "Luminesce",
     "level": 3,
     "description": "Touched object permanently radiates a bright light."},

    {"name": "Malice",
     "level":  6,
     "description": "L targeted creatures suddenly hate another targeted creature or group and wish to destroy them."},

    {"name": "Manse",
     "level":  8,
     "description": "A sturdy, furnished cottage appears for 24 hours. Caster may permit and forbit entry at will."},

    {"name": "Massive Gravity",
     "level":  3,
     "description": "The gravity is tripled in a 10m radius around the caster."},

    {"name": "Mirrorway",
     "level":  8,
     "description": "Targeted mirror becomes a door to another mirror that the caster looked into during the past 24 hours."},

    {"name": "Monstrosity",
     "level":  5,
     "description": "An object grows to the size of an elephant. If it is an animal, it is enraged."},

    {"name": "Muddify",
     "level":  4,
     "description": "Targeted stone area is turned to mud, up to 1,000 cubic feet."},

    {"name": "Nounify",
     "level":  2,
     "description": "Caster transforms into any inanimate object between the sizes of an apple and a grand piano."},

    {"name": "Ooze",
     "level":  1,
     "description": "Caster can ooze like an amoeba."},

    {"name": "Pacify",
     "level":  5,
     "description": "L targeted creatures are suddenly calm and want no part of violence."},

    {"name": "Paralyze",
     "level":  3,
     "description": "Targeted creature is paralyzed. "},

    {"name": "Petrify",
     "level":  8,
     "description": "Targeted creature is permanently turned to stone."},

    {"name": "Phantasm",
     "level":  5,
     "description": "Caster creates a controllable illusion. Any creature failing a PRE check believes it is real, and may be injured by it as if it were."},

    {"name": "Phantom Lantern",
     "level":  1,
     "description": "A floating light source. Moves wherever the caster wants."},

    {"name": "Phobia",
     "level":  5,
     "description": "L targeted creatures become terrified of targeted object."},

    {"name": "Pilfer",
     "level":  3,
     "description": "Teleports a visible item to caster's hand."},

    {"name": "Plant Master",
     "level":  5,
     "description": "Nearby plants and trees gain the ability to move 2m per round and will obey the caster."},

    {"name": "Polymorph",
     "level":  6,
     "description": "Target is transformed into an object of the caster's choice."},

    {"name": "Possess Undead",
     "level":  10,
     "description": "Take control of L undead creatures nearby."},

    {"name": "Provision",
     "level":  4,
     "description": "Creates enough food and drink to sustain 6 creatures for one day."},

    {"name": "Pull",
     "level":  1,
     "description": "Visible arget object of any size is pulled toward the caster  with the strength of L men for one round."},

    {"name": "Puppet",
     "level":  3,
     "description": "Caster totally controls target's speech."},

    {"name": "Purify Food & Drink",
     "level":  1,
     "description": "Removes all toxins from nearby food and drink."},

    {"name": "Push",
     "level":  1,
     "description": "Target object of any size is pushed away from the caster  with the strenght of L men for one round."},

    {"name": "Raise Corpse",
     "level":  10,
     "description": "Dead Target rises as an undead being under contol of the caster with HP matching those while alive."},

    {"name": "Read Mind",
     "level":  3,
     "description": "Caster can hear the surface thoughts of target individual."},

    {"name": "Reginald",
     "level":  2,
     "description": "A man in yellow clothing appears until end of spell. He will obey polite, safe requests."},

    {"name": "Repel",
     "level":  2,
     "description": "Two objects become strongly repelled by one another and cannot come closer than 10'."},

    {"name": "Resist Cold",
     "level":  1,
     "description": "Caster may ignore the effects of cold."},

    {"name": "Resist Fire",
     "level":  2,
     "description": "Caster may ignore the effects of fire."},

    {"name": "Restore Sanity",
     "level":  5,
     "description": "Return a character's mental health to its normal state."},

    {"name": "Resurrect",
     "level":  1,
     "description": "Return life to a corpse. Rises with 1 HP. Useable up to one week after death."},

    {"name": "Rose Binding",
     "level":  2,
     "description": "Rose bushes spring from the ground to hold target. 1d6 thorn damage per turn. STR check to break free."},

    {"name": "Scry",
     "level":  3,
     "description": "The GM will answer up to L yes/no questions about a touched object."},

    {"name": "Sculpt",
     "level":  4,
     "description": "Targeted stone, wood, or metal object or area can be sculpted by the caster as if it were made of clay."},

    {"name": "Seal",
     "level":  2,
     "description": "Magically seals a door or item to everyone except caster. Does not prevent the object from being broken."},

    {"name": "Séance",
     "level":  8,
     "description": "A dead body will respond to L questions, in short, simple answers of no more than 5 words each."},

    {"name": "Shell",
     "level":  4,
     "description": "Caster is impervious to conventional ranged attacks."},

    {"name": "Shield",
     "level":  1,
     "description": "Caster gains 2 Armor Points."},

    {"name": "Shrink",
     "level":  5,
     "description": "Caster and L touched creatures are shrunk to the size of a mouse."},

    {"name": "Shuffle",
     "level":  5,
     "description": "L+1 nearby creatures instantly switch places, who and where to be determined randomly."},

    {"name": "Silence",
     "level":  1,
     "description": "Completely muffles all noise within 100m of caster."},

    {"name": "Sleep",
     "level":  6,
     "description": "L creatures instantly fall into a light sleep."},

    {"name": "Sorcerer's Ward",
     "level":  7,
     "description": "Targeted creature is immune to magical spells up to power level 5."},

    {"name": "Spectral Coach",
     "level":  3,
     "description": "A spectral carriage appears. It will carry up to 6 humanoids for up to 3 hours. Carriage moves unnaturally quickly over all terrains, including water."},

    {"name": "Spider",
     "level":  1,
     "description": "Caster can climb surfaces like a spider."},

    {"name": "Spring",
     "level":  1,
     "description": "A spring of fresh water appears."},

    {"name": "Sticky",
     "level":  1,
     "description": "Target becomes extremely sticky."},

    {"name": "Stone to Flesh",
     "level":  8,
     "description": "Returns a pertrified creature to its original state."},

    {"name": "Storm",
     "level":  10,
     "description": "6d6 lightning damage each to L targets."},

    {"name": "Stretch",
     "level":  3,
     "description": "Caster's arms, legs, and neck can stretch up to L x meters."},

    {"name": "Suffer",
     "level":  5,
     "description": "Target is incapacitated by pain."},

    {"name": "Summon Aberration",
     "level":  15,
     "description": "Summon a randomly generated Major Xenoplanar Horror (see Bestiary section). The xenoplanar is not under the spell caster's control."},

    {"name": "Summon Horror",
     "level":  5,
     "description": "Summon a randomly generated Xenoplanar Horror Minion (see Bestiary section). The aberration is not under the spell caster's control."},

    {"name": "Swarm",
     "level":  3,
     "description": "Summons a swarm of flying insects under caster's control. Will blind and confuse target."},

    {"name": "Telekinesis",
     "level":  3,
     "description": "Caster may move items with their mind, up to weight of Lx10lbs."},

    {"name": "Telepathy",
     "level":  3,
     "description": "L+1 targeted individuals can hear one another's thoughts over any distance."},

    {"name": "Teleport",
     "level":  6,
     "description": "Instantly teleports caster to a spot they can see, or a spot that is out of sight but very well known to them."},

    {"name": "Teleport",
     "level":  6,
     "description": "Targeted object is instantly teleported from one spot to another spot on the ground up to Lx10m away."},

    {"name": "Terraform",
     "level":  8,
     "description": "Caster may shape the terrain around them in a 100m radius."},

    {"name": "Tether",
     "level":  2,
     "description": "Two objects become attached with an invisible cord and cannot be moved more than 10' appart."},

    {"name": "Thicket",
     "level":  5,
     "description": "A thicket of trees and dense brush up to 15m wide instantly sprouts up around targeted spot."},

    {"name": "Throw Voice",
     "level":  1,
     "description": "Caster can cause their voice to emanate from a spot up to 20m away."},

    {"name": "Transparency",
     "level":  3,
     "description": "Caster can see through solid matter."},

    {"name": "True Sight",
     "level":  3,
     "description": "Caster sees through all nearby illusions."},

    {"name": "Truth",
     "level":  3,
     "description": "Target creature will go into a trance and truthfully answer L yes/no questions."},

    {"name": "Uncurse",
     "level":  4,
     "description": "Removes one curse from one target."},

    {"name": "Ventriloquism",
     "level":  1,
     "description": "Creates a sound illusion that comes from targeted spot."},

    {"name": "Voyeur",
     "level":  4,
     "description": "Caster can see through the eyes of a creature they touched up to 12 hours earlier."},

    {"name": "Wall of Iron",
     "level":  5,
     "description": "A wall of iron appears in targeted spot. It is up to 20m long and 10m high."},

    {"name": "Wall of Ouch",
     "level":  5,
     "description": "A wall of fire, ice, thorns, or wind rises from the chosen ground, 15m long and 4m high. 2d6 damage per round inside the wall."},

    {"name": "Ward",
     "level":  5,
     "description": "A silver circle 10m in diameter appears around targeted spot. Choose one thing that cannot enter or leave it: living creatures, dead creatures, projectiles, or metal."},

    {"name": "Water Breathing",
     "level":  3,
     "description": "Caster can breathe underwater."},

    {"name": "Water Way",
     "level":  7,
     "description": "Water up to 20m deep will part in a 3m radius circle around the caster. "},

    {"name": "Web",
     "level":  3,
     "description": "Caster's chosen body part can shoot thick webbing."},

    {"name": "Wholeness",
     "level":  10,
     "description": "Complete healing of one creature. Damage, disease, poison."},

    {"name": "Wind Walk",
     "level":  10,
     "description": "Caster and 1 targeted creature turn to mist and can fly swiftly."},

    {"name": "Wisp",
     "level":  1,
     "description": "Caster's body becomes living smoke."},

    {"name": "Wizard Mark",
     "level":  1,
     "description": "Caster's finger can spray a dayglow paint. It is visible only to the caster, and can be seen through solid objects and at any distance."},

    {"name": "Word of Recall",
     "level":  12,
     "description": "Caster and nearby allies instantly teleport to a previously prepared location any distance away. Preparing a location involves casting Word of Recall on it ahead of time. Transport occurs from anywhere the spell is cast again."},

    {"name": "Word of Virtue",
     "level":  15,
     "description": "2d6 targeted creatures are affected within 30m. Creatures with fewer HPs than caster's maximum die instantly. Creatures with more HPs than caster's max are paralyzed."}
]

ARCANESPELLS = [
    {"level": 1, "spells": ["Arrow", "Bigger", "Bloodhound", "Cure Light Wounds", "Describble", "Detect Evil", "Earify", "Eye of the Sorcerer", "Feather Fall", "Freeze", "Haste", "Hole", "Leap",
                            "Light", "Ooze", "Phantom Lantern", "Pull", "Purify Food & Drink", "Push", "Resist Cold", "Shield", "Silence", "Spider", "Spring", "Sticky", "Throw Voice", "Ventriloquism", "Wisp", "Wizard Mark"]},

    {"level": 2, "spells": ["Calm", "Darkness", "Detect Foes", "Detect Magic", "Displace", "Flame", "Fog",
                            "Illusion", "Levitate", "Nounify", "Reginald", "Repel", "Resist Fire", "Rose Binding", "Seal", "Tether"]},

    {"level": 3, "spells": ["Amputate", "Animate Object", "Army ", "Beast Form", "Confuse", "Cure Poison", "Darkvision", "Deafen", "Disguise", "Dispel Magic", "Door", "Dopplegang", "Enchant Weapon", "Fear", "Find Traps", "Fly", "House of Mirrors",
                            "Hover", "Knock", "Lightning", "Luminesce ", "Massive Gravity", "Paralyze", "Pilfer", "Puppet", "Read Mind", "Scry", "Spectral Coach", "Stretch", "Swarm", "Telekinesis", "Telepathy", "Transparency", "True Sight", "Truth", "Water Breathing", "Web"]},

    {"level": 4, "spells": ["Bramble", "Cold Blast", "Cure Disease", "Cure Serious Wounds", "Feeblemind",
                            "Humanimal", "Illusory Clone", "Invisibility", "Muddify", "Provision", "Sculpt", "Shell", "Uncurse", "Voyeur"]},

    {"level": 5, "spells": ["Air Diver", "Babble ", "Body Swap", "Charm", "Command", "Control Weather", "Dispel", "Elemental Servant", "Fireball", "Frenzy", "Greed", "Monstrosity",
                            "Pacify", "Phantasm", "Phobia", "Plant Master", "Restore Sanity", "Shrink", "Shuffle", "Suffer", "Summon Horror", "Thicket", "Wall of Iron", "Wall of Ouch", "Ward"]},

    {"level": 6, "spells": ["Bind", "Cloak", "Counterspell",
                            "Malice", "Polymorph", "Sleep", "Teleport"]},

    {"level": 7, "spells": ["Animate Dead",
                            "Ethereal Tunnel", "Sorcerer's Ward", "Water Way"]},

    {"level": 8, "spells": ["Manse", "Mirrorway",
                            "Petrify", "Séance", "Stone to Flesh", "Terraform"]},

    {"level": 10, "spells": ["Conflagration", "Disenchant", "Earthquake", "Freeze Time",
                             "Great Warding", "Possess Undead", "Raise Corpse", "Storm", "Wholeness", "Wind Walk"]},

    {"level": 12, "spells": ["Disintegrate", "Lay Waste", "Word of Recall"]},

    {"level": 15, "spells": ["Resurrect",
                             "Summon Aberration", "Word of Virtue"]}
]

NATURESPELLS = [
    {"level": 1, "spells": ["Cure Light Wounds",
                            "Purify Food & Drink", "Resist Cold", "Spring"]},

    {"level": 2, "spells": ["Fog", "Resist Fire", "Rose Binding"]},

    {"level": 3, "spells": ["Beast Form", "Cure Poison",
                            "Fly", "Swarm", "Water Breathing"]},

    {"level": 4, "spells": ["Bramble", "Humanimal",
                            "Muddify", "Provision", "Sculpt"]},

    {"level": 5, "spells": ["Control Weather", "Plant Master", "Thicket"]},

    {"level": 7, "spells": ["Water Way"]},

    {"level": 8, "spells": ["Terraform"]},

    {"level": 10, "spells": ["Earthquake", "Wind Walk"]}
]

VIRTURESPELLS = [
    {"level": 1, "spells": ["Cure Light Wounds", "Detect Evil",
                            "Light", "Purify Food & Drink", "Resist Cold", "Shield"]},
    {"level": 2, "spells": ["Calm", "Detect Foes", "Reginald"]},
    {"level": 3, "spells": ["Cure Poison", "Luminesce ",
                            "Read Mind", "Scry", "Telepathy", "True Sight", "Truth"]},
    {"level": 4, "spells": ["Cure Disease",
                            "Cure Serious Wounds", "Provision", "Uncurse"]},
    {"level": 5, "spells": ["Babble ", "Charm", "Command",
                            "Dispel", "Pacify", "Ward", "Restore Sanity"]},
    {"level": 8, "spells": ["Manse"]},
    {"level": 10, "spells": ["Wholeness"]},
    {"level": 15, "spells": ["Resurrect", "Word of Virtue"]}
]

STEALTHSPELLS = [
    {"level": 1, "spells": ["Bloodhound", "Describble", "Earify", "Haste",
                            "Leap", "Silence", "Spider", "Throw Voice", "Ventriloquism"]},

    {"level": 2, "spells": ["Darkness"]},

    {"level": 3, "spells": ["Darkvision", "Disguise",
                            "Find Traps", "Knock", "Pilfer"]},

    {"level": 4, "spells": ["Invisibility"]},

    {"level": 5, "spells": ["Babble "]},

    {"level": 6, "spells": ["Cloak"]}

]

def allSpellsOfType(listName):
    allSpells = []
    for dict in listName:
        allSpells = allSpells + dict["spells"]
    return allSpells


PROFESSIONS = ["Accountant", "Actor", "Anthropologist", "Antiquarian", "Archeologist", "Architect", "Engineer (Specify)", "Explorer", "Farmer", "Federal Agent", "Film Crew", "Firefighter", "Photographer", "Physicist", "Pilot", "Plumber", "Police Detective", "Police Officer", "Artist", "Athlete", "Bail Bondsman", "Bank Robber", "Banker", "Bartender", "Forensics", "Forester/Ranger", "Gambler", "Gangster", "Gardener", "Hired Muscle", "Politician", "Prison Guard", "Private Detective", "Professor", "Programmer/Coder", "Psychiatrist", "Biologist", "Bookstore Owner", "Bounty Hunter", "Burglar", "Butler/Maid", "Cab Driver", "Hit Man", "Journalist", "Judge", "Laborer/Factory Worker", "Lawyer", "Librarian", "Psychologist", "Race Car Driver", "Researcher", "Restaurateur",
               "Retail Clerk", "Roadie/Stagehand", "Carpenter", "Cartographer", "Chef", "Chemist", "Clergy", "Con Man", "Loan Shark", "Locksmith", "Lumberjack", "Machinist", "Management", "Mathematician", "Safecracker", "Sailor", "Salesman", "Secretary", "Security Guard", "Singer", "Construction", "Corporate", "Cowboy", "Cryptographer", "Designer", "Dilettante", "Mayor", "Mechanic", "Merchant", "Military Officer", "Miner", "Museum Curator", "Smuggler", "Soldier", "Sports Coach", "Stockbroker", "Student", "Stunt Man", "Diplomat", "Doctor/Dentist", "Drifter", "Driver", "Educator", "Electrician", "Musician", "Nurse", "Parapsychologist", "Park Ranger", "Pharmacist", "Phone Operator", "Surveyor", "Talent Agent", "Telemarketer", "Undertaker", "Writer", "Zookeeper"]

PSYCHICPOWERS = ["Telepathy", "Telekinesis", "Empath",
                 "Clairvoyance", "Pyrokinesis", "Psychometry"]

SUPERPOWERS = ["Heightened Balance", "Animal Communication", "Chameleon", "Hypnotic Suggestion", "Durability", "Elasticity", "Blast", "Speed ", "Flight", "Force Shield", "Genius", "Heat Vision", "Project Illusion",
               "Immunity (Specify)", "Invisibility", "Liquid/Gas Form", "Mental Blast", "Psychometry", "Rage Transformation", "Stealthy", "Shapeshift - Animal", "Shapeshift - People", "Shapeshift - Size", "Sticky", "Super Strength", "Teleport", "Super Senses"]

PHYSICALMUTATIONS = ["Acid Spit", "Adrenal Boost", "Amphibious", "Bioluminescence", "Blast", "Chameleon Skin", "Climber", "Extra Large", "Echolocation", "Elasticity", "Electrical Discharge", "Heat Vision", "Extra Body Parts", "Natural Armor", "Distance Vision", "Heightened Senses", "Magnetic Control", "Natural Armor",
                     "Oversized Body Parts", "Heightened Balance", "Photosynthetic", "Poisonous (Specify)", "Quills", "Regeneration", "Repulsive Spray", "Retractable Claws", "Shapeshift - Animal", "Shapeshift - People", "Shapeshift - Size", "Speedy", "Heightened Smell", "Super Strength", "Tough", "Extra Small", "Web Maker", "Wing"]

MENTALMUTATIONS = ["Clairvoyance", "Command", "Cryokinetic", "Sense", "Danger Sense", "Empath", "Fear", "Force Shield", "Genius", "Immunity", "Internal Compass", "Levitate",
                   "Magnetic Control", "Mind Blast", "Project Illusion", "Psychic Healer", "Psychic Vampire", "Pyrokinesis", "Restore Health", "Sleep Wave", "Telekinesis", "Telepathy", "Teleport"]

ANIMALSTOCKS = [
    {"animal": ["Alligator", " Crocodile"], "specials": [
        "Natural Armor", " Hold Breath", " Locking Jaw"]},
    {"animal": ["Badger"], "specials": [
        "Tough", " Burrower", " Night Vision"]},
    {"animal": ["Bat"], "specials": ["Echolocation", " Wings"]},
    {"animal": ["Bear"], "specials": ["Tough", " Strong", " Natural Armor"]},
    {"animal": ["Beaver"], "specials": ["Swimmer", " Gnawer", " Hold Breath"]},
    {"animal": ["Beetle"], "specials": [
        "Natural Armor", " Wings", " Exoskeleton"]},
    {"animal": ["Cat", " Tiger", " Lion", " Cougar"], "specials": [
        "Night Vision", " Retractable Claws", " Heightened Balance", " Pounce"]},
    {"animal": ["Cow", " Bull", " Ox"],
     "specials": ["Superior Strength", " Horns"]},
    {"animal": ["Crab", " Lobster"], "specials": ["Amphibious", " Armored"]},
    {"animal": ["Dog", " Fox", " Wolf"], "specials": [
        "Heightened Smell", " Tough", " Leader", " Super Digestion"]},
    {"animal": ["Eagle", " Hawk"], "specials": [
        "Wings", " Distance Vision", " Grip"]},
    {"animal": ["Eel"], "specials": ["Electrical Discharge", " Gills"]},
    {"animal": ["Elephant"], "specials": ["Extra Large",
                                          " Prehensile Limb (nose)", " Natural Armor"]},
    {"animal": ["Fish"], "specials": ["Gills", " Scale Armor"]},
    {"animal": ["Frog"], "specials": [
        "Amphibious", " Pounce", " Sticky Tongue"]},
    {"animal": ["Goat", " Sheep"], "specials": [
        "Charge Attack", " Immunity (Cold)", " Super Digestion"]},
    {"animal": ["Grasshopper", " Cricket"], "specials": ["Wings", " Leap"]},
    {"animal": ["Horse", " Zebra"], "specials": ["Swift", " Endurance"]},
    {"animal": ["Kangaroo"], "specials": ["Leap", " Swift", " Endurance"]},
    {"animal": ["Lizard"], "specials": [
        "Regenerate Limbs", " Chameleon Powers", " Cold Blooded"]},
    {"animal": ["Mantis"], "specials": [
        "Wings", " Retractable Claws", " Exoskeleton"]},
    {"animal": ["Monkey", " Ape"], "specials": [
        "Climber", " Heightened Balance", " Prehensile Tail"]},
    {"animal": ["Octopus"], "specials": ["Extra Limbs",
                                         " Contortionist", " Tentacles", " Chameleon Powers"]},
    {"animal": ["Opossum"], "specials": ["Night Vision", " Prehensile Tail"]},
    {"animal": ["Owl"], "specials": ["Wings", " Night Vision", " Grip"]},
    {"animal": ["Pig", " Boar"], "specials": ["Tusks", " Super Digestion"]},
    {"animal": ["Porcupine"], "specials": ["Quills", " Natural Armor"]},
    {"animal": ["Raccoon"], "specials": [
        "Night Vision", " Tough", " Super Digestion"]},
    {"animal": ["Rat"], "specials": [
        "Contortionist", " Night Vision", " Heightened Smell"]},
    {"animal": ["Rhinoceros"], "specials": [
        "Natural Armor", " Charge Attack", " Tough"]},
    {"animal": ["Scorpion"], "specials": [
        "Poisonous (Sting)", " Extra Claws", " Exoskeleton"]},
    {"animal": ["Seal", " Walrus"], "specials": [
        "Hold Breath", " Resist Cold"]},
    {"animal": ["Skunk"], "specials": ["Repulsive Spray", " Tough"]},
    {"animal": ["Snake"], "specials": ["Contortionist",
                                       " Poisonous (Bite)", " Heightened Smell"]},
    {"animal": ["Spider"], "specials": [
        "Stick to Walls", " Web Maker", " Poisonous (Bite)"]},
    {"animal": ["Squirrel"], "specials": [
        "Heightened Balance", " Climber", " Contortionist"]},
    {"animal": ["Turtle", " Tortoise", " Terrapin"],
     "specials": ["Hold Breath", " Natural Armor"]},
    {"animal": ["Wasp", " Bee"], "specials": [
        "Wings", " Poisonous (Sting)", " Exoskeleton"]},
    {"animal": ["Weasel", " Otter"], "specials": [
        "Contortionist", " Swimmer", " Night vision"]},
]

CYBERNETICS = ["Finger Laser", "Calc/Info Chip", "Cyber-Enhanced Vision", "Cyber-Enhanced Hearing", "Leg Servos",
               "Strength Booster", "Memory Card", "Bone Struts", "Gyro Stabilizer", "Biohazard Filter", "EMF/Radiation Sensor", "Olfactory Array"]


KNACKS = ["Chess", "Radio Repair", "Drawing", "Singing", "Wrestling", "Guitar", "Simple Chemistry", "Math", "Basic Programming", "Writing Poetry", "War History", "Gardening", "Cooking", "Racket Sports", "Juggling", "Computer Games", "Auto Mechanics", "Ham Radio",
          "Baseball", "Dancing", "Oil Painting", "Knots", "Roller Skating", "Cosmetics", "Horseback Riding", "Sewing", "Baking", "Speed Reading", "Crossword Puzzles", "Bocce", "Remembering Names", "Impersonations", "Comedy", "Card Tricks", "Fashion", "Fishing"]

SPECIES = [
    {
        "name": "Template",
        "description": "",
        "specials": ["special1", "special2"],
        "attMods": [],
        "languages": [],
        "xtraLang": {"choose": False, "number": 0, "list": ["Missile", "Invisibility"]},
    }
]

CLASSES = [
    # {
    #     "name": "Template",
    #     "attMods": [{"attribut": "att", "mod": 0}],
    #     "professions": {"choose": False, "number": 0, "list": ["Doctor", "Farmer"]},
    #     "knacks": {"choose": False, "number": 0, "list": ["Chess", "Drawing"]},
    #     "weapons": ["heavy", "Medium", "Light", "Ranged", "Melee", "None"],
    #     "armor": ["None", "Light", "Medium", "heavy"],
    #     "weaponPros": {"choose": False, "number": 0, "list": ["Swords", "Axes"]},
    #     "weaponMasteries": {"choose": False, "number": 0, "list": ["Swords", "Axes"]},
    #     "specials": ["special1", "special2"],
    #     "specialsXtra": {"choose": False, "number": 0, "list": ["Pilot", "Pickpocket"]},
    #     "foci": {"choose": False, "number": 0, "list": []},
    #     "paths": {"choose": False, "number": 0, "list": []},
    #     "resources": {"choose": False, "number": 0, "list": ["Toolkit", "Computer"]},
    #     "xtraGear": [],
    #     "notes": [],
    #     "startCash": 0.0,
    #     "spells": {"choose": False, "number": 0, "list": ["Missile", "Invisibility"]},
    #     "xtraLang": {"choose": False, "number": 0, "list": ["Missile", "Invisibility"]},
    # },

    {
        "name": "Fighter",
        "attMods": [{"attribut": "hp", "mod": 6}],
        "professions": {"choose": False, "number": 0, "list": []},
        "knacks": {"choose": False, "number": 0, "list": []},
        "weapons": ["Any"],
        "armor": ["Any"],
        "weaponPros": {"choose": True, "number": 1, "list": ["All Weapons"]},
        "weaponMasteries": {"choose": False, "number": 0, "list": []},
        "specials": ["Extra Attack", "Decapitate", "Extra HP"],
        "specialsXtra": {"choose": False, "number": 0, "list": []},
        "foci": {"choose": False, "number": 0, "list": []},
        "paths": {"choose": False, "number": 0, "list": []},
        "resources": {"choose": False, "number": 0, "list": []},
        "xtraGear": [],
        "notes": ["Starting at level 1, a fighter gains an extra attack per round of combat at every odd level of experience.", "Fighters may use any weapon with Proficiency"],
        "startCash": 0.0,
        "spells": {"choose": False, "number": 0, "list": []},
        "xtraLang": {"choose": False, "number": 0, "list": []},
    },

    {
        "name": "Thief",
        "attMods": [],
        "professions": {"choose": False, "number": 0, "list": []},
        "knacks": {"choose": False, "number": 0, "list": []},
        "weapons": ["Light", "Medium"],
        "armor": ["Light"],
        "weaponPros": {"choose": True, "number": 2, "list": WEAPONTYPESfantasy},
        "weaponMasteries": {"choose": False, "number": 0, "list": []},
        "specials": ["Stealthy", "Locksmith", "Detect Traps", "Disarm Traps", "Backstabber", "Heightened Balance", "Climber", "Disguise", "Pick Pocket", "Unsavory Contacts", "Read Languages"],
        "specialsXtra": {"choose": False, "number": 0, "list": []},
        "foci": {"choose": False, "number": 0, "list": []},
        "paths": {"choose": False, "number": 0, "list": []},
        "resources": {"choose": False, "number": 0, "list": []},
        "xtraGear": ["Lockpicks"],
        "notes": [],
        "startCash": 0.0,
        "spells": {"choose": False, "number": 0, "list": []},
        "xtraLang": {"choose": False, "number": 0, "list": []},
    },

    {
        "name": "Wizard",
        "attMods": [{"attribut": "att", "mod": 0}],
        "professions": {"choose": False, "number": 0, "list": []},
        "knacks": {"choose": False, "number": 0, "list": []},
        "weapons": ["None"],
        "armor": ["None"],
        "weaponPros": {"choose": False, "number": 0, "list": []},
        "weaponMasteries": {"choose": False, "number": 0, "list": []},
        "specials": ["Arcane Magic"],
        "specialsXtra": {"choose": False, "number": 0, "list": []},
        "foci": {"choose": False, "number": 0, "list": []},
        "paths": {"choose": False, "number": 0, "list": []},
        "resources": {"choose": False, "number": 0, "list": []},
        "xtraGear": ["Spell Book"],
        "notes": [],
        "startCash": 0.0,
        "spells": {"choose": True, "number": 4, "list": allSpellsOfType(ARCANESPELLS)},
        "xtraLang": {"choose": False, "number": 0, "list": []}
    },

    {
        "name": "Paladin",
        "attMods": [{"attribut": "att", "mod": 0}],
        "professions": {"choose": False, "number": 0, "list": []},
        "knacks": {"choose": False, "number": 0, "list": []},
        "weapons": ["Any"],
        "armor": ["Any"],
        "weaponPros": {"choose": True, "number": 2, "list": WEAPONTYPESfantasy},
        "weaponMasteries": {"choose": False, "number": 0, "list": []},
        "specials": ["Banish Evil", "Extra HP", "Virtue Magic"],
        "specialsXtra": {"choose": False, "number": 0, "list": []},
        "foci": {"choose": False, "number": 0, "list": []},
        "paths": {"choose": False, "number": 0, "list": []},
        "resources": {"choose": False, "number": 0, "list": []},
        "xtraGear": [],
        "notes": ["To successfully cast a spell, a paladin must make a PRE check instead of an INT check.", "If a paladin shows a pattern of unvirtuous behaviour, they lose their paladin status and revert to the fighter class."],
        "startCash": 0.0,
        "spells": {"choose": True, "number": 2, "list": allSpellsOfType(VIRTURESPELLS)},
        "xtraLang": {"choose": False, "number": 0, "list": []},
    },

    {
        "name": "Druid",
        "attMods": [],
        "professions": {"choose": False, "number": 0, "list": []},
        "knacks": {"choose": False, "number": 0, "list": []},
        "weapons": ["Medium"],
        "armor": ["Light"],
        "weaponPros": {"choose": True, "number": 1, "list": ["Swords", "Axes", "Bows", "Staffs",
               "Bludgeons", "Daggers"]},
        "weaponMasteries": {"choose": True, "number": 1, "list": ["Staffs"]},
        "specials": ["Shapeshift - Animal", "Animal Familiar", "Survival", "Nature Magic"],
        "specialsXtra": {"choose": False, "number": 0, "list": []},
        "foci": {"choose": False, "number": 0, "list": []},
        "paths": {"choose": False, "number": 0, "list": []},
        "resources": {"choose": False, "number": 0, "list": []},
        "xtraGear": [],
        "notes": [],
        "startCash": 0.0,
        "spells": {"choose": True, "number": 4, "list": allSpellsOfType(NATURESPELLS)},
        "xtraLang": {"choose": False, "number": 0, "list": []},
    },

    {
        "name": "Ranger",
        "attMods": [],
        "professions": {"choose": False, "number": 0, "list": []},
        "knacks": {"choose": False, "number": 0, "list": []},
        "weapons": ["Any"],
        "armor": ["Light", "Medium"],
        "weaponPros": {"choose": True, "number": 1, "list": ["Swords", "Axes", "Staffs",
               "Bludgeons", "Daggers"]},
        "weaponMasteries": {"choose": True, "number": 1, "list": ["Bows"]},
        "specials": ["Stealthy", "Survival", "Animal Familiar", "Stealth Magic"],
        "specialsXtra": {"choose": False, "number": 0, "list": []},
        "foci": {"choose": False, "number": 0, "list": []},
        "paths": {"choose": False, "number": 0, "list": []},
        "resources": {"choose": False, "number": 0, "list": []},
        "xtraGear": [],
        "notes": [],
        "startCash": 0.0,
        "spells": {"choose": True, "number": 2, "list": allSpellsOfType(STEALTHSPELLS)},
        "xtraLang": {"choose": True, "number": 1, "list": ["Orcish", "Goblinoid", "Giant", "Molevan", "Fishfolkese", "Lizardovian", "Gnoll", "Elven", "Dwarvish", "Halfling"]}
    },

    {
        "name": "Monk",
        "attMods": [],
        "professions": {"choose": False, "number": 0, "list": []},
        "knacks": {"choose": False, "number": 0, "list": []},
        "weapons": ["Light", "Medium"],
        "armor": ["Light"],
        "weaponPros": {"choose": True, "number": 1, "list": WEAPONTYPESfantasy},
        "weaponMasteries": {"choose": False, "number": 0, "list": []},
        "specials": ["Brawler", "Heightened Balance", "Climber"],
        "specialsXtra": {"choose": False, "number": 0, "list": []},
        "foci": {"choose": False, "number": 0, "list": []},
        "paths": {"choose": False, "number": 0, "list": []},
        "resources": {"choose": False, "number": 0, "list": []},
        "xtraGear": [],
        "notes": ["A monk starts level 1 knowing one spell from the list. Monks succeed at spell casting with a PRE check instead of an INT check. Monks may add a new spell from the list every odd numbered level thereafter."],
        "startCash": 0.0,
        "spells": {"choose": True, "number": 1, "list": ["Cure Light Wounds", "Invisibility", "Telepathy", "Leap", "Spider", "Wind Walk", "Feather Fall"]},
        "xtraLang": {"choose": False, "number": 0, "list": []},
    },

    {
        "name": "Barbarian",
        "attMods": [],
        "professions": {"choose": False, "number": 0, "list": []},
        "knacks": {"choose": False, "number": 0, "list": []},
        "weapons": ["Any"],
        "armor": ["Any"],
        "weaponPros": {"choose": False, "number": 1, "list": ["Swords", "Bows", "Staffs",
               "Bludgeons", "Daggers"]},
        "weaponMasteries": {"choose": False, "number": 1, "list": ["Axes"]},
        "specials": ["Berserk", "Extra HP", "Naked Fighter", "Brawler"],
        "specialsXtra": {"choose": False, "number": 0, "list": []},
        "foci": {"choose": False, "number": 0, "list": []},
        "paths": {"choose": False, "number": 0, "list": []},
        "resources": {"choose": False, "number": 0, "list": []},
        "xtraGear": [],
        "notes": [],
        "startCash": 0.0,
        "spells": {"choose": False, "number": 0, "list": []},
        "xtraLang": {"choose": False, "number": 0, "list": []},
    },

]

SPYSPECIALTIES = [
    {"name": "", "description": ""},
]

GENRES = [
    {
        "name": "fantasy",
        "classes": ["Fighter", "Thief", "Wizard", "Paladin", "Druid", "Monk", "Ranger", "Barbarian"],
        "basicKit": ["Backpack", "Bedroll", "3 days rations", "3 torches", "flint and steel"],
        "species": ["Human", "Dwarf", "Elf", "Halfling"],
        "startingCash": 10,
        "commonLanguages": ["Common"]
    },
    
    # {
    #     "name": "genreName",
    #     "classes": [],
    #     "basicKit": [],
    #     "species": [],
    #     "startingCash": 0,
    #     "commonLanguages": []
    # }
]
