ent=int(input("Introduce un número entero positivo: "))
while ent<0:
    ent=int(input("Error. Introduce un número entero positivo: "))
for x in range(1,ent+1):
    print("*"*x) 