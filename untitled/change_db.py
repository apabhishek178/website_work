from tkinter import *
from tkinter import messagebox
import mysql.connector
import tkinter

root = tkinter.Tk()
root.geometry("400x400")
root.title("database")

db = mysql.connector.connect(host="",user="root",password="",database="")


def click():
    cmd = "update appliance set status ='off' where name = 'bulb'"
b1=Button(root,text="cetpa",command=click)
root.mainloop()