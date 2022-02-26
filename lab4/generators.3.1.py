class Div:
    def __init__(self, n):
        self.n = n
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        x = self.num
        while x % 3 != 0 or x % 4 != 0:
            self.num += 1
            x = self.num
        if self.num <= self.n:
            self.num += 1
            return x
        else:
            raise StopIteration
n = int(input())
l = Div(n)
for x in l:
    print(x)