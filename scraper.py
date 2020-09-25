import requests
from bs4 import BeautifulSoup

url = 'https://drift-city-remastered.fandom.com/wiki/Speed_Parts'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

part_table = soup.find('table', class_ = 'article-table')

list = []

class currPart:
    def __init__(self,currPartName,currPartType,currPartLevel):
        self.currPartName = currPartName
        self.currPartType = currPartType
        self.currPartLevel = currPartLevel


for team in part_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        Part = row.find_all('td')
        index = 0
        for partData in Part:
            print(str(index))
            if(index == 0):
                curr = partData.text
                print(curr.strip())


            if(index == 5):
                index = 0
            else:
                index += 1
                
            

            
