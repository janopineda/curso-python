import subprocess

subprocess.run('echo que > hola.txt',shell=True)

num1=int(input("Dame el primer numero"))
num2=int(input("Dame el segundo numero"))
suma=num1+num2
if suma==3:
    subprocess.call(["del","hola.txt"],shell=True)
    print("se ha borrado hola.txt")