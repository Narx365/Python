#En esta linea se especifica el input y que sea entero
ent=int(input("Dame un numero entero positivo: "))

#En este if se confirma primero que sea un numero positivo
if (ent<0):
    print("El numero es negativo, debe ser positivo")
#Luego se comprueba que tenga un max de 3 cifras
elif(ent>999):
    print("Error: Demasiadas cifras")
#Y a partir de aquí se comprueba si tiene 1, 2 o 3 cifras.
elif (ent<100 and ent>9):
    print("Este numero tiene 2 cifras")
elif (ent<10):
    print("Este numero tiene 1 cifra")
else:
    print("Este numero tiene 3 cifras")