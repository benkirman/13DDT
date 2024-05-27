import subprocess
from tkinter import *

top=Tk()
top.geometry("400x400")
def second():
    print("Killing First")
    top.destroy()
    subprocess.run(["python", "Second.py"])

B=Button(top, text="Go to second page", command= second)
B.pack()

top.mainloop()