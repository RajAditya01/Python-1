from tkinter import *
import tkinter as tk 
from tkinter import ttk
import pandas as pd

#######
#  Title: Measure of Central Tendancy and Dispersion
# 
# @author Dr. Rajeev Gupta
# 
# @version 1.00	07.10.2021 -  Baseline Code
########


# creating Main window 
root = Tk() 
root.title("Project-1: Measure of Central Tendancy and Dispersion")
root.minsize(500, 500) 
root.maxsize(1200, 988)

# Adding widgets to the Main window 

title_label = Label(text = 'Title: Measure of Central Tendancy and Dispersion', font=('Arial',16))
author_label = Label(text = 'Author Details: ',font=('Arial',12) )
title_label.pack()
author_label.pack()

number_label = Label(text = 'Enter List of Numbers: ',font=('Arial',10) ).place(x=10, y=75)
number_text = Text(height=1, width=30).place(x=180, y=75)

ctLabel = Label(text = 'Measure of Central Tendancy',font=('Arial',12) ).place(x=10, y=150)
var = IntVar()
r1_ct = Radiobutton(text = "Airthmetic Mean", variable = var, value = 1).place(x=10, y=200)
r2_ct = Radiobutton(text = "Harmonic Mean", variable = var, value = 2).place(x=10, y=220)
r3_ct = Radiobutton(text = "Geometric Mean", variable = var, value = 3).place(x=10, y=240)
r4_ct = Radiobutton(text = "Mode", variable = var, value = 4).place(x=10, y=260)
r5_ct = Radiobutton(text = "Median", variable = var, value = 5).place(x=10, y=280)
 
dispLabel = Label(text = 'Measure of Dispersion',font=('Arial',12) ).place(x=10, y=310)


quitButton = Button(text = 'Quit from System', command=root.destroy).pack(padx=5, pady=20, side=tk.BOTTOM)

root.mainloop()