def func(x):
    global q
    if x == len(q) - 1:
        q[x] = "1"
    elif int(q[x]) == 0:
        pass
    else:
        b = int(q[x])
        i = 1
        j = 1
        q[x] = "0"
        while x - i >= 0 and i <= b:
            func(x - i)
            i += 1
        while x + j < len(q) and j <= b:
            func(x + j)
            j += 1
s = str(input())
q = s.split(" ")
q[len(q)-1] = "0"
func(1)
print(q[len(q)-1])