contar=0
print("bienvendo a tu examen")
print("1. El color de homero si´mpson es amarillo")
print("a) Verde   b) Amarillo c) No tiene pelo")
respuesta=input("Ingresa la letra de tu respuesta: ")
if respuesta == "c":
    contar= contar + 1
    print("Homero no tiene pelo")
else:
    print("incorrecto, homero tenia color castaño")

print("2. Marge tiene una cabezota")
print("a) Si   b) No c) Tal vez")


print ("el total de las respuestas correctas es: ", contar  )
