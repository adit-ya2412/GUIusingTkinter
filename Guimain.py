from tkinter import *

root=Tk() #this is a root widget or the place where all the widgets are placed.
#creating a label widget
myLabel= Label(root,text="Hello World")
#shoving it into the screen
myLabel.pack()#it packs the widget as much the widget is

root.mainloop()