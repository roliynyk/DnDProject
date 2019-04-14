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
