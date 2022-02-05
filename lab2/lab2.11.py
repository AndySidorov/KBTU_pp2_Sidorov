s = input()
q = s.split(" ")
l = []
for x in q:
    if not x[len(x)-1].isalnum():
        x = x[0:len(x)-1]
    if x not in l:
        l.append(x)
l.sort()
print(len(l))
for x in l:
    print(x)