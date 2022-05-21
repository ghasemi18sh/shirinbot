import telebot
import random
import qrcode
from telebot import types
from telebot import TeleBot

bot = telebot.TeleBot("5158247388:AAGj0293-UKxZDXDv2IMIeMseEH1vGVpDfk")

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.reply_to(message, 'سلام! ' +  message.from_user.first_name + "برای کمک /help رو بزن")

@bot.message_handler(commands=['help'])
def helperr(message):
  bot.send_message(message.chat.id,
                                  """برای شروع 
  /start
  برای بازی
  /newGame
  برای QrCode
  /qrcode
  برای سن
  /age
  """)

@bot.message_handler(commands =['age'])
def send_age(message):
    bot.reply_to(message,f"سال تولدت را وارد کن")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        year = int(message.text)
        now = 1401 - year
        bot.reply_to(message,f"تو هستی {now} ساله.")


@bot.message_handler(commands=['newGame'])
def start_message(message):
  bot.reply_to(message," یک عدد بین 1 تا 50 انتخاب کن.")
  rdm = random.randint(0,50)
  @bot.message_handler(func= lambda m: True)
  def echo(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('a')  
    a = int(message.text)
    if rdm==a:
      bot.reply_to(message,'افرین')
    elif a<rdm:
      bot.reply_to(message,'بالا')
    elif a>rdm:
      bot.reply_to(message,'پایین')
@bot.message_handler(commands=['qrcode'])
def creat_qr(message):
    bot.send_message(message.chat.id, 'متن را وارد کن ')
    @bot.message_handler(content_types=['text'])
    def creat_qr(message):
        qrcode_image =  qrcode.make(message.text)
        qrcode_image.save('qrcode.png')
        photo = open('qrcode.png','rb')
        bot.send_photo(message.chat.id, photo)

bot.infinity_polling()