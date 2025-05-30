from tkinter import *
from tkinter import messagebox
from datetime import datetime

class Biblioteca:
    def __init__(self):          #titulo, alumno, fecha
        self.categoriaCiencias=[["Origen","None","None"]
                                ,["hola2","alex2","fecha2"]]
        
        self.categoriaLiteratura=[["hola3","alex3","fecha3"],
                                  ["hola4","alex4","fecha4"]] 

        self.alumnos=[["alex","Telefono","dominicio"],
                      ["Raul","Telefono2","dominicio2"],
                      ["miguel","Telefono3","dominicio3"]] 

    def InicioMenu(self):
        ventana = Tk()
        ventana.title("Biblioteca")
        ventana.geometry("300x200")
        Button(ventana, text="Registrar Libros", command=self.registrarLibros,width=20).pack()
        Button(ventana, text="Mostrar Libros", command=self.MostrarLibros,width=20).pack()
        Button(ventana, text="Prestar Libro", command=self.ObtenerLibro,width=20).pack()
        Button(ventana, text="Registrar Alumno", command=self.regAlumno,width=20).pack()
        Button(ventana, text="Ver Alumnos", command=self.verAlumnos,width=20).pack()
        ventana.mainloop()

    def regAlumno(self):
        ventana = Toplevel()
        ventana.title("Registrar Alumno")
        ventana.geometry("300x200")
        Label(ventana, text="Nombre:").pack()
        self.nombre_entry = Entry(ventana)
        self.nombre_entry.pack()
        Label(ventana, text="Teléfono:").pack()
        self.telefono_entry = Entry(ventana)
        self.telefono_entry.pack()
        Label(ventana, text="Domicilio:").pack()
        self.domicilio_entry = Entry(ventana)
        self.domicilio_entry.pack()
        Button(ventana, text="Guardar", command=self.guardarAlumno).pack()

    def verAlumnos(self):
        ventana=Toplevel()
        self.alumnos.sort()
        for AlumnRegs in self.alumnos:
            Label(ventana, text=AlumnRegs).pack()

    def guardarAlumno(self):
        nombre = self.nombre_entry.get()
        telefono = self.telefono_entry.get()
        domicilio = self.domicilio_entry.get()
        self.alumnos.append([nombre, telefono, domicilio])
        messagebox.showinfo("Éxito", "Alumno registrado correctamente")
        

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
        Button(ventana, text="Guardar", command=self.guardarLibro).pack()
 

    def guardarLibro(self):
        titulo = self.titulo_entry.get()
        fecha = "None"
        alumno= "None"
        categoria = self.categoria_var.get()
        if categoria == "Ciencias":
            self.categoriaCiencias.append([titulo, alumno, fecha])
            messagebox.showinfo("Éxito", "Libro registrado en Ciencias")
        elif categoria == "Literatura":
            self.categoriaLiteratura.append([titulo, alumno, fecha])
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
        self.alum=StringVar()
        ventana = Toplevel()
        if categoria == "Ciencias":
            self.categoriaCiencias.sort()
            self.catego.set(self.categoriaCiencias[0][0])
            OptionMenu(ventana, self.catego, *self.categoriaCiencias).pack()
            Label(ventana, text="Nombre").pack()
            OptionMenu(ventana, self.alum, *self.alumnos).pack()
            self.tiempo=datetime.now()
            Label(ventana, text="Fecha de préstamo: " + str(self.tiempo)).pack()
            Button(ventana, text="Prestar Libro", command=self.prestarLibro).pack()

        elif categoria == "Literatura":
            self.categoriaLiteratura.sort()
            self.catego.set(self.categoriaLiteratura[0][0])
            OptionMenu(ventana, self.catego, *self.categoriaLiteratura).pack()
            Label(ventana, text="Nombre").pack()
            OptionMenu(ventana, self.alum, *self.alumnos).pack()
            self.tiempo=datetime.now()
            Label(ventana, text="Fecha de préstamo: " + str(self.tiempo)).pack()
            Button(ventana, text="Prestar Libro", command=self.prestarLibro).pack()

    def prestarLibro(self):
        pass

App= Biblioteca()
App.InicioMenu()