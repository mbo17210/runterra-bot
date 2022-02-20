class Hand:
    MAX_HAND = 10
    def __init__(self, cards):
        self.cards = []
        self.size = 0

    def insert(self, card):
        if self.size < self.MAX_HAND:
            self.cards.append(card)
        else:
            self.burn(card)

    def removeById(self, card_id):
        for pos, card in enumerate(self.cards):
            if card.compareId(card_id):
                self.cards.pop(pos)
                return card

    def burn(self, card):
        print("Burnt", card.name, "because hand was full.")