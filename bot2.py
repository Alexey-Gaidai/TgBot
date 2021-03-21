import telebot
import config

from telebot import types
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('pic/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Привет, Дружище! \nЯ - <b>{1.first_name}</b>, бот сделанный для лабораторной работы по ИСиТ.".format(message.from_user, bot.get_me()),
      parse_mode='html')
 
@bot.message_handler(content_types=['voice'])
def onetwothree(message):
  if message.content_type == 'voice':
    bot.send_message(message.chat.id, "Голосовые не принимаю)")
bot.polling(none_stop=True)