from tkinter import *
from tkinter import messagebox

compas=[]
contrasena=[]

class usuario:
    def user(self):
        root=Tk()
        root.title("Usuario")
        root.geometry("300x300")
        lbUser=Label(root,text="Usuario:")
        lbUser.pack()
        self.entUser=Entry(root)
        self.entUser.pack()
        lbPass=Label(root,text="Contraseña:")
        lbPass.pack()
        self.entPass=Entry(root,show="*")
        self.entPass.pack()
        btEntrar=Button(root,text="Entrar",command=self.ana)
        btEntrar.pack()
        btRegi=Button(root,text="Registrar",command=self.registrar)
        btRegi.pack()
        root.mainloop()

    def ana(self):
        veriUser=self.entUser.get()
        veriPass=self.entPass.get()
        if compas.count(veriUser) and contrasena.count(veriPass):
            messagebox.showinfo("Bienvenido","Bienvenido")
        else:
            messagebox.showinfo("Error","Usuario no registrado")

    def registrar(self):
        vent=Toplevel()
        vent.title("Registro")
        lbUser=Label(vent,text="Usuario:")
        lbUser.pack()
        self.regUser=Entry(vent)
        self.regUser.pack()
        lbPass=Label(vent,text="Contraseña:")
        lbPass.pack()
        self.regPass=Entry(vent,show="*")
        self.regPass.pack()
        btGuardar=Button(vent,text="Guardar",command=self.guardar)
        btGuardar.pack()

    def guardar(self):
        registroUser=self.regUser.get()
        registroPass=self.regPass.get()
        compas.append(registroUser)
        contrasena.append(registroPass)
        messagebox.showinfo("Registro","Registro exitoso")


app=usuario()
app.user()