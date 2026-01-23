lista1 = []
lista2 = []

print ("carga lista 1")
for i in range(5):
    lista1.append(int(input("valor ")))

s1 = sum(lista1)
s2 = sum(lista2)

if s1>s2:
    print("lista 1 es mayor")
elif s2>s1:
    print("lista 2 es mayor")
else:
    print("listas iguales")