# Esta lista representa una secuencia numérica, pero ha sido invadida por unos (1). Debes usar un ciclo for para recorrer la lista y sustituir los números que no forman parte de la secuencia original.
# Tu tarea es detectar y corregir la secuencia reemplazando los valores incorrectos por los que deberían estar, manteniendo la estructura original de la lista.

lista=[[1,1,3,1,1,1],
       [1,1,1,1,5,6],
       [1,1,1,4,1,1],
       [1,1,1,1,1,1]] 

# Respuesta
for x in range(6):
    lista[0][x]=x+1
    lista[1][x]=x+1
    lista[2][x]=x+1
    lista[3][x]=x+1

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

#-------------------------------------------------------------------
# Realiza un programa que, con base en las medidas de sus lados, determine qué tipo de triángulo es.
# Para ello, debes pedir al usuario que ingrese tres valores numéricos (uno para cada lado del triángulo). Utiliza estructuras condicionales if para analizar los valores ingresados y clasificar el triángulo como:

# Equilátero (todos los lados son iguales),
# Isósceles (dos lados son iguales), o
# Escaleno (todos los lados son diferentes).

# Puedes utilizar la función input() para recibir los datos del usuario.

#--------------------------------------------------------------------
#Si en un gato se equivoco pedro al poner x en lugar de o, para esto se determino que perdio, realiza un remplazo usando asiganción, pidiendo un input

lista=[["X","X","O"],
       ["X","O","O"],
       ["X","X", ]] 

#Por esta razón, se determinó que perdió la partida.
# Tu tarea consiste en realizar un reemplazo, utilizando asignación directa. Deberás pedir al usuario (con input()) la posición donde desea corregir el valor incorrecto y sustituirlo por una "O".

#-----------------------------------------------------------------------


# En la siguiente lista, cada fila representa a un alumno con sus respectivas calificaciones en las materias: Matemáticas, Física, Informática y Español. La última columna está marcada con una "X", indicando que falta calcular el promedio.
#       nombre mat,fic,inf,esp,promedio
lista=[["Pedro",7,8,7,9,"X"],
       ["Luis",6,10,9,8,"X"],
       ["Marcos",5,4,10,3,"X"],
       ["Luis",5,10,5,6,"X"]] 
# Tu tarea es utilizar el índice (index) para localizar la posición de la "X" en cada fila y sustituirla por el promedio de las calificaciones correspondientes. Usa la fórmula del promedio aritmético para resolverlo.

#
# Realiza un programa que convierta los números enteros del 1 al 10 a su representación binaria.
# Para ello, utiliza un ciclo for y la función integrada bin() de Python, que permite convertir un número decimal a binario.

#El programa debe imprimir cada número junto con su equivalente en binario.