from tkinter import *

raiz=Tk()
raiz.title("calculadora")

resultado="Resultado"
seleccion=StringVar()

def pensar():
    opcion=seleccion.get()
    numUno=float(num1.get())
    numDos=float(num2.get())
    if opcion=="RealizarSuma":
        sumar(numUno,numDos)

def sumar(numUno,numDos):
    resultado=numUno+numDos
    return immprimir.config(text=str(resultado))
    

#---------- incio de ventana


mensaje=Label(raiz,text="Núm 1").pack()
num1=Entry(raiz)
num1.pack()
mensaje2=Label(raiz,text="Núm 2").pack()
num2=Entry(raiz)
num2.pack()

selecSumar=Radiobutton(raiz,text="Sumar",variable=seleccion,value="RealizarSuma")
selecSumar.pack()
selecResta=Radiobutton(raiz,text="Resta",variable=seleccion,value="RealizarResta")
selecResta.pack()
selecMulti=Radiobutton(raiz,text="Multiplicar",variable=seleccion,value="RealizarMulti")
selecMulti.pack()

enviar=Button(raiz,text="Sumar",command=pensar).pack()
immprimir=Label(raiz,text=resultado)
immprimir.pack()

raiz.mainloop()