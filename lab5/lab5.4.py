import re
n = int(input())
l = []
pattern = r'^[A-Z][a-z]+$'
for x in range(n):
    s = input()
    t = re.search(pattern, s)
    if t != None:
        l.append(t.string)
print("Answers:")
for x in l:
    print(x)