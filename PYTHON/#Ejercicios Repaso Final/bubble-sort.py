lista = [5, 2, 9, 1, 5, 6]
aux = 0
for x in (lista):
    for y in range(len(lista)-1):
        if lista[y] > lista[y+1]:
            aux = lista[y]
            lista[y] = lista[y+1]
            lista[y+1] = aux
        print(lista)
print(lista)