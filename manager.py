from deck import *
from random import getrandbits


class Manager(object):
    def __init__(self):
        self.file = open('test.txt', 'w')  # open our output file
        self.deck = Deck()  # initialize the deck
        self.deck.shuffleDeck()  # randomize the ordering of the deck
        self.players = {True: self.genHand(), False: self.genHand()}  # generate hands for players
        self.turn(bool(getrandbits(1))) #initialize the game by starting off with a random player

    def genHand(self):  # pops the first five elements off of the deck, giving those as a list to the player
        hand = []
        for i in range(0, 5):
            hand.append(self.deck.contents.pop(0))
        return hand


    def check(self, card, hand): # simple comparison between the card selected and what's in the opposing players  hand
        if card in hand:
            return 1
        return 0

    def selCard(self, hand):  # randomly select a card to "go fish"
        return hand[randint(0, len(hand))]

    def goFish(self, player): # pop the next card off of the deck and add it to the fishing player's hand.
        player.append(self.deck.contents.pop(0))

    def writeHands(self, file): # write the contents of the player's hand to a file
        file.write("playerA's hand is: " + ' '.join(str(e)
                                                    for e in manager.players[True]) + "\n")
        file.write("playerB's hand is: " + ' '.join(str(e)
                                                    for e in manager.players[True]) + "\n")



    def turn(self, player):
        print(self.players[player])



    def __del__(self):
        self.file.close()  # close the file stream after program completion

