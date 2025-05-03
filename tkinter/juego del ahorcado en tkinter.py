from tkinter import *
from random import randrange
import time

palabras={"hola" : ["h","o", "l", "a"],
         "adios" : ["a", "d", "i", "o", "s"],
         "perro" : ["p", "e", "r", "o"],
         "gato" : ["g", "a", "t", "o"],
         "raton" : ["r", "a", "t", "o", "n"],
         "elefante" : ["e", "l", "e", "f", "a", "n", "t", "e"]
         }
raton=["_", "_", "_", "_" , "_"]
hola=["_", "_", "_", "_" ]
adios=["_", "_", "_", "_" , "_"]
perro=["_", "_", "_", "_" , "_"]
gato=["_", "_", "_", "_" ]
elefante=["_", "_", "_", "_" , "_", "_", "_", "_"]

class JuegoDelAhorcado:
    def ventanaUno(self):
        win = Tk()
        self.pal=Button(text="Comenzar a jugar", command=self.palabraT)
        self.pal.pack()
        win.mainloop()
    
    def palabraT(self):
        numero=randrange(0, len(palabras))
        palabra=list(palabras)[numero]
        if palabra=="raton":
            self.ratonConec()

    def ratonConec (self):
        root = Toplevel()
        self.mostrar=Label(root, text=f"{raton[0]} {raton[1]} {raton[2]} {raton[3]} {raton[4]}")
        self.mostrar.pack()
        self.escribir=Entry(root)
        self.escribir.pack()
        self.boton=Button(root,text="Enviar", command=self.raton1)
        self.boton.pack()
        self.error=Label(root, text="")
        self.error.pack()

    def raton1(self):
        revisa=self.escribir.get()
        if revisa==palabras["raton"][0]:
            raton[0]="r"
        elif revisa==palabras["raton"][1]:
            raton[1]="a"
        elif revisa==palabras["raton"][2]:
            raton[2]="t"
        elif revisa==palabras["raton"][3]:
            raton[3]="o"
        elif revisa==palabras["raton"][4]:
            raton[4]="n"
        else:
            self.error.config(text="Letra incorrecta")
            time.sleep(2)
            self.error.config(text="")
            contador=+1
            if contador==5:
                self.error.config(text="Perdiste")
                time.sleep(2)
                self.error.config(text="")
                self.mostrar.config(text="Fin del juego")
                self.escribir.config(state=DISABLED)
                self.boton.config(state=DISABLED)  
        self.mostrar.config(text=f"{raton[0]} {raton[1]} {raton[2]} {raton[3]} {raton[4]}")
        self.escribir.delete(0, END)

run=JuegoDelAhorcado().ventanaUno()
