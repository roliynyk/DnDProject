import tkinter as tk
from tkinter import *
import LoadData
import os, os.path
from os import listdir
from os.path import isfile, join
import json

class LoadCharGui(tk.Tk):

    def __init__(self, character):
        self.character = character
        self.newCharCanvas()

    # Calls all other buttons and things in the gui
    def newCharCanvas(self):
        self.newCharacterWindow = tk.Tk()
        self.newCharacterWindow.title("Load Character Window")
        C = tk.Canvas(self.newCharacterWindow, bg=None, height=200, width=200)
        C.pack()

        self.characterSelection(C)

        self.newCharacterWindow.mainloop()

    def characterSelection(self, C):
        tk.Label(C, text="Select Character to Load").place(relx=0.2, rely=0.05)
        #Setup the variable or the option menu
        self.dropVar1 = tk.StringVar(C)
        #Get path to the character saves
        path = os.getcwd() + '/Character_Data'
        onlyfiles = [f for f in listdir(path)]
        self.dropVar1.set('Select a File')
        #Set option menu
        dropMenu = tk.OptionMenu(C, self.dropVar1, onlyfiles[0], *onlyfiles[1:], command = self.SetVal)
        dropMenu.pack()
        dropMenu.place(relx=0.2, rely=0.2, width=130, height=30)
        #Set load button and function
        load = tk.Button(C, text ="Load", command = lambda : self.GetCharData(self.filename))
        load.pack()
        load.place(relx=0.2, rely=0.4, width=130, height=30)

    def SetVal(self, val):
        self.filename = val
        assert isinstance(self.filename, str)
        #print(self.filename)

    #Method to get character data and return it to main
    def GetCharData(self, filename):
        #open file here and read in data
        with open(os.getcwd() + '/Character_Data/' + filename) as f:
            char_json = json.load(f)
        self.character.updateStats(char_json)
        self.newCharacterWindow.destroy()
        #Load back into main here
        