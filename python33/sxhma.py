from tkinter import *
#import random
tk = Tk()
canvas = Canvas(tk, width=400,height=400)#κυκλος
canvas.pack()
canvas.create_oval(1, 1, 300, 300)

tk = Tk()
canvas = Canvas(tk, width=400,height=400)#ελειψη μεσα σε παρ/μο κοκκινο
canvas.pack()
canvas.create_oval(1, 1, 300, 200)
canvas.create_rectangle(2, 2, 300, 200, outline="#ff0000")#f902c4 ροζ

tk = Tk()
canvas = Canvas(tk, width=400,height=400)
canvas.pack()
canvas.create_arc(10, 10, 200, 80, extent=45, style=ARC)#τοξα διαφορα
canvas.create_arc(10, 80, 200, 160, extent=90, style=ARC)
canvas.create_arc(10, 160, 200, 240, extent=135, style=ARC)
canvas.create_arc(10, 240, 200, 320, extent=180, style=ARC)
canvas.create_arc(10, 320, 200, 400, extent=359, style=ARC)

tk = Tk()
canvas = Canvas(tk, width=400,height=400)
canvas.pack()
canvas.create_arc(10, 10, 200, 100, extent=180, style=ARC)#τοξο σκετο
canvas.create_rectangle(2, 2, 300, 200, outline="#ff0000")#f902c4 ροζ

#from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400,height=400)
canvas.pack()
canvas.create_rectangle(10, 10, 50, 50)#τετραγωνο

canvas.create_rectangle(100, 100, 300, 50)#παρ/μο οριζοντιο

canvas.create_rectangle(100, 200, 150, 350)#παρ/μο κατακορυφο


