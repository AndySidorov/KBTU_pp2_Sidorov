import math
def func(n):
    return d[n]
d = dict(())
l = []
p = input()
p = p.split(" ")
n = int(input())
for x in range(n):
    s = input()
    q = s.split(" ")
    a, b = q
    a = math.sqrt((int(a)-int(p[0]))**2+(int(b)-int(p[1]))**2)
    d[s] = a
    l.append(s)
l.sort(key = func)
for x in l:
    print(x)