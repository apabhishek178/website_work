from tkinter import *
import random

root = Tk()
x=0
root.title("ACTION")

frame = Frame(root,background='red')
frame.pack()
canvas = Canvas(height=180,width=120)
canvas.pack()
image2 = PhotoImage(file="one.png")
canvas.create_image(0, 0,anchor='nw', image=image2)
canvas.image = image2

def roll():
    global x
    x=random.randrange(1,7)
    if(x is 1):
        canvas.delete("all")
        image1 = PhotoImage(file="one.png")
        canvas.create_image(0, 0, anchor='nw', image=image1)
        canvas.image = image1
    elif(x is 2):
        canvas.delete("all")
        image1 = PhotoImage(file="two.png")
        canvas.create_image(0, 0, anchor='nw', image=image1)
        canvas.image = image1
    elif(x is 3):
        canvas.delete("all")
        image1 = PhotoImage(file="three.png")
        canvas.create_image(0, 0, anchor='nw', image=image1)
        canvas.image = image1
    elif(x is 4):
        canvas.delete("all")
        image1 = PhotoImage(file="four.png")
        canvas.create_image(0, 0, anchor='nw', image=image1)
        canvas.image = image1
    elif(x is 5):
        canvas.delete("all")
        image1 = PhotoImage(file="five.png")
        canvas.create_image(0, 0, anchor='nw', image=image1)
        canvas.image = image1
    else:
        canvas.delete("all")
        image1 = PhotoImage(file="six.png")
        canvas.create_image(0, 0, anchor='nw', image=image1)
        canvas.image = image1

button1=Button(frame,text="roll it",width=25,fg="white",bg="black",command=roll)
button1.pack(side=RIGHT)
root.mainloop()

