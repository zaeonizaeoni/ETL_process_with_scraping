import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import sqlite3


url = 'https://worldpopulationreview.com/country-rankings/tea-consumption-by-country'
db_name = 'Countries_consumption'
table_name = 'tea_consumption_by_countries'
db_connection = sqlite3.connect(db_name)

def extract():
    pass

def transform():
    pass

def load_to_csv():
    pass

def load_to_database():
    pass

def log_progress():
    pass
