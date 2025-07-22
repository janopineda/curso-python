"""
numerso=[1,2,3,5,6,4]
        #0 1 2 3 4 5
print(numerso)
####################
contador=0
for x in range(len(numerso)):
    contador=contador+1
    numerso[x]=contador

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
        modificar=str(input("Dame el nombre"))
        if nombres.count(modificar):
            num=nombres.index(modificar)
            nombre=str(input("dame el nuevo nombre"))
            nombres[num]=nombre
        else:
            print("Adriana sal")
    if opt.lower()=="b":
        print("secc. ver nombres")
        for i in range(len(nombres)):
            print(f"{i}.{nombres[i]}")
    if opt.lower()=="c":
        print("adriana salte")
        x=False
