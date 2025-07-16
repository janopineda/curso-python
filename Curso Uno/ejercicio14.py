valor=int(0)
valor=int(input("Como salir del bucle con numeros"))
valor2=str(input("dime una palabra para salir del bucle"))
while valor < 20:# mayor a 20
    print("me caigo ahhhhhh")
    if valor2 == "pato":
        print("Salir")
        valor=21
    else:
        print("estas atrapado")       
print("Estas afuera")