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
        Logger.log(self.name + " hits, drawing " + card.fullName + ".")

    def deal(self, card):
        self.hand.add(card)
        Logger.log(self.name + " is dealt " + card.fullName + ".")

    # returns all the cards in hand to the deck
    def returnHand(self, deck):
        deck.contents += self.hand.contents # adds all the cards to the deck
        self.hand.contents = [] # removes all cards from the hand
        Logger.log(self.name + " returns their hand to the deck.")