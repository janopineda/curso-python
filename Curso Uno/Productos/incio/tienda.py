"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠞⠛⠛⠉⠉⠉⠉⠉⠙⠛⢦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠞⠉⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠐⢹⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡾⠋⠀⠀⠀⠀⢀⣀⣤⣤⠴⠶⠶⠶⠶⠶⡶⡾⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⠋⠀⠀⢀⡴⠾⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡼⠁⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀tiene su ardilla hoy?
⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⣰⣏🐿️⣀⣀ 
⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀⢸⡇⣠⠏⠉⠛⠛⠋⠁
⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⢸⣿⠋⠀⠀⠀⠀⠀⠀
⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⠀
⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⣼⠃⣧⠀⠀⠀⠀⠀⠀⠀
"""

producto=["Oreos","Chicles","Churromaiz"]
nombreProduc=None
calcular=[]
costos=[18,5,20]
stock=[20,30,5]
precios=0
resultado=0
datosCompra=[]
secciones=["a) Agregar Productos",
           "b) Consulta",
           "c) Comprar",
           "d) Ver cuanto se ha comprado",
           "s) Salir"]


def verTotaldeVen ():
    Totalvendido=0
    for x in range(len(datosCompra)):
        Totalvendido=Totalvendido+datosCompra[x]
    return Totalvendido

def darDeAltaProduc (nombreProduc, precio,cuantos):
    while producto.count(nombreProduc):
        print("no se puede articulo repetido ")
        nombreProduc=input("Dame el nombre del producto :").capitalize()
        precio=int(input("Dame el costo :"))
        cuantos=int(input("Cuantos productos tienes : "))
    else:
        producto.append(nombreProduc)
        costos.append(precio)
        stock.append(cuantos)

def comprarIVA(valor):
    resultado=valor*1.16
    return resultado

def consulta():
    for i in range(len(producto)):
        print(f"{i}. {producto[i]} cant: {stock[i]} ${costos[i]}")

def compra():
    Totalpago=0
    almacenar=0
    seguircomp=None
    while seguircomp !="n":
        BuscarProduc=input("Dame el nombre de producto : ").capitalize()
        CuantosProduc=int(input("Cuantos quieres : "))
        num=producto.index(BuscarProduc)
        valor=costos[num]*CuantosProduc
        NumResta=stock[num]-CuantosProduc
        stock[num]=NumResta
        almacenar=comprarIVA(valor)
        Totalpago += almacenar
        print(f"El costo a pagar : {almacenar}")
        seguircomp=input("Quieres seguir comprando S/N").lower()
    else:
        print(f"El total a pagar es : {Totalpago}" )
        datosCompra.append(Totalpago)

while True:

    for x in secciones:
        print(x)
    selec=input("Dame la opcion : ")

    if selec=="a":
        nombreProduc=input("Dame el nombre : ")
        precio=int(input("Dame el precio : "))
        cuantos=int(input("Cuantos productos tienes : "))
        darDeAltaProduc (nombreProduc, precio,cuantos)

    if selec=="b":
        consulta()
    
    if selec=="c":
        repetir=0
        print("Estos son los productos ")
        consulta()
        compra()
    
        
                