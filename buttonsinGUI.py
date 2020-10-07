from tkinter import *
root=Tk()
def myclick():
    mylabel=Label(root,text="I TOLD U NOT TO CLICK :(")
    mylabel.pack()

myButton= Button(root,text="Do not Click me!",state=NORMAL,padx=50,pady=30,command=myclick,fg="red",bg="#000000")#state attribute maybe used for Disabling the button
#fg and bg is used for colouring text in box and background colour of buuton ,hexa values or names of simple colour
myButton.pack()

root.mainloop()