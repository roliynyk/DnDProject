import tkinter as tk
from tkinter import *
import apicalls as ap

class NewCharGui(tk.Tk):
    def __init__(self):
        self.newCharCanvas()

    def raceSelection(self, C):
        race = []
        for i in ap.getRaceData():
            race.append(i['name'])

        tk.Label(C, text="Choose a Race").place(relx=0.01, rely=0.01)
        var1 = tk.StringVar(C)
        var1.set(race[0])
        drop = tk.OptionMenu(C, var1, *race)
        drop.pack()
        drop.place(relx=0.01, rely=0.05, width=110, height=30)

    def classSelection(self,C):
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
    def infoBox(self,C):
        raceInfo = tk.Listbox(C)
        raceInfo.insert(END,)
        raceInfo.pack()
        raceInfo.place(relx=0.01, rely=0.6, width=290, height=100)

    # calls all other buttons and things in the gui
    def newCharCanvas(self):
        newCharacterWindow = tk.Tk()
        newCharacterWindow.title("New Character Window")
        C = tk.Canvas(newCharacterWindow, bg=None, height=600, width=600)
        C.pack()
        self.raceSelection(C)
        self.classSelection(C)
        self.infoBox(C)
        newCharacterWindow.mainloop()
