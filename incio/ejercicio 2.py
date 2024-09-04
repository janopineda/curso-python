Edad=None
Precio=None
print("Ingresa tu edad")
Edad=int(input("Edad:"))
if Edad<4:
    Precio="gratis"
if Edad>=4 and Edad<=18:
    Precio="$45"
if Edad>18:
    Precio="$150"
print("El precio a pagar es", Precio)