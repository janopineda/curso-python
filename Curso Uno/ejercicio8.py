edad=int(0)
edad=int(input("edad crack"))
if edad < 4 :
    print("es gratis")
elif edad > 3 and edad <=18:
    print("pagas $45.00")
elif edad > 18:
    print("paga $150.00")
else:
    print("error")