#en esta parte se piden los 5 inputs de numeros enteros
ent1=int(input("dame un numero entero: "))
ent2=int(input("dame otro numero entero: "))
ent3=int(input("dame otro numero entero: "))
ent4=int(input("dame otro numero entero: "))
ent5=int(input("dame un ultimo numero entero: "))

#en esta parte se calcula que numero es el mayor de los 5
if (ent1>ent2 and ent1>ent3 and ent1>ent4 and ent1>ent5):
    print(ent1, "es el numero mas alto")
elif (ent2>ent1 and ent2>ent3 and ent2>ent4 and ent2>ent5):
    print(ent2, "es el numero mas alto")
elif (ent3>ent1 and ent3>ent2 and ent3>ent4 and ent3>ent5):
    print(ent3, "es el numero mas alto")
elif (ent4>ent1 and ent4>ent2 and ent4>ent3 and ent4>ent5):
    print(ent4, "es el numero mas alto")
elif (ent5>ent1 and ent5>ent2 and ent5>ent3 and ent5>ent4):
    print(ent5, "es el numero mas alto")

#esta linea existe en caso de que se de un empate en el mayor numero
else:
    print("hay un empate entre 2 numeros o mas para el mayor")


#en esta parte se calcula que numero es el menor de los 5
if (ent1<ent2 and ent1<ent3 and ent1<ent4 and ent1<ent5):
    print(ent1, "es el numero mas bajo")
elif (ent2<ent1 and ent2<ent3 and ent2<ent4 and ent2<ent5):
    print(ent2, "es el numero mas bajo")
elif (ent3<ent1 and ent3<ent2 and ent3<ent4 and ent3<ent5):
    print(ent3, "es el numero mas bajo")
elif (ent4<ent1 and ent4<ent2 and ent4<ent3 and ent4<ent5):
    print(ent4, "es el numero mas bajo")
elif (ent5<ent1 and ent5<ent2 and ent5<ent3 and ent5<ent4):
    print(ent5, "es el numero mas bajo")
#esta linea existe en caso de que se de un empate en el menor numero
else:
    print("hay un empate entre 2 numeros o mas para el menor")

#estas ultimas lineas calculan y dan al usuario la media de los 5 numeros
avg=(ent1+ent2+ent3+ent4+ent5)/5
print("la media es " ,avg)