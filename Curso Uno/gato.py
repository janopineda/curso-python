matriz=[[" A1 ", "|", " B1 ", "|"," C1 " ],
        ["------------------" ],
        [" A2 ", "|", " B2 ", "|"," C2 " ],
        ["------------------" ],
        [" A3 ", "|", " B3 ", "|"," C3 " ]
        ]
run=True
opciones=str()

def funxWin (opciones):
    global run
    print("revisando")
    if opciones == matriz[1][0] and opciones == matriz[3][0]:
        print("aqui no se puede")
    elif opciones.upper() =="A1":
        if matriz[0][0]==" X " and  matriz[0][0]==" O ":
            print("No se puede")
        else:
            matriz[0][0]=" X "
    elif opciones.upper() =="A2":
        if matriz[2][0]==" X " and matriz[2][0]==" O ":
            print("No se puede")
        else:
            matriz[2][0]=" X "
    elif opciones.upper() =="A3":
        if matriz[4][0]==" X " and matriz[4][0]==" O ":
            print("No se puede")
        else:
            matriz[4][0]=" X "
    elif opciones.upper() =="B1":
        if matriz[0][2]==" X " and matriz[0][2]==" O ":
            print("No se puede")
        else:
            matriz[0][2]=" X "
    elif opciones.upper() =="B2":
        if matriz[2][2]==" X " and matriz[2][2]==" O ":
            print("No se puede")
        else:
            matriz[2][2]=" X "
    elif opciones.upper() =="B3":
        if matriz[4][2]==" X " and matriz[4][2]==" O ":
            print("No se puede")
        else:
            matriz[4][2]=" X "
    elif opciones.upper() =="C1":
        if matriz[0][4]==" X " and matriz[0][4]==" O ":
            print("No se puede")
        else:
            matriz[0][4]=" X "
    elif opciones.upper() =="C1":
        if matriz[0][4]==" X "and matriz[0][4]==" O ":
            print("No se puede")
        else:
            matriz[0][4]=" X "
    elif opciones.upper() =="C2":
        if matriz[2][4]==" X " and matriz[2][4]==" O ":
            print("No se puede")
        else:
            matriz[2][4]=" X "
    elif opciones.upper() =="C3":
        if matriz[4][4]==" X " and matriz[4][4]==" O ":
            print("No se puede")
        else:
            matriz[4][4]=" X "
    if matriz[0][0] == " X " and matriz[0][2] == " X " and matriz[0][4]== " X ":
        print("Ganaste")
        # linea 0 - x x x
        # linea 2 - 0 0 0
        # linea 3 - 0 0 0
        run=False
    elif matriz[2][0] == " X " and matriz[2][2] == " X " and matriz[2][4]== " X ":
        print("Ganaste")
        # linea 0 - 0 0 0
        # linea 2 - x x x
        # linea 3 - 0 0 0
        run=False
    elif matriz[4][0] == " X " and matriz[4][2] == " X " and matriz[4][4]== " X ":
        print("Ganaste")
        # linea 0 - 0 0 0
        # linea 2 - 0 0 0
        # linea 3 - x x x
        run=False
    elif matriz[0][0] == " X " and matriz[2][2] ==" X "  and matriz[4][4] == " X ":
        print("Ganaste")
        # linea 0 - x 0 0
        # linea 2 - 0 x 0
        # linea 3 - 0 0 x
        run=False
    elif matriz[0][4] == " X " and matriz[2][2] ==" X "  and matriz[4][0] == " X ":
        print("Ganaste")
        # linea 0 - 0 0 x
        # linea 2 - 0 x 0
        # linea 3 - x 0 0
        run=False
    elif matriz[0][0] == " X " and matriz[0][2] ==" X "  and matriz[0][4] == " X ":
        print("Ganaste")
        # linea 0 - x x x
        # linea 2 - 0 0 0
        # linea 3 - 0 0 0
        run=False
    elif matriz[2][0] == " X " and matriz[2][2] ==" X "  and matriz[2][4] == " X ":
        print("Ganaste")
        # linea 0 - 0 0 0
        # linea 2 - x x x
        # linea 3 - 0 0 0
        run=False
    elif matriz[4][0] == " X " and matriz[4][2] ==" X "  and matriz[4][4] == " X ":
        print("Ganaste")
        # linea 0 - 0 0 0
        # linea 2 - 0 0 0
        # linea 3 - x x x 
        run=False

while run:
    print(matriz[0][0],matriz[0][1],matriz[0][2],matriz[0][3],matriz[0][4])
    print(matriz[1][0])
    print(matriz[2][0],matriz[2][1],matriz[2][2],matriz[2][3],matriz[2][4])
    print(matriz[3][0])
    print(matriz[4][0],matriz[4][1],matriz[4][2],matriz[4][3],matriz[4][4])

    opciones=input("Jugardor 1 - donde colocaras X : ")
    opciones2=input("Jugardor 2 - donde colocaras O : ")

    funxWin(opciones)
    

    ######### jugador 2
    if opciones2 == matriz[1][0] and opciones2 == matriz[3][0]:
        print("aqui no se puede")
    elif opciones2.upper() =="A1":
        if matriz[0][0]==" X " and  matriz[0][0]==" O ":
            print("No se puede")
        else:
            matriz[0][0]=" O "
    elif opciones2.upper() =="A2":
        if matriz[2][0]==" X " and matriz[2][0]==" O ":
            print("No se puede")
        else:
            matriz[2][0]=" O "
    elif opciones2.upper() =="A3":
        if matriz[4][0]==" X " and matriz[4][0]==" O ":
            print("No se puede")
        else:
            matriz[4][0]=" O "
    elif opciones2.upper() =="B1":
        if matriz[0][2]==" X " and matriz[0][2]==" O ":
            print("No se puede")
        else:
            matriz[0][2]=" O "
    elif opciones2.upper() =="B2":
        if matriz[2][2]==" X " and matriz[2][2]==" O ":
            print("No se puede")
        else:
            matriz[2][2]=" O "
    elif opciones2.upper() =="B3":
        if matriz[4][2]==" X " and matriz[4][2]==" O ":
            print("No se puede")
        else:
            matriz[4][2]=" O "
    elif opciones2.upper() =="C1":
        if matriz[0][4]==" X " and matriz[0][4]==" O ":
            print("No se puede")
        else:
            matriz[0][4]=" O "
    elif opciones2.upper() =="C1":
        if matriz[0][4]==" X "and matriz[0][4]==" O ":
            print("No se puede")
        else:
            matriz[0][4]=" O "
    elif opciones2.upper() =="C2":
        if matriz[2][4]==" X " and matriz[2][4]==" O ":
            print("No se puede")
        else:
            matriz[2][4]=" O "
    elif opciones2.upper() =="C3":
        if matriz[4][4]==" X " and matriz[4][4]==" O ":
            print("No se puede")
        else:
            matriz[4][4]=" O "
    elif matriz[0][0] == " O " and matriz[0][2] == " O " and matriz[0][4]== " O ":
        print("Ganaste")
        # linea 0 - x x x
        # linea 2 - 0 0 0
        # linea 3 - 0 0 0
        run=False
    elif matriz[2][0] == " O " and matriz[2][2] == " O " and matriz[2][4]== " O ":
        print("Ganaste")
        # linea 0 - 0 0 0
        # linea 2 - x x x
        # linea 3 - 0 0 0
        run=False
    elif matriz[4][0] == " O " and matriz[4][2] == " O " and matriz[4][4]== " 0 ":
        print("Ganaste")
        # linea 0 - 0 0 0
        # linea 2 - 0 0 0
        # linea 3 - x x x
        run=False
    elif matriz[0][0] == " O " and matriz[2][2] ==" O "  and matriz[4][4] == " O ":
        print("Ganaste")
        # linea 0 - x 0 0
        # linea 2 - 0 x 0
        # linea 3 - 0 0 x
        run=False
    elif matriz[0][4] == " O " and matriz[2][2] ==" O "  and matriz[4][0] == " O ":
        print("Ganaste")
        # linea 0 - 0 0 x
        # linea 2 - 0 x 0
        # linea 3 - x 0 0
        run=False
    elif matriz[0][0] == " O " and matriz[0][2] ==" O "  and matriz[0][4] == " O ":
        print("Ganaste")
        # linea 0 - x x x
        # linea 2 - 0 0 0
        # linea 3 - 0 0 0
        run=False
    elif matriz[2][0] == " O " and matriz[2][2] ==" O "  and matriz[2][4] == " O ":
        print("Ganaste")
        # linea 0 - 0 0 0
        # linea 2 - x x x
        # linea 3 - 0 0 0
        run=False
    elif matriz[4][0] == " O " and matriz[4][2] ==" O "  and matriz[4][4] == " O ":
        print("Ganaste")
        # linea 0 - 0 0 0
        # linea 2 - 0 0 0
        # linea 3 - x x x 
        run=False

