#textentrybox1.py
from tkinter import*
import tkinter
#hold onto global reference fot the root window
root=None
#hold onto the text box also
entrybox=None


def buttonpushed():
    global entrybox
    txt=entrybox.get()   #to store entered text in txt variable
    print("the text is:",txt)

def createtextbox(parent): #function to create a text box
    global entrybox
    entrybox=Entry(parent)  #antrybox created
    entrybox.pack()   #packing this entrybox to the gui window

def main():
    global root
    root=Tk()   #creates the gui window
    createtextbox(root)
    myButton=Button(root,text="print the text",command=buttonpushed)
    myButton.pack()
    root.mainloop()

main()


