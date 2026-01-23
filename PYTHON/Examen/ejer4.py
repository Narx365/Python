#en la primera linea de codigo establecemos la variable par a 0, pues la usaremos mas tarde
par=int(0)
#lo siguiente es establecer un loop de 8 outputs (1-9)
for x in range(1,9):
    #en esta linea siguiente pedimos el input del usuario
    ent=int(input("dame un numero entero: "))
    #en el if que sigue, comrobamos si el numero es par o impar y gestionamos en cuestion
    if (ent%2==0):
        #esta linea hace la suma de los numeros pares
        par=par+ent
        #estas dos lineas dan el output de los numeros pares
        print ("el numero ",ent," es par")
        print ("la suma total de los pares es " ,par)
    else:
        #estas dos lineas dan el output de los numeros impares
        print ("el numero ",ent," es impar")
        print ("la suma total de los pares es " ,par)
