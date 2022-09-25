t = str(input())
q = t.split(' ')
s, c = q
s = int(s)
c = int(c)
b = True
if s <= 500 and c % 2 == 0:
    for x in range(2, int(s/2 + 1)):
        if s % x == 0:
            b = False
            break
    if b == True:
        print("Good job!")
    else:
        print("Try next time!")
else:
    print("Try next time!")