import os.path

LOGS_PATH = 'logs'

class Logger:
    @staticmethod
    def setFile(filename):
        Logger.file = open(os.path.join(LOGS_PATH, filename), 'w')

    @staticmethod
    def log(message):
        Logger.file.write(message + "\n")