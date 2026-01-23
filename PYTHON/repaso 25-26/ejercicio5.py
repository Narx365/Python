lista = []
print("ingresa al menos 2 numeros enteros, para terminar ingresa -0")
ent = int(input("dame un numero entero: "))
while ent!= -0:
    lista.append(ent)
    ent = int(input("dame un numero entero: "))
lista.sort()
print ("el mayor numero es: " ,lista[-1] , "el menor numero es: " ,lista[0])
print(lista)
