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

def select(ID):
    s_query = f'''SELECT * FROM bot where ID = {ID}'''
    cursor.execute(s_query)
    return cursor.fetchone()




bot = telebot.TeleBot('secret')

@bot.message_handler(commands=['start'])
def start(message):
	sti = open('st.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)
	bot.send_message(message.chat.id, "ЙОУ, {0.first_name}!\nЯ твой помощник в мире скейтбординга😎".format(message.from_user, bot.get_me()))

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание кнопок
	btn1 = types.KeyboardButton("Лучший скейтборд этого сезона")
	btn2 = types.KeyboardButton("Предложение дня")
	btn3 = types.KeyboardButton("Выбор скейта по ID")
	markup.add(btn1, btn2, btn3)
	bot.send_message(message.chat.id,
                     'Лучший скейтборд этого сезона - это именно то, что тебе нужно, если хочешь быть самым крутым.\nПредложение дня - то, что актуально на сегодняшний день.\nВыбор скейта по ID - просто доверься выбору наших сотрудников и тебе понравится :)\n',
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
	elif (message.text.strip() == "Выбор скейта по ID"):
		sent = bot.send_message(message.chat.id,
                         f'Введите идентификатор(ID, целое число) от 1 до 13, чтобы получить информацию о конкретном предложении: ')
		bot.register_next_step_handler(sent, ret_id)
	else:
		bot.send_message(message.chat.id, "Наш бот поможет подобрать вам или близким скейтборд мечты. Скорее пробуйте! ")
		
def ret_id(message):
	try:
        	now_id = (message.text)
        	now_id = int(float(now_id))
        	z = list(select(now_id))
        	a2 = f'Название: {z[2]};\nЦена: {z[3]};\n'
        	bot.send_message(message.chat.id, a2)
        	bot.send_photo(message.chat.id, open(z[4], 'rb'))
        	bot.send_message(message.chat.id, "Для повторного поиска по ID воспользуйтесь соответствующей кнопкой в 'меню'")
	except ValueError:
		bot.send_message(message.chat.id,
                         "По такому ID нет данных. Попробуйте заново через 'меню' кнопок найти интересующее вас предложение")
		
		
	
bot.polling(none_stop=True, interval=0)

cursor.close()
connection.close()



