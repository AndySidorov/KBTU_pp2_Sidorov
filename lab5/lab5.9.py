import re
s = input()
pattern = r'([a-z]*)([A-Z])'
x = re.sub(pattern, r"\1 \2", s)
print(x.strip())