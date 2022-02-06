import json
from card import Minion, Spell, Effect

#Change if library location moves
library_location = r'card/card_library.json'

#Load JSON
f = open(library_location)
card_data = json.load(f)

card_library = {}

#Feed in one effect dictionary from card loader and load it as an effect
def effectLoader(effect):
    targets = 0 if "targets" not in effect else effect["targets"]
    num_targets = 0 if "num_targets" not in effect else effect["num_targets"]
    damage = 0 if "damage" not in effect else effect["damage"]
    atk_buff = 0 if "atk_buff" not in effect else effect["atk_buff"]
    def_buff = 0 if "def_buff" not in effect else effect["def_buff"]
    buff_target = None if "buff_target" not in effect else effect["buff_target"]
    hit_nexus = 0 if "hit_nexus" not in effect else effect["hit_nexus"]
    return Effect(targets, num_targets, damage, atk_buff, def_buff, buff_target, hit_nexus)

#Loads minion w/ info from library
def minionLoader(minion, effects, name = None):
    cost = minion["cost"]
    name = name if name != None else minion["name"]
    attack = minion["attack"]
    health = minion["health"]
    tag = None if "tag" not in minion else minion["tag"]
    keywords = [] if "keywords" not in minion else minion["keywords"]
    return Minion(cost, name, attack, health, tag, keywords, effects)

#Loads spell w/ info from library
def spellLoader(spell, effects):
    cost = spell["cost"]
    name = spell["name"]
    speed = spell["speed"]
    return Spell(cost, name, speed, effects)
    


for item in card_data["Champions"]:
    unleveled_effects = []
    if "effects" in item["unleveled"]:
        for effect in item["unleveled"]["effects"]:
            unleveled_effects.append(effectLoader(effect))
    unleveled_champ = minionLoader(item["unleveled"], unleveled_effects, item["name"])
    
    leveled_effects = []
    if "effects" in item["leveled"]:
        for effect in item["leveled"]["effects"]:
            leveled_effects.append(effectLoader(effect))
    leveled_champ = minionLoader(item["leveled"], leveled_effects, item["name"])

    card_library[item["name"]] = [unleveled_champ, leveled_champ]

for item in card_data["Minions"]:
    effects = []
    if "effects" in item:
        for effect in item["effects"]:
            effects.append(effectLoader(effect))
    card_library[item["name"]] = minionLoader(item, effects)

for item in card_data["Spells"]:
    effects = []
    #Spells always have effect
    for effect in item["effects"]:
        effects.append(effectLoader(effect))
    card_library[item["name"]] = spellLoader(item, effects)

for key in card_library:
    print(key)
print(card_library["Doombeast"].id)
