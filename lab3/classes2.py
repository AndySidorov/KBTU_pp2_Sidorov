class Shape():
    def __init__(self, l):
        self.length = l
    def area(self):
        print(0)
class Square(Shape):
    def area(self):
        print(self.length ** 2)
l = int(input())
a = Shape(l)
b = Square(l)
a.area()
b.area()