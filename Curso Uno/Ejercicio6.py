edad=int(0)
ingresos=float(0.0)
print("cual es tu edad")
edad=int(input("R: "))
if edad < 17 :
    print("Adriana salte")
else:
    print("cual es tu ingreso")
    ingresos=float(input("R:"))
    if ingresos >= 1000:
        print("paga impuestos ")
    else:
        print("sea feliz y ve por tu camino, loser")