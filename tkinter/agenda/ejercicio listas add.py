from tkinter import *

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
        
        ventana=Toplevel()

        contar=len(self.Nombres)

        for x in range(contar):
            lbNombre=Label(ventana, text=f"Nombre : {self.Nombres[x]}")
            lbNombre.pack()
            lbdir=Label(ventana, text=f"Dirección : {self.direccion[x]}")
            lbdir.pack()
            lbtel=Label(ventana,text=f"Telefono : {self.tel[x]} \n")
            lbtel.pack()
    
    def ventana(self):
        root=Tk()
        root.geometry("200x150")
        
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

        
        root.mainloop()
        
rumoles=aggr()
rumoles.ventana()