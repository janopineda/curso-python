from tkinter import *

class Calculadora:
    def __init__(self):
        self.resultado = 0
        self.datoUno = None
        self.datoDos = None
        self.insertar = None
        
    def Suma (self):
        dato_uno = float(self.datoUno.get())
        dato_dos = float(self.datoDos.get())
        self.resultado = dato_uno + dato_dos
        self.insertar.config(text=str(self.resultado))
        
    def Resta(self):
        dato_uno = float(self.datoUno.get())
        dato_dos = float(self.datoDos.get())
        self.resultado = dato_uno - dato_dos
        self.insertar.config(text=str(self.resultado))

        
    def window(self):
        raiz = Tk()
        raiz.title("Calculadora")
        raiz.geometry("500x500")
               
        self.insertar = Label(raiz, text=str(self.resultado))
        self.insertar.pack()
        
        self.datoUno = Entry(raiz)
        self.datoUno.pack()
        
        self.datoDos = Entry(raiz)
        self.datoDos.pack()
        
        Bt = Button(raiz, text="+", command=self.Suma)
        Bt.pack()
        
        bt = Button(raiz, text="-", command=self.Resta)
        bt.pack()
        
        raiz.mainloop()
        
Calc = Calculadora()
Calc.window()
