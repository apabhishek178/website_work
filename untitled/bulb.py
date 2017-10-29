from tkinter import *
import tkinter
root=tkinter.Tk()
root.geometry("600x600+300+400")
root.title("bulb action")
#pic1=PhotoImage(file="bulbon.png")
#pic2=PhotoImage(file="bulboff.png")
x=0

def switch():
    global x
    pic1 = PhotoImage(file='bulbon.png')
    pic2 = PhotoImage(file='bulboff.png')
    if(x%2 is 0):
        pane1=Label(root,image=pic1)
    else:
        pane1 = Label(root, image=pic2)
    pane1.pack()
    x+=1
b1=Button(root,text="push",bg="green",fg="white",command=switch,bd=10,relief=SUNKEN,font=('times new roman',20),height=1,width=1)
b1.pack()

root.mainloop()