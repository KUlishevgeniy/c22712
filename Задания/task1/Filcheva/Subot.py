import telebot
import psycopg2
from telebot import types
# Создаем экземпляр бота
bot = telebot.TeleBot('5898574743:AAF2y_y3U2IfWwQVJ_lF6mmiDPlx1YgU9-Q')
# Функция, обрабатывающая команду /start

def reply_to_user(message, bot):
    query = f"insert into Distilleries(name, place, contacts) values ('{message.text.strip()}', "
    bot.send_message(message.chat.id, "Введите адрес винокурни")
    bot.register_next_step_handler(message, f2, bot, query)

def f2(message, bot, query):
    query += f"'{message.text.strip()}', "
    bot.send_message(message.chat.id, "Введите контакты")
    bot.register_next_step_handler(message, f3, bot, query)

def f3(message, bot, query):
    query += f"'{message.text.strip()}')"
    connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4t5')
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    bot.send_message(message.chat.id, "Done")

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
    if n.isalpha():
        if n == 'Да':
            bot.send_message(put.chat.id, 'Введите название винокурни')
            bot.register_next_step_handler(put, reply_to_user, bot)
        elif n == 'Нет':
            bot.send_message(put.chat.id, 'Хорошего дня')

    else:
        connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4t5')
        cursor = connection.cursor()
        cursor.execute(f"select place, contacts, imagelink from Distilleries where id = {n}")
        for place, contacts, imagelink in cursor.fetchall():
            answer = 'Адрес: ' + place + '     ' + 'Контакты: ' + contacts + '     ' + 'Фото: ' + imagelink
            bot.send_message(put.chat.id, answer)
        cursor.close()
        connection.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Да')
        item2 = types.KeyboardButton('Нет')
        markup.add(item1)
        markup.add(item2)
        bot.send_message(put.chat.id, 'Хотите ли добавить еще одну винокурнею Крыма?',  reply_markup=markup )


bot.polling(none_stop=True, interval=0)
