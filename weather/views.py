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
        # print(self.json_text)
        return self.json_data



def index(request):

    template = loader.get_template('weather/hwi.html')
    hwi = WeatherWismar()

    context = {
        'uri': hwi.uri,
        'api_response': WeatherWismar().apiCall4hwi()
    }

    return HttpResponse(template.render(context, request))


