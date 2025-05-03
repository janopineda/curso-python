from tkinter import *
root=Tk()

nume=0

def sumar():
    global nume
    nume+=1
    num.config(text=nume)

def restar():
    global nume
    nume-=1
    num.config(text=nume)


boton1=Button(root,text="+",command=sumar).pack()
num=Label(root,text=nume)
num.pack()
boton2=Button(root,text="-").pack()
root.mainloop()