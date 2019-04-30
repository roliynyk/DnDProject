import LoadData
import tkinter as tk
import random
import character
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
class NewCharacter(Tk):

    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.raceDic = {'Dwarf': 0, 'Elf': 1, 'Halfling': 2, 'Human': 3, 'Dragonborn': 4, 'Gnome': 5, 'Half-Elf': 6, 'Half-Orc': 7, 'Tiefling': 8}

        #Data referenced form api
        self.races = LoadData.DataDictionary().races
        self.classes = LoadData.DataDictionary().classes
        self.alignments = LoadData.DataDictionary().alignments

        #Class functions
        self.raceSelection()
        self.classSelection()
        self.alignmentSelection()
        self.subracesSelection()
        self.levelSelection()
        self.hitPoints()
        self.characterBackground()
        self.createCharacter()
        self.selectAbilities()

        #Tk stuff
        self.parent = parent #no idea what this does but it breaks stuff if its not there
        self.infoBox(self)
        self.geometry('500x500')
        self.grid()
        print(self.races)

    # Box that produces data output based on selection
    def infoBox(self, val):
        listBox = Listbox(self)

        if isinstance(val, str):
            info = self.writeRaceData(val)
            for i in info:
                listBox.insert(END, i)

        listBox.pack()
        listBox.place(relx=0.01, rely=0.4, width=490, height=250)

    # Populates information about the race in the GUI
    def writeRaceData(self, val):

        #basic stats that don't require too much formatting
        speed = self.races[self.raceDic[val]]['speed']
        bonuses = self.races[self.raceDic[val]]['ability_bonuses']

        # descriptions that need better formatting, currently using list comprehension
        size = list([self.races[self.raceDic[val]]['size_description'][i:i + 80] for i in range(0, len(self.races[self.raceDic[val]]['size_description']), 80)])
        age = list([self.races[self.raceDic[val]]['age'][i:i + 80] for i in range(0, len(self.races[self.raceDic[val]]['age']), 80)])
        alignment = list([self.races[self.raceDic[val]]['alignment'][i:i + 75] for i in range(0, len(self.races[self.raceDic[val]]['alignment']), 75)])

        info = ["Race: " + val, "Speed: " + str(speed), "Bonuses: "+str(bonuses) ]
        age[0] = "Age: " + age[0]
        alignment[0] = "Alignment: " + alignment[0]
        size[0] = "Size: " + size[0]

        info.extend(age)
        info.extend(size)
        info.extend(alignment)

        return info

    # Character Race selection menu
    def raceSelection(self):

        Label(self, text="Select Your Race").place(relx = 0.02, rely = 0.01)
        race = []

        for i in self.races:
            race.append(i['name'])

        self.dropVar = StringVar()
        self.dropVar.set(race[0])
        self.dropMenu = OptionMenu(self, self.dropVar, *race, command=self.infoBox)
        self.dropMenu.place(relx=0.01, rely=0.05, width=130, height=30)

    # Character Class selection menu
    def classSelection(self):

        Label(self, text="Select Your Class").place(relx=0.02, rely=0.14)
        classSelection = []

        for i in self.classes:
            classSelection.append(i['name'])

        self.dropVar = StringVar()
        self.dropVar.set(classSelection[0])  # default choice
        self.dropMenu = OptionMenu(self, self.dropVar, *classSelection)
        self.dropMenu.place(relx=0.01, rely=0.18, width=130, height=30)

    # Alignment selection menu
    def alignmentSelection(self):
        Label(self, text="Select Your Alignment").place(relx=0.02, rely=0.26)
        self.dropVar = StringVar()
        self.dropVar.set(self.alignments[0])  # default choice
        self.dropMenu = OptionMenu(self, self.dropVar, *self.alignments)
        self.dropMenu.place(relx=0.01, rely=0.3, width=130, height=30)

    # Subraces is populated based on race selection
    def subracesSelection(self):
        subrace = ["subraces", "get", "called", "depending", "on race"]
        self.dropVar = StringVar()
        self.dropVar.set(subrace[0])  # default choice
        self.dropMenu = OptionMenu(self, self.dropVar, *subrace)
        self.dropMenu.place(relx=0.35, rely=0.05, width=130, height=30)

    # Specify the level of the character
    def levelSelection(self):
        # Might need to make this accept xp or 1-20 value for level
        Label(self, text="Enter Level").place(relx=0.8, rely=0.01)
        listBox = Text(self)
        listBox.pack()
        listBox.place(relx=0.80, rely=0.05, width=60, height=22)

    # Sets the Characters HP stats
    def hitPoints(self):
        #determined by hit die and some other stuff, need to research
        hp = Button(self, text="Roll for HP")
        hp.pack()
        hp.place(relx=0.7, rely=0.18, width=130, height=30)

    def characterBackground(self):
        background = Button(self, text="Background")
        background.pack()
        background.place(relx=0.35, rely=0.3, width=130, height=30)

    # Generates the Character (Do text file stuff)
    def createCharacter(self):
        create = Button(self, text="Create Character")
        create.pack()
        create.place(relx=0.7, rely=0.3, width=130, height=30)

    # allows selection of abilities based on class
    def selectAbilities(self):
        abilities = Button(self, text="Select Abilities")
        abilities.pack()
        abilities.place(relx=0.35, rely=0.18, width=130, height=30)

def create_form():
    form = NewCharacter(None)
    form.title('New Character')
    form.mainloop()

'''

import tkinter as tk
from tkinter import *
import apicalls as ap

def raceSelection(C):
    race = []
    for i in ap.getRaceData():
        race.append(i['name'])

    tk.Label(C, text="Choose a Race").place(relx=0.01, rely=0.01)
    var1 = tk.StringVar(C)
    var1.set(race[0])
    drop = tk.OptionMenu(C, var1, *race)
    drop.pack()
    drop.place(relx=0.01, rely=0.05, width=110, height=30)

def classSelection(C):
    classSelection = []
    for i in ap.getClassData():
        classSelection.append(i['name'])

    tk.Label(C, text="Choose a Class").place(relx=0.01, rely=0.115)
    var1 = tk.StringVar(C)
    var1.set(classSelection[0])
    drop = tk.OptionMenu(C, var1, *classSelection)
    drop.pack()
    drop.place(relx=0.01, rely=0.15, width=110, height=30)

# creates the info box when things are selected in the gui
def infoBox(C):
    raceInfo = tk.Listbox(C)
    raceInfo.insert(END,)
    raceInfo.pack()
    raceInfo.place(relx=0.01, rely=0.6, width=290, height=100)

# calls all other buttons and things in the gui
def newCharCanvas():
    newCharacterWindow = tk.Tk()
    newCharacterWindow.title("New Character Window")
    C = tk.Canvas(newCharacterWindow, bg=None, height=600, width=600)
    C.pack()
    raceSelection(C)
    classSelection(C)
    infoBox(C)
    newCharacterWindow.mainloop()
    
'''