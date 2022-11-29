from tkinter import *
from tkinter.ttk import *
import statistics
import matplotlib.pyplot as plt

def _mode(lmode):
    l = [int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), int(e2.get())]
    mode = statistics.mode(l)
    lmode.config(text = mode)

def _mean(lm):
    # if i==0:
        l=[int(e1.get()),int(e2.get()),int(e3.get()),int(e4.get()),int(e5.get())]
        mean=statistics.mean(l)
        lm.config(text=mean)
        # lm.pack()
    # if i==1:
    #     lm.root.destroy

def _median(lmd):
    # if i==0:
        l = [int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), int(e5.get())]
        median=statistics.median(l)
        lmd.config(text=median)

        # lmd.pack()
    # if i==1:
    #     lmd.root.destroy

def delbock():
    lm.config(text='<Mean>')
    lmd.config(text='<Median>')
    lmode.config(text='<Mode>')
    # lm.destroy()
    # lmd.destroy()
def _clearall():
    l = [int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), int(e5.get())]
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    delbock()
    l = Label(root,text=plt.hist(l))
    # _median(1)
    # _mean(1)
root =Tk()
root.geometry("800x500")
root.title("Aditya Raj")
heading = Label(root,text='''Designed by 
        Aditya Raj 
        11212714
                    Enter Five no to calculate Mean Median Mode''')
heading.pack(fill=X)
style = Style()

style.configure('TButton', font=
('calibri', 20, 'bold'),
                borderwidth='4',height=60,widht=5)
st = Style()
st.configure('TLabel',font=
('Helvetica', 16, 'bold'),borderwidth='4',height=60,widht=5)
# st.map()

# Changes will be reflected
# by the movement of mouse.
style.map('TButton', foreground=[('active', '!disabled', 'green')],
          background=[('active', 'black')])
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
e1.place(x=30,y=155)
# e1.pack(padx=10,pady=10)
e2.place(x=30,y=195)
# e2.pack(padx=10,pady=10)
e3.place(x=30,y=235)
# e3.pack(padx=10,pady=10)
e4.place(x=30,y=275)
# e4.pack(padx=10,pady=10)
e5.place(x=30,y=315)
# e5.pack(padx=10,pady=10)
lm = Label(root,text='<Mean>')
lmd = Label(root,text='<Median>')
lmode = Label(root, text = '<Mode>')
m = Button(root,text="Mean",command= lambda :_mean(lm))
m.pack(padx=30,pady=10)
lm.pack()
md = Button(root,text="Median",command=lambda : _median(lmd))
md.pack(padx=10,pady=10)
lmd.pack()
mode = Button(root, text = "Mode", command= lambda :_mode(lmode))
mode.pack(padx=10,pady=10)
lmode.pack()
clear = Button(root,text="Clear All",command=_clearall)
clear.pack(padx=10,pady=10)


root.mainloop()