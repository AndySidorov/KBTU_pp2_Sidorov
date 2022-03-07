import re
s = input()
pattern = r'[., ]'
x = re.sub(pattern, ":", s)
print(x)