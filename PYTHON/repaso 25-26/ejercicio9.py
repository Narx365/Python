def suma_lista(lista):
    return sum(lista)/len(lista)

lista = []
ent = 1
num = int(input("cuantos numeros vas a mediar?: "))
for i in range(1, num+1):
    ent = int(input("dame un numero para la lista: "))
    lista.append(ent)
print( suma_lista(lista))