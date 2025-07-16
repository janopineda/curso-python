Nombres=["Daniel","Chevi","Luis","Luis Pollo"]
Domicilio=["Calle 11","Calle 22","Calle 25","Calle 30"]
Tel=["44444554","44458878","44422335","45568525"]


print("Dame el Nombre")
aggrNombre=input()
Nombres.append(aggrNombre)

print("Dame el domicilio")
aggrDomi=input()
Domicilio.append(aggrDomi)

print("Dame el telefono")
aggrTel=input()
Tel.append(aggrTel)

print ("Nombre :",  Nombres[4] )
print ("Domicilio :", Domicilio[4])
print("Telefono :", Tel[4])

print(Nombres)
print(Domicilio)
print(Tel)