from game import *
from logger import *


def main():
    Logger.setFile('log.txt')
    game = Game()
    game.addPlayer('Jack')
    game.addPlayer('Ben')
    game.deal()

if __name__ == "__main__":
    main()
