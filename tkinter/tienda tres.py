from tkinter import *
import openpyxl

partes = ["llanta", "ventana", "mofle"]
precios = [100, 200, 900]
subtotal = 0
iva = 0
total = 0

agregarProducto=[]
agregarPrecio=[]

class Refa:
    def __init__(self):
        self.ventanita()

    def sumarParte(self, parte):
        global subtotal, iva, total
        agregarProducto.append(parte)
        buscar=partes.index(parte)
        precio=precios[buscar]
        agregarPrecio.append(precio)
        subtotal=subtotal+precio
        iva=subtotal*0.16
        total=subtotal+iva

    def ticketVenta(self):
        ventana = Tk()
        ventana.geometry("400x200")
        ventana.configure(background="#E3EDFF")
        Label(ventana, text="Ticket de venta").pack()
        Label(ventana, text="Producto").pack()
        for i in range(len(agregarProducto)):
            Label(ventana, text=f"{agregarProducto[i]} - ${agregarPrecio[i]}").pack()
        Label(ventana, text="Subtotal").pack()
        Label(ventana, text=subtotal).pack()
        Label(ventana, text="IVA").pack()
        Label(ventana, text=iva).pack()
        Label(ventana, text="Total").pack()
        Label(ventana, text=total).pack()
        Button(ventana, text="imprimrir ticket", command=self.pasarExcel).pack()
        
    def pasarExcel(self):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["Producto", "Precio"])
        for i in range(len(agregarProducto)):
            ws.append([agregarProducto[i], agregarPrecio[i]])
        ws.append(["Subtotal", subtotal])
        ws.append(["IVA", iva])
        ws.append(["Total", total])
        wb.save("ticketVenta.xlsx")

        
    def ventanita(self):
        ventana = Tk()
        ventana.geometry("400x200")
        ventana.configure(background="#E3EDFF")

        for i in range(len(partes)):
            Button(ventana,text=f"{partes[i]} precio ${precios[i]}",command=lambda p=partes[i]: self.sumarParte(p)).pack()
        enviar=Button(ventana, text="Ticket de venta", command=self.ticketVenta)
        enviar.pack()
        ventana.mainloop()

app = Refa()