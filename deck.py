from card import *
import random
import itertools

class Deck(object):
    def __init__(self):
        self.board = [None]*52
        self.suits = "cdhs"
        self.ranks = "23456789JQKA"
        self.deck = self.generateDeck()
    def generateDeck(self):
        return tuple(''.join(card) for card in itertools.product(self.ranks, self.suits))

