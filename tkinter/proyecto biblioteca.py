from tkinter import *
from tkinter import messagebox

class Biblioteca:
    def __init__(self):
        self.categoriaCiencias=[["hola","alex","fecha"],["hola2","alex2","fecha2"]]
        self.categoriaLiteratura=[["hola3","alex3","fecha3"],["hola4","alex4","fecha4"]]  

    def InicioMenu(self):
        ventana = Tk()
        ventana.title("Biblioteca")
        ventana.geometry("300x200")
        Button(ventana, text="Registrar Libros", command=self.registrarLibros).pack()
        Button(ventana, text="Mostrar Libros", command=self.MostrarLibros).pack()
        ventana.mainloop() 

    def registrarLibros(self):
        ventana = Tk()
        self.categoria_var = StringVar()
        ventana.title("Registrar Libros")
        self.categoria_var.set("None")
        ventana.geometry("300x200")
        Label(ventana, text="Seleccione la categoría:").pack()
        OptionMenu(ventana, self.categoria_var, "Ciencias", "Literatura").pack()
        Label(ventana, text="Título:").pack()
        self.titulo_entry = Entry(ventana)
        self.titulo_entry.pack()
        Label(ventana, text="Autor:").pack()
        self.autor_entry = Entry(ventana)
        self.autor_entry.pack()
        Button(ventana, text="Guardar", command=self.guardarLibro).pack()
        ventana.mainloop()

    def guardarLibro(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        fecha = "None"
        categoria = self.categoria_var.get()
        if categoria == "Ciencias":
            self.categoriaCiencias.append([titulo, autor, fecha])
            messagebox.showinfo("Éxito", "Libro registrado en Ciencias")
        elif categoria == "Literatura":
            self.categoriaLiteratura.append([titulo, autor, fecha])
            messagebox.showinfo("Éxito", "Libro registrado en Literatura")

App= Biblioteca()
App.InicioMenu()