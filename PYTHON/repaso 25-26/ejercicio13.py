def cuantas_vocales(ent):
    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    contador = 0
    for caracter in ent:
        if caracter in vocales:
            contador += 1
    return contador

ent = str(input("Ingrese una cadena de texto y le diré cuantas vocales tiene: "))

print(cuantas_vocales(ent))