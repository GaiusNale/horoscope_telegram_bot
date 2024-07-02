import os 
import requests
import telebot 
from keysus import key

BOT_TOKEN = key

def get_daily_horoscope(sign: str, day: str) -> dict:
    """ Get Daily Horoscope 
    Data format 
    sign: str
    date: str (can be used as Today, Yesterday, Tommorow or a particular day i.e  YYYY-MM-DD)"""

    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    params = {"sign":sign, "day":day}
    response = requests.get(url, params)

    return response.json()


# bot = telebot.TeleBot(BOT_TOKEN)

# @bot.message_handler(commands=['start', 'hello'])
# def welcome(message):
#     bot.reply_to(message, "Oi oi oi")

# @bot.message_handler(func=lambda msg: True)
# def echo_messages(message):
#     bot.reply_to(message, message.text)

# bot.infinity_polling()

