import turtle
wn = turtle.Screen()
#g=(input("Please enter your name: "))
#wn.title('by Nικος')
#wn.bgcolor("lightgreen")
#tess = turtle.Turtle()
#tess.shape("turtle")
#tess.color("blue")
#tess.penup() # this is new
#size = 20
#for i in range(30):
    #tess.stamp() # leave an impression on the canvas
    #size = size + 3 # increase the size on every iteration
    #tess.forward(size) # move tess along
    #tess.right(24) # and turn her
#wn.mainloop()
#turtle.setup(800,550) 
import turtle        
def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    turtle.setup(800,550)    
    #t.setposition(-20, 0)
    t.setheading(0) 
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
wn = turtle.Screen() # Set up the window and its attributes
wn.title('Ποσοστο βροχης:Δευτερα,Τριτη,Τεταρτη,Πεμπτη,Παρασκευη,Σαββατο,Κυριακη')
#x=0
#y=0
wn.bgcolor("lightgreen")
tess = turtle.Turtle() # create tess and set some attributes
tess.color("brown", "blue")
tess.pensize(2)
xs = [48,117,200,240,160,260,220]#pososto broxhs
tess.penup()
tess.setpos(-300, -200)
tess.pendown()
for a in xs:
    draw_bar(tess, a)
#wn.mainloop()
wn.exitonclick()

