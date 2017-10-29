from tkinter import *
from tkinter import messagebox
import mysql.connector
import tkinter
top=tkinter.Tk()
top.title("my first database connector")
top.geometry("1080x720")
top['bg']="powder blue"
bulbonn=PhotoImage(file="bulbon.png")
bulbof=PhotoImage(file="bulboff.png")
dice=PhotoImage(file="wtf.png")

def bulbclick():
    db2 = mysql.connector.connect(host="",database="device",user="root",password="nanmol890",)
    cursor1=db2.cursor()
    x=messagebox.askyesorno(title="bulb",message="wanna glow the bulb")
    if (x==True):
        messagebox.showinfo(title="bulb", message="bulb has glown")
        cmd="UPDATE deviceinfo set status=\"on\"where id="
        cursor1.execute(cmd)
        print("bulb is on")
        db2.commit()
        cursor1.close()
        db2.close()

    else:
        messagebox.showinfo(title="bulb", message="bulb is switched off")
        cmd = "UPDATE deviceinfo set status=\"off\"where id="
        cursor1.execute(cmd)
        print("bulb is off")
        db2.commit()
        cursor1.close()
        db2.close()
        b1=Button(top,text='HELLO',bg="blue",fg="red",font=('arial',25),bd=10,relief=GROOVE,command=bulbclick)
        b1.pack(side="TOP")
        top.mainloop()