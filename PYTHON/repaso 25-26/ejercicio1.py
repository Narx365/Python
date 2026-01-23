def factorial(n):
    val = 1
    for i in range(1, num + 1):
        val *= i
    return val



num = int(input("dame un numero entero y te diré su factorial: "))
print(factorial(num))