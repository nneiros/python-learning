from tkinter import *
tk = Tk()
tk.title('Σημαιες')
canvas = Canvas(tk, width=400, height=400)

canvas.pack()

myimage = PhotoImage(file="shmaia.gif")
canvas.create_image(90, 90, image=myimage, anchor=NW)
import os
print(os.getcwd())
