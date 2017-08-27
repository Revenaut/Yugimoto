from random import shuffle
from card import *


class Deck:
    def __init__(self):
        self.reset()

    # reset the deck to the original 52 cards
    def reset(self):
        self.contents = []
        for rank in RANKS:
            for suit in SUITS:
                self.contents.append(Card(rank, suit))
        self.shuffle()

    # randomly arrange the order of the elements in the deck list.
    def shuffle(self):
        shuffle(self.contents)
        Logger.log("The deck is shuffled.")

    # removes and returns the top card of the deck
    def draw(self):
        return self.contents.pop()

    # adds a card to the top of the deck
    def addCards(self, cards):
        self.contents += cards