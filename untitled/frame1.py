from tkinter import *
import tkinter
root=tkinter.Tk()
topframe=Frame(root)
topframe.pack()
bottomframe=Frame(root)
bottomframe.pack(side=RIGHT)

button1=Button(root,text="1",fg="red",font=28)
button2=Button(root,text="2",fg="green",font=26)
button3=Button(root,text="3",fg="blue",font=24)
button4=Button(bottomframe,text="4",fg="purple",font=22)
button1.pack(side=TOP)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

root.mainloop()