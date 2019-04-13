import tkinter as tk
import random
import character
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def rollDice(sides):
   random.seed()
   number = str(random.randint(0, sides))
   #output the number wherever we need it to display
   statInfo = tk.Text(master, height=1, width=20)
   statInfo.pack()
   statInfo.insert(END, number)
   statInfo.place(relx=0.75, rely=0.6)

def helloCallBack():
   tk.messagebox.showinfo( "Hello Python", "Hello World")

#Create text for the character such as name and stats
def createTextInfo():
   basicCharacterInfo = tk.Text(master, height=13, width=30)
   basicCharacterInfo.pack()
   basicCharacterInfo.insert(END, "TODO: Make calls to get name and other info")
   basicCharacterInfo.place(relx=0.22, rely=0.06)
   C.pack()

   statInfo = tk.Text(master, height=6, width=10)
   statInfo.pack()
   statInfo.insert(END, "STR\nDEX\nCON\nINT\nWIS\nCHA\n")
   statInfo.place(relx=0.01, rely=0.3)

def createCharacter(name, class_type, race, background, alignment, experience, health, armor, profficiency, stats):
   return character.Character(name, class_type, race, background, alignment, experience, health, armor, profficiency, stats)

master = tk.Tk()
C = tk.Canvas(master, bg=None, height=900, width=900)

# new character button
new = tk.Button(master, text ="New", command = helloCallBack)
new.pack()
new.place(relx=0.01, rely=0.01, width=50, height=30)

# load character button
load = tk.Button(master, text ="Load", command = helloCallBack)
load.pack()
load.place(relx=0.08, rely=0.01, width=50, height=30)

# character image things
charImg = Image.open("character-image/rick.jpeg")
charImg = charImg.resize((180,210), Image.ANTIALIAS)
characterPic = ImageTk.PhotoImage(charImg)
panel = tk.Label(master, image = characterPic)
panel.pack()
panel.place(relx=0.01, rely=0.06)

hp = Image.open("icons/hp.png")
hp = hp.resize((35, 35))
hpInfo = ImageTk.PhotoImage(hp)
hpp = tk.Label(master, image = hpInfo)
hpp.pack()
hpp.place(relx=0.52, rely=0.06)

armor = Image.open("icons/armor.png")
armor = armor.resize((35, 35))
armorInfo = ImageTk.PhotoImage(armor)
armorp = tk.Label(master,image=armorInfo)
armorp.pack()
armorp.place(relx=0.52, rely=0.12)

xp = Image.open("icons/xp.png")
xp = xp.resize((35, 35))
xpInfo = ImageTk.PhotoImage(xp)
xp = tk.Label(master,image=xpInfo)
xp.pack()
xp.place(relx=0.52, rely=0.18)

#character spells
spells = tk.Button(master, text ="Spells", command = helloCallBack)
spells.pack()
spells.place(relx=0.15, rely=0.3, width=200, height=30)

inventory = tk.Button(master, text ="Inventory", command = helloCallBack)
inventory.pack()
inventory.place(relx=0.15, rely=0.35, width=200, height=30)

skills = tk.Button(master, text ="Skills", command = helloCallBack)
skills.pack()
skills.place(relx=0.15, rely=0.40, width=200, height=30)

background = tk.Button(master, text ="Background", command = helloCallBack)
background.pack()
background.place(relx=0.15, rely=0.45, width=200, height=30)

#roll types
stren = tk.Button(master, text ="Str", command = helloCallBack)
stren.pack()
stren.place(relx=0.5, rely=0.3, width=200, height=30)

dex = tk.Button(master, text ="Dex", command = helloCallBack)
dex.pack()
dex.place(relx=0.5, rely=0.35, width=200, height=30)

con = tk.Button(master, text ="Con", command = helloCallBack)
con.pack()
con.place(relx=0.5, rely=0.4, width=200, height=30)

intel = tk.Button(master, text ="Int", command = helloCallBack)
intel.pack()
intel.place(relx=0.5, rely=0.45, width=200, height=30)

wis = tk.Button(master, text ="Wis", command = helloCallBack)
wis.pack()
wis.place(relx=0.5, rely=0.5, width=200, height=30)

cha = tk.Button(master, text ="Cha", command = helloCallBack)
cha.pack()
cha.place(relx=0.5, rely=0.55, width=200, height=30)

#dice rolls
d4 = tk.Button(master, text ="D4", command = lambda : rollDice(4))
d4.pack()
d4.place(relx=0.75, rely=0.3, width=200, height=30)

d6 = tk.Button(master, text ="D6", command = lambda : rollDice(6))
d6.pack()
d6.place(relx=0.75, rely=0.35, width=200, height=30)

d8 = tk.Button(master, text ="D8", command = lambda : rollDice(8))
d8.pack()
d8.place(relx=0.75, rely=0.4, width=200, height=30)

d10 = tk.Button(master, text ="D10", command = lambda : rollDice(10))
d10.pack()
d10.place(relx=0.75, rely=0.45, width=200, height=30)

d20 = tk.Button(master, text ="D20", command = lambda : rollDice(20))
d20.pack()
d20.place(relx=0.75, rely=0.5, width=200, height=30)

d100 = tk.Button(master, text ="D100", command = lambda : rollDice(100))
d100.pack()
d100.place(relx=0.75, rely=0.55, width=200, height=30)

createTextInfo()
#Example caracter creation call
Blarg = createCharacter("Blarg", "Brawler", "Elf", "Parents died", "Self", 0, 20, 15, 0, {"Str":1})
Blarg.printName()
print(Blarg.returnStat("Str"))
Blarg.updateStat("Str", 2)
print(Blarg.returnStat("Str"))
master.mainloop()