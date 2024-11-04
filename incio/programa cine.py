#opciones
total=0
COSTO=90
opciones=None
sele=None
selecasiento=None
Nombre=[]
Telefono=[]
Compra=[]
Bolet=[]
y=list(range(1,9)) , list(range(1,9)) 

while opciones != "s":
    print("a) Comprar")
    print("b) Promociones")
    print("c) cancelar boleto")
    print("s) Salir S/s\n")
    seleccion=input("Selecione la opcion : ")
    opciones=seleccion.lower()

    # opcion de compra de boleto
    if opciones == "a" or opciones == "comprar":
        print(f"el costo del boleto es de {COSTO}")
        print("Filas disponibles")
        print(f"Fila A:   {y[0][0]}   {y[0][1]}   {y[0][2]}   {y[0][3]}   {y[0][4]}   {y[0][5]}   {y[0][6]}   {y[0][7]}") 
        print(f"Fila B:   {y[1][0]}   {y[1][1]}   {y[1][2]}   {y[1][3]}   {y[1][4]}   {y[1][5]}   {y[1][6]}   {y[1][7]}") 
        boletos=int(input("Cuantos boletos quieres : "))
        DatoNombre=input("Dame el nombre : ")
        DatoTelefono=input("Dame el Telefon : ")
        Nombre.append(DatoNombre)
        Bolet.append(boletos)
        Telefono.append(DatoTelefono)
        selecfila=input("Dame la fila : ")

        if selecfila.lower()=="a":
            for f in range(boletos):
                silla=int(input(f"Dame la silla {f+1} :"))
                try:
                    sentarse=silla-1
                    while y[0][sentarse]=="X":
                        silla=int(input(f"Dame la silla {f+1} :"))
                        sentarse=silla-1
                    else:
                        y[0][sentarse] = "X"
                        print(f"Fila A:   {y[0][0]}   {y[0][1]}   {y[0][2]}   {y[0][3]}   {y[0][4]}   {y[0][5]}   {y[0][6]}   {y[0][7]}") 
                        print(f"Fila B:   {y[1][0]}   {y[1][1]}   {y[1][2]}   {y[1][3]}   {y[1][4]}   {y[1][5]}   {y[1][6]}   {y[1][7]}") 
                except:
                    print("Esta silla no existe en la fila")
                    print("Reinicia toda la compra")
                    boletos=0 

        if selecfila.lower()=="b":
            for f in range(boletos):
                silla=int(input(f"Dame la silla {f+1} :"))
                try:
                    sentarse=silla-1
                    y[1][sentarse] = "X"
                    print(f"Fila A:   {y[0][0]}   {y[0][1]}   {y[0][2]}   {y[0][3]}   {y[0][4]}   {y[0][5]}   {y[0][6]}   {y[0][7]}") 
                    print(f"Fila B:   {y[1][0]}   {y[1][1]}   {y[1][2]}   {y[1][3]}   {y[1][4]}   {y[1][5]}   {y[1][6]}   {y[1][7]}") 
                except:
                    print("Esta silla no existe en la fila")
                    print("Reinicia toda la compra")
                    boletos=0 

        total=boletos*COSTO
        print(f"El total es: {total}")

    if opciones == "b" or opciones == "promociones":
        print("a) Tienes tarjeta ")
        print("b) Miercoles de promo ")
        sele=input("Seleciona la opcion ")
        if sele=="a":
            print("Has seleccionado tarjeta")
            promo1=total*0.5
            total=promo1
            print(f"Vas a pagar ${total}")
        if sele=="b":
            print("Miercoles de %30")
            promo2=total*0.3
            total=promo2
    if opciones == "c" or opciones=="cancelar":
        print("se a cancelado la compra ")
        total=0