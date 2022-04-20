import requests

city = "Moscow,RU"
appid = "aa2e2c84ed4a53a0941701439de11f0b"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params=dict(q=city, units='metric', lang='ru', APPID=appid))
data = res.json()
print('Город', city)
print('Погода:', data['weather'][0]['description'])
print('Температура:', data['main']['temp'])
print('Скорость ветра:', data['wind']['speed'])
print('Видимость:', data['visibility'])
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params=dict(q=city, units='metric', lang='ru', APPID=appid))
data = res.json()
print('Прогноз погоды на неделю:')
for i in data['list']:
    print('Дата<', i['dt_txt'], ">\r\nТемпература<", '{0:+3.0f}'.format(i['main']['temp']),
          ">\r\nПогодные условия<", i['weather'][0]['description'], ">\r\nСкорость ветра<", i['wind']['speed'],
          "м/c", ">\r\nВидимость<", i['visibility'], "метров", ">")
    print("__________________________________________")