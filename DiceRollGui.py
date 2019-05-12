import tkinter as tk
import random
import character
import NewCharacterGui as ncg
from tkinter import constants as cons
from tkinter import messagebox
from tkinter import Frame
from PIL import Image, ImageTk

class DiceRoll(tk.Tk):
    def __init__(self):
        #Create window code etc here
        self.newDiceCanvas()
        
    def widgets(self, C):
        # Dice rolls
        d4 = tk.Button(C, text ="D4", command = lambda : self.rollDice(4, C))
        d4.place(relx=.1, rely=0.1, width=200, height=30)

        d6 = tk.Button(C, text ="D6", command = lambda : self.rollDice(6, C))
        d6.place(relx=.1, rely=0.2, width=200, height=30)

        d8 = tk.Button(C, text ="D8", command = lambda : self.rollDice(8, C))
        d8.place(relx=.1, rely=0.3, width=200, height=30)

        d10 = tk.Button(C, text ="D10", command = lambda : self.rollDice(10, C))
        d10.place(relx=.1, rely=0.4, width=200, height=30)

        d20 = tk.Button(C, text ="D20", command = lambda : self.rollDice(20, C))
        d20.place(relx=.1, rely=0.5, width=200, height=30)

        d100 = tk.Button(C, text ="D100", command = lambda : self.rollDice(100, C))
        d100.place(relx=.1, rely=0.6, width=200, height=30)

    def rollDice(self, sides, C):
        random.seed()
        number = str(random.randint(1, sides))
        # Output the number wherever we need it to display
        statInfo = tk.Text(C, height=1, width=20)
        statInfo.pack()
        statInfo.insert(cons.END, number)
        statInfo.place(relx=.1, rely=0.7)




    def newDiceCanvas(self):
        newDiceWindow = tk.Tk()
        newDiceWindow.title("Dice")
        C = tk.Canvas(newDiceWindow, bg=None, height=400, width=250)
        C.pack()
        self.widgets(C)
        newDiceWindow.mainloop()