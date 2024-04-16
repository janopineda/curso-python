import tkinter as tk
from tkinter import *

import os
class usuario:
    def __init__(self):
        self.info=None
        self.sayhola="Esta vacio"
        self.imp=None
        
    def hola (self):
        comprobarTexto=self.info.get()
        
        if comprobarTexto=="hola":
            self.sayhola="hola"
            self.imp.config(text=str(self.sayhola))
            
        else:
            self.sayhola="ño"
            self.imp.config(text=str(self.sayhola))
            
    def win (self):
        root=tk.Tk()
        root.title("ventana chida")
        
        self.info=Entry(root)
        self.info.pack()
        
        Btm=Button(root, text="enviar", command=self.hola)
        Btm.pack()
        
        self.imp=Label(root, text=str(self.sayhola))
        self.imp.pack()
        
        root.mainloop()
        
mostanch=usuario()
mostanch.win()

