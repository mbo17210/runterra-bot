from enum import Enum
import itertools

class Card:
    newid = itertools.count().next
    def __init__(self, name, cost, region):
        self.name = name
        self.region = region
        self.cost = cost
        self.id = Card.newid()
        

    def __eq__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        
        return self.name == other.name
        

class Minion(Card):
    #Effect is from class effect.
    def __init__(self, cost, attack, defense, effect, tag, keywords=[]):
        super().__init__(cost)
        self.attack = attack
        self.defense = defense
        self.effect = effect
        self.tag = tag
        self.keywords = keywords

class Keyword(Enum):
    FEARSOME: 0
    NOBLOCK: 1
    EPHEMERAL: 2
    CHALLENGER: 3

class Spell(Card):
    #Speed is from SpellSpeed Enum. Effect is of class effect.
    def __init__(self, cost, speed, effect):
        super().__init__(cost)
        self.speed = speed
        self.effect = effect

class SpellSpeed(Enum):
    BURST = 3
    FAST = 2
    SLOW = 1


class Effect:
    #If num_targets = 0, that implies the card doesn't specifically target something
    #Hit nexus: 0 = no, 1 = possible, 2 = must (eg decimate)
    def __init__(self, targets, num_targets, damage, atk_buff, def_buff, hit_nexus)

class Targets(Enum):
    ENEMIES = 1
    ALLIES = 2
    ALL = 3