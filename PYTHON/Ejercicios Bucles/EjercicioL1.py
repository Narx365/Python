asignatura="ab"
while asignatura != "informatica":
    ent=input("cual es la asignatura mas interesante? ")
    if (ent=="informatica"):
        print("estas en lo cierto")
        asignatura=ent
    else:
        entif=input("Estás seguro?")
        if (entif=="no"):
            continue
        else:
            print("datos incorrectos")