import psycopg2
from psycopg2 import sql
import requests
from bs4 import BeautifulSoup
from IPython.core.display import clear_output

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
    # connects to database, scrapes data, and inserts into database
    def scrape(self):
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
                owner = listing.find("div", class_ = "_3F9rC")
                number = listing.find("div", class_ = "_2fCP2")
                if listing.find("div", class_ = "_2fCP2") is not None:
                    self.apartment = owner.text
                    self.phone = number.text
                else: 
                    self.apartment = owner.text
                    self.phone = ""
            cur.execute(sql.SQL("insert into {} values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)").format(sql.Identifier('ApartmentLeads')),[self.address, self.apartment, self.unit, self.squareFoot, self.bed, self.bath, self.rent, self.phone, self.latitude, self.longitude, self.amenities, self.picture])
        # commit changes and close connection
        conn.commit()
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
        sql = "CREATE TABLE \"ApartmentLeads\"(address TEXT, apartment TEXT, unit TEXT, \"squareFoot\" INTEGER, bed INTEGER, bath INTEGER, rent INTEGER, phone TEXT, latitude FLOAT, longitude FLOAT, amenities TEXT, picture TEXT)"
        cur.execute(sql)
        conn.commit()
        conn.close()

p1 = ApartmentUnit("", "", "", 0, 0, 0, 0, "", 0, 0, "", "")
p1.scrape()
# Here, create a new function encapsulating the above two lines. Create a new object every loop