import requests

url = 'http://www.dnd5eapi.co/api/'
r = requests.get(url)

#get character race
def getRaceData():

    raceDictionary = []

    for i in range(1,10):
        race = requests.get(url + 'races/{}'.format(i)).json()
        raceDictionary.append(race)

    return raceDictionary

#character classes
def getClassData():

    classDictionary = []

    for i in range(1,13):
        cclass = requests.get(url + 'classes/{}'.format(i)).json()
        classDictionary.append(cclass)

    return classDictionary

def getSkillsData():

    skillDictionary = []

    for i in range(1,19):
        skill = requests.get(url + 'skills/{}'.format(i)).json()
        skillDictionary.append(skill)

    return skillDictionary

def getSpellData():

    spellsDictionary = []

    for i in range(1, 320):
        spells = requests.get(url + 'spells/{}'.format(i)).json()
        spellsDictionary.append(spells)
    
    return spellsDictionary

def getEquipmentData():
    equipmentDictionary = []

    for i in range(1, 19):
        equipment = requests.get(url + 'equipment/'.format(i)).json()
        equipmentDictionary.append(equipment)

    return equipmentDictionary
# for i in getClassData():
#     print(i)
