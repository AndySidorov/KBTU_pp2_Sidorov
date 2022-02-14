def spy_game(l):
    b = False
    a = 0
    cnt = 0
    for x in range(len(l)):
        if int(l[x]) == a:
            cnt += 1
            if cnt == 2:
                a = 7
            if cnt == 3:
                b = True
                break
    return b
s = input()
q = s.split(" ")
b = spy_game(q)
print(b)