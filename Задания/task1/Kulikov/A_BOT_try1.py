import telebot
import psycopg2
from telebot import types
tovars=['1','2','3','4']

def getcontent(i):
    connection = psycopg2.connect(dbname='dbdata',
                                  user='postgres', password='Q1w2e3r4',
                                  host='localhost')
    cursor = connection.cursor()
    cursor.execute('''SELECT id, phone, price
    FROM public.svyaznoy
    where id = ''' + str(i))
    b = cursor.fetchall()
    for a in b:
        c = 'Название модели: ' + str(a[1]) + ' Цена: ' + str(a[2])
    cursor.close()
    connection.close()
    return c

bot = telebot.TeleBot('6053050329:AAFEBguQ5-UE80bB_aNjjSoUdIT91BlPJCY')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Здравствуйте, я Ваш бот, и вы попали в магазин, в котором есть всего 4 товара! Напишите цифру от 1 до 4,чтобы узнать информацию о нем)')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() in tovars:
        answer = getcontent(message.text.strip())
        bot.send_message(message.chat.id, answer)
        img = open('tovar'+str(message.text.strip())+'.jpeg','rb')
        bot.send_photo(message.chat.id, img)
    else:
        answer = 'Да, пока только 4, но все впереди!'
        bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True, interval=0)