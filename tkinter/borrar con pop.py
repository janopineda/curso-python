from tkinter import *

class Ventana:
    def __init__(self):
        self.Datos=["alex","see"]
        self.Precio=[10,15]

    def borrar(self):
        buscar=self.nab.get()
        print("Dato a buscar ",buscar)
        for x in self.Datos:
            if x==buscar:
                lol=self.Datos.index(x)
                self.Datos.pop(lol)
                self.Precio.pop(lol)
        print(f"Dato de la lista {self.Datos}")
        print(f"Datos de precio de la lista {self.Precio}")


    def ventana(self):
        ventana = Tk()
        ventana.title("Inicio de sesion")
        ventana.geometry("400x300")
        ventana.configure(background="#ADD8E6")
        self.nab=Entry(ventana)
        self.nab.pack()
        bt=Button(ventana,text="borrar",command=self.borrar)
        bt.pack()

        ventana.mainloop()

 

pocho = Ventana()
pocho.ventana()