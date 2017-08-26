from deck import *
class Manager(object):
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffleDeck()
        print(len(self.deck.contents))

        self.playerA = self.genHand(),
        self.playerB = self.genHand()
    def genHand(self):
        hand = []
        for i in range(0, 5):
            hand.append(self.deck.contents.pop(0))
        return hand
