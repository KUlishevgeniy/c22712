from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
s = Service('C:\\Users\\Yekaterina\\Downloads\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.citilink.ru/catalog/noutbuki/')
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')


name=soup.find_all('div', class_='app-catalog-1tp0ino e1an64qs0')
print (name[1].text)
description=soup.find_all('div', class_='app-catalog-1o4umte eevw8x70')
print (description[1].text)
