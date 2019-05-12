import tkinter as tk
import random
import character
import NewCharacterGui as ncg
import LoadCharacterGui as lcg
from tkinter import *
from tkinter import constants as cons
from tkinter import messagebox
from PIL import Image, ImageTk
import DiceRollGui as drg
import LoadData
import pprint
import os
from os import listdir
import json
from functools import wraps

class Frame1(Frame):
    def __init__(self, parent):
        self.data = LoadData.DataDictionary()
        Frame.__init__(self, parent)
        self.parent = parent
        self.widgets()

    def widgets(self):
        self.C = Canvas(self, bg = None, width = 900, height = 900)
        self.C.pack()

        #Example caracter creation call and method/variable calls
        self.Blarg = self.createCharacter("Blarg", "Brawler", "Elf", "Parents died", "Self", 0, 20, 15, 0, {"Str":1, "Dex":1, "Con":1, "Int":1, "Wis":1, "Cha":1})

        #Call new character stuff here
        self.NewCharacterStuff(self.Blarg)

        #Call Images here
        self.Images(self.Blarg)

        #Call spells etc here
        self.SpellsEtc()

        #Call roll type buttons here
        self.RollTypes(self.Blarg, self.C)

        self.createTextInfo(self.Blarg)

    def call_count(function, count=[0]):


        @wraps(function)
        def increase_count(*args, **kwargs):
            count[0] += 1
            return function(*args, **kwargs), count[0]

        return increase_count

    @call_count
    def rollDicewithStat(self, toon, stat, sides):
        random.seed()
        number = random.randint(1, sides)
        number = number + toon.returnStat(stat)
        tk.messagebox.showinfo("Stat Check", str(number))

    def NewCharacterStuff(self, character):
        # New character button
        new = tk.Button(self, text ="New", command = lambda : ncg.NewCharGui(self.data))
        new.place(relx=0.01, rely=0.01, width=50, height=30)

        # Load character button
        load = tk.Button(self, text ="Load", command = lambda : self.Load(character))
        load.place(relx=0.08, rely=0.01, width=50, height=30)

        # Save character
        save_char = tk.Button(self, text ="Save", command = lambda : self.SaveChar(character))
        save_char.place(relx=0.16, rely=0.01, width=50, height=30)

        # Print Character Info button EXAMPLE
        print_char = tk.Button(self, text ="Update Character", command = lambda : self.UpdateChar(character))
        print_char.place(relx=0.3, rely=0.01, width=100, height=30)
    
    def Load(self, character):
        lcg.LoadCharGui(character)
        
    #Example of how to access updated character info
    #Mostly used for debugging
    def UpdateChar(self, character):
        #Delete old values
        self.listBoxH.delete(0, 'end')
        self.listBoxA.delete(0, 'end')
        self.listBoxX.delete(0, 'end')
        #Insert new values
        self.listBoxH.insert(END, str(character.health))
        self.listBoxA.insert(END, str(character.armor))
        self.listBoxX.insert(END, str(character.experience))
        #Update other gui elements
        self.createTextInfo(self.Blarg)

    def SaveChar(self, character):
        #Open new .txt file and save character data in json
        #Can add functionality to name files after the character name and update if the save already exists
        counter = 1
        path = os.getcwd() + '/Character_Data'
        onlyfiles = [f for f in listdir(path)]
        for f in onlyfiles:
            if character.name in f:
                counter += 1
        filename = "character_" + character.name + "_" + str(counter) + ".json"
        with open(os.getcwd() + '\\Character_Data\\' + filename, "w+") as f:
            #parsed, indent=4, sort_keys=True
            parsed = json.loads(json.dumps(character.returnAll()))
            json.dump(parsed, f, indent=4)

        saveSuccess = tk.Text(self, height=1, width=20)
        saveSuccess.pack()
        saveSuccess.insert(cons.END, "Save Successful")
        saveSuccess.place(relx=.75, rely=0.65, width=200, height=40)

    def Images(self, character):
        # Character image things
        charImg = Image.open("character-image/rick.jpeg")
        charImg = charImg.resize((180,210), Image.ANTIALIAS)
        characterPic = ImageTk.PhotoImage(charImg)
        panel = tk.Label(self, image = characterPic)
        panel.image = characterPic
        panel.place(relx=0.01, rely=0.06)

        # Health image
        hp = Image.open("icons/hp.png")
        hp = hp.resize((35, 35))
        hpInfo = ImageTk.PhotoImage(hp)
        hpp = tk.Label(self, image = hpInfo)
        hpp.image = hpInfo
        hpp.place(relx=0.52, rely=0.06)

        #Health input box (current/total)
        tk.Label(self, text="Enter Health").place(relx=0.6, rely=0.04)
        tk.Label(self, text="/" + str(character.health)).place(relx=0.67, rely=0.07)
        self.listBoxH = tk.Entry(self)
        self.listBoxH.insert(END, str(character.health))
        self.listBoxH.pack()
        self.listBoxH.place(relx=0.6, rely=0.07, width=60, height=22)

        # Armor image
        armor = Image.open("icons/armor.png")
        armor = armor.resize((35, 35))
        armorInfo = ImageTk.PhotoImage(armor)
        armorp = tk.Label(self, image = armorInfo)
        armorp.image = armorInfo
        armorp.place(relx=0.52, rely=0.12)

        #Armor input box (current/total)
        tk.Label(self, text="Enter Armor").place(relx=0.6, rely=0.1)
        tk.Label(self, text="/" + str(character.armor)).place(relx=0.67, rely=0.13)
        self.listBoxA = tk.Entry(self)
        self.listBoxA.insert(END, str(character.armor))
        self.listBoxA.pack()
        self.listBoxA.place(relx=0.6, rely=0.13, width=60, height=22)

        # XP images
        xp = Image.open("icons/xp.png")
        xp = xp.resize((35, 35))
        xpInfo = ImageTk.PhotoImage(xp)
        xp = tk.Label(self, image = xpInfo)
        xp.image = xpInfo
        xp.place(relx=0.52, rely=0.18)

        #XP input box
        tk.Label(self, text="Enter XP").place(relx=0.6, rely=0.16)
        self.listBoxX = tk.Entry(self)
        self.listBoxX.insert(END, str(character.experience))
        self.listBoxX.pack()
        self.listBoxX.place(relx=0.6, rely=0.19, width=60, height=22)

        update = tk.Button(self, text="Update", command = lambda: character.updateHealthEtc(int(self.listBoxH.get()), int(self.listBoxA.get()), int(self.listBoxX.get())))
        update.place(relx=0.72, rely=0.125, width=200, height=30)

    def RollTypes(self, toon, C):
        # Roll types
        stren = tk.Button(self, text ="Str", command = lambda: print(self.rollDicewithStat(toon,"Str",20)))
        stren.place(relx=0.5, rely=0.3, width=200, height=30)

        dex = tk.Button(self, text ="Dex", command = lambda: print(self.rollDicewithStat(toon,"Dex",20)))
        dex.place(relx=0.5, rely=0.35, width=200, height=30)

        con = tk.Button(self, text ="Con", command = lambda: print(self.rollDicewithStat(toon,"Con",20)))
        con.place(relx=0.5, rely=0.4, width=200, height=30)

        intel = tk.Button(self, text ="Int", command = lambda: print(self.rollDicewithStat(toon,"Int",20)))
        intel.place(relx=0.5, rely=0.45, width=200, height=30)

        wis = tk.Button(self, text ="Wis", command = lambda: print(self.rollDicewithStat(toon,"Wis",20)))
        wis.place(relx=0.5, rely=0.5, width=200, height=30)

        cha = tk.Button(self, text ="Cha", command = lambda: print(self.rollDicewithStat(toon,"Cha",20)))
        cha.place(relx=0.5, rely=0.55, width=200, height=30)

        #roll = tk.Button(self, text ="New Roll", command = drg.DiceRoll)
        #roll.place(relx=0.75, rely=0.3, width=200, height=30)

        # Dice rolls
        d4 = tk.Button(C, text ="D4", command = lambda : self.rollDice(4, C))
        d4.place(relx=.75, rely=0.3, width=200, height=30)

        d6 = tk.Button(C, text ="D6", command = lambda : self.rollDice(6, C))
        d6.place(relx=.75, rely=0.35, width=200, height=30)

        d8 = tk.Button(C, text ="D8", command = lambda : self.rollDice(8, C))
        d8.place(relx=.75, rely=0.4, width=200, height=30)

        d10 = tk.Button(C, text ="D10", command = lambda : self.rollDice(10, C))
        d10.place(relx=.75, rely=0.45, width=200, height=30)

        d20 = tk.Button(C, text ="D20", command = lambda : self.rollDice(20, C))
        d20.place(relx=.75, rely=0.5, width=200, height=30)

        d100 = tk.Button(C, text ="D100", command = lambda : self.rollDice(100, C, True))
        d100.place(relx=.75, rely=0.55, width=200, height=30)

    def rollDice(self, sides, C, hundred=False):
        random.seed()
        if hundred:
            number = str(random.choice([10,20,30,40,50,60,70,80,90,100]))
        else:
            number = str(random.randint(1, sides))
        # Output the number wherever we need it to display
        statInfo = tk.Text(C, height=1, width=20)
        statInfo.pack()
        statInfo.insert(cons.END, "Dice: D" + str(sides) + "\nRole: " + str(number))
        statInfo.place(relx=.75, rely=0.6, width=200, height=40)

    def SpellsEtc(self):
        # Character spells
        spells = tk.Button(self, text ="Spells", command = self.helloCallBack)
        spells.place(relx=0.15, rely=0.3, width=200, height=30)

        inventory = tk.Button(self, text ="Inventory", command = self.helloCallBack)
        inventory.place(relx=0.15, rely=0.35, width=200, height=30)

        skills = tk.Button(self, text ="Skills", command = self.helloCallBack)
        skills.place(relx=0.15, rely=0.40, width=200, height=30)

        background = tk.Button(self, text ="Background", command = self.helloCallBack)
        background.place(relx=0.15, rely=0.45, width=200, height=30)

    #Function for debugging button presses etc...
    def helloCallBack(self):
        tk.messagebox.showinfo("Hello Python", "Hello World")

    # Create text for the character such as name and stats
    def createTextInfo(self, character):
        basicCharacterInfo = tk.Text(self, height=13, width=30)
        basicCharacterInfo.pack()
        basicCharacterInfo.insert(cons.END, "Name: " + character.name + "\n")
        #basicCharacterInfo.insert(cons.END, "Stats: " + str(character.returnStats()) + "\n")
        basicCharacterInfo.place(relx=0.22, rely=0.06)

        stats_dict = character.returnStats()
        statInfo = tk.Text(self, height=6, width=10)
        statInfo.pack()
        statInfo.insert(cons.END, "STR: " + str(stats_dict["Str"]) + "\nDEX: " + str(stats_dict["Dex"]) + "\nCON: " + str(stats_dict["Con"]) + 
            "\nINT: " + str(stats_dict["Int"]) + "\nWIS: " + str(stats_dict["Wis"]) + "\nCHA: " + str(stats_dict["Cha"]))
        statInfo.place(relx=0.01, rely=0.3)

    def createCharacter(self,name, class_type, race, background, alignment, experience, health, armor, profficiency, stats):
        return character.Character(name, class_type, race, background, alignment, experience, health, armor, profficiency, stats)

class MainWindow(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.mainWidgets()

    def mainWidgets(self):
        self.window = Frame1(self)
        self.window.pack()

if __name__ == "__main__":
    app = MainWindow(None)
    app.mainloop()