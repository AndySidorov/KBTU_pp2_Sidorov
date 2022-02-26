import math
sides = int(input())
length = int(input())
area = (sides * math.pow(length,2)) / (4 * math.tan(math.pi/sides))
print(round(area, 2))
# A = n*a^2/4tan(π/n)