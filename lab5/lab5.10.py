import re
s = input()
pattern = r'([A-Z])'
x = re.sub(pattern, r" \1", s)
x = x.lower()
x = re.sub(" ", "_", x)
print(x)