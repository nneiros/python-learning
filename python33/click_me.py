from tkinter import *
tk = Tk()
btn = Button(tk, text="κλεισε το παραθυρο απο το [χ]")
btn.pack()
def hello():
    print("γεια σου")
from tkinter import *
tk = Tk()
btn = Button(tk, text="πατα κλικ θα δεις κατι στην γραμμη της python", command=hello)
btn.pack()
