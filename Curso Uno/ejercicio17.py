ListaUno=[3,5,9,8,7]
ListaDos=[2,4,6,10,11]
ListaTres=[]

print(ListaUno)
print(ListaDos)

for x in range(len(ListaUno)):
    ListaTres.append(ListaUno[x])
ListaUno.clear()

for x in range(len(ListaDos)):
    ListaUno.append(ListaDos[x])
ListaDos.clear()

for x in range(len(ListaTres)):
    ListaDos.append(ListaTres[x])
ListaTres.clear()

print("-----------------------")
print(ListaUno)
print(ListaDos)