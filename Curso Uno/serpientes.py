from colorama import Fore, Style
from random import randrange
import os
cont=0
pasosJugadorUno=0
TurnoJuno=0
TurnoJdos=0
pasosJugadorDos=0
posicion=0
posicion2=0
tablero = [str(i) for i in range(1, 51)]

def tirarDado():
    turno=randrange(1,12)
    return turno

def turno(dado):
    global cont
    global posicion
    global posicion2
    global pasosJugadorUno
    global TurnoJuno
    global TurnoJdos
    cont+=1
    if cont==1:
        tablero[posicion] = f"{TurnoJuno}"
        TurnoJuno=TurnoJuno+(dado+pasosJugadorUno)
        if TurnoJuno==TurnoJdos:
            print("los tienen la misma casilla")
        else:
            posicion=tablero.index(str(TurnoJuno))
            tablero[posicion] = Fore.RED + f"{TurnoJuno}" + Style.RESET_ALL
    if cont==2:
        tablero[posicion2] = f"{TurnoJdos}"
        TurnoJdos=TurnoJdos+(dado+pasosJugadorDos)
        if TurnoJdos==TurnoJuno:
            print("Tienes la misma casilla")
        else:
            posicion2=tablero.index(str(TurnoJdos))
            tablero[posicion2] = Fore.BLUE + f"{TurnoJdos}" + Style.RESET_ALL
            cont=0


while True:
    os.system("cls")
    print(" ".join(map(str, tablero[40:51])),Fore.BLUE+"META")
    print(Fore.WHITE+" ".join(map(str, tablero[30:40][::-1])))
    print(" ".join(map(str, tablero[20:30])))
    print(" ".join(map(str, tablero[10:20][::-1])))
    print(Fore.BLUE+"  SALIDA", Fore.WHITE+" ".join(map(str, tablero[0:10])))

    dado=tirarDado()
    print("Tirar dados :", dado)
    turno(dado)

    input("Tirar turno, presiona Enter")
    
