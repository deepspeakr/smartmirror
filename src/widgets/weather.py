import traceback
import requests
import json
from tkinter import LEFT, TOP, Frame, Label, N, W
from PIL import Image, ImageTk

import src.config.config as config


class Weather(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="BLACK")
        self.degreeFrm = Frame(self, bg="black")
        self.degreeFrm.pack(side=TOP, anchor=W)
        self.iconLbl = Label(self.degreeFrm, bg="black")
        self.iconLbl.pack(side=LEFT, anchor=N)
        self.icon = ''
        self.city = ""
        self.label_city = Label(self, font="dreams 35", bg="BLACK", fg="WHITE")
        self.label_city.pack(side=TOP, anchor="w")
        self.temperature = ""
        self.label_temperature = Label(self, font="dreams 30", bg="BLACK", fg="WHITE")
        self.label_temperature.pack(side=TOP, anchor="w")

        self.humidity = ""
        self.label_humidity = Label(self, font="dreams 25", bg="BLACK", fg="WHITE")
        self.label_humidity.pack(side=TOP, anchor="w")

        self.no_weather_data1 = "Cannot get weather data"
        self.label_no_weather_data = Label(self, font="dreams 10", bg="BLACK", fg="WHITE")
        self.label_no_weather_data.pack(side=TOP, anchor="w")

        self.update_weather()

    def get_ip(self):
        try:
            ip_url = "http://jsonip.com/"
            req = requests.get(ip_url)
            ip_json = json.loads(req.text)
            return ip_json['ip']
        except Exception as e:
            traceback.print_exc()
            return "Error: %s. Cannot get ip." % e

    def get_location(self):
        try:
            if config.IPSTACK_API is None:
                raise ValueError("API key for ipstack is not set. Update corresponding value in config.py.")
            url_location = "http://api.ipstack.com/%s?access_key=%s" % (self.get_ip(), config.IPSTACK_API)
            req = requests.get(url_location)
            location_json = json.loads(req.text)
            if config.DEBUG:
                print(f"INFO: Using following location for weather widget: {location_json}")
            return location_json['latitude'], location_json['longitude']
        except Exception as e:
            traceback.print_exc()
            return "Error: %s. Cannot get location." % e

    def update_weather(self):
        if config.WEATHER_API is None:
            raise ValueError("API key for openweather is not set. Update corresponding value in config.py.")
        api_key = config.WEATHER_API

        latitude, longitude = self.get_location()

        url_weather = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric" % (
            latitude, longitude, api_key)
        weather_get = requests.get(url_weather)
        if weather_get.status_code == 200:
            weather = weather_get.json()
            if config.DEBUG:
                print(f"INFO: Weather JSON: {weather}")
            temperature2 = str(weather[u'main'][u'temp'])
            humidity2 = str(weather[u'main'][u'humidity'])
            city2 = str(weather[u'name'])

            if self.temperature != temperature2:
                self.temperature = temperature2
                self.label_temperature.config(text="Temperature: " + temperature2 + " °C")
            if self.humidity != humidity2:
                self.humidity = humidity2
                self.label_humidity.config(text="Humidity: " + humidity2 + " %")
            if self.city != city2:
                self.city = city2
                self.label_city.config(text=city2)

            icon_id = weather[u'weather'][0]['icon']
            icon2 = None
            if icon_id != " ":
                icon2 = icon_id
            icon_dir = "icons/" + icon_id + "@2x.png"
            if config.DEBUG:
                print(f"INFO: Using icon: {icon_dir}")
            if icon2 is not None:
                if self.icon != icon2:
                    self.icon = icon2
                    image = Image.open(icon_dir)
                    image = image.resize((100, 100), Image.ANTIALIAS)
                    photo = ImageTk.PhotoImage(image)

                    self.iconLbl.config(image=photo)
                    self.iconLbl.image = photo
            else:
                # remove image
                self.iconLbl.config(image='')

        else:
            self.label_no_weather_data.config(text=self.no_weather_data1)
            self.label_temperature.config(text="")
            self.label_humidity.config(text="")
            self.label_city.config(text="")

        self.after(600000, self.update_weather)
