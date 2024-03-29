import telebot
import psycopg2
import config
from telebot import types
import random

connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')

cursor = connection.cursor()

sel_query = """SELECT * FROM public.parser"""
cursor.execute(sel_query)
array = list(cursor.fetchall())

bot = telebot.TeleBot('6293063008:AAEFscB5LEjxC_4irrcgT-z6Eb0NXYOxZng')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомный продукт")
    item2 = types.KeyboardButton("Повтори!")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id,
                     '"Рандомный продукт" - для получения карточки товара\n "Повтори!" - для повторения сообщений.',
                     reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if (message.text.strip() == 'Рандомный продукт'):
        i = random.choice(array)
        ans = f'Название: {i[1]}\nЦена: {i[2]}\nРейтинг: {i[3]}\n'
        bot.send_message(message.chat.id, ans)
        bot.send_photo(message.chat.id, open(i[4], 'rb'))
    elif (message.text.strip() == 'Повтори!'):
        bot.send_message(message.chat.id, 'Ввод: ' + message.text)


bot.polling(none_stop=True, interval=0)
