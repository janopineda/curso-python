from tkinter import *
class tienda_chida:
    def __init__ (self):
        print("conectado")

    def vennta(self):
        root=Tk()
        Marco=Frame(root,bg="#AEF98B")
        Marco.pack()
        lb=Label(Marco,text="Hola",bg="#AEF98B")
        lb.pack()
        
        root.mainloop()

run=tienda_chida()
run.vennta()