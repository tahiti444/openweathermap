from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .services.load import *


def index(request, units="EU"):

    # load template to render
    template = loader.get_template("weather/hwi.html")
    # create an object for Wismars weather
    hwi = WeatherWismar()
    hwi.apiCall4hwi() # and execute the API call
    api_response = hwi.json_data
    # parse to the contents
    if units == "EU":
        context = {
            # 'uri': hwi.uri,
            "city": hwi.name,
            "temp": round(hwi.temp - 273, ndigits=1),
            "temp_min": round(hwi.temp_min - 273, ndigits=1),
            "temp_max": round(hwi.temp_max - 273, ndigits=1),
            "icon": hwi.icon,
            "iconUrl": hwi.iconUrl,
            "api_response": api_response,
        }

    return HttpResponse(template.render(context, request))
