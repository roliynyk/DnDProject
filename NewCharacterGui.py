import sys
import apicalls as ap
import LoadData
from tkinter import *

# My frame for form
class NewCharacter(Tk):

    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.inputArr = []
        self.raceDic = {'Dwarf': 0, 'Elf': 1, 'Halfling': 2, 'Human': 3, 'Dragonborn': 4, 'Gnome': 5, 'Half-Elf': 6, 'Half-Orc': 7, 'Tiefling': 8}
        self.parent = parent
        self.races = LoadData.DataDictionary().races
        self.classes = LoadData.DataDictionary().classes
        self.raceSelection()
        self.classSelection()
        self.infoBox(self)
        self.geometry('500x500')
        self.grid()

    def infoBox(self, val):
        listBox = Listbox(self)

        if isinstance(val, str):
            info = self.writeRaceData(val)
            for i in info:
                listBox.insert(END, i)

        listBox.pack()
        listBox.place(relx=0.01, rely=0.4, width=490, height=250)

    def writeRaceData(self, val):

        speed = self.races[self.raceDic[val]]['speed']
        age = list([self.races[self.raceDic[val]]['age'][i:i + 80] for i in range(0, len(self.races[self.raceDic[val]]['age']), 80)])
        alignment = list([self.races[self.raceDic[val]]['alignment'][i:i + 75] for i in range(0, len(self.races[self.raceDic[val]]['alignment']), 75)])
        info = ["Race: " + val, "Speed: " + str(speed)]
        age[0] = "Age: " + age[0]
        alignment[0] = "Alignment: " + alignment[0]
        info.extend(age)
        info.extend(alignment)
        return info

    def raceSelection(self):
        print("FUNCTION WAS CALLED")
        race = []

        for i in self.races:
            race.append(i['name'])

        self.dropVar = StringVar()
        self.dropVar.set(race[0])
        self.dropMenu = OptionMenu(self, self.dropVar, *race, command=self.infoBox)
        self.dropMenu.place(relx=0.01, rely=0.05, width=110, height=30)

    def classSelection(self):
        # Dropdown Menu
        classSelection = []
        c_class=ap.getClassData()

        for i in c_class:
            classSelection.append(i['name'])

        self.dropVar = StringVar()
        self.dropVar.set(classSelection[0])  # default choice
        self.dropMenu1 = OptionMenu(self, self.dropVar, *classSelection, command=self.infoBox)
        self.dropMenu1.place(relx=0.01, rely=0.15, width=110, height=30)

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