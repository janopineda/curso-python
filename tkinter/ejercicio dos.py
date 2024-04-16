from tkinter import *

class Calculadora:
    def __init__(self):
        self.contador = 1
        self.texto1 = None
        
    def miProgramma(self):
        self.contador += 1
        self.texto1.config(text=str(self.contador))
        
    def miProgramma2(self):
        self.contador -= 1
        self.texto1.config(text=str(self.contador))
        
    def window(self):
        raiz = Tk()
        raiz.title("Contador")
        raiz.geometry("500x500")
               
        self.texto1 = Label(raiz, text=str(self.contador))
        self.texto1.pack()
        
        Bt = Button(raiz, text="+1", command=self.miProgramma)
        Bt.pack()
        
        bt = Button(raiz, text="-1", command=self.miProgramma2)
        bt.pack()
        
        raiz.mainloop()
        
Calc = Calculadora()
Calc.window()
