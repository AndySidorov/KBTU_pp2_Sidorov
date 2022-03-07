import re
s = input()
x = re.sub("_", " ", s)
x = "a" + x
x = x.title()
x = x[1:len(x)]
x = re.sub(" ", "", x)
print(x)