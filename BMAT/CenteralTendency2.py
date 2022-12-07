from tkinter import *
import tkinter as tk 
from tkinter import ttk
import pandas as pd
from collections import Counter 
root = Tk() 
root.title("Project-1: Measure of Central Tendancy and Dispersion")
root.minsize(500, 500) 
root.maxsize(1200, 988)
def Mean():
	INPUT = inputtxt.get("1.0", "end-1c")
	l=[]
	str=""
	n=len(INPUT)
	for i in range(n+1):
		if(i==n):
			l.append(int(str))
			break;
		if(INPUT[i]==" "):
			l.append(int(str))
			str=""
			continue
		str+=INPUT[i]
	print(l)
	totalsum=sum(l)
	mean=totalsum/len(l)
	Output.insert(END, mean)
def Mode():
	INPUT = inputtxt.get("1.0", "end-1c")
	l1=[]
	str=""
	n=len(INPUT)
	for i in range(n+1):
		if(i==n):
			l1.append(int(str))
			break;
		if(INPUT[i]==" "):
			l1.append(int(str))
			str=""
			continue
		str+=INPUT[i]
	l1.sort()
	data = Counter(l1)
	get_mode = dict(data)
	mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
	if len(mode) == len(l1):
		get_mode = "No mode found"
	else:
		get_mode = "Mode = " + ', '.join(map(str, mode))   
	Output.insert(END, get_mode)		
def Median():
	INPUT = inputtxt.get("1.0", "end-1c")
	l1=[]
	str=""
	str=""
	n=len(INPUT)
	for i in range(n+1):
		if(i==n):
			l1.append(int(str))
			break;
		if(INPUT[i]==" "):
			l1.append(int(str))
			str=""
			continue
		str+=INPUT[i]
	l1.sort()
	n=len(l1)
	if n%2==0:
		median=((l1[n//2-1]+l1[n//2])/2)
	else:
		median=l1[n//2]
	Output.insert(END, median)

def Take_input():
	INPUT = inputtxt.get("1.0", "end-1c")
	print(INPUT)
	for i in range(len(INPUT)):
		print(INPUT[i])		
	Output.insert(END, INPUT)

	
title_label = Label(text = 'Title: Measure of Central Tendancy and Dispersion', font=('Arial',16))
author_label = Label(text = 'Author Details: ',font=('Arial',12) )
title_label.pack()
author_label.pack()
number_label = Label(text = 'Enter List of Numbers: ',font=('Arial',10) ).place(x=10, y=75)
inputtxt = Text(root, height = 1,
				width = 20,
				bg = "light yellow")
ctLabel = Label(text = 'Measure of Central Tendancy',font=('Arial',12) ).place(x=10, y=150)
var = IntVar()
r1_ct = Radiobutton(text = "Airthmetic Mean", variable = var, value = 1,command = lambda:Mean()).place(x=10, y=200)
r2_ct = Radiobutton(text = "Harmonic Mean", variable = var, value = 2).place(x=10, y=220)
r3_ct = Radiobutton(text = "Geometric Mean", variable = var, value = 3).place(x=10, y=240)
r4_ct = Radiobutton(text = "Mode", variable = var, value = 4,command = lambda:Mode()).place(x=10, y=260)
r5_ct = Radiobutton(text = "Median", variable = var, value = 5,command = lambda:Median()).place(x=10, y=280)
Output = Text(root, height = 1,
			width = 10,
			bg = "light cyan")

Display = Button(root, height = 2,
				width = 20,
				text ="Show",
				command = lambda:Take_input())

# number_label.pack()
# ctLabel.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()