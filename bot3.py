import telebot
import config

from telebot import types
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('pic/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Привет, Дружище! \nЯ - <b>{1.first_name}</b>, бот сделанный для лабораторной работы по ИСиТ.\nНапиши мне Привет!".format(message.from_user, bot.get_me()),
      parse_mode='html')
name = '';
surname = '';
age = 0;

@bot.message_handler(content_types=['text'])
def start(message):
	if message.text == 'Привет':
		bot.send_message(message.from_user.id, "Как тебя зовут?");
		bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
	else:
		bot.send_message(message.from_user.id, 'Напиши: Привет');
def get_name(message):
	global name;
	name = message.text;
	bot.send_message(message.from_user.id, 'Привет, '+name+'. Какая у тебя фамилия?');
	bot.register_next_step_handler(message, get_surname);
def get_surname(message):
	global surname;
	surname = message.text;
	bot.send_message(message.from_user.id,'Короче, '+name+' '+surname+', я тебе код написал и в благородство играть не буду: выполнишь для меня пару лаб — и мы в расчете. Заодно посмотрим, как быстро у тебя приложение после ребута компилируется. А по твоей теме постараюсь разузнать. Хрен его знает, на кой ляд тебе этот SQL сдался, но я в чужие дела не лезу, хочешь изучить, значит надо...');
	bot.send_message(message.from_user.id,'А сколько тебе лет то?');
	bot.register_next_step_handler(message, get_age);
def get_age(message):
	global age;
	while age == 0: #проверяем что возраст изменился
		try:
			age = int(message.text) #проверяем, что возраст введен корректно
		except Exception:
			bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
	bot.send_message(message.from_user.id, 'Понял, '+name+', тебе ' +str(age)+' лет. Смотри, не постарей раньше времени')
bot.polling(none_stop=True)
