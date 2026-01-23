def contarVocales(ltr, frs):
    cont = 0
    for x in frs:
        if x in ltr:
            cont +=1
    return cont

frs = str(input("dame una frase: "))
ltr = str("aeiouAEIOUáéíóúÁÉÍÓÚ")
print("hay un total de",contarVocales(ltr, frs), "vocales.")