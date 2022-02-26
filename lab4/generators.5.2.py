def squares(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
l = squares(n)
for x in l:
    print(x)