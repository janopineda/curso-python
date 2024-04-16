from tkinter import *
import os
import cv2
from time import sleep
class tienda:
    def __init__(self):
        print("conectado")
        
        #ruta del archivo fuente
        self.ruta=os.path.dirname(__file__)
        
        #ruta de imagenes
        self.rutaImg=os.path.join(self.ruta,"imagenes")
        self.rutaVideo=os.path.join(self.ruta,"videos")
        
        
    def programa1(self):
        ven=Toplevel()
        archivo=cv2.VideoCapture('video.mp4')
        while archivo.isOpened():
            ret, im = archivo.read()
            if ret == False:
                break
            cv2.imshow('imagen',im)
            if cv2.waitKey(1) ==27:
                break
            sleep(1/30)
        
        lb=Label(ven,text="hola")
        lb.pack()
        
    def programa2(self):
        ven=Toplevel()
        lb=Label(ven,text="hola")
        lb.pack()
    def win (self):
        raiz=Tk()
        
        datos1 = [ 
                  ["id01","Hola brother","img1","foto1.png",self.programa1], 
                  ["id02","que onda","img2","foto1.png",self.programa2] 
                  ]
        x=1
        
        columnas_max = 1
        print(datos1[0][3])
        print(len(datos1))
        
        
        contar = len(datos1)
        
        #xscrollbar = Scrollbar(self.new_method(raiz), orient=VERTICAL)
        #xscrollbar.grid(row=0, column=10, sticky=N+E)
        
        
        for f in range(contar):
            Marco=LabelFrame(raiz,bg="#7AFACA")
            Marco.grid(row=f // 3 ,column=f % 3 , padx=10, pady=10)
        
            datos1[f][2]=PhotoImage( file=os.path.join(self.rutaImg,datos1[f][3]) )
            imagen=Label(Marco,image=datos1[f][2],bg="#7AFACA")
            imagen.pack()
            
            
            datos1[f][0]=Label(Marco,text=datos1[f][1],bg="#7AFACA")
            datos1[f][0].pack()#place(x=f*100,y=0)
            
            ejecutar=datos1[f][4]
            boton=Button(Marco,text="enviar",bg="#ABDD7C",command=ejecutar)
            boton.config(relief=SUNKEN, bd=0)
            boton.pack(fill=BOTH)
            
        raiz.mainloop()

    def new_method(self, raiz):
        return raiz
        
working=tienda()
working.win()