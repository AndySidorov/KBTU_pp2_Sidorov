s = input()
b = True
for x in range(len(s)):
    if s[x] != s[len(s)-1-x]:
        b = False
        break
print(b)