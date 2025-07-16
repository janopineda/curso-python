numero=0
cont=0
numero=int(input("Dame el numero a imprimir "))

for x in range(numero):
    cont=cont+1
    if cont==4:
        for y in range(8):
            if y>=4 and y<=7:
                print(y)
        