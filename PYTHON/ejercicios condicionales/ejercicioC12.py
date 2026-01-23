form=input("quieres calcular el area de un triangulo o de un circulo?  (t o T son triangulo, c o C son circulo) ")
if (form=="c" or form=="C") :
    Radio=int(input("Dime el radio: "))
    print("el area del circulo es "  ,(Radio*Radio)*3.14)
elif (form=="t" or form=="T"):
    Base=int(input("dime la base del triangulo: "))
    altura=int(input("dime la altura del triangulo: "))
    print("el area del triangulo es " ,(Base*altura)/2)
else :
    print("operación incorrecta")