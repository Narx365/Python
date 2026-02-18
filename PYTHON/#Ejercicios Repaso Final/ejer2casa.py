def contar_vocales(frase):
    cont_a = 0
    cont_e = 0
    cont_i = 0
    cont_o = 0
    cont_u = 0

    for x in frase:
        if x == "a" or x == "A":
            cont_a += 1
        elif x == "e" or x == "E":
            cont_e += 1
        elif x == "i" or x == "I":
            cont_i += 1
        elif x == "o" or x == "O":
            cont_o += 1
        elif x == "u" or x == "U":
            cont_u += 1

    return cont_a, cont_e, cont_i, cont_o, cont_u


def contar_palabras(frase):
    palabras = 0
    dentro = False

    for x in frase:
        if x != " " and dentro == False:
            palabras += 1
            dentro = True
        elif x == " ":
            dentro = False

    return palabras


def palabra_mas_larga(frase):
    palabra_actual = ""
    palabra_larga = ""
    dentro = False

    for x in frase:
        if x != " ":
            palabra_actual += x
            dentro = True
        else:
            if dentro == True:
                if len(palabra_actual) > len(palabra_larga):
                    palabra_larga = palabra_actual
                palabra_actual = ""
                dentro = False
    if len(palabra_actual) > len(palabra_larga):
        palabra_larga = palabra_actual

    return palabra_larga

frase = input("Dime una frase: ")

a, e, i, o, u = contar_vocales(frase)
palabras = contar_palabras(frase)
larga = palabra_mas_larga(frase)

print("Cantidad de palabras:", palabras)
print("Vocales 'a':", a)
print("Vocales 'e':", e)
print("Vocales 'i':", i)
print("Vocales 'o':", o)
print("Vocales 'u':", u)
print("La palabra más larga es:", larga)
