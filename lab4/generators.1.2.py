def Square(n):
    num = 0
    while num <= n:
        yield num**2
        num += 1
n = int(input())
l = Square(n)
for x in l:
    print(x)