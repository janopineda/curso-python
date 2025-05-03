from tkinter import *
root=Tk()
operacion=StringVar()


def pensar():
    opt=operacion.get()
    numUno=float(num1.get())
    numDos=float(num2.get())
    print(opt)  
    if opt=="sumar":
        resultado=numUno+numDos
    elif opt=="restar":
        resultado=numUno-numDos
    elif opt=="multiplicar":
        resultado=numUno*numDos
    r.config(text=str(resultado))

root.title("Calculadora pro")

mensaje1=Label(root,text="Num 1").pack()
num1=Entry(root)
num1.pack()

mensaje2=Label(root,text="Num 2").pack()
num2=Entry(root)
num2.pack()

Radiobutton(root,text="Sumar",value="sumar",variable=operacion).pack()
Radiobutton(root,text="Restar",value="restar",variable=operacion).pack()
"""
mensaje3=Label(root,text="Operacion").pack()
operacion=Entry(root)
operacion.pack()
"""

enviar=Button(root,text="Enviar",command=pensar).pack()

r=Label(root,text="Resultado")
r.pack()

root.mainloop()