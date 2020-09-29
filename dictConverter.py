import json

dict_speedPartsList = {}

def buildSpeedPartsDictionary():
    import partScraper as ps
    for x in range(len(ps.speedPartlist)):
        Part = {
            "name" : ps.speedPartlist[x].currPartName.strip(),
            "type" : ps.speedPartlist[x].currPartType.strip(),
            "level" : ps.speedPartlist[x].currPartLevel.strip(),
            "price" : ps.speedPartlist[x].currPartPrice.strip(),
            "base" : ps.speedPartlist[x].currPartBase.strip(),
            "image" : ps.speedPartlist[x].currPartImage.strip(),
        }

        dict_speedPartsList[ps.speedPartlist[x].currPartName.strip()] = Part
    
    print(dict_speedPartsList)

    with open("docs/parts/speedParts.json", 'w') as fp:
        json.dump(dict_speedPartsList,fp,indent = 2,separators=(',', ':'))
        



dict_accelPartsList = {}

def buildAccelPartsDictionary():
    import partScraper as ps
    for x in range(len(ps.accelPartlist)):
        Part = {
            "name" : ps.accelPartlist[x].currPartName.strip(),
            "type" : ps.accelPartlist[x].currPartType.strip(),
            "level" : ps.accelPartlist[x].currPartLevel.strip(),
            "price" : ps.accelPartlist[x].currPartPrice.strip(),
            "base" : ps.accelPartlist[x].currPartBase.strip(),
            "image" : ps.accelPartlist[x].currPartImage.strip(),
        }

        dict_accelPartsList[ps.accelPartlist[x].currPartName.strip()] = Part
    
    print(dict_accelPartsList)

    with open("docs/parts/accelParts.json", 'w') as fp:
        json.dump(dict_accelPartsList,fp,indent = 2,separators=(',', ':'))


dict_duraPartsList = {}

def buildDuraPartsDictionary():
    import partScraper as ps
    for x in range(len(ps.duraPartlist)):
        Part = {
            "name" : ps.duraPartlist[x].currPartName.strip(),
            "type" : ps.duraPartlist[x].currPartType.strip(),
            "level" : ps.duraPartlist[x].currPartLevel.strip(),
            "price" : ps.duraPartlist[x].currPartPrice.strip(),
            "base" : ps.duraPartlist[x].currPartBase.strip(),
            "image" : ps.duraPartlist[x].currPartImage.strip(),
        }

        dict_duraPartsList[ps.duraPartlist[x].currPartName.strip()] = Part
    
    print(dict_duraPartsList)

    with open("docs/parts/duraParts.json", 'w') as fp:
        json.dump(dict_duraPartsList,fp,indent = 2,separators=(',', ':'))


dict_boostPartsList = {}

def buildBoostPartsDictionary():
    import partScraper as ps
    for x in range(len(ps.boostPartlist)):
        Part = {
            "name" : ps.boostPartlist[x].currPartName.strip(),
            "type" : ps.boostPartlist[x].currPartType.strip(),
            "level" : ps.boostPartlist[x].currPartLevel.strip(),
            "price" : ps.boostPartlist[x].currPartPrice.strip(),
            "base" : ps.boostPartlist[x].currPartBase.strip(),
            "image" : ps.boostPartlist[x].currPartImage.strip(),
        }

        dict_boostPartsList[ps.boostPartlist[x].currPartName.strip()] = Part
    
    print(dict_boostPartsList)

    with open("docs/parts/boostParts.json", 'w') as fp:
        json.dump(dict_boostPartsList,fp,indent = 2,separators=(',', ':'))


