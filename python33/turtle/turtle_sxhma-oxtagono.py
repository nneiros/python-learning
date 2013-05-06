import turtle
t = turtle.Pen()
#t.forward(50)# οχταγωνο σκετο μαυρο
#t.right(45)
#t.forward(50)
#t.right(45)
#t.forward(50)
#t.right(45)
#t.forward(50)
#t.right(45)
#t.forward(50)
#t.right(45)
#t.forward(50)
#t.right(45)
#t.forward(50)
#t.right(45)
#t.forward(50)
def octagon(red, green, blue):#οχταγωνο βαμμενο μπλε
      t.color(red, green, blue)
      t.begin_fill()
      for x in range(0,8):
           t.forward(50)
           t.right(45)
      t.end_fill()
octagon(0, 0, 1)


