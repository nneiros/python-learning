import turtle
wn = turtle.Screen()
wn.title('Κατασκευη τριγωνου')
wn.bgcolor('lightgreen')
t = turtle.Pen()# αρχη τριγωνου
t.forward(100)
t.left(135)
t.forward(70)
t.left(90)
t.forward(70)
wn.exitonclick()
import turtle
wn = turtle.Screen()
wn.title('Κατασκευη παραλληλογραμμου')
wn.bgcolor('lightgreen')
t = turtle.Pen()# αρχη παραλληλογραμμου
t.forward(150)
t.left(90)
t.forward(50)
t.left(90)
t.forward(150)
t.left(90)
t.forward(50)
wn.exitonclick()
for x in range(0, 20):# για σου
    print("για σου %s" % x)
    if x < 9:
        break

first_name = "τζειμς"
second_name = "μποντ"
print("το ονομα μου ειναι %s %s" % (first_name, second_name))
