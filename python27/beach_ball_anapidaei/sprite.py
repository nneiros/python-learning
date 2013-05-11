#n = input("Please enter your name: ")
import turtle
#wn = turtle.Screen()
#wn.bgcolor("lightgreen")
#tess = turtle.Turtle()
#tess.shape("turtle")
#tess.color("blue")
#tess.penup() # this is new
#size = 20
#for i in range(30):
#    tess.stamp() # leave an impression on the canvas
#    size = size + 3 # increase the size on every iteration
#    tess.forward(size) # move tess along
#    tess.right(24) # and turn her
#wn.mainloop()
#turtle.setup(400,500) 
def draw_bar(t, height):
#""" Get turtle t to draw one bar, of height. """

    t.begin_fill() # added this line
    t.left(90)
    t.forward(height)
    t.write('  '+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill() # added this line
    t.forward(10)
wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")
tess = turtle.Turtle() # create tess and set some attributes
tess.color("blue", "red")
tess.pensize(2)
xs = [48,117,200,240,160,260,220]
for a in xs:
    draw_bar(tess, a)
wn.mainloop()

#import turtle
#turtle.setup(400,500) # determine the window size
#wn = turtle.Screen() # get a reference to the window
#wn.title("Handling keypresses!") # Change the window title
#wn.bgcolor("lightgreen") # Set the background color
#tess = turtle.Turtle() # Create our favorite turtle
# The next four functions are our "event handlers".
#def h1():
#     tess.forward(30)
#def h2():
#     tess.left(45)
#def h3():
#     tess.right(45)
#def h4():
#     wn.bye() # Close down the turtle window
# These lines "wire up" keypresses to the handlers we've defined.
#wn.onkey(h1, "Up")
#wn.onkey(h2, "Left")
#wn.onkey(h3, "Right")
#wn.onkey(h4, "q")
# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
#wn.listen()
#wn.mainloop()
