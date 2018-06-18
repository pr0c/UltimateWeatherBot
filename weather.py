#!/usr/bin/env python3
import requests, json

api = ('http://api.openweathermap.org/data/2.5/weather?q=%s&appid=1947089d8ce1bcc3c318ca30b2aba583',)

def getWeather(city):
    response = requests.get(api[0] % city);
    cityWeather = response.json()
    if cityWeather["cod"] == "404":
        weatherUI = ('404',)
        return weatherUI
    temp = cityWeather["main"]["temp"]
    weatherUI = list()
    weatherUI.append("--=====[Weather]=====--\n")
    weatherUI.append("City: %(cityName)s,%(country)s Weather: %(weather)s\n"
    % {"cityName": city, "weather": cityWeather["weather"][0]["description"], "country": cityWeather["sys"]["country"]})
    weatherUI.append("Temperature: %(t_fahr).01f F | %(t_celsius).01f C\n"
    % {"t_fahr": ((float(temp)-273.15)*1.8+32), "t_celsius": (float(temp)-273.15)})
    weatherUI.append("Wind speed: %(wind_speed)s\n" % {"wind_speed": cityWeather["wind"]["speed"]})
    weatherUI.append("=======================")
    return weatherUI
