from tkinter import *
from tkinter import messagebox
import tkinter


class Login(Frame):
    def __init__(self,master):
        super().__init__(master)


        self.l1=Label(self,text="username")
        self.e1=Entry(self)
        self.l2=Label(self,text="password")
        self.e2=Entry(self,show="*")
        self.c1=Checkbutton(self,text="keep me logged in")
        self.l1.grid(row=0)
        self.e1.grid(row=0,column=1)
        self.l2.grid(row=2)
        self.e2.grid(row=2,column=1)
        self.c1.grid(row=3,column=0)
        b1=Button(self,text="login",command=self.loginin)
        b1.grid(columnspan=2) #for tab sapce in column
        self.pack()

    def loginin(self):

        user=self.e1.get()
        password=self.e2.get()

        if(user=="apabhishek178" and password=="abhi1234"):
            messagebox.showinfo("welcome","hey abhishek")
        elif(user=="akanshi1234" and password=="1234"):
            messagebox.showinfo("welcome","hey bataku")
        else:
            messagebox.showinfo("error","wrong username or password")

root=tkinter.Tk()
self=Login(root)
root.mainloop()