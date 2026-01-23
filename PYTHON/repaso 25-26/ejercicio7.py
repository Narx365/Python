suma = 0
ent = 1
lista = []
while ent != 0:
    ent = int(input("Ingrese un número entero positivo (0 para terminar): "))
    if ent != 0:
        lista.append(ent)
for i in lista:
    if i % 2 == 0:
        suma += 1
print("la numero total de los pares es ", suma)
