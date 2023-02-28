
def menu():
    print ("1) registro")
    print ("2) pagos")
    
def listaCalf():
    precio=3000
    precio2=precio*1.16
    sinIva=precio2-precio
    totalbruto=precio-sinIva
    for elemtos in range(len(alumnos)):
        print("")
        print("El alumno ",alumnos[elemtos]," tiene la calificación de",calif[elemtos])
        alumx=alumnos[elemtos]
        califx=calif[elemtos]
        if califx==10:
            print("tiene beca del 50%")
            precioTotal=totalbruto*0.50
            conIva=precioTotal*1.15
            print("Precio Neto ",round(precioTotal,2))
            print("Precio con iva ",round(conIva,2))
            print("")
            
        elif califx>=6:
            print("tiene beca del 15%")
            precioTotal=totalbruto*0.15
            conIva=precioTotal*1.15
            print("Precio Neto ",round(precioTotal,2))
            print("Precio con iva ",round(conIva,2))
            print("")
        elif califx<=5:
            print("Se paga completo")
            precioTotal=totalbruto*1
            conIva=precioTotal*1.15
            print("Precio Neto ",round(precioTotal,2))
            print("")

def registro(regAlum,regCalf):
    alumnos.append(regAlum)
    calif.append(regCalf)

    return regAlum,regCalf
#-------------- Desarrollo de programa ------------
registMenu=4
alumnos=[]
calif=[]
opt=0
#----------------------- menú
while opt !=3 :
    menu()
    opt=int(input("Dame la opcion :"))
    match opt:
        case 1:
            while registMenu !=0 :    
                regAlum=input("Dame el nombre del alumno:")
                regCalf=int(input("Dame la calificacion :"))
                registro(regAlum,regCalf)
                listaCalf()
                
                registMenu=int(input("Quieres ingresar mas alumnos(uno continuar, dos salir) [1/0]"))
        case 2:
            listaCalf()
