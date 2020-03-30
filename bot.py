#This is for the test bot only

import telebot  #imports pyTelegramBotAPI
import time


bot_token = "935833055:AAGKz1k1ICpnZCveQ648TVLabUmN5QDWWa4"
bot = telebot.TeleBot(token=bot_token) #Bot Object
initial_response = '''Welcome to THE Feisty Fern Bot! This bot is intended to give you updates on the change of price of any token you choose. Within a customized time frame.

                    Commands:
                    /start -- You will see this message.
                    /enter -- Records your username into our database so we can get you started!
                    /watch -- Allows you to set which token to be updated on and the percentage of change within a timeframe of your choice. (example: '/watch BTC 15m <5%' [text an update when there's a 5% change in the price of BTC within 15 minutes])
                    /delete -- Deletes your username and data
                    '''

@bot.message_handler(commands=['start'])    #wrapper for all functions below
def send_welcome(message):
    '''This will send a message on the command /start'''
    bot.reply_to(message, initial_response) #this takes 2 parameters--the command /start and the bot's desired reply

@bot.message_handler(commands=['enter'])    #wrapper for all functions below
def send_help(message):
    '''This will send a message on the command /help'''
    username = message.from_user.username
    firstname = message.from_user.first_name
    text = message.text
    if username == None:    #users need a username in order to properly store their data in the DB
        bot.reply_to(message, "You need a username to use this bot ;)")
    else:
        bot.reply_to(message, "Waz Up, {}! Username: {}".format(firstname, username))

@bot.message_handler(commands=['watch'])    #wrapper for all functions below
def send_help(message):
    '''This will send a message on the command /help'''
    username = message.from_user.username
    firstname = message.from_user.first_name
    text = message.text
    if username == None:    #users need a username in order to properly store their data in the DB
        bot.reply_to(message, "You need a username to use this bot ;)")
    else:
        bot.reply_to(message, "Waz Up, {}! Username: {}".format(firstname, username))

    print(username)
    print(firstname)
    print(text)



bot.polling()
