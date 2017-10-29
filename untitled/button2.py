#button2.py
import tkinter
from tkinter import *
def buttonpushed():
    print("button is pushed")
root=Tk()
w=Label(root,text="hello everyone")
w.pack()
mybutton=Button(root,text="push it",command=buttonpushed)
mybutton.pack()
root.mainloop()