from random import shuffle
import itertools

class Deck(object):
    def __init__(self):
        self.board = [None]*52
        self.suits = "cdhs"
        self.ranks = "23456789JQKA"
        self.contents = list(''.join(card) for card in itertools.product(self.ranks, self.suits))
    def shuffleDeck(self):
        shuffle(self.contents)
