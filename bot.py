#This is for the test bot only

import telebot  #imports pyTelegramBotAPI
import os
from flask import Flask, request

bot_token = "935833055:AAGKz1k1ICpnZCveQ648TVLabUmN5QDWWa4"
bot = telebot.TeleBot(token=bot_token) #Bot Object
server = Flask(__name__)

@bot.message_handler(commands=['start'])    #wrapper for all functions below
def send_welcome(message):
    '''This will send a message on the command /start'''
    bot.reply_to(message, "Welcome to THE Feisty Fern test bot! Use the command /help for more info") #this takes 2 parameters--the command /start and the bot's desired reply

@bot.message_handler(commands=['help'])    #wrapper for all functions below
def send_welcome(message):
    '''This will send a message on the command /help'''
    bot.reply_to(message, "Testing underway")

@server.route('/' + bot_token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://heroku.com/' + bot_token)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
