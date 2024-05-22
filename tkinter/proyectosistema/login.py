import var as conf
from tkinter import *
from tkinter import messagebox
from gtts import gTTS
from PIL import ImageTk, Image
from playsound import playsound
import os

class wi:
    def menu(self):
        rola=os.path.dirname(__file__)
        win=Toplevel()
        win.config(bg="#B5FAA6")
        derechaW=Frame(win)
        boton1=Button(derechaW,text="Consulta", width=25, height=3)
        boton1.pack()
        boton2=Button(derechaW,text="Alta", width=25, height=3)
        boton2.pack()
        boton3=Button(derechaW,text="Baja", width=25, height=3)
        boton3.pack()
        derechaW.pack(side=RIGHT)

        izquierda=Frame(win)
        lbSW=Label(izquierda,text="Selecciona la opcion",padx=10,bg="#B5FAA6")
        lbSW.pack(fill = Y)
        izquierda.pack(side=LEFT)

        win.update()

        tts=gTTS("Bienvenido Al sistema de Calificaciones", lang="es")
        habla=str(os.path.join(rola,"hola.mp3"))
        tts.save(habla)
        playsound(habla)


    def contrasenaF(self):
        User=self.UserEntry.get()
        Contrasena=self.PwEntry.get()
        if User == "Jano" and Contrasena == "Pollo":
            self.menu()
        else:
            messagebox.showerror("Contraseña", "la contraseña es invalida")

    def win(self):
        self.root=Tk()
        self.root.configure(bg="#58B22E")
        self.root.geometry(conf.tamanoVentana)

        ventana=Frame(self.root)
        ventana.configure(background="#58B22E")
        ventana.pack()
        
        logo = Image.open(os.path.join(conf.ubImg,"logo.png"))
        logo = logo.resize((130, 130))
        logoIMG=ImageTk.PhotoImage(logo)


        logoC=Label(ventana,image=logoIMG, bg="#58B22E")
        logoC.grid(row=1, column=1)

        userlba=Frame(ventana, background="#FF00E2")
        userlba.grid(row=10, column=1)

        User=Label(userlba, text="Usuario",bg="#FF00E2", padx=15, pady=10)
        User.configure(font="Arial 12 bold" , bg="#FF00E2")
        User.grid(row=11,column=1)

        self.UserEntry=Entry(userlba)
        self.UserEntry.configure(width=25)
        self.UserEntry.grid(row=12,column=1,padx=15, pady=2)

        Pw=Label(userlba, text="Contraseña",bg="#FF00E2", padx=15, pady=2)
        Pw.configure(font="Arial 12 bold" , bg="#FF00E2")
        Pw.grid(row=13,column=1)

        self.PwEntry=Entry(userlba, show="*")
        self.PwEntry.configure(width=25)
        self.PwEntry.grid(row=14,column=1,padx=15, pady=2)

        boton=Button(userlba,text="Entrar", width=15, height=2, background="#B2009E",command=self.contrasenaF)
        boton.config(bd=0)
        boton.grid(row=16,column=1,padx=15, pady=20)
        self.root.mainloop()

run=wi()
run.win()