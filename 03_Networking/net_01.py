# Fetch Current Weather
# -*- coding: utf-8 -*-

import requests
import re


def wind_degrees_to_name(degree: int) -> str:
    if degree > 337.5:
        return 'Northerly'
    if degree > 292.5:
        return 'North Westerly'
    if degree > 247.5:
        return 'Westerly'
    if degree > 202.5:
        return 'South Westerly'
    if degree > 157.5:
        return 'Southerly'
    if degree > 122.5:
        return 'South Easterly'
    if degree > 67.5:
        return 'Easterly'
    if degree > 22.5:
        return 'North Easterly'
    return 'Northerly'


def weather_by_zip_code():
    # ---> getting and checking zip code <---
    pattern = r"^\d\d-\d\d\d$"
    entered_zip_code = input("Podaj kod pocztowy: ")
    # checking if zip code has proper format
    if not re.match(pattern, entered_zip_code):
        raise NameError("Invalid zip code format!")

    # ---> getting site's code <---
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?zip={},pl&units=metric&directi&appid=99358e54d159b50cfb3520522cfa187c".format(entered_zip_code))

    request_json = r.json()

    # ---> creating output message <---
    # making sure that the zip code exists
    try:
        city_name = "city name: " + request_json['name']
    except KeyError:
        print("This zip code doesn't exist")
        raise
    country = "country: " + request_json['sys']['country']
    temp = "temperature: " + str(request_json['main']['temp']) + " °C"
    humidity = "humidity: " + str(request_json['main']['humidity']) + " %"
    pressure = "pressure: " + str(request_json['main']['pressure']) + " hPa"
    wind_speed = "wind speed: " + str(request_json['wind']['speed']) + " m/s"
    wind_direction = "wind direction: " + wind_degrees_to_name(request_json['wind']['deg'])
    weather_description = "weather description: " + request_json['weather'][0]['description']

    print(city_name, country, temp, humidity, pressure, wind_speed, wind_direction, weather_description, sep='\n')


weather_by_zip_code()
