ent = int(input("ingrese la cantidad de puntos a procesar: "))
c1 = c2 = c3 = c4 = 0

for i in range(n):
    print ("punto: ")
    x = float(input("ingrese x: "))
    y = float(input("ingrese y: "))

    if x > 0 and y > 0:
        c1 += 1
    elif x < 0 and y >0:
        c2 += 1
    elif x<0 and y>0:
        c3 += 1
    elif x >0 and y<0:
        c4 += 1
    else:
        break
