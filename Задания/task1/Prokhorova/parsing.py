import psycopg2
import wget
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')

cursor = connection.cursor()

create_table = """ create table food 
    (id serial primary key, name varchar(200), price varchar(100), gram varchar(100), stock varchar(100))"""

cursor.execute(create_table)
connection.commit()

driver = Service('C:\\Users\\Honor\\Desktop\\учеба\\прога\\скачали хроме\chromedriver.exe')
browser = webdriver.Chrome(service=driver)
browser.get('https://vkusvill.ru/goods/gotovaya-eda/')
html_code = browser.page_source
soup = BeautifulSoup(html_code, 'lxml')

name = soup.find_all('a', class_="ProductCard__link rtext _desktop-md _mobile-sm gray900 js-datalayer-catalog-list-name")
price = soup.find_all('span', class_="Price Price--md Price--label Price--gray")
gram = soup.find_all('div', class_="ProductCard__weight rtext _desktop-sm gray500 nobr")
stock = soup.find_all('div', class_="Rating__text subtitle _desktop-sm gray900")


for i in range(15):


    ins_qwery = f"""insert into public.food(name, price, gram, stock) values ('{name[i].text}', '{price[i].text}', '{gram[i].text}', '{stock[i].text}')"""
    cursor.execute(ins_qwery)
    connection.commit()




cursor.close()

connection.close()