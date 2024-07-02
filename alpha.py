import os 
import requests
import telebot 
from keysus import key

BOT_TOKEN = key
bot = telebot.TeleBot(BOT_TOKEN)


def get_daily_horoscope(sign: str, day: str) -> dict:
    """ Get Daily Horoscope 
    Data format 
    sign: str
    date: str (can be used as Today, Yesterday, Tommorow or a particular day i.e  YYYY-MM-DD)"""

    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    params = {"sign":sign, "day":day}
    response = requests.get(url, params)

    return response.json()

@bot.message_handler(commands= ['horoscope'])

def sign_picker(message):
    text = "What's your Zodiac sign?"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode= "Markdown")
    bot.register_next_step_handler(sent_msg, day_picker)

def day_picker(message):
    sign = message.text 
    text = "What day would you like to find out about?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date with the format YYYY-MM-DD"
    sent_msg = bot.send_message (
        message.chat.id, text, parse_mode= "Markdown"
    )
    bot.register_next_step_handler(
        sent_msg, fetch_horoscope, sign_picker
    )


# @bot.message_handler(commands=['start', 'hello'])
# def welcome(message):
#     bot.reply_to(message, "Oi oi oi")

# @bot.message_handler(func=lambda msg: True)
# def echo_messages(message):
#     bot.reply_to(message, message.text)

# bot.infinity_polling()

