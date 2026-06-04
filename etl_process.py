import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import sqlite3


url = 'https://worldpopulationreview.com/country-rankings/tea-consumption-by-country'
db_name = 'Countries_consumption'
table_name = 'tea_consumption_by_countries'
db_connection = sqlite3.connect(db_name)
df = pd.DataFrame(columns=['Country', 'Annual total tea consumption 2022 (TON)'])

def extract(url, df):
    html_page = requests.get(url).text
    table = BeautifulSoup(html_page, 'html.parser')
    data = table.find_all('tbody')
    rows = data[0].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            content = {
                'Country': col[1].span.a.contents[0],
                'tea_consumption_by_countries': col[2].contents[0]
            }
            df1 = pd.DataFrame(content, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
    return df

def transform():
    pass

def load_to_csv():
    pass

def load_to_database():
    pass

def log_progress():
    pass

extract(url, df)