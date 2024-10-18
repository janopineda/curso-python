#opciones
total=0
COSTO=90
opciones=None
sele=None

while opciones != "s":
    print("a) Comprar")
    print("b) Promociones")
    print("c) cancelar boleto")
    print("s) Salir\n")
    seleccion=input("Selecione la opcion S/s : ")
    opciones=seleccion.lower()

    # opcion de compra de boleto
    if opciones == "a" or opciones == "comprar":
        print(f"el costo del boleto es de {COSTO}")
        boletos=int(input("Cuantos boletos quieres : \n"))
        total=boletos*COSTO
        print(f"El total es: {total}")

    if opciones == "b" or opciones == "promociones":
        print("a) Tienes tarjeta ")
        print("b) Miercoles de promo ")
        sele=input("Seleciona la opcion ")
        if sele=="a":
            print("Has selecionado tarjeta")
            promo1=total*0.5
            total=promo1
            print(f"Vas a pagar ${total}")
        if sele=="b":
            print("Miercoles de %30")
            promo2=total*0.3
            total=promo2
    if opciones == "c" or opciones=="cancelar":
        print("se a cancelado la compra ")
        total=0*0