import json
f = open("5.txt", "w")
q = input().split()
f.write(json.dumps(q))
f.close()