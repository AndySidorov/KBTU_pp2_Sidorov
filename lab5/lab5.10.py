import re
s = input()
pattern = r'([A-Z])'
x = re.sub(pattern, r"_\1", s)
x = x.lower()
print(x)