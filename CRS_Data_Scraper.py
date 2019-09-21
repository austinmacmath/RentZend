from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import sql
from time import sleep, time
from IPython.core.display import clear_output


class building():
    def __init__(self, propertyAddress, propertyCounty, units, totalSquareFeet, yearBuilt, extraFeatures, assessedLand2018, assessedImprovements2018, totalAssessment2018, assessedLand2017, assessedImprovements2017, totalAssessment2017, assessedLand2016, assessedImprovements2016, totalAssessment2016, ownerName, ownerMailingAddress, ownerOccupied):
        self.propertyAddress = propertyAddress
        self.propertyCounty = propertyCounty
        self.units = units
        self.totalSquareFeet = totalSquareFeet
        self.yearBuilt = yearBuilt
        self.extraFeatures = extraFeatures
        self.assessedLand2018 = assessedLand2018
        self.assessedLand2017 = assessedLand2017
        self.assessedLand2016 = assessedLand2016
        self.assessedImprovements2018 = assessedImprovements2018
        self.assessedImprovements2017 = assessedImprovements2017
        self.assessedImprovements2016 = assessedImprovements2016
        self.totalAssessment2018 = totalAssessment2018
        self.totalAssessment2017 = totalAssessment2017
        self.totalAssessment2016 = totalAssessment2016
        self.ownerName = ownerName
        self.ownerMailingAddress = ownerMailingAddress
        self.ownerOccupied = ownerOccupied

    def scrape(self, property_):
        #if property_.find("section", id = "Main_PropertyInfoMain_locationSection") is not None:
        self.propertyAddress = property_.find("section", id = "Main_PropertyInfoMain_locationSection").find("td").text
        self.propertyCounty = property_.find("section", id = "Main_PropertyInfoMain_locationSection").find_all("tr")[3].find("td").text
        self.units = property_.find("section", id = "buildingSection1").find_all("tr")[1].find_all("td")[2].text
        self.totalSquareFeet = property_.find("section", id = "buildingSection1").find_all("tr")[4].find("td").find("div").text
        self.yearBuilt = property_.find("section", id = "buildingSection1").find_all("tr")[2].find("td").text
        #self.extraFeatures = 
        self.assessedLand2018 = property_.find("table", id = "Main_PropertyInfoMain_TaxAssessmentHistoryTable").find_all("tr")[1].find_all("td")[0].text
        self.assessedLand2017 = property_.find("table", id = "Main_PropertyInfoMain_TaxAssessmentHistoryTable").find_all("tr")[1].find_all("td")[4].text
        self.assessedLand2016 = property_.find("table", id = "Main_PropertyInfoMain_TaxAssessmentHistoryTable").find_all("tr")[1].find_all("td")[8].text
        self.assessedImprovements2018 = property_.find("table", id = "Main_PropertyInfoMain_TaxAssessmentHistoryTable").find_all("tr")[2].find_all("td")[0].text
        self.assessedImprovements2017 = property_.find("table", id = "Main_PropertyInfoMain_TaxAssessmentHistoryTable").find_all("tr")[2].find_all("td")[4].text
        self.assessedImprovements2016 = property_.find("table", id = "Main_PropertyInfoMain_TaxAssessmentHistoryTable").find_all("tr")[2].find_all("td")[8].text
        self.totalAssessment2018 = property_.find("table", id = "Main_PropertyInfoMain_TaxAssessmentHistoryTable").find_all("tr")[3].find_all("td")[0].text
        self.totalAssessment2017 = property_.find("table", id = "Main_PropertyInfoMain_TaxAssessmentHistoryTable").find_all("tr")[3].find_all("td")[4].text
        self.totalAssessment2016 = property_.find("table", id = "Main_PropertyInfoMain_TaxAssessmentHistoryTable").find_all("tr")[3].find_all("td")[8].text
        self.ownerName = property_.find("section", id = "Main_PropertyInfoMain_currentOwnerSection").find("div").find("td").text
        self.ownerMailingAddress = property_.find("section", id = "Main_PropertyInfoMain_currentOwnerSection").find("div").find_all("tr")[1].find("td").text
        self.ownerOccupied = property_.find("section", id = "Main_PropertyInfoMain_currentOwnerSection").find("div").find_all("tr")[2].find("td").text
""" 
    def get_propertyAddress(self):
        return self.propertyAddress
 """
def create_relation():
    conn = psycopg2.connect(
            host = "138.68.224.211", 
            database = "rentzend", 
            user = "austin", 
            password = "eLKNd293ngfl!Sflkj",
            port=2345
            )
    cur = conn.cursor()
    sql = "CREATE TABLE \"CRSData\"(\"propertyAddress\" TEXT, \"propertyCounty\" TEXT, units TEXT, \"totalSquareFeet\" TEXT, \"yearBuilt\" TEXT, \"extraFeatures\" TEXT, \"assessedLand2018\" TEXT, \"assessedImprovements2018\" TEXT,  \"totalAssessment2018\" TEXT, \"assessedLand2017\" TEXT, \"assessedImprovements2017\" TEXT,  \"totalAssessment2017\" TEXT, \"assessedLand2016\" TEXT, \"assessedImprovements2016\" TEXT,  \"totalAssessment2016\" TEXT, \"ownerName\" TEXT, \"ownerMailingAddress\" TEXT, \"ownerOccupied\" TEXT)"
    cur.execute(sql)
    conn.commit()
    conn.close()

#create_relation()

def insert(build, relation):
    conn = psycopg2.connect(
            host = "138.68.224.211", 
            database = "rentzend", 
            user = "austin", 
            password = "eLKNd293ngfl!Sflkj",
            port=2345
            )
    cur = conn.cursor()
    cur.execute(sql.SQL("INSERT INTO {} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)").format(sql.Identifier(relation)),[build.propertyAddress,build.propertyCounty, build.units, build.totalSquareFeet, build.yearBuilt, build.extraFeatures, build.assessedLand2018, build.assessedImprovements2018, build.totalAssessment2018, build.assessedLand2017, build.assessedImprovements2017, build.totalAssessment2017, build.assessedLand2016, build.assessedImprovements2016, build.totalAssessment2016, build.ownerName, build.ownerMailingAddress, build.ownerOccupied])
    conn.commit()
    conn.close()

def main():
    start_time = time()
    request = 0
    for x in range(1, 1341):
        myfile = open(str(x) + "CRS-data.htm")
        html = myfile.read()
        soup = BeautifulSoup(html, "html.parser")

        apartmentBuilding = building("","","","","","","","","","","","","","","","","","")
        apartmentBuilding.scrape(soup)
        insert(apartmentBuilding, "CRSData")

        request += 1
        current_time = time()
        elapsed_time = current_time - start_time
        print("Import: {}; Frequency: {} imports/sec".format(request, request/elapsed_time))
        clear_output(wait = True)

if __name__ == "__main__":
    main()

print("hello from Module 1")