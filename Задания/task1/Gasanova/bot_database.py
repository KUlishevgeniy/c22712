import telebot 
import psycopg2
from telebot import types
import random

connection = psycopg2.connect(host='localhost', dbname='work', user='dialuna', password='Timka07') # да-да :D
cursor = connection.cursor()

try:
	sel_query = """SELECT * FROM bot"""
	cursor.execute(sel_query)
except psycopg2.errors.UndefinedTable:
	connection.rollback()
	import problems
	sel_query = """SELECT * FROM bot"""
	cursor.execute(sel_query)
    
array = list(cursor.fetchall())


bot = telebot.TeleBot('secret')

@bot.message_handler(commands=['start'])
def start(message):
	sti = open('st.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)
	bot.send_message(message.chat.id, "ЙОУ, {0.first_name}!\nЯ твой помощник в мире скейтбординга😎".format(message.from_user, bot.get_me()))

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание кнопок
	btn1 = types.KeyboardButton("Лучший скейтборд этого сезона")
	btn2 = types.KeyboardButton("Предложение дня")
	btn3 = types.KeyboardButton("Выбор редакции нашей компании")
	markup.add(btn1, btn2, btn3)
	bot.send_message(message.chat.id,
                     'Лучший скейтборд этого сезона - это именно то, что тебе нужно, если хочешь быть самым крутым.\nПредложение дня - то, что актуально на сегодняшний день.\nВыбор редакции - просто доверься выбору наших сотрудников и тебе понравится :)\n',
                     reply_markup=markup)
                     
                     
@bot.message_handler(content_types=['text'])        
def handle_text(message):
	if (message.text.strip() == "Лучший скейтборд этого сезона"):
		i = random.choice(array)
		inf = f'Название: {i[2]}\nЦена: {i[3]}\n'
		bot.send_message(message.chat.id, inf)
		bot.send_photo(message.chat.id, open(i[4], 'rb'))
		cat = open('kotik.webm', 'rb')
		bot.send_video(message.chat.id, cat)
	elif (message.text.strip() == "Предложение дня"):
		i = random.choice(array)
		inf = f'Название: {i[2]}\nЦена: {i[3]}\n'
		bot.send_message(message.chat.id, inf)
		bot.send_photo(message.chat.id, open(i[4], 'rb'))
		cat = open('kotik.webm', 'rb')
		bot.send_video(message.chat.id, cat)	
	elif (message.text.strip() == "Выбор редакции нашей компании"):
		i = random.choice(array)
		inf = f'Название: {i[2]}\nЦена: {i[3]}\n'
		bot.send_message(message.chat.id, inf)
		bot.send_photo(message.chat.id, open(i[4], 'rb'))
		cat = open('kotik.webm', 'rb')
		bot.send_video(message.chat.id, cat)
	else:
		bot.send_message(message.chat.id, "Наш бот поможет подобрать вам или близким скейтборд мечты. Скорее пробуйте! ")
		
		
	
bot.polling(none_stop=True, interval=0)
