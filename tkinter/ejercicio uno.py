from tkinter import *

def sumarNumero():
    print("saludos")

root = Tk()
etiquetaText=Label(root,text="Numero 1")
etiquetaText.pack()
botonEnviar=Button(root,text="Enviar",command=sumarNumero)
botonEnviar.pack()
root.mainloop()