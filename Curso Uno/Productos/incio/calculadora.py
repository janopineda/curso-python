sumar=None
restar=None
multiplicacion=None
dividir=None
Opt=None
Num1=None
Num2=None
print("Dame el tipo de operacion")
Opt=input("R:")
if Opt=="Sumar":
    print("Dame Num1")
    Num1=int(input("Num1"))
    print("Dame Num2")
    Num2=int(input("Num2"))
    sumar=Num1+Num2
    print("El resultado", sumar)
if Opt=="restar":
    print("Dame Num1")
    Num1=int(input("Num1"))
    print("Dame Num2")
    Num2=int(input("Num2"))
    restar=Num1-Num2
    print("El resultado", restar)
if Opt=="multiplicacion":
    print("Dame Num1")
    Num1=int(input("Num1"))
    print("Dame Num2")
    Num2=int(input("Num2"))
    multiplicacion=Num1*Num2
    print("El resultado", multiplicacion)
if Opt=="dividir":
    print("Dame Num1")
    Num1=int(input("Num1"))
    print("Dame Num2")
    Num2=int(input("Num2"))
    dividir=Num1/Num2
    print("El resultado", dividir)