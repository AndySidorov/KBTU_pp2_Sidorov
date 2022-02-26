import datetime
today = datetime.datetime.now()
before = datetime.timedelta(days = -1)
after = datetime.timedelta(days = 1)
yesterday = today + before
tomorrow = today + after
print(yesterday)
print(today)
print(tomorrow)