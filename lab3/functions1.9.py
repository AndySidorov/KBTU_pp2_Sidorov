import math
def volume(R):
    return 4 * math.pi * (R ** 3) / 3
R = int(input())
V = volume(R)
print(V) 