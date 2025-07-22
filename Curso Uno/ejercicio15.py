numerso=[1,2,3,5,6,7]
        #0 1 2 3 4 5
####################
"""
print(numerso)

numerso[3]=4
numerso[4]=5
numerso[5]=6

print(numerso)

"""
####################

nombres=["Alex","yabasta","emilio","chaval"]
x=True
while x :
    print("a) modificar")
    print("b) ver nombres")
    print("c) salir")
    opt=str(input("Dame la opcion"))
    if opt.lower()=="a":
        print("Seleciona el nombre")
        for i in range(len(nombres)):
            print(f"{i}.{nombres[i]}")
        modificar=int(input("Dame el numero que deseas cambiar"))
        if modificar > -1 and modificar < 4:
            nombre=str(input("dame el nuevo nombre"))
            nombres[modificar]=nombre
        else:
            print("Adriana sal")
    if opt.lower()=="b":
        print("secc. ver nombres")
        for i in range(len(nombres)):
            print(f"{i}.{nombres[i]}")
    if opt.lower()=="c":
        print("adriana salte")
        x=False
        