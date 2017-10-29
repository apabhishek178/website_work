#button3.py
from tkinter import *
import tkinter
root=None

def buttonpushed():
    global root
    root.destroy()

def main():
    global root
    root=Tk()
    w=Label(root,text="hello everyone!")
    w.pack()
    mybutton=Button(root,text="exit",command=buttonpushed)
    mybutton.pack()
    root.mainloop()
main()