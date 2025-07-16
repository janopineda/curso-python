y=list(range(1,9)) , list(range(1,9)) 
contar=0
contador1=0
contador2=0
while True: 
    print ("a) compra de boletos")
    seleccion=input("Dame la opcion ")

    if seleccion.lower() == "a":
        contador1=0
        contador2=0
        for i in range( len(y[0]) ):
            if y[0][i] == "X":
                contador1=contador1+1
            if y[1][i] == "X":
                contador2=contador2+1
        if contador1==8 and contador2==8:
            print("la sala se lleno")
        else:
            print(f"Fila A:   {y[0][0]}   {y[0][1]}   {y[0][2]}   {y[0][3]}   {y[0][4]}   {y[0][5]}   {y[0][6]}   {y[0][7]}") 
            print(f"Fila B:   {y[1][0]}   {y[1][1]}   {y[1][2]}   {y[1][3]}   {y[1][4]}   {y[1][5]}   {y[1][6]}   {y[1][7]}") 
            fila=input("Dame la fila A/B")
            if fila.lower()=="a":
                contadorfilaa=0
                for i in range(len(y[0])):
                    if y[0][i]=="X":
                        contadorfilaa=contadorfilaa+1
                if contadorfilaa==8:
                    print("Fila a esta llena")
                    input("Presiona enter para continuar")
                else:
                    x=int(input("Dame la silla : "))
                    alma=x-1
                    while y[0][alma] == "X":
                        print("")
                        print("La silla esta ocupada por un intruso")
                        print(f"Fila A:   {y[0][0]}   {y[0][1]}   {y[0][2]}   {y[0][3]}   {y[0][4]}   {y[0][5]}   {y[0][6]}   {y[0][7]}") 
                        print(f"Fila B:   {y[1][0]}   {y[1][1]}   {y[1][2]}   {y[1][3]}   {y[1][4]}   {y[1][5]}   {y[1][6]}   {y[1][7]}")
                        x=int(input("Dame la silla : ")) 
                        alma=x-1
                    else:
                        y[0][alma] = "X"
                        print(f"Fila A:   {y[0][0]}   {y[0][1]}   {y[0][2]}   {y[0][3]}   {y[0][4]}   {y[0][5]}   {y[0][6]}   {y[0][7]}") 
                        print(f"Fila B:   {y[1][0]}   {y[1][1]}   {y[1][2]}   {y[1][3]}   {y[1][4]}   {y[1][5]}   {y[1][6]}   {y[1][7]}")
                    
