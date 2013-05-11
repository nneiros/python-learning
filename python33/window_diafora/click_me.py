from tkinter import *
tk = Tk()
btn = Button(tk, text="Κλεισε το παραθυρο απο το [x]")
btn.pack()
def hello():
    print("Γεια σου")
from tkinter import *
tk = Tk()
btn = Button(tk, text="Πατα κλικ θα δεις κατι στην γραμμη της python", command=hello)
btn.pack()
