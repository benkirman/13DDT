from tkinter import *

root = Tk()

myLabel1 = Label(root, text ="Hello World!")
myLabel2 = Label(root, text ="Let's do Grid!")
myLabel3 = Label(root, text ="I'm bouncing!")
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=1, column=1)

root.mainloop()