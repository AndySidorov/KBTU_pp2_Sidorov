def squares(a,b):
    while a <= b:
        yield a**2
        a += 1
a, b = int(input()), int(input())
l = squares(a, b)
for x in l:
    print(x)