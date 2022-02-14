def has_33(l):
    b = False
    for x in range(len(l)-1):
        if int(l[x]) == 3 and int(l[x+1]) == 3:
            b = True
            break
    return b
s = input()
q = s.split(" ")
b = has_33(q)
print(b)