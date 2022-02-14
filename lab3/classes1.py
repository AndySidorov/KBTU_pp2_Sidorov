class string():
    def __init__(self, word):
        self.value=word
    def getString(self):
        self.value = input()
    def printString(self):
        print(self.value.upper())
a = string(input())
a.getString()
a.printString()