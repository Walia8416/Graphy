#============================================================================
# Author: Aditya Walia 
# Github: Walia8416
#============================================================================

import tkinter as tk
from tkinter import ttk

class TableGen:

	def __init__(self,choice,l1,l2):

		self.choice = choice

		tab = tk.Tk()
		tab.geometry("400x400")
		tab.title("Your Data")
		tab.resizable(False, False)

		Dtable = ttk.Treeview(tab, selectmode='browse')
		Dtable.place(x=20, y= 100)

		verscrlbar = ttk.Scrollbar(tab, orient='vertical', command=Dtable.yview)
		verscrlbar.place(x=10, y=100, height=220)

		Dtable.configure(xscrollcommand = verscrlbar.set)
		Dtable["columns"] = ("1", "2")
		Dtable['show'] = 'headings'

		Dtable.column("1", width=170, anchor='c')
		Dtable.column("2", width=170, anchor='c')
		if choice=='1':
			Dtable.heading("1", text="X-Coordinate")
			Dtable.heading("2", text="Y-Coordinate")

		else:
			Dtable.heading("1", text="Item")
			Dtable.heading("2", text="Value")



		for i in range(len(l1)):
			Dtable.insert("", 'end', text="L1", values=(l1[i], l2[i]))

		tab.mainloop() 
