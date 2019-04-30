import tkinter as tk
import random
import character
import NewCharacterGui as ncg
from tkinter import *
from tkinter import constants as cons
from tkinter import messagebox
from PIL import Image, ImageTk
import DiceRollGui as drg

class Frame1(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.widgets()

    def widgets(self):
        self.C = Canvas(self, bg = None, width = 900, height = 900)
        self.C.pack()

        #Call new character stuff here
        self.NewCharacterStuff()

        #Call Images here
        self.Images()

        #Call spells etc here
        self.SpellsEtc()

        #Call roll type buttons here
        self.RollTypes()

        #Example caracter creation call and method/variable calls
        Blarg = self.createCharacter("Blarg", "Brawler", "Elf", "Parents died", "Self", 0, 20, 15, 0, {"Str":1})
        print(Blarg.name)
        print(Blarg.returnStat("Str"))
        Blarg.updateStat("Str", 2)
        print(Blarg.returnStat("Str"))

        self.createTextInfo(Blarg)
    
    def NewCharacterStuff(self):
        # New character button
        new = tk.Button(self, text ="New", command = ncg.NewCharGui)
        new.place(relx=0.01, rely=0.01, width=50, height=30)

        # Load character button
        load = tk.Button(self, text ="Load", command = self.helloCallBack)
        load.place(relx=0.08, rely=0.01, width=50, height=30)

    def Images(self):
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

        # Armor image
        armor = Image.open("icons/armor.png")
        armor = armor.resize((35, 35))
        armorInfo = ImageTk.PhotoImage(armor)
        armorp = tk.Label(self, image = armorInfo)
        armorp.image = armorInfo
        armorp.place(relx=0.52, rely=0.12)

        # Other images
        xp = Image.open("icons/xp.png")
        xp = xp.resize((35, 35))
        xpInfo = ImageTk.PhotoImage(xp)
        xp = tk.Label(self, image = xpInfo)
        xp.image = xpInfo
        xp.place(relx=0.52, rely=0.18)

    def RollTypes(self):
        # Roll types
        stren = tk.Button(self, text ="Str", command = self.helloCallBack)
        stren.place(relx=0.5, rely=0.3, width=200, height=30)

        dex = tk.Button(self, text ="Dex", command = self.helloCallBack)
        dex.place(relx=0.5, rely=0.35, width=200, height=30)

        con = tk.Button(self, text ="Con", command = self.helloCallBack)
        con.place(relx=0.5, rely=0.4, width=200, height=30)

        intel = tk.Button(self, text ="Int", command = self.helloCallBack)
        intel.place(relx=0.5, rely=0.45, width=200, height=30)

        wis = tk.Button(self, text ="Wis", command = self.helloCallBack)
        wis.place(relx=0.5, rely=0.5, width=200, height=30)

        cha = tk.Button(self, text ="Cha", command = self.helloCallBack)
        cha.place(relx=0.5, rely=0.55, width=200, height=30)

        roll = tk.Button(self, text ="New Roll", command = drg.DiceRoll)
        roll.place(relx=0.75, rely=0.3, width=200, height=30)

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

    def helloCallBack(self):
        tk.messagebox.showinfo("Hello Python", "Hello World")

    # Create text for the character such as name and stats
    def createTextInfo(self, character):
        basicCharacterInfo = tk.Text(self, height=13, width=30)
        basicCharacterInfo.pack()
        basicCharacterInfo.insert(cons.END, "Name: " + character.name)
        basicCharacterInfo.place(relx=0.22, rely=0.06)

        statInfo = tk.Text(self, height=6, width=10)
        statInfo.pack()
        statInfo.insert(cons.END, "STR\nDEX\nCON\nINT\nWIS\nCHA\n")
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