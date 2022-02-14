import math
def filter_prime(num):
    prime = []
    for x in num:
        if int (x) < 2:
            pass
        else:
            b = True
            for y in range(2, int(math.sqrt(int(x)))+1):
                if int(x) % y == 0:
                    b = False
                    break
            if b:
                prime.append(x)
    return prime
s = input()
q = s.split(" ")
p = filter_prime(q)
print(p)