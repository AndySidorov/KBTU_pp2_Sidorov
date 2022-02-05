n = int(input())
q = dict(())
l = []
m = 0
for x in range(n):
    s = input()
    p = s.split(" ")
    a, b = p
    if a not in q:
        q[a] = int(b)
        l.append(a)
    else:
        q[a] += int(b)
    if m < q[a]:
        m = q[a]
l.sort()
for x in range(len(l)):
    if q[l[x]] < m:
        print(l[x], "has to receive", m - q[l[x]], "tenge")
    else:
        print(l[x], "is lucky!")