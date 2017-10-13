#@description
# This class is used for pre-processing data.
#

class Preprocessor:
    test = 0
    def __init__(self):
        self.test = 0

    def read(self, file):
        data = open(file, 'r')
        for line in data:
            print(line)



