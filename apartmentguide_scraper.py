from random import randint
from time import sleep, time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from IPython.core.display import clear_output

request = 0
start_time = time()

owners = []
numbers = []

for i in range(1, 81):
    url = "https://www.apartmentguide.com/apartments/California/Oakland/?page=" + str(i)
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    listings = soup.find_all("div", class_ = "_2HiBK")

    request += 1
    sleep(randint(1, 3))
    current_time = time()
    elapsed_time = current_time - start_time
    
    for listing in listings:
        if listings is not None:
            owner = listing.find("div", class_ = "_3F9rC")
            number = listing.find("div", class_ = "_2fCP2")
            if listing.find("div", class_ = "_2fCP2") is not None:
                owners.append(owner.text)
                numbers.append(number.text)
            else: 
                owners.append(owner.text)
                numbers.append("empty")

    print('Request: {}; Frequency: {} requests/s'.format(request, request/elapsed_time))
    clear_output(wait = True)
    
df = pd.DataFrame({"Owners": owners, "Numbers" : numbers})
df.to_csv("apartmentguide.csv")
