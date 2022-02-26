import datetime
day1 = datetime.datetime.strptime(input(), "%Y-%m-%d %H:%M:%S.%f")
day2 = datetime.datetime.strptime(input(), "%Y-%m-%d %H:%M:%S.%f")
dif = abs(day1 - day2)
print(dif.total_seconds())