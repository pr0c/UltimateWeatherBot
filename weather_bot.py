#!/usr/bin/env python3
import config, telebot, weather
from telebot import types

bot = telebot.TeleBot(config.token, threaded=True, skip_pending=False, num_threads=4)

@bot.message_handler(commands=['start'])
def handle_start_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=None, one_time_keyboard=True, selective=None, row_width=1)
    itembtn1 = types.KeyboardButton('/help')
    itembtn2 = types.KeyboardButton('/weather')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Choose a command", reply_markup=markup)

@bot.message_handler(commands=['weather'])
def handle_choose_city(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=None, one_time_keyboard=True, selective=None, row_width=1)
    itembtn1 = types.KeyboardButton('Lviv')
    itembtn2 = types.KeyboardButton('Skvyra')
    itembtn3 = types.KeyboardButton('Kyiv')
    itembtn4 = types.KeyboardButton('/start')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Choose a city:", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_get_weather(message):
    cityWeatherList = weather.getWeather(message.text)
    if cityWeatherList[0] == "404":
        bot.send_message(message.chat.id, "City not found")
        return True

    cityWeather = ""
    for i in cityWeatherList:
        cityWeather += i
    bot.send_message(message.chat.id, cityWeather)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0, timeout=20)
