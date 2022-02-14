def histogram(l):
    for x in l:
        for y in range(int(x)):
            print("*", end = "")
        print()
s = input()
q = s.split(" ")
histogram(q)