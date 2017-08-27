from manager import *
from deck import *
from hand import *
from random import randint


def main():
    hand = Hand()
    deck = Deck()
    hand.add(deck.contents[0])
    hand.add(deck.contents[1])
    print(hand.show)
    print(hand.value)

if __name__ == "__main__":
    main()
