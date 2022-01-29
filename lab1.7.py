a = str(input())
sum = 0
for x in range(len(a)):
    sum += int(a[len(a)-x-1])*(2**x)
print(sum)