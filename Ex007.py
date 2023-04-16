#!/usr/bin/python3

from tkinter import *

def set():
    # Esta mensagem vai para tela gráfica
    fTk = Tk()
    fTk.configure(bg = "light yellow")
    fTk.geometry("300x200")
    a1 = Label(fTk, text = t1.get('1.0', '1.end') )
    a1.pack()

oTk = Tk()
oTk.configure(bg = "#448080")
oTk.geometry("400x200")
a = Label(oTk, text ="Controles do Tk")
b1 = Button(oTk, text = "Botão1", bg = "light blue", command = set)
t1 = Text(oTk, height = 1, width = 52)
#b1.geometry("50x30")
a.pack()
b1.pack()
t1.pack()

oTk.mainloop()
