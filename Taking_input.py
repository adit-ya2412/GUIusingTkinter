from tkinter import *
root=Tk()

e=Entry(root,width=30,bg="blue",fg="White",borderwidth=5)
#there are many parameters , this is some general
e.pack()
e.insert(0,"Your name:")#0 is  given because it indexes the box where u want to type
def myclick():
    hello=e.get()+" ,Hello there"
    mylabel=Label(root,text=hello.upper())
    mylabel.pack()

myButton= Button(root,text="Press this to display your name",state=NORMAL,padx=50,pady=30,command=myclick,fg="red",bg="#000000")#state attribute used for Disabling the button
#fg and bg is used for colouring text in box and background colour of buuton ,hexa values or names of simple colour
myButton.pack()

root.mainloop()
