from tkinter import *
class prog:
    def __init__(self):
        self.ListaNomb=["Alex","Raul"]

    def agreg(self):
        Nombre=self.r.get()
        self.ListaNomb.append(Nombre)
        self.List.delete(0, END)
        self.List.insert(0,*self.ListaNomb) 
        
    def borrar(self):
        Nombre=self.r.get()
        self.ListaNomb.remove(Nombre)
        self.List.delete(0, END)
        self.List.insert(0,*self.ListaNomb)

    def ventana(self):
        root=Tk()
        l=Label(root,text="Nombre")
        l.pack()

        self.r=Entry(root)
        self.r.pack()

        send=Button(root,text="Enviar",command=self.agreg)
        send.pack()

        senddel=Button(root,text="Borrar",command=self.borrar)
        senddel.pack()
        
        self.List=Listbox()
        self.List.insert(0,*self.ListaNomb)     
        self.List.pack()

        root.mainloop()
ron=prog()
ron.ventana()