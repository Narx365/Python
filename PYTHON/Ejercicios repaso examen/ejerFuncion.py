def operación(num1, num2, operando):
    if operando == "+":
        return num1+num2
    elif operando == "-":
        return num1-num2
    else:
        return "no se conoce el operando"
    
resultado = operación(5, 4, "+")
print(resultado)
    
resultado = operación(10, 12, "-")
print(resultado)

num1 = float(input("dame un primer num: "))
num2 = float(input("dame un segundo num: "))
operando = str(input("dame uno de estos operadores (+, -): "))
print(operación(num1, num2, operando))