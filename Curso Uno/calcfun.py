keep=0
def operacion(num,signo):
    global keep
    if signo=="+":
        if keep >= 0 and keep <= 20:
            keep-=num
        else:
            return "Esta lleno"
    if signo=="-":
        keep-=num
    return keep


while True:
    num=int(input("Dame el numero"))
    signo=str(input(" + - "))
    r=operacion(num,signo)
    print(r)
    