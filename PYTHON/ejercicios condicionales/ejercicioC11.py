año=int(input("dime un año: "))
if(año%4==0 and año%100!=0):
    print(año, " es bisiesto porque es multiplo de 4 sin ser multiplo de 100")
elif (año%4==0 and año%400==0):
    print(año, "es bisiesto porque es multiplo de 4 y de 400")
else:
    print(año, "no es bisiesto")