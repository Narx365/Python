num1=int(input("dame un numero: "))
num2=int(input("dame Otro numero: "))
num3=int(input("dame un tercer numero: "))
if (num1>=num2 and num1>=num3) :
    print("el mayor numero es " ,num1)
elif (num2>=num1 and num2>=num3) :
    print("el mayor numero es " ,num2)
elif (num3>=num1 and num3>=num2) :
    print("el mayor numero es " ,num3)
else:
    print("ha habido algun error")