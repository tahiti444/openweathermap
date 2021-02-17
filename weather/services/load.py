from django.utils import timezone
import pytz

import json
import requests
import time

from ..models import ResponseAPI

class WeatherWismar(object):
    def __init__(
        self,
        https="https://",
        root="api.openweathermap.org/data/2.5/weather?",
        city="Wismar",
        path_credentials="./keys/credentials.json",
    ):

        self.https = https
        self.root = root
        self.city = city

        # open credentials file and extract key
        with open(path_credentials, "r") as f:
            data = json.load(f)
        key = str(data["key"])

        # api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
        self.uri = self.https + self.root + "q=" + self.city + "&" + "appid=" + key

    def apiCall4hwi(self):
        self.json_data = requests.get(self.uri).json()
        self.json_text = json.dumps(self.json_data, sort_keys=True, indent=2)

        # self.date = time.asctime()
        # self.date = time.strftime("%Y-%m-%d %H:%M")
        self.date = timezone.now()

        self.name = self.json_data["name"]

        self.temp = self.json_data["main"]["temp"]
        self.temp_min = self.json_data["main"]["temp_min"]
        self.temp_max = self.json_data["main"]["temp_max"]

        self.icon = self.json_data["weather"][0]["icon"]
        self.iconUrl = "https://openweathermap.org/img/w/" + self.icon + ".png"
        # self.imageLoad()
        self.save2DB()

        # self.mytest = "mytest"
        # return self.json_data

    def save2DB(self):
        response_attrs = {
            "time" :self.date,
            "city": self.city,
            "temp": self.temp,
            "temp_min": self.temp_min,
            "temp_max": self.temp_max,
            # "icon": self.icon,
            # "iconUrl": self.iconUrl,
            # "api_response": self.json_text,
            # 'uri': self.uri,
        }
        ResponseAPI.objects.create(**response_attrs)
