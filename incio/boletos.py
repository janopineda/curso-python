y=list(range(1,9)) , list(range(1,9)) 
contar=0

while True: 
    print(f"Fila A:   {y[0][0]}   {y[0][1]}   {y[0][2]}   {y[0][3]}   {y[0][4]}   {y[0][5]}   {y[0][6]}   {y[0][7]}") 
    print(f"Fila B:   {y[1][0]}   {y[1][1]}   {y[1][2]}   {y[1][3]}   {y[1][4]}   {y[1][5]}   {y[1][6]}   {y[1][7]}") 
    
    contar=0 # reinicia el valor de el conteo de asientos
    for x in range(len(y[0])):
        if y[0][x]=="X":
            contar=contar+1 # cuenta las sillas que estan ocupadas
    print(f"asientos ocupados en la fila A {contar}")
    
    if contar==8:
        print("Esta llena la fila")
        input("Continuar")
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
    
