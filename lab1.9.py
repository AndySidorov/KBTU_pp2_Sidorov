a = int(input())
for x in range(a):
    s = str(input())
    b = s.find("@gmail.com")
    if b != -1:
        print(s[0:len(s)-10])