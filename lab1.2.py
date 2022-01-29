s = str(input())
sum = 0
for x in range(len(s)):
    sum += ord(s[x])
if sum > 300:
    print("It is tasty!")
else:
    print("Oh, no!")