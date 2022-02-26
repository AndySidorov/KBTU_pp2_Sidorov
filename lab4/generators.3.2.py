def div(n):
    num = 0
    while num <= n:
        while num % 3 != 0 or num % 4 != 0:
            num += 1
        if num <= n:
            yield num
        num += 1
n = int(input())
l = div(n)
for x in l:
    print(x)        