def suma_pares(lista):
    suma = 0
    for n in lista:
        if n %2 == 0:
            suma += n
    return suma

lista= [ ]

ent = 1
while ent != 0:
    ent = int(input("dame un numero para la lista, 0 para cerrar lista: "))
    lista.append(ent)
print(" ",suma_pares(lista))