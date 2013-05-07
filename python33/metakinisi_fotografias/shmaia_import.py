from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
myimage = PhotoImage(file="shmaia.gif")
canvas.create_image(0, 0, image=myimage, anchor=NW)
import os
print(os.getcwd())
