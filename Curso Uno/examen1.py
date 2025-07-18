menu=True
while menu:
    print("a) contar del 1 al 10 binario")
    print("b) sumar numeros binario")
    print("c) restar numero binario")
    opcion=input("Dame la opt")

    if opcion.lower()=="a":
        for x in range(1,11):
            numeroBinario= bin(x)[2:]
            print(numeroBinario)
    
    if opcion.lower()=="b":
        numeroUno=int(input("Dame el numero :"))
        numeroDos=int(input("Dame el segundo :"))
        resultado=numeroUno+numeroDos
        numbin=bin(resultado)[2:]
        print("El resultado es ",resultado," y en binario ",numbin)

    if opcion.lower()=="c":
        numeroUno=int(input("Dame el numero :"))
        numeroDos=int(input("Dame el segundo :"))
        resultado=numeroUno-numeroDos
        numbin=bin(resultado)[2:]
        print("El resultado es ",resultado," y en binario ",numbin)
