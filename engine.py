from re import A
class Game:
    def __init__(self, players, turn):
        self.players = players
        self.turn = turn
        
    def gameStart(self):
        self.mulligan()

    def gameLoop(self):
        self.roundStart()
        #roundAction()
        self.roundEnd()
    def roundStart(self):
        self.turn = self.turn + 1
        #updateMana
        for p in self.players:
            p.updateMana(p, self.turn)
            p.draw(1)
        #check for game end

    def roundAction():
        return "hi"
        
    def roundEnd(self):
        for p in self.players:
            p.endRound()

    def mulligan(self):
        for p in self.players:
            drawn_cards = p.deck.drawNum(4)
            discard = []
            for pos in discard:
                p.deck.bottomDeck(drawn_cards[pos])
                drawn_cards.pop(pos)
            
            drawn_cards.extend(p.deck.drawNum(len(discard)))
            
            p.hand.extend(drawn_cards)


class Player:
    STARTING_HEALTH = 20
    MAXIMUM_MANA = 10

    def __init__(self, action, passed, mana, spellMana, hand, deck):
        #not implemented 
        #self.region = regions  
        self.action = action
        self.passed = passed
        self.health = self.STARTING_HEALTH
        self.mana = mana
        self.spell_mana = spellMana
        self.max_mana = 0
        self.hand = hand
        self.deck = deck

    def takeDamage(self, incoming_damage):
        self.health -= incoming_damage


    def incrementMaxMana(self):
        if self.max_mana < self.MAXIMUM_MANA:
            self.max_mana += 1

    def updateMana(self):
        self.incrementMaxMana()
        self.spell_mana = min(3, self.mana + self.spell_mana)
        self.mana = self.max_mana
    
    def draw(self, num_cards):
        if self.deck.size == 0:
            self.health = 0

        for card in self.deck.drawNum(num_cards):
            self.hand.insert(card)
