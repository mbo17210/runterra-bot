from re import A
class Game:
    def __init__(self, players, turn):
        self.players = players
        self.turn = turn
    def gameLoop(self):
        roundStart(self)
        #roundAction()
        roundEnd(self)
    def roundStart(self):
        self.turn = self.turn + 1
        #updateMana
        for p in self.players:
            p.updateMana(p, self.turn)
            p.draw(1)
        #check for game end
    def roundEnd(self):
        for p in self.players:
            p.endRound()

class Player:
    def __init__(self, regions, action, passed, health, mana, spellMana, hand, deck):
        self.region = regions
        self.action = action
        self.passed = passed
        self.health = health
        self.mana = mana
        self.spellMana = spellMana
        self.hand = hand
        self.deck = deck
    def updateMana(self, maxMana):
        self.spellMana = min(3, self.mana + self.spellMana)
        self.mana = maxMana
    def draw(self, numCards):
        self.deck = self.deck - numCards
        if self.deck < 0:
            self.health = 0
        self.hand = self.hand + numCards