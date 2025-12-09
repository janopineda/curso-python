import openpyxl
import os
from datetime import datetime
fila=[["1","2","3","4","5","6","7","8","9","10"],
      ["1","2","3","4","5","6","7","8","9","10"]]
comprados=[[],# boleto
           [],# nombre
           [],# telefono
           []]# comprado
ticket=[[],# boleto
           [],# nombre
           [],# telefono
           []]# comprado
costo=90
contar=0
cont=0
while True:
      os.system('cls')
      print("a) Comprar Boleto")
      print("b) Reporte de venta")
      print("c) Eliminar Boleto")
      opciones=str(input("Dame la opccion > "))

      if opciones.lower()=="a":
            os.system('cls')
            print("A", " ".join(fila[0]))
            print("B", " ".join(fila[1]))
            name=str(input("Dame tu nombre : "))
            telefono=str(input("Dame tu numero telefonico :"))
            promo=str(input("Dame la tipo de promo feliz/free :"))
            boletos=int(input("Cuantos boletos :"))
            contar=0
            while contar<boletos:
                  seccion=str(input("Dime en que fila :"))
                  if seccion=="a":
                        placeFila=0
                  elif seccion=="b":
                        placeFila=1
                  try:
                        silla=fila[placeFila].index(str(input("Dame la silla: ")))
                  except:
                        print("Ese asiento no esta disponible")
                        continue
                  if promo.lower()=="feliz":
                        monetario=costo*0.3
                  elif promo.lower()=="free":
                        monetario=costo*0.6
                  else:
                        monetario=costo
                  lugar=str(seccion.capitalize()+"_"+str(silla+1))
                  comprados[0].append(lugar)
                  comprados[1].append(name)
                  comprados[2].append(telefono)
                  comprados[3].append(monetario)
                  ticket[0].append(lugar)
                  ticket[1].append(name)
                  ticket[2].append(telefono)
                  ticket[3].append(monetario)
                  fila[placeFila][silla]="X"
                  contar+=1
                  print("")
                  print("ticket")
                  for x in range(len(ticket[0])):
                        print(f"Boleto {ticket[0][x]} Nombre: {ticket[1][x]}  Telefono: {ticket[2][x]}  ${round(ticket[3][x], 2)}")
                  print("")
                  wb = openpyxl.Workbook()
                  Hoja = wb.active
                  Hoja.title = "Tiket"
                  Hoja["A1"]="CinePeck"
                  Hoja["A2"]="Boleto"
                  Hoja["B2"]="Nombre"
                  Hoja["C2"]="Telefono"
                  Hoja["D2"]="Precio"
                  for x in range(len(ticket[0])):
                        Hoja[f"A{x+3}"]=ticket[0][x]
                        Hoja[f"B{x+3}"]=ticket[1][x]
                        Hoja[f"C{x+3}"]=ticket[2][x]
                        Hoja[f"D{x+3}"]=ticket[3][x]
                  
                  direccion = os.path.dirname(__file__)
                  hora = datetime.now().strftime("%H-%M-%S")  
                  wb.save(f"{direccion}\\{hora}_ticket.xlsx")
                  ticket = [[], [], [], []]
                  os.startfile(f"{direccion}\\{hora}_ticket.xlsx")
                  
           
      if opciones.lower()=="b":
            for x in range(len(comprados[0])):
                        print(f"Boleto {comprados[0][x]} Nombre: {comprados[1][x]}  Telefono: {comprados[2][x]}  ${round(comprados[3][x], 2)}")
            print("")
            horaR = datetime.now().strftime("%H-%M-%S")  
            wb = openpyxl.Workbook()
            Hoja = wb.active
            Hoja.title = f"Reporte {horaR}"
            Hoja["A1"]="CinePeck"
            Hoja["A2"]="Boleto"
            Hoja["B2"]="Nombre"
            Hoja["C2"]="Telefono"
            Hoja["D2"]="Precio"
            for x in range(len(comprados[0])):
                  Hoja[f"A{x+3}"]=comprados[0][x]
                  Hoja[f"B{x+3}"]=comprados[1][x]
                  Hoja[f"C{x+3}"]=comprados[2][x]
                  Hoja[f"D{x+3}"]=comprados[3][x]
            suma=sum(comprados[3])
            filasN=len(comprados[0])+4
            Hoja[f"C{filasN}"]="Total"
            Hoja[f"D{filasN}"]=suma
            
            direccion = os.path.dirname(__file__)
            wb.save(f"{direccion}\\{horaR}_reporte.xlsx")
            os.startfile(f"{direccion}\\{horaR}_reporte.xlsx")

      if opciones.lower()=="c":
            for x in range(len(comprados[0])):
                        print(f"Boleto {comprados[0][x]} Nombre: {comprados[1][x]}  Telefono: {comprados[2][x]}  ${round(comprados[3][x], 2)}")
            print("")
            cont=0
            while cont<1:
                  try:
                        objeto=comprados[0].index(str(input("Dame el boleto a borrar")))
                  except:
                         print("Esa silla ya fue borrada o no se encuentra")
                         continue
                  comprados[0].pop(objeto)
                  comprados[1].pop(objeto)
                  comprados[2].pop(objeto)
                  comprados[3].pop(objeto)
                  cont+=1  