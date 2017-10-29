from tkinter import *
from tkinter import messagebox
import tkinter
import os
root=tkinter.Tk()


def donothing():
    print("ohkk tata")

def add_file():
    x=input("enter the file name")
    fo = open(x,"r+")
menu1=Menu(root)
root.config(menu=menu1)

submenu=Menu(menu1)
menu1.add_cascade(label="file",menu=submenu)
submenu.add_command(label="new file",command=add_file)
submenu.add_command(label="open file",command=donothing)
submenu.add_separator()
submenu.add_command(label="exit",command=exit)

submenu=Menu(menu1)
menu1.add_cascade(label="edit",menu=submenu)
submenu.add_command(label="edit file",command=donothing)
toolbar=Frame(root)
button1=Button(toolbar,text="insert",command=donothing)
button1.pack(side=LEFT,padx=2,pady=2)
button2=Button(toolbar,text="print",command=donothing)
button2.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)

status=Label(root,text="bye bye cetpa",bd=1,relief=SUNKEN)
status.pack(side=BOTTOM,fill=X)

root.mainloop()