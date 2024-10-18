x=True
while x:
    print("Deseas continuar")
    y=input("Deseas continuar")
    if y=="s" or y=="S":
        x=True
    elif y.lower()=="n":
        x=False      