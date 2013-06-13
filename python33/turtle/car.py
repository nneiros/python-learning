import turtle
wn = turtle.Screen()
wn.title('Zωγραφιζω ενα αυτοκινητο')#ettiketa
wn.bgcolor('yellow')#xroma fontou
t = turtle.Pen()
t.reset()
t.color(1,0,0)#xroma grammis
t.begin_fill()
t.forward(200)#grammi 100 mprosta
t.left(90)
t.forward(40)#grammi 20 epano
t.left(90)
t.forward(40)#grammi 20 piso
t.right(90)
t.forward(40)#grammi 20 pano
t.left(90)
t.forward(120)#grammi 60 piso
t.left(90)
t.forward(40)#grammi 20 kato
t.right(90)
t.forward(40)#grammi 20 piso
t.left(90)
t.forward(40)#grammi 20 kato
t.end_fill()
t.color(0,0,0)#xroma rodas
t.up()
t.forward(20)#10
t.down()
t.begin_fill()
t.circle(20)#kyklos roda 1(10)
t.end_fill()
t.setheading(0)
t.up()
t.forward(180)#90
t.right(90)
t.forward(20)#10
t.setheading(0)
t.begin_fill()
t.down()
t.circle(20)#kyklos roda 2(10)
t.end_fill()
wn.exitonclick()#patao klik pontikiou kai exo exodo
