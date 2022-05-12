from email import message
from tracemalloc import start
import telebot
import random
from telebot import types
bot = telebot.TeleBot("5158247388:AAGj0293-UKxZDXDv2IMIeMseEH1vGVpDfk")

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.reply_to(message, 'Hello! ' +  message.from_user.first_name)

@bot.message_handler(commands=['help'])
def helperr(message):
  bot.send_message(message.chat.id,
                                  """برای شروع 
  /start
  برای بازی
  /newGame
  برای QrCode
  /qrcode
  """)

@bot.message_handler(commands=['newGame'])
def start_message(message):
  bot.reply_to(message,"Choose a number between 1 to 50.")
  rdm = random.randint(0,50)
  @bot.message_handler(func= lambda m: True)
  def echo(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('a')  
    a = int(message.text)
    if rdm==a:
      bot.reply_to(message,'nice')
    elif a<rdm:
      bot.reply_to(message,'up')
    elif a>rdm:
      bot.reply_to(message,'down')

bot.infinity_polling()
