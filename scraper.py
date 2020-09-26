import requests
from bs4 import BeautifulSoup

##########################################################
# Scrape **Speed Parts** Data from the DCR wiki page     #
##########################################################

speedPartsUrl = 'https://drift-city-remastered.fandom.com/wiki/Speed_Parts'

sPreq = requests.get(speedPartsUrl)
sPreqSoup = BeautifulSoup(sPreq.text, 'html.parser')

speedPart_table = sPreqSoup.find('table', class_ = 'article-table')

speedPartlist = []

class currSpeedPart:
    def __init__(self,currPartName,currPartType,currPartLevel,currPartPrice,currPartBase,currPartImage):
        self.currPartName = currPartName
        self.currPartType = currPartType
        self.currPartLevel = currPartLevel
        self.currPartPrice = currPartPrice
        self.currPartBase = currPartBase
        self.currPartImage = currPartImage



for FullPart in speedPart_table.find_all('tbody'):
    rows = FullPart.find_all('tr')
    for row in rows:
        Part = row.find_all('td')
        index = 0
        newPart = currSpeedPart('partName','partType','partLevel','partPrice','partBase','partImage')
        speedPartlist.append(newPart)
        
        for partData in Part:
            if(index == 0):
                thisPartName = partData.text
                speedPartlist[len(speedPartlist) - 1].currPartName = thisPartName
            elif(index == 1):
                thisPartType = partData.text
                speedPartlist[len(speedPartlist) - 1].currPartType = thisPartType
            elif(index == 2):
                thisPartLevel = partData.text
                speedPartlist[len(speedPartlist) - 1].currPartLevel = thisPartLevel
            elif(index == 3):
                thisPartPrice = partData.text
                speedPartlist[len(speedPartlist) - 1].currPartPrice = thisPartPrice
            elif(index == 4):
                thisPartBase = partData.text
                speedPartlist[len(speedPartlist) - 1].currPartBase = thisPartBase    
            elif(index == 5):
                thumbnailClass = partData.find('img')
                if thumbnailClass.has_attr('data-src'):
                    currPartImage = thumbnailClass['data-src']
                else:
                    currPartImage = thumbnailClass['src']
                
                index = 0
            
            index += 1
                
            


##########################################################
# Scrape **Speed Option Parts** Data from the DCR wiki page     #
##########################################################
            
speedOptionPartsUrl = 'https://drift-city-remastered.fandom.com/wiki/Speed_Option_Parts'

speedOptionReq = requests.get(speedOptionPartsUrl)
speedOptionSoup = BeautifulSoup(speedOptionReq.text, 'html.parser')

speedOption_table = speedOptionSoup.find('table', class_ = 'article-table')

speedOptionlist = []

for speedOptionItem in speedOption_table.find_all('tbody'):
    rows = speedOptionItem.find_all('tr')
    for row in rows:
        speedOptionPart = row.find_all('td')
        print(speedOptionPart)