a = int(input())
z = str(input())
if z == 'b':
    print(a*1024)
elif z == 'k':
    b = int(input())
    txt = ".{}f"
    print(format(a / 1024, txt.format(b)))