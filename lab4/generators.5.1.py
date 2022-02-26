class downto:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n >= 0:
            x = self.n
            self.n -= 1
            return x
        else:
            raise StopIteration
n = int(input())
l = downto(n)
for x in l:
    print(x)