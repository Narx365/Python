cont=0
for x in range(1, 4):
    ent=input("quieres tomar algo? ")
    if (ent=="Sí"):
        print("ahora te traigo un café")
        cont=cont+1
    elif (ent=="No"):
        print("Venga, que tengo buen café")
    else:
        print("eeh, algo has escrito mal eh?")
print("te has tomado " ,cont, " cafes.")