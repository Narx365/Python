def esPar(ent):
    return ent%2==0

for i in range(1,6):
    ent= float(input("dame un numero: "))
    if esPar(ent):
        print("es par")
    else:
        print("es impar")