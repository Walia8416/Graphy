#============================================================================
# Author: Aditya Walia 
# Github: Walia8416
#============================================================================

import tkinter as tk
from genFunc import *


def gen():

	graphGen(str(var.get()))

ffg = 'white'
win = tk.Tk() 
win.geometry("700x700")
win.resizable(False, False)
win.title("GRAPHY")

headLabel = tk.Label(win, text="GRAPH GEN")
headLabel.config(font=('Courier', 54, 'bold' ,'underline'), fg=ffg)

choiceLabel = tk.Label(win, text="Please Select Your Mode Of Operation - ")
choiceLabel.config(font=('Arial', 19,'underline' ), fg=ffg)

var = tk.IntVar()
R1 = tk.Radiobutton(win, text="LINE GRAPH", variable=var, value=1, command=gen)
R1.config(font=('Arial', 27))

R2 = tk.Radiobutton(win, text="BAR GRAPH", variable=var, value=2, command=gen)
R2.config(font=('Arial', 27))

R3 = tk.Radiobutton(win, text="PIE CHART", variable=var, value=3, command=gen)
R3.config(font=('Arial', 27))

headLabel.place(x=150, y=50)
choiceLabel.place(x=20, y=200)
R1.place(x=25, y=300)
R2.place(x=25, y=400)
R3.place(x=25, y=500)
win.mainloop()