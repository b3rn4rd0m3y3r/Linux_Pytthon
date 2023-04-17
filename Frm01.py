#!/usr/bin/python3

from tkinter import *

def set():
    # Esta mensagem vai para tela gráfica
    fTk = Tk()
    fTk.configure(bg = "light green")
    fTk.geometry("600x200")
    texto = t1.get('1.0', '1.end') + " " + t2.get('1.0', '1.end') + " " + t3.get('1.0', '4.end')
    a1 = Label(fTk, text = texto )
    a1.pack()

oTk = Tk()
#Font_form = oTk.font.Font
oTk.configure(bg = "#448080")
oTk.geometry("600x600")
oTk.grid_columnconfigure(2, minsize = 8 )
a1 = Label(oTk, text ="Nome", font = ("Mono Space", 18, "bold"), width = 8, bg = "#448080", anchor = "w")
t1 = Text(oTk, height = 1, width = 40,  padx = 1)
a2 = Label(oTk, text ="Email", font = ("Mono Space", 18, "bold"), width = 8, bg = "#448080", anchor = "w")
t2 = Text(oTk, height = 1, width = 40,  padx = 1)
a3 = Label(oTk, text ="Mensagem", font = ("Mono Space", 18, "bold"), width = 8, bg = "#448080", anchor = "w")
t3 = Text(oTk, height = 4, width = 40,  padx = 1)
b1 = Button(oTk, text = "Botão1", bg = "light blue", command = set)
a1.grid(row=0, column=0)
t1.grid(row=0, column=1)
a2.grid(row=1, column=0)
t2.grid(row=1, column=1)
a3.grid(row=2, column=0)
t3.grid(row=2, column=1)
b1.grid(row=3,columnspan=2)

oTk.mainloop()
