from tkinter import *
import random
tk = Tk()
tk.title('Διαφoρα τριγωνα τυχαια')
canvas = Canvas(tk, width=600, height=500)
canvas.pack()
colors = ['red','green','blue','yellow','orange','white','purple']
def random_triangle():
    p1 = random.randrange(600)
    p2 = random.randrange(500)
    p3 = random.randrange(600)
    p4 = random.randrange(500)
    p5 = random.randrange(600)
    p6 = random.randrange(500)
    color = random.choice(colors)
    canvas.create_polygon(p1, p2, p3, p4, p5, p6, \
                fill=color, outline="")
for x in range(0, 100):
     random_triangle()
