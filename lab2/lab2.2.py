size = int(input())
s = str(input())
q = s.split(" ")
m = 0
for x in range(size):
    for y in range (x+1, size):
        if m < int(q[x]) * int(q[y]):
            m = int(q[x]) * int(q[y])
print (m)