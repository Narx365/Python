#aquí se pide el input al usuario, como en el ejercicio no se especifica si es entero o no, he puesto float, permitiendo todas las posibilidades.
ent1=float(input("dame un numero del 1 al 10: "))

#esta linea revisa que el numero pedido está entre el 1 y el 10 ambos inclusive
if (ent1<=10 and ent1>=1):
    #en este for se comienza a calcular la tabla de multiplicar, loopeando el print interno
    for x in range(0, 10):
        #este print da primero los valores que se estan multiplicando de forma que se vean agradables en el output, y despues da la solución 
        print(ent1, " * " ,x+1, " = " ,ent1*(x+1))
#esta linea da un agradable mensaje de output en caso de que el numero no esté entre el 1 y el 10 ambos inclusive
else:
    print("el numero no está entre 1 y 10")