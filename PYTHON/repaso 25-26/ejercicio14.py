def tabla(num):
    for y in range(1, 11):
        print(num, " * " ,y, "=" ,num*y )

num = int(input("Ingrese un número entero: "))
print(tabla(num))