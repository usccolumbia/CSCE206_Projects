# -*- coding: utf-8 -*-
"""
Titration solver

University of South Carolina 
CSCE206  Scientific Application Programming
Spring 2013  Final project



Created on Tue Nov  5 20:55:49 2013

"""

import re as re
from Tkinter import *
from tkMessageBox import *
from string import ascii_lowercase
from math import *
from sympy.solvers import solve
from sympy import Symbol
from fractions import gcd
from collections import defaultdict
import os 


root = Tk()


# Titration Equation
Title = Label(root, text='Titration Solver', font=("Calibri", 30))
Title.grid(row=0, column=0, columnspan=7)
Blank1 = Label(root, text='')
Blank1.grid(pady=3)
titr_label = Label(root, text='Equation', fg='darkgreen', font=("Calibri", 20))
titr_label.grid(row=1, column=3, padx=12)
titr = Label(root, width = 30)
titr.grid(row=2, column=3, ipadx=50)
def eqfinder():
    import tkMessageBox    
    if Acomp.get() != '' and Bcomp.get() != '':    
        # Finds the Element that ISNT 'H'    
        Aelem = re.search(r"[^H]+", Acomp.get()) 
        # Finds the Element that ISNT 'OH'    
        Belem = re.search(r"[^OH]+", Bcomp.get())
        equation = str(Acomp.get()) + str(' ') + str('(aq)') + str(' ') \
                        + str('+') + str(' ') + str(Bcomp.get()) + str(' ') \
                        + str('(aq)') + str(' ') + str('->') + str(' ') \
                        + str('H2O (l)') + str(' ') + str('+') + str(' ') \
                        + str(Belem.group()) + str(Aelem.group()) + str(' ') \
                        + str('(aq)')
        titr.configure(text='%s' % equation)
    else:
        result = tkMessageBox.showwarning("ERROR", "No Result! 2 Compounds Required.")
generate = Button(root, text='GENERATE', command=eqfinder, bg='lightgreen')
generate.grid(row=2, column=4, columnspan=2)



# Acid Label
Acid = Label(root, text='Acid', fg='red', font=("Calibri", 20))
Acid.grid(row=4, column=0, columnspan=2)

# Compound
Acomp = Entry(root, width=6)
Acomp.grid(row=5, column=1)
Acomp_label = Label(root, text='Compound', font=("Calibri", 16))
Acomp_label.grid(row=5, column=0)

# Volume
Avol = Entry(root, width=6)
Avol.grid(row=6, column=1)
Avol_label = Label(root, text='Volume', font=("Calibri", 16))
Avol_label.grid(row=6, column=0)
Avol_units = Label(root, text='mL', width=4)
Avol_units.grid(row=6, column=2)

# Concentration
Aconc = Entry(root, width=6)
Aconc.grid(row=7, column=1)
Aconc_label = Label(root, text='Concentration', font=("Calibri", 16))
Aconc_label.grid(row=7, column=0)
Aconc_units = Label(root, text='mmol/mL', width=7)
Aconc_units.grid(row=7, column=2)



# Base Label
Base = Label(root, text='Base', fg='blue', font=("Calibri", 20))
Base.grid(row=9, column=0, columnspan=2)

# Compound
Bcomp = Entry(root, width=6)
Bcomp.grid(row=10, column=1)
Bcomp_label = Label(root, text='Compound', font=("Calibri", 16))
Bcomp_label.grid(row=10, column=0)

# Volume
Bvol = Entry(root, width=6)
Bvol.grid(row=11, column=1)
Bvol_label = Label(root, text='Volume', font=("Calibri", 16))
Bvol_label.grid(row=11, column=0)
Bvol_units = Label(root, text='mL', width=4)
Bvol_units.grid(row=11, column=2)

# Concentration
Bconc = Entry(root, width=6)
Bconc.grid(row=12, column=1)
Bconc_label = Label(root, text='Concentration', font=("Calibri", 16))
Bconc_label.grid(row=12, column=0)
Bconc_units = Label(root, text='mmol/mL', width=7)
Bconc_units.grid(row=12, column=2)



# Titration Equation
def calc():
    import tkMessageBox    
    if Avol.get() == '' and Aconc.get() == '' and Bvol.get() == '' and Bconc.get() == '':
        result = tkMessageBox.askokcancel("ERROR", "No Result! 3 Parameters Required.")
        if result is True:
            Avol.delete(0, END)
            Aconc.delete(0, END)
            Bvol.delete(0, END)
            Bconc.delete(0, END)
        else:
            pass
    elif Avol.get() != '' and Aconc.get() != '' and Bvol.get() != '' and Bconc.get() != '':
        result = tkMessageBox.showwarning("WARNING!", "Too Many Parameters!")
    elif Avol.get() != '' and Aconc.get() != '' and Bconc.get() != '':
        Avol_v = float(Avol.get())
        Aconc_v = float(Aconc.get())
        Bconc_v = float(Bconc.get())        
        Bvol_v = ((Avol_v*Aconc_v)/Bconc_v)
        Bvol.insert(0, Bvol_v)
    elif Avol.get() != '' and Aconc.get() != '' and Bvol.get() != '':
        Avol_v = float(Avol.get())
        Aconc_v = float(Aconc.get())
        Bvol_v = float(Bvol.get())        
        Bconc_v = (Avol_v*Aconc_v)/(Bvol_v)
        Bconc.insert(0, Bconc_v)
    elif Aconc.get() != '' and Bvol.get() != '' and Bconc.get() != '':
        Aconc_v = float(Aconc.get())
        Bvol_v = float(Bvol.get())
        Bconc_v = float(Bconc.get())        
        Avol_v = ((Bvol_v*Bconc_v)/Aconc_v)
        Avol.insert(0, Avol_v)
    elif Avol.get() != '' and Bvol.get() != '' and Bconc.get() != '':
        Avol_v = float(Avol.get())
        Bvol_v = float(Bvol.get())
        Bconc_v = float(Bconc.get())
        Aconc_v = ((Bvol_v*Bconc_v)/Avol_v)
        Aconc.insert(0, Aconc_v)
    else:
        pass
def clear1():
    Acomp.delete(0, END)    
    Avol.delete(0, END)
    Aconc.delete(0, END)
    Bcomp.delete(0, END)    
    Bvol.delete(0, END)
    Bconc.delete(0, END)
calc = Button(root, text='CALCULATE', command=calc, bg='green')
calc.grid(row=1, column=0)
clear1 = Button(root, text='CLEAR', command=clear1, bg='red')
clear1.grid(row=1, column=1)



# Acidity/Basicity Label
AB = Label(root, text='Acidity/Basicity', fg='orange', font=("Calibri", 20))
AB.grid(row=14, column=0, columnspan=2)

# pH
pH = Entry(root, width=6)
pH.grid(row=15, column=1)
pH_label = Label(root, text='pH', font=("Calibri", 16))
pH_label.grid(row=15, column=0)

# pOH
pOH = Entry(root, width=6)
pOH.grid(row=16, column=1)
pOH_label = Label(root, text='pOH', font=("Calibri", 16))
pOH_label.grid(row=16, column=0)

# pH Equation
def find():
    import tkMessageBox    
    if Avol.get() == '' and Aconc.get() == '' and Bvol.get() == '' and Bconc.get() == '':
        result = tkMessageBox.showwarning("ERROR", "No Result!\nAt Least 2 Parameters Required.")
    elif Avol.get() != '' and Aconc.get() != '' and Bvol.get() == '' and Bconc.get() == '':
        Aconc_v2 = float(Aconc.get())
        pH.delete(0, END)
        pOH.delete(0, END)        
        pH_v = -log10(Aconc_v2)
        if pH_v > 0 and pH_v < 7:        
            pH.insert(0, pH_v)
            pOH_v = 14.0 - pH_v
            pOH.insert(0, pOH_v)
        elif pH_v == 7:
            pH.insert(0, pH_v)
            pOH_v = 14.0 - pH_v
            pOH.insert(0, pOH_v)
        else:
            result = tkMessageBox.showwarning("ERROR", "Result is Out-of-Range!\nTry New Acid Values.")
    elif Avol.get() == '' and Aconc.get() == '' and Bvol.get() != '' and Bconc.get() != '':
        Bconc_v2 = float(Bconc.get())
        pH.delete(0, END)
        pOH.delete(0, END)        
        pOH_v = -log10(Bconc_v2)
        if pOH_v <= 14 and pOH_v > 7:        
            pOH.insert(0, pOH_v)
            pH_v = 14.0 - pOH_v
            pH.insert(0, pH_v)
        elif pOH_v == 7:
            pOH.insert(0, pOH_v)
            pH_v = 14.0 - pOH_v
            pH.insert(0, pH_v)
        else:
            result = tkMessageBox.showwarning("ERROR", "Result is Out-of-Range!\nTry New Acid Values.")
    elif Avol.get() != '' and Aconc.get() != '' and Bvol.get() != '' and Bconc.get() != '':
        pH.delete(0, END)
        pOH.delete(0, END)        
        Avol_v = float(Avol.get())
        Aconc_v = float(Aconc.get())
        Bvol_v = float(Bvol.get())
        Bconc_v = float(Bconc.get())
        H_init = Avol_v * Aconc_v
        OH_init = Bvol_v * Bconc_v
        if H_init > OH_init:
            H_final = H_init - OH_init
            OH_final = OH_init - OH_init
        elif H_init < OH_init:
            H_final = H_init - H_init
            OH_final = OH_init - H_init
        else:
            pH_v = 7.0
            pH.insert(0, pH_v)
            pOH_v = 14.0 - pH_v
            pOH.insert(0, pOH_v)
        if H_final > OH_final:
            Vol_tot = Avol_v + Bvol_v
            Molarity = H_final / Vol_tot
            pH_v = -log10(Molarity)
            if pH_v >= 0 and pH_v < 7:                
                pH.insert(0, pH_v)
                pOH_v = 14.0 - pH_v
                pOH.insert(0, pOH_v)
            else:
                result = tkMessageBox.showwarning("ERROR", "Result is Out-of-Range!\nTry New Values.")
        elif H_final < OH_final:
            Vol_tot = Avol_v + Bvol_v
            Molarity = OH_final / Vol_tot
            pOH_v = -log10(Molarity)
            if pOH_v > 7 and pOH_v <= 14:            
                pOH.insert(0, pOH_v)
                pH_v = 14.0 - pOH_v
                pH.insert(0, pH_v)
            else:
                result = tkMessageBox.showwarning("ERROR", "Result is Out-of-Range!\nTry New Values.")
    else:
        result = tkMessageBox.showwarning("ERROR", "Not Enough Parameters!")
def clear2():
    pH.delete(0, END)
    pOH.delete(0, END)        
find = Button(root, text='FIND', command=find, bg='lightblue')
find.grid(row=15, column=2)
clear2 = Button(root, text='CLEAR', command=clear2, bg='red')
clear2.grid(row=16, column=2)

# Creates space at the bottom of the window
Blank4 = Label(root, text='')
Blank4.grid(pady=5)
Blank5 = Label(root, text='')
Blank5.grid(padx=10)



# Conc vs. pH Curve Table

# Sets up the table
table_vol_label = Label(root, text='Vol', font=("Calibri", 16))
table_vol_label.grid(row=6, column=4)
table_vol = range(10)
for i in range(len(table_vol)):
    table_vol[i] = Entry(root, width=6)
    table_vol[i].grid(row=(i+7), column=4)
table_pH_label = Label(root, text='pH', font=("Calibri", 16))
table_pH_label.grid(row=6, column=5)
table_pH = range(10)
for i in range(len(table_pH)):
    table_pH[i] = Entry(root, width=6)
    table_pH[i].grid(row=(i+7), column=5)

# Adds Conc and pH values to the table
def table_add():
    import tkMessageBox    
    i = 0      
    while i < 10:
        if Bvol.get() == '' or pH.get() == '':
            result = tkMessageBox.showwarning("ERROR", "Need 2 Values To Add!\n(Base Vol and pH)")
            break
        elif table_vol[i].get() == '' or table_pH[i].get() == '':
            table_vol[i].delete(0, END)
            table_pH[i].delete(0, END)            
            table_vol_v = float(Bvol.get())
            table_pH_v = float(pH.get())
            table_vol[i].insert(0, table_vol_v)
            table_pH[i].insert(0, table_pH_v)
            break
        elif table_vol[9].get() != '':
            result = tkMessageBox.showwarning("ERROR", "Too Many Values Entered!")
            break
        else:
            pass
        i = i + 1
def clear3():
    for i in range(len(table_vol)):
        table_vol[i].delete(0, END)
        table_pH[i].delete(0, END)   
add = Button(root, text='ADD', command=table_add, bg='yellow')
add.grid(row=10, column=6)
clear3 = Button(root, text='CLEAR', command=clear3, bg='red')
clear3.grid(row=11, column=6)



# Creates a graph from the table
def graph():
    import tkMessageBox    
    x = []
    y = []
    if table_vol[1] != '':
        for i in range(len(table_vol)):
            if table_vol[i].get() != '':            
                x.append(float(table_vol[i].get()))
                y.append(float(table_pH[i].get()))
        max_list = zeros(len(x))
        max_list = max_list.tolist()
        for i in range(len(max_list)-1):
            max_list[i+1] = (y[i+1]-y[i])/(x[i+1]-x[i])
        maximum = max(max_list)        
        markers_on_x = []
        markers_on_y = []        
        for i in range(len(max_list)):
            if max_list[i] == maximum:
                markers_on_x.append(x[i])                
                markers_on_y.append(y[i])
        plot(x, y, 'g-')
        plot(markers_on_x, markers_on_y, 'rD')
        xlabel('Volume Base Added (mL)')
        ylabel('pH')
        legend(['mL', 'Inflection Point'], loc='upper left')
        title('Titration Curve')
        show()
    else:
        result = tkMessageBox.showwarning("ERROR", "You need values in Table!")
graph = Button(root, text='GRAPH', command=graph, bg='purple')
graph.grid(row=12, column=6)




# Equation Solver
eq_solver = Label(root, text='Equation Solver', font=("Calibri", 20))
eq_solver.grid(row=9, column=3)
eq_enter = Entry(root, width=30)
eq_enter.grid(row=10, column=3, ipadx=10)
eq_result = Label(root, width=30)
eq_result.grid(row=12, column=3, ipadx=30)

def balance():
    Ls=list('abcdefghijklmnopqrstuvwxyz')
    eq=eq_enter.get()
    Ss,Os,Es,a,i=defaultdict(list),Ls[:],[],1,1
    for p in eq.split('->'):
        for k in p.split('+'):
            c = [Ls.pop(0), 1]
            for e,m in re.findall('([A-Z][a-z]?)([0-9]*)',k):
                m=1 if m=='' else int(m)
                a*=m
                d=[c[0],c[1]*m*i]
                Ss[e][:0],Es[:0]=[d],[[e,d]]
        i=-1
    Ys=dict((s,eval('Symbol("'+s+'")')) for s in Os if s not in Ls)
    Qs=[eval('+'.join('%d*%s'%(c[1],c[0]) for c in Ss[s]),{},Ys) for s in Ss]+[Ys['a']-a]
    k=solve(Qs,*Ys)
    if k:
        N=[k[Ys[s]] for s in sorted(Ys)]
        g=N[0]
        for a1, a2 in zip(N[0::2],N[1::2]):g=gcd(g,a2)
        N=[i/g for i in N]
        pM=lambda c: str(c) if c!=1 else ''
        ans = '->'.join('+'.join(pM(N.pop(0))+str(t) for t in p.split('+')) for p in eq.split('->'))
    else:ans = 'No Result!'
    eq_result.configure(text='%s' % ans)
equals = Button(root, text='BALANCE', command=balance)
equals.grid(row=11, column=3)



# Quit/Help Button
def kill():
    root.destroy()
def help():
    root2 = Tk()    
    frame = Frame(root2)
    frame.pack(fill='both')
    
    def kill2():
        root2.destroy()
    button = Button(frame, text="QUIT", command=kill2, bg='darkred')
    button.pack(side=BOTTOM)

    text = Text(frame)
    text.pack(side=TOP)

    choosen = open("C:\Users\Katherine\Dropbox\Python Stuff\MHK Project\HelpMenu2.txt", 'r')
    text.insert(END, choosen.read())
    root2.mainloop()
quit = Button(root, text='QUIT', command=kill, bg='darkred')
quit.grid(row=18 ,column=6)
help = Button(root, text='HELP', command=help, bg='pink')
help.grid(row=18, column=5)


root.mainloop()