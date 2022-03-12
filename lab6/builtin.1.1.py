def func(x):
    global n
    return int(x) * n
n = int(input())
mult = map(func, input().split())
for x in list(mult):
    print(x, end = " ")