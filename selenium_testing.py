import requests
import psycopg2
from bs4 import BeautifulSoup
from selenium import webdriver
from IPython.core.display import clear_output
from random import randint
from time import sleep, time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
#options.add_argument('--headless')
driver = webdriver.Chrome("/Users/austinmac/Downloads/chromedriver", chrome_options=options)

urls = []

url = "https://www.apartmentguide.com/apartments/California/Oakland/?page=1"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
conn = psycopg2.connect(
                host = "138.68.224.211", 
                database = "rentzend", 
                user = "austin", 
                password = "eLKNd293ngfl!Sflkj",
                port=2345
                )


listings = soup.find_all("div", class_ = "_2HiBK")
for listing in listings:
    if listings is not None:
        href = listing.find("div", class_ = "WUEp2").find("a")["href"]
        url2 = "https://apartmentguide.com" + href
        html2 = requests.get(url2).text
        soup2 = BeautifulSoup(html2, "html.parser")

        urls.append(url2)
        print(url2)
        sleep(randint(1,3))

