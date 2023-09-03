from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

import requests
import pandas as pd

page = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs"

url = requests.get(page)

page_content = url.content

soup = BeautifulSoup( page_content , 'html.parser')
#print(soup.prettify())


tables = soup.find_all('table' , {"class" : "wikitable sortable jquery-tablesorter"})
#

td = []

table_rows = tables[0].find_all('tr')

for tr in table_rows :
    td_tags = tr.find_all('td')
    row = [i.text.rstrip() for i in td_tags]
    td.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]

td_len = len(td)

final_data = []

for i in range(1,td_len) :
    Star_names.append(td[i][0])
    Distance.append(td[i][5])
    Mass.append(td[i][7])
    Radius.append(td[i][8])

    required_data = [Star_names , Distance , Mass , Radius]
    final_data.append(required_data)

headers = ['Star_name' , 'Distance' , 'Mass' , 'Radius']
data_df = pd.DataFrame(final_data, headers)

data_df.to_csv("scapped_data_2.csv" , index = True , index_label = "id")