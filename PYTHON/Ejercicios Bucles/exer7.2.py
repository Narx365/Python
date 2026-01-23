cont=0
ent1=input("dame una Frase: ")
ent2=input("dime una letra: ")
for x in str(ent1):
    if (x==ent2):
        cont=cont+1
    else:
        continue
print(cont)
