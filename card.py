from enum import Enum

class Rank(Enum):
    TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE = range(13)

class Suit(Enum):
    CLUBS, DIAMONDS, HEARTS, SPADES = range(4)

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit