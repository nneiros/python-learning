import turtle
turtle.title('sxhma1')
turtle.reset() # reset the environment
turtle.bgcolor("lightblue") # change background color
turtle.pencolor("brown") # change pen color
turtle.penup() # lift the pen
turtle.back(200) # back up the turtle
turtle.pendown() # lower the pen
size = 1
while size < 80:
 turtle.pensize(size)
 turtle.forward(5)
 size = size + 1
turtle.done()


import turtle
turtle.title('Διαφορα σχηματα')
turtle.pensize(3) # Set pen thickness to 3 pixels
turtle.penup() # Pull the pen up
turtle.goto(-200, -50)
turtle.pendown() # Pull the pen down
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("red")
turtle.circle(40, steps = 3) # Draw a triangle
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("blue")
turtle.circle(40, steps = 4) # Draw a square
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("green")
turtle.circle(40, steps = 5) # Draw a pentagon
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("yellow")
turtle.circle(40, steps = 6) # Draw a hexagon
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("purple")
turtle.circle(40) # Draw a circle
turtle.end_fill() # Fill the shape

turtle.color("green")
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.write("Σχηματα με διαφορα χρωματα", 
  font = ("Times", 18, "bold"))
turtle.hideturtle()

turtle.done() 


import turtle
import random

turtle.title("Kατασκευη σχηματων")
turtle.setup(500, 500, 0, 0)

def polygon(sides, length):

    for x in range(sides):
        turtle.forward(length)
        turtle.right(360/sides)

# hide the turtle
turtle.hideturtle()

# tell python to no longer update the graphics
turtle.tracer(0)

for x in range(1000):
    # choose a random spot
    xpos = random.randint(-200,200)
    ypos = random.randint(-200,200)

    # goto this spot
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()

    # generate a random color
    red = random.random() # returns a number between 0 and 1
    green = random.random()
    blue = random.random()

    # fill in our shape
    turtle.fillcolor(red, green, blue)

    # draw the shape
    turtle.begin_fill()
    polygon(4, 50)
    turtle.end_fill()

# update the screen with our drawing
turtle.update()

turtle.exitonclick()
#---------------------------------------------------------
from turtle import *
setup()
colors = ['green', 'red']
title('sxhma')
def drawzig2(depth,size):

    if depth == 0:
        pass
    elif depth:
        pencolor(colors[depth % len(colors)])
        left(90)
        fd(size/2)
        right(90)
        fd(size)
        left(45)
        drawzig2(depth-1,size/2)
        right(45)
        fd(-size)
        left(90)
        fd(-size)
        right(90)
        fd(-size)
        left(45)
        drawzig2(depth-1,size/2)
        right(45)
        fd(size)
        left(90)
        fd(size/2)
        right(90)

drawzig2(4,100)
done()
#-----------------------------------------------------
import turtle
turtle.setup(width=500, height=500)
#turtle.pencolor('#FF0000')
screen = turtle.Screen()
screen.title('Επιδειξη διαγωνιων by Νικος')
t = turtle.Pen()
#color.Pen('red')
t.up()
t.goto(-250,250)
t.down()
t.goto(500,-500)
done()
#-----------------------------------------------------------------------

from tkinter import *
tk = Tk()
tk.title('Διαγωνιοι')
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_line(0, 0, 500, 500)
canvas.create_line(0, 50, 500, 500)
canvas.create_line(50, 0, 500, 500)
canvas.create_line(0, 100, 500, 200)
canvas.create_line(100, 0, 500, 200)
#------------------------------------------------------------------------

from tkinter import *
tk = Tk()
tk.title('Διαφορα σχηματα')
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
#--------------------------------------------------------------------------------------------------           
import turtle
import random

def polygon(sides, length):

    for x in range(sides):
        turtle.forward(length)
        turtle.right(360/sides)

turtle.title("Kατασκευη πολυγωνου")
turtle.setup(500,500, 0,0)

keepgoing = True

while keepgoing == True:

    # get a number of sides from the user
    sides = int(turtle.textinput("Πολυγωνα", "Δωσε # πλευρες"))

    # if the user enters a 0 then we can end the loop
    if sides == 0:
        keepgoing = False
    else:
        # clear the canvas
        turtle.clear()

        # draw the polygon
        polygon(sides, 100)

turtle.exitonclick()
