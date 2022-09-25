s = str(input())
t = str(input())
x = s.find(t)
y = s.rfind(t)
if x == -1:
    pass
elif x == y:
    print(x)
else:
    print(x,y)