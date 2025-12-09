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
contador=0
contador1=0
contador2=0
disponibles=0
y=list(range(1,9)) , list(range(1,9)) 

while opciones != "s":
    print("a) Comprar")
    print("b) cancelar boleto")
    print("c) Reporte de compras de boletos")
    print("s) Salir S/s\n")
    seleccion=input("Selecione la opcion : ")
    opciones=seleccion.lower()

    # opcion de compra de boleto
    if opciones == "a" or opciones == "comprar":
        contador1=0
        contador2=0
        for x in range(len(y[0])):
            if y[0][x]=="X":
                contador+=1
        for x in range(len(y[1])):
            if y[1][x]=="X":
                contador2+=1
        if contador==8 and contador2==8:
            print("la sala se lleno ")
            input("Presiona para continuar")
        else:
            print(f"el costo del boleto es de {COSTO}")
            print("Filas disponibles")
            print(f"Fila A:   {y[0][0]}   {y[0][1]}   {y[0][2]}   {y[0][3]}   {y[0][4]}   {y[0][5]}   {y[0][6]}   {y[0][7]}") 
            print(f"Fila B:   {y[1][0]}   {y[1][1]}   {y[1][2]}   {y[1][3]}   {y[1][4]}   {y[1][5]}   {y[1][6]}   {y[1][7]}") 
            boletos=int(input("Cuantos boletos quieres : "))
            DatoNombre=input("Dame el nombre : ")
            DatoTelefono=input("Dame el Telefon : ")
            Nombre.append(DatoNombre)
            Telefono.append(DatoTelefono)
            total=boletos*COSTO
            selecfila=input("Dame la fila : ")

            if selecfila.lower()=="a":
                contador=0
                for x in range( len(y[0]) ):
                    if y[0][x]=="X":
                        contador=contador+1
                print(f"sillas ocupadas {contador}")
                disponibles=len(y[0])-contador
                if contador==8:
                    print("la fila A esta llena ")
                    input("Da enter para continuar")
                elif contador<disponibles:
                    print(f"No se puede pedir la cantidad\nsolo tienes disponible {disponibles}")
                else:
                    for f in range(boletos):
                        silla=int(input(f"Dame la silla {f+1} :"))
                        try:
                            sentarse=silla-1
                            while y[0][sentarse]=="X":
                                print("Esta ocupado seleccione otro")
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
                    Bolet.append(boletos)
                    print("boletos ",boletos)

            if selecfila.lower()=="b":
                contador=0
                for x in range( len(y[0]) ):
                    if y[1][x]=="X":
                        contador=contador+1
                disponibles=len(y[0])-contador
                if contador==8:
                    print("la fila A esta llena ")
                    input("Da enter para continuar")
                    boletos=0
                    Bolet.append(boletos)

                elif disponibles>contador:
                    print(f"No se puede pedir la cantidad\nsolo tienes disponible {disponibles}")
                else:
                    for f in range(boletos):
                        silla=int(input(f"Dame la silla {f+1} :"))
                        try:
                            sentarse=silla-1
                            while y[1][sentarse]=="X":
                                print("Esta ocupado seleccione otro")
                                silla=int(input(f"Dame la silla {f+1} :"))
                                sentarse=silla-1
                            else:
                                y[1][sentarse] = "X"
                                print(f"Fila A:   {y[0][0]}   {y[0][1]}   {y[0][2]}   {y[0][3]}   {y[0][4]}   {y[0][5]}   {y[0][6]}   {y[0][7]}") 
                                print(f"Fila B:   {y[1][0]}   {y[1][1]}   {y[1][2]}   {y[1][3]}   {y[1][4]}   {y[1][5]}   {y[1][6]}   {y[1][7]}") 
                        except:
                            print("Esta silla no existe en la fila")
                            print("Reinicia toda la compra")
                            boletos=0 
            submenu=input("Deseas Promociones Si/No :")
            if submenu.lower() == "si":
                print("Estas son las promociones")
                print("a) Tienes tarjeta ")
                print("b) Miercoles de promo ")
                sele=input("Seleciona la opcion ")
                if sele=="a":
                    print("Has seleccionado tarjeta")
                    promo1=total*0.5
                    total=promo1
                    print(f"Vas a pagar ${total} \n")
                    Compra.append(total)
                elif sele=="b":
                    print("Miercoles de %30")
                    promo2=total*0.3
                    total=promo2
                    print(f"Vas a pagar ${total} \n")
                    Compra.append(total)

            if submenu.lower() == "no":
                Bolet.append(boletos)
                print(f"El total es: {total} \n")
    if opciones == "c" or opciones=="reporte":
        print("reporte")
    if opciones == "b" or opciones=="cancelar":
        print("se a cancelado la compra ")
        total=0