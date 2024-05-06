from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text='You lose!')
    myLabel.pack()

myButton =Button(root, text="Click me to win!", padx=10, pady=10, command=myClick,
                  fg="#FFFFFF", bg="blue")

myButton.pack()

root.mainloop()