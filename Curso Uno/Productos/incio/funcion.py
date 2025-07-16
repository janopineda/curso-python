nombre=["Carlos", "Miguel", "Lucas","Pedro","Xochi","Pablo"]
califica=[10,9,8,7,10,9]
resultado=0
datos=[]

def promedio (agregar):
    calcular=0
    datos.append(agregar)
    for x in range(len(datos)):
        calcular=calcular+datos[x]
    resultado=calcular/len(datos)
    return resultado

for x in range(len(nombre)):
    print(f"Nombre : {nombre[x]}  Calif: {califica[x]}")
    agregar=califica[x]
    prom=promedio(agregar)

print(f"El promedio es {prom}")




