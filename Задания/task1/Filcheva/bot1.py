import telebot
import psycopg2
from telebot import types
# Создаем экземпляр бота
bot = telebot.TeleBot('5898574743:AAF2y_y3U2IfWwQVJ_lF6mmiDPlx1YgU9-Q')
# Функция, обрабатывающая команду /start

@bot.message_handler(commands=["start"])
def start_messanger(messanger):
    connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4t5')
    cursor = connection.cursor()
    cursor.execute("select id, name from Distilleries")
    first_step = []
    for id, name in cursor.fetchall():
        f_s = str(id) + '. ' + name
        first_step.append(f_s)
    my_str = '\n'.join(first_step)
    bot.send_message(messanger.chat.id, 'Я на связи. Выберите интересующую вас Винокурню, введите ее номер\n' + my_str.strip())
    cursor.close()
    connection.close()


@bot.message_handler(content_types=["text"])
def output(put):
    n = put.text.strip()
    m = int(n)
    connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4t5')
    cursor = connection.cursor()

    if (m==1):
        cursor.execute("select place, contacts, imagelink from Distilleries where id in(1)")

        for place, contacts, imagelink in cursor.fetchall():
            answer = 'Адрес: ' + place + '     ' + 'Контакты: ' + contacts + '     ' + 'Фото: ' + imagelink
            bot.send_message(put.chat.id, answer)
        cursor.close()
        connection.close()

    if (m == 2):
        cursor.execute("select place, contacts, imagelink from Distilleries where id in(2)")

        for place, contacts, imagelink in cursor.fetchall():
            answer = 'Адрес: ' + place + '     ' + 'Контакты: ' + contacts + '     ' + 'Фото: ' + imagelink
            bot.send_message(put.chat.id, answer)
        cursor.close()
        connection.close()

    if (m == 3):
        cursor.execute("select place, contacts, imagelink from Distilleries where id in(3)")

        for place, contacts, imagelink in cursor.fetchall():
            answer = 'Адрес: ' + place + '     ' + 'Контакты: ' + contacts + '     ' + 'Фото: ' + imagelink
            bot.send_message(put.chat.id, answer)
        cursor.close()
        connection.close()

    if (m == 4):
        cursor.execute("select place, contacts, imagelink from Distilleries where id in(4)")

        for place, contacts, imagelink in cursor.fetchall():
            answer = 'Адрес: ' + place + '     ' + 'Контакты: ' + contacts + '     ' + 'Фото: ' + imagelink
            bot.send_message(put.chat.id, answer)
        cursor.close()
        connection.close()

    if (m == 5):
        cursor.execute("select place, contacts, imagelink from Distilleries where id in(5)")

        for place, contacts, imagelink in cursor.fetchall():
            answer = 'Адрес: ' + place + '     ' + 'Контакты: ' + contacts + '     ' + 'Фото: ' + imagelink
            bot.send_message(put.chat.id, answer)
        cursor.close()
        connection.close()

    if (m == 6):
        cursor.execute("select place, contacts, imagelink from Distilleries where id in(6)")

        for place, contacts, imagelink in cursor.fetchall():
            answer = 'Адрес: ' + place + '     ' + 'Контакты: ' + contacts + '     ' + 'Фото: ' + imagelink
            bot.send_message(put.chat.id, answer)
        cursor.close()
        connection.close()

    if (m == 7):
        cursor.execute("select place, contacts, imagelink from Distilleries where id in(7)")

        for place, contacts, imagelink in cursor.fetchall():
            answer = 'Адрес: ' + place + '     ' + 'Контакты: ' + contacts + '     ' + 'Фото: ' + imagelink
            bot.send_message(put.chat.id, answer)
        cursor.close()
        connection.close()

    if (m == 8):
        cursor.execute("select place, contacts, imagelink from Distilleries where id in(8)")

        for place, contacts, imagelink in cursor.fetchall():
            answer = 'Адрес: ' + place + '     ' + 'Контакты: ' + contacts + '     ' + 'Фото: ' + imagelink
            bot.send_message(put.chat.id, answer)
        cursor.close()
        connection.close()

    if (m == 9):
        cursor.execute("select place, contacts, imagelink from Distilleries where id in(9)")

        for place, contacts, imagelink in cursor.fetchall():
            answer = 'Адрес: ' + place + '     ' + 'Контакты: ' + contacts + '     ' + 'Фото: ' + imagelink
            bot.send_message(put.chat.id, answer)
        cursor.close()
        connection.close()

    if (m == 10):
        cursor.execute("select place, contacts, imagelink from Distilleries where id in(10)")

        for place, contacts, imagelink in cursor.fetchall():
            answer = 'Адрес: ' + place + '     ' + 'Контакты: ' + contacts + '     ' + 'Фото: ' + imagelink
            bot.send_message(put.chat.id, answer)
        cursor.close()
        connection.close()


bot.polling()
