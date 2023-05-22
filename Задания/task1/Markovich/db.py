import telebot
import psycopg2
from telebot import types
import random

connection = psycopg2.connect(dbname='dbdata', user='postgres',password='Q1w2e3r4', host='localhost')
cursor = connection.cursor()


sel_query = """SELECT * FROM public.pizza"""
cursor.execute(sel_query)
array = list(cursor.fetchall())

bot = telebot.TeleBot('6161398146:AAEY99Cox8omow3OnURN_mwXDOpAOfTp09w')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Хочу пирог!")
    item2 = types.KeyboardButton("Какова цена?")
    item3 = types.KeyboardButton("Описание")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(
        m.chat.id, '"Хочу пирог!" - для получения пирога\n "Какова цена?" - для получения цены\n "Описание" - описание',
        reply_markup=markup)

i = random.choice(array)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if (message.text.strip() == 'Хочу пирог!'):
        ans = f'{i[1]}\n'
        bot.send_message(message.chat.id, ans)
        try:
            bot.send_photo(message.chat.id, open(i[4], 'rb'))
        except telebot.apihelper.ApiTelegramException:
            bot.send_message(message.chat.id, "Проблемы с загрузкой картинки....Продолжайте")
    elif (message.text.strip() == 'Какова цена?'):
        ans = f'{i[3]}\n'
        bot.send_message(message.chat.id, ans)
    elif (message.text.strip() == 'Описание'):
        ans = f'{i[2]}\n'
        bot.send_message(message.chat.id, ans)

bot.polling(none_stop=True, interval=0)

cursor.close()
connection.close()