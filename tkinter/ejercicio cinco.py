from tkinter import *
from tkinter.messagebox import *
#from ttkbootstrap import *
import os

class tienda:

    def __init__(self):
        self.menu_lista=["meme.png", "meme2.png"]

        #configuracion de la ruta
        ruta=os.path.dirname (__file__)
        self.carpetaImg =os.path.join(ruta,"imagenes")
        
    def compraMeme (self):
        raiz = Toplevel()
        raiz.geometry("100x100")
        texto=Label(raiz,text="hola ventana")
        texto.pack()

        
    def ventana (self):
        root=Tk()
        root.title("tienda la lupita")
        root.geometry("500x500")
        
        #Muestra mensaje de bienvenida con ventana emergente
        showinfo(title="Bienvenido",
		    message="Bienvenido a tu Cafeteria tolteca.")
        
        Marco=Frame(root)
        Marco.config(bg="lightblue")
        Marco.config(width=101,height=32)
        Marco.pack(side=LEFT)  
                     

        img=PhotoImage(file=os.path.join(self.carpetaImg, "meme.png" ) )
        img_che=img.subsample(2,2)
        lista1=Label(root,image=img_che)
        lista1.place(x=100,y=10)
        
        bt=Button(root,text= "Comprar",command=self.compraMeme)
        bt.place(x=100, y=60)
        
        imgE=PhotoImage(file=os.path.join(self.carpetaImg, "meme2.png" ) )
        img_ch=imgE.subsample(2,2)
        lista2=Label(root,image=img_ch)
        lista2.place(x=330,y=10)
        
        bt2=Button(root,text= "Comprar")
        bt2.place(x=330, y=60)

        
        root.mainloop()
        
vender=tienda()
vender.ventana()