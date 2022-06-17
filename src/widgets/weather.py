import traceback
from src.config.config import weather_api
import requests
import json
import time


def get_weather():
    try:

        api_key = weather_api
        appid = 3099434  # Gdańsk
        url = "http://api.openweathermap.org/data/2.5/weather?id=%s&&units=metric&appid=%s" % (appid, api_key)
        response = requests.get(url)
        conditions_data = json.loads(response.text)
        print(conditions_data)

        city_name = conditions_data[u'name']
        temp_cur = conditions_data[u'main'][u'temp']
        icon = str(conditions_data[u'weather'][0][u'icon'])
        icon = icon[0:2]
        humidity = conditions_data[u'main'][u'humidity']
        wind = str(conditions_data[u'wind'][u'speed'])
        wind_dir = str(conditions_data[u'wind'][u'deg'])
        epoch = int(conditions_data[u'dt'])
        utime = time.strftime('%H:%M', time.localtime(epoch))
        print("aktualna temperatura dla miasta", city_name, "to:", temp_cur)

    except Exception as e:
        traceback.print_exc()
        return "Error"
