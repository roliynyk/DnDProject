import tkinter as tk
from tkinter import *
from tkinter import OptionMenu
import random

class NewCharGui(tk.Tk):

    def __init__(self, data, character):
        self.data = data
        self.character = character
        self.newCharCanvas()

    #Race selection drop down
    def raceSelection(self, C):
        race = []
        for i in self.races:
            race.append(i['name'])

        tk.Label(C, text="Select Your Race").place(relx=0.02, rely=0.01)
        self.raceVar = tk.StringVar(C)
        self.raceVar.set(race[0])
        raceMenu = tk.OptionMenu(C, self.raceVar, race[0], *race[1:], command = self.infoBoxPop)
        raceMenu.pack()
        raceMenu.place(relx=0.01, rely=0.03, width=130, height=30)

    # Class selection drop down button
    def classSelection(self, C):
        classSelection = []
        for i in self.classes:
            classSelection.append(i['name'])

        tk.Label(C, text="Choose a Class").place(relx=0.02, rely=0.08)
        self.classVar = tk.StringVar(C)
        self.classVar.set(classSelection[0])
        classMenu = OptionMenu(C, self.classVar, classSelection[0], *classSelection[1:], command = self.infoBoxPop)
        classMenu.pack()
        classMenu.place(relx=0.01, rely=0.1, width=130, height=30)

    def charName(self, C):
        tk.Label(C, text="Character Name").place(relx=0.72, rely=0.03)
        self.characterName = tk.Text(C)
        self.characterName.pack()
        self.characterName.place(relx=0.72, rely=0.06, width=120, height=22)

    def createChar(self, C):
        create = tk.Button(C, text ="Create Character", command = lambda: self.getSelectionInfo())
        create.place(relx=0.68, rely=0.22, width=150, height=45)

    def alignmentSelection(self, C):
        tk.Label(C, text="Select Your Alignment").place(relx=0.015, rely=0.15)
        self.alignmentVar = StringVar(C)
        self.alignmentVar.set(self.alignments[0])  # default choice
        alignmentMenu = OptionMenu(C, self.alignmentVar, *self.alignments)
        alignmentMenu.place(relx=0.01, rely=0.17, width=130, height=30)

    # Specify the level of the character
    def levelSelection(self, C):
        # Might need to make this accept xp or 1-20 value for level
        tk.Label(C, text="Enter Level").place(relx=0.75, rely=0.09)
        self.levelText = tk.Text(C)
        self.levelText.pack()
        self.levelText.place(relx=0.75, rely=0.11, width=60, height=22)

    def spellSelection(self, C):
        spells = []
        count = 0

        #taking top 20 results for spells since OptionMenu is not scrollable
        for i in self.spells[0]['results']:
            if count == 20:
                break
            else:
                spells.append(i['name'])
            count += 1

        tk.Label(C, text="Select Spells").place(relx=0.2, rely=0.15)
        self.spellsVar = tk.StringVar(C)
        self.spellsVar.set(spells[0])

        #Unable to make OptionMenu scrollable, need an alternative function
        spellsMenu = tk.OptionMenu(C, self.spellsVar, spells[0], *spells[1:], command=self.infoBoxPop)
        spellsMenu.pack()
        spellsMenu.place(relx=0.2, rely=0.17, width=130, height=30)

    def equipmentSelection(self, C):
        equipment = []
        count = 0

        #taking top 20 results for equipment since OptionMenu is not scrollable
        for i in self.equipment[0]['results']:
            if count == 20:
                break
            else:
                equipment.append(i['name'])
            count += 1
        print(equipment)

        tk.Label(C, text="Select Equipment").place(relx=0.2, rely=0.22)
        self.equipVar = tk.StringVar(C)
        self.equipVar.set(equipment[0])

        # Unable to make OptionMenu scrollable, need an alternative function
        equipMenu = tk.OptionMenu(C, self.equipVar, equipment[0], *equipment[1:], command=self.infoBoxPop)
        equipMenu.pack()
        equipMenu.place(relx=0.2, rely=0.24, width=130, height=30)

    # Sets the Characters HP stats
    def hitPoints(self, C):
        # determined by hit die and some other stuff, need to research
        hp = tk.Button(C, text="Roll for HP", command = self.diceRollHp)
        hp.pack()
        hp.place(relx=0.7, rely=0.15, width=130, height=30)

    def strengthMod(self, C):
        tk.Label(C, text="STR").place(relx=0.45, rely=0.06)
        self.str = tk.Text(C)
        self.str.pack()
        self.str.place(relx=0.45, rely=0.081, width=60, height=22)

    def dexterityMod(self, C):
        tk.Label(C, text="DEX").place(relx=0.45, rely=0.108)
        self.dex = tk.Text(C)
        self.dex.pack()
        self.dex.place(relx=0.45, rely=0.1285, width=60, height=22)

    def constitutionMod(self, C):
        tk.Label(C, text="CON").place(relx=0.45, rely=0.15)
        self.con = tk.Text(C)
        self.con.pack()
        self.con.place(relx=0.45, rely=0.175, width=60, height=22)

    def intelligenceMod(self, C):
        tk.Label(C, text="INT").place(relx=0.55, rely=0.108)
        self.int = tk.Text(C)
        self.int.pack()
        self.int.place(relx=0.55, rely=0.1285, width=60, height=22)

    def wisdomMod(self, C):
        tk.Label(C, text="WIS").place(relx=0.55, rely=0.06)
        self.wis = tk.Text(C)
        self.wis.pack()
        self.wis.place(relx=0.55, rely=0.081, width=60, height=22)

    def charismaMod(self, C):
        tk.Label(C, text="CHA").place(relx=0.55, rely=0.155)
        self.cha = tk.Text(C)
        self.cha.pack()
        self.cha.place(relx=0.55, rely=0.175, width=60, height=22)

    def rollStatMod(self, C):
        tk.Label(C, text="Roll for stats, type the\n result into the modifiers").place(relx=0.45, rely=0.018)
        hp = tk.Button(C, text="Roll for Stats", command = self.diceRollStats)
        hp.pack()
        hp.place(relx=0.45, rely=0.21, width=130, height=30)

    def diceRollStats(self):
        rollList = []

        for i in range(4):
            rollList.append(random.randint(1, 6))
        rollList.sort(reverse=True)
        del rollList[3]
        total = sum(rollList)
        self.infoBoxPop(total)

    def diceRollHp(self):
        try:
            level = int(self.levelText.get('1.0', END).strip())
            hitDie = int(self.hitDice)
            hp = 0
            for i in range(1, level+1):
                print(i)
                if i == 1:
                    hp += hitDie
                else:
                    hp += random.randint(1, hitDie)
            self.total_health = hp
            self.hp_str = "Your Health is: " + str(hp)
            self.infoBoxPop(self.hp_str)

        except ValueError:
            self.infoBoxPop("Enter level and select a character class to roll Hp")

    # User writes data for background of their character
    def characterBackground(self, C):
        tk.Label(C, text="Character's Background").place(relx=0.01, rely=0.28)
        self.background = tk.Text(C)
        self.background.pack()
        self.background.place(relx=0.01, rely=0.308, width=790, height=180)

    # allows selection of abilities based on class
    def selectAbilities(self, C):
        abilities = tk.Button(C, text="Select Abilities")
        abilities.pack()
        abilities.place(relx=0.2, rely=0.17, width=130, height=30)

    def subraceSelection(self, C):
        subrace = []
        for i in self.races[self.raceDic[self.raceVar.get()]]['subraces']:
            subrace.append(i['name'])

        self.subraceVar = StringVar(C)
        self.subraceVar.set(subrace[0])

        self.subraceDropMenu = OptionMenu(C, self.subraceVar, *subrace)
        self.subraceDropMenu.place(relx=0.2, rely=0.03, width=130, height=30)

    # Need to make an additional button to add multiple proficiencies, currently only adds one.
    def proficincySelection(self, C):
        proficiencies = []

        print(self.classes[self.classDic[self.classVar.get()]])
        for i in self.classes[self.classDic[self.classVar.get()]]['proficiency_choices'][0]['from']:
            proficiencies.append(i['name'].strip('Skill: '))

        self.proficVar = StringVar(C)
        self.proficVar.set(proficiencies[0])

        self.proficDropMenu = OptionMenu(C, self.proficVar, *proficiencies)
        self.proficDropMenu.place(relx=0.2, rely=0.1, width=130, height=30)

    # creates the info box when things are selected in the gui
    def infoBox(self, C):
        self.listBox = Listbox(C)
        self.listBox.pack()
        self.listBox.place(relx=0.01, rely=0.62, width=790, height=250)

    # populates the info box with data
    def infoBoxPop(self, var):

        self.listBox.delete(0, 'end')
        if isinstance(var, str):
            if "Your Health is:" in var:
                self.listBox.insert(END, var)

            elif "Enter level" in var:
                self.listBox.insert(END, var)

            elif var in self.raceDic:
                self.updateSubraces(var)
                info = self.writeRaceData(var)
                [self.listBox.insert(END, i) for i in info]

            elif var in self.classDic:
                self.updateProficincies(var)
                info = self.writeClassData(var)
                [self.listBox.insert(END, i) for i in info]

        elif isinstance(var, int):
            self.listBox.insert(END, "Type in " + str(var)+ " for one of the modifiers.")

    # creates a dropdown for proficiencies
    def updateProficincies(self, var):

        proficDicList = self.classes[self.classDic[var]]['proficiency_choices'][0]['from']

        self.proficVar.set(proficDicList[0]['name'].strip("Skill: "))

        self.proficDropMenu['menu'].delete(0, 'end')
        for i in proficDicList:
            self.proficDropMenu['menu'].add_command(label=i['name'].strip("Skill: "), command=tk._setit(self.proficVar, i['name'].strip("Skill: ")))

    #updates the subrace dropdown
    def updateSubraces(self, var):

        subraceDicList = self.races[self.raceDic[var]]['subraces']
        if len(subraceDicList) > 0:
            self.subraceVar.set(subraceDicList[0]['name'])
        else:
            self.subraceVar.set('')
        self.subraceDropMenu['menu'].delete(0, 'end')
        for i in subraceDicList:
            self.subraceDropMenu['menu'].add_command(label=i['name'], command=tk._setit(self.subraceVar, i['name']))

    # Populates the info box with selected Class Data
    def writeClassData(self, val):

        self.hitDice = str(self.classes[self.classDic[val]]['hit_die'])
        savingThrows = "Saving Throws: "

        for i in self.classes[self.classDic[val]]['saving_throws']:
            if i != self.classes[self.classDic[val]]['saving_throws'][-1]:
                savingThrows += i['name'] +', '
            else:
                savingThrows += i['name']

        classInfo = ["Class: " + val, "Hit Die: D" + self.hitDice,
                     savingThrows]

        return classInfo

    # Populates information about the race in the GUI
    def writeRaceData(self, val):

        # basic stats that don't require too much formatting
        speed = self.races[self.raceDic[val]]['speed']
        bonuses = self.races[self.raceDic[val]]['ability_bonuses']

        # descriptions that need better formatting, currently using list comprehension
        size = list([self.races[self.raceDic[val]]['size_description'][i:i + 120] for i in
                     range(0, len(self.races[self.raceDic[val]]['size_description']), 120)])
        age = list([self.races[self.raceDic[val]]['age'][i:i + 120] for i in
                    range(0, len(self.races[self.raceDic[val]]['age']), 120)])
        alignment = list([self.races[self.raceDic[val]]['alignment'][i:i + 120] for i in
                          range(0, len(self.races[self.raceDic[val]]['alignment']), 120)])

        info = ["Race: " + val, "Speed: " + str(speed), "Bonuses: " + str(bonuses)]
        age[0] = "Age: " + age[0]
        alignment[0] = "Alignment: " + alignment[0]
        size[0] = "Size: " + size[0]

        info.extend(age)
        info.extend(size)
        info.extend(alignment)

        return info

    # calls all other buttons and things in the gui
    def newCharCanvas(self):
        self.newCharacterWindow = tk.Tk()
        self.newCharacterWindow.title("New Character Window")
        C = tk.Canvas(self.newCharacterWindow, bg=None, height=800, width=800)
        C.pack()

        self.raceDic = self.data.raceNameDict
        self.classDic = self.data.classNameDict
        self.races = self.data.races
        self.classes = self.data.classes
        self.alignments = self.data.alignments
        self.spells = self.data.spellsDict
        self.equipment = self.data.equipmentDict

        self.raceSelection(C)
        self.classSelection(C)
        self.createChar(C)
        self.alignmentSelection(C)
        self.levelSelection(C)
        self.charName(C)
        self.hitPoints(C)
        self.characterBackground(C)
        self.selectAbilities(C)
        self.constitutionMod(C)
        self.dexterityMod(C)
        self.strengthMod(C)
        self.wisdomMod(C)
        self.intelligenceMod(C)
        self.charismaMod(C)
        self.rollStatMod(C)
        self.infoBox(C)
        self.subraceSelection(C)
        self.proficincySelection(C)
        self.spellSelection(C)
        self.equipmentSelection(C)
        self.newCharacterWindow.mainloop()

    def getSelectionInfo(self):

        # Example on how to get new selection info, can be used to index into character info dict from api
        print("Selections: " + self.raceVar.get())
        print("Class: " + self.classVar.get())
        print("Alignment: " + self.alignmentVar.get())
        print("Level: " + self.levelText.get('1.0',END))

        self.character.updateAll(self.characterName.get('1.0',END), self.classVar.get(), self.raceVar.get(), self.background.get('1.0',END), 
            self.alignmentVar.get(), int(self.levelText.get('1.0',END)), self.total_health, 6, self.proficVar.get(), 
            {"Str":int(self.str.get('1.0',END)), "Dex":int(self.dex.get('1.0',END)), "Con":int(self.con.get('1.0',END)), 
            "Int":int(self.int.get('1.0',END)), "Wis":int(self.wis.get('1.0',END)), "Cha":int(self.cha.get('1.0',END))})
        self.newCharacterWindow.destroy()