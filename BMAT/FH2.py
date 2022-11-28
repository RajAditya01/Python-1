import csv  
from tkinter import *
import tkinter as tk 
from tkinter import messagebox


def saverecord():
  name=name_entry.get()
  branch=branch_entry.get()
  year=year_entry.get()
  cgpa=cgpa_entry.get()

  row = [[name + "','" + branch + "','" + year + "','" + cgpa + "'}"]]
  
  messagebox.showinfo("Row Value",row)

  name_var.set("")
  branch_var.set("")
  year_var.set("")
  cgpa_var.set("")
  
  # name of csv file  
  file = open("university_records.csv", 'a+')
  
  
  # writing to csv file  
  with file:  
    # creating a csv writer object  
    csvwriter = csv.writer(file)  
        
    # writing the fields  
    csvwriter.writerows(row) 
    
  
  messagebox.showinfo("Confirmation","Row Added Successfully !!")
   
    

# creating Main window 
root = Tk() 
root.title("GUI APP - Write data into .csv file using python")
root.minsize(500, 300) 


# declaring string variable name, branch, year and cgpa

name_var=tk.StringVar() 
branch_var=tk.StringVar() 
year_var=tk.StringVar() 
cgpa_var=tk.StringVar() 


# creating labels for name, branch, year and cgpa using widget Label 
name_label = tk.Label(root, text = 'Name', font=('Arial', 12, 'bold')) 
branch_label = tk.Label(root, text = 'Branch', font=('Arial', 12, 'bold'))
year_label = tk.Label(root, text = 'Year', font=('Arial', 12, 'bold'))
cgpa_label = tk.Label(root, text = 'CGPA', font=('Arial', 12, 'bold'))


# creating a entry for input name, branch, year and cgpa using widget Entry 
name_entry = tk.Entry(root, textvariable = name_var,font=('Arial',12,'normal')) 
branch_entry = tk.Entry(root, textvariable = branch_var,font=('Arial',12,'normal'))
year_entry = tk.Entry(root, textvariable = year_var,font=('Arial',12,'normal'))
cgpa_entry = tk.Entry(root, textvariable = cgpa_var,font=('Arial',12,'normal'))

saveBt = Button(root, text = 'Save Record', command=saverecord)
quitBt = Button(root, text = 'Quit from System',command=root.destroy)


name_label.place(x=10, y=10)
branch_label.place(x=10,y=50)
year_label.place(x=10,y=100)
cgpa_label.place(x=10,y=150)

name_entry.place(x=100, y=10)
branch_entry.place(x=100,y=50)
year_entry.place(x=100,y=100)
cgpa_entry.place(x=100,y=150)


saveBt.place(x=350, y=45, width=100)
quitBt.place(x=350, y=250, width=100) 

mainloop()