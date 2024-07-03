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
    date: str (can be used as Today, Yesterday, Tomorrow or a particular day i.e  YYYY-MM-DD)"""

    url = "https://aztro.sameerkumar.website"
    params = {"sign": sign, "day": day}
    response = requests.post(url, params=params)
    
    # Check if the request was successful
    if response.status_code != 200:
        return {"error": f"Failed to retrieve data. Status code: {response.status_code}"}
    
    return response.json()

@bot.message_handler(commands=['horoscope'])
def sign_picker(message):
    text = "What's your Zodiac sign?"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_picker)

def day_picker(message):
    sign = message.text
    text = "What day would you like to find out about?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date with the format YYYY-MM-DD"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, lambda msg: fetch_horoscope(msg, sign.capitalize()))

def fetch_horoscope(message, sign):
    day = message.text
    horoscope = get_daily_horoscope(sign, day)
    
    if "error" in horoscope:
        bot.send_message(message.chat.id, horoscope["error"])
        return
    
    # Construct the horoscope message from the response
    horoscope_msg = f"*Horoscope*: {horoscope.get('description', 'No description available')}\n\n*Sign:* {sign}\n*Day*: {day.capitalize()}"
    bot.send_message(message.chat.id, "Here's your horoscope.")
    bot.send_message(message.chat.id, horoscope_msg, parse_mode="Markdown")

@bot.message_handler(commands=['start', 'hello'])
def welcome(message):
    bot.reply_to(message, "Hello! You can use the /horoscope command to get your horoscopes!")

bot.infinity_polling()
