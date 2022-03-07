import re
s = input()
pattern = r'([A-Z])'
x = re.sub(pattern, r" \1", s)
print(x.strip())