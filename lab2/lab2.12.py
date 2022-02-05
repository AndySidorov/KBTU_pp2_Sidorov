s = input()
l = []
b = True
for x in s:
    if x == "(" or x == "[" or x == "{":
        l.append(x)
    elif len(l) == 0:
        b = False
        break
    elif x == ")":
        if l[len(l)-1] == "(":
            l.pop(len(l)-1)
        else:
            b = False
            break
    elif x == "]":
        if l[len(l)-1] == "[":
            l.pop(len(l)-1)
        else:
            b = False
            break
    elif x == "}":
        if l[len(l)-1] == "{":
            l.pop(len(l)-1)
        else:
            b = False
            break
if b and len(l) == 0:
    print("Yes")
else:
    print("No")