import turtle
wn = turtle.Screen()
wn.title('Κατασκευη αστεριου κιτρινου με κοκκινη γραμμη')
wn.bgcolor('lightgreen')
t = turtle.Pen()
t.reset()
def mystar(size, filled):
      if filled:
          t.begin_fill()
      for x in range(1,19):
            t.forward(size)
            if x % 2 == 0:
                 t.left(175)
            else:
                  t.left(225)
      if filled:
           t.end_fill()
t.color(1, 0.85, 0)
mystar(120, True)
t.color(1, 0, 0)
mystar(120, False)
wn.exitonclick()
