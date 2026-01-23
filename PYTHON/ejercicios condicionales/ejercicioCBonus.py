num1=int(input("Dame un numero: "))
num2=int(input("Dame otro numero: "))
oper=input("que operación quieres completar? no uses espacios, solo (+), (-), (/), o (*). ")
if (oper=="+") :
    print("la suma es " ,num1+num2)
elif (oper=="-"):
    print("la resta es " ,num1-num2)
elif (oper=="*"):
    print("la multiplicación es " ,num1*num2)
elif (oper=="/"):
    print("la división es " ,num1/num2)
else:
    print("andate a la mrda, por pndejo")