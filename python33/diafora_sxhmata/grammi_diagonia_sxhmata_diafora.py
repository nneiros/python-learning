from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_line(0, 0, 500, 500)
import turtle
turtle.setup(width=500, height=500)
t = turtle.Pen()
t.up()
t.goto(-250,250)
t.down()
t.goto(500,-500)
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400,height=400)
canvas.pack()
canvas.create_rectangle(10, 10, 50, 50)
1
canvas.create_rectangle(100, 100, 300, 50)
canvas.create_rectangle(100, 200, 150, 350)
import random
def random_rectangle(width, height):
     x1 = random.randrange(width)
     y1 = random.randrange(height)
     x2 = random.randrange(x1 + random.randrange(width))
     y2 = random.randrange(y1 + random.randrange(height))
     canvas.create_rectangle(x1, y1, x2, y2)
random_rectangle(400, 400)
for x in range(0, 100):
    random_rectangle(400, 400)
def random_rectangle(width, height, fill_colour):
     x1 = random.randrange(width)
     y1 = random.randrange(height)
     x2 = random.randrange(x1 + random.randrange(width))
     y2 = random.randrange(y1 + random.randrange(height))
     canvas.create_rectangle(x1, y1, x2, y2, fill=fill_colour)
           
