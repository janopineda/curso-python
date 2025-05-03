from tkinter import *
from tkinter import messagebox
ns=[]
ds=[]
ts=[]
class caja:

    def cajaUs(self):
        root=Tk()
        root.title("cajero HBI")
        root.geometry("200x200")
        usu=Label(root,text="usuario")
        usu.pack()
        self.usuario=Entry(root)
        self.usuario.pack()
        psw=Label(root,text="contrasena")
        psw.pack()
        self.contrasena=Entry(root)
        self.contrasena.pack()
        boton2=Button(root,text="Entrar",command=self.iniciodesesion)
        boton2.pack()
        root.mainloop()

    def iniciodesesion(self):
        us=self.usuario.get()
        con=self.contrasena.get()
        checkUser="Toilet"
        checkPsw="Pomni"
        if us == checkUser and con==checkPsw:
            vent=Toplevel()
            etNombr=Label(vent,text="Nombre")
            etNombr.pack()
            self.nnomb=Entry(vent)
            self.nnomb.pack()
            etDirec=Label(vent,text="Direccion")
            etDirec.pack()
            self.ddire=Entry(vent)
            self.ddire.pack()
            etTelef=Label(vent,text="Telefono")
            etTelef.pack()
            self.ttele=Entry(vent)
            self.ttele.pack()
            bt=Button(vent,text="Guardar",command=self.password)
            bt.pack()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")


    def password(self):
        vent=Toplevel()
        etic=Label(vent,text="Contraseña")
        etic.pack()
        self.contrasena=Entry(vent)
        self.contrasena.pack()
        boton=Button(vent,text="Guardar",command=self.guardarInfo)
        boton.pack()

    def guardarInfo(self):
        nombre=self.nnomb.get()
        direccion=self.ddire.get()
        telefono=self.ttele.get()
        paseLibre=self.contrasena.get()

        if paseLibre == "1234":
            if nombre in ns:
                messagebox.showerror("Error", "El nombre ya existe")
            else:
                ns.append(nombre)
                ds.append(direccion)
                ts.append(telefono)
                messagebox.showinfo("Guardado", "Información guardada con éxito")     
app=caja()
app.cajaUs()