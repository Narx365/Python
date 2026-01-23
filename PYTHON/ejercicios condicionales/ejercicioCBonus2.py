lad1=int(input("dime un lado del triangulo: "))
lad2=int(input("dime otro lado del triangulo: "))
lad3=int(input("dime el ultimo lado del triangulo: "))
if (lad1<=0 or lad2<=0 or lad3<=0):
    print("los datos introducidos son incorrectos")
else:
    if (lad1==lad2 and lad2==lad3) :
        print("el triangulo es equilatero")
    elif (lad1==lad2 or lad2==lad3 or lad3==lad1):
        print("el triangulo es isosceles")
    elif (lad1!=lad2 and lad2!=lad3 and lad3!=lad1):
        print("el triangulo es escaleno")
    else:
        print("los datos estan mal introducidos")