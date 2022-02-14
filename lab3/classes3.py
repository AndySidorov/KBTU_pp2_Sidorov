class Shape():
    def __init__(self, l):
        self.length = l
    def area(self):
        print(0)
class Rectangle(Shape):
    def __init__(self,l,w):
        super().__init__(l)
        self.width = w
    def area(self):
        print(self.length * self.width)
l = int(input())
w = int(input())
a = Shape(l)
b = Rectangle(l,w)
a.area()
b.area()