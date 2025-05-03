import openpyxl

nombres=["Juan","Pedro","Maria","Jose","Ana"]
matematicas=[10,8,9,7,6]
espanol=[9,8,10,7,6]
ciencias=[8,9,10,7,6]


wb=openpyxl.Workbook()
Hoja=wb.active
Hoja.title="Ejercicio Calificaciones"

Hoja["A1"]="Nombre"
Hoja["B1"]="Matematicas"
Hoja["C1"]="Espanol"
Hoja["D1"]="Ciencias"
Hoja["E1"]="Promedio"

for i in range(len(nombres)):
    Hoja["A"+str(i+2)]=nombres[i]
    Hoja["B"+str(i+2)]=matematicas[i]
    Hoja["C"+str(i+2)]=espanol[i]
    Hoja["D"+str(i+2)]=ciencias[i]
    promedio=(matematicas[i]+espanol[i]+ciencias[i])/3
    Hoja["E"+str(i+2)]=promedio

wb.save("calificaciones.xlsx")

