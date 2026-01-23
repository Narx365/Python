def invertir_lista(lista):
    return lista[::-1]

ent = 1
lista = []
while ent != 0:
    ent = int(input("Ingrese un número entero (0 para terminar): "))
    if ent != 0:
        lista.append(ent)

print(invertir_lista(lista))
