def suma_lista(lista):
    return sum(lista)

lista = []
ent = 1
while ent != 0:
    ent = int(input("dame un numero para la lista, 0 para cerrar lista: "))
    lista.append(ent)
print( suma_lista(lista))