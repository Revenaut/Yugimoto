from deck import *
from hand import *

class Player:
    def __init__(self, name):
        self.hand = Hand()
        self.name = name