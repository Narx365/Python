def esPrimo(num):
    contador = 0
    confirmacion = False
    for i in range(1, num):
        if (num % i) == 0:
            contador += 1
            if contador == 2:
                confirmacion = True
                break
        else:
            confirmacion = False
            continue
    if confirmacion == True:
        return ("No es un número primo")
    else:
        return ("Sí es un número primo")
numero = int(input("Introduce un número: "))
print (esPrimo(numero))