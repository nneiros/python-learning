
#programma gia kataskevi bar=48,117,200,240,160,260,220
import turtle
def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.setheading(90)            # face the turtle up
    t.begin_fill()
    t.forward(height)           # draw up the left side
    t.write('  ' + str(height)) # write the value at the top of the bar
    t.right(90)
    t.forward(40)               # width of bar, along the top
    t.right(90)
    t.forward(height)           # down again!
    t.end_fill()

wn = turtle.Screen()
wn.title('Κατασκευη γραφηματος')
wn.bgcolor('lightgreen')
tess = turtle.Turtle()
tess.color('blue','red')
values = [48, 117, 400, 240, 160, 260, 220,90,15,321]

tess.penup()
tess.setpos(-300, -200)
tess.pendown()

for value in values:
    draw_bar(tess, value)

wn.exitonclick()
#-----------------------------------------------------------------------------------------------------------------------
#kataskevi 4 tetragonon apo 4 xelones(roz,mavro,kitrino,kokkino)
import turtle
def make_window(color, title):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    turtle.setup(800, 600)
    w = turtle.Screen()
    w.bgcolor(color)
    w.title('4 Χελωνακια=4 χρωματα=4 τετραγωνα')
    return w

def make_turtle(color, size, shape):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    t.shape(shape)
    return t

def draw_square(t, size, x, y):
    """
      Use turtle, t, to draw a square of size, size, starting with a lower
      left hand corner at x, y.  Returns the turtle to its previous state
      after drawing the square.
    """
    # Store the location and direction of the turtle
    tx = t.xcor()
    ty = t.ycor()
    th = t.heading()

    # Move the turtle to lower left corner of square facing East (heading 0)
    t.penup()
    t.setpos(x, y)
    t.setheading(0)
    t.pendown()

    # Draw the square
    for i in range(4):
        t.forward(size)
        t.left(90)

    # Return turtle to original location and direction
    t.penup()
    t.setpos(tx, ty)
    t.setheading(th)


wn = make_window("lightgreen", "Tess, Alex, Dave, and Jaunice")

tess = make_turtle("hotpink", 5, "arrow")
alex = make_turtle("black", 1, "turtle")
dave = make_turtle("yellow", 2, "circle")
jaunice = make_turtle("red", 3, "triangle")

draw_square(tess, 50, -225, 125)
draw_square(alex, 100, 150, 100)
draw_square(dave, 200, -300, -250)
draw_square(jaunice, 150, 125, -225)
wn.exitonclick()
#----------------------------------------------------------------------------------------------------------------------------
#kataskevi polaplon sinexomenon tetragonon se morfi saligarou.
import turtle
def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-color square of sz."""
    for c in ['red', 'purple', 'hotpink', 'blue']:
        t.color(c)
        t.forward(sz)
        t.left(90)

# Set up the window and its attributes
turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title('Kατασκευη πολυτετραγωνων σε σπειρα')

# create tess and set some attributes
tess = turtle.Turtle()
tess.pensize(3)

size = 20                        # size of the smallest square
for i in range(25):
    draw_multicolor_square(tess, size)
    size = size + 10             # increase the size for next time
    tess.forward(10)             # move tess along a little
    tess.right(18)               # and give her some extra turn

wn.exitonclick()
#-------------------------------------------------------------------------------------------------------------------------------

