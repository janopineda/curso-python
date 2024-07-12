productos=["leche","huevo","jabon"]
nombres=["chichapa","rangel","zote"]
precios=[12,15,30]
iva=0.16
operacion=0
valor=0
contar=0

repetir=int(input("Dame cuantos productos quieres :"))

for y in range(repetir):
    print("\nDame el nombre del producto")
    buscar=input("R: ")
    cantidad=int(input("Cuantos deseas :"))
    print(" ")

    for x in productos:
        if x == buscar:
            dato=productos.index(x)
            contar=contar+1
            print(f"\nEl producto es: {productos[dato]} - {nombres[dato]} ${precios[dato]}")
            print(f"producto en cuenta : {contar}\ncantidad:{cantidad}\n")

            sumar=precios[dato]*cantidad
            valor=valor+sumar

calculoiva=valor*iva
operacion=calculoiva+valor
print(f"El subtotal es : ${valor}")
print(f"El iva es : ${calculoiva}")
print(f"El total es: ${operacion}")


