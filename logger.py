import os.path

LOGS_PATH = 'logs'

class Logger:
    # makes the logger output to the given filename
    @staticmethod
    def setFile(filename):
        Logger.file = open(os.path.join(LOGS_PATH, filename), 'w')

    # writes a message to the file
    @staticmethod
    def log(message):
        Logger.file.write(message + "\n")