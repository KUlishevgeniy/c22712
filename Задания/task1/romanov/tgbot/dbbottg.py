import telebot
import psycopg2
import config
from telebot import types
import random
import parshell

connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')

cursor = connection.cursor()

sel_query = """SELECT * FROM public.parser"""
cursor.execute(sel_query)
array = list(cursor.fetchall())

bot = telebot.TeleBot('5803518584:AAEDCHZdvz-RurPpxJhVV0MNeCxWDVU5czk')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Случайная доска")
    item2 = types.KeyboardButton("П")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id,
                     '"Случайная доска" (название, цена, фото)\n "П" - д',
                     reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if (message.text.strip() == 'Случайная доска'):
        i = random.choice(array)
        ans = f'Название: {i[1]}\nЦена: {i[2]}\n'
        bot.send_message(message.chat.id, ans)
        bot.send_photo(message.chat.id, open(i[3], 'rb'))
    elif (message.text.strip() == 'П'):
        bot.send_message(message.chat.id, 'Вы нажали кнопку п: ' + message.text)


bot.polling(none_stop=True, interval=0)