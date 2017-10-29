from tkinter import *
import tkinter
root=tkinter.Tk()
root.geometry("600x600+300+400")
root.title("welcome")
pic=PhotoImage(file="abc.png")
def click():
    print("byee byee tata")
b1=Button(root,bg="green",fg="white",command=click,bd=10,relief=SUNKEN,font=('times new roman',20),height=300,width=300,image=pic)
b1.pack()

root.mainloop()

