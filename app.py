import tkinter as tk
from tkinter import ttk


count = 0

def reset():
    global count
    

    count = 0

    label1.configure(text=f' {count} E s')

def clicked(): # without event because I use `command=` instead of `bind`
    global count

    count = count + 1

    label1.configure(text=f' {count} E s ')




    if count == 21:

        label= tk.Label(windows, text="Advancment: haha meme go brrrrrr (get to 21 E s")
        label.grid(column=0, row=2)

    if count == 100:
        label= tk.Label(windows, text="Advancment: a master upon E s (get to 100 E s")
        label.grid(column=0, row=3)

    if count == 1000:
        label= tk.Label(windows, text="Advancment: wow you actually made it this far? (get to 1000 E s")
        label.grid(column=0, row=4)


windows = tk.Tk()
windows.title("E Clicker")

label = tk.Label(windows, text="E Clicker")
label.grid(column=0, row=0)

label1 = tk.Label(windows)
label1.grid(column=0, row=1)

plusE = ttk.Button(windows, text="Add 1 E", command=clicked)
plusE.grid(column=1, row=0)

resetbutt = ttk.Button(windows, text="Reset Counter", command=reset)
resetbutt.grid(column=1, row=1)

windows.mainloop()
