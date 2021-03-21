import telebot
import config

from telebot import types
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('pic/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📰Покажи IT ресурсы📰")
    item2 = types.KeyboardButton("📚Изучение Программирования📚")
    item3 = types.KeyboardButton("🧘🏻Релакс🧘🏻")
    item4 = types.KeyboardButton("закрыть")

    markup.add(item1, item2, item3, item4)
 
    bot.send_message(message.chat.id, "Привет, Дружище! \nЯ - <b>{1.first_name}</b>, бот сделанный для лабораторной работы по ИСиТ.".format(message.from_user, bot.get_me()),
    	parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def onetwothree(message):
    if message.chat.type == 'private':
        if message.text == 'закрыть':
            markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, 'Выполнено', reply_markup=markup)
bot.polling(none_stop=True)
