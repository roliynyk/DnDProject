class Character():
    #Init character class
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
    #Test for correct assigning of values
    def printName(self):
        print(self.name)
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
    #Updates All
    def updateAll(self, name, class_type, race, background, alignment, experience, health, armor, stats):
        self.name = name
        self.class_type = class_type
        self.race = race
        self.background = background
        self.alignment = alignment
        self.health = health
        self.armor = armor
        self.experience = experience
        self.stats = stats  #Dictionary of all the stats