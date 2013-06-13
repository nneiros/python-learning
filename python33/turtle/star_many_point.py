import turtle
wn = turtle.Screen()
wn.title('Κατασκευη 1.αστεριου,2.πολυαστεριου.3.πολυτετραγωνου')
wn.bgcolor()
t = turtle.Pen()
t.color(1, 0, 0)
for x in range(1,9):
     t.forward(100)
     t.left(225)
t.reset()

t.color(1, 0.85, 0)
for x in range(1,38):
     t.forward(100)
     t.left(175)
t.reset()

t.color(1, 0.85, 0)
for x in range(1,20):
     t.forward(100)
     t.left(95)
wn.exitonclick()     
