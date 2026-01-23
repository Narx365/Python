def contar_positivos(lista):
    contador = 0
    for i in lista:
        if i > 0:
            contador += 1
    return contador

ent=1
while ent != 0:
    ent = int(input("dame un numero para la lista, 0 para cerrar lista: "))
    lista.append(ent)
lista = [10, -5, 3, 0, -2, 8, -1]

print("Cantidad de números positivos en la lista:", contar_positivos(lista))


