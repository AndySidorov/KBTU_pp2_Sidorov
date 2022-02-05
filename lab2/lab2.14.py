l = []
while 1:
    n = int(input())
    if n == 0:
        break
    l.append(n)
for x in range (len(l)):
    if x > len(l) - x - 1:
        break
    if x == len(l) - 1 - x:
        print(l[x], end = " ")
    else:
        print(l[x]+l[len(l)-x-1], end = " ")