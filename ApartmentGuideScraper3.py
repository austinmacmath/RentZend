import psycopg2
from psycopg2 import sql
import requests
from bs4 import BeautifulSoup
from IPython.core.display import clear_output
from selenium import webdriver
from random import randint
from time import sleep, time

start_time = time()

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/Users/austinmac/Downloads/chromedriver", chrome_options=options)

class ApartmentUnit():
    # constructor for ApartmentUnit class
    def __init__(self, address, apartment, unit, squareFoot, bed, bath, rent, phone, latitude, longitude, amenities, picture):
        self.address = address
        self.apartment = apartment
        self.unit = unit
        self.squareFoot = squareFoot
        self.bed = bed
        self.bath = bath
        self.rent = rent
        self.phone = phone
        self.latitude = latitude
        self.longitude = longitude
        self.amenities = amenities
        self.picture = picture
        self.url = ""

    # connects to database, scrapes data, and inserts into database
    def scrape(self):
        request = 0
        # url and setup of parser
        url = "https://www.apartmentguide.com/apartments/California/Oakland/?page=1"
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        # connection
        conn = psycopg2.connect(
                host = "138.68.224.211", 
                database = "rentzend", 
                user = "austin", 
                password = "eLKNd293ngfl!Sflkj",
                port=2345
                )
        cur = conn.cursor()
        # looking for tags/attributes
        listings = soup.find_all("div", class_ = "_2HiBK")
        for listing in listings:
            if listings is not None:

                request += 1
                sleep(randint(1, 3))
                current_time = time()
                elapsed_time = current_time - start_time

                href = listing.find("div", class_ = "WUEp2").find("a")["href"]
                url2 = "https://apartmentguide.com" + href
                driver.get(url2)

                view_all_buttons = driver.find_elements_by_class_name("KNMds")
                for x in range(len(view_all_buttons)):
                    if view_all_buttons[x].is_displayed():
                        sleep(randint(1,3))
                        driver.execute_script("arguments[0].click();", view_all_buttons[x])
                page_source = driver.page_source
                soup2 = BeautifulSoup(page_source, "html.parser")

                units = soup2.find_all("div", class_ = "_1g3Lq")
                for unit in units:

                    def one_unit(unit, listing):
                        unit_num = unit.find("div", class_ = "yxu6C")
                        self.unit = unit_num.text
                        rent_price = unit.find("div", class_ = "iQyC8")
                        self.rent = rent_price.text
                        square_feet = rent_price.next_sibling
                        self.squareFoot = square_feet.text
                        #if unit.find("div", class_ = "_2z1jT") is not None:
                        street_address = soup2.find("div", class_ = "_2z1jT").find("span")
                        #city = street_address.next_sibling
                        #state = city.next_sibling
                        #zip_code = state.next_sibling
                        self.address = street_address.text
                        bed = unit.find("div", class_ = "ye4H3").find("span")
                        self.bed = bed.text
                        bath = unit.find("div", class_ = "")

                        owner = listing.find("div", class_ = "_3F9rC")
                        number = listing.find("div", class_ = "_2fCP2")
                        if listing.find("div", class_ = "_2fCP2") is not None:
                            self.apartment = owner.text
                            self.phone = number.text
                        else: 
                            self.apartment = owner.text
                            self.phone = ""

                    def reset():
                        self.address = ""
                        self.apartment = ""
                        self.unit = ""
                        self.squareFoot = ""
                        self.bed = ""
                        self.bath = ""
                        self.rent = ""
                        self.phone = ""
                        self.latitude = ""
                        self.longitude = ""
                        self.amenities = ""
                        self.picture = ""
                        self.url = ""                        

                    one_unit(unit, listing)
                    cur.execute(sql.SQL("insert into {} values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)").format(sql.Identifier('ApartmentLeads')),[self.address, self.apartment, self.unit, self.squareFoot, self.bed, self.bath, self.rent, self.phone, self.latitude, self.longitude, self.amenities, self.picture])
                    conn.commit()
                    reset()

            print('Request: {}; Frequency: {} requests/s'.format(request, request/elapsed_time))
            clear_output(wait = True)
        # close connection
        conn.close()

# creates a relation in the database
def create_relation():
        conn = psycopg2.connect(
                host = "138.68.224.211", 
                database = "rentzend", 
                user = "austin", 
                password = "eLKNd293ngfl!Sflkj",
                port=2345
                )
        cur = conn.cursor()
        sql = "CREATE TABLE \"ApartmentLeads\"(address TEXT, apartment TEXT, unit TEXT, \"squareFoot\" TEXT, bed TEXT, bath TEXT, rent TEXT, phone TEXT, latitude TEXT, longitude TEXT, amenities TEXT, picture TEXT)"
        cur.execute(sql)
        conn.commit()
        conn.close()

# creates an ApartmentUnit object
p1 = ApartmentUnit("", "", "", "", "", "", "", "", "", "", "", "")
p1.scrape()
# Here, create a new function encapsulating the above two lines. Create a new object every loop

#create_relation()