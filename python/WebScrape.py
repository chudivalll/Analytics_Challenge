#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:23:25 2020

@author: mac
"""
from urllib.request import urlopen as uReq

import pandas
import pyodbc
from bs4 import BeautifulSoup as soup
from selenium import webdriver

# Dataset
server = "localhost"
database = "Scholastic"
username = "AIS_challenge"
password = "ScholasticChallenge"
cnxn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
    + server
    + ";DATABASE="
    + database
    + ";UID="
    + username
    + ";PWD="
    + password
)
cursor = cnxn.cursor()

df = pandas.read_sql_query(
    """
SELECT*FROM ZipcodeStats
""",
    cnxn,
)

df2 = pandas.Series([])
i = 0
for i in range(len(df)):
    # The website
    my_url = "http://www.mapszipcode.com/florida/miami/" + str(df.iloc[i, 0]) + "/"

    # opens up a connection, grabbing the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")

    # Output
    containers = page_soup.findAll("div", {"class": "dat"})[0].text
    df2[i] = containers
    i = i + 1

df.insert(6, "Population", df2)
# %%
df.to_csv("ZipcodeStatistics.csv", index=False)
