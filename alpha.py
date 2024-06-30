import os 
import telebot 
from keysus import key

BOT_TOKEN = key

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def welcome(message):
    bot.reply_to(message, "Hello there")

@bot.message_handler(func=lambda msg: True)
def echo_messages(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()

