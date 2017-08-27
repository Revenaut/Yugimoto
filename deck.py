from random import shuffle
from card import *


class Deck:
    def __init__(self):
        self.genContents()

    # reset the deck to the original 52 cards
    def genContents(self):
        self.contents = []
        for rank in RANKS:
            for suit in SUITS:
                self.contents.append(Card(rank, suit))

    # randomly arrange the order of the elements in the deck list.
    def shuffle(self):
        shuffle(self.contents)
