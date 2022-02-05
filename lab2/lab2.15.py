def func(y):
    if y == "ZER":
        return "0"
    elif y == "ONE":
        return "1"
    elif y == "TWO":
        return "2"
    elif y == "THR":
        return "3"
    elif y == "FOU":
        return "4"
    elif y == "FIV":
        return "5"
    elif y == "SIX":
        return "6"
    elif y == "SEV":
        return "7"
    elif y == "EIG":
        return "8"
    elif y == "NIN":
        return "9"
def func2(y):
    if y == "0":
        return "ZER"
    elif y == "1":
        return "ONE"
    elif y == "2":
        return "TWO"
    elif y == "3":
        return "THR"
    elif y == "4":
        return "FOU"
    elif y == "5":
        return "FIV"
    elif y == "6":
        return "SIX"
    elif y == "7":
        return "SEV"
    elif y == "8":
        return "EIG"
    elif y == "9":
        return "NIN"
s = input()
n1 = ""
n2 = ""
N = ""
x = 0
while x < len(s):
    if s[x] == "+":
        x += 1
        n2 = n1
        n1 = ""
    n1 += func(s[x:x+3])
    x += 3
n3 = int(n1) + int(n2)
for x in str(n3):
    N += func2(x)
print(N)