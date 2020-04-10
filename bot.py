#This is for the test bot only

import telebot  #imports pyTelegramBotAPI
import time
import sqlite3
from coingeckodata import *
from db_functions import *

### Essential Variables ###
bot_token = "935833055:AAGKz1k1ICpnZCveQ648TVLabUmN5QDWWa4" #Telegram Bot
bot = telebot.TeleBot(token=bot_token) #Bot Object

initial_response = '''Welcome to THE Feisty Fern Bot! This bot is intended to give you updates on the change of price of any token you choose. Within a customized time frame.

                    Commands:
                    /start -- You will see this message.
                    /enter -- Records your username into our database so we can get you started!
                    /watch -- Allows you to set which token to be updated on and the percentage of change within a timeframe of your choice. (example: '/watch BTC 15m <5%' [text an update when there's a 5% change in the price of BTC within 15 minutes])
                    /delete -- Deletes your username and data
                    '''

### Initial SQL Table creation ###
SQL.initial_bot_table()

### Bot Commands ###
@bot.message_handler(commands=['start'])    #wrapper for all functions below
def send_welcome(message):
    '''This will send a message on the command /start'''
    bot.reply_to(message, initial_response) #this takes 2 parameters--the command /start and the bot's desired reply

@bot.message_handler(commands=['enter'])    #wrapper for all functions below
def send_enter(message):
    '''This will send a response and perform all functions related
     to the command /enter'''
    username = message.from_user.username
    firstname = message.from_user.first_name
    if username == None:    #users need a username in order to properly store their data in the DB
        bot.reply_to(message, "You need a username to use this bot ;)")
    else:
        SQL.create_tables_for_user(username)
        bot.reply_to(message, "Welcome, {}! Would you like to get updates on a certain token? ( /watch ) Or, would you like to delete your info? ( /delete )  ".format(firstname, username))

@bot.message_handler(commands=['watch'])    #wrapper for all functions below
def send_watch(message):
    '''This will send a response and perform all functions related
     to the command /watch'''
    username = message.from_user.username
    text = message.text
    print(text)
    if username == None:    #users need a username in order to properly store their data in the DB
        bot.reply_to(message, "You need a username to use this bot ;)")
    else:
        valid_info = WatchMessage.is_valid(text)
        if valid_info == True:
            bot.reply_to(message, "Thank you, {}! Your command is valid".format(username))
        else:
            bot.reply_to(message, "We're sorry, {}. Your command does not match the format this bot requires.".format(username))



@bot.message_handler(commands=['delete'])    #wrapper for all functions below
def send_delete(message):
    '''For the command /delete, this will delete all of the user's SQLite tables'''
    username = message.from_user.username
    deleted_user = SQL.delete_user(username)
    if deleted_user == "User existed":
        bot.reply_to(message, "All of your data has been deleted. If you want to use this bot again you have to send another /enter command")
    elif deleted_user == "User doesn't exist":
        bot.reply_to(message, "We have no record of you in our database. Send the /enter command to get started ;)")

### Runs the Bot ###
if __name__ == "__main__":
    bot.polling()
