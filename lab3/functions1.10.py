def unique(l):
    x = 0
    while x < len(l):
        y = x + 1
        while y < len(l):
            if l[x] == l[y]:
                l.pop(y)
                y-=1
            y+=1
        x+=1
    return l
s = input()
q = s.split(" ")
l = unique(q)
print(l)