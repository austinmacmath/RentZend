#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 00:03:45 2019

@author: austinmac
"""

import psycopg2
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
import os

#establish connection to database
#uncomment the below
conn = psycopg2.connect(
        host = os.getenv('HOST'), 
        database = "rentzend", 
        user = "austin", 
        password = os.getenv('PASSWORD')",
        port=2345
        )
#creates dataframe directly from table RentZendLeads from database

#uncomment the below
#database = pd.read_sql('SELECT * FROM "RentZendLeads"', conn)

#creates series of zip codes 
cities = database["city"]
#property_type = database["propertyType"]

#creates plot for every zip code in zips series
#need to do a unique graph, can't have duplicates, DONE
#graphs for cities instead of zip codes bc multiple zip codes for each city, DONE
def make_plots():
    for city in cities:
        plt.figure()
    #    print(cities[cities["city"] == city].index[0])
        zip_string = str(city)
    
#        print(int(database[database["city"] == zip_string].index[0]))
        
        data = database[database["city"] == zip_string]
        avg_rent_1 = data["rent"][data["bedrooms"] == 1].mean()
        avg_rent_2 = data["rent"][data["bedrooms"] == 2].mean()
        avg_rent_3 = data["rent"][data["bedrooms"] == 3].mean()
        avg_rent_4 = data["rent"][data["bedrooms"] == 4].mean()
        df = pd.DataFrame([["1 Bed", avg_rent_1], ["2 Bed", avg_rent_2], ["3 Bed", avg_rent_3], ["4 Bed", avg_rent_4]], columns = ["Bedrooms", "Rent"])
        sns.barplot(data = df, x = "Bedrooms", y = "Rent")
        plt.title("City: " + str(city))

#creates unique plots and saves them into working directory
def no_duplicates():
    for i in range(0, cities.size):
        for j in range(i + 1, cities.size):
            if j == cities.size - 1:
                data = database[database["city"] == cities[i]]
                avg_rent_1 = data["rent"][data["bedrooms"] == 1].mean()
                avg_rent_2 = data["rent"][data["bedrooms"] == 2].mean()
                avg_rent_3 = data["rent"][data["bedrooms"] == 3].mean()
                avg_rent_4 = data["rent"][data["bedrooms"] == 4].mean()
                df = pd.DataFrame([["1 Bed", avg_rent_1], ["2 Bed", avg_rent_2], ["3 Bed", avg_rent_3], ["4 Bed", avg_rent_4]], columns = ["Bedrooms", "Rent"])
                
                plt.figure()
                sns.barplot(data = df, x = "Bedrooms", y = "Rent")
                plt.title("City: " + cities[i])
                #careful, saves plots into WD
                #plt.savefig("" + cities[i] + "_graph.png")
            if cities[i] == cities[j]:
                break
            
def city_plot(city_name, property_type):
    data = database[(database["city"] == city_name) & (database["propertyType"] == property_type)]
    avg_rent_1 = data["rent"][data["bedrooms"] == 1].median()
    avg_rent_2 = data["rent"][data["bedrooms"] == 2].median()
    avg_rent_3 = data["rent"][data["bedrooms"] == 3].median()
    avg_rent_4 = data["rent"][data["bedrooms"] == 4].median()
    df = pd.DataFrame([["1 Bed", avg_rent_1], ["2 Bed", avg_rent_2], ["3 Bed", avg_rent_3], ["4 Bed", avg_rent_4]], columns = ["Bedrooms", "Rent"])
                
    plt.figure()
    sns.set_palette(sns.color_palette("bright"))
    sns.barplot(data = df, x = "Bedrooms", y = "Rent", zorder = 3)
    #plt.title(city_name + ": " + property_type)
    plt.axis("off")
    #plt.grid(zorder = 0)

    print(data.size)
    plt.savefig("" + city_name + "_" + property_type + "_graph.png")
    

#make_plots()
#close connection
#no_duplicates()
    
#Townhouse
#Single Family
#MANUFACTURED
#Condo
#APARTMENT
#TOWNHOUSE
#HOME_TYPE_UNKNOWN
#SINGLE_FAMILY
#LOT
#MULTI_FAMILY
#CONDO
    
city_plot("Sacramento", "TOWNHOUSE")

conn.close()
