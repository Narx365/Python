def contar_a(ent):
    contador=0
    for a in ent:
        if a == "a" or a == "A":
            contador += 1
    return contador

def contar_e(ent):
    contador=0
    for e in ent:
        if e == "e" or e == "E":
            contador += 1
    return contador


def contar_i(ent):
    contador=0
    for a in ent:
        if a == "i" or a == "I":
            contador += 1
    return contador


def contar_o(ent):
    contador=0
    for a in ent:
        if a == "o" or a == "O":
            contador += 1
    return contador


def contar_u(ent):
    contador=0
    for a in ent:
        if a == "u" or a == "U":
            contador += 1
    return contador




ent = str(input("Ingrese una cadena de texto: "))
vocales = "aeiouAEIOU"
contador = 0
for x in ent:
    if x == " ":
        contador=+1
print(contador)
print(contar_a(ent))
print(contar_e(ent))
print(contar_i(ent))
print(contar_o(ent))
print(contar_u(ent))
