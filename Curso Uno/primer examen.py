opciones="run"
x=int(0)
binOld=int(0)
datoBin=int(0)
contenedor=int(0)
sof=0
while x!=9:
    x=len(opciones)
    print("a) dar codificacion en binario")
    print("b) Que triangulo es ")
    print("c) Tabla de multiplicar")
    opciones=input("Dame la opcion")

    if opciones=="a":
        datoBin=int(input("Dame un numero :"))
        binario=format(datoBin,'b')
        if binario=="11001": 
            sof=int(0)
            while 30 > sof:
                sof+=1
                if sof > 20:
                    contenedor=format(sof,'b')
                    print(contenedor)

    elif opciones=="b":
        ladoa=int(input("lado a "))
        ladob=int(input("lado b "))
        ladoc=int(input("lado c "))
        if ladoa != ladob and ladob != ladoc and ladoa != ladoc:
            print("Es un triángulo escaleno")
        elif ladoa == ladob and ladob == ladoc:
            print("El triángulo es equilátero")
        elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
            print("El triángulo es isósceles")

    elif opciones=="c":
        n=int(0)
        cont=int(0)
        print ("Tabla de multiplicar")
        while n<11:
            for x in range(1,11):
                multi=cont*x
                print(f"{cont}x{x}={multi}")
            print("\n\n")
            cont=n+1
            n+=1

