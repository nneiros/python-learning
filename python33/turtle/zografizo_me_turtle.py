#zografizo me turtle
import turtle
turtle.setup(500,600) # determine the window size
wn = turtle.Screen() # get a reference to the window
wn.title("Xειρισμος με τα πληκτρα επανω,δεξια,αριστερα,q=εξοδος!") # Change the window title
wn.bgcolor("lightgreen") # Set the background color
tess = turtle.Turtle() # Create our favorite turtle
# The next four functions are our "event handlers".
def h1():
     tess.forward(30)
def h2():
     tess.left(45)
def h3():
     tess.right(45)
def h4():
     wn.bye() # Close down the turtle window
# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")#me to epano velaki kinitai pros ta ekei pou vlepei
wn.onkey(h2, "Left")#girnaei to velaki
wn.onkey(h3, "Right")#girnaei to velaki
wn.onkey(h4, "q")#exodos
# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()
print('*'*73)
#-----------------------------------------------------------------------------------------------------------------------
#zografizo patontas to koumpi tou pontikiou paragrafos 10.2
import turtle
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Zωγραφιζω πατωντας το κουμπι του ποντικιου!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("purple")
tess.pensize(2)
tess.shape("circle")
def h1(x, y):
     tess.goto(x, y)
wn.onclick(h1) # Wire up a click on the window.
def h2():
     wn.bye()
wn.onkey(h2, 'q')
wn.listen()
wn.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
import turtle
turtle.setup(500,500) # determine the window size
wn = turtle.Screen() # get a reference to the window
wn.title("Zωγραφιζω πατωντας το κουμπι του ποντικιου με 2 κερσορες!") # Change the window title
wn.bgcolor("lightgreen") # Set the background color
tess = turtle.Turtle() # Create two turtles
tess.color("purple")
alex = turtle.Turtle() # and move them apart
alex.color("blue")
alex.forward(100)
def handler_for_tess(x, y):
     wn.title("Πρωτος κερσορας {0}, {1}".format(x, y))
     tess.left(42)
     tess.forward(30)
def handler_for_alex(x, y):
     wn.title("Δευτερος κερσορας {0}, {1}".format(x, y))
     alex.right(84)
     alex.forward(50)
tess.onclick(handler_for_tess)
alex.onclick(handler_for_alex)
wn.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
import turtle
turtle.setup(450,500)
wn = turtle.Screen()
wn.title("Σχεδιασμος ενος φαναριου κυκλοφοριας,αλλαζει με space!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
def draw_housing():
     ''' Draw a nice housing to hold the traffic lights '''
     tess.pensize(3)
     tess.color('black', 'darkgrey')
     tess.begin_fill()
     tess.forward(80)
     tess.left(90)
     tess.forward(200)
     tess.circle(40, 180)
     tess.forward(200)
     tess.left(90)
     tess.end_fill()
draw_housing()
tess.penup()
# Position Tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape('circle')
tess.shapesize(3)
tess.fillcolor('green')
# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
# This variable holds the current state of the machine
state_num = 0
def advance_state_machine():
     global state_num
     if state_num == 0: # transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor('orange')
        state_num = 1
     elif state_num == 1: # transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor('red')
        state_num = 2
     else: # transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor('green')
        state_num = 0
# bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")
wn.listen() # listen for events
wn.mainloop()

