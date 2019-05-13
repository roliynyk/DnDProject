class Character():
    #Init character class
    #Add any new stats here in the same format as the others and add them to the updateAll() function as well
    #Then anywhere that that function is called will have to be updated to include the new values
    def __init__(self, name, class_type, race, background, alignment, experience, health, armor, profficiency, stats):
        self.name = name
        self.class_type = class_type
        self.race = race
        self.background = background
        self.alignment = alignment
        self.health = health
        self.armor = armor
        self.profficiency = profficiency
        self.experience = experience
        self.stats = stats  #Dictionary of all the stats

    #Print stat
    def returnStat(self, key):
        return self.stats[key]

    #Print all stats
    def returnStats(self):
        return self.stats
    #Returns all stats in a dictionary for the purpose of more easily storing data in json
    def returnAll(self):
        stat_dict = {}
        stat_dict.update({"name": self.name})
        stat_dict.update({"class_type": self.class_type})
        stat_dict.update({"race": self.race})
        stat_dict.update({"background": self.background})
        stat_dict.update({"alignment": self.alignment})
        stat_dict.update({"experience": self.experience})
        stat_dict.update({"health": self.health})
        stat_dict.update({"armor": self.armor})
        stat_dict.update({"profficiency": self.profficiency})
        stat_dict.update({"stats": self.stats})
        return stat_dict

    #Updates Experience
    def updateExperience(self, experience):
        self.experience = experience

    #Updates Helth
    def updateHealth(self, health):
        self.health = health

    #Updates Armor
    def updateArmor(self, armor):
        self.armor = armor

    #Updates Profficiency
    def updateProfficiency(self, profficiency):
        self.profficiency = profficiency

    #Updates Stats
    def updateStats(self, stats):
        self.stats = stats

    #Update stat
    def updateStat(self, key, value):
        self.stats[key] = value

    #Updates health armor and experience
    def updateHealthEtc(self, health, armor, experience):
        self.health = health
        self.armor = armor
        self.experience = experience

    #Updates All
    def updateAll(self, name, class_type, race, background, alignment, experience, health, armor, profficiency, stats):
        self.name = name
        self.class_type = class_type
        self.race = race
        self.background = background
        self.alignment = alignment
        self.health = health
        self.armor = armor
        self.profficiency = profficiency
        self.experience = experience
        self.stats = stats  #Dictionary of all the stats