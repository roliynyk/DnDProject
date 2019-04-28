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
        self.var1 = tk.StringVar(C)
        self.var1.set(race[0])
        drop = OptionMenu(C, self.var1, race[0], *race[1:])
        drop.pack()
        drop.place(relx=0.01, rely=0.05, width=110, height=30)

    def classSelection(self,C):
        classSelection = []
        for i in ap.getClassData():
            classSelection.append(i['name'])

        tk.Label(C, text="Choose a Class").place(relx=0.01, rely=0.115)
        self.var2 = tk.StringVar(C)
        self.var2.set(classSelection[0])
        drop = OptionMenu(C, self.var2, classSelection[0], *classSelection[1:])
        drop.pack()
        drop.place(relx=0.01, rely=0.15, width=110, height=30)

    # creates the info box when things are selected in the gui
    def infoBox(self,C):
        raceInfo = tk.Listbox(C)
        raceInfo.insert(END,)
        raceInfo.pack()
        raceInfo.place(relx=0.01, rely=0.6, width=290, height=100)

    def createChar(self, C):
        create = tk.Button(C, text ="Create Character", command = lambda : self.getSelectionInfo())
        create.place(relx=.5, rely=0.5, width=200, height=30)

    # calls all other buttons and things in the gui
    def newCharCanvas(self):
        newCharacterWindow = tk.Tk()
        newCharacterWindow.title("New Character Window")
        C = tk.Canvas(newCharacterWindow, bg=None, height=600, width=600)
        C.pack()
        self.raceSelection(C)
        self.classSelection(C)
        self.infoBox(C)
        self.createChar(C)
        newCharacterWindow.mainloop()

    def getSelectionInfo(self):
        #Example on how to get new selection info, can be used to index into character info dict from api
        print("Selections: " + self.var1.get() + ", " + self.var2.get())
