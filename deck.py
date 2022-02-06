import random

class Deck:
    STARTING_SIZE: 40
    def __init__(self, cards):
        self.cards = cards
        self.size = Deck.STARTING_SIZE

    def shuffle(self):
        random.shuffle(self.cards)

    #Draw a number of cards (num_cards) and return a list containing those cards
    def drawNum(self, num_cards):
        drawn_cards = []
        for count, card in enumerate(self.cards):
            if count < num_cards:
                self.size -= 1
                self.cards.remove(card)
                drawn_cards.append(card)

        return drawn_cards

    #Draw a specific card from the deck, by name
    def drawCard(self, card_name):
        for card in self.cards:
            if card == card_name:
                self.size -= 1
                self.cards.remove(card) 
                self.shuffle()
                return card

        
    #Implementation for draw effects can be done here later
    #Same thing for drawing by specific cost/spell speed/etc

    #Returns the top (num_cards) cards
    def look(self, num_cards):
        shown_cards = []
        for count, card in enumerate(self.cards):
            if count < num_cards:
                shown_cards.append(card)

        return shown_cards

    def bottomDeck(self, card):
        self.cards.append(card)
            

