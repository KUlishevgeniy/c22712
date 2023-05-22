from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import psycopg2
import wget

browser = webdriver.Chrome(service=Service('C:\\Users\\Yekaterina\\Downloads\\chromedriver_win32.zip\\chromedriver.exe'))
browser.get('https://msk.sushi-market.com/menu/rolly')
soup = BeautifulSoup(browser.page_source, "lxml")

Name = soup.find_all(attrs={"class": "goodsBlockName device-show"})
Info = soup.find_all(attrs={"class": "goodsBlockWeight"})
Des = soup.find_all(attrs={"class": "cardsList_text"})
Price = soup.find_all(attrs={"class": "product__price updated"})
Image = soup.find_all(attrs={"class": "cardsList_img add-to-cart__img"})

connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()
create_q = '''CREATE TABLE F0ood (ID serial primary key, Name varchar(5000), Info varchar(5000), Des varchar(10000), Price varchar(600), src varchar(1000))'''
cursor.execute(create_q)
connection.commit()

for j in range(25):
    url = Image[j].find('img').attrs['src']
    tempf = f"img\\food{j}.jpg"
    wget.download(url, tempf)
    insert_query = f'''INSERT into public.F0ood(Name, Info, Des, Price, src) values ('{Name[j].text}','{Info[j].text}','{Des[j].text}', '{Price[j].text}', '{tempf}') '''
    cursor.execute(insert_query)
connection.commit()

cursor.execute("SELECT * from F0ood")
print(cursor.fetchall())

cursor.close()
connection.close()
