from tkinter import *
import tkinter as tk 
from tkinter import messagebox
from tkinter import filedialog as fd 
from tkinter import ttk
import pandas as pd



def browse():
    global loc
    loc = fd.askopenfilename()
    lab_3 = Label(root, text = loc)
    lab_3.place(x=300, y=45)

def loaddata():
    # Using treeview widget 
    treeV = ttk.Treeview(root) 
    
    df = pd.read_excel (loc)
    
    cell_heading = df.columns.ravel()     
    frame = Frame(root, width = 400, height = 200)
    frame.place(x = 10, y = 80)
    
    tree_view = ttk.Treeview(frame, height = 33, selectmode = "extended")
    #for i in range(len(cell_heading)):
    #    tree_view.column(cell_heading[i], 50, anchor = CENTER)
    #    tree_view.heading(cell_heading[i] , text = cell_heading[i])
    
    tree_view["show"] = "headings"
    
    # Omit the declaration of scrollbar    
    
    #tree_view['yscroll'] = root.y_scollbar.set
    #tree_view['xscroll'] = root.x_scollbar.set
    tree_view.grid(row = 0, column = 0, sticky = NSEW)
    #for item in detail_info_list:
    #    tree_view.insert("",0, text = str(item.id), value=(...))
    
    # Inserting the items and their features to the columns built 
    
    




def mean():
        m = (10+20+30+40)/4
        messagebox.showinfo( "Mean is", m)
    #To open Workbook 
         
    
   


 
# creating Main window 
root = Tk() 
root.title("GUI APP - Correlation in Python")
root.minsize(800, 600) 


# Adding widgets to the Main window 

lab_1 = Label(root, text = 'Correlation Project', font =('Arial', 16))
lab_2 = Label(root, text = 'Selected Data', font =('Arial', 12))

browseBt = Button(root, text = 'Browse', command=browse)
loadBt = Button(root, text = 'Load Data', command=loaddata)
kpCor_Bt = Button(root, text = 'Karl Pearson', command=mean)
rankCor_Bt = Button(root, text = 'Rank Correlation', command=mean)
dataVis_Bt = Button(root, text = 'Data Visualization', command=mean)



quitBt = Button(root, text = 'Quit from System',command=root.destroy)



lab_1.place(x=340, y=5)
lab_2.place(x=10, y=45)
browseBt.place(x=650, y=45, width=100)
loadBt.place(x=650, y=85, width=100)

kpCor_Bt.place(x=650, y=125, width=100) 
rankCor_Bt.place(x=650, y=165, width=100) 
dataVis_Bt.place(x=650, y=205, width=100)

quitBt.place(x=650, y=550, width=100) 

mainloop()   