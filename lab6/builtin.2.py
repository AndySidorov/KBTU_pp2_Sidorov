s = input()
up = 0
low = 0
for x in s:
    if ord(x) >= ord("A") and ord(x) <= ord("Z"):
        up += 1
    if ord(x) >= ord("a") and ord(x) <= ord("z"):
        low += 1
print("Upper case:", up, "\nLower case:", low)