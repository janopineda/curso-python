Nombre=[]
Tele=[]
opt=None
while opt !="s":
    print("a) Agregar a phone")
    print("b) ver agenda")
    opt=input("Dame la op : ")
    if opt == "a":
        introNombre=input("Dame el nombre :")
        Nombre.append(introNombre)
        introTele=input("Dame el número : ")
        Tele.append(introTele)
    if opt =="b":
        for x in range( len(Nombre) ):
            print(f"\nNombre : {Nombre[x]}")
            print(f"Telefono : {Tele[x]}\n")