import tkinter as tk
from tkinter import *
import LoadData

class NewCharGui(tk.Tk):

    def __init__(self, data):
        self.data = data
        self.newCharCanvas()

    def raceSelection(self, C):
        race = []
        for i in self.races:
            race.append(i['name'])

        tk.Label(C, text="Select Your Race").place(relx=0.02, rely=0.01)
        self.dropVar1 = tk.StringVar(C)
        self.dropVar1.set(race[0])
        dropMenu = tk.OptionMenu(C, self.dropVar1, race[0], *race[1:], command = self.infoBoxPop)
        dropMenu.pack()
        dropMenu.place(relx=0.01, rely=0.05, width=130, height=30)

    def classSelection(self, C):
        classSelection = []
        for i in self.classes:
            classSelection.append(i['name'])

        tk.Label(C, text="Choose a Class").place(relx=0.02, rely=0.14)
        self.classVar = tk.StringVar(C)
        self.classVar.set(classSelection[0])
        classMenu = OptionMenu(C, self.classVar, classSelection[0], *classSelection[1:], command = self.infoBoxPop)
        classMenu.pack()
        classMenu.place(relx=0.01, rely=0.18, width=130, height=30)

    # creates the info box when things are selected in the gui
    def infoBox(self, C):
        self.listBox = Listbox(C)
        self.listBox.pack()
        self.listBox.place(relx=0.01, rely=0.4, width=490, height=250)

    def infoBoxPop(self, var):
        self.listBox.delete(0, 'end')
        if isinstance(var, str):
            if var in self.raceDic:
                info = self.writeRaceData(var)
            elif var in self.classDic:
                info = self.writeClassData(var)
            for i in info:
                self.listBox.insert(END, i)

    def writeClassData(self, val):

        hitDice = str(self.classes[self.classDic[val]]['hit_die'])
        proficiencyChoice = "Proficiency Choices: "
        for i in self.classes[self.classDic[val]]['proficiency_choices']:
            print(i)
            #proficiencyChoice += i

        savingThrows = "Saving Throws: "
        for i in self.classes[self.classDic[val]]['saving_throws']:
            if i != self.classes[self.classDic[val]]['saving_throws'][-1]:
                savingThrows += i['name'] +', '
            else:
                savingThrows += i['name']

        startingEquipment = ''
        classLevels =''
        classInfo = ["Class: " + val, "Hit Die: D" + hitDice,
                     savingThrows,
                     proficiencyChoice]

        return classInfo

    # Populates information about the race in the GUI
    def writeRaceData(self, val):

        # basic stats that don't require too much formatting
        speed = self.races[self.raceDic[val]]['speed']
        bonuses = self.races[self.raceDic[val]]['ability_bonuses']

        # descriptions that need better formatting, currently using list comprehension
        size = list([self.races[self.raceDic[val]]['size_description'][i:i + 80] for i in
                     range(0, len(self.races[self.raceDic[val]]['size_description']), 80)])
        age = list([self.races[self.raceDic[val]]['age'][i:i + 80] for i in
                    range(0, len(self.races[self.raceDic[val]]['age']), 80)])
        alignment = list([self.races[self.raceDic[val]]['alignment'][i:i + 75] for i in
                          range(0, len(self.races[self.raceDic[val]]['alignment']), 75)])

        info = ["Race: " + val, "Speed: " + str(speed), "Bonuses: " + str(bonuses)]
        age[0] = "Age: " + age[0]
        alignment[0] = "Alignment: " + alignment[0]
        size[0] = "Size: " + size[0]

        info.extend(age)
        info.extend(size)
        info.extend(alignment)

        return info

    def createChar(self, C):
        create = tk.Button(C, text ="Create Character", command = lambda : self.getSelectionInfo())
        create.place(relx=0.7, rely=0.3, width=130, height=30)

    def alignmentSelection(self, C):
        tk.Label(C, text="Select Your Alignment").place(relx=0.02, rely=0.26)
        self.alignmentVar = StringVar(C)
        self.alignmentVar.set(self.alignments[0])  # default choice
        alignmentMenu = OptionMenu(C, self.alignmentVar, *self.alignments)
        alignmentMenu.place(relx=0.01, rely=0.3, width=130, height=30)

    # Sub-races is populated based on race selection
    def subracesSelection(self, C):
        subrace = ["subraces", "get", "called", "depending", "on race"]
        self.dropVar = StringVar(C)
        self.dropVar.set(subrace[0])  # default choice
        dropMenu = OptionMenu(C, self.dropVar, *subrace)
        dropMenu.place(relx=0.35, rely=0.05, width=130, height=30)

    # Specify the level of the character
    def levelSelection(self, C):
        # Might need to make this accept xp or 1-20 value for level
        tk.Label(C, text="Enter Level").place(relx=0.8, rely=0.01)
        self.levelText = tk.Text(C)
        self.levelText.pack()
        self.levelText.place(relx=0.80, rely=0.05, width=60, height=22)

    # Sets the Characters HP stats
    def hitPoints(self, C):
        # determined by hit die and some other stuff, need to research
        hp = tk.Button(C, text="Roll for HP")
        hp.pack()
        hp.place(relx=0.7, rely=0.18, width=130, height=30)

    # User writes data for background of their character
    def characterBackground(self, C):
        background = tk.Button(C, text="Background")
        background.pack()
        background.place(relx=0.35, rely=0.3, width=130, height=30)

    # allows selection of abilities based on class
    def selectAbilities(self, C):
        abilities = tk.Button(C, text="Select Abilities")
        abilities.pack()
        abilities.place(relx=0.35, rely=0.18, width=130, height=30)

    # calls all other buttons and things in the gui
    def newCharCanvas(self):
        newCharacterWindow = tk.Tk()
        newCharacterWindow.title("New Character Window")
        C = tk.Canvas(newCharacterWindow, bg=None, height=500, width=500)
        C.pack()

        self.raceDic = self.data.raceNameDict
        self.classDic = self.data.classNameDict
        self.races = self.data.races
        self.classes = self.data.classes
        self.alignments = self.data.alignments

        self.raceSelection(C)
        self.classSelection(C)
        self.createChar(C)
        self.alignmentSelection(C)
        self.subracesSelection(C)
        self.levelSelection(C)
        self.hitPoints(C)
        self.characterBackground(C)
        self.selectAbilities(C)
        self.infoBox(C)

        newCharacterWindow.mainloop()

    def getSelectionInfo(self):
        # Example on how to get new selection info, can be used to index into character info dict from api
        print("Selections: " + self.dropVar.get())
        print("Class: " + self.classVar.get())
        print("Alignment: "+self.alignmentVar.get())
        print("level: "+self.levelText.get('1.0',END))