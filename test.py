class Manager(object):
    def __init__(self):
        self.board = [None]*14
    def addCard(self, elem, card):
        self.board[elem] = card


def main():
    manager = Manager()
    manager.addCard(1, "test")
    print(manager.board[1])

if __name__ == "__main__":
    main()
