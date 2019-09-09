#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:50:45 2019

@author: austinmac
"""

import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

data = pd.DataFrame()

townhouses = ["Townhouses"] * 10
apartments = ["Apartments"] * 10
condos = ["Condos"] * 10
#condos = apartments.append(["condos"] * 10)
both = apartments + condos + townhouses
def line():
    plt.figure(dpi = 500)
    x = range(2009, 2019)
    y = range(2009, 2019)
    q = range(2009, 2019)
    z = list(x) + list(y) + list(q)
    data = pd.DataFrame({"Rent" : [2516, 2384, 2371, 2251, 2251, 2195, 2300, 2350, 2200, 2250] + 
                         [2216, 2484, 2571, 2351, 2351, 2395, 2100, 2150, 2100, 2650] +
                         [2345, 2234, 2134, 2654, 2567, 2121, 2245, 2345, 2743, 2045],
                         "Years" : z, 
                         "Property Type" : both})
    
    sns.lineplot(data = data, x = "Years", y = "Rent", hue = "Property Type", palette = sns.color_palette(["#1F5FCC", "#FF7B42", "#E02020"]))
    # insert into above palette = sns.color_palette("hls", 3)
    plt.grid(axis = "y")
    plt.title("Rent Trend by Year")
    plt.savefig("LandingPageLinePlot.png")
    print(data)

total = sum([589, 1500])

def pie():
    plt.pie([589, 1500], startangle = 130, explode=([.1, 0]), colors = sns.color_palette())
    plt.savefig("pie.png")

def time():
    df = pd.DataFrame({"Single Family Home" : [7], "Townhouse" : [9], "Condo": [4]})
    plt.figure()
    sns.barplot(data = df, palette = "Greens")
    plt.xlabel("Property Type")
    plt.ylabel("Days")
    plt.title("Days on Market by Property Type")
    plt.savefig("days_on_market.jpg", dpi = 500, transparent = True)

line()