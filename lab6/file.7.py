f = open("text1.txt", "r")
g = open("text2.txt", "w")
x = f.read()
g.write(x)
g.close()
f.close()