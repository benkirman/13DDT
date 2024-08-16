import sqlite3
from tkinter import *
from tkinter import messagebox
import subprocess

#setup of the database
conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

#function to login the user
def login_user():
    uname = e1.get()
    password = e2.get()

    if uname == "" or password == "":
        messagebox.showinfo("", "Blank Not allowed")
    else:
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (uname, password))
        result = c.fetchone()
        if result:
            messagebox.showinfo("", "Login Success")
            root.destroy()
            subprocess.run(["python", "game.py"])
        else:
            messagebox.showinfo("", "Incorrect Username/Password")

#function to register the user
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
        else:
            try:
                c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (reg_uname, reg_password))
                conn.commit()
                messagebox.showinfo("", "Sign Up Successful")
                register_window.destroy()
            except sqlite3.IntegrityError:
                messagebox.showinfo("", "This username already exists")

    Button(register_window, text="Sign Up", command=register_user, height=3, width=13).grid(row=2, column=0, columnspan=2, pady=10)

#main window setup
root = Tk()
root.title("Login")
root.iconbitmap("flag.ico")
root.attributes('-fullscreen', True)

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

Button(root, text="Login", command=login_user, height=3, width=13).grid(row=3, column=1, pady=10, padx=10)
Button(root, text="Register", command=register, height=3, width=13).grid(row=3, column=2, pady=10, padx=10)
Button(root, text="Exit", command=root.destroy, height=3, width=13).grid(row=3, column=3, pady=10, padx=10)

root.configure(bg="#E3F2FD")

root.mainloop()
conn.close()