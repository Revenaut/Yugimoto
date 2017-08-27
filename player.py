from deck import *
from hand import *
from logger import *

class Player:
    def __init__(self, name):
        self.hand = Hand()
        self.name = name

    def hit(self, deck):
        card = deck.draw()
        self.hand.add(card)
        Logger.log(self.name + "hits, drawing " + card.fullName + ".")