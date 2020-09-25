import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://drift-city-remastered.fandom.com/wiki/Speed_Parts'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

part_table = soup.find('table', class_ = 'article-table')

for team in part_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        partNames = row.find_all('td')
        #print(partNames)
        for part in partNames:
            partData = part.text
            print(partData.strip())
