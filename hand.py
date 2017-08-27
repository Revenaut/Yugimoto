from card import *

class Hand:
    def __init__(self):
        self.contents = [] # list of cards
        self.value = 0 # current computed value of the hand
        self.softness = 0 # number of aces whose value can still be 1 or 11

    # adds a new card to the hand and recomputes the value of the hand
    def add(self, card):
        self.contents.append(card)
        if card.rank == "Ace":
            self.softness += 1
        self.value += RANKS[card.rank]
        if self.value > 21 and self.softness > 0:
            self.value -= 10
            self.softness -= 1

    # returns a comma separated list of the cards
    @property
    def show(self):
        return ", ".join([card.show for card in self.contents])

