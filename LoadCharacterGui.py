import tkinter as tk
from tkinter import *
import LoadData
import os, os.path
from os import listdir
from os.path import isfile, join

class LoadCharGui(tk.Tk):

    def __init__(self):
        self.newCharCanvas()

    # Calls all other buttons and things in the gui
    def newCharCanvas(self):
        newCharacterWindow = tk.Tk()
        newCharacterWindow.title("Load Character Window")
        C = tk.Canvas(newCharacterWindow, bg=None, height=200, width=200)
        C.pack()

        self.characterSelection(C)

        newCharacterWindow.mainloop()

    def characterSelection(self, C):
        tk.Label(C, text="Select Character to Load").place(relx=0.2, rely=0.05)
        #Setup the variable or the option menu
        self.dropVar1 = tk.StringVar(C)
        #Get path to the character saves
        path = os.getcwd() + '/Character_Data'
        onlyfiles = [f for f in listdir(path)]
        self.dropVar1.set(onlyfiles[0])
        #Set option menu
        dropMenu = tk.OptionMenu(C, self.dropVar1, onlyfiles[0], *onlyfiles[1:], command = self.SetVal)
        dropMenu.pack()
        dropMenu.place(relx=0.2, rely=0.2, width=130, height=30)
        #Set load button and function
        load = tk.Button(C, text ="Load", command = lambda : self.GetCharData)
        load.pack()
        load.place(relx=0.2, rely=0.4, width=130, height=30)

    # def SetVal(self, val):
    #     val_int = val
    #     assert isinstance(val_int, str)

    #     #open file

    #     print(val_int)

    #Method to get character data and return it to main
    def GetCharData(self):
        #open file here and read in data
        print("Hello World")
