def suma_lista(lista):
    sumat = []
    for i in lista:
        if i < 0:
            sumat.append(i)
    
    return sum(sumat)

lista = []
ent = 1
while ent != 0:
    ent = int(input("dame un numero para la lista, 0 para cerrar lista: "))
    lista.append(ent)
print( suma_lista(lista))