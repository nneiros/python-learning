import time
from tkinter import *
tk = Tk()
tk.title('Mετακινηση φωτογραφιας')
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
myimage = PhotoImage(file='face.gif')
canvas.create_image(0, 0, anchor=NW, image=myimage)
for x in range(0, 10):
    canvas.move(1, 10, 10)
    tk.update()
    time.sleep(0.1)#0.05
