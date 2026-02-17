list0=[]
negat=0
posit=0
may=0
min=0
ent1=1
while ent1 != 0:
    ent1 = int(input("Dame un numero: "))
    if ent1>may:
        may=ent1
    if ent1<min:
        min=ent1
    list0.append(ent1)
    if ent1<0:
        negat+=1
    elif ent1>0:
        posit+=1
    if ent1<list0[0]:
        min=ent1
print("La cantidad de numeros negativos es: ",negat)
print("La cantidad de numeros positivos es: ",posit)
print("El numero mayor es: ",may)
print("El numero menor es: ",min)
print("La lista de numeros es: ",list0)
