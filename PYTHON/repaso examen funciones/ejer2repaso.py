def esPrimo(num):
    trueFalse = 0
    for i in range(2, num):
        if num % i == 0:
            trueFalse= trueFalse+1
    if trueFalse>0:
        return "no es primo"
    else:
        return "es primo"


num = int(input("dame un numero y re diré si es primo o no: "))
print(esPrimo(num))