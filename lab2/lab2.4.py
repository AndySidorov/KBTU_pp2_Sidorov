n = int(input())
if n % 2 == 1:
    for x in range(n):
        for y in range(n):
            if x + y >= n - 1:
                print("#", end = "")
            else:
                print(".", end = "")
        print(" ")
if n % 2 == 0:
    for x in range(n):
        for y in range(n):
            if x + y <= x * 2:
                print("#", end = "")
            else:
                print(".", end = "")
        print(" ")