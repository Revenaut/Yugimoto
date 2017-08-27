from enum import Enum
Rank = Enum('Rank', 'TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN JACK QUEEN KING ACE')
Suit = Enum('Suit', 'CLUBS DIAMONDS HEARTS SPADES')

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit