from manager import *

def main():
    manager = Manager()
    manager.addCard(1, "test")
    print(manager.board[1])

if __name__ == "__main__":
    main()
