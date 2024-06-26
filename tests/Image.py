from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to get images")
root.iconbitmap('Flag.ico')

my_img = Image.open('vikram.jpg')
resized = my_img.resize((300, 225),Image.LANCZOS)
new_pic = ImageTk.PhotoImage(resized)

my_label = Label(root, image= new_pic)
my_label.pack(pady=20)

button_exit = Button(root, text="Exit program", command=root.quit)
button_exit.pack()

root.mainloop()