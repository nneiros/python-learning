from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)#κατασκευη παραθυρου
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)#κατασκευη τριγωνου
def movetriangle(event):
    if event.keysym == "Up":#κινηση τριγωνου,πανω,κατω,δεξια,αριστερα
        canvas.move(1, 0, -3)
    elif event.keysym == "Down":
        canvas.move(1, 0, 3)
    elif event.keysym == "Left":
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)
  
canvas.bind_all("<KeyPress-Up>", movetriangle)
canvas.bind_all("<KeyPress-Down>", movetriangle)
canvas.bind_all("<KeyPress-Left>", movetriangle)
canvas.bind_all("<KeyPress-Right>", movetriangle)
