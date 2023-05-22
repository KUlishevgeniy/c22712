import psycopg2
import wget
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')

cursor = connection.cursor()

cr_qwery = """ create table Parser 
    (id serial primary key, name varchar(100), price varchar(10), rate varchar(10), picture varchar(100))"""

#cursor.execute(cr_qwery)
connection.commit()

driver = Service('D:\GOGdriver\chromedriver.exe')
browser = webdriver.Chrome(service=driver)
browser.get('https://www.perekrestok.ru/cat/promo/10')
html_code = browser.page_source
soup = BeautifulSoup(html_code, 'lxml')

name = soup.find_all('div', class_="product-card__title")
price = soup.find_all('div', class_="price-new")
rate = soup.find_all('div', class_="rating-value")
picture = soup.find_all('div', class_="product-card__image-wrapper")

for i in range(15):
    url = picture[i].find('img').attrs['src']
    filename = f"C:\\Users\\71332\PycharmProjects\pythonProject1\\venv\Pictures\{i}.jpg"
    wget.download(url, filename)
    ins_qwery = f"""insert into public.Parser(name, price, rate, picture) values ('{name[i].text}', '{price[i].text}', '{rate[i].text}', '{filename}')"""
    cursor.execute(ins_qwery)
    connection.commit()




cursor.close()

connection.close()