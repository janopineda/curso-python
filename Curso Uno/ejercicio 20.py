opcciones=None
calificacion=float(0)
cantidadP=float(0)
promedio=float(0)
s=None
n=float(0)
precio=float(0)
while opcciones != "c":
    print("a) Calcular las promedio de materias")
    print("b) Coperativa")
    print("c) Salir")
    opcciones=input("Dame la opccion")
    if opcciones=="a":
        while n<12:
            print(f"Dame el valor de la Materia{n}")
            calificacion=float(input("Dame la calificacion"))
            calificacion+=calificacion
            n+=1
        promedio=calificacion/12
    if opcciones=="b":
        while s!="n":
            print("productos comprados",precio)
            precio=float(input("Dame la cantidad del producto"))
            cantidadP=cantidadP+precio
            s=input("quiere continuar s/n")
        print("Llevas comprado el dia de hoy ",cantidadP)
    