#This is for the test bot only

import telebot  #imports pyTelegramBotAPI
import time
import sqlite3
from coingeckodata import *
from db_functions import *

### Essential Variables ###
bot_token = "1239975962:AAHIVcPidz-MA8fQWSHDrpdh8Xlplcxs2c0" #Telegram Bot
bot = telebot.TeleBot(token=bot_token) #Bot Object

initial_response = '''Welcome to Trevor's Telegram Bot! This bot is intended to give you updates on the change of price of any token you choose, within a 10 minute timeframe.

                    Commands:
                    /start -- You will see this message.
                    /watch -- Allows you to set which token to be updated on and the percentage of change within a 10 minute timeframe. (example: '/watch bitcoin 5%' [text an update when there's a 5% change in the price of BTC within 10 minutes])
                    /stop -- Halts any updates
                    '''

### Initial SQL Table creation ###
SQL.initial_bot_table()

### Bot Commands ###
@bot.message_handler(commands=['start'])    #wrapper for all functions below
def send_welcome(message):
    '''This will send a message on the command /start'''
    bot.reply_to(message, initial_response) #this takes 2 parameters--the command /start and the bot's desired reply


@bot.message_handler(commands=['watch'])    #wrapper for all functions below
def send_watch(message):
    '''This will send a response and perform all functions related
     to the command /watch'''
    username = message.from_user.username
    firstname = message.from_user.first_name
    text = message.text
    print(text)
    if username == None:    #users need a username in order to properly store their data in the DB
        bot.reply_to(message, "You need a username to use this bot ;)")
    else:
        valid_info = WatchMessage.is_valid(text)
        if valid_info == True:
            #api_data = CoinGecko.watchquery(username, text)
            bot.reply_to(message, "Thank you, {}! Your command is valid".format(username))
        else:
            bot.reply_to(message, "We're sorry, {}. Your command does not match the format this bot requires.".format(username))


@bot.message_handler(commands=['stop'])    #wrapper for all functions below
def send_delete(message):
    '''For the command /stop, this will delete all of the user's SQLite tables, thus stopping any future updates'''
    username = message.from_user.username
    deleted_user = SQL.delete_user(username)
    if deleted_user == "User existed":
        bot.reply_to(message, "You will no longer recieve updates. Send the /watch command to receive updates again")
    elif deleted_user == "User doesn't exist":
        bot.reply_to(message, "We have no record of you in our database. Send the /watch command to get started ;)")


### Runs the Bot ###
if __name__ == "__main__":
    bot.polling()
