import telebot
import psycopg2
import config
bot = telebot.TeleBot(config.bot_token)

def select(request):
    try:
        connection = psycopg2.connect(host=config.host, dbname=config.dbname, user=config.user,
                                      password=config.password)
        cursor = connection.cursor()
        cursor.execute(request)
        result = cursor.fetchall()
    except:
         result = "Ошибка"
    finally:
        cursor.close()
        connection.close()
        return result

max_id = int(select("select max(id) from laptops")[0][0])
min_id = int(select("select min(id) from laptops")[0][0])
bot = telebot.TeleBot(config.bot_token)
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, f'Привет. Введите идентификатор от {min_id} до {max_id}, чтобы получить данные: ')

@bot.message_handler(content_types=["text"])
def from_bd(message):
    try:
        current_id = int(message.text)
    except BaseException:
        bot.send_message(message.chat.id, "Вы неправильно ввели ID. Попробуйте снова:")
        return
    if current_id > max_id or current_id < min_id:
        bot.send_message(message.chat.id, "ID нет в базе данных. Попробуйте снова:")
        return
    else:
        try:
            data = select(f"select * from laptops where id = {current_id}")[0][1:]
            if type(data) == str:
                bot.send_message(message.chat.id, "Ошибка на сервере")
                return
            print(data)
            s = data[:-1]
            names_of_columns = ["Товар", "Цена", "Диагональ", "Разрешение", "Процессор", "Оперативная память",
                                "Графический контроллер", "Объём диска"]
            everydata = []
            for data_name, column_name in zip(s, names_of_columns):
                everydata.append(column_name.capitalize() + ": " + data_name)
            bot.send_message(message.chat.id, "\n\n".join(everydata))
            bot.send_photo(message.chat.id, open(data[-1], 'rb'))
        except:
            bot.send_message(message.chat.id, "Ошибка на сервере")
    bot.send_message(message.chat.id, f"Введите следующий ID от {min_id} до {max_id}:")
bot.polling(none_stop=True, interval=0)


