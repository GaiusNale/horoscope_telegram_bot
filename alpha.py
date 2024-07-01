import os 
import requests
import telebot 
from keysus import key

BOT_TOKEN = key

def get_daily_horoscope(sign: str, day: str) -> dict:
    

# bot = telebot.TeleBot(BOT_TOKEN)

# @bot.message_handler(commands=['start', 'hello'])
# def welcome(message):
#     bot.reply_to(message, "Oi oi oi")

# @bot.message_handler(func=lambda msg: True)
# def echo_messages(message):
#     bot.reply_to(message, message.text)

# bot.infinity_polling()

