from tkinter import *
import tkinter
root=tkinter.Tk()
root.geometry("500x500+300+300")
root.title("my window")
chord=30,20,50,100

canvas1=Canvas(root,height=400,width=400,bg="blue")
canvas1.create_oval(20,20,150,300,fill="black")
canvas1.create_arc(chord,start=0,extent=90,fill="orange")
canvas1.create_rectangle(50,50,200,200,fill="brown")
canvas1.create_polygon(20,40,50,70,80,100,110,1300,fill="pink")
canvas1.pack()
root.mainloop()
