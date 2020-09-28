import json

dict_speedPartsList = {}

def buildSpeedPartsDictionary():
    import partScraper as ps
    for x in range(len(ps.speedPartlist)):
        Part = {
            "name" : ps.speedPartlist[x].currPartName,
            "type" : ps.speedPartlist[x].currPartType,
            "level" : ps.speedPartlist[x].currPartLevel,
            "price" : ps.speedPartlist[x].currPartPrice,
            "base" : ps.speedPartlist[x].currPartBase,
            "image" : ps.speedPartlist[x].currPartImage,
        }

        dict_speedPartsList[ps.speedPartlist[x].currPartName] = Part
    
    print(dict_speedPartsList)

    with open("docs/parts/speedParts.json", 'w') as fp:
        json.dump(dict_speedPartsList,fp)



dict_accelPartsList = {}

def buildAccelPartsDictionary():
    import partScraper as ps
    for x in range(len(ps.accelPartlist)):
        Part = {
            "name" : ps.accelPartlist[x].currPartName,
            "type" : ps.accelPartlist[x].currPartType,
            "level" : ps.accelPartlist[x].currPartLevel,
            "price" : ps.accelPartlist[x].currPartPrice,
            "base" : ps.accelPartlist[x].currPartBase,
            "image" : ps.accelPartlist[x].currPartImage,
        }

        dict_accelPartsList[ps.accelPartlist[x].currPartName] = Part
    
    print(dict_accelPartsList)


dict_duraPartsList = {}

def buildDuraPartsDictionary():
    import partScraper as ps
    for x in range(len(ps.duraPartlist)):
        Part = {
            "name" : ps.duraPartlist[x].currPartName,
            "type" : ps.duraPartlist[x].currPartType,
            "level" : ps.duraPartlist[x].currPartLevel,
            "price" : ps.duraPartlist[x].currPartPrice,
            "base" : ps.duraPartlist[x].currPartBase,
            "image" : ps.duraPartlist[x].currPartImage,
        }

        dict_duraPartsList[ps.duraPartlist[x].currPartName] = Part
    
    print(dict_duraPartsList)


dict_boostPartsList = {}

def buildBoostPartsDictionary():
    import partScraper as ps
    for x in range(len(ps.boostPartlist)):
        Part = {
            "name" : ps.boostPartlist[x].currPartName,
            "type" : ps.boostPartlist[x].currPartType,
            "level" : ps.boostPartlist[x].currPartLevel,
            "price" : ps.boostPartlist[x].currPartPrice,
            "base" : ps.boostPartlist[x].currPartBase,
            "image" : ps.boostPartlist[x].currPartImage,
        }

        dict_boostPartsList[ps.boostPartlist[x].currPartName] = Part
    
    print(dict_boostPartsList)


