import datetime
today = datetime.datetime.now()
dif = datetime.timedelta(days = -5)
ago = today + dif
print(ago)