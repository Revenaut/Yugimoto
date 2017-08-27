from card import *

RANKS = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}

SUITS = {
    "Clubs": 0,
    "Diamonds": 1,
    "Hearts": 2,
    "Spades": 3
}

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

