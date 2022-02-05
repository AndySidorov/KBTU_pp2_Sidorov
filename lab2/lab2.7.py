n1 = int(input())
d = dict(())
l = []
m = 0
for x in range(n1):
    s = input()
    q = s.split(" ")
    a, b = q
    if b not in d:
        d[b] = 1
        l.append(b)
    else:
        d[b] += 1
n2 = int(input())
for x in range(n2):
    s = input()
    q = s.split(" ")
    a, b, c = q
    if b in d:
        d[b] -= int(c)
for x in range(len(l)):
    if d[l[x]] > 0:
        m += d[l[x]]
print ("Demons left:", m)