from manager import *
from deck import *

def main():
    manager = Manager()
    print(manager.playerA)
    print(manager.playerB)
    print(len(manager.deck.contents))

if __name__ == "__main__":
    main()
