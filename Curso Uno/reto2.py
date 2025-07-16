ListaCalificaciones =[10.0, 9.5, 8.2, 7.2, 6.2, 5.0, 0.0]
ListaNombres=["Lucas","Maia","Adriana","Nico","jano","pepe", "Wis"]
alma=float(0.0)
contarLista=len(ListaNombres)

for x in range(contarLista):
    print(ListaNombres[x] , ListaCalificaciones[x])
    alma=alma+ListaCalificaciones[x]

resultado=alma/contarLista
print("el promedio general: ",round(resultado,1))