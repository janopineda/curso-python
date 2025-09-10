import time
contrasena=int(input("Dame la contraseña"))
convertir=str(contrasena)
texto=len(convertir)
if texto==3:
    print("Comprobando...")
    if convertir=="123":
        print("comenzando...")
        time.sleep(2)
        for x in range (10,0,-1):
            print("contando ",x)
            time.sleep(2)
    else:
        print("contrasena incorrecta")
else:
    print("No tiene tres digitos")

#----------------------------------------------
contrase=int(input("Dame la contrasena"))
if contrase>999:
    print("digitos incorrectos")
else:
    if contrase==123:
        for x in range (10,0,-1):
            print("contando ",x)
            time.sleep(2)
    else:
        print("Contrasena incorrecta")

