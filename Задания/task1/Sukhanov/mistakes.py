import psycopg2
import wget

from Задания.task1.Sukhanov import DZ_PARSBD

connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()
cr_qwery = '''create table Parser (id serial primary key, name varchar(100), price varchar(10), rate varchar(10), picture varchar(100))'''

try:
    cursor.execute(cr_qwery)
    connection.commit()
except psycopg2.errors.DuplicateTable:
    print("duplicate error")

for j in range(15):
    url = DZ_PARSBD.picture[j].find('img').attrs['src']
    tempf = f"img\\Parser{j}.jpg"
    wget.download(url, tempf)
    try:
        insert_query = f'''INSERT into public.Parser(name, price, rate, picture) values ('{DZ_PARSBD.name[j].text}', '{DZ_PARSBD.price[j].text}', '{DZ_PARSBD.rate[j].text}', '{tempf}') '''
        cursor.execute(insert_query)
        connection.commit()
    except:
        connection.rollback()

cursor.close()
connection.close()