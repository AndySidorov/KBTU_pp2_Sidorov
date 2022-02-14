def rev(l):
    for x in range(int(len(l)/2)):
        b = l[x]
        l[x] = l[len(l)-x-1]
        l[len(l)-x-1] = b
    return l
s = input()
q = s.split(" ")
r = rev(q)
for x in r:
    print(x, end = " ")