import turtle

myTurtle = turtle.Turtle(shape="turtle")
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-120, 0)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(60,60)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-60, 60)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-180, 60)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-60, 0)
myTurtle.setheading(0)
myTurtle.pendown()
myTurtle.color("red")
myTurtle.write("Νικος ολυμπιακη επιτροπη", font=("Arial", 16, "bold"))  

turtle.getscreen()._root.mainloop()
