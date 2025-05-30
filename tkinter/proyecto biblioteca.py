from tkinter import *
from tkinter import messagebox
from datetime import datetime

class Biblioteca:
    def __init__(self):
        self.categoriaCiencias=[["hola","alex","alumno","fecha"],["hola2","alex2","fecha2"]]
        self.categoriaLiteratura=[["hola3","alex3","alumno3","fecha3"],["hola4","alex4","alumno4","fecha4"]]  

    def InicioMenu(self):
        ventana = Tk()
        ventana.title("Biblioteca")
        ventana.geometry("300x200")
        Button(ventana, text="Registrar Libros", command=self.registrarLibros).pack()
        Button(ventana, text="Mostrar Libros", command=self.MostrarLibros).pack()
        Button(ventana, text="Obtener Libro", command=self.ObtenerLibro).pack()
        ventana.mainloop()

    def registrarLibros(self):
        ventana = Toplevel()
        self.categoria_var = StringVar()
        ventana.title("Registrar Libros")
        self.categoria_var.set("Ciencias") 
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
 

    def guardarLibro(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        fecha = "None"
        alumno= "None"
        categoria = self.categoria_var.get()
        if categoria == "Ciencias":
            self.categoriaCiencias.append([titulo, autor, alumno, fecha])
            messagebox.showinfo("Éxito", "Libro registrado en Ciencias")
        elif categoria == "Literatura":
            self.categoriaLiteratura.append([titulo, autor, alumno, fecha])
            messagebox.showinfo("Éxito", "Libro registrado en Literatura")


    def MostrarLibros(self):
        ventana=Toplevel()
        self.categoria_var = StringVar()
        self.categoria_var.set("Ciencias")
        OptionMenu(ventana, self.categoria_var, "Ciencias", "Literatura").pack()
        Button(ventana, text="Mostrar Libros", command=self.mostrarLibrosSeleccionados).pack()

    def mostrarLibrosSeleccionados(self):      
        categoria = self.categoria_var.get()
        ventana=Toplevel()
        if categoria == "Ciencias":
            self.categoriaCiencias.sort()
            for x in range(len(self.categoriaCiencias)):
                Label(ventana, text=self.categoriaCiencias[x]).pack()
        elif categoria == "Literatura":
            self.categoriaLiteratura.sort()
            for x in range(len(self.categoriaLiteratura)):
                Label(ventana, text=self.categoriaLiteratura[x]).pack()
        else:
            messagebox.showerror("Error", "Categoría no válida")

    def ObtenerLibro(self):
        ventana= Toplevel()
        self.categoria_var = StringVar()
        self.categoria_var.set("Ciencias")
        OptionMenu(ventana, self.categoria_var, "Ciencias", "Literatura").pack()
        Button(ventana, text="Obtener Libro", command=self.obtenerLibroSeleccionado).pack()

    def obtenerLibroSeleccionado(self):
        categoria = self.categoria_var.get()
        self.catego=StringVar()
        ventana = Toplevel()
        if categoria == "Ciencias":
            self.categoriaCiencias.sort()
            self.catego.set(self.categoriaCiencias[0][0])
            OptionMenu(ventana, self.catego, *self.categoriaCiencias).pack()
            Label(ventana, text="Nombre").pack()
            self.Nombre=Entry(ventana)
            self.Nombre.pack()
            self.tiempo=datetime.now()
            Label(ventana, text="Fecha de préstamo: " + str(self.tiempo)).pack()
            Button(ventana, text="Prestar Libro", command=self.prestarLibro).pack()

        elif categoria == "Literatura":
            self.categoriaLiteratura.sort()
            self.catego=StringVar()
            self.catego.set(self.categoriaLiteratura[0][0])
            OptionMenu(ventana, self.catego, *self.categoriaLiteratura).pack()
            Label(ventana, text="Nombre").pack()
            self.Nombre=Entry(ventana)
            self.Nombre.pack()
            self.tiempo=datetime.now()
            Label(ventana, text="Fecha de préstamo: " + str(self.tiempo)).pack()
            Button(ventana, text="Prestar Libro", command=self.prestarLibro).pack()

    def prestarLibro(self):
        pass

App= Biblioteca()
App.InicioMenu()