class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def show(self):
        return self.rank + " of " + self.suit