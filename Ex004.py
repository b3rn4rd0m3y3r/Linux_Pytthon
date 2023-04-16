#!/usr/bin/python3

from tkinter import *
oTk = Tk()
oTk.geometry("400x200")
a = Label(oTk, text ="Controles do Tk")
b1 = Button(oTk, text = "Botão1", bg = "light blue")
#b1.geometry("50x30")
a.pack()
b1.pack()

oTk.mainloop()
