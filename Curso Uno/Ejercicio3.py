# if , while 
# > mayor 2 > 1
# < menor 1 < 2
# == igual "hola" == "hola",---- 1 == 1
# != diferente 1 != 2
# >= mayor o igual     2 >= 1 2 >= 2
# <= menor o igual     1 <= 2 1 <= 1
"""
respuesta=input("como estas")
print(respuesta)

respuesta=str(input("como estas")) 
print(respuesta)

numero=int(input("ingresa un numero uno"))
numero2=int(input("ingresa un numero dos"))
resultado=numero+ numero2
print(resultado)
"""
print("para entrar necesitas el numero 1")
numeroUno=int(input("ingresa un numero"))
numeroDoos=int(input("ingresa otro numero"))
resultado=numeroUno-numeroDoos
print(f"el resultado de la resta es {resultado}")
if resultado == 1:
    print("entraste a la casa")
    print("Eres el dueno de la casa ")
    patron=str(input("Dame tu nombre bro "))
    if patron == "José":
        print("Binevendio Chaval José")
    else:
        print("Sacate, no eres el patroncito de la casa ")
else:
    print("Uuuuy no pasaste Crack")