from random import shuffle


class Deck:
    def __init__(self):
        self.contents = self.genContents()

    def genContents(self):  # generate a list of [0..13] 4 times.
        contents = []
        for x in range(13):
            for i in range(4):
                contents.append(x)
        return contents

    # randomly arrange the order of the elements in the deck list.
    def shuffle(self):
        shuffle(self.contents)
