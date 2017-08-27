from player import *
from deck import *
from logger import *

class Game:
    def __init__(self):
        self.players = []
        self.dealer = Player("The Dealer")
        deck = Deck()

    def addPlayer(self, name):
        self.players.append(Player(name))

    def restart(self):
        self.deck.reset()

    # Deals two cards to each player, and to the dealer
    def deal(self):
        for player in self.players + [self.dealer]:
            player.deal([self.deck.draw(), self.deck.draw()])

