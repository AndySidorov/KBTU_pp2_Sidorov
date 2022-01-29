s = str(input())
t = s.split(" ")
for x in range(len(t)):
    if len(t[x]) >= 3:
        print(t[x], end = " ")