s = input()
q = s.split()
if len(q) == 1:
    b = input()
    q.append(b)
n, x = q
p = []
for i in range(int(n)):
    p.append(int(x) + 2 * i)
c = p[0]
for j in range(1, len(p)):
    c ^= p[j]
print (c)