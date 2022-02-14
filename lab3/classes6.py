import math
class mylist():
    def __init__(self, numbers):
        self.list = numbers
    def filter(self):
        nonprime = []
        for x in self.list:
            if int (x) < 2:
                nonprime.append(x)
            else:
                for y in range(2, int(math.sqrt(int(x)))+1):
                    if int(x) % y == 0:
                        nonprime.append(x)
                        break
        self.list = nonprime
s = input()
q = mylist(s.split(" "))
print(q.list)
q.filter()
print(q.list)