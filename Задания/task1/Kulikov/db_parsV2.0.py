from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import wget
import psycopg2
import re
s = Service('C:\\Users\\Alex\\PycharmProjects\\pythonProject\\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://music.yandex.ru/chart')
time.sleep (1)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
Трек=soup.find_all('a', class_='d-track__title deco-link deco-link_stronger')
Длительность=soup.find_all('div', class_='d-track__info d-track__nohover')
Автор=soup.find_all('span', class_='d-track__artists')
Картинки=soup.find_all('img', class_='entity-cover__image deco-pane')
str_Картинки=[]
for i in range(len(Картинки)):
    str_Картинки.append(Картинки[i])
str_Картинки=str(str_Картинки)
str_Картинки=re.findall(r'src="(.*?)"',str_Картинки)
for i in range(len(str_Картинки)):
    str_Картинки[i]='https:'+str_Картинки[i]
#for i in range(len(str_cartinki)):
    #wget.download(str_cartinki[i], 'TOP'+str((i+1))+'.jpeg')


connection = psycopg2.connect(dbname = 'dbdata',
                           user='postgres', password='Q1w2e3r4',
                           host='localhost')
cursor=connection.cursor()
creat_table="""CREATE TABLE music
    (id serial primary key, "Трек" varchar(100),
    "Длительность" varchar(100),
    "Автор" varchar(100),
    "Картинки" varchar(100))"""
cursor.execute(creat_table)
connection.commit()
for Трек, Длительность, Автор, Картинки in zip(Трек, Автор, Длительность, Картинки):
    qwery=f"""INSERT INTO public.music(
	    Трек, Длительность, Автор, Картинки)
	    VALUES 
	    ('{Трек.text}','{Длительность.text}','{Автор.text}', '{Картинки.text}' )"""
    cursor.execute(qwery)
    connection.commit()
for i in range(1,len(str_Картинки)+1):
    puti = r'C:\papkta' + str(i) + '.jpeg'
    qwery=f"""UPDATE public.music
        SET Картинки='{puti}'
        WHERE id={i}"""
    cursor.execute(qwery)
    connection.commit()