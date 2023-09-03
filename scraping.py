from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import time
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
driver_path = "C:/Users/harsh/Downloads/Project 127/msedgedriver.exe"

browser = webdriver.Edge()
browser.get(start_url)

stars_data = []


def scrape():

    soup = BeautifulSoup(browser.page_source , "html.parser")
    
    for tables in soup.find_all("table" , attrs={"class" : "wikitable sortable jquery-tablesorter"}) :
        table_body = tables.find("tbody")
        tr_tags = table_body.find_all("tr")

        for tr_tag in tr_tags :
            td_tags  = tr_tag.find_all("td")
            #print(td_tags)

            temp_list=[]

            for td_data in td_tags :
                #print(td_data.text)
                
                data = td_data.text.strip()
                #print(data)

                temp_list.append(data)
            
            stars_data.append(temp_list)
            #print(stars_data)
                
    final_data = []

    for i in range(0,len(stars_data)) :
        Star_names = stars_data[i][1]
        Distance = stars_data[i][3]
        Mass = stars_data[i][5]
        Radius = stars_data[i][6]
        Lum = stars_data[i][7]

        required_data = [Star_names , Distance , Mass , Radius , Lum]
        final_data.append(required_data)

    return final_data
    
final_data = scrape()

headers = ["Star name " , "Distance " , "Mass" , "Radius" , "Luminosity"]

stars_data_df = pd.DataFrame(final_data , columns=headers)

stars_data_df.to_csv("scapped_data.csv" , index = True , index_label = "id")