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

def contar_palabras(ent):
    contador = 1
    cont=0
    val=0
    if ent=="":
        contador=0
    for x in ent:
        if x==" " and val==0:
            val=1
        if x!=" " and val>0:
            contador+=1
            val=0
        for y in ent:
            if x==" " and val==1:
                val=0
                if cont > mayor:
                    mayor = contador
            if x!=" " and val==0:
                val=1
        for z in ent:
            while val==1:
                cont+=1
    print(mayor)    

ent = str(input("Ingrese una cadena de texto: "))
vocales = "aeiouAEIOU"
contador = 0
for x in ent:
    if x == " ":
        contador=+1
print("hay un total de ",contar_a(ent), " letras a")
print(contar_e(ent))
print(contar_i(ent))
print(contar_o(ent))
print(contar_u(ent))
print(contar_palabras(ent))