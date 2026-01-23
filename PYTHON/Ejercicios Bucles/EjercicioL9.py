ent=int(input("cuantos numeros vas a comprobar? "))
sum=0
for x in range (0, ent):
    num=float(input("dame un numero: "))
    sum=sum+num
    
print("la suma total es: ", sum)