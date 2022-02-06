from enum import Enum

class Card:
    def __init__(self, cost, name):
        self.cost = cost
        self.name = name

class Minion(Card):
    #Effect is from class effect.
    def __init__(self, cost, name, attack, health, tag = None, effects = None):
        super().__init__(cost, name)
        self.attack = attack
        self.health = health
        self.tag = tag
        self.effects = effects

class Spell(Card):
    #Speed is from SpellSpeed Enum. Effect is of class effect.
    def __init__(self, cost, name, speed, effects):
        super().__init__(cost, name)
        self.speed = speed
        self.effects = effects

class SpellSpeed(Enum):
    BURST = 3
    FAST = 2
    SLOW = 1


class Effect:
    #If num_targets = 0, that implies the card doesn't specifically target something
    #Hit nexus: 0 = no, 1 = possible, 2 = must (eg decimate)
    def __init__(self, targets, num_targets, damage, atk_buff, def_buff, buff_target, hit_nexus):
        self.targets = targets
        self.num_targets = num_targets
        self.damage = damage
        self.atk_buff = atk_buff
        self.def_buff = def_buff
        self.buff_target = buff_target
        self.hit_nexus = hit_nexus

class Targets(Enum):
    ENEMIES = 1
    ALLIES = 2
    ALL = 3
    SELF = 4