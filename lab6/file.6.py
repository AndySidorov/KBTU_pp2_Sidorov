s = "{}.txt"
for x in range(26):
    f = open(s.format(chr(x + ord("A"))), "x")
    f.close()