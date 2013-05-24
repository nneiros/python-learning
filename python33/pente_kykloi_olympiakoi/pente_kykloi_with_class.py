import turtle

########################################################################
class MyTurtle(turtle.Turtle):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Turtle Constructor"""
        turtle.Turtle.__init__(self, shape="turtle")
        screen = turtle.Screen()
        screen.bgcolor("yellow")
        self.pensize(3)
    #----------------------------------------------------------------------
    def drawCircle(self, x, y, radius=50):
        """
        Moves the turtle to the correct position and draws a circle
        """
        self.penup()
        self.setposition(x, y)
        self.pendown()
        self.circle(radius)
        
    #----------------------------------------------------------------------
    def drawOlympicSymbol(self):
        """
        Iterates over a set of positions to draw the Olympics logo
        """
        positions = [(0, 0), (-120, 0), (60,60),
                     (-60, 60), (-180, 60)]
        for position in positions:
            self.drawCircle(position[0], position[1])
        self.drawText()

    def drawText(self):
        """
        Draw text to the screen
        """
        self.penup()
        self.setposition(-60, 0)
        self.setheading(0)
        self.pendown()
        self.color("black")
        self.write("London 2012", font=("Arial", 16, "bold"))               

if __name__ == "__main__":
    t = MyTurtle()
    t.drawOlympicSymbol()
    turtle.getscreen()._root.mainloop()
    
