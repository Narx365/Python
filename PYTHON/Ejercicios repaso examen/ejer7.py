numeros = []
for i in range(10):
    numeros.append(int(input("ingrese numero ")))

suma = sum(numeros[-5:])

print("la suma de los ultimos 5 es " ,suma)