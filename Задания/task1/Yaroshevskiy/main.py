from bs4 import BeautifulSoup
from selenium import webdriver
from wget import download
import psycopg2 as psyc


brow = webdriver.Chrome()
url = "https://ikey.ru/"
brow.get(url)

html = brow.page_source

soup = BeautifulSoup(html, "lxml")

products = soup.find_all(attrs={"class": "product"})

with psyc.connect(dbname="db_for_parse", user="perfecto") as conn:
    with conn.cursor() as cursor:
        for i, product in enumerate(products):
            img_tag = product.find(attrs={"class": "imagef"}).find("img")
            title = img_tag.attrs.get("alt")
            image = url + img_tag.attrs.get("src")
            price = product.find(attrs={"class": "product-price"}).text
            desc = product.find(attrs={"class": "product-desc"}).text
            download(url + img_tag.attrs.get("src"), f"images/{i}.jpg")

            cursor.execute(f"""insert into images(link, name, price, description, file)
                               values ('{image}', '{title}', '{price}', '{desc}', 'images/{i}.jpg')""")
        conn.commit()
