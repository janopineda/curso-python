def contrasenaF(UserEntry, PwEntry):
    User=self.UserEntry.get()
    Contrasena=self.PwEntry.get()
    if User == "Jano" and Contrasena == "Pollo":
        print("chido entraste")
    else:
        messagebox.showerror("Contraseña", "la contraseña es invalida")
