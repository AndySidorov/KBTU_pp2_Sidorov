f = open("4.txt", "r")
cnt = 0
while f.readline():
    cnt += 1
print(cnt)
f.close()