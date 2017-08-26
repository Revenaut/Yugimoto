from random import shuffle
import itertools

class Deck(object):
    def __init__(self):
        self.board = [None]*52
        self.suits = "cdhs"
        self.ranks = "23456789JQKAT"
        self.contents = self.genContents()
    def genContents(self):
        contents = []
        for x in range(13):
            for i in range(4):
                contents.append(x)
        return contents
    def shuffleDeck(self):
        shuffle(self.contents)
