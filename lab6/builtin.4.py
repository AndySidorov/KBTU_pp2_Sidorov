import datetime
import math
num = int(input())
ms = int(input())
now = datetime.datetime.now()
dif = datetime.timedelta(microseconds = ms * 1000)
after = now + dif
while datetime.datetime.now() < after:
    pass
else:
    print(math.sqrt(num))