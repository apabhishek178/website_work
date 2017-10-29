from tkinter import *

root = Tk()
x = 0
root.title("ACTION")

frame = Frame(root,background='red')
frame.pack()
canvas = Canvas(height=500,width=450,)
canvas.pack()
image2 = PhotoImage(file="bulboff.png")
canvas.create_image(0, 0, anchor='nw', image=image2)
canvas.image = image2
def bulb():
    global x
    if(x%2 is 0):
        canvas.delete("all")
        image1 = PhotoImage(file="bulbon.png")
        canvas.create_image(0, 0, anchor='nw', image=image1)
        canvas.image = image1
        x+=1
    else:
        canvas.delete("all")
        image1 = PhotoImage(file="bulboff.png")
        canvas.create_image(0, 0, anchor='nw', image=image1)
        canvas.image = image1
        x+=1
button1=Button(frame,text="push",width=25,fg="white",bg="black",command=bulb)
button1.pack(side=RIGHT)
root.mainloop()
