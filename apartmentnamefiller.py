#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:56:59 2019

@author: austinmac
"""

import pandas as pd
data = pd.read_csv("Apartment building prospect list - Sheet6 (1).csv")

address_list = data["Address Line 1"]

for i in range(0, len(data.index)):
    data.iloc[i, 1] = data.iloc[i, 2]
for i in range(0, address_list.size):
    for j in range(i + 1, address_list.size):
        if address_list[i] == address_list[j]:
            last_names = data["Company Name"][data["Address Line 1"] == address_list[j]]
            data["Last Name"][data["Address Line 1"] == address_list[i]] = str(last_names)