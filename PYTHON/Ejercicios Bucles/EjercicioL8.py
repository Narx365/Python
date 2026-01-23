ent=int(input("cuantos numeros vas a comprobar? "))
contNeg=0
for x in range (0, ent):
    num=int(input("dame un numero: "))
    if (num<0):
        contNeg=contNeg+1
    else:
        continue
print("Has introducido " ,contNeg, " numeros negativos.")