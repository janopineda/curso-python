from tkinter import *

class tienda_chucho:
    def __init__(self):
        self.precio=[]
        self.articulo=[]

    def agregar(self):
        x =len(self.articulo)
        self.articulo.append("Lata de chiles")
        self.precio.append(10)
        self.lb.config(text=f"El articulo que se agrego \n {self.articulo[x]} \ncosto ${self.precio[x]}")
        self.lb.pack()
        print(self.articulo)

    def listPay(self):
        vent=Toplevel()
        almacenDeSuma=0
        iva=0
        total=0
        x=len(self.articulo)
        for x in range(x):
            publicArt=Label(vent,text=f" {self.articulo[x]} {self.precio[x]}")
            publicArt.pack()
            almacenDeSuma=almacenDeSuma+self.precio[x]
        iva=almacenDeSuma*1.16
        total=almacenDeSuma+iva
        
        publieza=Label(vent,text=f"Subtotal ${almacenDeSuma} \nIva ${round(iva, 2)} \n Total ${total}")
        publieza.pack() 
        print("Subtotal :",almacenDeSuma)


    def ventana(self):
        root=Tk()
        boton=Button(root,text="Lata de chiles",command=self.agregar)
        boton.pack()
        
        self.lb=Label(root,text="Hola chevy")

        botoList=Button(root, text="lista",command=self.listPay)
        botoList.pack()
        

        root.mainloop()

de=tienda_chucho()
de.ventana()