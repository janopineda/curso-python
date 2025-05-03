from tkinter import *

direcciones=[]
nombres=[]
telefonos=[]

class agendita:
    def ventana(self):
        root=Tk()
        root.title("Agenda")
        root.geometry("300x300")
        lbUser=Label(root,text="Usuario:")
        lbUser.pack()
        self.entUser=Entry(root)
        self.entUser.pack()
        lbPass=Label(root,text="Contraseña:")
        lbPass.pack()
        self.entPass=Entry(root,show="*")
        self.entPass.pack()
        btEntrar=Button(root,text="Entrar",command=self.logint)
        btEntrar.pack()
        root.mainloop()
    
    def logint(self):
        UsuarioDef="Pollo"
        ContrasenaDef="aña"
        usuario=self.entUser.get()
        contrasena=self.entPass.get()
        if UsuarioDef==usuario and ContrasenaDef==contrasena:
            vent=Toplevel()
            vent.title("Bienvenido")
            btEntrar=Button(vent,text="Entrar",command=self.ingresar)
            btEntrar.pack()
        else:
            vent=Toplevel()
            vent.title("Error")
            lberro=Label(vent,text="Usuario o contraseña incorrectos")
            lberro.pack()

    def ingresar(self):
        win=Toplevel()
        win.title("Agenda")
        lbNombre=Label(win,text="Nombre:")
        lbNombre.pack()
        self.entNombre=Entry(win)
        self.entNombre.pack()
        lbTelefono=Label(win,text="Telefono:")
        lbTelefono.pack()
        self.entTelefono=Entry(win)
        self.entTelefono.pack()
        lbdireccion=Label(win,text="Direccion:")
        lbdireccion.pack()
        self.entDireccion=Entry(win)
        self.entDireccion.pack()
        btGuardar=Button(win,text="Guardar",command=self.guardar)
        btGuardar.pack()
        btVer=Button(win,text="Ver",command=self.ver)
        btVer.pack()

    def guardar(self):
        grnombre=self.entNombre.get()
        grtelefono=self.entTelefono.get()
        grdireccion=self.entDireccion.get()
        direcciones.append(grdireccion)
        nombres.append(grnombre)
        telefonos.append(grtelefono)
    
    def ver(self):
        win=Toplevel()
        win.title("Contactos")
        for i in range(len(nombres)):
            lbContacto=Label(win,text=f"Nombre: {nombres[i]} Telefono: {telefonos[i]} Direccion: {direcciones[i]}")
            lbContacto.pack()

app=agendita()
app.ventana()