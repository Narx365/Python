def es_primo(n):
        if n <= 1:
                return False
        for i in range(2, n):
               if n % i == 0:
                      return False
        return True

num = int(input("Ingrese un número entero y le diré si es primo: "))
print(es_primo(num))