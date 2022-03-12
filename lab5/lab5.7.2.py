import re
def func(t):
    return t.group(1).upper()
pattern = r'_([a-z])'
s = input()
x = re.sub(pattern, func, s)
print(x)