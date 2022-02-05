n = int(input())
for x in range(n):
    for y in range(n):
        if y == 0:
            print (x, end = " ")
        elif x == 0:
            print (y, end = " ")
        elif x == y:
            print (x*y, end = " ")
        else:
            print (0, end = " ")
    print(" ")