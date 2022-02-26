class Squares:
    def __init__(self, n):
        self.n = n
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= self.n:
            x = self.num**2
            self.num += 1
            return x
        else:
            raise StopIteration
n = int(input())
l = Squares(n)
for x in l:
    print(x)