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
                    speedPartlist[len(speedPartlist) - 1].currPartImage = thumbnailClass['data-src']
                else:
                    speedPartlist[len(speedPartlist) - 1].currPartImage = thumbnailClass['src']
                
                index = 0
            
            index += 1
                
            


#############################################################
# Scrape **Speed Option Parts** Data from the DCR wiki page #
#############################################################
            
speedOptionPartsUrl = 'https://drift-city-remastered.fandom.com/wiki/Speed_Option_Parts'

speedOptionReq = requests.get(speedOptionPartsUrl)
speedOptionSoup = BeautifulSoup(speedOptionReq.text, 'html.parser')

speedOption_table = speedOptionSoup.find('table', class_ = 'article-table')

speedOptionlist = []


class currSpeedOptionPart:
    def __init__(self,currPartName,currPartType,currPartLevel,currPartPrice,currPartBase,currPartImage):
        self.currPartName = currPartName
        self.currPartType = currPartType
        self.currPartLevel = currPartLevel
        self.currPartPrice = currPartPrice
        self.currPartBase = currPartBase
        self.currPartImage = currPartImage


for speedOptionItem in speedOption_table.find_all('tbody'):
    rows = speedOptionItem.find_all('tr')
    for row in rows:
        speedOptionPart = row.find_all('td')
        index = 0
        newSpeedOptionPart = currSpeedOptionPart('partName','partType','partLevel','partPrice','partBase','partImage')
        speedOptionlist.append(newSpeedOptionPart)
        
        for partData in speedOptionPart:
            if(index == 0):
                thisPartName = partData.text
                speedOptionlist[len(speedOptionlist) - 1].currPartName = thisPartName
            elif(index == 1):
                thisPartType = partData.text
                speedOptionlist[len(speedOptionlist) - 1].currPartType = thisPartType

            elif(index == 2):
                thisPartLevel = partData.text
                speedOptionlist[len(speedOptionlist) - 1].currPartLevel = thisPartLevel

            elif(index == 3):
                thisPartPrice = partData.text
                speedOptionlist[len(speedOptionlist) - 1].currPartPrice = thisPartPrice

            elif(index == 4):
                thisPartBase = partData.text
                speedOptionlist[len(speedOptionlist) - 1].currPartBase = thisPartBase    

            elif(index == 5):
                thumbnailClass = partData.find('img')
                if thumbnailClass.has_attr('data-src'):
                    speedOptionlist[len(speedOptionlist) - 1].currPartImage = thumbnailClass['data-src']
                else:
                    speedOptionlist[len(speedOptionlist) - 1].currPartImage = thumbnailClass['src']
                
                index = 0
            
            index += 1




##########################################################
# Scrape **Accel Parts** Data from the DCR wiki page     #
##########################################################

accelPartsUrl = 'https://drift-city-remastered.fandom.com/wiki/Acceleration_Parts'

aPreq = requests.get(accelPartsUrl)
aPreqSoup = BeautifulSoup(aPreq.text, 'html.parser')

accelPart_table = aPreqSoup.find('table', class_ = 'article-table')

accelPartlist = []

class currAccelPart:
    def __init__(self,currPartName,currPartType,currPartLevel,currPartPrice,currPartBase,currPartImage):
        self.currPartName = currPartName
        self.currPartType = currPartType
        self.currPartLevel = currPartLevel
        self.currPartPrice = currPartPrice
        self.currPartBase = currPartBase
        self.currPartImage = currPartImage



for FullPart in accelPart_table.find_all('tbody'):
    rows = FullPart.find_all('tr')
    for row in rows:
        Part = row.find_all('td')
        index = 0
        newPart = currAccelPart('partName','partType','partLevel','partPrice','partBase','partImage')
        accelPartlist.append(newPart)
        
        for partData in Part:
            if(index == 0):
                thisPartName = partData.text
                accelPartlist[len(accelPartlist) - 1].currPartName = thisPartName

            elif(index == 1):
                thisPartType = partData.text
                accelPartlist[len(accelPartlist) - 1].currPartType = thisPartType

            elif(index == 2):
                thisPartLevel = partData.text
                accelPartlist[len(accelPartlist) - 1].currPartLevel = thisPartLevel

            elif(index == 3):
                thisPartPrice = partData.text
                accelPartlist[len(accelPartlist) - 1].currPartPrice = thisPartPrice

            elif(index == 4):
                thisPartBase = partData.text
                accelPartlist[len(accelPartlist) - 1].currPartBase = thisPartBase    
 
            elif(index == 5):
                thumbnailClass = partData.find('img')
                if thumbnailClass.has_attr('data-src'):
                    accelPartlist[len(accelPartlist) - 1].currPartImage = thumbnailClass['data-src']

                else:
                    accelPartlist[len(accelPartlist) - 1].currPartImage = thumbnailClass['src']

                
                index = 0
            
            index += 1
                
            


#############################################################
# Scrape **Accel Option Parts** Data from the DCR wiki page #
#############################################################
            
accelOptionPartsUrl = 'https://drift-city-remastered.fandom.com/wiki/Acceleration_Option_Parts'

accelOptionReq = requests.get(accelOptionPartsUrl)
accelOptionSoup = BeautifulSoup(accelOptionReq.text, 'html.parser')

accelOption_table = accelOptionSoup.find('table', class_ = 'article-table')

accelOptionlist = []


class currAccelOptionPart:
    def __init__(self,currPartName,currPartType,currPartLevel,currPartPrice,currPartBase,currPartImage):
        self.currPartName = currPartName
        self.currPartType = currPartType
        self.currPartLevel = currPartLevel
        self.currPartPrice = currPartPrice
        self.currPartBase = currPartBase
        self.currPartImage = currPartImage


for accelOptionItem in accelOption_table.find_all('tbody'):
    rows = accelOptionItem.find_all('tr')
    for row in rows:
        accelOptionPart = row.find_all('td')
        index = 0
        newAccelOptionPart = currAccelOptionPart('partName','partType','partLevel','partPrice','partBase','partImage')
        accelOptionlist.append(newAccelOptionPart)
        
        for partData in accelOptionPart:
            if(index == 0):
                thisPartName = partData.text
                accelOptionlist[len(accelOptionlist) - 1].currPartName = thisPartName

            elif(index == 1):
                thisPartType = partData.text
                accelOptionlist[len(accelOptionlist) - 1].currPartType = thisPartType

            elif(index == 2):
                thisPartLevel = partData.text
                accelOptionlist[len(accelOptionlist) - 1].currPartLevel = thisPartLevel

            elif(index == 3):
                thisPartPrice = partData.text
                accelOptionlist[len(accelOptionlist) - 1].currPartPrice = thisPartPrice

            elif(index == 4):
                thisPartBase = partData.text
                accelOptionlist[len(accelOptionlist) - 1].currPartBase = thisPartBase    

            elif(index == 5):
                thumbnailClass = partData.find('img')
                if thumbnailClass.has_attr('data-src'):
                    accelOptionlist[len(accelOptionlist) - 1].currPartImage = thumbnailClass['data-src']

                else:
                    accelOptionlist[len(accelOptionlist) - 1].currPartImage = thumbnailClass['src']

                
                index = 0
            
            index += 1




##########################################################
# Scrape **Dura Parts** Data from the DCR wiki page     #
##########################################################

duraPartsUrl = 'https://drift-city-remastered.fandom.com/wiki/Durability_Parts'

dPreq = requests.get(duraPartsUrl)
dPreqSoup = BeautifulSoup(dPreq.text, 'html.parser')

duraPart_table = dPreqSoup.find('table', class_ = 'article-table')

duraPartlist = []

class currDuraPart:
    def __init__(self,currPartName,currPartType,currPartLevel,currPartPrice,currPartBase,currPartImage):
        self.currPartName = currPartName
        self.currPartType = currPartType
        self.currPartLevel = currPartLevel
        self.currPartPrice = currPartPrice
        self.currPartBase = currPartBase
        self.currPartImage = currPartImage



for FullPart in duraPart_table.find_all('tbody'):
    rows = FullPart.find_all('tr')
    for row in rows:
        Part = row.find_all('td')
        index = 0
        newPart = currDuraPart('partName','partType','partLevel','partPrice','partBase','partImage')
        duraPartlist.append(newPart)
        
        for partData in Part:
            if(index == 0):
                thisPartName = partData.text
                duraPartlist[len(duraPartlist) - 1].currPartName = thisPartName

            elif(index == 1):
                thisPartType = partData.text
                duraPartlist[len(duraPartlist) - 1].currPartType = thisPartType

            elif(index == 2):
                thisPartLevel = partData.text
                duraPartlist[len(duraPartlist) - 1].currPartLevel = thisPartLevel

            elif(index == 3):
                thisPartPrice = partData.text
                duraPartlist[len(duraPartlist) - 1].currPartPrice = thisPartPrice

            elif(index == 4):
                thisPartBase = partData.text
                duraPartlist[len(duraPartlist) - 1].currPartBase = thisPartBase    

            elif(index == 5):
                thumbnailClass = partData.find('img')
                if thumbnailClass.has_attr('data-src'):
                    duraPartlist[len(duraPartlist) - 1].currPartImage = thumbnailClass['data-src']

                else:
                    duraPartlist[len(duraPartlist) - 1].currPartImage = thumbnailClass['src']

                
                index = 0
            
            index += 1
                
            


#############################################################
# Scrape **Dura Option Parts** Data from the DCR wiki page  #
#############################################################
            
duraOptionPartsUrl = 'https://drift-city-remastered.fandom.com/wiki/Durability_Option_Parts'

duraOptionReq = requests.get(duraOptionPartsUrl)
duraOptionSoup = BeautifulSoup(duraOptionReq.text, 'html.parser')

duraOption_table = duraOptionSoup.find('table', class_ = 'article-table')

duraOptionlist = []


class currDuraOptionPart:
    def __init__(self,currPartName,currPartType,currPartLevel,currPartPrice,currPartBase,currPartImage):
        self.currPartName = currPartName
        self.currPartType = currPartType
        self.currPartLevel = currPartLevel
        self.currPartPrice = currPartPrice
        self.currPartBase = currPartBase
        self.currPartImage = currPartImage


for duraOptionItem in duraOption_table.find_all('tbody'):
    rows = duraOptionItem.find_all('tr')
    for row in rows:
        duraOptionPart = row.find_all('td')
        index = 0
        newDuraOptionPart = currDuraOptionPart('partName','partType','partLevel','partPrice','partBase','partImage')
        duraOptionlist.append(newDuraOptionPart)
        
        for partData in duraOptionPart:
            if(index == 0):
                thisPartName = partData.text
                duraOptionlist[len(duraOptionlist) - 1].currPartName = thisPartName
 
            elif(index == 1):
                thisPartType = partData.text
                duraOptionlist[len(duraOptionlist) - 1].currPartType = thisPartType
 
            elif(index == 2):
                thisPartLevel = partData.text
                duraOptionlist[len(duraOptionlist) - 1].currPartLevel = thisPartLevel

            elif(index == 3):
                thisPartPrice = partData.text
                duraOptionlist[len(duraOptionlist) - 1].currPartPrice = thisPartPrice

            elif(index == 4):
                thisPartBase = partData.text
                duraOptionlist[len(duraOptionlist) - 1].currPartBase = thisPartBase    

            elif(index == 5):
                thumbnailClass = partData.find('img')
                if thumbnailClass.has_attr('data-src'):
                    duraOptionlist[len(duraOptionlist) - 1].currPartImage = thumbnailClass['data-src']

                else:
                    duraOptionlist[len(duraOptionlist) - 1].currPartImage = thumbnailClass['src']

                
                index = 0
            
            index += 1




##########################################################
# Scrape **Boost Parts** Data from the DCR wiki page     #
##########################################################

boostPartsUrl = 'https://drift-city-remastered.fandom.com/wiki/Booster_Parts'

bPreq = requests.get(boostPartsUrl)
bPreqSoup = BeautifulSoup(bPreq.text, 'html.parser')

boostPart_table = bPreqSoup.find('table', class_ = 'article-table')

boostPartlist = []

class currBoostPart:
    def __init__(self,currPartName,currPartType,currPartLevel,currPartPrice,currPartBase,currPartImage):
        self.currPartName = currPartName
        self.currPartType = currPartType
        self.currPartLevel = currPartLevel
        self.currPartPrice = currPartPrice
        self.currPartBase = currPartBase
        self.currPartImage = currPartImage



for FullPart in boostPart_table.find_all('tbody'):
    rows = FullPart.find_all('tr')
    for row in rows:
        Part = row.find_all('td')
        index = 0
        newPart = currBoostPart('partName','partType','partLevel','partPrice','partBase','partImage')
        boostPartlist.append(newPart)
        
        for partData in Part:
            if(index == 0):
                thisPartName = partData.text
                boostPartlist[len(boostPartlist) - 1].currPartName = thisPartName

            elif(index == 1):
                thisPartType = partData.text
                boostPartlist[len(boostPartlist) - 1].currPartType = thisPartType

            elif(index == 2):
                thisPartLevel = partData.text
                boostPartlist[len(boostPartlist) - 1].currPartLevel = thisPartLevel

            elif(index == 3):
                thisPartPrice = partData.text
                boostPartlist[len(boostPartlist) - 1].currPartPrice = thisPartPrice

            elif(index == 4):
                thisPartBase = partData.text
                boostPartlist[len(boostPartlist) - 1].currPartBase = thisPartBase    

            elif(index == 5):
                thumbnailClass = partData.find('img')
                if thumbnailClass.has_attr('data-src'):
                    boostPartlist[len(boostPartlist) - 1].currPartImage = thumbnailClass['data-src']

                else:
                    boostPartlist[len(boostPartlist) - 1].currPartImage = thumbnailClass['src']

                
                index = 0
            
            index += 1
                
            


#############################################################
# Scrape **Boost Option Parts** Data from the DCR wiki page #
#############################################################
            
boostOptionPartsUrl = 'https://drift-city-remastered.fandom.com/wiki/Booster_Option_Parts'

boostOptionReq = requests.get(boostOptionPartsUrl)
boostOptionSoup = BeautifulSoup(boostOptionReq.text, 'html.parser')

boostOption_table = boostOptionSoup.find('table', class_ = 'article-table')

boostOptionlist = []


class currBoostOptionPart:
    def __init__(self,currPartName,currPartType,currPartLevel,currPartPrice,currPartBase,currPartImage):
        self.currPartName = currPartName
        self.currPartType = currPartType
        self.currPartLevel = currPartLevel
        self.currPartPrice = currPartPrice
        self.currPartBase = currPartBase
        self.currPartImage = currPartImage


for boostOptionItem in boostOption_table.find_all('tbody'):
    rows = boostOptionItem.find_all('tr')
    for row in rows:
        boostOptionPart = row.find_all('td')
        index = 0
        newBoostOptionPart = currBoostOptionPart('partName','partType','partLevel','partPrice','partBase','partImage')
        boostOptionlist.append(newBoostOptionPart)
        
        for partData in boostOptionPart:
            if(index == 0):
                thisPartName = partData.text
                boostOptionlist[len(boostOptionlist) - 1].currPartName = thisPartName

            elif(index == 1):
                thisPartType = partData.text
                boostOptionlist[len(boostOptionlist) - 1].currPartType = thisPartType
  
            elif(index == 2):
                thisPartLevel = partData.text
                boostOptionlist[len(boostOptionlist) - 1].currPartLevel = thisPartLevel

            elif(index == 3):
                thisPartPrice = partData.text
                boostOptionlist[len(boostOptionlist) - 1].currPartPrice = thisPartPrice

            elif(index == 4):
                thisPartBase = partData.text
                boostOptionlist[len(boostOptionlist) - 1].currPartBase = thisPartBase    

            elif(index == 5):
                thumbnailClass = partData.find('img')
                if thumbnailClass.has_attr('data-src'):
                    boostOptionlist[len(boostOptionlist) - 1].currPartImage = thumbnailClass['data-src']

                else:
                    boostOptionlist[len(boostOptionlist) - 1].currPartImage = thumbnailClass['src']

                
                index = 0
            
            index += 1

import dictConverter
dictConverter.buildSpeedPartsDictionary()