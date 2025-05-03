from tkinter import *

raiz=Tk()
raiz.title("calculadora")

resultado="Resultado"
seleccion=StringVar()
seleccion.set("RealizarSuma") 

def pensar():
    opcion=seleccion.get()
    numUno=float(num1.get())
    numDos=float(num2.get())
    if opcion=="RealizarSuma":
        sumar(numUno,numDos)
    if opcion=="RealizarResta":
        restar(numUno,numDos)

def sumar(numUno,numDos):
    resultado=numUno+numDos
    return immprimir.config(text=str(resultado))

def restar(numUno,numDos):
    resultado=numUno+numDos
    return immprimir.config(text=str(resultado))
    

#---------- incio de ventana


mensaje=Label(raiz,text="Núm 1").pack()
num1=Entry(raiz)
num1.pack()
mensaje2=Label(raiz,text="Núm 2").pack()
num2=Entry(raiz)
num2.pack()

Radiobutton(raiz,text="Sumar",variable=seleccion,value="RealizarSuma").pack()
Radiobutton(raiz,text="Resta",variable=seleccion,value="RealizarResta").pack()
Radiobutton(raiz,text="Multiplicar",variable=seleccion,value="RealizarMulti").pack()


enviar=Button(raiz,text="Sumar",command=pensar).pack()
immprimir=Label(raiz,text=resultado)
immprimir.pack()

raiz.mainloop()