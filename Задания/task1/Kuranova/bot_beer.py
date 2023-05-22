import telebot
import random
from telebot import types
import psycopg2

bot = telebot.TeleBot('6279990552:AAHxC0hfpQcOrcGKHwvWT7AabQqdE3a5Tp8')

def request(a):
    info = []
    connection = psycopg2.connect(host='localhost', dbname='breweries', user='postgres', password='Q1w2e3r4t5')
    cursor = connection.cursor()
    cursor.execute(a)
    res = cursor.fetchall()
    for id, name, place, link in res:
        s = [id, name, place, link]
        info.append(s)
    cursor.close()
    connection.close()
    return info

quote = ['В вине есть мудрость, в пиве есть свобода, в воде есть бактерии.\n\nБенджамин Франклин',
         'Пиво — интеллектуальный напиток. Какая досада, что его пьет так много идиотов.\n\nРэй Брэдбери',
'Пьянство — особая форма самоубийства, позволяющая тебе оживать на следующий день. Я, кажется, уже прожил десять или '
'пятнадцать тысяч жизней.\n\nЧарльз Буковски',
'Я пью, чтобы окружающие меня люди становились интереснее.\n\nДжордж Жан Натан',
'— Уинстон, да вы пьяны!\n— Все верно. А вы уродина. Завтра утром я протрезвею. А вы так и останетесь уродиной.\n\nУинстон Черчилль',
'— Есть в мире вещи получше, чем алкоголь.\n— Да, сэр.  Но алкоголь компенсирует их отсутствие.\n\nТерри Пратчетт',
'Если вы заметите человека, который пытается утопить свои горести в стакане, сообщите ему, что горести умеют плавать.\n\nПиттакус Лор',
'Алкоголь, возможно, опаснейший враг человека, но в Библии сказано: возлюби врага своего.\n\nФрэнк Синатра',
'Меня как-то спросили, мучит ли меня похмелье. Нет, ведь для того, чтобы случилось похмелье, нужно перестать пить.\n\nЛемми Килмистер',
'У меня нет проблем с алкоголем. За исключением тех случаев, когда я не могу достать выпивку.\n\nТом Уэйтс',
'Будь осторожен с крепкими напитками. Они могут заставить тебя выстрелить в сборщика налогов… и промахнуться.\n\nРоберт Хайнлайн',
'Плохого виски не бывает. Просто некоторые сорта виски лучше других.\n\nУильям Фолкнер',
'Не всякий, кто пьет, является поэтом. Многие пьют как раз из-за того, что они не поэты.\n\nДадли Мур',
'Компьютер позволяет совершить больше ошибок быстрее, чем какое-либо изобретение в человеческой истории, за исключением, '
'возможно, револьвера и текилы.\n\nМитч Рэдклифф',
'Я не доверяю верблюдам, и вообще всем, кто может неделю не пить.\n\nДжо Луис',
'Алкоголик — это тип, который тебе не нравится и который пьет столько же, сколько ты.\n\nДилан Томас',
'За алкоголь! Причину и решение всех проблем.\n\nГомер Симпсон']

c = request('select id, name, place, imagelink from Information')
def share(message):
    a = message.text
    b = a.split(',')
    connection = psycopg2.connect(host='localhost', dbname='breweries', user='postgres', password='Q1w2e3r4t5')
    cursor = connection.cursor()
    p = """INSERT INTO Information(id,Name, Place, ImageLink) VALUES
    ( '"""+str(int(c[-1][0])+1)+"""', '"""+b[0]+"""', '"""+b[1]+"""', '"""+b[2]+"""');"""
    cursor.execute(p)
    connection.commit()
    cursor.close()
    connection.close()
    bot.send_message(message.chat.id, 'Вы сделали неоценимую услугу! Спасибо вам большое!')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Где выпить?")
    item2 = types.KeyboardButton("Знаешь еще места, где можно выпить? Поделись)")
    item3 = types.KeyboardButton("Хочешь выпить, но нет повода или тоста? Не переживай, мы и такое предусмотрели;)")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(m.chat.id, 'Если не хочешь заморачиваться, то просто нажми любую из предложенных кнопок\n'
                                f'А можешь ввести число от {c[0][0]} до {c[-1][0]}, мы тебе выведем номер самой '
                                f'лучшей пивоварни :)', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Где выпить?':
        choice = random.randint(1, len(c)-1)
        bot.send_message(message.chat.id, f'{c[choice]}')
    elif message.text.strip().isnumeric():
        try:
            bot.send_message(message.chat.id, f'{c[int(message.text) - 1]}')
        except:
            bot.send_message(message.chat.id, "Кажись, вы попали не в тот интервал. Попробуйте снова.")
    elif message.text.strip() == 'Знаешь еще места, где можно выпить? Поделись)':
        bot.send_message(message.chat.id, 'Пиши название, адрес, контакты через запятую!')
        bot.register_next_step_handler(message, share)
    elif message.text.strip() == 'Хочешь выпить, но нет повода или тоста? Не переживай, мы и такое предусмотрели;)':
        bot.send_message(message.chat.id, 'Лови!')
        choice1 = random.randint(1, len(quote)-1)
        bot.send_message(message.chat.id, quote[choice1])

bot.polling(none_stop=True, interval=0)