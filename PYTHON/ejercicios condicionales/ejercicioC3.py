num1=float(input("dame un numero: "))
num2=float(input("dame otro numero: "))
if (num1>num2) :
    print(num1, " + " ,num2, " = " ,num1+num2)
    print(num1, " - " ,num2, " = " ,num1-num2)
elif (num1<num2) :
    if (num2 != 0) :
        print(num1, " * " ,num2, " = " ,num1*num2)
        print(num1, " / " ,num2, " = " ,num1/num2)
    else: 
        print("esto es una incongruencia, vuelve a integrar tus numeros")
else:
    print("pndejo d mierda, los dos numeros son iguales, andate a la mrda")
    