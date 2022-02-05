n = int(input())
l1 = []
l2 = []
for x in range(n):
    s = input()
    q = s.split(" ")
    if len(q) == 1:
        c = l1[0]
        l1.pop(0)
        l2.append(c)
    else:
        l1.append(q[1])
for x in l2:
    print(x, end = " ")