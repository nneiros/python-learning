#parathiro tkinter
from tkinter import *

class AppUI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master, relief=SUNKEN, bd=2)

        self.menubar = Menu(self)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Aρχειο", menu=menu)
        menu.add_command(label="Nεο")

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Διορθωσε", menu=menu)
        menu.add_command(label="Κοψε")
        menu.add_command(label="Αντιγραφο")
        menu.add_command(label="Επικολληση")

        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            # master is a toplevel window (Python 1.4/Tkinter 1.63)
            self.master.tk.call(master, "config", "-menu", self.menubar)

        self.canvas = Canvas(self, bg="white", width=400, height=400,
                             bd=0, highlightthickness=0)
        self.canvas.pack()


root = Tk()

app = AppUI(root)
app.pack()

root.mainloop()
#------------------------------------------------------------------------------------------
#parathiro me skala rithmisis
from tkinter import *
master = Tk()
w = Scale(master, from_=0, to=100)
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
mainloop()
#----------------------------------------------------------------------------------------------
#parathiri me skala rithmisis
from tkinter import *

def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)

root = Tk()
var = DoubleVar()
scale = Scale( root, variable = var )
scale.pack(anchor=CENTER)

button = Button(root, text="Get Scale Value", command=sel)
button.pack(anchor=CENTER)

label = Label(root)
label.pack()

root.mainloop()
#------------------------------------------------------------------------------------------------
#roloi parathiro
import sys    
from tkinter import *
import time

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
    clock.after(200, tick)

root = Tk()
time1 = ''

status = Label(root, text="Νικος", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=0, column=0)

clock = Label(root, font=('times', 20, 'bold'), bg='green')
clock.grid(row=0, column=1) 

tick()
root.mainloop()
#--------------------------------------------------------------------------------------
import tkinter as tk

board = [ [None]*10 for _ in range(10) ]

counter = 0

root = tk.Tk()

def on_click(i,j,event):
    global counter
    color = "red" if counter%2 else "black"
    event.widget.config(bg=color)
    board[i][j] = color
    counter += 1


for i,row in enumerate(board):
    for j,column in enumerate(row):
        L = tk.Label(root,text='    ',bg='grey')
        L.grid(row=i,column=j)
        L.bind('<Button-1>',lambda e,i=i,j=j: on_click(i,j,e))

root.mainloop()
#---------------------------------------------------------------------------
print('----------------------------------------------------------------------')

from tkinter import *

class ClearApp:
    def __init__(self, parent=0):
       self.mainWindow = Frame(parent)
       self.percentbar = Canvas(self.mainWindow)
       self.percentbar.config(height=10, width=100, bg='black')
       self.percentbar.create_line(0, 6, 0, 6, fill='red', width = 3, 
tag='bar')
       self.percentbar.pack()
       fOuter = Frame(self.mainWindow, border=1, relief="sunken")
       fButtons = Frame(fOuter, border=1, relief="raised")
       bDraw = Button(fButtons, text="Draw Bar",
                       width=8, height=1, command=self.drawBar)
       bQuit = Button(fButtons, text="Quit",
                       width=8, height=1, command=self.mainWindow.quit)
       bDraw.pack(side="left", padx=15, pady=1)
       bQuit.pack(side="right", padx=15, pady=1)
       fButtons.pack(fill=X)
       fOuter.pack(fill=X)
       self.mainWindow.pack()
       self.mainWindow.master.title("Percent bar")

    def drawBar(self):
       global x
       if x < 100 : x = x+10
       app.percentbar.coords('bar', 0, 6, x, 6)

app = ClearApp()
x = 0
app.mainWindow.mainloop()
#---------------------------------------------------------------------------
print('----------------------------------------------------------------------') 
#kikloi diaforoi
from tkinter import *
root = Tk()
def drawcircle(canv,x,y,rad):
    canv.create_oval(x-rad,y-rad,x+rad,y+rad,width=0,fill='blue')
canvas = Canvas(width=600, height=200, bg='white')  
canvas.pack(expand=YES, fill=BOTH) 
text = canvas.create_text(50,10, text="tk test")
#i'd like to recalculate these coordinates every frame
circ1=drawcircle(canvas,100,50,10)#[deksia,aristera],[pano,kato],aktina          
circ2=drawcircle(canvas,500,100,20)
circ3=drawcircle(canvas,200,100,20)
circ3=drawcircle(canvas,300,100,20)
root.mainloop()
#---------------------------------------------------------------------------
print('----------------------------------------------------------------------')
#website: www.zetcode.com
#parathiro me submenou
from tkinter import Tk, Frame, Menu

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Submenu")
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        fileMenu = Menu(menubar)       
        
        submenu = Menu(fileMenu)
        submenu.add_command(label="New feed")
        submenu.add_command(label="Bookmarks")
        submenu.add_command(label="Mail")
        fileMenu.add_cascade(label='Import', menu=submenu, underline=0)
        
        fileMenu.add_separator()
        
        fileMenu.add_command(label="Exit", underline=0, command=self.onExit)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)        
                
    def onExit(self):
        self.quit()

def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  
#---------------------------------------------------------------------------
print('----------------------------------------------------------------------')

from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Shapes")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_oval(10, 10, 80, 80, outline="red", 
            fill="green", width=2)
        canvas.create_oval(110, 10, 210, 80, outline="#f11", 
            fill="#1f1", width=2)
        canvas.create_rectangle(230, 10, 290, 60, 
            outline="#f11", fill="#1f1", width=2)
        canvas.create_arc(30, 200, 90, 100, start=0, 
            extent=210, outline="#f11", fill="#1f1", width=2)
            
        points = [150, 100, 200, 120, 240, 180, 210, 
            200, 150, 150, 100, 200]
        canvas.create_polygon(points, outline='red', 
            fill='green', width=2)
        
        canvas.pack(fill=BOTH, expand=1)

def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("330x220+300+300")
    root.mainloop()  

if __name__ == '__main__':
    main() 
#---------------------------------------------------------------------------
print('----------------------------------------------------------------------')
#parathiro me stixous
from tkinter import Tk, Canvas, Frame, BOTH, W

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Lyrics")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_text(20, 30, anchor=W, font="Purisa",
            text="Most relationships seem so transitory")
        canvas.create_text(20, 60, anchor=W, font="Purisa",
            text="They're good but not the permanent one")
        canvas.create_text(20, 130, anchor=W, font="Purisa",
            text="Who doesn't long for someone to hold")
        canvas.create_text(20, 160, anchor=W, font="Purisa",
            text="Who knows how to love without being told")                   
        canvas.create_text(20, 190, anchor=W, font="Purisa",
            text="Somebody tell me why I'm on my own")            
        canvas.create_text(20, 220, anchor=W, font="Purisa",
            text="If there's a soulmate for everyone")               
        canvas.pack(fill=BOTH, expand=1)

def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("420x250+300+300")
    root.mainloop()  

if __name__ == '__main__':
    main() 
#---------------------------------------------------------------------------
print('----------------------------------------------------------------------')
#parathira me titlous
from tkinter import*
msg=Message(text='Oh by the way, which one`s Pink?')
msg.config(bg='pink',font=('times',16,'italic'))
msg.pack(fill=X,expand=YES)
mainloop()

import tkinter

def goPush():
    win2=tkinter.Toplevel()
    win2.geometry('400x50')
    tkinter.Label(win2,text="If you have prepared as Help describes select Go otherwise select Go Back").pack()
    tkinter.Button(win2,text="Go",command=bounceProg).pack(side=tkinter.RIGHT,padx=5)
    tkinter.Button(win2, text="Go Back", command=win2.destroy).pack(side=tkinter.RIGHT)

def bounceProg():
    d=1
    print (d)
root=tkinter.Tk()
root.geometry('500x100')
tkinter.Button(text='Go', command=goPush).pack(side=tkinter.RIGHT,ipadx=50)
root.mainloop()

import tkinter as tk

class MyToplevel(tk.Toplevel):
    def __init__(self, title="hello, world", command=None):
        tk.Toplevel.__init__(self)
        self.wm_title(title)
        button = tk.Button(self, text="OK", command=lambda toplevel=self: command(toplevel))
        button.pack()

if __name__ == "__main__":
    def go(top):
        print ("my work here is done")
        top.destroy()

    app = tk.Tk()
    t = MyToplevel(command=go)
    t.wm_deiconify()
    app.mainloop()
#---------------------------------------------------------------------------
print('----------------------------------------------------------------------')
#ravdogramma mple
import tkinter as tk
def graph_points(seq, width=375, height=325):
    root = tk.Tk()
    c = tk.Canvas(root, width=width, height=height, bg='lightgreen')
    c.pack()
    y_stretch = 15
    y_gap = 20
    x_stretch = 10
    x_width = 20
    x_gap = 20
    for x, y in enumerate(data):
        x0 = x * x_stretch + x * x_width + x_gap
        y0 = height - (y * y_stretch + y_gap)
        x1 = x * x_stretch + x * x_width + x_width + x_gap
        y1 = height - y_gap
        c.create_rectangle(x0, y0, x1, y1, fill="blue")
        c.create_text(x0+2, y0, anchor=tk.SW, text=str(y))
    root.mainloop()

data = (18, 15, 10, 7, 5, 4, 2, 5, 8, 10, 13)
graph_points(data)
#---------------------------------------------------------------------------
print('----------------------------------------------------------------------')
#raketa games
from tkinter import *
import random
import time
class Ball:
      def __init__(self, canvas, paddle, score, color):
           self.canvas = canvas
           self.paddle = paddle
           self.score = score
           self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
           self.canvas.move(self.id, 245, 100)
           starts = [-3, -2, -1, 1, 2, 3]
           random.shuffle(starts)
           self.x = starts[0]
           self.y = -3
           self.canvas_height = self.canvas.winfo_height()
           self.canvas_width = self.canvas.winfo_width()
           self.hit_bottom = False
      def hit_paddle(self, pos):
           paddle_pos = self.canvas.coords(self.paddle.id)
           if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                    self.x += self.paddle.x
                    self.score.hit()
                    return True
           return False
      def draw(self):
           self.canvas.move(self.id, self.x, self.y)
           pos = self.canvas.coords(self.id)
           if pos[1] <= 0:
               self.y = 3
           if pos[3] >= self.canvas_height:
               self.hit_bottom = True
           if self.hit_paddle(pos) == True:
               self.y = -3
           if pos[0] <= 0:
               self.x = 3
           if pos[2] >= self.canvas_width:
               self.x = -3
class Paddle:
      def __init__(self, canvas, color):
           self.canvas = canvas
           self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
           self.canvas.move(self.id, 200, 300)
           self.x = 0
           self.canvas_width = self.canvas.winfo_width()
           self.started = False
           self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
           self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
           self.canvas.bind_all('<Button-1>', self.start_game)
      def draw(self):
            self.canvas.move(self.id, self.x, 0)
            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.x = 0
            elif pos[2] >= self.canvas_width:
                self.x = 0
      def turn_left(self, evt):
           self.x = -2
      def turn_right(self, evt):
           self.x = 2
      def start_game(self, evt):
           self.started = True
class Score:
      def __init__(self, canvas, color):
           self.score = 0
           self.canvas = canvas
           self.id = canvas.create_text(450, 10, text=self.score, \
                     fill=color)
      def hit(self):
            self.score += 1
            self.canvas.itemconfig(self.id, text=self.score)
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
score = Score(canvas, 'green')
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, score, 'red')
game_over_text = canvas.create_text(250, 200, text='GAME OVER', \
              state='hidden')
while 1:
      if ball.hit_bottom == False and paddle.started == True:
          ball.draw()
          paddle.draw()
      if ball.hit_bottom == True:
          time.sleep(1)
          canvas.itemconfig(game_over_text, state='normal')
      tk.update_idletasks()
      tk.update()
      time.sleep(0.01)
root.mainloop()

