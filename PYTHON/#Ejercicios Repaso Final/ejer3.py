nombre_alumno= input ("Escriba su nombre: ")
lista=[]
notas= 0
suspenso= 0
aprobado= 0
notable= 0
sobresaliente= 0

while True:
    nota= int(input("dime una nota del uno al 10, si escribes la nota -1 se acabará el programa: "))
    if nota == -1:
        break
    if nota < 0 or nota > 10:
        print("Nota INválida")
    else: 
        print("Nota válida")
        lista.append(nota)

        if nota <5:
            suspenso+= 1
        elif nota <7:
            aprobado+= 1
        elif nota <9:
            notable+= 1
        else:
            sobresaliente+= 1



if lista:
    mayor= max(lista)
    menor= min(lista)
    suma_notas= sum(lista)
    media= suma_notas/ len(lista)
    print ("nota media/promedio=", media)
    print ("La mayor nota es:", mayor)
    print ("La menor nota es:", menor)
else: 
    print ("No hay notas, por lo que hay:")
    
print (suspenso ,"suspensos")
print (aprobado ,"aprobados")
print (notable ,"notables")
print (sobresaliente ,"sobresalientes")