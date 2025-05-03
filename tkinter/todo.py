from tkinter import *
horas=[]
fechas=[]
actividades=[]

class ToDo:
    def guardarInfo(self):
        fecha=self.fechaN.get()
        hora=self.horaN.get()
        actividad=self.actividadN.get()
        fechas.append(fecha)
        horas.append(hora)
        actividades.append(actividad)

    def agregarActividad(self):
        vent=Toplevel()
        fechaE=Label(vent,text="Fecha")
        fechaE.pack()
        self.fechaN=Entry(vent)
        self.fechaN.pack()

        horaE=Label(vent,text="Hora")
        horaE.pack()
        self.horaN=Entry(vent)
        self.horaN.pack()

        actividadE=Label(vent,text="Actividad")
        actividadE.pack()
        self.actividadN=Entry(vent)
        self.actividadN.pack()
        guardar=Button(vent,text="Guardar",command=self.guardarInfo)
        guardar.pack()

    def verActividad(self):
        vent=Toplevel()
        etiqueta=Label(vent,text="Hola")
        etiqueta.pack()

    def win(self):
        root=Tk()
        boton1=Button(root,text="agregar actividad",command=self.agregarActividad)
        boton1.pack()
        boton2=Button(root,text="ver",command=self.verActividad)
        boton2.pack()
        root.mainloop()
app=ToDo()
app.win()
