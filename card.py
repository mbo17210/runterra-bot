class Card:
    def __init__(self, cost):
        self.cost = cost

class Minion(Card):
    #Effect is from class effect.
    def __init__(self, cost, attack, defense, effect, tag):
        super().__init__(cost)
        self.attack = attack
        self.defense = defense
        self.effect = effect
        self.tag = tag

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
    #If num_targets = 0, that implies the card doesn't specifically target something (random target). 
    #num_targets = 7 => targets all things possible
    #Hit nexus: 0 = no, 1 = possible, 2 = must (eg decimate)
    def __init__(self, targets, num_targets, damage, atk_buff, def_buff, hit_nexus)

class Targets(Enum):
    ENEMIES = 1
    ALLIES = 2
    ALL = 3
