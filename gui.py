import tkinter
from tkinter import messagebox

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

master = tkinter.Tk()

C = tkinter.Canvas(master, bg=None, height=900, width=900)

newCharacterButton = tkinter.Button(master, text ="New", command = helloCallBack)
newCharacterButton.pack()
C.pack()
master.mainloop()