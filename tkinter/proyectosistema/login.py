import var as conf
from tkinter import *
import os

def win(self):
    root=Tk()
    root.configure(bg="#58B22E")
    root.geometry(conf.tamanoVentana)

    ventana=Frame(root)
    ventana.configure(background="#58B22E")
    ventana.pack()
            
    logoIMG=PhotoImage(file=os.path.join(conf.ubImg,"logo.png"))
    logo=logoIMG.subsample(3)

    logoC=Label(ventana,image=logo, bg="#58B22E")
    logoC.grid(row=1, column=1)

    userlba=Frame(ventana, background="#FF00E2")
    userlba.grid(row=10, column=1)

    User=Label(userlba, text="Usuario",bg="#FF00E2", padx=15, pady=10)
    User.configure(font="Arial 12 bold" , bg="#FF00E2")
    User.grid(row=11,column=1)

    UserEntry=Entry(userlba)
    UserEntry.configure(width=25)
    UserEntry.grid(row=12,column=1,padx=15, pady=2)

    Pw=Label(userlba, text="Contraseña",bg="#FF00E2", padx=15, pady=2)
    Pw.configure(font="Arial 12 bold" , bg="#FF00E2")
    Pw.grid(row=13,column=1)

    PwEntry=Entry(userlba)
    PwEntry.configure(width=25)
    PwEntry.grid(row=14,column=1,padx=15, pady=2)

    boton=Button(userlba,text="Entrar", width=15, height=2, background="#B2009E")
    boton.config(bd=0)
    boton.grid(row=16,column=1,padx=15, pady=20)
    root.mainloop()