from random import shuffle
class Deck(object):
    def __init__(self):
        self.contents = self.genContents()
    def genContents(self):
        contents = []
        for x in range(13):
            for i in range(4):
                contents.append(x)
        return contents
    def shuffleDeck(self):
        shuffle(self.contents)
