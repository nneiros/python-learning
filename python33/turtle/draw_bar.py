print('*'*73)
#arithmos vroxoptosis(min,max,m.o. kai apoklisi)
import math
def rainfall ( ) :
      days = [ 'Δευ' , 'Tρι' , 'Τετ' , 'Πεμ' , 'Παρ' , 'Σαβ' , 'Κυρ' ]
      rain = [ ]
      for i in range ( 7 ) :
           r=0
           r = int(input ( 'Παρακαλω δωσε βροχοπτωση για ' + days[i] + ': ' ))
           rain.append ( r )
           #print(rain)
       # Minimum and Maximum
      minimum = rain[0]
      maximum = rain[0]
      for i in rain :
            if i < minimum : minimum = i
            if i > maximum : maximum = i
      mean = sum ( rain ) / len ( rain )
      sd = math.sqrt ( sum ( [ ( x - mean ) ** 2 for x in rain ] ) / ( len ( rain ) - 1 ) )
      # Print everything to the console
      print ('Mικροτερη βροχοπτωση αυτη την εβδομαδα:' , '#'*minimum,minimum)
      print ('Mεγαλυτερη βροχοπτωση αυτη την εβδομαδα:' ,'#'* maximum,maximum)
      print ('Mεση βροχοπτωση αυτη την εβδομαδα:' , mean)
      print ('Τυπικη αποκλιση βροχοπτωσης αυτη την εβδομαδα:' , sd)
      print('Aυτο ειναι το ραβδογραμμα με χαρακτηρες #.')
      for i in range ( len ( rain ) ) :
           print ('Βροχοπτωση για' , days[i] , '\t=\t' , '#'*rain[i],rain[i])

if __name__ == '__main__' :
      rainfall ( )
print('----------------------------------------------------------------------------------------------------')          
#import turtle
#wn = turtle.Screen()
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
days = [ 'Δευ' , 'Tρι' , 'Τετ' , 'Πεμ' , 'Παρ' , 'Σαβ' , 'Κυρ' ]
rain = [ ]
r=0
r = int(input ( 'Παρακαλω δωσε βροχοπτωση για ' + days[0] + ': ' ))
rain.append ( r )
r = int(input ( 'Παρακαλω δωσε βροχοπτωση για ' + days[1] + ': ' ))
rain.append ( r )
r = int(input ( 'Παρακαλω δωσε βροχοπτωση για ' + days[2] + ': ' ))
rain.append ( r )
r = int(input ( 'Παρακαλω δωσε βροχοπτωση για ' + days[3] + ': ' ))
rain.append ( r )
r = int(input ( 'Παρακαλω δωσε βροχοπτωση για ' + days[4] + ': ' ))
rain.append ( r )
r = int(input ( 'Παρακαλω δωσε βροχοπτωση για ' + days[5] + ': ' ))
rain.append ( r )
r = int(input ( 'Παρακαλω δωσε βροχοπτωση για ' + days[6] + ': ' ))
rain.append ( r )
print('Αυτο ειναι το ραβδογραμμα με turtles')
wn = turtle.Screen() # Set up the window and its attributes
wn.title('Ποσοστο βροχης:Δευτερα,Τριτη,Τεταρτη,Πεμπτη,Παρασκευη,Σαββατο,Κυριακη')
#x=0
#y=0
wn.bgcolor("lightgreen")
tess = turtle.Turtle() # create tess and set some attributes
tess.color("brown", "blue")
tess.pensize(2)
xs = (rain)#[48,117,200,240,160,260,220]#pososto broxhs
tess.penup()
tess.setpos(-300, -200)
tess.pendown()
for a in xs:
     draw_bar(tess, a)
#wn.mainloop()
wn.exitonclick()

