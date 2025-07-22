matriz=[[" A1 ", "|", " B1 ", "|"," C1 " ],
        ["------------------" ],
        [" A2 ", "|", " B2 ", "|"," C2 " ],
        ["------------------" ],
        [" A3 ", "|", " B3 ", "|"," C3 " ]
        ]
run=True
while run:
    print(matriz[0][0],matriz[0][1],matriz[0][2],matriz[0][3],matriz[0][4])
    print(matriz[1][0])
    print(matriz[2][0],matriz[2][1],matriz[2][2],matriz[2][3],matriz[2][4])
    print(matriz[3][0])
    print(matriz[4][0],matriz[4][1],matriz[4][2],matriz[4][3],matriz[4][4])

    opciones=input("Jugardor 1 - donde colocaras X : ")
    opciones2=input("Jugardor 2 - donde colocaras O : ")
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
    elif matriz[0][0] == " X " and matriz[0][2] == " X " and matriz[0][4]== " X ":
        print("Ganaste")
        run=False
    elif matriz[2][0] == " X " and matriz[2][2] == " X " and matriz[2][4]== " X ":
        print("Ganaste")
        run=False
    elif matriz[4][0] == " X " and matriz[4][2] == " X " and matriz[4][4]== " X ":
        print("Ganaste")
        run=False
    elif matriz[0][0] == " X " and matriz[2][2] ==" X "  and matriz[4][4] == " X ":
        print("Ganaste")
        run=False
    elif matriz[0][4] == " X " and matriz[2][2] ==" X "  and matriz[4][0] == " X ":
        print("Ganaste")
        run=False
