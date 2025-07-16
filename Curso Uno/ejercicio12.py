# ejercicio 1
boletos=int(input("dime un boleto del 1-10"))
for x in range (1,11):
    if boletos == x:
        print("Ganaste",x)
    else:
        print("No existe ese numero")
# ejercicio 2
ticket=int()
tikcet=int(input("dime la clave, este debe tener tres digitos en numero "))
cambiar=str(ticket)
if len(cambiar)==3:
    for x in range(1,10,-1):
        print("se abrira la puerta en ",x)
        if x == 1:
            print("puerta abierta")
else:
    print("no tienes el codigo")
