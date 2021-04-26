#============================================================================
# Author: Aditya Walia 
# Github: Walia8416
#============================================================================

import tkinter as tk
from treeView import *
import matplotlib.pyplot as plt

def graphGen(sel):
	coordinatesX = []
	coordinatesY = []

	def enterRow():
		if sel == '1':
			coordinatesX.append(int(xcEntry.get()))
			coordinatesY.append(int(ycEntry.get()))

		else:
			coordinatesX.append(xcEntry.get())
			coordinatesY.append(int(ycEntry.get()))


		ycEntry.delete(0, 'end')
		xcEntry.delete(0, 'end')

	def viewData():
		tt = TableGen(sel, coordinatesX, coordinatesY)

	def generate():

		if (len(coordinatesX) < 1):
			tk.messagebox.showerror("Error", "Please Enter Data Before Generating")

		else:
			
			if sel == '1':
				plt.xlabel(xEntry.get())
				plt.ylabel(yEntry.get())
				plt.title(tEntry.get())
				plt.plot(coordinatesX, coordinatesY)

			elif  sel == '2':
				plt.xlabel(xEntry.get())
				plt.ylabel(yEntry.get())
				plt.title(tEntry.get())
				plt.bar(coordinatesX, coordinatesY)
				
			elif  sel == '3':
				a = tEntry.get()
				plt.title(a)
				plt.pie(coordinatesY, labels=coordinatesX, autopct='%1.1f%%')
				plt.legend(coordinatesX, title=a, loc="lower right", bbox_to_anchor=(1,0), bbox_transform=plt.gcf().transFigure)
				
			coordinatesY.clear()
			coordinatesX.clear()
			xEntry.delete(0, 'end')
			yEntry.delete(0, 'end')
			tEntry.delete(0, 'end')
			winG.destroy()
			plt.show()

	winG = tk.Tk()
	winG.geometry("700x550")
	winG.resizable(False, False)
	
	headLab = tk.Label(winG, text="DATA ENTRY")
	headLab.config(font=('Arial', 30, 'underline', 'bold'))


	xaxis = tk.StringVar()
	yaxis = tk.StringVar()
	titl = tk.StringVar()
	xC = tk.StringVar()
	yC = tk.StringVar()


	winG.title("LINE GRAPH")
	xLab = tk.Label(winG, text="X-Axis Name:")
	xLab.config(font=('Arial', 18))
	xLab.place(x=10, y=150)

	xEntry = tk.Entry(winG, bd=2, textvariable=xaxis)
	xEntry.place(x=170, y=155)
	
	yLab = tk.Label(winG, text="Y-Axis Name:")
	yLab.config(font=('Arial', 18))
	yLab.place(x=360, y=150)

	yEntry = tk.Entry(winG, bd=2, textvariable=yaxis)
	yEntry.place(x=520, y=155)

	title = tk.Label(winG, text="Title:")
	title.config(font=('Arial', 18))
	title.place(x=10, y=250)

	tEntry = tk.Entry(winG, bd=2, textvariable=titl)
	tEntry.place(x=70, y=253)

	xCoor = tk.Label(winG)
	xCoor.config(font=('Arial', 18))
	
	xcEntry = tk.Entry(winG, bd=2, textvariable=xC, width=5)
	
	yCoor = tk.Label(winG)
	yCoor.config(font=('Arial', 18))
	
	ycEntry = tk.Entry(winG, bd=2, textvariable=yC, width=5)

	enter = tk.Button(winG, text="Enter", command=enterRow, width=10)
	enter.config(font=('Arial, 12'))
	enter.place(x=450, y=355)

	view = tk.Button(winG, text="View Data", command=viewData, width=10)
	view.config(font=('Arial, 12'))
	view.place(x=50, y=455)

	make = tk.Button(winG, text="Generate Graph", command=generate, width=15)
	make.config(font=('Arial, 12'))
	make.place(x=500, y=455)

	if (sel=='1'):
		xCoor.config(text="X-Coordinate:")
		yCoor.config(text="Y-Coordinate:")
		xCoor.place(x=10, y=350)
		yCoor.place(x=240, y=350)
		ycEntry.place(x=390, y=355)
		xcEntry.place(x=160, y=355)

	else:
		if sel == '2':
			winG.title("BAR GRAPH")

		else:
			winG.title("PIE CHART")
			yEntry.config(state=tk.DISABLED)
			xEntry.config(state=tk.DISABLED)

		xCoor.config(text="Item:")
		yCoor.config(text="Value:")
		xCoor.place(x=30, y=350)
		yCoor.place(x=240, y=350)
		ycEntry.config(width=8)
		xcEntry.config(width=10)
		ycEntry.place(x=350, y=355)
		xcEntry.place(x=110, y=355)
	
	headLab.place(x=210, y=25)
	winG.mainloop()