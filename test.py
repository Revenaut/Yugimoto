class Manager(object):
    def __init__(self):
        self.board = [None]*14
    def addCard(self, elem, card):
        self.board[elem] = card
