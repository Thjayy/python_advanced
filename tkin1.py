import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()

root.geometry('500x500')
def sleepfunc():
    time.sleep(5)
    lab['text'] = "Run qilishdan keyin"
btn = ttk.Button(root, text="Run", command=sleepfunc)
btn.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

lab = ttk.Label(root, text="Run qilishdan oldin")
lab.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


root.mainloop()