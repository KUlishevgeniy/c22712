import telebot
import psycopg2
from telebot import types
tovars=['1','2','3','4','5','6','7','8','9','10']

def getcontent(i):
    connection = psycopg2.connect(dbname='dbdata',
                                  user='postgres', password='Q1w2e3r4',
                                  host='localhost')
    cursor = connection.cursor()
    cursor.execute('''SELECT id, name, price
    FROM public.notes
    where id = ''' + str(i))
    b = cursor.fetchall()
    for a in b:
        c = 'Название фильма: ' + str(a[1]) + ' Рейтинг: ' + str(a[2])
    cursor.close()
    connection.close()
    return c

bot = telebot.TeleBot('6195865124:AAGar9f6rH3PYUtB4wVEpWFiagiX_F-YSAo')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Добрый день, назовите номер фильма и я выведу его название, рейтинг и картинку)))')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() in tovars:
        answer = getcontent(message.text.strip())
        bot.send_message(message.chat.id, answer)
        img = open('C:\\Users\\rusta\\OneDrive\\Рабочий стол\\pictures111\\' + str(message.text.strip())+'.jpg','rb')
        bot.send_photo(message.chat.id, img)
    else:
        answer = 'Иди учи уроки, фильмы потом посмотришь'
        bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True, interval=0)