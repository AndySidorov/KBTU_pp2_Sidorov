def pal(p):
    b = True
    for x in range(int(len(p)/2)):
        if p[x] != p[len(p)-x-1]:
            b = False
            break
    return b
s = input()
b = pal(s)
print(b)