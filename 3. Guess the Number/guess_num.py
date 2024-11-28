# ==================== Imports ===================

import random
from tkinter import *
from tkinter import ttk

# ================= GUI Interface ================

gam = Tk()
gam.geometry("440x550")
gam.config(bg ="cyan")
gam.title(" Guess the Number ")
gam.resizable(0,0)

# ==================== Labels ====================

L1 = Label(gam, text = " Guess the Number ", font = ("Eras Light ITC",24,"bold"))
L1.config(bg = "cyan" , fg = 'Black')
L1.place(x =80, y =10)

L2 = Label(gam,text= " Result ",font = ("Rockwell",30,"bold"))
L2.config(bg = "orange" , fg = 'Black')
L2.place(x = 130, y = 70)

L3 = Label(gam,text = "Select your Range", font = ("Eras Light ITC", 20, "bold"))
L3.config(bg = "cyan" , fg = 'Black')
L3.place(x = 20, y = 140)

L4 = Label(gam, text = "Enter Your Number", font= ("Eras Light ITC", 20,"bold"))
L4.config(bg = "cyan", fg = "Black")
L4.place(x= 20, y = 250)

L5 = Label(gam, text = "TO", font= ("Eras Light ITC", 32,"bold"))
L5.config(bg = "cyan", fg = "Black")
L5.place(x= 180, y = 190)

# =================== Main Code ===================

def sumbit():
    x1 = C1.get()
    x = int(x1)
    y1 = C2.get()
    y = int(y1)
    z = random.randint(x,y)
    act_num = str(z)
    own_num = E1.get()
   

    if own_num == act_num:
        L2 = Label(gam,text= " You Win ",font = ("Rockwell",30,"bold"))
        L2.config(bg = "Green" , fg = 'Black')
        L2.place(x = 120, y = 70)

    else:
        L2 = Label(gam,text= " You Loss ",font = ("Rockwell",30,"bold"))
        L2.config(bg = "red" , fg = 'Black')
        L2.place(x = 120, y = 70)

# ==================== Entry box ====================

E1 = Entry(gam,textvariable = "own_num",font =("Baskerville Old Face",32,))
E1.place(x = 20,y = 300, width= 400)

# ==================== Combo box ====================

C1 = ttk.Combobox(gam,font =("Baskerville Old Face",32),textvariable = "x", width=5)
C1["values"] = ('1','11','21','31','41','51','61','71','81','91')
C1.current(1)
C1.place(x = 20, y = 190)

C2 = ttk.Combobox(gam,font =("Baskerville Old Face",32),textvariable = "y", width=5)
C2["values"] = ('10','20','30','40','50','60','70','80','90',1000)
C2.current(1)
C2.place(x = 280, y = 190)

# ==================== Button ====================

B1 = Button(gam, text=" Let's Play ", font =("Baskerville Old Face",32), fg='black', bg='pink',command= sumbit) 
B1.place(x=100, y=370) 

# ====================        ====================

gam.mainloop()

# ======================================== End of Program ========================================