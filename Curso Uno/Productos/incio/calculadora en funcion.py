# VAR 
a=0
b=0
Selec=None
# fun
def sumar (a,b):
    resulSuma=a+b
    return resulSuma

def restar (a,b):
    resulResta=a-b
    return resulResta

def dividir (a,b):
    resulDivi=a/b
    return resulDivi

def multi (a,b):
    resulMult=a*b
    return resulMult

while True:
    print("a) suma")
    print("b) resta")
    print("c) multiplicación")
    print("d) divicion")
    Selec=input("Qué operación quieres")

    a=int(input("Dame el dato de numero A: "))
    b=int(input("Dame el dato de numero B: "))
    
    if Selec.lower=="suma":
        print(f"el resultado es {sumar(a,b)}")
    if Selec=="resta":
        print(f"el resultado es {restar(a,b)}")
    if Selec=="multiplicar":
        print(f"el resultado es {multi(a,b)}")
    if Selec=="divicion":
        print(f"el resultado es {dividir(a,b)}")