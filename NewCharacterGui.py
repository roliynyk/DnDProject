import sys
import apicalls as ap
import dataDict
from tkinter import *

# My frame for form
class simpleform_ap(Tk):

    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.inputArr = []
        self.raceDic = {'Dwarf': 1, 'Elf': 2, 'Halfling': 3, 'Human': 4, 'Dragonborn': 5,
                        'Gnome': 6, 'Half-Elf': 7, 'Half-Orc': 8, 'Tiefling': 9}
        self.parent = parent
        self.raceSelection()
        self.classSelection()
        self.infoBox(self)
        self.geometry('500x500')
        self.grid()

    def infoBox(self, val):
        listBox = Listbox(self)

        if isinstance(val, str):

            #print(dataDict.DataDictionary.races)
            speed = ap.getRaceData()[self.raceDic[val]]['speed']
            age = list([ap.getRaceData()[self.raceDic[val]]['age'][i:i + 60] for i in range(0, len(ap.getRaceData()[self.raceDic[val]]['age']), 60)])
            print(age)
            alignment = ap.getRaceData()[self.raceDic[val]]['alignment']
            info = ["Race: "+val,"speed: "+str(speed)]
            info.extend(age)
            for i in info:
                listBox.insert(END, i)

        listBox.pack()
        listBox.place(relx=0.01, rely=0.6, width=490, height=100)

    def raceSelection(self):
        # Dropdown Menu
        c_race=ap.getRaceData()
        race = []
        for i in c_race:
            race.append(i['name'])

        self.dropVar = StringVar()
        self.dropVar.set(race[0]) # default choice
        self.dropMenu1 = OptionMenu(self, self.dropVar, *race, command=self.infoBox)
        self.dropMenu1.place(relx=0.01, rely=0.05, width=110, height=30)

    def classSelection(self):
        # Dropdown Menu
        classSelection = []
        c_class=ap.getClassData()

        for i in c_class:
            classSelection.append(i['name'])

        self.dropVar = StringVar()
        self.dropVar.set(classSelection[0])  # default choice
        self.dropMenu1 = OptionMenu(self, self.dropVar, *classSelection, command=self.func)
        self.dropMenu1.place(relx=0.01, rely=0.15, width=110, height=30)

    def func(self,value):
        print( value)


def create_form(argv):
    form = simpleform_ap(None)
    form.title('New Character')
    form.mainloop()

if __name__ == "__main__":
    create_form(sys.argv)



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