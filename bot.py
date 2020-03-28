#This is for the test bot only

import telebot  #imports pyTelegramBotAPI
import time     #we need this later error handling

bot_token = "1077672229:AAF748sRH3irmCoraBVkIyXg8lACTQEyttY"

bot = telebot.TeleBot(token=bot_token) #Bot Object

@bot.message_handler(commands=['start'])    #wrapper for all functions below
def send_welcome(message):
    '''This will send a message on the command /start'''
    bot.reply_to(message, "Welcome to Feisty Fern's test bot! Use the command /help for more info") #this takes 2 parameters--the command /start and the bot's desired reply

@bot.message_handler(commands=['help'])    #wrapper for all functions below
def send_welcome(message):
    '''This will send a message on the command /help'''
    bot.reply_to(message, "TEST")



###Telegram will try to cancel this connection every hour. This will temporarily stop it from shutting down
while True:
    try:
        bot.polling() #activates the connection between the script and the bot
    except Exception:
        time.sleep(15)
