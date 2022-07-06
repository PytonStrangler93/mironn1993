from email import message
import telebot
from telebot import types
#БОТ ИЗ ВИДЕО
bot = telebot.TeleBot#('5434044927:AAGXRe1KEWlHOHGS5mjMm__qFgwVslpnEds')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    
#@bot.message_handler(content_types=['text'])
#def get_user_text(message):
#   if message.text == "hello":
#      bot.send_message(message.chat.id, 'Hi you too!', parse_mode='html')    
  # elif message.text == "id":
    #    bot.send_message(message.chat.id, f'Your ID: {message.from_user.id}', parse_mode='html')
    #elif message.text == "photo":
     #   photo = open('bebra.gif', 'rb' )
      #  bot.send_photo(message.chat.id, photo)
    #else:
     #   bot.send_message(message.chat.id, "I don't understand u", parse_mode='html')   
        
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Wow nice photo!')  

@bot.message_handler(commands=['/help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('website')
    start = types.KeyboardButton('start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Go to web!', reply_markup=markup)
    
bot.polling(none_stop=True)