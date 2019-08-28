from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep
from time import time
from random import randint
from IPython.core.display import clear_output

request = 0
start_time = time()

owner_list = []
address_list = []
phone_list = []

for i in range(1, 70):
    url = "https://www.rent.com/california/oakland-apartments?page=" + str(i)
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    request += 1
    sleep(randint(1, 3))
    current_time = time()
    elapsed_time = current_time - start_time

    listings = soup.find_all("div", class_ = "_3PdAH _1EbNE")

    for list_ in listings:
        if list_ is not None:
            owner = list_.find("div", class_ = "_3RRl_ _2Hrxl").a
            address = list_.find("div", class_ = "_3RRl_ _2Hrxl").find("div", class_ = "T9KnS").div
            if list_.find("div", class_ = "wy0Jz _1fGq_") is not None:
                phone = list_.find("div", class_ = "wy0Jz _1fGq_").find("div", class_ = "_35UBu")
            else:
                phone = list_.find("div", class_ = "wy0Jz _1fGq_")

            if phone is not None:
                owner_list.append(owner.text)
                address_list.append(address.text)
                phone_list.append(phone.text)
            else:
                owner_list.append(owner.text)
                address_list.append(address.text)
                phone_list.append("")
                #ind_listing = pd.DataFrame({"Owner" : [owner.text], "Address" : [address.text], "Phone" : [phone.text]})
                #df.concat([ind_listing])

            #print(owner.text + ": " + address.text + ": ")
            #see how to replace NoneType with empty string ""
            #print(type(phone))
    print('Request: {}; Frequency: {} requests/s'.format(request, request/elapsed_time))
    clear_output(wait = True)

df = pd.DataFrame({"Owner": owner_list, "Address": address_list, "Phone:": phone_list})
elapsed_time = time() - start_time
print(elapsed_time)
df.to_csv("Rent_Data.csv")
