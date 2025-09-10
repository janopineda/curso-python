lista=[[1,2,3,"x",5,6],
       [1,"x",3,4,5,6],
       [1,2,3,4,5,"x"],
       [1,2,3,4,"X",6]]

num=lista[0].index("x")
lista[0][num]=4

num=lista[1].index("x")
lista[1][num]=2

num=lista[2].index("x")
lista[2][num]=6

num=lista[3].index("x")
lista[3][num]=5

print(lista[0])

# remaplazar x por el número consecutivo