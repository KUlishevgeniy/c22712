#Небольшое предисловие: кнопки item1, item2 и item3 похожи по своему функционалу, однако между ними есть разница в реализации - item3 реализована через функцию, прописанную в доп.файле
import telebot
import psycopg2
from telebot import types
import random
from wwfuncs import select #импорт функции из другого файла

connection = psycopg2.connect(host='localhost', dbname='FHWDB', user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()

try:
    s_query = """SELECT * FROM public.parse"""
    cursor.execute(s_query)
except psycopg2.errors.UndefinedTable: #рассматриваем случай, когда таблицы нет
    connection.rollback() #возвращаемся "на действие назад"
    import FHWDB #создаём и заполняем таблицу, если её не существовало ранее
    connection = psycopg2.connect(host='localhost', dbname='FHWDB', user='postgres', password='Q1w2e3r4')
    cursor = connection.cursor()
    s_query = '''SELECT * FROM public.parse'''
    cursor.execute(s_query)
finally:
    arr = list(cursor.fetchall())

bot = telebot.TeleBot('5980905704:AAH2qIP4Gy60nhuKNAojOGpmI6zwNoJK1Iw')

min_id, max_id = 1, 60

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Хочу информацию о любых цветах, пожалуйста")
    item2 = types.KeyboardButton("Хочу картинку любых цветов, пожалуйста")
    item3 = types.KeyboardButton("Хочу информацию о предложении дня, пожалуйста")
    item4 = types.KeyboardButton("Общая информация о сведениях, находящихся в базе данных")
    item5 = types.KeyboardButton("Поиск конкретного предложения по ID")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)
    bot.send_message(m.chat.id,
                     '"Хочу информацию о любых цветах, пожалуйста" - для получения карточки цветов;\n "Хочу картинку любых цветов, пожалуйста" - для получения картинки цветов;\n "Хочу информацию о предложении дня, пожалуйста" - сводка о конкретных цветах;\n "Общая информация о сведениях, находящихся в базе данных" - сводка об характеристиках товаров, информация о которых находится в БД.\n "Поиск конкретного предложения по ID" - найдите инересующее вас предложение по ID',
                     reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if (message.text.strip() == "Хочу информацию о любых цветах, пожалуйста"):
        i = random.choice(arr)
        a1 = f'Название: {i[1]};\nЦена: {i[2]};\nСкидка(в процентах): {i[3]};\n'
        bot.send_message(message.chat.id, a1)
    elif (message.text.strip() == "Хочу картинку любых цветов, пожалуйста"):
        i = random.choice(arr)
        bot.send_photo(message.chat.id, open(i[4], 'rb'))
    elif (message.text.strip() == "Хочу информацию о предложении дня, пожалуйста"):
        j = random.randint(1, 61)
        i = list(select(j))
        a1 = f'Название: {i[1]};\nЦена: {i[2]};\nСкидка(в процентах): {i[3]};\n'
        bot.send_message(message.chat.id, "Предложение дня:\n")
        bot.send_message(message.chat.id, a1)
        bot.send_photo(message.chat.id, open(i[4], 'rb'))
    elif (message.text.strip() == "Поиск конкретного предложения по ID"):
        sent = bot.send_message(message.chat.id,
                         f'Введите идентификатор(ID, целое число) от {min_id} до {max_id}, чтобы получить информацию о конкретном предложении: ')
        bot.register_next_step_handler(sent, ret_id)
    else:
        bot.send_message(message.chat.id, "С помощью данного бота вы можете получить информацию о 60-и цветах одного из московских магазинов по их продаже, в частности их: название, цену, скидку(в процентах) и фото. Вы можете это осуществить, взаимодействуя с ботом. Попробуйте! ")

def ret_id(message):
    try:
        now_id = (message.text)
        now_id = int(float(now_id))
        z = list(select(now_id))
        a2 = f'Название: {z[1]};\nЦена: {z[2]};\nСкидка(в процентах): {z[3]};\n'
        bot.send_message(message.chat.id, a2)
        bot.send_photo(message.chat.id, open(z[4], 'rb'))
        bot.send_message(message.chat.id, "Для повторного поиска по ID воспользуйтесь соответствующей кнопкой в 'меню'")
    except ValueError:
        bot.send_message(message.chat.id,
                         "По такому ID нет данных. Попробуйте заново через 'меню' кнопок найти интересующее вас предложение")
    except TypeError:
        bot.send_message(message.chat.id,
                         "По такому ID нет данных. Попробуйте заново через 'меню' кнопок найти интересующее вас предложение")


bot.polling(none_stop=True, interval=0)

cursor.close()
connection.close()
