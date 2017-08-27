RANKS = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}

SUITS = {
    "Clubs": 0,
    "Diamonds": 1,
    "Hearts": 2,
    "Spades": 3
}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def show(self):
        return self.rank + " of " + self.suit

    @property
    def fullName(self):
        return ('an ' if self.rank in ["Eight", "Ace"] else 'a ') + self.show