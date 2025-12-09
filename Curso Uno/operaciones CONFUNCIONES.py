def operaciones (opt,num1,num2):
    if opt.lower()=="suma":
        re=num1+num2
    if opt.lower()=="resta":
        re=num1+num2
    return re

opt=str(input("Dame la operacion "))
num1=int(input("Dame el numero 1 "))
num2=int(input("Dame el numero 2 "))
resultado=operaciones(opt,num1,num2)
print(resultado)
    
    

