from manager import *
from deck import *

def main():
    deck = Deck()
    deck.shuffleDeck()
    print(deck.deck)

if __name__ == "__main__":
    main()
