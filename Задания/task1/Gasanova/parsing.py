# парсер к полусему 8 неделя 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from wget import download
import psycopg2 as psyc

# s = Service("chromedriver") на Ubuntu можно не указывать путь до драйвера если что :)
URL = "https://proskateshop.ru/skejtbordy/?utm_source=yandex&utm_medium=cpc&utm_campaign=cn%7Cskeyty_gz-1%7Ccid%7C51517250%7Csearch&utm_content=gid%7C4180310153%7Caid%7C8980588780%7C20506942844_20506942844%7Cmain&utm_term=%D0%9F%D0%B5%D0%BD%D0%BD%D0%B8%20%D0%B1%D0%BE%D1%80%D0%B4%20%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C&etext=2202.N39xvihj0F0Od_d4etv_6nh36sdlRP-T26wHLuCJfjo_JZtVI5O7HY5f8FOJnzuLZXB6eWZoZnp2dG1laHBlcA.aceac50a24e4832d82874cd59ca1f9a315d9b351&_openstat=ZGlyZWN0LnlhbmRleC5ydTs1MTUxNzI1MDs4OTgwNTg4NzgwO3lhbmRleC5ydTpndWFyYW50ZWU&yclid=1445113833197462400"
brow = webdriver.Chrome()
brow.get(URL)

html = brow.page_source

soup = BeautifulSoup(html, "lxml") 

penny = soup.find_all(attrs={"class": "product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-6"})

with psyc.connect(host = "localhost", dbname="work", user="dialuna", password = "Timka07") as conn:
    with conn.cursor() as cursor:
        for i, product in enumerate(penny[1:]):
            image_link = product.find("img").attrs.get("src")
            image_name = product.find("img").attrs.get("alt")
            price = product.find("p", attrs={"class": "price"}).text.strip()
            download( product.find("img").attrs.get("src"), f"images/{i}.jpg")

            cursor.execute(f"""insert into bot(link, name, price, file)
                               values ('{image_link}', '{image_name}', '{price}', 'images/{i}.jpg')""")
        
        conn.commit()
