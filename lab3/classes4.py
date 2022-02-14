import math
class Point():
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def show(self):
        print(self.x, self.y)
    def move(self):
        self.x = int(input())
        self.y = int(input())
    def dist(self, point):
        print(math.sqrt((self.x-point.x)**2+(self.y-point.y)**2))
s = input()
q = s.split(" ")
p1 = Point(int(q[0]),int(q[1]))
p2 = Point(int(q[2]),int(q[3]))
p1.show()
p2.show()
p1.move()
p2.move()
p1.dist(p2)
p2.dist(p1)