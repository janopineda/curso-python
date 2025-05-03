from random import randrange
import time

palabras={"hola" : ["h","o", "l", "a"],
         "adios" : ["a", "d", "i", "o", "s"],
         "perro" : ["p", "e", "r", "o"],
         "gato" : ["g", "a", "t", "o"],
         "raton" : ["r", "a", "t", "o", "n"],
         "elefante" : ["e", "l", "e", "f", "a", "n", "t", "e"]
         }

raton=["_", "_", "_", "_" , "_"]
hola=["_", "_", "_", "_" ]
adios=["_", "_", "_", "_" , "_"]
perro=["_", "_", "_", "_" , "_"]
gato=["_", "_", "_", "_" ]
elefante=["_", "_", "_", "_" , "_", "_", "_", "_"]

escribir=str("")
contador=0
numero=randrange(0, len(palabras))

palabra=list(palabras)[numero]
# enteros int boleanos bool str string textos o cadena de textos 
if palabra=="raton":
    while palabras["raton"]!=raton:
        print(raton[0], raton[1], raton[2], raton[3],raton[4])
        escribir=input("Di la palabra/letra: ")
        if escribir==palabras["raton"][0]:
            raton[0]="r"
        elif escribir==palabras["raton"][1]:
            raton[1]="a"
        elif escribir==palabras["raton"][2]:
            raton[2]="t"
        elif escribir==palabras["raton"][3]:
            raton[3]="o"
        elif escribir==palabras["raton"][4]:
            raton[4]="n"
        else:
            contador =+1
            if contador==3:
                print("Perdiste")
                
    else:
        if contador==3:
            print("Perdiste")
            time.sleep(2)
        else:
            print("Ganaste")
            time.sleep(2)

elif palabra=="hola":
    while palabras["hola"]!=hola:
        print(hola[0], hola[1], hola[2], hola[3])
        escribir=input("Di la palabra/letra: ")
        if escribir==palabras["hola"][0]:
            hola[0]="h"
        elif escribir==palabras["hola"][1]:
            hola[1]="o"
        elif escribir==palabras["hola"][2]:
            hola[2]="l"
        elif escribir==palabras["hola"][3]:
            hola[3]="a"
        else:
            contador =+1
            if contador==3:
                print("Perdiste")
                
    else:
        if contador==3:
            print("Perdiste")
            time.sleep(2)
        else:
            print("Ganaste")
            time.sleep(2)

elif palabra=="adios":
    while palabras["adios"]!=adios:
        print(adios[0], adios[1], adios[2], adios[3], adios[4])
        escribir=input("Di la palabra/letra: ")
        if escribir==palabras["adios"][0]:
            adios[0]="a"
        elif escribir==palabras["adios"][1]:
            adios[1]="d"
        elif escribir==palabras["adios"][2]:
            adios[2]="i"
        elif escribir==palabras["adios"][3]:
            adios[3]="o"
        elif escribir==palabras["adios"][4]:
            adios[4]="s"
        else:
            contador =+1
            if contador==3:
                print("Perdiste")
                
    else:
        if contador==3:
            print("Perdiste")
            time.sleep(2)
        else:
            print("Ganaste")
            time.sleep(2)

elif palabra=="perro":
    while palabras["perro"]!=perro:
        print(perro[0], perro[1], perro[2], perro[3], perro[4])
        escribir=input("Di la palabra/letra: ")
        if escribir==palabras["perro"][0]:
            perro[0]="p"
        elif escribir==palabras["perro"][1]:
            perro[1]="e"
        elif escribir==palabras["perro"][2]:
            perro[2]="r"
            perro[3]="r"
        elif escribir==palabras["perro"][4]:
            perro[4]="o"
        else:
            contador =+1
            if contador==3:
                print("Perdiste")
                
    else:
        if contador==3:
            print("Perdiste")
            time.sleep(2)
        else:
            print("Ganaste")
            time.sleep(2)

elif palabra=="gato":
    while palabras["gato"]!=gato:
        print(gato[0], gato[1], gato[2], gato[3])
        escribir=input("Di la palabra/letra: ")
        if escribir==palabras["gato"][0]:
            gato[0]="g"
        elif escribir==palabras["gato"][1]:
            gato[1]="a"
        elif escribir==palabras["gato"][2]:
            gato[2]="t"
        elif escribir==palabras["gato"][3]:
            gato[3]="o"
        else:
            contador =+1
            if contador==3:
                print("Perdiste")
                
    else:
        if contador==3:
            print("Perdiste")
            time.sleep(2)
        else:
            print("Ganaste")
            time.sleep(2)

if palabra=="elefante":
    while palabras["elefante"]!=elefante:
        print(elefante[0], elefante[1], elefante[2], elefante[3], elefante[4], elefante[5], elefante[6], elefante[7])
        escribir=input("Di la palabra/letra: ")
        if escribir==palabras["elefante"][0]:
            elefante[0]="e"
            elefante[2]="e"
            elefante[7]="e"
        elif escribir==palabras["elefante"][1]:
            elefante[1]="l" 
        elif escribir==palabras["elefante"][3]:
            elefante[3]="f"
        elif escribir==palabras["elefante"][4]:
            elefante[4]="a"
        elif escribir==palabras["elefante"][5]:
            elefante[5]="n"
        elif escribir==palabras["elefante"][6]:
            elefante[6]="t"
        else:
            contador =+1
            if contador==3:
                print("Perdiste")
                
    else:
        if contador==3:
            print("Perdiste")
            time.sleep(2)
        else:
            print("Ganaste")
            time.sleep(2)
