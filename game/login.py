import sqlite3
from tkinter import *
from tkinter import messagebox
import subprocess

users = {}

def Ok():
    uname = e1.get()
    password = e2.get()
    
    if uname == "" or password == "":
        messagebox.showinfo("", "Blank Not allowed")
    elif uname in users and users[uname] == password:
        messagebox.showinfo("", "Login Success")
        root.destroy()
        subprocess.run(["python", "game.py"])
    else:
        messagebox.showinfo("", "Incorrect Username/Password")

def register():
    register_window = Toplevel(root)
    register_window.title("Sign Up")
    register_window.geometry("300x200")

    Label(register_window, text="Username").grid(row=0, column=0, padx=10, pady=10, sticky=W)
    Label(register_window, text="Password").grid(row=1, column=0, padx=10, pady=10, sticky=W)

    reg_e1 = Entry(register_window)
    reg_e1.grid(row=0, column=1)

    reg_e2 = Entry(register_window)
    reg_e2.grid(row=1, column=1)
    reg_e2.config(show="*")

    def register_user():
        reg_uname = reg_e1.get()
        reg_password = reg_e2.get()

        if reg_uname == "" or reg_password == "":
            messagebox.showinfo("", "Blank not allowed")
        elif reg_uname in users:
            messagebox.showinfo("", "This username already exists")
        else:
            users[reg_uname] = reg_password
            messagebox.showinfo("", "Sign Up Successful")
            register_window.destroy()

        Button(register_window, text="Sign Up", command=register_user, height=3, width=13).grid(row=2, column=0, columnspan=2, pady=10)

root = Tk()
root.title("Login")
root.iconbitmap("flag.ico")
#root.attributes('-fullscreen', True)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(4, weight=1)

Label(root, text="Username").grid(row=1, column=1, padx=10, pady=10, sticky=W)
Label(root, text="Password").grid(row=2, column=1, padx=10, pady=10, sticky=W)

e1 = Entry(root)
e1.grid(row=1, column=2, padx=10, pady=10)

e2 = Entry(root)
e2.grid(row=2, column=2, padx=10, pady=10)
e2.config(show="*")

Button(root, text="Login", command=Ok, height=3, width=13).grid(row=3, column=1, pady=10, padx=10)
Button(root, text="Register", command=register, height=3, width=13).grid(row=3, column=2, pady=10, padx=10)
Button(root, text="Exit", command=root.destroy, height=3, width=13).grid(row=3, column=3, pady=10, padx=10)

root.mainloop()