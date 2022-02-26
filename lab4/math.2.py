import math
height = int(input())
base1 = int(input())
base2 = int(input())
bases = [base1, base2]
av = math.fsum(bases) / len(bases)
num = [av, height]
area = math.prod(num)
print(area)