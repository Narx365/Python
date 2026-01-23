ent=int(input("Introduce un número entero positivo: "))
contimp=str("1")
sal=str(" ")
while ent<0:
    ent=int(input("Error. Introduce un número entero positivo: "))
for x in range(0,ent):
    if x==0:
        if2=0
        var=str(1+if2)
        sal=str(var+" "+sal)
        print(sal)
    elif x>0:
        if2=x*2
        var=str(1+if2)
        sal=str(var+" "+sal)
        print(sal)
    else:
        print("datos erroneos")
    