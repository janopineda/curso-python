
from tkinter import*
class ven: # falta la clase
    def __init__(self):
        self.info=None
        self.imp=None
        self.sayhola=None
    
    def hola(self):#idetacion mal
        comprobarTexto = str(self.info.get())
        opt=comprobarTexto.lower()
        print(opt)
        
        if opt == "court lagacy":
            costo=50
            iva=costo*0.16
            total=costo+iva
            self.sayhola = "Costo: "+ str(costo) + "\nIVA: "+  str(iva) +"\nTotal: " + str(total)
            self.imp.config(text=str(self.sayhola))
            
        if opt == "Attack":
            costo=60
            iva=costo*0.16
            total=costo+iva
            self.sayhola = "Costo: "+ str(costo) + "\nIVA: "+  str(iva) +"\nTotal: " + str(total)
            self.imp.config(text=str(self.sayhola))

            
    def win(self):# mala identacion
        root = Tk()
        root.title("hola")
        lista=Label(root,text="Court Lagacy \n Attack \n Jordan 1 Mid")#lista de producto
        lista.pack()
        
        self.info = Entry(root)
        self.info.pack()
        
        Btm = Button(root, text="Enviar", command=self.hola)#                                                                                                                                           , command=self.hola)
        Btm.pack()
        
        self.imp = Label(root, text=str(self.sayhola) )
        self.imp.pack()
        
        root.mainloop()
            
venn=ven()
venn.win()