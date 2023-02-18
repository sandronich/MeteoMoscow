import json
import requests
from yaweather import YaWeather, Russia
from datetime import date

token = ""
chat_id = ""

# delta #
threshold = 5
# get current date#
today = date.today()
# from yandex#
y = YaWeather(api_key='')
res = y.forecast(Russia.Moscow)

print(res)
# check test.json existence #
try:
    with open("db.json", "rt") as fp:
        data = json.load(fp)
    print("Data: %s" % data)
except IOError:
    print("Could not read file, starting from scratch")
    data = []

data["day"].append(str(today)),
data["temp"].append(str(res.fact.temp))

with open("db.json", "wt") as fp:
    json.dump(data, fp)

avg_temp_day_by_day = 0

for x in range(-1, -8, -1):
    avg_temp_day_by_day = avg_temp_day_by_day + (float(data["temp"][x]) - float(data["temp"][x + 1]))

if threshold < round(avg_temp_day_by_day / 7, 1):
    message = "¡Atención! Среднее изменение температуры за неделю " + str(abs(round(avg_temp_day_by_day / 7, 1)))
else:
    message = "В Москве всё спокойно!"

url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json())