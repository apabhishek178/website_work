from tkinter import *
from tkinter import messagebox
import mysql.connector
import tkinter


top = tkinter.Tk()
top.title("my new gui")
top.geometry("1080x720")
top['bg'] = 'powderblue'
one=PhotoImage(file="one.png")
two=PhotoImage(file="two.png")
three=PhotoImage(file="three.png")
four=PhotoImage(file="four.png")


def clickone():
    db1 = mysql.connector.connect(host="",database="test",
                                 user="root",
                                 password="1234")
    cursor1 = db1.cursor()
    m1 = messagebox.askyesno(title="clickone",message="wanna change to on")
    if m1 is True:
        messagebox.showinfo(title="status",message="changed")
        cmd1 = "UPDATE appliance set status=\"on\" WHERE item_id=101"
        cursor1.execute(cmd1)
        print("value is changed")
        db1.commit()
        cursor1.close()
        db1.close()
    else:
        messagebox.showinfo(title="status", message=" not changed")
        cmd1 = "UPDATE set table_name status=\"not done\" WHERE id="
        cursor1.execute(cmd1)
        print("value is not changed")
        db1.commit()
        cursor1.close()
        db1.close()
b1 = Button(top,text = "bulb",bg ='grey',fg = "white",font = "times",command = clickone)
b1.pack()
top.mainloop()

