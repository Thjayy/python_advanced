import datetime
import pytz

# data = datetime.date.today()
# tkun = datetime.date(2024,5,22)
# print(tkun-data)

# data = datetime.datetime(2023,12,19,17,8,48,10000)
# d_today = datetime.datetime.today()
# d_now = datetime.datetime.now(tz=pytz.UTC)
# d_utc = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(d_today)
# print(d_now)
# print(d_utc)
# print(data)

# dt_utc = d_now.astimezone(pytz.timezone("Asia/Tashkent"))
# print(dt_utc)
# for i in pytz.all_timezones:
#     print(i)
data = datetime.datetime.now(tz=pytz.timezone("Asia/Tashkent"))
print(data.strftime("%B %d %Y %A - %H:%M:%S"))


eng_date = 'December 19 2023'
date = datetime.datetime.strptime(eng_date, '%B %d %Y')
print(date)