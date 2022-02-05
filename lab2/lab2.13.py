def func(t):
    q = t.split(" ")
    a, b, c = q
    return int(a) + int(b) * 100 + int(c) * 10000
l = []
while 1:
    s = input()
    if s == "0":
        break
    l.append(s)
l.sort(key=func)
for x in l:
    print(x)