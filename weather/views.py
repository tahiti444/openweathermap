from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import json
import requests

# Create your views here.

class WeatherWismar(object):
    def __init__(
        self,
        https = "https://",
        root = "api.openweathermap.org/data/2.5/weather?",
        city = "q=Wismar",
        path_credentials = "./keys/credentials.json"
        ):

        self.https = https
        self.root = root
        self.city = city

        # open credentials file and extract key
        with open(path_credentials, "r") as f:
            data = json.load(f)
        key = "appid=" + str(data["key"])

        # api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
        self.uri = self.https + self.root + self.city + "&" + key

    def apiCall4hwi(self):
        self.json_data = requests.get(self.uri).json()
        self.json_text = json.dumps(self.json_data, sort_keys=True, indent=2)
        
        self.name = self.json_data["name"]

        self.temp = self.json_data["main"]["temp"]
        self.temp_min = self.json_data["main"]["temp_min"]
        self.temp_max = self.json_data["main"]["temp_max"]

        self.icon = self.json_data["weather"][0]["icon"]
        self.iconUrl = "https://openweathermap.org/img/w/" + self.icon + ".png"
        # self.mytest = "mytest"
        # return self.json_data


def index(request):

    template = loader.get_template('weather/hwi.html')
    hwi = WeatherWismar()
    hwi.apiCall4hwi()

    api_response = hwi.json_data

    city = hwi.name

    temp = hwi.temp
    temp_min = hwi.temp_min
    temp_max = hwi.temp_max

    icon = hwi.icon
    iconUrl = hwi.iconUrl

    context = {
        # 'uri': hwi.uri,
        'city': city,
        'temp': temp,
        'temp_min': temp_min,
        'temp_max': temp_max,
        'icon': icon,
        'iconUrl': iconUrl,
        'api_response': api_response,
    }

    return HttpResponse(template.render(context, request))


