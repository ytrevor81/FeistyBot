#This is for the test bot only

import telebot  #imports pyTelegramBotAPI
import time


bot_token = "935833055:AAGKz1k1ICpnZCveQ648TVLabUmN5QDWWa4"
bot = telebot.TeleBot(token=bot_token) #Bot Object

@bot.message_handler(commands=['start'])    #wrapper for all functions below
def send_welcome(message):
    '''This will send a message on the command /start'''
    bot.reply_to(message, "Welcome to THE Feisty Fern test bot! Use the command /help for more info") #this takes 2 parameters--the command /start and the bot's desired reply

@bot.message_handler(commands=['help'])    #wrapper for all functions below
def send_help(message):
    '''This will send a message on the command /help'''
    username = message.from_user.username
    firstname = message.from_user.first_name
    if username == None:    #users need a username in order to properly store their data in the DB
        bot.reply_to(message, "You need a username to use this bot ;)")
    else:
        bot.reply_to(message, "Waz Up, {}! Username: {}".format(firstname, username))

    print(username)
    print(firstname)



bot.polling()
