import psycopg2
import wget
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import config
i = 1
s = Service("С:\DATA\ChromeDriver\chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.get("https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118/f/tolko-v-nalichii=da?from=under_search")
time.sleep(5)
"""
height = browser.execute_script("return document.body.scrollHeight")
time.sleep(4)
for i in range(10):
    browser.execute_script(f"window.scrollTo(0, {1000*i})")
    time.sleep(1)
"""
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
productst = soup.find_all('a', class_="product-title__text")
pricest = soup.find_all('span', class_="price__main-value")
features = soup.find_all('span', class_="product-feature-list__value")
pictures =  soup.find_all('div', class_="product-picture-container")
connection=psycopg2.connect(host=config.host, dbname=config.dbname, user=config.user, password=config.password)
cursor = connection.cursor()
insert = """CREATE TABLE public.laptops(
id serial primary key,
Product varchar(100),
Price varchar(15),
Diagonal varchar(5),
Resolution varchar(20),
CPU varchar(50),
RAM varchar(15),
Graphics_Controller varchar(40),
Volume varchar(25),
src varchar(200)
);
"""
cursor.execute(insert)
connection.commit()
for i in range(len(productst)):
    url = "https://"+pictures[i].find('img')['src']
    filename = f"C:/Users/Andrew/OneDrive/Desktop/Temp/c22712/Задания/task1/Lahin/DjangoProga/polls/static/img/laptops/{i+1}.jpg"
    u = []
    for j in range(10):
        u.append(features[10*i+j].text)
    wget.download(url, filename)
    t = pricest[i].text.replace("\xa0", " ")
    try:
        insert = f"""INSERT INTO public.laptops(
            Product, Price, Diagonal, Resolution, CPU, RAM, Graphics_Controller, Volume, src)
            VALUES
            ('{productst[i].text.strip()}', '{t.strip()}', '{u[0][:u[0].find("/")]}', '{u[0][u[0].find("/")+1:]}', 
            '{u[2]}', '{u[4]+" "+u[5]}', '{u[6]}', '{u[8]}', '{filename}');"""
        cursor.execute(insert)
        connection.commit()
    except:
        connection.rollback()

cursor.close()
connection.close()