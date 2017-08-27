from random import shuffle
from card import *


class Deck:
    def __init__(self):
        self.contents = self.genContents()

    def genContents(self):  # generate a list of [0..13] 4 times.
        contents = []
        for rank in RANKS:
            for suit in SUITS:
                contents.append(Card(rank, suit))
        return contents

    # randomly arrange the order of the elements in the deck list.
    def shuffle(self):
        shuffle(self.contents)
