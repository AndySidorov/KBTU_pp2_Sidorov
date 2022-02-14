def perm(l, i, j, t, f):
    while (i < len(l)):
        if i not in f:
            f.append(i)
            t += l[i]
            if j != len(l)-1:
                perm(l, 0, j + 1, t, f)
            if j == len(l) - 1 and t not in L:
                L.append(t)
            t = t[0:len(t)-1]
            f.pop(len(f)-1)
        i += 1
s = input()
l = []
L = []
f = []
t = ""
i = 0
j = 0
for x in range(len(s)):
    l.append(s[x])
perm(l, i, j, t, f)
print("Permutations:")
for x in L:
    print(x)
print("Number of permutations:", len(L))