#import turtle
#from tkinter import *
#tk = Tk()
#canvas = Canvas(tk, width=400, height=400)
#canvas.pack()
#myimage = PhotoImage(file='shmaia.gif’)
#canvas.create_image(0, 0, image=myimage, anchor=NW)
import os
print (os.getcwd())
import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
for x in range(0, 60):
     canvas.move(1, 5, 0)
     tk.update()
     time.sleep(0.05)       
#import time
#for x in range(0, 60):
 #    canvas.move(1, -5, -5)
  #   tk.update()
   #  time.sleep(0.05)
def movetriangle(event):
     canvas.move(1, 5, 0)
