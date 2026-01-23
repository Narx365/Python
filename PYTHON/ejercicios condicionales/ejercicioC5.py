num1=int(input("dame la nota del primer examen: "))
num2=int(input("dame la nota del segundo examen: "))
if (num1>=5 and num2>=5) :
    print("tu nota media es " ,(num1+num2)/2)
else:
    print("al menos uno de tus examenes está suspendido, por lo que no se puede mediar y suspendes")