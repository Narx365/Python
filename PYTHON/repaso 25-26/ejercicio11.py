def exponer(b, ex):
    return( b ** ex)

base = int(input("dame un numero entero: "))
exponente = int(input("dame un numero entero al que exponer el anterior: "))

print(exponer(base, exponente))