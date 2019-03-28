import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

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
image = Image.open("rick.jpeg")
image = image.resize((200,200), Image.ANTIALIAS)
characterPic = ImageTk.PhotoImage(image)
panel = tk.Label(master, image = characterPic)
panel.pack()
panel.place(relx=0.01, rely=0.06)


C.pack()
master.mainloop()