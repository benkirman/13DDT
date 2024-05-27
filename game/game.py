from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import subprocess

root = Tk()
root.title("Guess the Flag")
root.iconbitmap('flag.ico')
#root.attributes('-fullscreen', True)

flags = {
    'italy.png': 'italy',
    'ukraine.png': 'ukraine',
}

current_flag = 'italy.png'

score = 0

def check_guess():
    global score
    guess = entry.get().strip().capitalize()
    if guess == flags[current_flag]:
        result_label.config(text="Correct!", fg="green")
        score += 1
    else:
        result_label.config(text="Incorrect!", fg="red")
    score_label.config(text=f"Score: {score}")

def share():
    subprocess.run(["python", "share.py"])

my_img = Image.open(current_flag)
resized = my_img.resize((500, 325), Image.LANCZOS)
new_pic = ImageTk.PhotoImage(resized)

my_label = Label(root, image=new_pic)
entry = Entry(root, font=('Arial', 14))
guess_button = Button(root, text="Guess", command=check_guess)
result_label = Label(root, text="", font=('Arial', 14))
score_label = Label(root, text=f"Score: {score}", font=('Arial', 14))
share_button = Button(root, text="Share", command=share)
exit_button = Button(root, text="Exit", command=root.destroy)

score_label.grid(row=0, column=0, columnspan=3)
my_label.grid(row=1, column=0, columnspan=3, pady=20)
entry.grid(row=2, column=0, columnspan=3)
guess_button.grid(row=3, column=1)
share_button.grid(row=3, column=0)
exit_button.grid(row=3, column=2)
result_label.grid(row=4, column=0, columnspan=3)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(1, weight=1)

root.mainloop()