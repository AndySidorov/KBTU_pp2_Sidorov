def Even(n):
    num = 0
    while num <= n:
        if num % 2 == 0:
            yield num
        num += 1
n = int(input())
l = Even(n)
s = ""
for x in l:
    s += str(x) + ", "
print(s[0:len(s)-2])