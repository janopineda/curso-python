from tkinter import *

from numpy import append
class aggr:
    def __init__(self):
        self.Nombres=["Alex","Miguel"]
        self.direccion=["av 100", "calle 25"]
        self.tel=["444555","45554"]
        
        
    def agregar(self):
        varNom=str(self.ponerNombre.get())
        self.Nombres.append(varNom)
        
        varDir=str(self.ponerDire.get())
        self.direccion.append(varDir)
        
        varTel=str(self.ponerTel.get())
        self.tel.append(varTel)
        
        print(self.Nombres)
        print(self.direccion)
        print(self.tel)
    
    def ventana(self):
        root=Tk()
        root.geometry("500x600")
        
        lbNombre=Label(root,text="Nombre")
        lbNombre.pack()
        
        self.ponerNombre=Entry(root)
        self.ponerNombre.pack()
        
        lbDire=Label(root,text="Direccion")
        lbDire.pack()
        
        self.ponerDire=Entry(root)
        self.ponerDire.pack()
        
        lbTel=Label(root,text="Telefono")
        lbTel.pack()
        
        self.ponerTel=Entry(root)
        self.ponerTel.pack()
        
        Enviar=Button(root,text="Agregar",command=self.agregar)
        Enviar.pack()
        
        contar=len()
        
        root.mainloop()
        
rumoles=aggr()
rumoles.ventana()