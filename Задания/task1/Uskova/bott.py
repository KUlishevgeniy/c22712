import telebot
import psycopg2
from telebot import types
import random

connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()
try:
    sel_query = """SELECT * FROM public.f0ood"""
    cursor.execute(sel_query)
except psycopg2.errors.UndefinedTable:
    connection.rollback()
    import problems
    sel_query = """SELECT * FROM public.f0ood"""
    cursor.execute(sel_query)

array = list(cursor.fetchall())
bot = telebot.TeleBot('6280771915:AAG2rcsqHZbUjeaOD-llwR-UU-LabMprKBo')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Роллы")
    item2 = types.KeyboardButton("Хочу еще!")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id,
                     '"Роллы" - получите случайную порцию роллов\n'
                     ' "Хочу еще!" - вдруг вы не наелись', reply_markup=markup)

i = random.choice(array)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    global i
    if (message.text.strip() == 'Роллы'):
        i = random.choice(array)
        ans = f'Название: {i[1]}\nГраммы: {i[2]}\nОписание: {i[3]}\nЦена за 4 штуки: {i[4]}\n'
        bot.send_message(message.chat.id, ans)
        bot.send_photo(message.chat.id, open(i[5], 'rb'))
    elif (message.text.strip() == 'Хочу еще!'):
        bot.send_message(message.chat.id, 'Ввод: ' + message.text)

bot.polling(none_stop=True, interval=0)
