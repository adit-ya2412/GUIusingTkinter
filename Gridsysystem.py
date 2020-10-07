from tkinter import*
root=Tk()

#creating label widget

mylabel1=Label(root,text="Hello World!")
mylabel2=Label(root,text="My name is Aditya Chaudhary , What is your name")
mylabel3=Label(root, text="").grid(row=1,column=2)#this is object class notation
#now using grid manager we push in the label
mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=5)#it is relative to other label hence if no other label presenet,it will not change.

root.mainloop()